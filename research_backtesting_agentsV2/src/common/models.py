from typing import Optional, List
from datetime import datetime
from enum import Enum
from sqlmodel import Field, SQLModel, Column, JSON, Text, Relationship
from pgvector.sqlalchemy import Vector

# ==========================================
# 1. ENUMS (Granular Tracking)
# ==========================================

class StrategyStatus(str, Enum):
    # Discovery Phase
    SCOUTED = "scouted"             # Found by Scout, waiting for Sniper
    RESEARCHING = "researching"     # Sniper is analyzing PDF/Web
    
    # Development Phase
    READY_FOR_CODE = "ready_code"   # Logic extracted, needs Python script
    CODING = "coding"               # AI is generating the backtest script
    
    # Execution Phase
    QUEUED_FOR_BACKTEST = "queued"  # Code ready, waiting for execution slot
    FETCHING_DATA = "fetching_data" # Downloading OHLCV
    BACKTESTING = "backtesting"     # Running the engine
    
    # Outcomes
    COMPLETED = "completed"         # Done, results available
    FAILED = "failed"               # Crashed or syntax error
    ARCHIVED = "archived"           # Duplicate or low quality
    REJECTED = "rejected"           # Filtered out by Research Agent (Low Score)

class StrategyResult(str, Enum):
    PENDING = "PENDING"
    PROFITABLE = "PROFITABLE"
    MARGINAL = "MARGINAL"         # Positive return but weak metrics
    UNPROFITABLE = "UNPROFITABLE"
    CRASHED = "CRASHED"

class AgentStatus(str, Enum):
    """Status of an agent for real-time dashboard tracking."""
    IDLE = "idle"
    SCOUTING = "scouting"
    SNIPING = "sniping"
    CODING = "coding"
    BACKTESTING = "backtesting"
    ERROR = "error"
    STOPPED = "stopped"

# ==========================================
# 2. TABLES
# ==========================================

class StrategyEmbedding(SQLModel, table=True):
    """
    Dedicated table for Vector Embeddings to keep the main table light.
    Relationship: 1-to-1 with Strategy.
    """
    id: Optional[int] = Field(default=None, primary_key=True)
    
    # Foreign Key
    strategy_id: int = Field(foreign_key="strategy.id", unique=True)
    
    # The Vector (384 dimensions for MiniLM)
    embedding: List[float] = Field(sa_column=Column(Vector(384)))
    
    # Back-link (Optional in SQLModel but good practice)
    # strategy: "Strategy" = Relationship(back_populates="embedding_data")


class Strategy(SQLModel, table=True):
    """
    The Core Knowledge Entity. Lightweight metadata only.
    """
    id: Optional[int] = Field(default=None, primary_key=True)
    
    # --- IDENTITY ---
    name: str = Field(index=True)
    description: str = Field(sa_column=Column(Text))
    # Supports multi-timeframe testing (e.g. ["15m", "1h", "4h"])
    timeframes: List[str] = Field(default=["1h"], sa_column=Column(JSON))
    
    # --- KNOWLEDGE ---
    # The step-by-step logic extracted by the Sniper
    logic_steps: List[str] = Field(default=[], sa_column=Column(JSON))
    
    # Metadata
    tags: List[str] = Field(default=[], sa_column=Column(JSON))
    source_url: Optional[str] = None
    quality_score: int = Field(default=0)
    
    # --- ASSET CONFIGURATION ---
    # Supports multi-symbol testing (e.g. ["BTC/USDT", "ETH/USDT"])
    symbols: List[str] = Field(default=["BTC/USDT"], sa_column=Column(JSON))
    asset_type: str = Field(default="crypto", description="crypto, stock, or index")

    # --- STATE MANAGEMENT ---
    status: StrategyStatus = Field(default=StrategyStatus.SCOUTED)
    created_at: datetime = Field(default_factory=datetime.utcnow)
    
    # --- DEDUPLICATION ---
    # Combined fingerprint of indicators + entry conditions for detecting functional duplicates
    logic_fingerprint: Optional[str] = Field(default=None, index=True, description="Hash of indicators and entry logic for deduplication")

    # --- RELATIONSHIPS ---
    # Link to the separate embedding table
    embedding_rel: Optional["StrategyEmbedding"] = Relationship(
        sa_relationship_kwargs={"uselist": False, "cascade": "all, delete"}
    )
    
    # Link to Backtests (One Strategy -> Many Code Iterations/Results)
    backtests: List["BacktestResult"] = Relationship(back_populates="strategy")


