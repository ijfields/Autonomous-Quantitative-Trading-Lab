# Step-by-Step Guide: Building a Hyperliquid Funding Rate Scanner

**Source:** Moon Dev (YouTube)
**Video ID:** PNKidibnzRU
**Upload Date:** 2026-03-06

---

## What This Guide Covers

How to understand and build a funding rate scanner for Hyperliquid — a unique crypto-native signal that shows market sentiment (long/short imbalance) across crypto perps and the new HIP3 stock/futures/forex instruments.

---

## Prerequisites

- Python environment
- Hyperliquid API access
- Understanding of perpetual futures basics

---

## Step 1: Understand Funding Rates

| Funding Rate | What It Means | Market Is... |
|-------------|---------------|-------------|
| Positive (e.g., +100%) | Longs pay shorts | Long-heavy, "asking for shorts" |
| Negative (e.g., -100%) | Shorts pay longs | Short-heavy, "asking for longs" |
| Normal (~10% for BTC) | Balanced market | Neutral |
| Extreme (±200%+) | Significant imbalance | Potentially overextended |

- Funding rate is paid every **1 hour** on Hyperliquid
- Rates are shown as **annualized** percentages

---

## Step 2: Identify Available Instruments

Hyperliquid now covers:
- **Crypto perps:** BTC, ETH, SOL, and many altcoins
- **HIP3 instruments:** Stocks, futures, forex (newly launched)

HIP3 is significant because Wall Street traders on these same underlying assets (oil, nat gas, etc.) do NOT have funding rate data.

---

## Step 3: Build the Scanner

The scanner should:
1. Pull funding rates for all Hyperliquid instruments
2. Calculate annualized funding rates
3. Sort by highest and lowest readings
4. Display extreme outliers

**Code available at:** Moon Dev's algo trading roadmap → "Code from Videos" section → "HIP Funding Rate Scanner"

---

## Step 4: Interpret the Readings

| Reading | Interpretation | Potential Action |
|---------|---------------|-----------------|
| > +200% annualized | Extreme long bias | Consider contrarian short (with other confluence) |
| < -200% annualized | Extreme short bias | Consider contrarian long (with other confluence) |
| -100% to +100% | Normal range | No signal |
| ±10% (BTC-like) | Very balanced | No signal |

---

## Step 5: Combine with Other Data

Funding rates alone are NOT a trade signal. Combine with:
- **Open interest** (another metric unique to crypto — total open positions)
- Price action and technical analysis
- Volume analysis
- Market structure (support/resistance levels)

---

## Important Caveats

1. **Volume is lower** on HIP3 than traditional exchanges — signals may be noisier
2. **Extreme rates don't stay stable** — you can't just hold for 631%/year annualized return
3. **This is one data source** among many — use as confluence, not standalone
4. **Open interest context matters** — $11M OI is very different from $11B OI

---

## Additional Resources

- **MunDev AI API:** ~30 data sources including funding rates, liquidations, tick data
- **Daily Zoom calls:** Live Q&A with Moon Dev (access via mundave.com)
- **API docs:** mundave.com/docs → funding rate section

*Guide derived from: Hidden Trading Bot Signal No One Looks At.txt*
