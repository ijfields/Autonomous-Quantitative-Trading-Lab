
import asyncio
from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy import text
from src.common.config import DATABASE_URL

async def check_counts():
    print(f"Connecting to {DATABASE_URL}")
    engine = create_async_engine(DATABASE_URL)
    
    async with engine.connect() as conn:
        print("\n📊 STRATEGY PIPELINE STATUS")
        print("===========================")
        result = await conn.execute(text("SELECT status, COUNT(*) FROM strategy GROUP BY status ORDER BY count(*) DESC"))
        rows = result.fetchall()
        
        total = 0
        for status, count in rows:
            print(f"{status:<20} : {count}")
            total += count
            
        print("===========================")
        print(f"TOTAL                : {total}")

    await engine.dispose()

if __name__ == "__main__":
    asyncio.run(check_counts())
