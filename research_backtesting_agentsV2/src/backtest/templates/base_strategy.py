# CORPORATE BACKTEST TEMPLATE v4 (Production Ready)
# Features: Dynamic Sizing (95% Equity), Robust Data Mapping, Centralized Risk Logic

STRATEGY_TEMPLATE = """
import numpy as np
import pandas as pd
import pandas_ta as ta
from backtesting import Strategy
from backtesting.lib import crossover

# --- MONKEY PATCH: FIX MACD CRASHES ON SHORT DATA ---
# pandas_ta returns None if len(data) < slow_period. 
# Backtesting.py crashes if indicators return None.
# We patch it to return a DataFrame of NaNs instead.
_original_macd = ta.macd
def _safe_macd(close, fast=None, slow=None, signal=None, offset=None, **kwargs):
    # Defaults from pandas_ta
    fast = fast if fast else 12
    slow = slow if slow else 26
    signal = signal if signal else 9
    
    try:
        res = _original_macd(close, fast=fast, slow=slow, signal=signal, offset=offset, **kwargs)
        if res is None or res.empty:
            raise ValueError("Empty MACD result")
        return res
    except Exception:
        # Construct NaN DataFrame matching MACD shape (3 columns)
        l = len(close)
        nan_arr = np.full(l, np.nan)
        return pd.DataFrame({{
            'MACD': nan_arr,
            'Hist': nan_arr,
            'Signal': nan_arr
        }})

ta.macd = _safe_macd
# ----------------------------------------------------

class GeneratedStrategy(Strategy):
    # --- 1. DEFAULT CONFIGURATION (AI overrides these) ---
    stop_loss_pct = 0.02      # 2% Risk fallback
    take_profit_pct = 0.04    # 4% Target fallback
    atr_period = 14           # Volatility Lookback
    atr_multiplier = 1.5      # Stop distance in ATRs
    
    # AI-INJECTED PARAMETERS
    {params}

    def init(self):
        # --- 2. DATA NORMALIZATION ---
        # Convert Backtesting.py arrays to Pandas Series for TA-Lib compatibility
        # This prevents 99% of "Invalid Type" errors
        # IMPORTANT: Slice to [:len(self.data)] to handle backtesting.py's validation runs (50 items)
        self.close_s = pd.Series(self.data.Close[:len(self.data)])
        self.high_s  = pd.Series(self.data.High[:len(self.data)])
        self.low_s   = pd.Series(self.data.Low[:len(self.data)])
        self.open_s  = pd.Series(self.data.Open[:len(self.data)])
        self.vol_s   = pd.Series(self.data.Volume[:len(self.data)])

        # --- 3. CORE RISK INDICATORS ---
        # We always calculate ATR for dynamic risk management
        try:
            self.atr = self.I(ta.atr, self.high_s, self.low_s, self.close_s, self.atr_period)
        except Exception:
            self.atr = None # Graceful fallback if data is too short

        # --- 4. AI INDICATORS ---
        {indicators}

    def next(self):
        # --- 5. SAFETY CHECKS ---
        # Skip the warmup period (wait for indicators to settle)
        if len(self.data) < 50: 
            return

        # --- 6. AI LOGIC ---
        {logic}

    # --- 7. EXECUTION ENGINE (The "Broker") ---
    
    def entry_long(self, size=None, limit=None, stop=None):
        # 1. Check State
        # If we are already long, we don't pile on (unless we want pyramiding, but keeping simple for now)
        if self.position.is_long: return
        if self.position.is_short: self.position.close()
        
        # 2. Calculate Risk
        price = self.data.Close[-1]
        sl, tp = self._calc_stops(price, direction="long")

        # 3. Determine Size (Default 95% equity if not specified)
        # We leave 5% buffer for commissions/slippage to prevent "Insufficient Cash"
        if size is None:
            size = 0.95
            
        # 4. Execute
        self.buy(size=size, sl=sl, tp=tp, limit=limit, stop=stop)

    def entry_short(self, size=None, limit=None, stop=None):
        # 1. Check State
        if self.position.is_short: return
        if self.position.is_long: self.position.close()
        
        # 2. Calculate Risk
        price = self.data.Close[-1]
        sl, tp = self._calc_stops(price, direction="short")

        # 3. Determine Size
        if size is None:
            size = 0.95

        # 4. Execute
        self.sell(size=size, sl=sl, tp=tp, limit=limit, stop=stop)
    
    def exit_all(self):
        if self.position:
            self.position.close()

    def _calc_stops(self, price, direction):
        \"\"\"
        Centralized Risk Logic:
        Prioritizes Volatility (ATR) stops. Falls back to Fixed % if ATR fails.
        \"\"\"
        sl_dist = 0.0
        
        # Method A: Volatility Based (Preferred)
        if self.atr is not None and len(self.atr) > 0 and not np.isnan(self.atr[-1]):
            sl_dist = self.atr[-1] * self.atr_multiplier
        # Method B: Fixed Percentage (Fallback)
        else:
            sl_dist = price * self.stop_loss_pct

        if direction == "long":
            sl = price - sl_dist
            # Default 1:2 Risk/Reward Ratio if not specified
            tp = price + (sl_dist * 2)
        else:
            sl = price + sl_dist
            tp = price - (sl_dist * 2)
            
        return sl, tp
"""