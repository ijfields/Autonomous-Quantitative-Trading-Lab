# Step-by-Step Guide: Deploying an Optimized Trading Bot via SignalSwap.io

**Source:** Trade Tactics (YouTube)
**Video ID:** bETC3TYEpkU
**Upload Date:** 2026-03-09

---

## What This Guide Covers

How to optimize a trading bot's parameters, validate with out-of-sample testing, and deploy live to an exchange using SignalSwap.io webhooks from TradingView.

---

## Prerequisites

- TradingView Premium account (required for webhook alerts)
- Apex Pro or Bybit exchange account
- PineScript strategy loaded on TradingView
- Python back-tester (optional — can use SignalSwap's built-in module)

---

## Step 1: Optimize Your Strategy Parameters

1. Set up a parameter search across all combinations
2. Run on in-sample data (training set)
3. Hold out a portion of data for out-of-sample validation
4. Identify parameter sets with best risk-adjusted returns

**Target metrics:** 10% max drawdown, 60%+ win rate, 3.0+ profit factor.

---

## Step 2: Validate with Out-of-Sample Testing

1. Apply the best parameter set to the holdout data
2. Check if metrics hold up on unseen data
3. Optional: Run candlestick randomization stress test (thousands of data variations)
4. Only proceed if out-of-sample performance is acceptable

---

## Step 3: Mirror Parameters in TradingView

1. Open your PineScript strategy on TradingView
2. Update all parameters to match the optimized values
3. Verify metrics match your Python back-test results
4. Confirm on the correct chart/timeframe (e.g., Solana 30-min)

---

## Step 4: Set Up SignalSwap.io

1. Go to SignalSwap.io and sign up (free)
2. Use the referral link to sign up for Apex Pro (required for free access)
3. Generate API key on Apex Pro (API Management → Generate API → Trade mode)
4. Copy all 5 fields (API key + account ID + 3 others + L2 private key/Omni key)
5. Paste into SignalSwap exchange connection form
6. Click "Link Exchange Account"

---

## Step 5: Create Your Bot

1. Go to Bot Wizard on SignalSwap
2. Select your linked exchange
3. Choose trading pair
4. Set position size and total bot balance
5. Choose order type (market or limit)
6. Set leverage (start at 1.0x)
7. Click Next — generates webhook URL and alert message

---

## Step 6: Connect TradingView Alert

1. On TradingView, create a new alert on your strategy
2. Delete the default message text
3. Paste the SignalSwap alert message (should show green = valid)
4. Go to Notifications tab → paste webhook URL
5. Set alert to open-ended (no expiration)
6. Click Create

---

## Step 7: Monitor and Publish

1. Check trade history tab on SignalSwap dashboard for confirmed/failed trades
2. Monitor equity curve and performance metrics
3. After 60+ days active and profitable → eligible to publish to marketplace
4. Published bots earn 70% of subscription revenue

---

## Key Takeaway

> Validate before deploying. Split your data, test on holdout samples, stress test with randomized candles, and only go live when out-of-sample performance confirms your edge is real — not curve-fitted.

*Guide derived from: My Optimized Trading Bot is now The BEST in the WORLD (Copy My Method).txt*
