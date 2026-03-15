# Step-by-Step Guide: Claude Code Polymarket Trading Bots

**Source:** Moon Dev (YouTube)
**Video ID:** 1BbKTQOPOGQ
**Upload Date:** 2026-03-14

---

## What This Guide Covers
How to build and deploy a Polymarket binary-bet trading bot that uses liquidation data to predict BTC direction, including the hedging component on Hyperliquid and how to participate in the MoonDev Arena prediction contest.

---

## Step 1: Understand the Polymarket Binary Bet Structure
1. Polymarket offers 5-minute and 15-minute binary up/down markets on BTC.
2. You pay approximately $50 for a contract that pays $100 if correct -- a binary outcome.
3. Direction is all that matters: if BTC goes up even 1 cent, you win the full amount.
4. This creates extreme effective leverage:
   - 15-minute markets: approximately 1,400x effective leverage
   - 5-minute markets: approximately 2,400x effective leverage
   - Compared to Hyperliquid at 40-50x leverage
5. 288 trading opportunities per day on the 5-minute market.
6. Pros: defined risk (you can never lose more than your bet), no liquidation cascades, no funding rates.
7. Cons: 100% loss on wrong bets (no partial wins), without an edge you bleed the spread quickly.

## Step 2: Set Up the MoonDev API for Liquidation Data
1. Access the MoonDev API (requires API key from MoonDev Zoom sessions or platform).
2. Key data endpoints used:
   - BTC liquidation data (Hyperliquid + Binance)
   - Position snapshots (positions near liquidation)
   - Tick data (7-day, 30-day, 90-day windows)
3. The API provides real-time liquidation events showing when traders get liquidated, their position sizes, and the direction (long/short).

## Step 3: Understand the Liquidation Stink Bid Strategy
1. Monitor liquidation data from the MoonDev API in real time.
2. Focus on BTC liquidations in the $25,000 to $100,000 range (the "sweet spot" -- not chasing tiny or whale liquidations).
3. Long liquidations (longs getting wiped) = bearish signal = buy DOWN on Polymarket's 5-minute binary.
4. Short liquidations (shorts getting wiped) = bullish signal = buy UP on Polymarket's 5-minute binary.
5. Instead of market buying on Polymarket, place stink bids (limit orders below market price) to get a better entry.
6. Once the Polymarket leg fills, immediately hedge 40% of the position on Hyperliquid in the opposite direction.
7. The bot uses 3x leverage on the Hyperliquid hedge side.

## Step 4: Set Up Your Trading Accounts
1. **Polymarket**: Create an account, deposit USDC, set up API keys.
   - Important: Place one small trade through the Polymarket website first to trigger the deposit + allowance flow from your browser wallet to your proxy wallet.
   - The proxy wallet must have USDC deposited for API trading to work.
2. **Hyperliquid**: Create an account with a clean private key (separate from any potentially compromised accounts).
   - Store the private key securely in your .env file.

## Step 5: Deploy the Bot
1. Clone or create the Python bot code.
2. Configure your .env file with:
   - MoonDev API key
   - Polymarket API credentials
   - Hyperliquid private key
3. Set the liquidation range parameters (default: $25,000 to $100,000).
4. Set the total exposure per trade (default: $25).
5. Run the bot: `python run_it.py`
6. Monitor the output for:
   - Current liquidation totals (long and short)
   - Trade execution confirmations
   - Hedge placement confirmations

## Step 6: Participate in the MoonDev Arena
1. Go to mundav.com/arena.
2. Sign up for a free account (username must be one word, no spaces).
3. Download the historical data CSV files (60 days of BTC data).
4. Build a Python prediction model with a `predict(data)` function.
5. Your model receives a dictionary with 60+ keys of live market data every hour:
   - BTC price ticks
   - Hyperliquid liquidations
   - Binance liquidations
   - Positions near liquidation
6. Submit your model -- rolling daily contest with MoonDev credit prizes.

## Step 7: Apply the RBI Framework
1. **Research**: Study the liquidation data, Polymarket binary mechanics, and effective leverage dynamics.
2. **Back Test**: Use historical data from the MoonDev API to test your prediction model. Verify that your strategy has a positive edge (need above 50% win rate for binary bets).
3. **Implement**: Only deploy live with real capital after confirming a backtested edge.
4. Start with tiny bet sizes -- on binary markets, each trade risks 100% of the bet amount.

---

## Key Takeaway

> Polymarket's 5-minute binary markets offer approximately 2,400x effective leverage because the full payout is received for correctly predicting direction regardless of BTC move magnitude -- but without a proven edge above 50%, the 288 daily opportunities will drain your account fast, making backtesting and the RBI framework essential before going live.

*Guide derived from: Claude Code Polymarket Trading Bots [1BbKTQOPOGQ].en.vtt*
