# Step-by-Step Guide: Position Sizing Methods for Automated Trading

**Source:** Unbiased Trading (YouTube)
**Video ID:** uzwx8pe0QdA
**Upload Date:** 2026-03-10

---

## What This Guide Covers

Four position sizing methods ranked by sophistication, with formulas and implementation guidance for automated trading systems.

---

## Method 1: Fixed Percentage (Beginner)

```
Position Size = Account Value × Risk Percentage
```

- Use 1-2% per trade as baseline
- Self-correcting: compounds when winning, protects when losing
- Best for: simple strategies, beginners, or as a fallback

---

## Method 2: Equal Weighting (Portfolio Allocation)

```
Position Size = Total Capital / Number of Positions
```

- Only use when assets/strategies are demonstrably **uncorrelated**
- If correlation = 1, equal weighting creates hidden concentration
- Best for: diversified multi-strategy portfolios

---

## Method 3: Kelly Criterion (Advanced — Use Cautiously)

```
Kelly % = [Win Rate × (Win/Loss Ratio + 1) - 1] / Win/Loss Ratio
```

- Full Kelly is dangerous — produces 50%+ drawdowns even with a real edge
- Use **Quarter-Kelly** at most (typically lands at 5-10% risk)
- Only viable for HFT with thousands of trades
- For most traders: skip Kelly entirely

---

## Method 4: Volatility Targeting (Recommended)

### Step 1: Calculate Asset Volatility
1. Get daily returns for past 20 trading days
2. Calculate standard deviation
3. Annualize: multiply by √252 (equities/futures) or √365 (crypto)

### Step 2: Choose an Implementation

**ATR-Based (Simplest):**
```
Position Size = Risk Per Trade / ATR
```
- ATR available on TradingView or any platform
- Automatically shrinks in volatile markets, grows in calm markets

**Percent Volatility Model:**
```
Position Size = (Account Value × Risk %) / Annualized Volatility
```
- Example: $100K account, 2% risk, 40% vol → $5,000 position
- If vol doubles to 80% → position halves to $2,500

**Fixed % with Volatility Adjustment:**
- Base allocation scales inversely to volatility
- 60% vol asset → ~$5K; 15% vol asset → ~$20K (4x more capital)

### Step 3: Recalculate Regularly
- Volatility changes constantly — automate the recalculation
- Use rolling 20-day window

---

## The Override Rule

If any single loss changes your behavior (fear, revenge trading, system doubt), reduce size immediately. Trading smaller than the math suggests is often correct.

---

## Key Takeaway

> Position sizing — not entries and exits — determines profitability. Start with fixed percentage (1-2%), graduate to volatility targeting for diversified portfolios. Avoid full Kelly. Every position should contribute roughly equal risk to your portfolio.

*Guide derived from: The 4 position sizing formulas behind WINNING in trading#.txt*
