# Moon Dev Shorts Collection (8 clips) — Complete Transcript Analysis

**Channel:** Moon Dev
**Platform:** YouTube
**Format:** YouTube Shorts (all under 2.5 minutes)

---

## CLIP 1: Building a Momentum Strategy Using Short Liquidations
**Video ID:** meEKcRb7NGY | **Duration:** 66s | **Upload:** 2026-03-11

Moon Dev explains the core concept: check hourly trend direction, then look at how many short positions are clustered above current price about to get liquidated. If enough shorts are stacked in the trend direction, enter long expecting momentum from the liquidation cascade. He trades liquidations "both ways" (momentum and reversal) but starts this bot with the simpler momentum approach. Open-source plumbing others can extend.

---

## CLIP 2: Moon Dev Brainstorms a Guardian Agent to Kill Python Processes and Save RAM
**Video ID:** wLYRPFSkqJo | **Duration:** 138s | **Upload:** 2026-03-11

Designing a "Guardian Agent" daemon (`guardian_agent.py`) that monitors CPU/RAM/swap every 30 seconds, tracks per-process memory (especially Python child processes), sends graduated alerts at warning/red-zone thresholds (85% RAM), and performs "smart kill" of lowest-priority processes first. Key concern: identifying actual Python filenames to prioritize which agents to kill (protect live trading agents, kill old backtests first).

---

## CLIP 3: Hyperliquid Oil Volume Hits 346 Million with 162% Funding
**Video ID:** -fBrJX9Wrrc | **Duration:** 66s | **Upload:** 2026-03-11

HIP-3 protocol now supports non-crypto assets (oil, silver, stablecoins). Oil saw $346M in overnight volume proving real adoption. Annualized funding rate at 162% signals "everybody is long" — a crowded-trade observation. Funding rate flagged as a tradeable signal but no full strategy laid out.

---

## CLIP 4: Building Trending Bots for HIP-3 Gold and Oil Markets
**Video ID:** HZLuFGKt9SM | **Duration:** 70s | **Upload:** 2026-03-11

During crypto bear markets, HIP-3 assets (gold, oil, silver) always have something trending. Moon Dev is porting existing Hyperliquid crypto trend-following bots to HIP-3 commodity markets. References the "war trade" (geopolitical trend in oil/gold) as one instance of broader trend-following approach.

---

## CLIP 5: We Might Be Able to Take on Wall Street
**Video ID:** OOcxxSLDXaY | **Duration:** 42s | **Upload:** 2026-03-11

Motivational clip about community self-selection: members must be interested in automated trading, join Zoom calls, wake up early. This filtering over 5 years could produce a group that competes with institutional Wall Street players.

---

## CLIP 6: Correcting the Math on Hyperliquid Hourly Funding Rates
**Video ID:** tD4REh8dWNA | **Duration:** 38s | **Upload:** 2026-03-11

Common mistake: people use 8-hour funding rate convention (Binance) but Hyperliquid uses 1-hour rates. Correct annualization of 0.0245% hourly = **214.39%** annualized, not the lower 8-hour number. Critical distinction when evaluating funding-rate signals.

---

## CLIP 7: Patching Hyperliquid H3 Price Rounding for Limit Orders
**Video ID:** 2-6jlorQRdk | **Duration:** 40s | **Upload:** 2026-03-11

Bug fix: Hyperliquid SDK rounds prices to 5 significant figures, but HIP-3 assets need their own rounding rule (`h3_price_to_order_price`). Without the patch, sizing off mid-price but submitting a rounded-down limit price falls below minimum notional and gets rejected. Patched three functions: `h3_price_to_order_price`, `h3_limit_order`, `h3_lick_momentum`.

---

## CLIP 8: Build AI Agents for Every Little Thing You Do
**Video ID:** FUiud9rO864 | **Duration:** 38s | **Upload:** 2026-03-11

Philosophy clip: build an AI agent for every small, repetitive task. Shows a YouTube video clipping agent as example. Agent-first thinking as a lifestyle/productivity approach.

---

## TRADING STRATEGIES IDENTIFIED

Clip 1 contains a partial momentum strategy concept (hourly trend + short liquidation cluster = entry) but lacks explicit take-profit, stop-loss, or position-sizing rules. Clips 3-4 discuss tradeable signals (funding rates, HIP-3 commodity trends) without full strategy specifications. Remaining clips are infrastructure, bug fixes, or motivational content.

---

*Analysis derived from 8 Moon Dev YouTube Shorts transcripts*
