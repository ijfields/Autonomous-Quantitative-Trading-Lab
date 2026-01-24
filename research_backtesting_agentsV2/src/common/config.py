"""
Centralized Configuration Module
================================
All project paths and settings in one place.
Uses environment variables with sensible defaults.
"""

import os
from pathlib import Path

# --- PROJECT ROOT ---
# Priority: 1. Environment variable, 2. Auto-detect from this file's location
_env_root = os.getenv("PROJECT_ROOT")
if _env_root:
    PROJECT_ROOT = Path(_env_root)
else:
    # Auto-detect: This file is at src/common/config.py
    # Project root is 3 levels up
    PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent

# --- DIRECTORIES ---
DATA_CACHE_DIR = PROJECT_ROOT / "data_cache"
LOGS_DIR = PROJECT_ROOT / "logs"
TEMP_BACKTEST_DIR = PROJECT_ROOT / "temp_backtests"

# Ensure directories exist
DATA_CACHE_DIR.mkdir(exist_ok=True)
LOGS_DIR.mkdir(exist_ok=True)
TEMP_BACKTEST_DIR.mkdir(exist_ok=True)

# --- SCRIPTS ---
VENV_PYTHON = PROJECT_ROOT / "venv" / "bin" / "python"
RESET_SCRIPT = PROJECT_ROOT / "reset_strategy.py"
RESET_DB_SCRIPT = PROJECT_ROOT / "reset_db.py"

# --- API KEYS ---
# These are loaded from .env, not hardcoded
RESEARCH_KEYS = [k.strip() for k in os.getenv("RESEARCH_KEYS", "").split(",") if k.strip()]
BACKTEST_KEYS = [k.strip() for k in os.getenv("BACKTEST_KEYS", "").split(",") if k.strip()]

# --- MODEL SETTINGS ---
MODEL_FAST = os.getenv("MODEL_FAST", "gemma-3-27b-it")
MODEL_SMART = os.getenv("MODEL_SMART", "gemma-3-27b-it")

# --- DATABASE ---
DATABASE_URL = os.getenv("DATABASE_URL", "postgresql+asyncpg://myuser:mypassword@localhost:5432/trading_db")

# --- EXTERNAL SERVICES ---
SEARXNG_BASE_URL = os.getenv("SEARXNG_BASE_URL", "http://localhost:8081/")
