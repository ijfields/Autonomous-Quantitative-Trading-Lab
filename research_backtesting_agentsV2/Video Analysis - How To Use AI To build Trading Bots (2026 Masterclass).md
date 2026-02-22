# Video Analysis: How To Use AI To Build Trading Bots (2026 Masterclass)

**Speaker:** Moon Dev / Alex Finn
**Channel:** Moon Dev
**Video ID:** 3AmL2qcXB5k
**Upload Date:** 2026-01-23
**Duration:** ~3 hours 33 minutes

---

## Overview
A marathon live stream combining teaching, live coding, and bot management. Moon Dev walks through his complete 2026 algorithmic trading workflow: the RBI system (Research → Backtest → Implement), his AI coding toolkit (Claude Code + WhisperFlow + multi-agent parallelism), the Hyperliquid data layer providing exclusive liquidation/position/whale data, and live demonstrations of backtesting and bot management. The stream includes stat arb bot evaluation, robustness testing of winning strategies, social arbitrage research concepts, and a sales pitch for the Algo Trade Camp in the final hour.

---

## Key Concepts

### The RBI System
The speaker's core daily framework, repeated dozens of times:
- **Research:** Constantly find new strategy ideas from books, papers, podcasts, YouTube, proprietary data, TikTok trends
- **Backtest:** Code backtests in Python (backtesting.py) to validate ideas historically
- **Implement:** Only build bots for strategies that pass backtesting; start with tiny size ($10 positions)
- Success rate expectation: 1 out of 10 backtests winning is good

### Hand Trading = Gambling
The stream's strongest philosophical position:
- Even perfect hand traders lose to fees with leverage (40x leverage + 5 trades/day = blow up in 31 days from fees alone)
- Market orders cost 3x more than limit orders — bots use limit orders patiently
- Time spent staring at charts doesn't compound; time spent building systems does
- Emotional personal story about losing his best friend while being "in a trade"

### Hyperliquid Data Layer as Edge
- Self-hosted Hyperliquid node providing data "Wall Street doesn't want you to have"
- 19,000+ active wallets with visible positions, leverage, liquidation distances
- HLP market maker positions visible (7 strategies, $1K → $183M)
- Liquidation data across Binance, OKX, Bybit, and Hyperliquid
- HIP3: stocks, forex, and futures data on Hyperliquid (Apple, AMD, Google, Anthropic, etc.)

### Claude Code 2026 Workflow
- WhisperFlow voice-to-text (152 WPM vs 70 WPM typing)
- Multiple Claude Code instances running different projects simultaneously
- Multi-agent parallel backtesting ("launch 5 agents to test 5 ideas")
- Plan Mode (Shift+Tab) for complex projects — plan before executing
- Autonomous mode (`claude --dangerously-skip-permissions`) aliased to `C`
- Sub-agents specialized for backtesting, research, and bot building

### Repainting Problem in TradingView
- TradingView backtests suffer from repainting: indicators change historical values after the fact
- Future data leakage and look-ahead bias make backtests look better than reality
- Use TradingView ONLY for grabbing Pine Script indicator code → convert to Python
- All actual backtesting should be done in Python (backtesting.py, BackTrader, VectorBT)

---

## Strategies Identified

| # | Strategy | Type | Return | Sharpe | Status |
|---|----------|------|--------|--------|--------|
| 1 | V8 Pullback (liquidation) | Crypto momentum | 3,418% | 4.13 | Passed all 4 robustness tests |
| 2 | Lick Ratio Momentum (QQE + liquidations) | Crypto momentum | 101% | 1.66 | Passed all robustness tests |
| 3 | 500K Momentum | Crypto momentum | 58% | — | Passed robustness |
| 4 | Regular Stat Arb | Market neutral | Profitable | — | Live with tiny size |
| 5 | Copula Stat Arb | Market neutral | Losing | — | Live, adjusting SL to -6% |
| 6 | Gaussian Stat Arb | Market neutral | Losing | — | Live, adjusting SL to -6% |
| 7 | Fourier Stat Arb | Market neutral | Losing | — | Live, adjusting SL to -6% |
| 8 | QQE Cross + Momentum Filter | Crypto liquidation | 57% win rate | Low | Initial test, not implemented |
| 9 | Long vs Short Liquidation | Crypto liquidation | — | — | Tested by agent, initial scan |
| 10 | Consecutive Lick Bars | Crypto liquidation | — | — | Tested by agent, initial scan |
| 11 | Lick Mean Reversion | Crypto liquidation | — | — | Tested by agent, initial scan |
| 12 | Lick + RSI | Crypto liquidation | — | — | Tested by agent, initial scan |
| 13 | Lick Cooldown | Crypto liquidation | — | — | Tested by agent, initial scan |
| 14 | Social Arbitrage (TikTok trends) | Equity fundamental | — | — | Research phase, building agent |

