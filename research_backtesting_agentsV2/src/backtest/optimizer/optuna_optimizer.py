"""
Optuna Hyperparameter Optimizer
================================
Bayesian optimization for strategy parameters.
Runs up to 30 trials, prunes bad ones early, finds Sharpe > 1.0.
"""

import re
import json
import logging
import optuna
import asyncio
from typing import Dict, Tuple, Optional, Any
from dataclasses import dataclass
from src.backtest.engine.runner import code_runner
from src.backtest.data.loader import DataLoader

logger = logging.getLogger("OptunaOptimizer")

# Suppress Optuna's verbose logging
optuna.logging.set_verbosity(optuna.logging.WARNING)


@dataclass
class OptimizationResult:
    """Result of Optuna optimization."""
    success: bool
    best_params: Dict[str, Any]
    best_sharpe: float
    trials_run: int


# --- KNOWN PARAMETER RANGES (Harvard Patterns) ---
# These are empirically proven ranges for common strategy parameters.
# If a parameter name matches, use these ranges instead of auto-deriving.
KNOWN_PARAM_RANGES: Dict[str, Tuple[str, float, float]] = {
    # Bollinger Bands
    "bb_window": ("int", 10, 50),
    "bb_period": ("int", 10, 50),
    "bb_std": ("float", 1.5, 3.5),
    "num_std": ("float", 1.5, 3.5),
    
    # Keltner Channels
    "keltner_window": ("int", 10, 30),
    "keltner_atr_mult": ("float", 1.0, 2.5),
    
    # ADX
    "adx_period": ("int", 10, 25),
    "adx_threshold": ("int", 20, 35),
    
    # Exit Management (Stock-centric)
    "take_profit": ("percent", 0.01, 0.10),  # 1% to 10%
    "stop_loss": ("percent", 0.01, 0.07),    # 1% to 7%
    "take_profit_pct": ("percent", 0.01, 0.10),
    "stop_loss_pct": ("percent", 0.01, 0.07),
    
    # General Periods
    "atr_period": ("int", 7, 50),
    "rsi_period": ("int", 7, 25),
    "sma_period": ("int", 10, 100),
    "ema_period": ("int", 10, 100),
    
    # Multipliers
    "atr_multiplier": ("float", 0.5, 4.0),
}

# --- CRYPTO-SPECIFIC PARAMETER RANGES ---
# Crypto has 3-5x higher volatility than stocks, requiring wider ranges.
# This fixes the 100% "No trials completed" issue on BTC/ETH.
KNOWN_PARAM_RANGES_CRYPTO: Dict[str, Tuple[str, float, float]] = {
    # Exit Management (Crypto needs wider stops due to volatility)
    "take_profit": ("percent", 0.03, 0.25),      # 3% to 25% (vs 1-10% stocks)
    "stop_loss": ("percent", 0.03, 0.15),        # 3% to 15% (vs 1-7% stocks)
    "take_profit_pct": ("percent", 0.03, 0.25),
    "stop_loss_pct": ("percent", 0.03, 0.15),
    
    # ATR Multipliers (Crypto needs bigger buffers)
    "atr_multiplier": ("float", 1.5, 6.0),       # vs 0.5-4.0 for stocks
    "stop_loss_atr_multiplier": ("float", 2.0, 6.0),
    
    # Risk Sizing (Crypto trades need smaller position sizes due to volatility)
    "risk_percentage": ("percent", 0.005, 0.02), # 0.5% to 2% (vs 1-3% stocks)
}


