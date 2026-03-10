# learning to set env variables inline before running python — Complete Transcript Analysis

**Video Title:** learning to set env variables inline before running python
**Channel:** Moon Dev
**Video ID:** igp-nAvs0Ug
**Upload Date:** 2026-03-10
**Duration:** ~2.5m (~156s)
**Speaker:** Moon Dev
**Platform:** YouTube

---

## EXECUTIVE SUMMARY

A short informal clip where Moon Dev discovers that you can set environment variables inline before a Python command in the shell (e.g., `ENABLE_H3=1 python script.py`). He discusses how this differs from changing Python constants directly — the inline variables only set environment variables for that single command invocation, not permanent shell variables. The bridge pattern: use `os.environ.get()` in Python to read the shell env variable and assign it to a constant.

---

## KEY TOPICS

### Inline Environment Variables

- **Syntax:** `VAR_NAME=value python script.py`
- Sets environment variable for that single command only — does not persist in shell
- Can chain multiple: `ENABLE_H3=1 ENABLE_ORDER_TEST=1 python script.py`
- Does NOT change Python constants directly — only environment variables

### The Bridge Pattern

```python
import os
MY_CONSTANT = os.environ.get("MY_VAR", default_value)
```

- Shell sets env variable → Python reads it via `os.environ` → code uses it as effective constant
- Without this bridge, inline env vars have no effect on Python code

---

## TOOLS & PLATFORMS MENTIONED

| Tool/Platform | Purpose |
|---------------|---------|
| Python | Programming language |
| Shell/Bash | Command-line environment variables |

---

## ACTIONABLE TAKEAWAYS

1. **Inline env vars** are scoped to a single command — useful for toggling behavior without editing code
2. **Must use `os.environ.get()`** in Python to read them — they don't auto-replace constants
3. **Useful for trading bots:** Toggle features like `ENABLE_H3=1` or `ORDER_TEST=1` without modifying source

---

## SOURCE QUOTES

> "Five years in. Just learned that today, March 7th."

*Analysis derived from: learning to set env variables inline before running python.txt*
