import os
import pandas as pd
import yfinance as yf
import ccxt
import logging
from pathlib import Path
from datetime import datetime, timedelta

# Use absolute path based on project root (resolves correctly in subprocesses)
_PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent.parent
DATA_CACHE_DIR = _PROJECT_ROOT / "data_cache"
DATA_CACHE_DIR.mkdir(exist_ok=True)

logger = logging.getLogger("DataLoader")

# Production-Ready Data Limits (based on statistical significance)
# Format: (target_days, chunk_size_days, min_candles, rationale)
SMART_DATA_LIMITS = {
    "1m": (1, 0.2, 500, "Scalping: Recent data most relevant, fast regime changes"),
    "5m": (7, 1.0, 500, "Intraday: 1 week provides ~2000 candles"),
    "15m": (15, 3.0, 500, "Short-term: 2 weeks = ~1400 candles"),
    "30m": (30, 6.0, 500, "Medium intraday: 1 month optimal balance"),
    "1h": (60, 12.0, 500, "Medium-term: 2 months = ~1400 candles"),
    "4h": (180, 50.0, 300, "Swing: 6 months = ~1000 candles"),
    "1d": (365, 300, 200, "Position: 1 year minimum for trend analysis"),
}

# Yahoo Finance Limits (based on API capabilities)
# Format: (max_lookback_days, chunk_size_days)
YF_INTERVAL_LIMITS = {
    "1m": (7, 1),        # 1-min: Max 7 days, chunk 1 day at a time
    "2m": (60, 5),       # 2-min: Max 60 days, chunk 5 days
    "5m": (60, 5),       # 5-min: Max 60 days, chunk 5 days
    "15m": (60, 10),     # 15-min: Max 60 days, chunk 10 days
    "30m": (60, 15),     # 30-min: Max 60 days, chunk 15 days
    "90m": (60, 15),     # 90-min: Max 60 days, chunk 15 days
    "1h": (730, 30),     # 1-hour: Max 730 days (2 years), chunk 30 days
    "4h": (730, 60),     # 4-hour: Max 730 days (2 years), chunk 60 days
    "1d": (36500, 3650), # Daily: Effectively unlimited, chunk 10 years
}



# Try to import Coinbase SDK
try:
    from coinbase.rest import RESTClient as CoinbaseClient
    COINBASE_AVAILABLE = True
except ImportError:
    COINBASE_AVAILABLE = False
    logger.warning("⚠️ Coinbase SDK not installed. Using CCXT for crypto.")



