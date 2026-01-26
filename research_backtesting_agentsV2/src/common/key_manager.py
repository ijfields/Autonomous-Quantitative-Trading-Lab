import os
import time
import logging
from datetime import datetime
from typing import List, Dict

logger = logging.getLogger("KeyManager")

class KeyManager:
    def __init__(self, key_type: str):
        """
        Initialize with a specific pool of keys (RESEARCH or BACKTEST).
        key_type: "RESEARCH" or "BACKTEST"
        """
        env_var = f"{key_type}_KEYS"
        keys_str = os.getenv(env_var, "")
        self.keys = [k.strip() for k in keys_str.split(",") if k.strip()]

        if not self.keys:
            raise ValueError(f"CRITICAL: No keys found in .env for {env_var}")

        # Track usage times: { "AIza...": 1715000.0 }
        self.usage_history: Dict[str, float] = {k: 0.0 for k in self.keys}
        self.current_index = 0
        self.min_interval = 15.0 # Seconds between using the SAME key (Safety buffer for Gemma)

        # Exponential backoff for rate limiting
        self.consecutive_failures = 0
        self.max_backoff = 120  # Max 2 minute wait

        # Usage tracking (daily request counters)
        self.daily_requests: Dict[str, int] = {k: 0 for k in self.keys}
        self.last_reset_date = datetime.now().date()

    def _check_daily_reset(self):
        """Reset counters at midnight."""
        today = datetime.now().date()
        if today > self.last_reset_date:
            logger.info(f"📊 Daily reset. Yesterday's usage: {self.daily_requests}")
            self.daily_requests = {k: 0 for k in self.keys}
            self.last_reset_date = today

    def get_next_key(self) -> str:
        """
        Smart Rotation:
        1. Checks the next key in line.
        2. If it was used too recently, calculates exactly how long to sleep.
        3. Returns the key ready for use.
        """
        self._check_daily_reset()

        # Round-robin selection
        key = self.keys[self.current_index]
        
        # Check cooldown
        last_used = self.usage_history[key]
        now = time.time()
        time_since_use = now - last_used
        
        if time_since_use < self.min_interval:
            wait_time = self.min_interval - time_since_use
            logger.info(f"⏳ Key #{self.current_index+1} needs cool-down. Sleeping {wait_time:.1f}s...")
            time.sleep(wait_time)
        
        # Mark as used NOW
        self.usage_history[key] = time.time()

        # Increment daily usage counter
        self.daily_requests[key] += 1

        # Advance index for next time
        self.current_index = (self.current_index + 1) % len(self.keys)

        return key

    def flag_key_limited(self):
        """
        Call this if a 429/Quota error happens.
        Implements exponential backoff to handle rate limits gracefully.
        """
        self.consecutive_failures += 1
        backoff = min(2 ** self.consecutive_failures, self.max_backoff)
        logger.warning(f"⚠️  Key #{self.current_index+1} hit a limit! Backing off {backoff}s (failure #{self.consecutive_failures})...")
        time.sleep(backoff)

    def reset_backoff(self):
        """Reset the backoff counter after a successful API call."""
        if self.consecutive_failures > 0:
            logger.info(f"✅ Resetting backoff counter (was {self.consecutive_failures})")
            self.consecutive_failures = 0

    def get_usage_stats(self) -> dict:
        """Return current usage stats for logging."""
        self._check_daily_reset()
        return {
            f"key_{i+1}": {
                "requests_today": count,
                "key_preview": k[:10] + "..."
            }
            for i, (k, count) in enumerate(self.daily_requests.items())
        }

    def log_usage_summary(self):
        """Log a summary of current usage."""
        stats = self.get_usage_stats()
        total = sum(s["requests_today"] for s in stats.values())
        logger.info(f"📊 API Usage: {total} total requests today | {stats}")