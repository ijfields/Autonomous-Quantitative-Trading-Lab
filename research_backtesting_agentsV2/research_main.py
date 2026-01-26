import asyncio
import os
import sys
import logging
import random
import time
import re
import json
import ast
import hashlib
from pathlib import Path
from typing import List
from dotenv import load_dotenv
from pydantic import TypeAdapter, ValidationError
from colorama import Fore, Style

from src.common.database import init_db, get_session
from src.common.models import Strategy, StrategyStatus, StrategyEmbedding
from sqlmodel import select
from src.common.key_manager import KeyManager
from src.research.agents.research_agent import (
    universal_agent, 
    update_agent_model, # <--- The function to hot-swap keys
    ResearchDeps, 
    AgentAction, 
    SearchCommand,
    ReadCommand,
    FinishSniperCommand,
    FinishScoutCommand,
    SCOUT_SYSTEM_PROMPT,
    SNIPER_SYSTEM_PROMPT
)
from src.research.tools.web_tools import (
    search_general_web, 
    search_academic_papers, 
    search_github_code, 
    read_url_content,
    embedder 
)

import argparse

# --- ARGUMENT PARSING ---
parser = argparse.ArgumentParser()
parser.add_argument('--instance-id', type=int, default=1, help='Unique instance ID for this agent')
args = parser.parse_args()
INSTANCE_ID = args.instance_id

# --- CONFIGURATION ---
load_dotenv(Path(__file__).parent.parent / ".env")
log_dir = Path("logs")
log_dir.mkdir(exist_ok=True)

# Instance-specific log file
log_file = log_dir / f"research_agent_{INSTANCE_ID}_ops.log"

# Logging Setup
logging.basicConfig(
    level=logging.INFO,
    format=f'%(asctime)s | [Agent {INSTANCE_ID}] | %(levelname)s | %(message)s',
    datefmt='%H:%M:%S',
    handlers=[
        logging.FileHandler(log_file, mode='w'),  # Clear on each run
        logging.StreamHandler(sys.stdout)
    ]
)
for lib in ["httpx", "pydantic_ai", "httpcore", "docling", "rapidocr"]:
    logging.getLogger(lib).setLevel(logging.WARNING)

logger = logging.getLogger(f"ResearchAgent-{INSTANCE_ID}")

# --- INITIALIZE KEY MANAGER (SOLUTION A: STATIC PARTITIONING) ---
# This loads only RESEARCH_KEYS from .env
try:
    key_manager = KeyManager("RESEARCH")
    logger.info(f"🔑 Key Manager initialized with {len(key_manager.keys)} keys.")
except Exception as e:
    logger.critical(str(e))
    sys.exit(1)