class DataLoader:
    def __init__(self):
        self.ccxt_exchange = ccxt.binance()
        self.coinbase_client = None
        
        # Initialize Coinbase if credentials available
        if COINBASE_AVAILABLE:
            api_key = os.getenv("COINBASE_API_KEY")
            api_secret = os.getenv("COINBASE_API_SECRET")
            if api_key and api_secret:
                try:
                    self.coinbase_client = CoinbaseClient(api_key=api_key, api_secret=api_secret)
                    logger.info("✅ Coinbase API initialized successfully")
                except Exception as e:
                    logger.warning(f"⚠️ Coinbase init failed: {e}. Using CCXT fallback.")

    def _map_timeframe(self, tf: str) -> str:
        """normalize timeframe string for YF/CCXT"""
        tf = tf.lower()
        mapping = {
            "1min": "1m", "1minute": "1m",
            "5min": "5m", "5minute": "5m",
            "15min": "15m", "15minute": "15m", 
            "30min": "30m", "30minute": "30m",
            "1hour": "1h", "hour": "1h", "hr": "1h",
            "4hour": "4h", "4hr": "4h",
            "daily": "1d", "day": "1d", "d": "1d",
            "weekly": "1wk", "week": "1wk", "w": "1wk",
            "monthly": "1mo", "month": "1mo", "m": "1mo"
        }
        return mapping.get(tf, tf)
    
    def _map_coinbase_granularity(self, tf: str) -> str:
        """Map timeframe to Coinbase granularity string."""
        mapping = {
            "1m": "ONE_MINUTE",
            "5m": "FIVE_MINUTE",
            "15m": "FIFTEEN_MINUTE",
            "30m": "THIRTY_MINUTE",
            "1h": "ONE_HOUR",
            "2h": "TWO_HOUR",
            "6h": "SIX_HOUR",
            "4h": "ONE_HOUR",  # Coinbase doesn't have 4h, use 1h and resample
            "1d": "ONE_DAY",
        }
        return mapping.get(tf, "ONE_HOUR")

    def _filter_dates(self, df: pd.DataFrame, start_date: str = None, end_date: str = None) -> pd.DataFrame:
        """Apply date range filtering to DataFrame."""
        if df.empty or (not start_date and not end_date):
            return df
            
        # Ensure index is sorted
        df.sort_index(inplace=True)
        
        if start_date:
            df = df[df.index >= pd.Timestamp(start_date)]
        
        if end_date:
            df = df[df.index <= pd.Timestamp(end_date)]
            
        return df

    def fetch_data(self, symbol: str, timeframe: str, asset_type: str = "crypto", days: int = 365, start_date: str = None, end_date: str = None) -> pd.DataFrame:
        """
        Standardized fetcher with 'Shrink Ray' normalization.
        - Crypto: Coinbase (primary) -> CCXT (fallback) -> YF (last resort)
        - Forex: YFinance
        - Stocks: YFinance
        
        Args:
            start_date: Optional ISO date string (YYYY-MM-DD) to filter start
            end_date: Optional ISO date string (YYYY-MM-DD) to filter end
        """
        # 0. Normalize Inputs
        timeframe = self._map_timeframe(timeframe)
        
        safe_sym = symbol.replace("/", "").replace("-", "")
        cache_file = DATA_CACHE_DIR / f"{asset_type}_{safe_sym}_{timeframe}.parquet"
        
        df = pd.DataFrame()

        # 1. CHECK CACHE
        if cache_file.exists():
            last_modified = datetime.fromtimestamp(cache_file.stat().st_mtime)
            if datetime.now() - last_modified < timedelta(hours=24):
                logger.info(f"⚡ Cache Hit: {symbol}")
                try:
                    df = pd.read_parquet(cache_file)
                    return self._filter_dates(df, start_date, end_date)
                except:
                    pass

        # 2. DOWNLOAD
        logger.info(f"⬇️ API Download: {symbol} ({timeframe})")
        try:
            if asset_type == "crypto":
                # Priority 1: Coinbase
                if self.coinbase_client:
                    try:
                        df = self._fetch_crypto_coinbase(symbol, timeframe, days)
                        if not df.empty:
                            logger.info(f"✅ Coinbase: fetched {len(df)} candles for {symbol}")
                        else:
                            raise ValueError("Empty Coinbase DataFrame")
                    except Exception as e:
                        logger.warning(f"⚠️ Coinbase failed for {symbol}: {e}. Trying CCXT...")
                        df = pd.DataFrame()
                
                # Priority 2: CCXT Binance
                if df.empty:
                    try:
                        df = self._fetch_crypto_ccxt(symbol, timeframe, days)
                        if df.empty: raise ValueError("Empty CCXT DataFrame")
                        logger.info(f"✅ CCXT: fetched {len(df)} candles for {symbol}")
                    except Exception as e:
                        logger.warning(f"⚠️ CCXT failed for {symbol}: {e}. Fallback to YF.")
                        yf_sym = symbol.replace("/", "-").replace("USDT", "USD")
                        df = self._fetch_stock(yf_sym, timeframe, days)
                    
            elif asset_type == "forex":
                # Convert EUR/USD -> EURUSD=X
                yf_sym = symbol.replace("/", "") + "=X"
                logger.info(f"💱 Normalizing Forex Ticker: {symbol} -> {yf_sym}")
                df = self._fetch_stock(yf_sym, timeframe, days)
            else:
                # Stock
                df = self._fetch_stock(symbol, timeframe, days)
            
            if not df.empty:
                df.columns = [c.capitalize() for c in df.columns]
                df.dropna(inplace=True)
                
                # Normalize Timezone (Fix for YF/Crypto mismatch)
                if df.index.tz is not None:
                    df.index = df.index.tz_localize(None)
                
                # --- TIMESTAMP VALIDATION (Harvard Improvement) ---
                if hasattr(df.index, 'max'):
                    latest_ts = df.index.max()
                    if pd.notna(latest_ts):
                        now = datetime.now()
                        if latest_ts > now + timedelta(hours=24):
                            logger.warning(f"⚠️ Future timestamps detected ({latest_ts} > now). Possible API bug!")
                        elif latest_ts < now - timedelta(days=7):
                            logger.warning(f"⚠️ Stale data detected (latest: {latest_ts}). Data may be outdated.")
                            
                # Save to cache
                if len(df) > 50:
                    df.to_parquet(cache_file)
            
            return self._filter_dates(df, start_date, end_date)
            
        except Exception as e:
            logger.error(f"❌ Data Error ({symbol}): {e}")
            return pd.DataFrame()

    def _fetch_stock(self, symbol: str, timeframe: str, days: int) -> pd.DataFrame:
        """Production Yahoo Finance fetcher with chunking and resume capability.
        
        Features:
        - Respects YF API limits per interval
        - Chunks large requests for stability
        - Rate limiting to avoid throttling
        - Smart defaults from interval config
        """
        import time
        
        # Get interval limits
        if timeframe in YF_INTERVAL_LIMITS:
            max_lookback, chunk_days = YF_INTERVAL_LIMITS[timeframe]
            days = min(days, max_lookback)
            logger.info(f"📊 YF {timeframe}: Capped to {days} days (max: {max_lookback})")
        else:
            # Unknown interval, use conservative defaults
            chunk_days = 30
            days = min(days, 60)
        
        # Calculate date range
        end_date = datetime.now()
        start_date = end_date - timedelta(days=days)
        
        all_chunks = []
        current_start = start_date
        
        try:
            # Chunk download loop
            while current_start < end_date:
                chunk_end = min(current_start + timedelta(days=chunk_days), end_date)
                
                # YF requires start < end
                if chunk_end <= current_start:
                    break
                
                logger.debug(f"📥 YF chunk: {current_start.date()} to {chunk_end.date()}")
                
                # Download chunk
                chunk_df = yf.download(
                    symbol, 
                    start=current_start, 
                    end=chunk_end, 
                    interval=timeframe, 
                    progress=False, 
                    threads=False
                )
                
                if not chunk_df.empty:
                    # Handle MultiIndex columns (happens with some symbols)
                    if isinstance(chunk_df.columns, pd.MultiIndex):
                        chunk_df.columns = chunk_df.columns.get_level_values(0)
                    
                    all_chunks.append(chunk_df)
                
                current_start = chunk_end
                
                # Rate limiting: longer sleep for heavy intervals
                if current_start < end_date:
                    sleep_time = 1.5 if timeframe in ["1m", "2m"] else 0.3
                    time.sleep(sleep_time)
            
            if not all_chunks:
                logger.warning(f"⚠️ YF returned no data for {symbol} @ {timeframe}")
                return pd.DataFrame()
            
            # Combine all chunks
            df = pd.concat(all_chunks)
            
            # Ensure we have Close column
            if "Close" not in df.columns and "Adj Close" in df.columns:
                df["Close"] = df["Adj Close"]
            
            # Select standard OHLCV columns
            required_cols = ["Open", "High", "Low", "Close", "Volume"]
            df = df[required_cols]
            
            logger.info(f"✅ YFinance: Fetched {len(df)} candles for {symbol} ({timeframe})")
            return df
            
        except Exception as e:
            logger.error(f"❌ YF Download Failed for {symbol}: {e}")
            return pd.DataFrame()

    def _fetch_crypto_coinbase(self, symbol: str, timeframe: str, days: int) -> pd.DataFrame:
        """Production-ready Coinbase fetcher with chunking and smart limits.
        
        Features:
        - Respects 300-candle API limit via chunking
        - Smart defaults based on timeframe
        - Rate limiting (3 req/sec)
        - Proper error handling with fallback
        """
        import time
        
        # Convert BTC/USDT -> BTC-USD (Coinbase format)
        cb_symbol = symbol.replace("/USDT", "-USD").replace("/", "-")
        granularity = self._map_coinbase_granularity(timeframe)
        
        # Get smart defaults for this timeframe
        if timeframe in SMART_DATA_LIMITS:
            target_days, chunk_days, min_candles, reason = SMART_DATA_LIMITS[timeframe]
            days = min(days, target_days)  # Cap to recommended max
            logger.info(f"📊 Using smart limit for {timeframe}: {days} days ({reason})")
        else:
            chunk_days = 10  # Default fallback
        
        # Calculate time range
        end_time = datetime.now()
        start_time = end_time - timedelta(days=days)
        
        all_candles = []
        current_start = start_time
        
        try:
            # Chunk requests to stay under 300-candle limit
            while current_start < end_time:
                current_end = min(current_start + timedelta(days=chunk_days), end_time)
                
                chunk_start_ts = int(current_start.timestamp())
                chunk_end_ts = int(current_end.timestamp())
                
                logger.debug(f"📥 Fetching chunk: {current_start.strftime('%Y-%m-%d')} to {current_end.strftime('%Y-%m-%d')}")
                
                response = self.coinbase_client.get_candles(
                    product_id=cb_symbol,
                    start=str(chunk_start_ts),
                    end=str(chunk_end_ts),
                    granularity=granularity
                )
                
                if response and hasattr(response, 'candles') and response.candles:
                    for candle in response.candles:
                        all_candles.append({
                            "Date": datetime.fromtimestamp(int(candle.start)),
                            "Open": float(candle.open),
                            "High": float(candle.high),
                            "Low": float(candle.low),
                            "Close": float(candle.close),
                            "Volume": float(candle.volume)
                        })
                
                current_start = current_end
                
                # Rate limiting: ~3 req/sec (Coinbase allows 5/sec for private endpoints)
                if current_start < end_time:
                    time.sleep(0.35)
            
            if not all_candles:
                logger.warning(f"⚠️ Coinbase returned no candles for {symbol}")
                return pd.DataFrame()
            
            # Convert to DataFrame
            df = pd.DataFrame(all_candles)
            df.set_index("Date", inplace=True)
            df.sort_index(inplace=True)
            
            # Resample if needed (e.g., 4h from 1h)
            if timeframe == "4h" and granularity == "ONE_HOUR":
                df = df.resample("4h").agg({
                    "Open": "first",
                    "High": "max",
                    "Low": "min",
                    "Close": "last",
                    "Volume": "sum"
                }).dropna()
            
            logger.info(f"✅ Coinbase: Fetched {len(df)} candles for {symbol} ({timeframe})")
            return df
            
        except Exception as e:
            logger.warning(f"⚠️ Coinbase failed for {symbol}: {e}")
            return pd.DataFrame()

    def _fetch_crypto_ccxt(self, symbol: str, timeframe: str, days: int) -> pd.DataFrame:
        """Fetch crypto data from CCXT (Binance) with Robust Fallbacks."""
        # 1. Normalize Timeframe common aliases
        tf_map = {"H1": "1h", "H4": "4h", "D1": "1d", "M5": "5m", "M15": "15m", "M30": "30m"}
        timeframe = tf_map.get(timeframe.upper(), timeframe)

        # 2. Normalize Symbol variations
        original_symbol = symbol
        symbol = symbol.upper().replace("-", "/") # BTC-USDT -> BTC/USDT
        
        # 3. Define candidates to try (e.g. BTC/USDT, BTCUSDT)
        candidates = [symbol]
        if "/" not in symbol and "USDT" in symbol:
            candidates.append(symbol.replace("USDT", "/USDT"))
        if "/" in symbol:
            candidates.append(symbol.replace("/", "")) # BTC/USDT -> BTCUSDT

        ohlcv = []
        used_symbol = symbol

        since = self.ccxt_exchange.parse8601((datetime.now() - timedelta(days=days)).isoformat())

        for cand in candidates:
            try:
                # logger.info(f"Trying symbol: {cand}")
                ohlcv = self.ccxt_exchange.fetch_ohlcv(cand, timeframe, since=since)
                if ohlcv:
                    used_symbol = cand
                    break
            except Exception as e:
                # logger.debug(f"Failed to fetch {cand}: {e}")
                continue
        
        if not ohlcv:
            # If all failed, raise known error
            logger.error(f"❌ DATA FAILURE: Could not find data for {original_symbol} (tried {candidates}) on timeframe {timeframe}")
            return pd.DataFrame()

        df = pd.DataFrame(ohlcv, columns=["Date", "Open", "High", "Low", "Close", "Volume"])
        df["Date"] = pd.to_datetime(df["Date"], unit="ms")
        df.set_index("Date", inplace=True)
        return df