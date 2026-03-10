# Hidden Trading Bot Signal No One Looks At — Complete Transcript Analysis

**Video Title:** Hidden Trading Bot Signal No One Looks At
**Channel:** Moon Dev
**Video ID:** PNKidibnzRU
**Upload Date:** 2026-03-06
**Duration:** ~11m (~665s)
**Speaker:** Moon Dev
**Platform:** YouTube

---

## EXECUTIVE SUMMARY

Moon Dev introduces the Hyperliquid funding rate as a powerful hidden signal for trading bots — one that traditional Wall Street doesn't have access to. He explains how funding rates work on perpetual exchanges (longs pay shorts when positive, shorts pay longs when negative), demonstrates a funding rate scanner he built that shows extreme readings across all Hyperliquid assets (crypto and the new HIP3 stocks/futures/forex), and provides the code via his algo trading roadmap. Key insight: extreme funding rates (e.g., -200% or +200% annualized) indicate market imbalance that can be exploited. The scanner covers both crypto perps and the newly launched HIP3 traditional market instruments.

---

## KEY TOPICS

### What is the Funding Rate?
- A fee paid between longs and shorts on perpetual exchanges (no expiration futures)
- On Hyperliquid: paid every 1 hour
- **Positive funding:** Longs pay shorts (market is long-heavy, "begging for shorts")
- **Negative funding:** Shorts pay longs (market is short-heavy, "begging for longs")
- Normal range (BTC): ~10% annualized
- Extreme readings: ±200%+ annualized = significant imbalance

### Why This is Unique
- **Wall Street doesn't have this** — funding rates are a crypto-native mechanism from perpetual exchanges
- Only available on Hyperliquid and similar perp DEXes
- Shows real-time sentiment: how many longs vs. shorts
- Open interest data also available (another metric Wall Street can't see)

### HIP3: Stocks/Futures/Forex on Hyperliquid
- Hyperliquid recently added traditional market instruments
- Stocks, futures, and forex now tradeable on-chain
- These instruments ALSO have funding rates — unique data that doesn't exist on NYSE, IBKR, etc.
- Example shown: Oil at -200% to +200% swings during wartime

### The Funding Rate Scanner
- Built by Moon Dev, code shared on algo trading roadmap
- Scans all Hyperliquid assets for highest and lowest funding rates
- Outputs annualized funding rate for each asset
- Examples shown:
  - Natural Gas: +161% (majority long, begging for shorts)
  - Unknown asset: -631% (extreme short pressure, longs earning massively)
  - Oil: swinging between -200% and +200%

### Caveats
- Lower volume on HIP3 than NYSE — sentiment signal may be noisier
- Extreme funding rates don't stay stable — can't just buy and earn 631%/year
- It's a signal/data source, not a guaranteed trade
- Open interest on some HIP3 instruments is only ~$11M

### Moon Dev Ecosystem
- Code available at: algo trading roadmap (mundave.com/roadmap)
- Hyperliquid data layer API available to Zoom participants
- Daily live Zoom calls for Q&A and code sharing
- MunDev AI data sources include ~30 different data feeds including funding rates

---

## TOOLS & PLATFORMS MENTIONED

| Tool/Platform | Purpose |
|---------------|---------|
| Hyperliquid | Perpetual DEX with funding rates |
| HIP3 | Hyperliquid's stock/futures/forex instruments |
| Funding Rate Scanner | Moon Dev's custom tool (code shared) |
| MunDev AI API | Data layer for Hyperliquid (tick data, liquidations, etc.) |
| mundave.com/roadmap | Code repository / algo trading roadmap |
| mundave.com/docs | API documentation for MunDev AI |

---

## STRATEGY EXTRACTED

**Hyperliquid Funding Rate Scanner**

| Parameter | Value |
|-----------|-------|
| Type | Sentiment / mean_reversion |
| Style | Swing / position |
| Asset | All Hyperliquid perps (crypto + HIP3 stocks/futures/forex) |
| Signal | Extreme funding rate readings (±200%+ annualized) |
| Direction | Contrarian (extreme negative → consider long; extreme positive → consider short) |
| Data frequency | Hourly funding rate updates |
| Confidence | 0.50 (signal only, no complete strategy defined) |
| Automation feasibility | HIGH (API data available, scanner code provided) |

---

## ACTIONABLE TAKEAWAYS

1. **Funding rates are a unique crypto-native signal** that traditional markets don't offer
2. **Extreme readings indicate imbalance** — ±200%+ annualized = market is "begging" for the other side
3. **HIP3 extends this signal to stocks/futures/forex** — novel data that doesn't exist on traditional exchanges
4. **Build a scanner** to monitor all assets for extreme funding rate readings
5. **Use as one input among many** — not a standalone trade signal
6. **Watch open interest alongside funding rates** — both are crypto-unique sentiment indicators

---

## SOURCE QUOTES

> "Wall Street doesn't have this and I think it's one of crypto's most powerful kind of hidden signals that nobody really understands."

> "If it's negative 200%, I feel like it's low-key begging [people to long]."

> "The last 700,000 years that the stock market has been opened, we never had access to this."

> "Finally, retail is starting to get an edge here on Wall Street."

*Analysis derived from: Hidden Trading Bot Signal No One Looks At.txt*