# NICHES LIST
NICHES = [
    # --- 1. Momentum & Trend (Classic) ---
    "Multi-Timeframe Momentum", "Trend Following Donchian Channels",
    "Volatility Breakout Strategies", "Adaptive Moving Average Logic",
    "Turtle Trading System", "Golden Cross Optimization",
    "Parabolic SAR Trailing Stops", "Ichimoku Cloud Edge-to-Edge",
    
    # --- 2. Mean Reversion & Oscillators ---
    "Mean Reversion Bollinger Bands", "RSI Regime Switching",
    "Statistical Arbitrage Pairs Trading", "RSI Divergence Strategies",
    "Dual Thrust Trading Algorithm", "Supertrend Pullback Strategies",
    "Williams %R Overbought/Oversold", "CCI Commodity Channel Index Reversion",
    
    # --- 3. Volatility & Pattern ---
    "Volatility Risk Premium Harvesting", "ATR Trailing Stop Strategies", 
    "Inside Bar Breakout Pattern", "Pattern Recognition Head and Shoulders",
    "Machine Learning Alpha Factors", "Kalman Filter Mean Reversion",
    "GARCH Volatility Forecasting", "Implied Volatility vs Historical Volatility",
    
    # --- 4. Advanced Squeeze & Channel ---
    "Bollinger Squeeze with ADX Confirmation",
    "Keltner Channel Breakout", "Volatility Contraction Pattern",
    "PnL-Based Exit Management",
    
    # --- 5. Crypto-Native & On-Chain (NEW) ---
    "Perpetual Futures Funding Rate Arbitrage", "Liquidation Cascade Reversal",
    "CEX-DEX Arbitrage Opportunities", "Token Unlock Event Volatility",
    "Stablecoin Depeg Mean Reversion", "Bitcoin Dominance Cycle Rotation",
    "Altcoin Season Index Rotation", "Exchange Inflow/Outflow Signals",
    
    # --- 6. Order Flow & Microstructure (NEW) ---
    "Order Book Imbalance (OFI) Scalping", "VPOC (Volume Point of Control) Shift",
    "Bid-Ask Spread Capture", "Iceberg Order Detection",
    "VWAP Deviation Mean Reversion", "TWAP Execution Logic",
    
    # --- 7. Statistical & Quant (NEW) ---
    "Cointegration Pairs Trading", "Hurst Exponent Trend vs Mean Reversion",
    "Ornstein-Uhlenbeck Process Modeling", "Kelly Criterion Position Sizing",
    "Fractal Dimension Index", "Shannon Entropy Volatility",
    
    # --- 8. Event-Driven & Sentiment (NEW) ---
    "FOMC Meeting Volatility Straddle", "Earnings Surprise Post-Drift",
    "Social Volume Spike Reversal", "Fear and Greed Index Contrarian",
    "Weekend Efficiency Gap Fill"
]

# --- FINGERPRINT FOR DEDUPLICATION ---
def compute_logic_fingerprint(logic_steps: List[str]) -> str:
    """
    Compute a fingerprint combining indicator signature and entry conditions.
    Two strategies with the same fingerprint are functionally identical.
    """
    # 1. Extract indicator signature
    indicators = set()
    indicator_patterns = [
        r'SMA\s*\(\s*(\d+)\s*\)', r'EMA\s*\(\s*(\d+)\s*\)', r'RSI\s*\(\s*(\d+)\s*\)',
        r'MACD', r'ATR', r'Bollinger', r'Donchian', r'Stochastic', r'ADX',
        r'CCI', r'Williams', r'VWAP', r'OBV', r'MFI'
    ]
    
    for step in logic_steps:
        step_upper = step.upper()
        for pattern in indicator_patterns:
            matches = re.findall(pattern, step, re.IGNORECASE)
            if matches:
                # For patterns with params, include the value
                indicators.add(f"{pattern.split('(')[0].strip()}:{matches[0] if matches[0] else 'yes'}")
            elif re.search(pattern, step, re.IGNORECASE):
                indicators.add(pattern)
    
    indicator_sig = "|".join(sorted(indicators))
    
    # 2. Extract entry conditions hash
    entry_steps = [s.lower().strip() for s in logic_steps if '[ENTRY' in s.upper()]
    entry_hash = hashlib.md5(json.dumps(sorted(entry_steps)).encode()).hexdigest()[:8]
    
    # 3. Combine: "indicators_hash:entry_hash"
    full_fingerprint = f"{hashlib.md5(indicator_sig.encode()).hexdigest()[:8]}:{entry_hash}"
    
    return full_fingerprint

# --- HELPERS ---
def get_agent_response_text(result) -> str:
    """Safely extracts text from the Agent result."""
    if hasattr(result, 'data') and isinstance(result.data, str): return result.data
    if hasattr(result, 'output') and isinstance(result.output, str): return result.output
    if hasattr(result, 'content') and isinstance(result.content, str): return result.content
    return str(result)

def extract_json_str(text: str) -> str:
    text = text.strip()
    match = re.search(r"```(?:json)?\s*(\{.*?\})\s*```", text, re.DOTALL)
    if match: return match.group(1)
    match = re.search(r"(\{.*\})", text, re.DOTALL)
    if match: return match.group(1)
    return text

