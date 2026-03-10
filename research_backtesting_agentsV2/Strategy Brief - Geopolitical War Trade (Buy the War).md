# Strategy Brief: Geopolitical War Trade (Buy the War)

## Source
- **Video:** Claude Chrome Built My WW3 Trading Bot
- **Channel:** Moon Dev
- **Speakers:** Moon Dev
- **Video ID:** NORE7LoTxzY
- **Upload Date:** 2026-03-04
- **Timestamp:** Full livestream (~1h32m)

---

## Strategy Overview

| Field | Value |
|-------|-------|
| Name | Geopolitical War Trade (Buy the War) |
| Type | macro / event-driven |
| Style | Contrarian long during geopolitical conflict |
| Asset | Oil (USO), Gold (GLD), Natural Gas (UNNG/UNG), BTC |
| Timeframe | Days to weeks (event duration) |
| Direction | Long-biased |
| Risk-Reward | Asymmetric — options for defined risk, commodity upside |
| Confidence | 0.55 |
| Transcript Quality | medium (livestream format, conversational, multi-topic) |
| Automation Feasibility | LOW |

---

## Core Concept

During geopolitical conflicts (wars, military escalations), commodities and safe havens spike. The "buy the war" pattern has a 74% historical success rate — markets initially panic, then recover or continue higher on supply disruption fears. Use Hyperliquid HIP3 positioning data (unique liquidation visibility) and Polymarket prediction odds to time entries and gauge conviction.

**Philosophy:** "Buy the war works 74% of the time. Historically, you buy the fear."

---

## Entry Logic

### Primary Signals
1. **Geopolitical escalation event** — war, military strikes, sanctions
2. **HIP3 extreme positioning** — >70% of traders short on affected commodity = contrarian long
3. **Polymarket ceasefire odds** — <30% ceasefire probability = conflict has runway

### Asset Selection
| Asset | When to Enter | Vehicle |
|-------|--------------|---------|
| Oil | Immediate (first mover) | USO calls |
| Gold | Immediate (safe haven) | GLD calls |
| Natural Gas | Delayed (lagging mover) | UNNG/UNG calls |
| BTC | After initial selloff recovers | Direct or futures |

### Entry Timing
- Oil and gold: Enter within 24-48 hours of escalation
- Natural gas: Watch for 3-7 day lag — enter when price hasn't moved but thesis is intact
- BTC: Wait for initial risk-off selling to stabilize

---

## Exit Logic

1. **Ceasefire probability rises >50%** on Polymarket → start taking profits
2. **HIP3 positioning normalizes** (short squeeze plays out) → exit commodity positions
3. **Gold premium exceeds 2-sigma historical range** → trim
4. **Conflict de-escalation confirmed** in news → exit all war trades
5. **Time-based:** Options expiration forces exit if thesis hasn't played out

---

## Risk Management

| Parameter | Value |
|-----------|-------|
| Position sizing | Smaller than normal — event-driven = binary risk |
| Vehicle | Options preferred (defined risk) over futures (unlimited risk) |
| Max portfolio allocation | 10-15% total across all war trades |
| Stop loss | Option premium loss (defined by trade) |
| Correlation risk | All war trades are correlated — a ceasefire kills all positions simultaneously |

---

## Filters

1. **HIP3 positioning** — must show >70% one-directional bias for contrarian signal
2. **Polymarket odds** — ceasefire probability <30% for entry, >50% for exit
3. **News sentiment** — escalation confirmed across multiple sources (not just rumors)
4. **Historical pattern** — verify the specific conflict type matches "buy the war" historical precedent
5. **Liquidity check** — ensure sufficient options volume on chosen ETFs

---

## Missing / Unclear Elements

- **Exact historical backtest** — 74% win rate cited but no formal study reference
- **Position sizing formula** — "smaller than normal" not quantified
- **BTC entry timing** — "after initial selloff" not defined precisely
- **Natural gas lag duration** — 3-7 days mentioned anecdotally, not tested
- **HIP3 data reliability** — HIP3 is newer, limited history for validation
- **Exit timing** — no specific profit target percentages
- **Airdrop impact** — HIP3 airdrop speculation may distort positioning data

---

## Lumibot / Backtest Implementation Notes

| Consideration | Assessment |
|---------------|-----------|
| Data availability | MEDIUM — commodity ETF data available; HIP3 positioning data requires API |
| Backtesting feasibility | LOW — geopolitical events are rare, each unique; insufficient sample size for statistical backtest |
| Automatable components | Polymarket odds monitoring, HIP3 positioning alerts, options order execution |
| Discretionary components | Geopolitical event identification, escalation assessment, conflict duration judgment |
| Key challenge | Events are unique — can't backtest "Iran war 2026" specifically |
| Suggested approach | Build alert system: HIP3 positioning extremes + Polymarket odds monitoring → manual trade execution |

---

## Source Quotes

> "72% of traders on HIP3 are short oil right now. That's a contrarian signal if I've ever seen one."

> "Natural gas hasn't moved yet. That's the lagging trade."

> "Buy the war works 74% of the time. Historically, you buy the fear."

*Strategy extracted from: Claude Chrome Built My WW3 Trading Bot.txt*
