import asyncio
import json
import logging
import sys
import textwrap
import re
import traceback
from pathlib import Path
from typing import Dict, Any, Optional


from src.backtest.templates.base_strategy import STRATEGY_TEMPLATE

logger = logging.getLogger("CodeRunner")

TEMP_DIR = Path("temp_backtests")
TEMP_DIR.mkdir(exist_ok=True)

class CodeRunner:
    """
    Centralized execution engine for running generated strategies in a subprocess.
    Handles:
    1. Template Injection (Base Strategy + AI Code)
    2. Subprocess Management
    3. JSON Output Parsing (Regex-based)
    4. Temporary File Cleanup
    """

    @staticmethod
    def _indent_code(code_str: str, target_spaces: int = 4) -> str:
        """
        Smart Indenter:
        1. Dedents the input block to remove common leading whitespace.
        2. Applies the specific 'target_spaces' indentation to EVERY line.
        """
        if not code_str:
            return ""
            
        # 1. Normalize to 0 indentation (Dedent)
        dedented = textwrap.dedent(str(code_str)).strip()
        
        # 2. Split into lines
        lines = dedented.split("\n")
        
        if not lines: return ""
        
        # 3. Apply Target Indentation
        # The first line inherits the indentation of the {tag} in the template.
        # We only indent subsequent lines to match that level.
        first_line = lines[0] 
        rest_lines = [(" " * target_spaces) + line for line in lines[1:]]
        
        return "\n".join([first_line] + rest_lines)

    async def create_script(self, 
                            strategy_id: int, 
                            class_parameters: str, 
                            init_indicators: str, 
                            next_logic: str,
                            symbol: str, 
                            timeframe: str, 
                            asset_type: str,
                            start_date: str = None,
                            end_date: str = None,
                            optimize: bool = False,
                            tunable_params: Dict[str, Any] = None,
                            optimization_target: str = "Sharpe Ratio",
                            file_suffix: str = "") -> Path:
        """
        Generates the executable Python script.
        """
        
        # 1. Indent Code Blocks
        # class params are at class level (indent 4)
        params_code = self._indent_code(class_parameters, 4)
        # init and next are inside methods (indent 8)
        indicators_code = self._indent_code(init_indicators, 8)
        logic_code = self._indent_code(next_logic, 8)

        # 2. Fill Template
        strategy_code = STRATEGY_TEMPLATE.format(
            params=params_code,
            indicators=indicators_code,
            logic=logic_code
        )

        # Prepare date args
        start_date_repr = f'"{start_date}"' if start_date else "None"
        end_date_repr = f'"{end_date}"' if end_date else "None"

        # 3. Append Execution Block
        if optimize:
            # --- OPTIMIZED EXECUTION BLOCK (Turbo Mode) ---
            # Moves the Optuna loop INSIDE the process to reuse data loading
            
            # Serialize tunable params for injection
            # Format: {"param_name": ("int", 10, 5, 20), ...}
            tunable_params_json = json.dumps(tunable_params) if tunable_params else "{}"
            
            execution_block = f"""
# --- INTERNALIZED OPTIMIZATION LOOP (TURBO MODE) ---
def run_optimization_loop():
    import sys
    import json
    import pandas as pd
    import optuna
    import re
    from backtesting import Backtest
    
    # Add project root to path
    import os
    sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
    from src.backtest.data.loader import DataLoader

    # Suppress Optuna logging specifically in this subprocess
    optuna.logging.set_verbosity(optuna.logging.WARN)

    try:
        # 1. Load Data (ONCE)
        loader = DataLoader()
        data = loader.fetch_data("{symbol}", "{timeframe}", "{asset_type}", start_date={start_date_repr}, end_date={end_date_repr})
        
        if data.empty:
            print("---JSON_START---")
            print(json.dumps({{"error": "No data found", "symbol": "{symbol}", "timeframe": "{timeframe}"}}))
            print("---JSON_END---")
            return
            
        tunable_params = {tunable_params_json}
        
        # 2. Define Objective Function
        def objective(trial):
            # Patch the class attributes dynamically
            for name, (ptype, default, pmin, pmax) in tunable_params.items():
                if ptype == 'int':
                    val = trial.suggest_int(name, int(pmin), int(pmax))
                else:
                    val = trial.suggest_float(name, pmin, pmax)
                
                # Hot-patch the Strategy Class
                setattr(GeneratedStrategy, name, val)
            
            try:
                # Run Backtest
                bt = Backtest(data, GeneratedStrategy, cash=1_000_000, commission=.001)
                stats = bt.run()
                
                # Return Target Metric (Dynamic)
                # Handle cases where Metric is NaN or too few trades
                trades = stats["# Trades"]
                target_val = stats["{optimization_target}"]
                
                if trades < 5:
                    raise optuna.TrialPruned(f"Too few trades: {{trades}}")
                    
                if pd.isna(target_val):
                     return -10.0
                     
                return float(target_val)
                
            except Exception as e:
                # Log within trial if needed, but mainly Prune
                raise optuna.TrialPruned(str(e))

        # 3. Run Optimization
        study = optuna.create_study(
            direction='maximize',
            pruner=optuna.pruners.MedianPruner(n_startup_trials=5, n_warmup_steps=3)
        )
        
        study.optimize(objective, n_trials=30, timeout=120)

        # 4. Extract Best Result
        best_trial = study.best_trial
        best_params = best_trial.params
        best_sharpe = best_trial.value
        
        result = {{
            "success": True,
            "best_params": best_params,
            "best_sharpe": best_sharpe,
            "trials_run": len(study.trials),
            "error": None
        }}
        
        print("---JSON_START---")
        print(json.dumps(result))
        print("---JSON_END---")

    except Exception as e:
        import traceback
        error_res = {{
            "error": str(e),
            "traceback": traceback.format_exc()
        }}
        print("---JSON_START---")
        print(json.dumps(error_res))
        print("---JSON_END---")

if __name__ == "__main__":
    run_optimization_loop()
"""

        else:
            # --- STANDARD EXECUTION BLOCK (Single Run) ---
            execution_block = f"""
# --- AUTO-GENERATED EXECUTION BLOCK ---
# We wrap execution in a function to PREVENT GLOBAL VARIABLE LEAKAGE.
# This ensures that 'data' is not accessible to the Strategy class via global scope.
def run_and_print_backtest():
    import sys
    import json
    import pandas as pd
    from backtesting import Backtest
    
    # Add project root to path
    import os
    sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
    from src.backtest.data.loader import DataLoader

    try:
        # 1. Load Data
        loader = DataLoader()
        data = loader.fetch_data("{symbol}", "{timeframe}", "{asset_type}", start_date={start_date_repr}, end_date={end_date_repr})
        
        if data.empty:
            print("---JSON_START---")
            print(json.dumps({{"error": "No data found"}}))
            print("---JSON_END---")
            return

        # 2. Configure Backtest
        # cash=1M to handle high priced assets
        # Commission = 0.1%
        bt = Backtest(data, GeneratedStrategy, cash=1_000_000, commission=.001)
        
        # 3. Run
        stats = bt.run()
        
        # 4. Extract Metrics
        def safe_float(val):
            try: return round(float(val), 2) if pd.notna(val) else 0.0
            except: return 0.0

        # Extract data range for duration metrics
        data_start = data.index.min()
        data_end = data.index.max()
        backtest_days = (data_end - data_start).days if pd.notna(data_start) and pd.notna(data_end) else 0

        result = {{
            "return_pct": safe_float(stats["Return [%]"]),
            "buy_hold_pct": safe_float(stats["Buy & Hold Return [%]"]),
            "sharpe": round(float(stats["Sharpe Ratio"]), 3) if pd.notna(stats["Sharpe Ratio"]) else 0.0,
            "sortino": round(float(stats["Sortino Ratio"]), 3) if pd.notna(stats["Sortino Ratio"]) else 0.0,
            "max_drawdown": safe_float(stats["Max. Drawdown [%]"]),
            "trades": int(stats["# Trades"]),
            "win_rate": safe_float(stats["Win Rate [%]"]),
            "volatility": safe_float(stats["Volatility (Ann.) [%]"]),
            "duration_avg": str(stats["Avg. Trade Duration"]),
            "backtest_start_date": data_start.isoformat() if pd.notna(data_start) else None,
            "backtest_end_date": data_end.isoformat() if pd.notna(data_end) else None,
            "backtest_period_days": backtest_days,
            "error": None
        }}
        
        # Print JSON with a special delimiter to make it easy to find
        print("---JSON_START---")
        print(json.dumps(result))
        print("---JSON_END---")

    except Exception as e:
        import traceback
        error_res = {{
            "error": str(e),
            "traceback": traceback.format_exc()
        }}
        print("---JSON_START---")
        print(json.dumps(error_res))
        print("---JSON_END---")

if __name__ == "__main__":
    run_and_print_backtest()
"""
        
        # 4. Write File
        filename = f"strat_{strategy_id}{file_suffix}.py"
        file_path = TEMP_DIR / filename
        
        # Sync write is fast enough for small files
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(strategy_code + execution_block)
            
        return file_path

    async def run_subprocess(self, script_path: Path, timeout: float = 45.0) -> Dict[str, Any]:
        """
        Runs the script in a subprocess and parses the JSON output.
        """
        try:
            process = await asyncio.create_subprocess_exec(
                sys.executable, str(script_path),
                stdout=asyncio.subprocess.PIPE,
                stderr=asyncio.subprocess.PIPE
            )
            
            try:
                stdout, stderr = await asyncio.wait_for(process.communicate(), timeout=timeout)
            except asyncio.TimeoutError:
                try: process.kill() 
                except: pass
                return {"error": "Execution Timed Out"}
            except asyncio.CancelledError:
                try: process.kill()
                except: pass
                raise

            stdout_str = stdout.decode().strip()
            stderr_str = stderr.decode().strip()

            # Parse JSON: Regex search for the delimited block
            # This is much safer than "last line"
            match = re.search(r"---JSON_START---\n(.*?)\n---JSON_END---", stdout_str, re.DOTALL)
            
            if not match:
                # Capture ALL output for debugging
                return {
                    "error": f"No JSON output found (Return Code: {process.returncode})",
                    "logs": stderr_str,
                    "raw_output": stdout_str 
                }
            
            json_str = match.group(1)
            
            try:
                result = json.loads(json_str)
                # Attach raw logs/output to the success result too for debugging
                result["logs"] = stderr_str
                # result["raw_output"] = stdout_str 
                return result
            except json.JSONDecodeError:
                return {
                    "error": f"Invalid JSON Format (Return Code: {process.returncode})",
                    "raw_output": stdout_str
                }

        except Exception as e:
            return {"error": f"Subprocess Exception: {e}"}
        finally:
            # Cleanup File
            try:
                if script_path.exists():
                    pass # script_path.unlink() # KEEP FILE FOR DEBUGGING
            except Exception as e:
                logger.warning(f"Failed to delete temp file {script_path}: {e}")

code_runner = CodeRunner()