class BacktestResult(SQLModel, table=True):
    """
    Stores the Code and the Performance of a specific run.
    Moving 'code' here allows multiple iterations (v1, v2) for the same strategy.
    """
    id: Optional[int] = Field(default=None, primary_key=True)
    
    # Link to parent Strategy
    strategy_id: int = Field(foreign_key="strategy.id")
    strategy: Strategy = Relationship(back_populates="backtests")
    
    # --- THE IMPLEMENTATION ---
    # The Python code used for this specific test
    code: Optional[str] = Field(default=None, sa_column=Column(Text))
    
    # --- CONTEXT ---
    symbol: str = Field(default="BTC/USDT", description="The specific symbol this result is for")
    timeframe: str = Field(default="1h", description="The specific timeframe this result is for")

    # --- METRICS ---
    sharpe_ratio: Optional[float] = None
    sortino_ratio: Optional[float] = None
    win_rate: Optional[float] = None
    total_return_pct: Optional[float] = None
    buy_hold_return_pct: Optional[float] = None # <-- ADDED
    max_drawdown_pct: Optional[float] = None
    volatility_pct: Optional[float] = None      # <-- ADDED
    trades_count: Optional[int] = None
    
    # --- DURATION METRICS (for return context) ---
    backtest_period_days: Optional[int] = Field(default=None, description="Total duration of backtest in days")
    daily_return_pct: Optional[float] = Field(default=None, description="Average daily return percentage")
    weekly_return_pct: Optional[float] = Field(default=None, description="Average weekly return percentage")
    annualized_return_pct: Optional[float] = Field(default=None, description="Annualized return percentage (365-day projection)")
    
    # --- CONFIGURATION ---
    # e.g. {"symbol": "BTC/USDT", "timeframe": "1h", "stop_loss": 0.05}
    parameters: dict = Field(default={}, sa_column=Column(JSON))
    
    # --- LOGS ---
    execution_log: Optional[str] = Field(default=None, sa_column=Column(Text))
    error_message: Optional[str] = Field(default=None, sa_column=Column(Text))
    
    result_rating: StrategyResult = Field(default=StrategyResult.PENDING)
    tested_at: datetime = Field(default_factory=datetime.utcnow)
    
    # --- OPTIMIZATION (Optuna) ---
    is_optimized: bool = Field(default=False)
    optimized_params: dict = Field(default={}, sa_column=Column(JSON))
    optimization_trials: int = Field(default=0)


class AgentHeartbeat(SQLModel, table=True):
    """
    Real-time agent status for dashboard monitoring.
    Each running agent updates this periodically.
    """
    id: Optional[int] = Field(default=None, primary_key=True)

    # --- IDENTITY ---
    instance_id: int = Field(index=True, description="Agent instance number (1, 2, 3...)")
    agent_type: str = Field(index=True, description="'research' or 'backtest'")

    # --- STATUS ---
    status: AgentStatus = Field(default=AgentStatus.IDLE)
    current_task: Optional[str] = Field(default=None, description="Current activity description")
    current_niche: Optional[str] = Field(default=None, description="Current niche being explored (research only)")

    # --- TIMESTAMPS ---
    last_heartbeat: datetime = Field(default_factory=datetime.utcnow)
    started_at: datetime = Field(default_factory=datetime.utcnow)

    # --- ERROR TRACKING ---
    recent_errors: List[dict] = Field(default=[], sa_column=Column(JSON), description="Last 10 errors [{type, message, timestamp}]")

    # --- METRICS ---
    api_calls_today: int = Field(default=0)
    strategies_found_today: int = Field(default=0)