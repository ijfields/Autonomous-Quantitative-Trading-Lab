# How To Backtest Properly With Claude Code (MUST WATCH) — Complete Transcript Analysis

**Video Title:** How To Backtest Properly With Claude Code (MUST WATCH)
**Channel:** AI Pathways
**Video ID:** lIMu8ysJW68
**Upload Date:** 2026-03-08
**Duration:** ~17m
**Speaker:** AI Pathways (host)
**Platform:** YouTube

---

## EXECUTIVE SUMMARY

Demonstrates why traditional backtesting is fundamentally unreliable (curve fitting) and how to use Claude Code to build a walk-forward analysis engine in Streamlit. Two strategies tested: RSI crossover (199% traditional → 5.8% walk-forward, 75% was fake) and ATR + Butterworth filter (1,500% traditional → 7% walk-forward). Critical technical warning: use `lfilter` not `filtfilt` to prevent look-ahead bias. The walk-forward methodology (12-month training / 3-month blind test, 19 folds) is the institutional-grade approach for honest backtesting.

---

## KEY TOPICS

### The Curve Fitting Problem

- Optimizing across the full historical window = "memorizing the answer key"
- Standard RSI crossover showed ~199% return on traditional backtest — entirely illusory
- Walk-forward revealed only **5.8%** was real (75% return degradation)

### Walk-Forward Analysis Methodology

| Step | Window | Purpose |
|------|--------|---------|
| 1 | **12-month training** | Optimizer searches thousands of parameter combinations |
| 2 | **3-month blind test** | Best parameters locked, applied to unseen data |
| 3 | **Walk forward** | Window advances by blind test length, repeat |
| 4 | **Stitch OOS returns** | Only blind-test results concatenated for "true" performance |

- For 2018–2024 data: produces **19 folds**
- If strategy was curve-fit, it loses money on blind window
- If genuine edge exists, it persists into unseen data

### Two Strategies Tested

| Strategy | Traditional Backtest | Walk-Forward | Return Degradation |
|----------|---------------------|--------------|-------------------|
| RSI Crossover + 20-SMA | ~199% | 5.8% | 75% was fake |
| ATR + Butterworth Filter | ~1,500% | ~7% | 75%+ was fake |

### Critical Technical Warning: `filtfilt` vs `lfilter`

- **`filtfilt` (scipy):** Applies filter forward AND backward — **uses future price data** (look-ahead bias). AI agents default to this.
- **`lfilter`:** Forward-only (strictly causal) — no future data leaks
- **Always instruct Claude Code to use `lfilter`**

### Building with Claude Code — Workflow

1. Open VS Code with blank project folder
2. Install Claude Code extension
3. Prompt with detailed specification (Streamlit, Plotly, yfinance, SPY, walk-forward engine)
4. Include: 0.1% transaction costs (exchange fee + slippage)
5. Dashboard shows fold-by-fold progress, best parameters per fold, traditional vs walk-forward equity curves
6. Return degradation metric quantifies how much was fake

---

## TOOLS & PLATFORMS MENTIONED

| Tool/Platform | Purpose |
|---------------|---------|
| Claude Code | AI coding agent generating the full application |
| VS Code | Development environment |
| Python | Programming language (no manual coding) |
| Streamlit | Web dashboard framework |
| Plotly | Interactive charting |
| Yahoo Finance (yfinance) | Historical price data |
| SciPy | Signal processing (Butterworth filter, lfilter) |

---

## ACTIONABLE TAKEAWAYS

1. **Never trust single-window backtests** — assume curve fitting until proven via walk-forward
2. **Build a walk-forward engine** — 12-month train / 3-month blind test is a solid starting config
3. **Always include transaction costs** — 0.1% slippage + fees minimum
4. **Watch for look-ahead bias** — explicitly use `lfilter` not `filtfilt` for signal processing
5. **Only trust stitched OOS returns** — the concatenation of all blind-test windows is the true performance
6. **Complexity does not equal edge** — ATR + Butterworth looked 7.5x better but performed nearly identically on walk-forward
7. **Check return degradation** — the gap between traditional and walk-forward quantifies how much was fake
8. **Iterate rapidly with Claude Code** — build engine, run walk-forward, swap in new strategy hypothesis, re-test

---

*Analysis derived from: How To Backtest Properly With Claude Code (MUST WATCH).txt*
