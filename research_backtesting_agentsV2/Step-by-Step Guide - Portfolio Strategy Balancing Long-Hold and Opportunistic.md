# Step-by-Step Guide: Building a Multi-Asset Evergreen Portfolio

**Source:** Multi Strat Mark (YouTube)
**Video ID:** eQmJCJOO0zA
**Upload Date:** 2026-02-28

---

## What This Guide Covers

How to build a diversified multi-asset portfolio using risk budgeting, correlation analysis, and a 50/50 static/dynamic framework — designed to perform across all market environments.

---

## Prerequisites

- Portfolio Visualizer account (free at portfoliovisualizer.com)
- Brokerage account with ETF access
- Understanding of basic portfolio concepts (allocation, diversification)

---

## Step 1: Understand the Two Types of Risk

| Risk Type | What It Is | Example |
|-----------|-----------|---------|
| **Systematic** (beta) | Risk related to overall market | SPY = 1.0 beta |
| **Idiosyncratic** | Risk independent of market | DBMF moves same amount as SPY but at different times |

**Key insight:** Your portfolio allocation (weights) is only ONE factor. You need to understand how much risk each asset contributes relative to the market.

---

## Step 2: Set Up Portfolio Visualizer

1. Go to Portfolio Visualizer (free)
2. Enter your portfolio tickers and weights
3. Look at three key outputs:
   - **Correlation matrix** — color-coded (blue = correlated, red = inverse, white = uncorrelated)
   - **Risk budget** — how much systematic risk each asset contributes
   - **Standard deviation** — each asset's total volatility (idiosyncratic + systematic)

---

## Step 3: Read the Correlation Matrix

| Color | Meaning |
|-------|---------|
| Blue | Correlated (moves together) |
| Red | Inversely correlated (moves opposite) |
| White | Uncorrelated (independent) |
| Yellow | Slightly inverse / neutral |

**Quick test:** If your matrix is mostly blue, you have concentration risk. You want a mix of colors.

---

## Step 4: Build Your Asset Menu

| Asset | Role | Systematic Risk | Idiosyncratic Risk |
|-------|------|----------------|-------------------|
| SPY | Core equity | High | Medium |
| Gold | Inflation hedge, diversifier | Low | Medium |
| DBMF (managed futures) | Crisis alpha, trend following | Very low | High |
| Buffer ETF | Protected equity exposure | Lower than SPY | Lower than SPY |
| TQQQ | Growth/leverage | Very high | High |
| BTA (anti-beta) | Equity hedge | Negative | Medium |
| Bonds (AGG) | Ballast, low volatility | Low | Low |

---

## Step 5: Set Target Correlations

| Market Environment | Target Portfolio Correlation to SPY |
|-------------------|-----------------------------------|
| Up market (VIX < 25) | ~0.6 (participate in gains) |
| Down market (VIX > 25) | ~0.3 (protection via diversification) |

This asymmetric profile means you capture most of the upside but only a fraction of the downside.

---

## Step 6: Apply the 50/50 Framework

### 50% Static Evergreen Hold
- Diversified across multiple asset classes
- Example: 60% stocks, 20% bonds, 20% gold (better than simple 60/40)
- Add managed futures and buffer ETFs for additional diversification
- Rebalance periodically (quarterly or annually)
- "10 assets you'd hold for a decade"

### 50% Dynamic Signal-Driven
- Adjust allocations based on market signals and regime changes
- Can shift between 90/10 stocks/bonds (bull) to 40/60 (defensive)
- Monitor correlations for clustering (all assets moving together = danger signal)
- Active management of this portion

---

## Step 7: Monitor and Adjust

Check periodically:
1. Has the correlation matrix changed significantly? (clustering warning)
2. Is managed futures allocation performing its hedge role?
3. Are risk budgets still balanced?
4. Has VIX moved above 25? (switch to crisis correlation assessment)

---

## Common Mistakes to Avoid

| Mistake | Why It's Wrong |
|---------|---------------|
| Only looking at allocation weights | Ignores risk contribution (25% DBMF ≈ 1.3% systematic risk) |
| Assuming correlations are stable | They cluster in crises — measure in different regimes |
| Avoiding all leverage | Leverage can REDUCE risk when used to balance risk budgets |
| Set-and-forget for decades | Correlations change; a 60/40 from 2010 doesn't work the same in 2026 |
| Chasing the "secret stock" | Portfolio construction > individual picks |

---

## Key Takeaway

> Build an evergreen portfolio like a redwood tree — it may not be the fastest growing, but when forest fires come, it survives. You have your sanity, your time, and you're not watching the market all day.

*Guide derived from: Portfolio Strategy： Balancing Long-Hold and Opportunistic Investments.txt*
