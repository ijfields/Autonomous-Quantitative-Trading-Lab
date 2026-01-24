"""
Static Code Validator & Auto-Fixer
===================================
Medallion-grade deterministic validation.
Scans AI-generated strategy code for common errors and auto-corrects them.

This runs BEFORE the Reviewer Agent to catch obvious issues that LLMs
consistently fail to fix via prompting.
"""

import re
import ast
import logging
from typing import Tuple, List
from dataclasses import dataclass

logger = logging.getLogger("CodeValidator")

# --- FORBIDDEN PATTERNS ---
# These are common AI hallucinations that will cause silent failures

FORBIDDEN_DATA_COLUMNS = [
    "FundingRate",
    "OpenInterest",
    "OrderBook",
    "Bid",
    "Ask",
    "Spread",
    "Depth",
]

# --- BANNED DATA PATTERNS ---
# These patterns indicate the strategy requires data we don't have (only OHLCV available)
# If any match, the strategy should be rejected before wasting backtest resources
BANNED_DATA_PATTERNS = [
    # Order book / Level 2 data
    (r'\border[_\s]?book\b', 'Order Book data'),
    (r'\bbid[_\s]?ask\b', 'Bid/Ask data'),
    (r'\bbid\b(?!.*irectional)', 'Bid price'),  # Negative lookahead to allow "bidirectional"
    (r'\bask\b(?!.*ed)', 'Ask price'),  # Negative lookahead to allow "asked"
    (r'\bspread\b', 'Bid/Ask Spread'),
    (r'\bdepth\b', 'Market Depth'),
    (r'\blevel[_\s]?2\b', 'Level 2 data'),
    
    # Crypto-specific unavailable data
    (r'\bfunding[_\s]?rate\b', 'Funding Rate'),
    (r'\bopen[_\s]?interest\b', 'Open Interest'),
    (r'\bliquidation', 'Liquidation data'),
    (r'\bperp(?:etual)?\b', 'Perpetual/Futures specific'),
    
    # On-chain / blockchain data
    (r'\bon[_\s]?chain\b', 'On-chain data'),
    (r'\bwallet\b', 'Wallet data'),
    (r'\bwhale\b', 'Whale tracking'),
    (r'\bgas[_\s]?price\b', 'Gas price'),
    (r'\bblock(?:chain)?\b', 'Blockchain data'),
    
    # Sentiment / alternative data
    (r'\bsentiment\b', 'Sentiment data'),
    (r'\btwitter\b', 'Twitter/Social data'),
    (r'\breddit\b', 'Reddit data'),
    (r'\bnews\b', 'News data'),
    (r'\bfear[_\s]?greed\b', 'Fear & Greed index'),
    (r'\bgoogle[_\s]?trends\b', 'Google Trends'),
    
    # Multi-exchange / arbitrage
    (r'\barbitrage\b', 'Arbitrage (multi-exchange)'),
    (r'\bcross[_\s]?exchange\b', 'Cross-exchange data'),
]


# Wrong: ta.momentum.rsi → Right: ta.rsi
TA_SUBMODULE_FIXES = {
    r"ta\.momentum\.(\w+)": r"ta.\1",      # ta.momentum.rsi → ta.rsi
    r"ta\.volatility\.(\w+)": r"ta.\1",    # ta.volatility.atr → ta.atr
    r"ta\.trend\.(\w+)": r"ta.\1",         # ta.trend.sma → ta.sma
    r"ta\.volume\.(\w+)": r"ta.\1",        # ta.volume.obv → ta.obv
    r"ta\.overlap\.(\w+)": r"ta.\1",       # ta.overlap.ema → ta.ema
}

# Common function name fixes
TA_FUNCTION_FIXES = {
    "ta.momentum": "ta.mom",  # Wrong function name
    "ta.volatility": "ta.atr",  # Module used as function
}


@dataclass
class ValidationResult:
    """Result of code validation."""
    fixed_code: str
    issues_found: List[str]
    is_critical: bool  # If True, code cannot be executed


