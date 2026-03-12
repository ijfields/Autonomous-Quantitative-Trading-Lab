# Step-by-Step Guide: Moon Dev Shorts Collection — Key Insights

**Source:** Moon Dev (YouTube)
**Format:** 8 YouTube Shorts compiled

---

## What This Guide Covers

Key technical insights from 8 Moon Dev shorts: liquidation momentum concept, guardian agent design, Hyperliquid HIP-3 observations, funding rate math, and SDK bug fixes.

---

## Insight 1: Short Liquidation Momentum Entry (meEKcRb7NGY)

1. Check hourly trend direction (up or down)
2. Look at how many short positions are clustered above current price
3. If enough shorts are stacked in the trend direction → enter long
4. Thesis: liquidation cascade creates momentum in the trend direction
5. Can also trade liquidations as reversal signals (more complex)

---

## Insight 2: Guardian Agent for RAM Management (wLYRPFSkqJo)

1. Build a lightweight Python daemon (`guardian_agent.py`)
2. Monitor CPU/RAM/swap every 30 seconds
3. Track per-process memory (especially Python child processes)
4. Send graduated alerts at 85% RAM threshold
5. "Smart kill" lowest-priority processes first (protect live trading, kill old backtests)

---

## Insight 3: HIP-3 Commodity Opportunities (-fBrJX9Wrrc, HZLuFGKt9SM)

1. Hyperliquid HIP-3 now supports oil, silver, gold, stablecoins
2. Oil hit $346M overnight volume — proving real adoption
3. During crypto bear markets, HIP-3 commodities always have something trending
4. Port existing crypto trend-following bots to HIP-3 markets

---

## Insight 4: Hyperliquid Funding Rate Math (tD4REh8dWNA)

1. Hyperliquid uses **1-hour** funding rates (NOT 8-hour like Binance)
2. Correct annualization: 0.0245% hourly = **214.39%** annualized
3. 162% funding = "everybody is long" → crowded-trade signal
4. Always verify the funding period before calculating annualized rates

---

## Insight 5: HIP-3 Price Rounding Bug Fix (2-6jlorQRdk)

1. Hyperliquid SDK rounds to 5 significant figures by default
2. HIP-3 assets need custom rounding: `h3_price_to_order_price`
3. Without fix: limit orders fall below minimum notional → rejected
4. Patch three functions: `h3_price_to_order_price`, `h3_limit_order`, `h3_lick_momentum`

---

## Key Takeaway

> Build AI agents for every repetitive task. For trading specifically: test with real slippage from the start (remove paper mode), follow the Research → Backtest → Incubate pipeline, and ruthlessly delete underperforming strategies — it's a numbers game.

*Guide derived from 8 Moon Dev YouTube Shorts transcripts*