def parse_agent_output(raw_text: str):
    json_str = extract_json_str(raw_text)
    try:
        return TypeAdapter(AgentAction).validate_json(json_str)
    except ValidationError:
        try:
            py_dict = ast.literal_eval(json_str)
            return TypeAdapter(AgentAction).validate_json(json.dumps(py_dict))
        except:
            raise

# --- EXECUTION ENGINE ---
async def execute_agent_loop(mode: str, initial_input: str, deps: ResearchDeps, model_type: str = "smart"):
    """Execute the agent loop for scout or sniper mode.

    Args:
        mode: "SCOUT" or "SNIPER"
        initial_input: The initial prompt/input for the agent.
        deps: Research dependencies (db session).
        model_type: "fast" for high-quota model (scout), "smart" for reasoning model (sniper).
    """
    system_prompt = SCOUT_SYSTEM_PROMPT if mode == "SCOUT" else SNIPER_SYSTEM_PROMPT
    
    # --- NEGATIVE PROMPTING (Scout Only) ---
    if mode == "SCOUT":
        try:
            # We use a new session to fetch context
            async for temp_session in get_session():
                existing_names = await get_recent_strategy_names(temp_session, limit=50)
                if existing_names:
                    negative_constraint = (
                        "\n\n⛔ NEGATIVE CONSTRAINTS (Evolutionary Memory):\n"
                        "The following strategies ALREADY EXIST in our database. \n"
                        "You must NOT generate variations of these. Explore completely different concepts:\n"
                        f"[{', '.join(existing_names[:50])}]"
                    )
                    system_prompt += negative_constraint
                    logger.info(f"🧠 Injected {len(existing_names)} existing strategies into Scout memory.")
                break # Close generator
        except Exception as e:
            logger.warning(f"⚠️ Failed to inject negative/memory context: {e}")

    history = [f"USER_GOAL: {initial_input}"]
    
    max_steps = 6 if mode == "SCOUT" else 15
    
    for step in range(max_steps):
        logger.info(f"🤖 {mode} Step {step+1}/{max_steps}")
        
        history_text = "\n".join(history[-6:]) 
        full_context = f"{system_prompt}\n\n--- HISTORY ---\n{history_text}\n\nYOUR NEXT COMMAND (Return ONLY raw JSON, no text):"
        
        try:
            # Run Agent with Timeout
            result = await asyncio.wait_for(
                universal_agent.run(full_context, deps=deps), 
                timeout=600.0
            )
            raw_text = get_agent_response_text(result)
            
            try:
                command = parse_agent_output(raw_text)
                # Reset backoff on successful API response
                key_manager.reset_backoff()
            except Exception:
                logger.warning(f"⚠️  JSON Parse Failed. Asking retry.")
                history.append("SYSTEM ERROR: Invalid JSON format. Output strictly the JSON object.")
                continue
            
            # Execute Command
            if isinstance(command, SearchCommand):
                # Determine queries to execute (support both single and list)
                queries_to_run = command.queries if command.queries else ([command.query] if command.query else [])
                
                if not queries_to_run:
                    logger.warning("⚠️ SearchCommand with no queries. Skipping.")
                    history.append("SYSTEM ERROR: No query provided.")
                    continue
                
                logger.info(f"🔎 SEARCH ({len(queries_to_run)} queries): {command.tool}")
                
                # Select search function
                if command.tool == "search_general":
                    search_fn = search_general_web
                elif command.tool == "search_academic":
                    search_fn = search_academic_papers
                else:
                    search_fn = search_github_code
                
                # Execute in parallel
                results = await asyncio.gather(*[search_fn(q) for q in queries_to_run])
                
                # Format results
                result_entries = []
                for i, (q, out) in enumerate(zip(queries_to_run, results)):
                    if "No results" in out or len(out) < 50:
                        result_entries.append(f"[Query {i+1}: '{q}']\nNo results.")
                    else:
                        result_entries.append(f"[Query {i+1}: '{q}']\n{out[:1000]}...")
                
                history.append(f"CMD: {command.tool} (x{len(queries_to_run)})\nRESULTS:\n" + "\n---\n".join(result_entries))

            elif isinstance(command, ReadCommand):
                # Determine URLs to read (support both single and list)
                urls_to_read = command.urls if command.urls else ([command.url] if command.url else [])
                
                if not urls_to_read:
                    logger.warning("⚠️ ReadCommand with no URLs. Skipping.")
                    history.append("SYSTEM ERROR: No URL provided.")
                    continue
                
                logger.info(f"📖 READ ({len(urls_to_read)} URLs)")
                
                # Execute in parallel
                results = await asyncio.gather(*[read_url_content(u) for u in urls_to_read])
                
                # Format results
                result_entries = []
                for i, (u, out) in enumerate(zip(urls_to_read, results)):
                    if len(out) < 100:
                        result_entries.append(f"[URL {i+1}: '{u}']\nFailed to read.")
                    else:
                        result_entries.append(f"[URL {i+1}: '{u}']\n{out[:2000]}")
                
                history.append(f"CMD: read_content (x{len(urls_to_read)})\nRESULTS:\n" + "\n---\n".join(result_entries))

            elif isinstance(command, FinishScoutCommand):
                logger.info(f"✅ SCOUT SUCCESS: {command.result.topic}")
                return command.result

            elif isinstance(command, FinishSniperCommand):
                logger.info(f"✅ SNIPER SUCCESS: {command.result.name}")
                return command.result
                
        except asyncio.TimeoutError:
            logger.error(f"❌ TIMEOUT at Step {step+1}.")
            history.append("SYSTEM: Previous action timed out.")
            
        except Exception as e:
            err = str(e)
            # --- KEY ROTATION LOGIC ---
            if "429" in err or "quota" in err.lower() or "503" in err or "403" in err:
                logger.warning(f"⚠️  API Limit Hit ({err[:50]}...). Rotating Key...")
                
                # 1. Mark current key as exhausted
                key_manager.flag_key_limited()
                
                # 2. Get fresh key
                new_key = key_manager.get_next_key()
                
                # 3. Update Agent (preserve model type)
                update_agent_model(new_key, model_type)

                # 4. Retry loop immediately
                logger.info("🔄 Retrying step with new key...")
                continue
            else:
                logger.error(f"❌ System Error: {e}")
                history.append(f"SYSTEM ERROR: {e}")
                
    logger.warning(f"❌ {mode} Failed (Max Steps Reached).")
    return None

