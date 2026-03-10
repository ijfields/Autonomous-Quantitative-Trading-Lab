# Strategy Brief: Multi-Asset Evergreen Portfolio

## Source
- **Video:** Portfolio Strategy: Balancing Long-Hold and Opportunistic Investments
- **Channel:** Multi Strat Mark
- **Speakers:** Mark, Jordy, Connor
- **Video ID:** eQmJCJOO0zA
- **Upload Date:** 2026-02-28
- **Timestamp:** Full video (~28m)

---

## Strategy Overview

| Field | Value |
|-------|-------|
| Name | Multi-Asset Evergreen Portfolio |
| Type | portfolio_construction / risk_parity |
| Style | long-term hold + dynamic allocation |
| Asset | Multi-asset: SPY, Gold, DBMF, Buffer ETF, TQQQ, BTA |
| Timeframe | Weekly to monthly rebalancing |
| Direction | Long-biased with hedges |
| Risk-Reward | Target: equity-like returns with 50% less drawdown |
| Confidence | 0.70 |
| Transcript Quality | high (educational, structured, uses Portfolio Visualizer live) |
| Automation Feasibility | MEDIUM |

---

## Core Concept

Build a 50/50 portfolio: half in a static diversified "evergreen" allocation (hold for a decade), half in a dynamic signal-driven allocation. Use risk budgeting (not just weight allocation) to ensure each asset contributes meaningfully without creating systematic risk concentration. Target 0.6 correlation to SPY in up markets and 0.3 in down markets for asymmetric return capture.

**Philosophy:** "This isn't some holy grail. But over a long period of time when forest fires come, we stand up."

---

## Entry Logic

### Static Half (50%)
- **Allocation:** Diversified across uncorrelated asset classes
- **Example:** 60% stocks, 20% bonds, 20% gold (or more complex version with buffer ETFs + managed futures)
- **Rebalancing:** Periodic (quarterly/annually)
- **Rule:** "10 assets you'd hold for a decade"

### Dynamic Half (50%)
- **Signals:** Market regime indicators (VIX levels, correlation clustering, trend signals)
- **Adjustment:** Shift weights between stocks/bonds/alternatives based on signals
- **Range:** Can go from 90% stocks / 10% bonds to 40% stocks / 60% defensive
- **Note:** Signal definition is future work — not fully specified in this episode

---

## Exit Logic

### Static Half
- No exits — hold and rebalance periodically
- Only change composition if fundamental thesis changes for an asset

### Dynamic Half
- Signal-driven reallocation (not individual trade exits)
- Monitor correlation clustering as danger signal
- Reduce equity exposure when VIX > 25 and correlations spike

---

## Risk Management

| Parameter | Value |
|-----------|-------|
| Risk budgeting | Weight by risk contribution, not just allocation |
| Correlation targets | 0.6 up-market / 0.3 down-market to SPY |
| Regime measurement | Correlation at VIX < 25 vs. VIX > 25 |
| Leverage usage | Allowed to balance risk budgets (e.g., treasury futures) |
| Max drawdown goal | Significantly less than SPY (exact target not specified) |

---

## Filters

1. **Correlation matrix** — use Portfolio Visualizer color-coded matrix as "sniff test"
2. **Risk budget analysis** — each asset should contribute meaningfully but not dominate
3. **Regime awareness** — measure correlations in both normal and crisis environments
4. **Clustering detection** — if all assets become correlated (all blue), reduce exposure

---

## Missing / Unclear Elements

- **Specific dynamic signals** — the signal-driven half is acknowledged as future work
- **Exact weights** — portfolio weights not finalized (conceptual framework only)
- **Rebalancing frequency** — "periodic" but not specified exactly
- **Tax implications** — mentioned as future topic but not covered
- **Leverage specifics** — treasury futures mentioned but no exact notional/leverage ratios
- **VIX thresholds** — 25 mentioned as dividing line, but no tiered response system
- **Backtest results** — Return Stacked portfolio mentioned (21% vs 17%) but no formal backtest of the specific portfolio shown

---

## Lumibot / Backtest Implementation Notes

| Consideration | Assessment |
|---------------|-----------:|
| Data availability | HIGH — all mentioned ETFs have extensive history |
| Backtesting feasibility | MEDIUM — static half easy; dynamic half needs signal definition |
| Automatable components | Correlation monitoring, risk budget calculation, rebalancing, VIX regime detection |
| Discretionary components | Dynamic allocation signals (not yet defined), asset selection changes |
| Key challenge | Defining the dynamic allocation signals — this is acknowledged as future work |
| Suggested approach | Backtest static half first with various weight combinations → add VIX-based regime switching → then overlay trend/momentum signals for dynamic half |

---

## Source Quotes

> "People are very afraid of the word leverage. It is less risky to take leverage [when balancing risk budgets]."

> "I want to be 0.6 correlated to the market when the market's going up and 0.3 correlated when the market's going down."

> "The average Joe could go in and make his portfolio, understand what they're doing, without having to do day trading."

*Strategy extracted from: Portfolio Strategy： Balancing Long-Hold and Opportunistic Investments.txt*
