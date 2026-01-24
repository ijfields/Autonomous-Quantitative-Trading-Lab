import os
import logging
from dataclasses import dataclass
from typing import Optional

from pathlib import Path
from dotenv import load_dotenv
from pydantic_ai import Agent
from pydantic_ai.models.gemini import GeminiModel

from src.common.models import Strategy
from src.backtest.agents.coder_agent import PythonStrategyCode, parse_code_response

# --- CONFIGURATION ---
load_dotenv(Path(__file__).parent.parent.parent.parent / ".env")
logger = logging.getLogger("ReviewerAgent")

# Re-use Coder Keys for now (or a separate env var if preferred)
keys_str = os.getenv("BACKTEST_KEYS", "") or os.getenv("RESEARCH_KEYS", "") or os.getenv("GOOGLE_API_KEYS", "")
API_KEYS = [k.strip() for k in keys_str.split(",") if k.strip()]

if not API_KEYS:
    raise ValueError("CRITICAL: No API Keys available for Reviewer Agent.")

def create_model(api_key: str):
    model_name = os.getenv("MODEL_SMART", "gemma-3-27b-it")
    # Avoid global state mutation for thread safety - but here we must use env var for GeminiModel
    os.environ["GEMINI_API_KEY"] = api_key
    os.environ["GOOGLE_API_KEY"] = api_key
    return GeminiModel(model_name)

current_model = create_model(API_KEYS[0])

# --- DEPENDENCIES ---
@dataclass
class ReviewerDeps:
    strategy: Strategy
    original_code: PythonStrategyCode

# --- PROMPT ---
REVIEWER_SYSTEM_PROMPT = """
ROLE: Senior Python Code Reviewer & QA Engineer (Quant Finance - Crypto/HFT).
TASK: Review and POLISH the provided `backtesting.py` strategy code.

--- CRITICAL VALIDATION CHECKLIST ---
1. **LIBRARIES & HALLUCINATIONS**:
   - ❌ `ta.max`, `ta.min`, `ta.correlation`, `ta.rolling_mean` -> **THESE DO NOT EXIST**.
   - ✅ Check if `pandas_ta` function is valid (sma, ema, rsi, bbands, atr, etc.).
   - If invalid, rewrite using standard Pandas: `self.close_s.rolling(n).max()`.

2. **INDICATOR SAFETY**:
   - ❌ `self.I(ta.atr, ...)` missing high/low args? ATR/ADX need (high, low, close).
   - ❌ `self.I(lambda ...)`? Lambda will crash pickle. REJECT IT.
   - ❌ Dynamic parameters? `length=self.variable` crashes. Must be `length=14`.

3. **NaN & LENGTH SAFETY**:
   - Does `next_logic` check `if len(self.rsi) < X`?
   - Indicators return NaNs at start. If code accesses `self.rsi[-1]` on tick 0 -> CRASH or WRONG.
   - **MANDATE**: `if len(self.data) < 50: return` at start of `next()`.

4. **SYNTAX SAFETY**:
   - `try:` block without `except:`? Syntax Error.
   - `self.entry_long(size=...)`? **INVALID ARGUMENT**. Remove `size`.
   - `self.data.Close.shift()`? **INVALID**. Use `self.data.Close[-2]`.

--- RULES (LOGIC) ---
1. **THRESHOLDS MUST BE PERCENTAGES**:
   - WRONG: `if diff > 100:` (Absolute price)
   - RIGHT: `if diff_pct > 0.01:` (1%)

2. **HANDLING "0 TRADES" FEEDBACK**:
   - If feedback says "0 trades", **LOOSEN CONDITIONS**:
     - RSI > 80 -> RSI > 60
     - Volume > 1M -> Volume > 100k
     - AND -> OR conditions.

--- WORKING EXAMPLE (GOLD STANDARD) ---
```python
# GOOD next_logic:
if len(self.data) < 50: return # Safety check

try:
    change_pct = (self.data.Close[-1] - self.data.Close[-2]) / self.data.Close[-2]
    
    # Check for NaN in indicators
    if np.isnan(self.rsi[-1]): return
    
    # LOOSE Entry logic
    if change_pct > 0.001 and self.rsi[-1] < 70:
        self.entry_long()
    elif change_pct < -0.001 and self.rsi[-1] > 30:
        self.entry_short()
    
    # Simple Exit
    if self.position.is_long and change_pct < -0.005:
        self.exit_all()
except Exception:
    pass
```

--- OUTPUT ---
Return strictly a JSON object with keys: `class_parameters`, `init_indicators`, `next_logic`.
"""

# --- AGENT ---
reviewer_agent = Agent(current_model, deps_type=ReviewerDeps)

def rotate_reviewer_key(index: int):
    new_key = API_KEYS[index % len(API_KEYS)]
    reviewer_agent.model = create_model(new_key)
    logger.info(f"🔄 Reviewer switched to Key #{index % len(API_KEYS)}")