# --- FEEDBACK LOOP HELPER ---
async def get_recent_failures(session, limit=10):
    """Fetch recently failed/rejected strategies to avoid repeating mistakes."""
    try:
        from sqlalchemy import text
        # Fetch rejected strategies or failed backtests
        query = text("""
            SELECT name, description 
            FROM strategy 
            WHERE status IN ('REJECTED', 'FAILED') 
            ORDER BY created_at DESC 
            LIMIT :limit
        """)
        result = await session.execute(query, {'limit': limit})
        return [{"name": r.name, "desc": r.description[:150]} for r in result]
    except Exception as e:
        logger.error(f"⚠️ Failed to fetch failure context: {e}")
        return []

async def get_recent_strategy_names(session, limit: int = 50) -> List[str]:
    """Fetch recent unique strategy names for Negative Prompting."""
    try:
        from sqlalchemy import text
        # Get diverse set of names, prioritizing those with higher quality logic
        # Fixed: PostgreSQL requires ORDER BY columns in SELECT when using DISTINCT
        query = text("""
            SELECT name FROM strategy
            WHERE status != 'REJECTED'
            GROUP BY name
            ORDER BY MAX(created_at) DESC
            LIMIT :limit
        """)
        result = await session.execute(query, {'limit': limit})
        return [row[0] for row in result]
    except Exception as e:
        logger.error(f"⚠️ Failed to fetch strategy names: {e}")
        return []

