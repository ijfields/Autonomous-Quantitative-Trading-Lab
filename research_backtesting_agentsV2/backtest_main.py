import asyncio
import os
import sys
import logging
import time
import random
from pathlib import Path
from dotenv import load_dotenv
from colorama import Fore, Style, init as colorama_init

# Initialize colorama for cross-platform color support
colorama_init(autoreset=True)

from src.common.database import init_db, get_session
from src.common.models import Strategy, StrategyStatus, BacktestResult, StrategyResult
from src.common.key_manager import KeyManager

# Backtest Components
from src.backtest.agents.coder_agent import (
    coder_agent, 
    rotate_coder_key, 
    CoderDeps, 
    CODER_SYSTEM_PROMPT, 
    parse_code_response
)
from src.backtest.agents.reviewer_agent import (
    reviewer_agent,
    ReviewerDeps,
    REVIEWER_SYSTEM_PROMPT,
    rotate_reviewer_key
)
from src.backtest.engine.executor import backtest_executor
from src.backtest.validators.code_validator import validate_and_fix, extract_error_context
from src.backtest.optimizer.optuna_optimizer import optimize_strategy, inject_parameters
from src.backtest.data.loader import DataLoader

# --- CONFIGURATION ---
TEST_UNIVERSE = [
    {"symbol": "SPY", "type": "stock"},
    {"symbol": "QQQ", "type": "stock"},  # Added back - indexes work well
    {"symbol": "BTC/USDT", "type": "crypto"},
    {"symbol": "ETH/USDT", "type": "crypto"},
    # Forex removed - no reliable volume data
]

import argparse

# --- ARGUMENT PARSING ---
parser = argparse.ArgumentParser()
parser.add_argument('--instance-id', type=int, default=1, help='Unique instance ID for this agent')
args = parser.parse_args()
INSTANCE_ID = args.instance_id

load_dotenv()
log_dir = Path("logs")
log_dir.mkdir(exist_ok=True)

# Instance-specific log file
log_file = log_dir / f"backtest_agent_{INSTANCE_ID}_ops.log"

logging.basicConfig(
    level=logging.INFO,
    format=f'%(asctime)s | [Agent {INSTANCE_ID}] | %(levelname)s | %(message)s',
    datefmt='%H:%M:%S',
    handlers=[
        logging.FileHandler(log_file, mode='w'),  # Clear on each run
        logging.StreamHandler(sys.stdout)
    ]
)
# Silence noise
for lib in ["httpx", "pydantic_ai", "httpcore", "docling"]:
    logging.getLogger(lib).setLevel(logging.WARNING)

logger = logging.getLogger(f"BacktestAgent-{INSTANCE_ID}")

# --- INITIALIZE KEY MANAGER ---
try:
    # Uses BACKTEST_KEYS from .env
    key_manager = KeyManager("BACKTEST")
    logger.info(f"🔑 Backtest Key Manager loaded with {len(key_manager.keys)} keys.")
except Exception as e:
    logger.critical(f"Key Manager Error: {e}")
    sys.exit(1)


def extract_error_context(logs: str, trades: int) -> str:
    """
    Parses logs to find why strategy failed or made 0 trades.
    """
    if trades == 0:
        return "Strategy ran without errors but made 0 trades. YOUR ENTRY CONDITIONS ARE TOO STRICT. LOOSEN THE THRESHOLDS (e.g., change RSI > 80 to RSI > 60). ENSURE self.entry_long() or self.entry_short() IS CALLED."
    
    # Simple log extraction (last 5 lines)
    if logs:
        return "\n".join(logs.splitlines()[-10:])
    return "Unknown execution error."

