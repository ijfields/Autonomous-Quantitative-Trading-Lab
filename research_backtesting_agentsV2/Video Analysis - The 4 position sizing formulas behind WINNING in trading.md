# The 4 Position Sizing Formulas Behind WINNING in Trading — Complete Transcript Analysis

**Video Title:** The 4 position sizing formulas behind WINNING in trading.
**Channel:** Unbiased Trading
**Video ID:** uzwx8pe0QdA
**Upload Date:** 2026-03-10
**Duration:** ~12m
**Speaker:** Unbiased Trading (host)
**Platform:** YouTube

---

## EXECUTIVE SUMMARY

Position sizing — not entries and exits — determines whether you make money or blow up. Four methods are presented in order of sophistication: Fixed Percentage, Equal Weighting, Kelly Criterion, and Volatility Targeting. The speaker personally uses Volatility Targeting across automated crypto and futures strategies, achieving +13-15% while crypto markets dropped 30-40%.

---

## KEY TOPICS

### Method 1: Fixed Percentage Position Sizing

- **Formula:** Position Size = Account Value × Risk Percentage
- **Example:** $80,000 × 2% = $1,600 risk per trade
- Self-correcting: grows when winning, shrinks when losing
- Speaker's baseline: 1-2% per trade
- **Downside:** Treats every trade identically, ignores volatility

### Method 2: Equal Weighting

- **Formula:** Position Size = Total Capital / Number of Positions
- **Example:** $100,000 / 10 = $10,000 per position
- **Critical caveat:** Only works with uncorrelated assets. Correlated assets at equal weight = hidden concentration
- **Downside:** Ignores volatility entirely

### Method 3: Kelly Criterion

- **Origin:** Bell Labs 1950s, adopted by gamblers and traders
- **Formula:** Kelly % = [Win Rate × (Win/Loss Ratio + 1) - 1] / Win/Loss Ratio
- **Example:** 60% WR, $300 avg win / $150 avg loss → Kelly suggests 40% risk (dangerous)
- **Three failures:** Extremely sensitive to input errors; assumes constant edge; produces 50%+ drawdowns
- **Fractional Kelly (1/4):** Lands at 5-10% — at which point, just use aggressive fixed percentage
- **Only viable for:** Very high frequency strategies with thousands of trades

### Method 4: Volatility Targeting (Speaker's Primary Method)

Size based on how much risk each position actually contributes. High vol = smaller position; low vol = larger.

**4a. ATR-Based:** Position Size = Risk Per Trade / ATR

**4b. Percent Volatility Model:** Position Size = (Account × Risk %) / Annualized Volatility

**4c. Fixed % with Volatility Adjustment:** Base allocation scales inversely to volatility

**How to calculate volatility:**
- Daily returns over past 20 trading days → standard deviation → annualize: ×√252 (equities) or ×√365 (crypto)

---

## THE OVERRIDING RULE

> If losing a trade makes you afraid to take the next signal, want to revenge trade, or question your entire system — you are sized too big. The perfect position size lets you execute without emotional interference.

---

## TOOLS & PLATFORMS MENTIONED

| Tool/Platform | Purpose |
|---------------|---------|
| NinjaTrader | Automated futures trading |
| TradingView | ATR and volatility indicators |
| Automated crypto portfolio | Speaker's primary trading vehicle |

---

## SPECIFIC NUMBERS

- Speaker's crypto: +13-15% while market down 30-40%
- Recommended baseline: 1-2% risk per trade
- Kelly at 60% WR / 2:1 W/L: suggests 40% (too aggressive)
- Quarter-Kelly: 5-10% risk
- Volatility lookback: 20 trading days
- Annualization: √252 (equities), √365 (crypto)

---

*Analysis derived from: The 4 position sizing formulas behind WINNING in trading#.txt*
