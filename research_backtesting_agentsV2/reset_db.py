import asyncio
from src.common.database import init_db, get_session
from src.common.models import Strategy, BacktestResult, StrategyEmbedding
from sqlalchemy import delete

async def reset_database():
    print("☢️ NUCLEAR RESET: Clearing ALL data...")
    await init_db()
    async for session in get_session():
        # Delete in order of dependencies
        await session.execute(delete(BacktestResult))
        await session.execute(delete(StrategyEmbedding))
        await session.execute(delete(Strategy))
        await session.commit()
        print("✅ Database cleared.")
        break

if __name__ == "__main__":
    asyncio.run(reset_database())
