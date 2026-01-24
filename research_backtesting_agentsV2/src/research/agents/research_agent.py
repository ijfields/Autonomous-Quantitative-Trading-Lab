import os
import logging
import json
from dataclasses import dataclass
from typing import List, Optional, Literal, Union
from datetime import datetime

from pydantic import BaseModel, Field
from pydantic_ai import Agent, RunContext
from pydantic_ai.models.gemini import GeminiModel
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from src.common.models import Strategy
from src.research.tools.web_tools import (
    search_general_web, 
    search_academic_papers, 
    search_github_code, 
    read_url_content
)

# --- 1. DEPENDENCIES ---
@dataclass
class ResearchDeps:
    db_session: AsyncSession

# --- 2. DATA MODELS ---
class StrategyAnalysisResult(BaseModel):
    name: str = Field(description="A professional, institutional name.")
    description: str = Field(description="A technical summary.")
    logic_steps: List[str] = Field(description="Strict execution rules tags: [VARIABLES], [DATA], [INDICATOR], [ENTRY LONG], [EXIT LONG], [ENTRY SHORT], [EXIT SHORT], [RISK].")
    tags: List[str] = Field(description="Max 5 tags.")
    best_source_url: Optional[str] = Field(description="URL source.")
    quality_score: int = Field(description="0-10 Score.")
    is_duplicate: bool = Field(description="True if exists in DB.")
    # timeframe: str = Field(description="Optimal resolution: '1m', '5m', '15m', '1h', '4h', '1d'.", default="1h") <-- REMOVED
    
    # --- NEW FIELDS ---
    timeframes: List[str] = Field(description="List of optimal resolutions. E.g. ['5m', '1h']. Default to ['1h'].", default=["1h"])
    symbols: List[str] = Field(description="List of best tickers for this strategy. E.g. ['BTC/USDT', 'ETH/USDT'] or ['SPY', 'QQQ']. Default to ['BTC/USDT'] if unsure.", default=["BTC/USDT"])
    asset_type: Literal["crypto", "stock", "index"] = Field(description="The asset class: crypto, stock, or index (e.g. SPY, QQQ).", default="crypto")


class TopicDiscoveryResult(BaseModel):
    topic: str = Field(description="The specific strategy name found.")
    source_context: str = Field(description="Where it was found.")

# --- 3. COMMAND SCHEMAS ---
class SearchCommand(BaseModel):
    tool: Literal["search_general", "search_academic", "search_github"]
    query: Optional[str] = Field(default=None, description="Single search query (legacy).")
    queries: Optional[List[str]] = Field(default=None, description="List of queries to run in parallel.")
    rationale: str = Field(description="Why this search.")

class ReadCommand(BaseModel):
    tool: Literal["read_content"]
    url: Optional[str] = Field(default=None, description="Single URL to read (legacy).")
    urls: Optional[List[str]] = Field(default=None, description="List of URLs to read in parallel.")
    rationale: str = Field(description="Why read this.")

class FinishSniperCommand(BaseModel):
    tool: Literal["finish_sniper"]
    result: StrategyAnalysisResult

class FinishScoutCommand(BaseModel):
    tool: Literal["finish_scout"]
    result: TopicDiscoveryResult

AgentAction = Union[SearchCommand, ReadCommand, FinishSniperCommand, FinishScoutCommand]

# --- 4. MODEL FACTORY (FIXED) ---
def create_model(api_key: str):
    """Creates a Gemini Model instance with the specific key."""
    model_name = os.getenv("MODEL_SMART", "gemma-3-27b-it")
    # Avoid global state mutation for thread safety - BUT GeminiModel requires env vars
    os.environ["GEMINI_API_KEY"] = api_key
    os.environ["GOOGLE_API_KEY"] = api_key
    return GeminiModel(model_name)

# --- 5. INITIALIZATION ---
_initial_keys = os.getenv("RESEARCH_KEYS", "").split(",")
if not _initial_keys or not _initial_keys[0].strip():
    # Fallback to GOOGLE_API_KEYS if RESEARCH_KEYS is missing (legacy compat)
    _initial_keys = os.getenv("GOOGLE_API_KEYS", "").split(",")
    if not _initial_keys or not _initial_keys[0].strip():
        raise ValueError("CRITICAL: No API keys found in .env (checked RESEARCH_KEYS and GOOGLE_API_KEYS)")

_current_model = create_model(_initial_keys[0].strip())

# --- 6. THE AGENT ---
universal_agent = Agent(_current_model, deps_type=ResearchDeps)

# --- 7. KEY ROTATION HOOK ---
def update_agent_model(api_key: str):
    """
    Called by main.py to hot-swap the API key.
    """
    new_model = create_model(api_key)
    universal_agent.model = new_model