def validate_and_fix(code: str) -> ValidationResult:
    """
    Main entry point. Validates and auto-fixes common AI code errors.
    
    Returns:
        ValidationResult with fixed code and list of issues found
    """
    issues = []
    fixed_code = code
    is_critical = False
    
    # --- 1. FIX TA SUBMODULE PATHS ---
    for pattern, replacement in TA_SUBMODULE_FIXES.items():
        matches = re.findall(pattern, fixed_code)
        if matches:
            for match in matches:
                issues.append(f"Fixed: ta.submodule.{match} → ta.{match}")
            fixed_code = re.sub(pattern, replacement, fixed_code)
    
    # --- 2. FIX WRONG FUNCTION NAMES ---
    for wrong, right in TA_FUNCTION_FIXES.items():
        if wrong in fixed_code:
            issues.append(f"Fixed: {wrong} → {right}")
            fixed_code = fixed_code.replace(wrong, right)
    
    # --- 3. CHECK FOR FORBIDDEN DATA COLUMNS ---
    for col in FORBIDDEN_DATA_COLUMNS:
        pattern = rf"self\.data\.{col}"
        if re.search(pattern, fixed_code, re.IGNORECASE):
            issues.append(f"CRITICAL: Strategy uses self.data.{col} which doesn't exist in OHLCV data")
            is_critical = True
            # We can't auto-fix this, needs AI rewrite
    
    # --- 3b. CHECK FOR BANNED DATA PATTERNS (UNAVAILABLE DATA) ---
    # Scan the full code for references to data types we don't have
    for pattern, data_type in BANNED_DATA_PATTERNS:
        if re.search(pattern, fixed_code, re.IGNORECASE):
            issues.append(f"CRITICAL: Strategy requires {data_type} - we only have OHLCV data")
            is_critical = True

    # This requires parsing the code to find self.I() calls and their arguments.
    # For simplicity and to avoid full AST parsing for this specific check,
    # we'll use regex to find lines that contain both 'self.I' and 'self.data.'
    # This might have false positives but is a quick check.
    
    # Split code into lines to check for specific line issues
    code_lines = fixed_code.splitlines()
    for line_num, line in enumerate(code_lines):
        if "self.I" in line and "self.data." in line:
            # Heuristic: if self.I is called and self.data. is in the same line,
            # it's likely an issue. This is a simplification.
            issues.append(f"CRITICAL: Do NOT use `self.data.Close` inside `self.I()`. Use `self.close_s` (Pandas Series) instead. Line: {line.strip()}")
            is_critical = True # Mark as critical as it's a common source of errors
    
    # --- 5. CHECK FOR LAMBDA IN self.I() ---
    # Pattern: self.I(lambda ...
    # Lambda functions inside self.I() ALWAYS crash because backtesting.py can't handle them
    lambda_pattern = r"self\.I\s*\(\s*lambda"
    if re.search(lambda_pattern, fixed_code):
        issues.append("CRITICAL: Lambda functions inside self.I() are FORBIDDEN - they crash backtesting.py. Use a named pandas_ta function instead.")
        is_critical = True
    
    # --- 6. CHECK ENTRY LOGIC EXISTS ---
    has_entry_long = "entry_long" in fixed_code or "self.buy" in fixed_code
    has_entry_short = "entry_short" in fixed_code or "self.sell" in fixed_code
    
    if not has_entry_long and not has_entry_short:
        issues.append("CRITICAL: No entry logic found (missing entry_long/entry_short/buy/sell)")
        is_critical = True
    
    # --- 6. DETECT ABSOLUTE THRESHOLDS (CRYPTO BUG) ---
    # Pattern: > 0.0001 or < 0.001 (absolute values that never trigger on BTC=$95k)
    abs_threshold_pattern = r"[<>]\s*(0\.0{2,}\d+)"  # Matches > 0.0001, < 0.00001, etc.
    abs_matches = re.findall(abs_threshold_pattern, fixed_code)
    if abs_matches:
        issues.append(f"WARNING: Found absolute thresholds {abs_matches}. These likely NEVER TRIGGER on crypto. Use PERCENTAGE thresholds instead (e.g., change_pct > 0.005 for 0.5%).")
    
    # --- 7. CHECK FOR POSITION.ENTRY_PRICE (VERSION MISMATCH) ---
    if "self.position.entry_price" in fixed_code:
        issues.append("CRITICAL: `self.position.entry_price` does not exist in this library version. Use manual tracking or `self.data.Close[-1]`.")
        is_critical = True
    
    # --- 8. CHECK FOR VOLUME-BASED INDICATORS (FOREX ISSUE) ---
    # Volume indicators return None on Forex/some crypto data
    volume_patterns = [
        (r"ta\.obv", "OBV (On Balance Volume)"),
        (r"ta\.vwap", "VWAP"),
        (r"ta\.mfi", "MFI (Money Flow Index)"),
        (r"ta\.adosc", "ADOSC (Chaikin)"),
        (r"ta\.sma.*[Vv]olume", "SMA on Volume"),
        (r"ta\.ema.*[Vv]olume", "EMA on Volume"),
        (r"self\.data\.Volume", "Direct Volume access"),
        (r"self\.volume", "Volume variable"),
        (r"sma\(V", "SMA(V) - Volume SMA"),  # Catches sma(V,20) pattern
    ]
    
    for pattern, indicator_name in volume_patterns:
        if re.search(pattern, fixed_code, re.IGNORECASE):
            issues.append(f"WARNING: Strategy uses {indicator_name} - this will FAIL on Forex (no volume data) and may crash on some crypto.")
    
    # --- 6. VERIFY PYTHON SYNTAX ---
    try:
        ast.parse(fixed_code)
    except SyntaxError as e:
        issues.append(f"CRITICAL: Python SyntaxError - {e}")
        is_critical = True
    
    if issues:
        logger.info(f"Validator found {len(issues)} issues: {issues}")
    
    return ValidationResult(
        fixed_code=fixed_code,
        issues_found=issues,
        is_critical=is_critical
    )


