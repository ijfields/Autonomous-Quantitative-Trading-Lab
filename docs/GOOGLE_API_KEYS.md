# Google Gemini API Key Setup Guide

This guide explains how to set up and manage Google Gemini API keys for the Autonomous Trading Laboratory.

## Table of Contents
- [Creating API Keys](#creating-api-keys)
- [Free Tier Limits](#free-tier-limits)
- [Multi-Key Rotation Strategy](#multi-key-rotation-strategy)
- [Environment Configuration](#environment-configuration)
- [Common Errors & Solutions](#common-errors--solutions)
- [Best Practices](#best-practices)

---

## Creating API Keys

### Step 1: Access Google AI Studio
1. Go to [Google AI Studio](https://aistudio.google.com/app/apikey)
2. Sign in with your Google account

### Step 2: Create a New API Key
1. Click **"Create API Key"** button
2. Select a Google Cloud project (or create a new one)
3. Copy the generated key immediately - it won't be shown again

### Step 3: Repeat for Multiple Keys
For production use, create **3 separate API keys** to enable rotation:
- Each key can be in the same project or different projects
- Different projects = separate rate limit quotas (recommended)

**Tip**: Use different Google accounts for completely isolated quotas.

---

## Free Tier Limits

Google Gemini free tier has the following limits per API key:

| Metric | Limit | Notes |
|--------|-------|-------|
| Requests per Minute (RPM) | 15 | Hard limit, returns 429 |
| Tokens per Minute | 1,000,000 | Rarely hit before RPM |
| Tokens per Day | 1,500,000 | Resets at midnight PT |
| Requests per Day | 1,500 | ~100 requests/hour sustained |

### Calculating Capacity

With **3 keys** using rotation:
- Effective RPM: ~45 requests/minute (15 x 3)
- Effective daily requests: ~4,500 (1,500 x 3)
- With backoff delays: ~30-35 RPM sustained

This is sufficient for running 1-2 research agents continuously.

---

## Multi-Key Rotation Strategy

The system uses automatic key rotation with exponential backoff:

```
Key 1 (active) → Rate limit hit → Key 2 (active) → Rate limit hit → Key 3 (active)
       ↑                                                                    |
       └────────────────── After cooldown period ───────────────────────────┘
```

### How It Works
1. **Normal operation**: Uses first available key
2. **Rate limit (429)**: Marks key as "hot", switches to next key
3. **All keys hot**: Waits with exponential backoff (30s, 60s, 120s, max 300s)
4. **Key cooldown**: After 60 seconds, key becomes available again

### Configuration

In `.env`:
```bash
# Research agents use these keys
RESEARCH_KEYS=key1,key2,key3

# Backtest agents use separate keys (optional)
BACKTEST_KEYS=key4,key5,key6
```

Separating research and backtest keys prevents the two agent types from exhausting each other's quotas.

---

## Environment Configuration

### Minimal Setup (Single Key)
```bash
RESEARCH_KEYS=AIzaSy...your_key_here
BACKTEST_KEYS=AIzaSy...your_key_here
```

### Recommended Setup (Multi-Key)
```bash
# 3 keys for research agents
RESEARCH_KEYS=AIzaSyA...,AIzaSyB...,AIzaSyC...

# 3 keys for backtest agents (can be same or different)
BACKTEST_KEYS=AIzaSyD...,AIzaSyE...,AIzaSyF...

# Model configuration
MODEL_FAST=gemini-2.5-flash-lite    # High quota, used for Scout
MODEL_SMART=gemini-2.5-flash        # Better reasoning, used for Sniper/Coder
```

### Model Selection

| Agent Phase | Model | Why |
|-------------|-------|-----|
| Scout | MODEL_FAST | High throughput, simple searches |
| Sniper | MODEL_SMART | Better reasoning for strategy analysis |
| Coder | MODEL_SMART | Code generation requires precision |

---

## Common Errors & Solutions

| Error Code | Message | Cause | Solution |
|------------|---------|-------|----------|
| **429** | Resource exhausted | Rate limit hit | Automatic: Key rotation + backoff. Manual: Add more keys |
| **500** | Internal error | Google server issue | Automatic: Retry with backoff. Usually transient |
| **503** | Service unavailable | Google overloaded | Automatic: Retry. If persistent, check Google status |
| **403** | Forbidden | Invalid key or quota | Check key is valid, has Gemini API enabled |
| **400** | Bad request | Malformed request | Check prompt size, usually a bug |

### Error Handling Flow

```
API Call → 429/500/503 Error
    ↓
Mark current key as "hot"
    ↓
Get next available key
    ↓
If all keys hot:
    ↓
Wait (exponential backoff: 30s → 60s → 120s → 300s max)
    ↓
Retry with cooled key
```

### Debugging Rate Limits

Check the logs for patterns:
```bash
# View research agent logs
tail -f logs/research_agent_1_ops.log | grep "429\|Rotating"
```

If you see constant rotation, you need more keys or slower operation.

---

## Best Practices

### 1. Use Separate Projects
Create API keys in different Google Cloud projects for isolated quotas:
- Project A: Research keys
- Project B: Backtest keys

### 2. Monitor Usage
Check Google Cloud Console for usage patterns:
1. Go to [Google Cloud Console](https://console.cloud.google.com/)
2. Select your project
3. Navigate to **APIs & Services** > **Credentials**
4. Click on your API key to see usage metrics

### 3. Set Quotas (Optional)
In Google Cloud Console, you can set custom quotas to prevent unexpected bills if you upgrade:
1. Go to **APIs & Services** > **Quotas**
2. Find "Gemini API"
3. Set daily request limits

### 4. Secure Your Keys
- Never commit `.env` files to git
- Use environment variables in production
- Rotate keys periodically (every 3-6 months)

### 5. Handle Graceful Degradation
If all keys are exhausted:
- The system will pause research (not crash)
- Resume automatically when quotas reset
- Check logs for "All keys exhausted" messages

---

## Troubleshooting

### "No API keys found" on startup
```
CRITICAL: No API keys found in .env
```
**Solution**: Ensure `RESEARCH_KEYS` is set in your `.env` file.

### Constant 429 errors despite rotation
**Cause**: All keys from same project share quota.
**Solution**: Create keys in different Google Cloud projects.

### Keys work in curl but fail in app
**Cause**: Environment not loaded.
**Solution**: Ensure `.env` is in the correct directory (`research_backtesting_agentsV2/`).

### "Forbidden" on specific URLs during web scraping
**Cause**: Some websites block automated scrapers (403).
**Note**: This is not an API key issue. The web tools handle this gracefully.

---

## Quick Reference

```bash
# Test a key works
curl -H "Content-Type: application/json" \
     -H "x-goog-api-key: YOUR_API_KEY" \
     "https://generativelanguage.googleapis.com/v1beta/models?key=YOUR_API_KEY"

# Check current environment
grep "KEYS" .env

# Verify keys are loaded (in Python)
python -c "import os; from dotenv import load_dotenv; load_dotenv(); print(len(os.getenv('RESEARCH_KEYS','').split(',')))"
```

---

## Related Documentation
- [Google AI Studio](https://aistudio.google.com/)
- [Gemini API Documentation](https://ai.google.dev/docs)
- [Rate Limits Reference](https://ai.google.dev/pricing)