# --- MAIN LOOP ---
async def run_24_7_loop():
    logger.info("🚀 SYSTEM LAUNCHED (Continuous Rotation)")
    await init_db()

    while True:
        # 1. Ensure we have a valid key before starting cycle (start with fast model for scout)
        current_key = key_manager.get_next_key()
        update_agent_model(current_key, model_type="fast")

        async for session in get_session():
            deps = ResearchDeps(db_session=session)
            
            # 2. SCOUT (With Feedback Loop)
            niche = random.choice(NICHES)
            
            # Fetch "Post-Mortem" Context
            failures = await get_recent_failures(session)
            avoid_context = ""
            if failures:
                avoid_context = "\n\n❌ AVOID REPEATING THESE RECENT FAILURES:\n" + "\n".join([f"- {f['name']}: {f['desc']}..." for f in failures])
            
            logger.info(f"\n🔭 SCOUTING: {niche}")
            
            prompt = f"Find a specific, novel trading strategy in the '{niche}' niche.{avoid_context}\n\nFocus on verifiable alpha, not generic advice."
            scout_res = await execute_agent_loop("SCOUT", prompt, deps, model_type="fast")
            
            if not scout_res:
                logger.warning("Scout failed. Skipping cycle.")
                break

            # 3. SNIPER (switch to smart model for deeper analysis)
            logger.info(f"🦅 SNIPING: {scout_res.topic}")
            sniper_key = key_manager.get_next_key()
            update_agent_model(sniper_key, model_type="smart")
            sniper_res = await execute_agent_loop("SNIPER", f"Analyze {scout_res.topic}", deps, model_type="smart")
            
            if sniper_res:
                    # --- DEDUPLICATION CHECK (Database-based) ---
                    # Check if a similar strategy already exists using embedding similarity
                    vec = embedder.encode(f"{sniper_res.name} {sniper_res.description}").tolist()
                    
                    # Query for strategies with similar embeddings (cosine similarity > 0.85)
                    from sqlalchemy import text
                    # --- MULTI-ASSET FILTER (UNSUPPORTED ARCHITECTURE) ---
                    # Our backtesting framework only supports single-asset strategies.
                    # Pair Trading / Statistical Arbitrage requires multiple assets and will fail.
                    multi_asset_keywords = ["pair trading", "pairs trading", "statistical arbitrage", 
                                            "cointegration", "correlation breakout", "spread trading",
                                            "hedge ratio", "long short pair"]
                    strategy_text = f"{sniper_res.name} {sniper_res.description}".lower()
                    
                    is_multi_asset = any(kw in strategy_text for kw in multi_asset_keywords)
                    
                    # --- DUPLICATE CHECK (Adaptive Thresholds) ---
                    # We lower the vector threshold to 0.80 but enforce strict metadata matching for candidates between 0.80-0.95
                    
                    if is_multi_asset:
                        logger.info(f"⛔ MULTI-ASSET STRATEGY DETECTED: '{sniper_res.name}'. Our framework is single-asset only. SKIPPING.")
                        break  # Skip to next cycle
                    
                    similarity_query = text("""
                        SELECT s.id, s.name, s.status, s.asset_type, s.timeframes,
                               1 - (se.embedding <=> :query_embedding) as similarity
                        FROM strategy s
                        JOIN strategyembedding se ON se.strategy_id = s.id
                        WHERE 1 - (se.embedding <=> :query_embedding) > 0.80
                        AND s.status != 'REJECTED'
                        ORDER BY similarity DESC
                        LIMIT 1
                    """)
                    
                    result = await session.execute(similarity_query, {"query_embedding": str(vec)})
                    duplicate = result.first()
                    
                    is_vector_dup = False
                    if duplicate:
                        sim = duplicate.similarity
                        # 1. High Similarity (> 0.95) -> Always Duplicate
                        if sim > 0.95:
                            is_vector_dup = True
                            logger.info(f"⚠️ HIGH SIMILARITY DUPLICATE (>0.95): '{sniper_res.name}' vs '{duplicate.name}' ({sim:.2f})")
                        
                        # 2. Medium Similarity (0.80 - 0.95) -> Check Metadata
                        elif sim > 0.80:
                            # Check Asset Type Match
                            asset_match = (duplicate.asset_type == sniper_res.asset_type)
                            
                            # Check Timeframe Overlap (if any timeframe matches)
                            # timeframes is JSON list, e.g. ["1h", "4h"]
                            dup_tf = set(duplicate.timeframes) if duplicate.timeframes else set()
                            new_tf = set(sniper_res.timeframes) if sniper_res.timeframes else set()
                            tf_match = not dup_tf.isdisjoint(new_tf) # True if overlap exists
                            
                            if asset_match and tf_match:
                                is_vector_dup = True
                                logger.info(f"⚠️ METADATA DUPLICATE (0.80-0.95): '{sniper_res.name}' vs '{duplicate.name}' ({sim:.2f}) [Asset: {asset_match}, TF: {tf_match}]")
                            else:
                                logger.info(f"✅ ALLOWED SIMILARITY ({sim:.2f}): '{sniper_res.name}' vs '{duplicate.name}' (Different Metadata)")

                    if is_vector_dup:
                        sniper_res.is_duplicate = True  # Override the agent's output
                    
                    # --- FINGERPRINT DEDUPLICATION CHECK (Logic-based) ---
                    fingerprint = compute_logic_fingerprint(sniper_res.logic_steps)
                    
                    fingerprint_query = select(Strategy).where(Strategy.logic_fingerprint == fingerprint, Strategy.status != StrategyStatus.REJECTED).limit(1)
                    fingerprint_result = await session.execute(fingerprint_query)
                    fingerprint_dup = fingerprint_result.scalars().first()
                    
                    if fingerprint_dup:
                        logger.info(f"⚠️ LOGIC DUPLICATE: '{sniper_res.name}' has same fingerprint as '{fingerprint_dup.name}' (fingerprint: {fingerprint})")
                        sniper_res.is_duplicate = True
                    
                    # --- STATUS DECISION ---
                    if sniper_res.is_duplicate:
                        logger.info(f"⚠️ Duplicate strategy '{sniper_res.name}' detected. SKIPPING SAVE to DB.")
                        break # Skip to next cycle, effectively deleting it
                        
                    elif sniper_res.quality_score < 5:
                        logger.info(f"🗑️ Low Quality ({sniper_res.quality_score}). Saving as REJECTED.")
                        status = StrategyStatus.REJECTED
                    else:
                        status = StrategyStatus.READY_FOR_CODE # Always ready if Score >= 5

                    strat_embed = StrategyEmbedding(embedding=vec)
                    
                    strat = Strategy(
                        name=sniper_res.name,
                        description=sniper_res.description,
                        logic_steps=sniper_res.logic_steps,
                        tags=sniper_res.tags,
                        source_url=sniper_res.best_source_url,
                        quality_score=sniper_res.quality_score,
                        status=status,
                        embedding_rel=strat_embed,
                        symbols=sniper_res.symbols,
                        timeframes=sniper_res.timeframes,
                        asset_type=sniper_res.asset_type,
                        logic_fingerprint=fingerprint 
                    )
                    
                    try:
                        session.add(strat)
                        await session.commit()
                        logger.info(f"💾 SAVED: {strat.name} [{status}]")
                    except Exception as e:
                        logger.error(f"❌ DB Save Failed: {e}")

            break

        # 4. ZERO DELAY (The Manager handles timing)
        # We just loop immediately. If keys are hot, Manager will sleep inside get_next_key()
        key_manager.log_usage_summary()
        logger.info(f"🔄 Cycling...")

import signal

if __name__ == "__main__":
    # Handle SIGTERM (Docker/PM2 stop signal) by converting it to KeyboardInterrupt
    signal.signal(signal.SIGTERM, signal.default_int_handler)
    try:
        asyncio.run(run_24_7_loop())
    except KeyboardInterrupt:
        logger.info("🛑 Research Agent Stopped.")
    except KeyboardInterrupt:
         logger.info(f"{Fore.YELLOW}🛑 Research Agent Stopped Gracefully.{Style.RESET_ALL}")