async def process_strategy(strategy: Strategy, session):
    """
    The Core Pipeline: Code -> Validate -> Review -> Execute -> Retry
    Medallion-grade: Static validation + AI feedback loop.
    """
    logger.info(f"⚙️ Processing Strategy ID {strategy.id}: '{strategy.name}'")
    
    MAX_RETRIES = 3
    
    # 1. GENERATE CODE
    # ----------------
    deps = CoderDeps(strategy=strategy)
    user_msg = f"Implement strategy: {strategy.name}. Logic: {strategy.logic_steps}"
    full_prompt = f"{CODER_SYSTEM_PROMPT}\n\nUSER REQUEST:\n{user_msg}\n\nReturn strictly JSON:"
    
    generated_code = None
    
    for attempt in range(3):
        try:
            current_key = key_manager.get_next_key()
            key_idx = key_manager.keys.index(current_key)
            rotate_coder_key(key_idx)
            
            result = await coder_agent.run(full_prompt, deps=deps)
            
            raw_text = ""
            if hasattr(result, 'data'): raw_text = str(result.data)
            elif hasattr(result, 'output'): raw_text = str(result.output)
            else: raw_text = str(result)
            
            generated_code = parse_code_response(raw_text)
            logger.info(f"{Fore.GREEN}✅ Code Generated Successfully.{Style.RESET_ALL}")
            break
            
        except Exception as e:
            err_str = str(e).lower()
            if "429" in str(e) or "quota" in err_str or "503" in str(e):
                logger.warning(f"⚠️ Coder Rate Limit. Rotating key...")
                key_manager.flag_key_limited()
                await asyncio.sleep(5)
            elif "parse" in err_str or "json" in err_str or "validation" in err_str:
                # Parse/Validation failure - retry with same key
                logger.warning(f"⚠️ Coder Parse Failure (Attempt {attempt+1}/3): {e}")
                await asyncio.sleep(2)
                # Continue to next attempt
            else:
                logger.error(f"❌ Coder Error (Attempt {attempt+1}/3): {e}")
                if attempt < 2:
                    await asyncio.sleep(2)
                    # Try again
                else:
                    break  # Give up after all retries
    
    if not generated_code:
        logger.error(f"{Fore.RED}❌ Failed to generate code. Marking FAILED.{Style.RESET_ALL}")
        strategy.status = StrategyStatus.FAILED
        session.add(strategy)
        await session.commit()
        return

    # 2. STATIC VALIDATION (DETERMINISTIC FIX)
    # ----------------------------------------
    logger.info("🔍 Static Validator: Scanning code...")
    
    # Build full code string from generated_code object
    full_code_str = f"{generated_code.class_parameters}\n{generated_code.init_indicators}\n{generated_code.next_logic}"
    
    validation_result = validate_and_fix(full_code_str)
    
    if validation_result.issues_found:
        logger.info(f"🔧 Validator found {len(validation_result.issues_found)} issues: {validation_result.issues_found}")
    
    # CRITICAL: Skip broken strategies immediately
    # CRITICAL: We DO NOT skip immediately anymore. We let the Reviewer Agent try to fix it.
    if validation_result.is_critical:
        logger.warning(f"⛔ CRITICAL validation failure detected. Passing to Reviewer to fix.")
        # strategy.status = StrategyStatus.FAILED # REMOVED
        # session.add(strategy)
        # await session.commit()
        # return
    
    # 3. REVIEW & POLISH + EXECUTION + RETRY LOOP
    # --------------------------------------------
    # We use the FIRST symbol and FIRST timeframe for the refinement loop.
    primary_symbol = strategy.symbols[0] if strategy.symbols else "BTC/USDT"
    primary_timeframe = strategy.timeframes[0] if strategy.timeframes else "1h"
    
    logger.info(f"🎯 Using Primary Symbol '{primary_symbol}' and Timeframe '{primary_timeframe}' for code refinement.")
    
    # Initialize feedback_msg with validator issues
    feedback_msg = ""
    if validation_result.issues_found:
        feedback_msg = "Static Validator Issues: " + "; ".join(validation_result.issues_found)
    
    final_code_stable = False
    
    for retry in range(MAX_RETRIES):
        # 3a. Reviewer Agent
        # Run Reviewer ONLY if we have feedback (error/issues) OR it's a retry.
        should_review = (retry > 0) or (feedback_msg != "")
        
        if should_review:
            logger.info(f"🧐 Reviewer Agent: Pass {retry + 1}/{MAX_RETRIES}...")
            try:
                rev_deps = ReviewerDeps(strategy=strategy, original_code=generated_code)
                
                code_json = generated_code.model_dump_json()
                
                # Include feedback
                if feedback_msg:
                    rev_prompt = f"{REVIEWER_SYSTEM_PROMPT}\n\n[PREVIOUS EXECUTION FEEDBACK]:\n{feedback_msg}\n\n[ORIGINAL CODE JSON]:\n{code_json}\n\n[STRATEGY DESC]:\n{strategy.description}\n\nFix the issues and return strictly JSON:"
                else:
                    rev_prompt = f"{REVIEWER_SYSTEM_PROMPT}\n\n[ORIGINAL CODE JSON]:\n{code_json}\n\n[STRATEGY DESC]:\n{strategy.description}\n\nReturn strictly JSON:"
                
                current_key = key_manager.get_next_key()
                key_idx = key_manager.keys.index(current_key)
                rotate_reviewer_key(key_idx)
                
                rev_result = await reviewer_agent.run(rev_prompt, deps=rev_deps)
                
                rev_text = ""
                if hasattr(rev_result, 'data'): rev_text = str(rev_result.data)
                elif hasattr(rev_result, 'output'): rev_text = str(rev_result.output)
                else: rev_text = str(rev_result)
                
                generated_code = parse_code_response(rev_text)
                logger.info("✨ Code Polished Successfully.")
                
            except Exception as e:
                logger.error(f"⚠️ Reviewer Failed: {e}")
                # Continue with existing code to see if it works anyway
        
        # 3b. Execute Backtest (Test Run on Primary)
        exec_result = await backtest_executor.run_backtest(
            strategy_id=strategy.id,
            code=generated_code,
            symbol=primary_symbol,
            timeframe=primary_timeframe,
            asset_type=strategy.asset_type
        )
        
        # 3c. Check Result
        trades = exec_result.get("trades", 0)
        logs = exec_result.get("logs", "")
        error_msg = exec_result.get("error", "")
        
        if trades > 0:
            logger.info(f"{Fore.GREEN}✅ Strategy executed on {primary_symbol} ({primary_timeframe}) with {trades} trades!{Style.RESET_ALL}")
            final_code_stable = True
            break  # Success!
        elif error_msg:
            # IT CRASHED
            feedback_msg = f"Runtime Error or Syntax Error:\n{error_msg}\nLogs:\n{logs[-1000:]}"
            logger.error(f"❌ Execution Failed on attempt {retry + 1}. Feedback: {feedback_msg}")
        else:
            # 0 TRADES (Logic Issue)
            feedback_msg = extract_error_context(logs or error_msg or "", trades)
            logger.warning(f"⚠️ 0 trades on attempt {retry + 1}. Feedback: {feedback_msg}")
            
        if retry == MAX_RETRIES - 1:
            logger.error(f"{Fore.RED}❌ Max retries reached. Strategy failed to produce trades on {primary_symbol} ({primary_timeframe}).{Style.RESET_ALL}")
    
    # 4. FINAL EXECUTION ON ALL SYMBOLS AND TIMEFRAMES
    # ------------------------------------------------
    # Use the explicitly defined Test Universe instead of strategy.symbols
    timeframes_to_test = strategy.timeframes if strategy.timeframes else ["1h"]
    
    logger.info(f"🌏 Running full backtest suite on Universe: {len(TEST_UNIVERSE)} assets, Timeframes={timeframes_to_test}")
    
    final_code_str = f"{generated_code.class_parameters}\n{generated_code.init_indicators}\n{generated_code.next_logic}"
    
    for asset_config in TEST_UNIVERSE:
        sym = asset_config["symbol"]
        run_asset_type = asset_config["type"]

        for tf in timeframes_to_test:
            logger.info(f"👉 Testing Symbol: {sym} | Timeframe: {tf} | Type: {run_asset_type}")
            
            # Run Backtest
            sym_result = await backtest_executor.run_backtest(
                strategy_id=strategy.id,
                code=generated_code,
                symbol=sym,
                timeframe=tf,
                asset_type=run_asset_type
            )
            
            # Optimization (Only if it traded)
            optimization_result = None
            if sym_result.get("trades", 0) > 0:
                logger.info(f"🔬 Starting Optimization for {sym} ({tf})...")
                try:
                    optimization_result = await optimize_strategy(
                        strategy_id=strategy.id,
                        class_parameters=generated_code.class_parameters,
                        init_indicators=generated_code.init_indicators,
                        next_logic=generated_code.next_logic,
                        symbol=sym,
                        timeframe=tf,
                        asset_type=strategy.asset_type,
                        n_trials=20, # Reduced trials for speed since we test many combos
                        timeout=200
                    )
                except Exception as e:
                    logger.error(f"⚠️ Optimization failed for {sym} ({tf}): {e}")

            # Verification Run (if optimized)
            if optimization_result and optimization_result.best_sharpe > 1.0:
                logger.info(f"🔄 Verify: Re-running backtest with optimized params...")
                try:
                    # Determine split date again for verification (Out-of-Sample)
                    verify_start_date = None
                    try:
                        loader = DataLoader()
                        # Use same logic as optimizer (default 365 days)
                        full_data = await asyncio.to_thread(loader.fetch_data, sym, tf, run_asset_type)
                        if not full_data.empty and len(full_data) > 100:
                            split_idx = int(len(full_data) * 0.7)
                            # Start verification from the split point (testing set)
                            verify_start_date = full_data.index[split_idx].strftime("%Y-%m-%d")
                            logger.info(f"🧪 Independent Verification on Test Set (Start: {verify_start_date})")
                    except Exception as e:
                        logger.warning(f"Failed to calculate verification split: {e}")

                    # Inject params
                    optimized_class_params = inject_parameters(
                        generated_code.class_parameters, 
                        optimization_result.best_params
                    )
                     # Update code (in memory object)
                    generated_code.class_parameters = optimized_class_params
                    
                    # Update final string for DB
                    final_code_str = f"{generated_code.class_parameters}\n{generated_code.init_indicators}\n{generated_code.next_logic}"
                    
                    # Re-Run
                    sym_result = await backtest_executor.run_backtest(
                        strategy_id=strategy.id,
                        code=generated_code,
                        symbol=sym,
                        timeframe=tf,
                        asset_type=run_asset_type,
                        start_date=verify_start_date
                    )
                    logger.info(f"✅ Verified Stats: Return={sym_result.get('return_pct')}% Sharpe={sym_result.get('sharpe')}")
                    
                except Exception as e:
                    logger.error(f"⚠️ Verification Failed: {e}")

            # Determine Rating using Multi-Ratio Alpha Detection
            rating = StrategyResult.PENDING
            final_return = sym_result.get("return_pct", 0) or 0
            final_sharpe = sym_result.get("sharpe", 0) or 0
            final_sortino = sym_result.get("sortino", 0) or 0
            buy_hold = sym_result.get("buy_hold_pct", 0) or 0
            max_dd = abs(sym_result.get("max_drawdown", 0) or 0)
            final_trades = sym_result.get("trades", 0)
            
            # Calculate Calmar Ratio: Annualized Return / |Max Drawdown|
            # Standard formula: (Daily Return * 365) / Max DD
            backtest_days = sym_result.get("backtest_period_days", 365) or 365
            daily_ret = final_return / backtest_days if backtest_days > 0 else 0
            annualized_ret = daily_ret * 365  # Annualize the daily return
            calmar = (annualized_ret / max_dd) if max_dd > 0 else 0
            
            # 1. CRASHED: Error or no trades
            if sym_result.get("error") or final_trades == 0:
                rating = StrategyResult.CRASHED
            # 2. UNPROFITABLE: Negative return
            elif final_return <= 0:
                rating = StrategyResult.UNPROFITABLE
            else:
                # Positive return - check for alpha
                # Alpha Criteria: Need 2+ of these 4 to be PROFITABLE
                alpha_checks = [
                    final_sharpe >= 1.0,      # Good risk-adjusted return
                    final_sortino >= 1.5,     # Good downside risk management
                    calmar >= 1.0,            # Good drawdown recovery (annualized)
                    final_return > buy_hold,  # Beats passive strategy
                ]
                alpha_score = sum(alpha_checks)
                
                # Additional safety checks
                has_significance = final_trades >= 5
                has_safe_dd = max_dd <= 50
                
                if alpha_score >= 2 and has_significance and has_safe_dd:
                    rating = StrategyResult.PROFITABLE
                else:
                    rating = StrategyResult.MARGINAL
            
            logger.debug(f"📊 Rating: {rating.value} | Return={final_return:.2f}% Sharpe={final_sharpe:.2f} Sortino={final_sortino:.2f} Calmar={calmar:.3f} vs B&H={buy_hold:.2f}%")

            params_log = {
                "symbol": sym, 
                "timeframe": tf,
                "retries_used": retry + 1 if final_code_stable else MAX_RETRIES
            }
            
            # Calculate duration metrics
            backtest_days = sym_result.get("backtest_period_days", 0)
            total_return = sym_result.get("return_pct", 0.0)
            
            # Safely calculate derived metrics
            daily_return = (total_return / backtest_days) if backtest_days > 0 else 0.0
            weekly_return = (total_return / (backtest_days / 7)) if backtest_days > 7 else 0.0
            annualized_return = (total_return * (365 / backtest_days)) if backtest_days > 0 else 0.0

            # Create Result Record
            bt_record = BacktestResult(
                strategy_id=strategy.id,
                code=final_code_str,
                symbol=sym, # Specific Symbol
                timeframe=tf, # Specific Timeframe
                sharpe_ratio=optimization_result.best_sharpe if optimization_result else sym_result.get("sharpe"),
                sortino_ratio=sym_result.get("sortino"),
                win_rate=sym_result.get("win_rate"),
                total_return_pct=sym_result.get("return_pct"),
                buy_hold_return_pct=sym_result.get("buy_hold_pct"),
                max_drawdown_pct=sym_result.get("max_drawdown"),
                volatility_pct=sym_result.get("volatility"),
                trades_count=sym_result.get("trades"),
                # Duration metrics
                backtest_period_days=backtest_days,
                daily_return_pct=round(daily_return, 4),
                weekly_return_pct=round(weekly_return, 4),
                annualized_return_pct=round(annualized_return, 2),
                execution_log=sym_result.get("logs"),
                error_message=sym_result.get("error"),
                result_rating=rating,
                parameters=params_log,
                is_optimized=bool(optimization_result and optimization_result.trials_run > 0),
                optimized_params=optimization_result.best_params if optimization_result else {},
                optimization_trials=optimization_result.trials_run if optimization_result else 0
            )
            
            # Always save results to DB for analysis
            session.add(bt_record)
            
            # Dynamic logging based on rating
            if rating == StrategyResult.PROFITABLE:
                logger.info(f"✅ Saved PROFITABLE Result for {sym} ({tf}): Return={bt_record.total_return_pct}% Sharpe={bt_record.sharpe_ratio}")
            elif rating == StrategyResult.UNPROFITABLE:
                logger.info(f"📉 Saved UNPROFITABLE Result for {sym} ({tf}): Return={bt_record.total_return_pct}% Sharpe={bt_record.sharpe_ratio}")
            else:
                logger.error(f"❌ Saved CRASHED/FAILED Result for {sym} ({tf}): Error={bt_record.error_message}")

    strategy.status = StrategyStatus.COMPLETED
    session.add(strategy)
    await session.commit()
    logger.info(f"🏁 Strategy {strategy.name} Completed.")


