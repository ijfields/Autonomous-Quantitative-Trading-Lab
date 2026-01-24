import os
import time
import logging
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

    def get_next_key(self) -> str:
        """
        Smart Rotation:
        1. Checks the next key in line.
        2. If it was used too recently, calculates exactly how long to sleep.
        3. Returns the key ready for use.
        """
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
        
        # Advance index for next time
        self.current_index = (self.current_index + 1) % len(self.keys)
        
        return key

    def flag_key_limited(self):
        """
        Call this if a 429/Quota error happens. 
        It forces the manager to skip to the next key immediately.
        """
        logger.warning(f"⚠️  Key #{self.current_index+1} hit a limit! Skipping...")
        # Since we incremented index in get_next_key, we are effectively 
        # already pointing to the next one for the next call. 
        # We just add a small penalty delay to the system to let things settle.
        time.sleep(2)