# Step-by-Step Guide: Claude Code Polymarket Trading Bots

**Source:** Moon Dev (YouTube)
**Video ID:** 1BbKTQOPOGQ
**Upload Date:** 2026-03-14

---

## What This Guide Covers

How to build a Polymarket trading bot that uses liquidation data to trade 5-minute binary BTC markets, hedge on Hyperliquid, and use CVD (Cumulative Volume Delta) from tick data for order flow analysis.

---

## Step 1: Understand the Polymarket 5-Minute Binary Markets

1. Polymarket offers 5-minute and 15-minute binary markets on BTC price direction (up or down).
2. You bet on whether BTC will be higher or lower at the end of the window.
3. Binary mechanics: odds are roughly 50/50, so you pay ~$50 for a contract that pays $100 if correct.
4. If BTC goes up even 1 cent, you win 100% return. The size of the move is irrelevant -- only direction matters.
5. Effective leverage is approximately 2,400x compared to traditional Hyperliquid perpetual futures (where profit is proportional to price movement).
6. There are 288 five-minute windows per day (288 potential trades).

**Key risk:** Without a real edge, you are paying the spread and slowly bleeding. At 288 bets/day, even a 49% win rate drains you fast.

---

## Step 2: Understand the Lick Stinkbot Strategy

The "Lick Stinkbot" is a liquidation-momentum strategy for Polymarket:

1. **Data source:** MoonDev API provides real-time liquidation data from Hyperliquid, Binance, and OKX.
2. **Signal:** Watch for BTC liquidations in the $25,000 to $100,000 range (the "sweet spot" -- front of the wave, not chasing).
3. **Direction logic:**
   - Long liquidations (longs getting stopped out) = bearish signal = buy "down" on Polymarket.
   - Short liquidations (shorts getting stopped out) = bullish signal = buy "up" on Polymarket.
4. **Entry method:** Instead of market buying, the bot places a stink bid (limit order) on the Polymarket binary contract.
5. **Hedge:** Once the Polymarket leg fills, immediately hedge 40% of the position on Hyperliquid in the opposite direction at 3x leverage.
6. **Hold to expiry:** The 5-minute binary resolves at the end of the window -- no take profit or stop loss needed.

**Important:** The $25K-$100K threshold is an arbitrary starting point, not backtested. This is an idea to test, not a proven strategy.

---

## Step 3: Set Up the Bot Environment

1. Clone or obtain the Lick Stinkbot Python script (available on MoonDev's algo trading roadmap).
2. Set up your `.env` file with:
   - MoonDev API key (for liquidation data, tick data, position snapshots)
   - Polymarket API credentials (API key and secret)
   - Hyperliquid private key (for the hedge leg)
3. **Polymarket proxy wallet:** Ensure your proxy wallet (derived from the API key) has USDC deposited. If it shows zero balance, place one small trade through the Polymarket website to trigger the deposit + allowance flow from your browser wallet to the proxy wallet.
4. Run the bot: `python lick_stinkbot.py`
5. The bot will display: Hyperliquid balance, liquidation range being monitored, trade history, and current liquidation activity.

---

## Step 4: Understand the Effective Leverage Math

**On Hyperliquid (50x leverage):**
- You put $100, controlling $5,000 of BTC.
- If BTC moves 0.1% in 15 minutes, you make $5 (5% return).

**On Polymarket (15-min binary):**
- You put $100 betting BTC goes up.
- If BTC goes up even 0.001%, you win. You doubled your money: 100% return.
- This is where the ~1,400x effective leverage comes from on 15-min markets.

**On Polymarket (5-min binary):**
- In 5 minutes, BTC moves even less, so Hyperliquid profits are even smaller.
- But binary still pays 100% for being right.
- Effective leverage jumps to ~2,400x.
- 288 opportunities per day (3x more than 15-min markets).

**Pros:** Defined risk (never lose more than your bet), no liquidation cascades, no funding rates, execution simplicity (no stop losses or position sizing needed), edge amplification (even 52-53% accuracy prints money at binary scale).

**Cons:** 100% loss per wrong trade (no partial wins), the 50/50 trap bleeds you without a real edge, leverage comparison can be misleading since risk structure is fundamentally different.

---

## Step 5: Build a CVD Scanner for Order Flow Analysis

CVD (Cumulative Volume Delta) is a powerful order flow indicator built from tick data:

1. **What it tracks:** Running total of buying volume minus selling volume over time at the tick level.
   - Buy volume = trades hitting the ask (aggressive buyers).
   - Sell volume = trades hitting the bid (aggressive sellers).
   - Delta per tick = buy volume - sell volume.
   - CVD = cumulative sum of all deltas.

2. **Signal patterns:**
   - Price rising + CVD rising = healthy trend, aggressive buyers driving it.
   - Price rising + CVD flat/falling = divergence, move driven by short covering not real demand.
   - Price falling + CVD falling = healthy downtrend, aggressive sellers in control.
   - Price falling + CVD flat/rising = divergence, buyers stepping in, possible accumulation/reversal.

3. **Algorithmic uses:**
   - Divergence detection: compare slope of price vs. slope of CVD.
   - Trend confirmation: only take longs if CVD slope is positive, shorts when negative.
   - CVD rate of change: sudden spikes indicate aggressive order sweeps (institutional footprints).
   - CVD at key levels: watch behavior at support/resistance for stronger signals.

4. **Building from tick data:**
   - Each tick from the MoonDev API includes side (buy/sell) and size.
   - Compute delta per tick, accumulate into CVD.
   - Resample on any timeframe as needed.
   - Use Python's Rich library for flicker-free terminal display (instead of console clear/repaint).

---

## Step 6: Use the MoonDev Arena for Model Testing

1. Visit mundav.com/arena to access the free prediction competition.
2. Sign up for an account (username must be one word, no spaces).
3. Download the 60-day historical data CSVs:
   - BTC price ticks
   - Hyperliquid liquidations
   - Binance liquidations
   - Positions near liquidation
4. Build a Python prediction model that takes an hourly data snapshot and predicts BTC direction.
5. Submit your model -- it runs in a Docker sandbox and receives live data every hour.
6. Daily winner receives $1,795 MoonDev credit.
7. You do not need an API key for external data -- the arena server pulls directly from MoonDev API.

---

## Key Takeaway

> Polymarket's 5-minute binary BTC markets offer ~2,400x effective leverage with defined risk, but without a proven edge you are just flipping coins. The play is to bet tiny amounts with a data-driven edge (liquidation momentum, CVD divergence, or ML models) hundreds of times per day and let the math compound. Without the edge, it is a casino. With it, it is a printing press.

*Guide derived from: Claude Code Polymarket Trading Bots.txt*
