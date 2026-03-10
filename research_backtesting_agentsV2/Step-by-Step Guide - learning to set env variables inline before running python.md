# Step-by-Step Guide: Setting Inline Environment Variables for Python Scripts

**Source:** Moon Dev (YouTube)
**Video ID:** igp-nAvs0Ug
**Upload Date:** 2026-03-10

---

## What This Guide Covers

How to set environment variables inline before running a Python script — useful for toggling trading bot features without editing code.

---

## Step 1: Basic Inline Syntax

```bash
VARIABLE_NAME=value python script.py
```

This sets `VARIABLE_NAME` for only that command. It does not persist in your shell.

---

## Step 2: Multiple Variables

```bash
ENABLE_H3=1 ENABLE_ORDER_TEST=1 python my_bot.py
```

Chain as many as needed before the `python` command.

---

## Step 3: Read in Python

```python
import os

ENABLE_H3 = int(os.environ.get("ENABLE_H3", 0))
ENABLE_ORDER_TEST = int(os.environ.get("ENABLE_ORDER_TEST", 0))
```

Without `os.environ.get()`, your Python constants won't be affected.

---

## Key Takeaway

> Inline env vars are a clean way to toggle trading bot behavior per-run without touching source code. Just remember the bridge: shell sets it, `os.environ.get()` reads it.

*Guide derived from: learning to set env variables inline before running python.txt*