def extract_error_context(stderr: str, trades: int) -> str:
    """
    Extracts a concise error message for feedback to the Reviewer Agent.
    Filters out useless noise like tqdm progress bars.
    """
    # Filter out tqdm noise (progress bars)
    stderr = re.sub(r"Backtest\.run:.*?\[.*?\]", "", stderr)
    stderr = re.sub(r"\d+%\|[█▌▉▊▋▍▎░ ]+\|", "", stderr)
    stderr = stderr.strip()
    
    if trades == 0:
        base_msg = "CRITICAL: Strategy executed but made 0 trades. "
    else:
        base_msg = ""
    
    # Look for common error patterns
    if "AttributeError" in stderr:
        match = re.search(r"AttributeError: ([^\n]+)", stderr)
        if match:
            return base_msg + f"AttributeError: {match.group(1)}. Check indicator function names."
    
    if "TypeError" in stderr:
        match = re.search(r"TypeError: ([^\n]+)", stderr)
        if match:
            return base_msg + f"TypeError: {match.group(1)}. Check function arguments."
    
    if "KeyError" in stderr:
        match = re.search(r"KeyError: ([^\n]+)", stderr)
        if match:
            return base_msg + f"Missing data column: {match.group(1)}. Use only Open/High/Low/Close/Volume."
    
    # Generic fallback for 0 trades
    if trades == 0:
        return (
            "Strategy ran without errors but made 0 trades. "
            "YOUR ENTRY CONDITIONS ARE TOO STRICT. "
            "LOOSEN THE THRESHOLDS (e.g., change RSI > 80 to RSI > 60). "
            "ENSURE self.entry_long() or self.entry_short() IS CALLED."
        )
    
    # Generic error with truncated output
    if stderr.strip():
        return base_msg + f"Execution error: {stderr[:150]}"
    
    return ""
