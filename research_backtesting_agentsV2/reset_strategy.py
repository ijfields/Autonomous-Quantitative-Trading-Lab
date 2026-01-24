import asyncio
from src.common.database import init_db, get_session
from src.common.models import Strategy, StrategyStatus
from sqlalchemy import select

async def reset_strategies():
    print("♻️ Resetting strategies to READY_FOR_CODE...")
    await init_db()
    async for session in get_session():
        # 1. Delete all backtest results
        print("🗑️ Deleting all backtest history...")
        from sqlalchemy import text
        await session.execute(text("DELETE FROM backtestresult"))
        
        # 2. Reset strategy statuses
        # Select strategies that are COMPLETED, FAILED, or CRASHED
        stmt = select(Strategy).where(Strategy.status.in_([
             StrategyStatus.COMPLETED, 
             StrategyStatus.FAILED,
             StrategyStatus.RESEARCHING,
             StrategyStatus.BACKTESTING
             # NOTE: REJECTED is intentionally excluded - they stay rejected
        ]))
        result = await session.execute(stmt)
        strategies = result.scalars().all()
        
        count = 0
        for strategy in strategies:
            strategy.status = StrategyStatus.READY_FOR_CODE
            session.add(strategy)
            count += 1
        
        # Reset all strategies not just the filtered ones? 
        # Actually user said "clean all backtests", implying we want to re-run everything.
        # But maybe we should be safer. The API says "Reset strategies to READY_FOR_CODE".
        
        await session.commit()
        print(f"✅ Deleted all backtest history.")
        print(f"✅ Reset {count} strategies to READY_FOR_CODE.")
        break

if __name__ == "__main__":
    asyncio.run(reset_strategies())
