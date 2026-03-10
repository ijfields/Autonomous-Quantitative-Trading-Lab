# Step-by-Step Guide: Building a $100K/mo Chrome Extension with AI

**Source:** Greg Isenberg (YouTube)
**Video ID:** 5lNHx6IC8Fc
**Upload Date:** 2024-10-18

---

## What This Guide Covers

A complete framework for finding Chrome extension business ideas and building them using Claude + Cursor AI — from idea validation to live extension.

---

## Prerequisites

- Claude account (free or paid)
- Cursor AI (paid recommended for higher request limits)
- Google Chrome or Chromium browser (Arc works too)
- Basic familiarity with files/folders (no coding experience required)

---

## Part 1: Finding Ideas

### Method 1: GitHub Issue Mining

1. Browse popular open-source repos on GitHub
2. Look for recurring unresolved issues
3. If a problem keeps appearing → Chrome extension opportunity

### Method 2: Chrome Web Store + AI

1. Go to Chrome Web Store → sort by highest rated
2. Browse popular non-AI extensions
3. Ask: "How can I add AI to this?"
4. AI-ified versions of popular tools = quick differentiation

### Method 3: Product Hunt 1-Star Reviews

1. Search "Chrome extension" on Product Hunt
2. Read the 1-star reviews (not 5-star)
3. 1-star reviews tell you exactly what's broken → fix it in your version

### Method 4: Reddit Pain-Point Alerts

1. Set up IFTTT alert for Reddit posts containing "I wish Chrome could"
2. Get notified automatically when someone expresses a Chrome-related wish
3. Each notification = a potential validated idea

### Method 5: YouTube Tutorial Comments

1. Find popular coding/productivity tutorials
2. Read comments for recurring struggles
3. Build a Chrome extension that solves the common pain point

---

## Part 2: Building the Extension

### Step 1: Generate Initial Code with Claude

1. Open Claude (web interface)
2. Prompt: "I want to build a Chrome extension that [your idea]. Help me build this."
3. Claude will provide: manifest.json, popup.html, popup.js, background.js
4. Copy each file's code

### Step 2: Create Project Files

1. Create a new folder for your extension
2. Create each file Claude specified (manifest.json, popup.html, etc.)
3. Paste the code into each file
4. Save all files

### Step 3: Load in Chrome (Developer Mode)

1. Go to `chrome://extensions` in your browser
2. Enable "Developer Mode" (top right toggle)
3. Click "Load Unpacked"
4. Select your extension folder
5. Extension appears in your toolbar

### Step 4: Test and Iterate with Cursor

1. Open your extension folder in Cursor AI
2. Test the extension — note what doesn't work
3. Tell Cursor what to fix: "Make it so when I click [button], it actually [does thing]"
4. Accept Cursor's changes → reload extension → test again
5. Repeat until working

### Step 5: Polish and Publish

1. Add an icon and description to manifest.json
2. Test across multiple websites
3. Create a Chrome Web Store developer account ($5 one-time fee)
4. Upload your extension
5. Write a compelling description with screenshots

---

## Revenue Models

| Model | Example |
|-------|---------|
| Freemium | Basic features free, premium features paid |
| Subscription | Monthly/annual subscription for full access |
| One-time purchase | Single payment for lifetime access |
| Marketplace evolution | Start as extension → grow into full SaaS (VidIQ model) |

---

## Key Takeaway

> Chrome extensions are the lowest-friction path from idea to revenue. Use Claude for the initial code scaffold, Cursor for iteration, and 1-star reviews for validated problem identification. You don't need to know how to code — AI handles the implementation.

*Guide derived from: Do this to build a $100k/mo chrome extension using AI (Cursor AI, Claude).txt*
