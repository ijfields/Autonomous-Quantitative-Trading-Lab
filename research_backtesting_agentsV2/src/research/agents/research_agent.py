import os
import logging
import json
from dataclasses import dataclass
from typing import List, Optional, Literal, Union
from datetime import datetime

from pydantic import BaseModel, Field
from pydantic_ai import Agent, RunContext
from pydantic_ai.models.gemini import GeminiModel
from pydantic_ai.models.anthropic import AnthropicModel
from pydantic_ai.models.openai import OpenAIChatModel
from pydantic_ai.providers.moonshotai import MoonshotAIProvider
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

# --- 4. MODEL FACTORY (MULTI-PROVIDER) ---
def create_model(api_key: str, model_type: str = "smart"):
    """Creates a Model instance for the configured provider.

    Args:
        api_key: The API key to use.
        model_type: "fast" for high-quota model (scout), "smart" for reasoning model (sniper).

    Supports:
        - Gemini (default): LLM_PROVIDER=gemini
        - Claude:           LLM_PROVIDER=claude  + ANTHROPIC_API_KEY
        - Kimi (Moonshot):  LLM_PROVIDER=kimi    + MOONSHOTAI_API_KEY
    """
    provider = os.getenv("LLM_PROVIDER", "gemini").lower()

    if provider == "claude":
        if model_type == "fast":
            model_name = os.getenv("MODEL_FAST", "claude-3-5-haiku-latest")
        else:
            model_name = os.getenv("MODEL_SMART", "claude-sonnet-4-20250514")
        anthropic_key = api_key if api_key.startswith("sk-ant") else os.getenv("ANTHROPIC_API_KEY", api_key)
        os.environ["ANTHROPIC_API_KEY"] = anthropic_key
        return AnthropicModel(model_name)

    elif provider == "kimi":
        if model_type == "fast":
            model_name = os.getenv("MODEL_FAST", "kimi-k2-0711-preview")
        else:
            model_name = os.getenv("MODEL_SMART", "kimi-k2-0711-preview")
        kimi_key = api_key if api_key.startswith("sk-") else os.getenv("MOONSHOTAI_API_KEY", api_key)
        return OpenAIChatModel(model_name, provider=MoonshotAIProvider(api_key=kimi_key))

    else:
        # Gemini (default)
        if model_type == "fast":
            model_name = os.getenv("MODEL_FAST", "gemini-2.5-flash-lite")
        else:
            model_name = os.getenv("MODEL_SMART", "gemini-2.5-flash")
        os.environ["GEMINI_API_KEY"] = api_key
        os.environ["GOOGLE_API_KEY"] = api_key
        return GeminiModel(model_name)

# --- 5. INITIALIZATION ---
_provider = os.getenv("LLM_PROVIDER", "gemini").lower()

if _provider == "claude":
    _initial_key = os.getenv("ANTHROPIC_API_KEY", "")
    if not _initial_key:
        raise ValueError("CRITICAL: ANTHROPIC_API_KEY not found in .env (LLM_PROVIDER=claude)")
    _initial_keys = [_initial_key]
    logging.getLogger(__name__).info("Using Claude (Anthropic) as LLM provider")

elif _provider == "kimi":
    _initial_key = os.getenv("MOONSHOTAI_API_KEY", "")
    if not _initial_key:
        raise ValueError("CRITICAL: MOONSHOTAI_API_KEY not found in .env (LLM_PROVIDER=kimi)")
    _initial_keys = [_initial_key]
    logging.getLogger(__name__).info("Using Kimi (Moonshot AI) as LLM provider")

else:
    _initial_keys = os.getenv("RESEARCH_KEYS", "").split(",")
    if not _initial_keys or not _initial_keys[0].strip():
        _initial_keys = os.getenv("GOOGLE_API_KEYS", "").split(",")
        if not _initial_keys or not _initial_keys[0].strip():
            raise ValueError("CRITICAL: No API keys found in .env (checked RESEARCH_KEYS and GOOGLE_API_KEYS)")
    logging.getLogger(__name__).info("Using Gemini (Google) as LLM provider")

_current_model = create_model(_initial_keys[0].strip())

# --- 6. THE AGENT ---
universal_agent = Agent(_current_model, deps_type=ResearchDeps)

# --- 7. KEY ROTATION HOOK ---
def update_agent_model(api_key: str, model_type: str = "smart"):
    """
    Called by main.py to hot-swap the API key and/or model.

    Args:
        api_key: The API key to use.
        model_type: "fast" for high-quota model (scout), "smart" for reasoning model (sniper).
    """
    new_model = create_model(api_key, model_type)
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
    "3. **Volatility Breakout**: Entry: Close > Open + (ATR * 1.5).\n"
)