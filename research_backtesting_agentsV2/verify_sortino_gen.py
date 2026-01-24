
import asyncio
from pathlib import Path
from src.backtest.engine.runner import code_runner

async def test_generation():
    print("🚀 Generating Test Optimization Script...")
    
    # Dummy Strategy Data
    class_params = "period = 14"
    indicators = "self.sma = self.I(ta.sma, self.data.Close, self.period)"
    logic = "pass"
    
    # Generate Script targeting Sortino
    path = await code_runner.create_script(
        strategy_id=9999,
        class_parameters=class_params,
        init_indicators=indicators,
        next_logic=logic,
        symbol="BTC/USDT",
        timeframe="1h",
        asset_type="crypto",
        optimize=True,
        tunable_params={"period": ("int", 14, 5, 20)},
        optimization_target="Sortino Ratio",  # <--- TESTING THIS
        file_suffix="_TEST_SORTINO"
    )
    
    print(f"✅ Generated: {path}")
    
    # Read file to verify injection
    with open(path, "r") as f:
        content = f.read()
        
    if 'stats["Sortino Ratio"]' in content:
        print("🎉 SUCCESS: Found 'stats[\"Sortino Ratio\"]' in the generated code.")
    else:
        print("❌ FAILURE: Did not find 'stats[\"Sortino Ratio\"]' in the code.")
        print("--- SNIPPET ---")
        start = content.find("def objective")
        print(content[start:start+500])

if __name__ == "__main__":
    asyncio.run(test_generation())
