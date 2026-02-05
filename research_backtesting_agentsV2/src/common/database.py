import os
from typing import AsyncGenerator
from sqlmodel import SQLModel, text
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv

# Import models so they register with SQLModel.metadata before create_all
# Use relative import to avoid duplicate table registration
from src.common.models import Strategy, StrategyEmbedding, BacktestResult, AgentHeartbeat

# 1. Load Environment Variables
from pathlib import Path
load_dotenv(Path(__file__).parent.parent.parent.parent / ".env")

# 2. Get Database URL
DB_URL = os.getenv("DATABASE_URL")
if not DB_URL:
    raise ValueError("DATABASE_URL missing in .env")

# 3. Create the Async Engine
engine = create_async_engine(DB_URL, echo=False, future=True)

# 4. Initialization Function (Runs on startup)
async def init_db():
    async with engine.begin() as conn:
        # A. Enable Vector Extension (Critical for AI)
        await conn.execute(text("CREATE EXTENSION IF NOT EXISTS vector"))
        # B. Create All Tables defined in models.py
        await conn.run_sync(SQLModel.metadata.create_all)
        
        # C. Auto-Migrate: Add 'timeframe' column if missing (REMOVED - DEPRECATED)
        # try:
        #     await conn.execute(text("ALTER TABLE strategy ADD COLUMN IF NOT EXISTS timeframe TEXT DEFAULT '1h'"))
        # except Exception as e:
        #     print(f"Migration Info: {e}")
        
        # D. Auto-Migrate: Add Optuna optimization columns
        try:
            await conn.execute(text("ALTER TABLE backtestresult ADD COLUMN IF NOT EXISTS is_optimized BOOLEAN DEFAULT FALSE"))
            await conn.execute(text("ALTER TABLE backtestresult ADD COLUMN IF NOT EXISTS optimized_params JSON DEFAULT '{}'"))
            await conn.execute(text("ALTER TABLE backtestresult ADD COLUMN IF NOT EXISTS optimization_trials INTEGER DEFAULT 0"))
        except Exception as e:
            print(f"Optimization Migration Info: {e}")

# 5. Session Dependency (Used by the Agent)
async def get_session() -> AsyncGenerator[AsyncSession, None]:
    async_session = sessionmaker(
        engine, class_=AsyncSession, expire_on_commit=False
    )
    async with async_session() as session:
        yield session