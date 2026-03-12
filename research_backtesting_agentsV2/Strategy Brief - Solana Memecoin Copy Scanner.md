# Strategy Brief: Solana Memecoin Copy Scanner

## Source
- **Video:** I Built 3 Trading Bots That Run 24/7 (Here's What They Made While I Slept)
- **Channel:** Moon Dev
- **Video ID:** hNRN7-Q8PKE
- **Date:** 2026-03-10

## Strategy Type
Copy Trading / Token Discovery / Research Tool

## Market
Solana DEX (Raydium/Jupiter implied)

## Thesis
Use a follow-list of profitable wallets to discover trending Solana memecoins at $1 research scale. The scanner surfaces opportunities; human judgment (or a separate bot) scales into winners. Not a pure profit-first strategy — functions as a research/discovery tool.

## Entry Rules
1. Monitor follow-list wallets via Solana RPC / API
2. Algorithm filters follow-list activity for buy signals
3. Buy tokens that pass filter at $1 position size
4. Check token freshness: last trade 16 seconds ago = active/good; 16 minutes ago = too stale

## Exit Rules
1. **Sell losers bot** (companion): automatically closes bad positions
2. **Manual review**: tokens that "float to the top" (up and trending) get human attention
3. Scale into winners only after manual review
4. **Refunds bot** (companion): claims Solana account close refunds (rent reclamation)

## Position Sizing
- $1 per token (research scale)
- Scale up only after manual review and conviction

## Risk Management
- $1 max loss per position
- Most tokens are acknowledged rug pulls — this is priced in
- Companion "sell losers" bot limits downside duration
- Only profitable during active "Solana season"
- Currently costs couple hundred $/month as a scanner during quiet periods

## Three-Bot Architecture
| Bot | Function |
|-----|----------|
| **Main scanner** | Follow-list monitoring + $1 buys |
| **Sell losers** | Auto-closes positions that decline |
| **Refunds** | Claims Solana account close rent reclamation (73+ accounts example) |

## Technical Requirements
- Solana wallet with RPC endpoint
- Follow-list of profitable wallet addresses
- Filtering algorithm (activity-based)
- Token freshness checking (last trade timestamp)
- Separate bots for selling and rent reclamation

## Key Considerations
- Highly seasonal — profitable during memecoin bull runs, costs money during quiet periods
- Rug pull risk is fundamental and expected (hence $1 sizing)
- Research value: discovering trending tokens early, even at a loss, provides alpha for larger manual trades
- Rent reclamation: Solana charges account rent; closing unused token accounts recovers SOL

## Performance Reference
- "Very very profitable when Solana season was here"
- Currently running at cost (couple hundred $/month) as scanner

## Backtesting Priority
Low — memecoin markets are highly regime-dependent and difficult to backtest meaningfully. Better suited for live paper trading at $1 scale.

---

*Brief derived from: I Built 3 Trading Bots That Run 24⧸7 (Here's What They Made While I Slept).txt*
