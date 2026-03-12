# Step-by-Step Guide: SPX 0DTE Trend Spread Engine Credit Spread System

**Source:** Stock Market Options Trading / AlphaCrunching (YouTube)
**Video ID:** vcKwWAguOm0
**Upload Date:** 2026-03-11

---

## What This Guide Covers

A systematic SPX 0DTE credit spread strategy using time-of-day optimization and rolling 90-day performance ranking.

---

## Step 1: Understand the Time-Slot Ranking System

1. The engine logs 0DTE credit spread trades every trading day
2. Time slots: 10:00 AM, 10:15 AM, 10:30 AM, 11:30 AM, 12:15 PM, etc. (through 3:00 PM ET)
3. Each Sunday, a report ranks time slots by trailing **90-day win rate**
4. Focus only on the **top 5** performing time slots

---

## Step 2: Determine Trade Direction

1. Assess the prevailing trend at the selected time slot
2. **Bearish trend** → sell **call credit spreads** (above the market)
3. **Bullish trend** → sell **put credit spreads** (below the market)
4. Always trade with the trend, not against it

---

## Step 3: Execute the Trade

1. At the selected time slot, sell the credit spread at the strikes indicated
2. The 10:30 AM slot had a **91.8%** win rate (expired worthless) over trailing 90 days
3. Let the spread expire worthless (0DTE = same-day expiration)

---

## Step 4: Weekly Review and Adaptation

1. Every Sunday, review the updated 90-day performance report
2. Top time slots shift over time — only trade the current top tier
3. If a time slot's win rate degrades, stop trading it until it recovers

---

## Key Takeaway

> Not all 30-minute windows are equal for 0DTE credit spreads. A rolling 90-day performance ranking identifies the highest-probability time slots, and trading with the prevailing trend direction adds a systematic edge. The 10:30 AM Eastern slot has historically been the strongest performer.

*Guide derived from: SPX 0DTE Credit Spread Strategy | Trend Spread Engine.txt*