def extract_parameters(
    class_parameters: str, 
    asset_type: str = "stock"
) -> Dict[str, Tuple[str, float, float, float]]:
    """
    Extract tunable parameters from strategy class_parameters code.
    Uses KNOWN_PARAM_RANGES or KNOWN_PARAM_RANGES_CRYPTO based on asset_type.
    
    Args:
        class_parameters: The strategy class parameters code
        asset_type: 'crypto', 'stock', or 'index'
    
    Returns:
        Dict of param_name -> (type, default, min, max)
        type is one of: 'int', 'float', 'percent'
    """
    params = {}
    
    # Pattern: variable_name = number
    pattern = r"(\w+)\s*=\s*([0-9.]+)"
    matches = re.findall(pattern, class_parameters)
    
    for name, value in matches:
        try:
            val = float(value)
        except ValueError:
            continue
        
        # Priority 1: Use asset-specific ranges if available
        # Crypto gets wider ranges due to higher volatility
        if asset_type == "crypto" and name in KNOWN_PARAM_RANGES_CRYPTO:
            known = KNOWN_PARAM_RANGES_CRYPTO[name]
            param_type, known_min, known_max = known
            params[name] = (param_type, val, known_min, known_max)
            logger.debug(f"Using CRYPTO range for {name}: {known_min}-{known_max}")
            continue
        
        # Priority 2: Use general KNOWN_PARAM_RANGES if this param name is known
        if name in KNOWN_PARAM_RANGES:
            known = KNOWN_PARAM_RANGES[name]
            param_type, known_min, known_max = known
            params[name] = (param_type, val, known_min, known_max)
            continue
        
        # Priority 3: Auto-derive ranges from default value
        if val == int(val) and val >= 5:
            # Integer period (like SMA period)
            params[name] = ('int', int(val), max(5, int(val) // 2), int(val) * 3)
        elif 0 < val < 1:
            # Percentage or ratio - wider for crypto
            if asset_type == "crypto":
                params[name] = ('percent', val, val / 2, min(val * 5, 0.5))  # 5x range for crypto
            else:
                params[name] = ('percent', val, val / 2, min(val * 3, 0.5))
        elif val >= 1:
            # Multiplier or threshold
            params[name] = ('float', val, val / 2, val * 2)
        else:
            # Small number, could be anything
            params[name] = ('float', val, val / 2, val * 2)
    
    return params


def inject_parameters(class_parameters: str, params: Dict[str, Any]) -> str:
    """Inject parameter values into class_parameters code."""
    modified_params = class_parameters
    for name, value in params.items():
        # Replace variable = number with variable = new_value
        pattern = rf"({name}\s*=\s*)[0-9.]+"
        modified_params = re.sub(pattern, rf"\g<1>{value}", modified_params)
    return modified_params


async def optimize_strategy(
    strategy_id: int,
    class_parameters: str,
    init_indicators: str,
    next_logic: str,
    asset_type: str = "crypto",
    symbol: str = "BTC/USDT",
    timeframe: str = "1h",
    n_trials: int = 30,
    timeout: int = 300,
    days: int = 365
) -> OptimizationResult:
    """
    Run Optuna optimization on a strategy using TURBO MODE (Internalized Optimization).
    
    Args:
        strategy_id: The strategy ID
        class_parameters: The class_parameters code
        init_indicators: The init_indicators code
        next_logic: The next_logic code
        symbol: Trading pair
        timeframe: Data resolution
        n_trials: Max number of trials (Ignored in Turbo Mode logic, but kept for signature)
        timeout: Max seconds to run
        
    Returns:
        OptimizationResult with best params
    """
    
    # 1. Extract tunable parameters
    tunable_params = extract_parameters(class_parameters, asset_type=asset_type)
    
    if not tunable_params:
        logger.warning("No tunable parameters found in strategy")
        return OptimizationResult(
            success=False,
            best_params={},
            best_sharpe=0.0,
            trials_run=0
        )
    
    logger.info(f"🔬 Optimizing {len(tunable_params)} parameters: {list(tunable_params.keys())}")

    # 2. Determine Train/Test Split (70/30)
    loader = DataLoader()
    try:
        data = await asyncio.to_thread(loader.fetch_data, symbol, timeframe, asset_type, days=days)
    except Exception as e:
        logger.warning(f"Failed to fetch data for split calculation: {e}")
        data = None

    train_end_date = None
    if data is not None and not data.empty:
        # Check for stale data (common cause of Disjoint Window Bug)
        last_date = data.index.max()
        # Use simple naive check: if data ends more than 14 days ago, it's stale
        import pandas as pd
        if last_date < pd.Timestamp.now() - pd.Timedelta(days=14):
             logger.warning(f"⚠️ Optimization Data Stale (Last: {last_date}). Skipping Walk-Forward Split to prevent 'No Data' crash.")
        else:
            n_rows = len(data)
            if n_rows > 100:
                split_idx = int(n_rows * 0.7)
                train_end_date = data.index[split_idx].strftime("%Y-%m-%d")
                logger.info(f"📅 Walk-Forward Split: Training until {train_end_date} ({split_idx}/{n_rows} bars)")
            else:
                logger.warning("Dataset too small for split, using full data for optimization.")
    
    # 3. Run Optimization in Turbo Mode (Internalized)
    try:
        # Create Script with optimize=True
        script_path = await code_runner.create_script(
            strategy_id=strategy_id,
            class_parameters=class_parameters,
            init_indicators=init_indicators,
            next_logic=next_logic,
            symbol=symbol,
            timeframe=timeframe,
            asset_type=asset_type,
            end_date=train_end_date,
            optimize=True,
            tunable_params=tunable_params,
            file_suffix="_turbo_opt"
        )
        
        # Run Subprocess (This runs the whole 30-trial loop internally)
        result = await code_runner.run_subprocess(script_path, timeout=timeout)
        
        if result.get("error"):
             logger.error(f"Optimization Routine Failed: {result.get('error')}")
             logger.error(f"Logs: {result.get('logs')}")
             return OptimizationResult(False, {}, 0.0, 0)
             
        # Result contains {"success": True, "best_params": {...}, "best_sharpe": 1.5, ...}
        best_sharpe = float(result.get("best_sharpe", 0.0))
        best_params = result.get("best_params", {})
        trials_run = result.get("trials_run", 0)
        
        logger.info(f"✨ TURBO OPTIMIZATION COMPLETE: Sharpe={best_sharpe:.2f} | Trials={trials_run}")
        
        return OptimizationResult(
            success=best_sharpe > 1.0,
            best_params=best_params,
            best_sharpe=best_sharpe,
            trials_run=trials_run
        )
        
    except Exception as e:
        logger.error(f"Turbo Optimization Crash: {e}")
        import traceback
        logger.error(traceback.format_exc())
        return OptimizationResult(False, {}, 0.0, 0)
