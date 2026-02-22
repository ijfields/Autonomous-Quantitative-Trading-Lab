# Step-by-Step Guide: Futures Options Weekly Strangle ($2,000/Week Income Strategy)

## Prerequisites

- **Broker:** Futures-enabled brokerage account (e.g., Interactive Brokers) with margin approval for selling naked puts and calls on futures
- **Capital:** Minimum $2,500-$3,000 per micro contract for margin. Small accounts (under $5K): 1-2 contracts. Larger accounts (100K+): $2,000+/week target
- **Instruments:** S&P 500 E-mini Micro futures options (MES symbol), weekly expirations (7-10 DTE)
- **Knowledge:** Options Greeks (delta, theta), strangles, futures assignment mechanics, Fibonacci retracement basics
- **Tools:** Charting platform, spreadsheet tracker, broker options chain access
- **Time:** 15 minutes every Sunday at 6 PM ET (futures market open), optional mid-week check

---

## Step-by-Step Process

### Step 1: Understand the Core Strategy and Edge

- OTM options expire worthless most of the time -- this is your edge
- Delta approximates probability: 20-delta = ~80% chance of expiring worthless
- You act as "insurance writer" or "casino" -- collecting premium from hedgers/speculators
- Institutions buy puts as portfolio protection; you sell that insurance
- Avoid zero-DTE as a buyer -- most 0-DTE buyers lose

> Speaker tip: "Instead of being the person that is chasing the out the money option, why don't we sell it?"

### Step 2: Choose the Right Instrument

- Use micro e-mini S&P 500 futures (MES symbol) for options trading
- Futures market opens Sunday 6 PM ET -- after-hours access unavailable with equity options
- ~$2,000-$3,000 margin per micro contract
- S&P 500 eliminates single-stock risk; assignment means buying the index at a deep discount

> Speaker tip: "The futures market is open at Sunday at 6 PM."

### Step 3: Determine Position Size by Account Size

- **Under $5K:** 1 micro contract/week, target $50/week
- **$5K-$50K:** 2-10 contracts/week, scale gradually
- **$50K-$100K+:** 20-30 put contracts + calls, target $2,000-$3,000/week
- Only sell what you can hold if assigned; start conservatively

> Speaker tip: "If you have a small account less than 5K... try to get $50 a week and you build your way up."

### Step 4: Sell Three Laddered Put Layers (Sunday 6 PM ET)

- **Layer 1:** ~10 delta, ~4%+ below market, heaviest size
- **Layer 2:** ~15 delta, ~3-3.2% below market, medium size
- **Layer 3:** ~20 delta, ~2.5-2.6% below market, lightest size
- Align strikes with Fibonacci support levels; target 7-10 DTE

> Speaker tip: "I sell three layers of out the money puts every week. This is the core."

- Example (Nov 30, S&P ~6900): 6600 puts (~$1,000), 6660 puts (~$700), 6700 puts (~$900)

### Step 5: Set Up the Call Side (Optional)

- Sell calls at 5-7 delta, ~3%+ above market
- One layer, simpler than put side; optional but adds $500-$1,000/week
- Covered if you hold long S&P 500 futures

> Speaker tip: "The calls I adjust. I do very far delta. Sometimes five, six, seven delta."

- Example: 7070 calls for ~$740

### Step 6: Verify Total Premium and Risk

- Sum all layers; confirm meets weekly target
- Verify max assignment exposure within account capacity
- Market must stay between call and lowest put strike for full profit

> Speaker tip: "As long as the market stays between these lines, I'm going to make profit."

### Step 7: Monitor and Manage During the Week

- **Easiest:** Let expire worthless, collect full premium
- **Profit target:** Close at 50% or 75% of max profit
- **Hedging:** Use Fibonacci levels and delta management
- Do not panic on interim unrealized losses

> Speaker tip: "The easiest way is to just let them expire and you collect all the profit."

### Step 8: Handle Assignment

- Accept assigned futures contracts -- long S&P 500 at 2-5% discount
- Sell covered calls against position (wheel strategy)
- Laddered entry provides favorable blended average cost
- S&P 500 historically recovers from pullbacks

> Speaker tip: "You're basically getting paid to wait."

### Step 9: Track Every Trade

- Record date, strikes, deltas, contracts, premium, expiration, outcome
- Track put and call sides separately; update weekly
- Speaker uses free public Google Sheet tracker

### Step 10: Scale Gradually

- Speaker went from hundreds/week to $2,000+/week over 8 months
- Scale only after consistent profitability; start skeptically small
- Reinvest premium into LEAPS, shares, or other positions

> Speaker tip: "In the beginning, I was very skeptical. I really started off small."

---

## Common Pitfalls

1. **Oversizing too early** -- sell only what you can hold if assigned
2. **Panicking on interim drawdowns** -- premium spikes are normal on pullbacks
3. **Ignoring delta discipline** -- stay in 10-20 delta range for puts, 5-7 for calls
4. **Skipping the tracker** -- document every trade from day one
5. **Using spreads** -- speaker advises against them (too little premium)
6. **Buying zero-DTE** -- most buyers lose; the edge is in selling
7. **Not willing to hold assignment** -- must genuinely accept S&P 500 at a discount
8. **Neglecting Fibonacci support** -- adds confluence beyond raw delta
9. **Starting too big psychologically** -- build emotional tolerance gradually
10. **Missing Sunday 6 PM window** -- maximizes theta decay from earliest entry

---

## Quick Reference: Weekly Execution Checklist

- [ ] Sunday 6:00 PM ET: Log into broker
- [ ] Open MES options chain (7-10 DTE)
- [ ] Sell Put Layer 1: ~10 delta, furthest OTM, heaviest size
- [ ] Sell Put Layer 2: ~15 delta, middle, medium size
- [ ] Sell Put Layer 3: ~20 delta, closest to ATM, lightest size
- [ ] Sell Calls: ~5-7 delta, ~3% above market
- [ ] Verify total premium meets target
- [ ] Log trades in spreadsheet
- [ ] Mid-week: brief check only
- [ ] Expiry: confirm expired worthless, update P&L
- [ ] Repeat next Sunday

---

## Resources

| Resource | Type | Description |
|----------|------|-------------|
| tradingwarss.com | Website | Indicators and Discord access |
| TradingWarz Discord | Community | Live Sunday alerts and Fibonacci setups |
| Free Google Sheet Tracker | Spreadsheet | Public trade log, updated 1-2x/week |
| TradingWarz Substack | Newsletter | Weekly performance updates |
| Interactive Brokers (implied) | Broker | Futures-enabled with mobile app |

*Extracted from: My Futures Options Trading Routine for a Quick 2000 per Week.txt*
