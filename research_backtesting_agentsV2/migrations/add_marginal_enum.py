"""
Migration: Add MARGINAL to strategyresult enum
Run this ONCE to add the new enum value to PostgreSQL.
"""
import asyncio
import asyncpg
import os
from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL").replace("postgresql+asyncpg://", "postgresql://")

async def migrate():
    conn = await asyncpg.connect(DATABASE_URL)
    
    try:
        # Add MARGINAL to the enum if it doesn't exist
        await conn.execute("""
            ALTER TYPE strategyresult ADD VALUE IF NOT EXISTS 'marginal';
        """)
        print("✅ Successfully added 'marginal' to strategyresult enum!")
    except Exception as e:
        print(f"❌ Migration error: {e}")
    finally:
        await conn.close()

if __name__ == "__main__":
    asyncio.run(migrate())
