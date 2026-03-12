# Step-by-Step Guide: Multi-Timeframe Delta Indicator in TradingView

**Source:** LuxAlgo (YouTube)
**Video ID:** fWcJICkPLSE
**Upload Date:** 2026-03-11

---

## What This Guide Covers

How to build a multi-timeframe cumulative volume delta (CVD) indicator in TradingView using LuxAlgo's Quant AI, showing HTF candles with delta values directly on your chart.

---

## Step 1: Generate Base Delta Values

1. Open LuxAlgo Quant AI code generator
2. Prompt: "Show delta values underneath each candle on the current timeframe"
3. Add: "Include a dashboard showing 15-min, 60-min, and 4-hour deltas"
4. Result: working indicator with floating dashboard

---

## Step 2: Replace Dashboard with PO3 HTF Candles

1. Prompt iteration: "Replace the dashboard with PO3-style higher-timeframe candles rendered directly on the chart"
2. HTF candles form in real time showing how each 15-min, 60-min, and 4-hour candle is developing
3. Each HTF candle displays its accumulated delta value

---

## Step 3: Add Countdown Timers

1. Prompt iteration: "Add countdown timers to each higher-timeframe candle"
2. Shows remaining time before each HTF candle closes (e.g., "1h 9min left on the 4-hour candle")

---

## Step 4: Read Multi-Timeframe Delta Alignment

1. **All timeframes bullish delta** → strong directional conviction for longs
2. **Lower TF bullish, higher TF bearish** → potential divergence / counter-trend risk
3. **Front half vs. back half of 4-hour candle** → timing context for entries
4. Use as a filter alongside other entry triggers (price action, levels, etc.)

---

## Key Takeaway

> Multi-timeframe delta analysis makes buying/selling pressure visible across time horizons simultaneously. If lower timeframe delta is bullish but higher timeframe delta is bearish, you may be trading against the larger flow. The PO3-style overlay with countdown timers turns this into an actionable real-time tool.

*Guide derived from: This Delta Indicator is Mind Blowing.txt*
