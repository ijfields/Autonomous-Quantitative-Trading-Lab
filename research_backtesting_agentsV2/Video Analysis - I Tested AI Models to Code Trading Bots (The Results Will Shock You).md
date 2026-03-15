# Video Analysis: I Tested AI Models to Code Trading Bots (The Results Will Shock You)

**Speaker:** Brian (quantlabs)
**Channel:** quantlabs
**Video ID:** zuZBI_ul5wM
**Upload Date:** 2026-03-12
**Duration:** 24 min 55 sec

---

## Summary

Brian from quantlabsnet.com compares several AI models for generating Python trading bots from large news-driven trading prompts (~1,500 lines). He tests GLM 5 (cheapest Chinese AI), Codex 5.3 (OpenAI), Claude 4.6 (Anthropic), and MiniMax against his futures trading environment built on the Rithmic API. The key finding is that for this specific use case (generating trading bots from large analytical prompts), GLM 5 produces comparable quality to Codex at significantly lower cost, while Claude 4.6 generates marginally more bots (e.g., adding copper/HG) at roughly 3x the cost of Codex -- not worth the premium. MiniMax and Qwen break down with prompts this large due to communication issues with the AI servers.

The video also shows real simulated trading results from news-driven bots generated overnight and that morning. In a volatile market driven by Middle East geopolitical events, Bitcoin halving momentum and natural gas mean-reversion strategies outperformed, while gold showed extreme drawdowns. VIX was the only consistent performer in down markets. Brian argues that the future of trading is "systematic portfolio management" -- using AI to generate fresh trading bots multiple times daily in response to evolving news, then deploying only the profitable ones.

## Key Topics
- Head-to-head comparison of LLMs for trading bot code generation (GLM 5, Codex 5.3, Claude 4.6, MiniMax)
- Cost vs quality tradeoffs for AI-generated trading code
- News-driven trading bot generation from large analytical prompts
- Simulated trading results during geopolitical volatility (Iran/Middle East war)
- Futures instruments: Bitcoin, natural gas, gold, crude oil, Ethereum, VIX, treasuries
- Systematic portfolio management as the future of quant trading
- Speed comparison: Codex fastest, GLM 5 slow but cheapest
- Prompt size limitations with cheaper Chinese models (MiniMax, Qwen break on ~1,500-line prompts)

## Tools & Technologies Mentioned
- GLM 5 (Chinese AI, cheapest option)
- Codex 5.3 / OpenAI (fast, good value)
- Claude 4.6 / Anthropic (3x cost of Codex for marginal benefit)
- MiniMax (breaks on large prompts)
- Qwen (breaks on large prompts)
- Rithmic API (futures/options trading platform)
- Python (primary language for bot generation)
- JavaScript, HTML (secondary languages)
- quantlabsnet.com (analytics platform, private chat group)
- hftcode.com (Algo Trader Pro Blueprint)

## Strategies Found

The video shows several AI-generated news-driven strategies with simulated results, though specific entry/exit rules are not disclosed due to Rithmic terms of service:

1. **Bitcoin Halving Momentum** -- Most profitable in yesterday morning's session; futures-based momentum strategy driven by halving-related news
2. **Natural Gas EU Gas Cap Reversion** -- Mean-reverting strategy exploiting natural gas spread volatility; Sharpe ratio 4.3 but extreme drawdowns (~$36K max drawdown)
3. **Gold Geopolitical Tail Hedge** -- Futures tail hedge driven by Iran/Middle East war; showed extreme drawdowns, higher than Bitcoin
4. **Fed Stagflation Curve (Treasury ZN)** -- Treasury futures strategy with good win ratio
5. **Ethereum Staking Support (Put Sell)** -- Put-selling combination on Ethereum futures
6. **VIX** -- Only consistently profitable instrument during severe down markets

Specific code and detailed entry/exit rules were not shown due to Rithmic API terms of service restrictions.

## Notable Quotes / Insights
- "Codex is pretty well as good as Claude... for the price of it now, which is generally three times on average more than Codex."
- "When things get really bad, the only one performing is VIX."
- "Systematic portfolio managers... this is easily by far the most important metric when it comes to what will be the future of quant trading."
- "If you're using Claude Code and you don't know what you're doing, you're going to get hosed one way or another on the cost."
- "The Chinese LLMs are getting there now... if you're in the world of Python... the Chinese ones seem to be okay."
- "Being able to respond, to create a trading plan for a certain time period and then be able to create bots quickly -- that's where I'd use the latest Codex."

## Actionable Takeaways
1. For large prompt trading bot generation, GLM 5 offers the best cost efficiency; Codex 5.3 is the best value for speed; Claude 4.6 provides marginal benefit at 3x cost.
2. Avoid MiniMax and Qwen for very large prompts (~1,500 lines) as they break down due to server communication limits.
3. Generate news-driven trading bots multiple times daily and deploy only those showing profitability in simulated conditions.
4. In extreme geopolitical volatility, expect VIX to be the only consistent performer while other instruments show unpredictable behavior.
5. Think of AI-driven trading as systematic portfolio management: let AI decide which instruments and strategies to deploy based on the current news cycle.
6. For Python-based trading bot code, Chinese LLMs are now competitive with Western models at significantly lower cost.
7. If speed matters (reacting to breaking news), use Codex despite the higher cost; if cost matters more, use GLM 5 and accept slower generation.
