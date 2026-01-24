
import asyncio
from src.common.database import get_session
from sqlalchemy import text

async def analyze_rejected():
    async for session in get_session():
        # Count total rejected
        result = await session.execute(text("SELECT count(*) FROM strategy WHERE status = 'REJECTED'"))
        total_rejected = result.scalar()
        print(f"Total Rejected: {total_rejected}")

        # Sample rejected strategies
        print("\n--- Latest 5 Rejected Strategies ---")
        result = await session.execute(text("SELECT name, description, quality_score, created_at FROM strategy WHERE status = 'REJECTED' ORDER BY created_at DESC LIMIT 5"))
        for row in result:
            print(f"Name: {row.name}")
            print(f"Score: {row.quality_score}")
            print(f"Description: {row.description[:100]}...")
            print("-" * 30)
            
        # Check reasons if stored (we don't explicit store reason column, but we might infer from quality score or logs)
        # Low quality < 5. Duplicate is... marked as rejected. 
        # We can check if any existing valid strategy has similar name?
        
        break

if __name__ == "__main__":
    import sys
    import os
    # Add project root to python path
    sys.path.append(os.getcwd())
    asyncio.run(analyze_rejected())