---

## Backtestable Parameters
- **Liquidation momentum:** When large liquidations occur ($5M+), trade in the direction of the cascade (if long liquidations → short, if short liquidations → long)
- **Lick ratio momentum:** When liquidation ratio exceeds 2:1, enter in the dominant direction
- **Stat arb:** Pairs trading with simultaneous long and short for market neutrality; 2% take-profit, 6% stop-loss, 12-hour max hold time
- **QQE mod + liquidation data:** Combine TradingView's QQE indicator signals with liquidation volume for entry confirmation
- **Social arbitrage:** Monitor TikTok for consumer trend tags → identify publicly traded companies experiencing viral demand → enter before institutional awareness

---

## Tools, Platforms & Resources

| Tool | Purpose | Notes |
|------|---------|-------|
| Claude Code | Primary AI coding agent | Terminal-based, multiple instances, multi-agent |
| WhisperFlow | Voice-to-text | whisperflow.ai, 152 WPM |
| Cursor | Beginner-friendly AI IDE | Free fork of VS Code, supports all models |
| backtesting.py | Backtesting framework | Speaker's preferred Python library |
| CCXT | Exchange connectivity | Connects to all major exchanges |
| Hyperliquid data layer | Proprietary data | 55+ endpoints, self-hosted node |
| TradingView | Indicator code source ONLY | DO NOT use for backtesting |
| Cherry Servers | VPS for 24/7 bots | ~$50/month |
| Google Scholar | Academic strategy papers | Free research resource |
| Apple Notes | Idea tracking | Quick note-taking for strategies |
| GitHub (mundave) | Code sharing | Trading bot repo + AI agents repo |
| RBI Agent | Autonomous backtesting | Loops through ideas.txt endlessly |

---

## Critical Insights & Actionable Takeaways

1. **The RBI system is the entire framework** — Research ideas daily, Backtest in Python (not TradingView), Implement only winners with tiny size. This cycle repeats indefinitely.

2. **Claude Code with WhisperFlow is the current meta** — Voice input + multi-agent parallel backtesting + Plan Mode reduces what used to be 8-hour backtests to minutes. The speaker runs 3+ Claude Code projects simultaneously.

3. **1 out of 10 winning backtests is good** — Reset expectations. Jim Simons built $31B with this mindset. Most ideas fail, and that's the game.

4. **Fees kill hand traders mathematically** — At 40x leverage with 5 trades/day, you're bankrupt in 31 days from fees alone. Bots using limit orders extend that to 717 days before even considering profitable strategies.

5. **Robustness testing validates edge** — Signal permutation (shuffle signals randomly — if random beats real, no edge), parameter sensitivity, and transaction cost buffer tests must pass before implementation.

6. **TradingView's repainting is a backtest killer** — Indicators that use close price before candle closes create future data leakage. Only use TradingView to grab Pine Script code for conversion to Python.

7. **Tiny size is non-negotiable for new bots** — The speaker runs $10 positions on live bots for weeks before scaling. Even after passing backtests, strategies may fail in live markets.

8. **Social arbitrage is an untapped edge** — Consumer trends visible on TikTok weeks before Wall Street prices them in (Abercrombie, Crocs, Celsius examples). Building AI agents to automate this discovery.

9. **VPS hosting enables true 24/7 operation** — SSH into a cloud server running Claude Code and bots. Close your laptop; bots keep running. ~$50/month removes power outage and connectivity risk.

10. **The autonomous RBI agent is the endgame** — A Python script that reads ideas from a text file, researches each one, codes a backtest, debugs it, reports results, and loops forever. This is the ultimate application of the RBI system.

*Analyzed from: How To Use AI To build Trading Bots (2026 Masterclass).txt*