import signal

async def run_backtest_loop():
    logger.info(f"{Fore.CYAN}🚀 BACKTEST FACTORY STARTED{Style.RESET_ALL}")
    
    # Handle SIGTERM (Docker/PM2 stop signal) by converting it to KeyboardInterrupt
    signal.signal(signal.SIGTERM, signal.default_int_handler)
    
    await init_db()
    
    while True:
        processed_count = 0
        
        async for session in get_session():
            strategy = None # Ensure it's defined for cleanup scope
            try:
                # 1. Find Strategies waiting for code
                # We explicitly look for 'READY_FOR_CODE'
                from sqlalchemy import select
                stmt = select(Strategy).where(Strategy.status == StrategyStatus.READY_FOR_CODE).limit(1).with_for_update(skip_locked=True)
                result = await session.execute(stmt)
                strategy = result.scalars().first()
                
                if strategy:
                    # Lock it immediately
                    strategy.status = StrategyStatus.CODING
                    session.add(strategy)
                    await session.commit()
                    
                    # Process
                    await process_strategy(strategy, session)
                    processed_count += 1
                
            except (KeyboardInterrupt, asyncio.CancelledError):
                logger.warning(f"\n{Fore.YELLOW}🛑 Interruption Detected! Cleaning up active strategy...{Style.RESET_ALL}")
                if strategy:
                    logger.info(f"♻️ Rolling back Strategy {strategy.id} to 'READY_FOR_CODE'")
                    strategy.status = StrategyStatus.READY_FOR_CODE
                    session.add(strategy)
                    
                    # Optional: Clean up any partial backtest results if needed
                    # For now, just resetting status ensures it gets picked up again cleanly
                    await session.commit()
                raise # Re-raise to exit the loop
            
            break # Release session
        
        if processed_count == 0:
            logger.info("💤 No strategies ready. Sleeping 5s...")
            await asyncio.sleep(5)
        else:
            # Small cool down between runs
            await asyncio.sleep(5)

if __name__ == "__main__":
    try:
        asyncio.run(run_backtest_loop())
    except KeyboardInterrupt:
        logger.info(f"{Fore.YELLOW}🛑 Backtester Stopped Gracefully.{Style.RESET_ALL}")