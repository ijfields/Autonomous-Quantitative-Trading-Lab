
import asyncio
from src.common.database import get_session
from src.common.models import BacktestResult, StrategyResult
from sqlalchemy import select
from collections import Counter

async def analyze_crashes():
    print("🔍 Analyzing Backtest Crashes...")
    
    error_patterns = Counter()
    total_crashes = 0
    
    async for session in get_session():
        # Query all crashed backtests
        query = select(BacktestResult).where(BacktestResult.result_rating == StrategyResult.CRASHED)
        result = await session.execute(query)
        crashed_tests = result.scalars().all()
        
        total_crashes = len(crashed_tests)
        print(f"📉 Total Crashed Backtests: {total_crashes}")
        
        for bt in crashed_tests:
            msg = bt.error_message or "No error message logged."
            
            # Simple clustering/simplification of error messages
            if "ModuleNotFoundError" in msg:
                key = "ModuleNotFoundError (Missing Libs)"
            elif "SyntaxError" in msg:
                key = "SyntaxError (Bad Code Generation)"
            elif "KeyError" in msg:
                # Often "KeyError: 'close'" or similar
                key = f"KeyError (Data Missing?): {msg.split('KeyError')[1].strip()[:30]}" 
            elif "AttributeError" in msg:
                # AttributeError: 'DataFrame' object has no attribute 'ta'
                key = f"AttributeError (Pandas/TA issue): {msg.split('AttributeError')[1].strip()[:50]}"
            elif "EmptyDataError" in msg or "No data found" in msg:
                key = "No Data Found / Empty DataFrame"
            elif "MemoryError" in msg:
                key = "MemoryError (OOM)"
            elif "TimedOut" in msg or "Timeout" in msg:
                key = "Execution Timeout"
            else:
                # Generic fallback: verify first 50 chars
                key = f"Other: {msg[:100]}..."
                
            error_patterns[key] += 1

        print("\n📊 Top Crash Reasons:")
        print("="*40)
        for reason, count in error_patterns.most_common():
            print(f"- {count}: {reason}")
            
        # Detail sample for "Other"
        print("\n📝 Sample 'Other' Errors:")
        others = [bt for bt in crashed_tests if "Other" in (
            f"Other: {(bt.error_message or '')[:100]}..." 
            if not any(x in (bt.error_message or "") for x in ["ModuleNotFoundError", "SyntaxError", "KeyError", "AttributeError", "EmptyDataError", "No data found", "MemoryError", "TimeOut"]) 
            else ""
        )]
        for bt in others[:5]:
             print(f"ID {bt.id}: {bt.error_message}")
             
        break

if __name__ == "__main__":
    import sys
    import os
    sys.path.append(os.getcwd())
    asyncio.run(analyze_crashes())