# --- 8. PROMPTS ---
SCOUT_SYSTEM_PROMPT = (
    f"Current Date: {datetime.now().strftime('%Y-%m-%d')}\n"
    "ROLE: Quantitative Strategist.\n"
    "TASK: Find ONE new, specific quantitative trading strategy topic.\n\n"
    
    "--- OUTPUT INSTRUCTIONS (STRICT JSON) ---\n"
    "You must return a JSON object with a 'tool' field.\n\n"
    
    "EXAMPLE 1 (Single Search)::\n"
    '  { "tool": "search_general", "query": "volatility breakout strategies python 2025", "rationale": "Finding specific code" }\n\n'
    
    "EXAMPLE 2 (Parallel Search - FASTER)::\n"
    '  { "tool": "search_general", "queries": ["RSI divergence trading", "momentum crypto strategy", "mean reversion stocks"], "rationale": "Exploring multiple angles at once" }\n\n'
    
    "EXAMPLE 3 (Finish - DO NOT OUTPUT A SCHEMA, OUTPUT VALUES):\n"
    '  { "tool": "finish_scout", "result": { "topic": "Adaptive RSI Regime Switching", "source_context": "Found on QuantConnect forum" } }\n\n'
    
    "--- PROTOCOL ---\n"
    "1. SEARCH: Use `search_general`. TARGET: 'Price Action', 'OHLCV', 'Volatility', 'Momentum', 'Trend'.\n"
    "2. PARALLEL SEARCH: Use `queries` (list) to run MULTIPLE searches at once. This is FASTER.\n"
    "3. ASSET CLASSES: You MUST vary your searches. Look for 'Forex Trading Strategy', 'Stock Market Quant Strategy', 'Crypto Algorithmic Trading'.\n"
    "4. BAN LIST: DO NOT search for 'Order Book', 'Funding Rate', 'On-Chain', 'Arbitrage', 'HFT'. We DO NOT have this data.\n"
    "5. ANALYZE: Pick the most interesting specific concept immediately.\n"
    "6. FINISH: Call `finish_scout` with the TOPIC NAME.\n"
)

SNIPER_SYSTEM_PROMPT = (
    f"Current Date: {datetime.now().strftime('%Y-%m-%d')}\n"
    "ROLE: Senior Quantitative Developer (HFT & Algorithmic).\n"
    "TASK: Reverse-engineer a trading strategy into a strict Python-ready specification.\n\n"
    
    "--- OUTPUT INSTRUCTIONS (STRICT JSON) ---\n"
    "EXAMPLE 1 (Single Search):\n"
    '  { "tool": "search_academic", "query": "RSI Divergence Python Implementation", "rationale": "Need logic" }\n\n'
    
    "EXAMPLE 2 (Parallel Search - FASTER):\n"
    '  { "tool": "search_general", "queries": ["RSI Divergence implementation", "RSI Python backtest", "RSI strategy rules"], "rationale": "Gathering multiple sources" }\n\n'
    
    "EXAMPLE 3 (Single Read):\n"
    '  { "tool": "read_content", "url": "https://arxiv.org/pdf/...", "rationale": "Extracting logic" }\n\n'
    
    "EXAMPLE 4 (Parallel Read - FASTER):\n"
    '  { "tool": "read_content", "urls": ["https://example.com/strat1", "https://example.com/strat2"], "rationale": "Comparing sources" }\n\n'
    
    "EXAMPLE 5 (Finish - OUTPUT DATA, NOT SCHEMA):\n"
    '  { "tool": "finish_sniper", "result": { "name": "Dual SMA Crossover", "description": "...", "logic_steps": ["[DATA]...", "[ENTRY]..."], "tags": ["Trend"], "timeframes": ["1h", "4h"], "best_source_url": "...", "quality_score": 9, "is_duplicate": false, "symbols": ["BTC/USDT"], "asset_type": "crypto" } }\n\n'
    
    "--- LOGIC RULES ---\n"
    "1. TAGS: [VARIABLES], [DATA], [INDICATOR], [ENTRY LONG], [EXIT LONG], [ENTRY SHORT], [EXIT SHORT], [RISK].\n"
    "2. TIMEFRAMES: You MUST determine ALL optimal timeframes. Return a LIST. e.g. ['5m', '15m'] or ['1h', '4h']. Default to ['1h'] if unsure.\n"
    "3. SYMBOLS & ASSETS (CRITICAL):\n"
    "   - You MUST extract the intended asset class: 'crypto', 'stock', or 'index'.\n"
    "   - FOREX IS NOT SUPPORTED - skip any forex strategies.\n"
    "   - You MUST suggest a LIST of best symbols. E.g. ['BTC/USDT', 'ETH/USDT'] or ['SPY', 'QQQ'].\n"
    "   - If the strategy is generic, default to ['BTC/USDT'] and 'crypto'.\n"
    "4. DATA CONSTRAINTS (CRITICAL):\n"
    "   - We ONLY have OHLCV data (Open, High, Low, Close, Volume).\n"
    "   - DO NOT extract strategies that require: Funding Rate, Order Book, Bid/Ask Spread, On-Chain data, or Multiple Exchanges.\n"
    "   - If a strategy requires this data, SKIP IT and find another strategy.\n"
    "5. DIVERSITY ENFORCEMENT:\n"
    "   - DO NOT OUTPUT 'Bollinger Band Mean Reversion' unless explicitly asked. We have too many.\n"
    "   - PREFER: RSI, MACD, ATR, Donchian Channels, Moving Averages, Fractal Breakouts.\n"
    "   - PREFER: Strategies that work on Stocks (SPY, QQQ) or Forex (EUR/USD) to balance the crypto bias.\n"
    
    "--- FEW-SHOT EXAMPLES (GOOD OUTPUTS) ---\n"
    "1. **Dual SMA Trend**: Entry: SMA(20) > SMA(50). Exit: SMA(20) < SMA(50).\n"
    "2. **RSI Divergence**: Entry: Price Lower Low AND RSI Higher Low (Bullish).\n"
    "3. **Volatility Breakout**: Entry: Close > Open + (ATR * 1.5).\n"
)