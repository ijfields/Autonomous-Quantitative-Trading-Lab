
import logging
from typing import Dict, Any, Optional

from src.backtest.agents.coder_agent import PythonStrategyCode
from src.backtest.engine.runner import code_runner

logger = logging.getLogger("BacktestExecutor")

class BacktestExecutor:
    def __init__(self):
        pass

    async def run_backtest(self, 
                           strategy_id: int, 
                           code: PythonStrategyCode, 
                           symbol: str = "BTC/USDT", 
                           timeframe: str = "1h", 
                           asset_type: str = "crypto",
                           start_date: str = None,
                           end_date: str = None
                           ) -> Dict[str, Any]:
        logger.info(f"🚀 Executing Strategy {strategy_id} on {symbol}...")
        
        # 1. Create Script
        script_path = await code_runner.create_script(
            strategy_id=strategy_id,
            class_parameters=code.class_parameters,
            init_indicators=code.init_indicators,
            next_logic=code.next_logic,
            symbol=symbol,
            timeframe=timeframe,
            asset_type=asset_type,
            start_date=start_date,
            end_date=end_date
        )
        
        # 2. Run Process
        result = await code_runner.run_subprocess(script_path)
        
        if result.get("error"):
             logger.error(f"❌ Execution Error: {result['error']}\nLogs: {result.get('logs', '')}")
             
        return result

backtest_executor = BacktestExecutor()