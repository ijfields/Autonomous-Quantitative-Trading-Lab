# Strategy Brief: Hyperliquid Funding Rate Scanner

## Source
- **Video:** Hidden Trading Bot Signal No One Looks At
- **Channel:** Moon Dev
- **Speaker:** Moon Dev
- **Video ID:** PNKidibnzRU
- **Upload Date:** 2026-03-06
- **Timestamp:** Full video (~11m)

---

## Strategy Overview

| Field | Value |
|-------|-------|
| Name | Hyperliquid Funding Rate Scanner |
| Type | sentiment / mean_reversion |
| Style | swing_trade / position_trade |
| Asset | All Hyperliquid perps (crypto + HIP3 stocks/futures/forex) |
| Timeframe | Hourly (funding rate update frequency) |
| Direction | Contrarian (fade extreme imbalance) |
| Risk-Reward | Undefined (signal only, no complete entry/exit framework) |
| Confidence | 0.50 |
| Transcript Quality | medium (conceptual explanation with code walkthrough, no backtested results) |
| Automation Feasibility | HIGH |

---

## Core Concept

Monitor Hyperliquid's funding rates across all instruments. Extreme positive funding (>+200% annualized) indicates the market is long-heavy and "begging for shorts." Extreme negative funding (<-200% annualized) indicates short-heavy and "begging for longs." Use these imbalance readings as a contrarian sentiment signal for trading bots.

**Unique edge:** Wall Street does not have access to funding rate data on traditional instruments. HIP3 brings stocks, futures, and forex onto Hyperliquid, creating a novel data source for assets that have never had this type of sentiment indicator.

---

## Entry Logic

### Signal 1: Extreme Funding Rate
- **Data:** Hyperliquid funding rate (hourly, annualized)
- **Long signal:** Funding rate < -200% annualized (shorts paying longs, market begging for longs)
- **Short signal:** Funding rate > +200% annualized (longs paying shorts, market begging for shorts)
- **Normal range (no signal):** -100% to +100% annualized

### Signal 2: Open Interest Context (suggested)
- **Data:** Total open positions on Hyperliquid
- **Filter:** Higher OI = more meaningful signal (>$50M OI preferred)
- **Note:** Some HIP3 instruments have only $11M OI — less reliable

### Signal 3: Confluence (not defined by source)
- Source does NOT provide specific entry rules
- Suggests using funding rate as one input among many
- Price action, volume, and technical analysis should complement

---

## Exit Logic

Not defined by source. This is a **signal/scanner** rather than a complete trading strategy.

---

## Risk Management

| Parameter | Value |
|-----------|-------|
| Risk per trade | Not defined |
| Stop-loss | Not defined |
| Position sizing | Not defined |
| Max concurrent positions | Not defined |

---

## Filters

1. **Extreme readings only** — ±200%+ annualized to avoid noise
2. **OI threshold** — prefer instruments with higher open interest
3. **Rate stability** — extreme rates don't persist; enter quickly or miss the signal

---

## Missing / Unclear Elements

- **No entry/exit rules** — this is a scanner, not a complete strategy
- **No backtesting results** — conceptual explanation only
- **No position sizing** — no risk management framework
- **No holding period** — unclear how long to hold contrarian positions
- **No stop-loss methodology** — no defined risk parameters
- **Volume concerns** — HIP3 instruments have low volume vs. traditional exchanges
- **Rate persistence** — how long extreme rates typically last before reverting is not discussed
- **Correlation with price** — no statistical analysis of funding rate → price direction correlation

---

## Lumibot / Backtest Implementation Notes

| Consideration | Assessment |
|---------------|-----------:|
| Data availability | MEDIUM — Hyperliquid API provides funding rates; MunDev AI API offers enhanced access |
| Backtesting feasibility | LOW — No defined entry/exit rules to backtest; would need to design a complete strategy around the signal |
| Automatable components | Scanner (funding rate retrieval, sorting, alerting on extremes) |
| Discretionary components | ALL trading decisions (entry, exit, sizing, risk management) |
| Key challenge | Converting a sentiment signal into a backtestable strategy with defined rules |
| Suggested approach | Build scanner first → collect data → analyze correlation between extreme funding rates and subsequent price moves → design entry/exit rules based on empirical data |

---

## Source Quotes

> "Wall Street doesn't have this and I think it's one of crypto's most powerful kind of hidden signals."

> "If it's negative 200%, I feel like it's low-key begging people to long."

> "Finally, retail is starting to get an edge here on Wall Street."

*Strategy extracted from: Hidden Trading Bot Signal No One Looks At.txt*
