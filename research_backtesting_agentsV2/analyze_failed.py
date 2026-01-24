import asyncio
from src.common.database import get_session
from src.common.models import Strategy, StrategyStatus
from sqlalchemy import select
from collections import Counter

async def analyze_failed():
    print("🔍 Analyzing 'FAILED' Strategies (Generation Failures)...")
    
    error_patterns = Counter()
    
    async for session in get_session():
        # Query strategies with status = FAILED
        query = select(Strategy).where(Strategy.status == StrategyStatus.FAILED)
        result = await session.execute(query)
        failed = result.scalars().all()
        
        print(f"📉 Total Failed Strategies: {len(failed)}")
        
        if not failed:
            print("No FAILED strategies found. Checking alternate sources...")
            break
        
        print("\n--- Detailed Failure Analysis ---")
        for strat in failed:
            print(f"\n🆔 ID: {strat.id}")
            print(f"📛 Name: {strat.name}")
            print(f"📜 Description: {strat.description[:200] if strat.description else 'N/A'}...")
            print(f"📊 Quality Score: {strat.quality_score}")
            print(f"📅 Created: {strat.created_at}")
            print(f"🔖 Tags: {strat.tags}")
            print(f"🔗 Source: {strat.source_url}")
            print("-" * 50)

        break

if __name__ == "__main__":
    import sys
    import os
    sys.path.append(os.getcwd())
    asyncio.run(analyze_failed())
