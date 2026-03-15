# Step-by-Step Guide: Claude Code + OpenRouter = FREE Forever (No RAM Needed)

**Source:** Efran | AI Automation (YouTube)
**Video ID:** Shkx096xonQ
**Upload Date:** 2026-03-11

---

## What This Guide Covers

How to run Claude Code completely for free by connecting it to free cloud-hosted models through OpenRouter, with no local RAM or GPU requirements.

---

## Step 1: Install Claude Code

1. Ensure you have Claude Code installed on your computer.
2. If not already installed, follow the official Anthropic installation instructions for your OS.

---

## Step 2: Create a Project Folder and Settings File

1. Open your code editor (Cursor, VS Code, AntiGravity, etc.).
2. Create a new folder for your project (e.g., `cloud`).
3. Inside that folder, create a file named `settings.json`.
4. Add the following JSON structure:
   ```json
   {
     "apiKey": "YOUR_OPENROUTER_API_KEY",
     "model": "MODEL_NAME_HERE"
   }
   ```

---

## Step 3: Get an OpenRouter API Key

1. Go to [openrouter.ai](https://openrouter.ai) and create a free account.
2. Navigate to **Settings > API Keys**.
3. Click **Create a new key**.
4. Copy the API key.
5. Paste it into the `apiKey` field in your `settings.json`.
6. Note: No credits are needed for free models. You will have $0 balance and it still works.

---

## Step 4: Choose a Free Model

1. On OpenRouter, go to the Models page and filter for **free** LLMs.
2. Available free models include:
   - **QPOS 120B** -- 120 billion parameters, free (would require 65 GB RAM locally)
   - **Qwen Coder** -- free coding-focused model
   - **Qwen 3/40B** -- free (would require 290 GB RAM locally)
3. Copy the model identifier string (e.g., `qwen/qwen-coder-free`).
4. Paste it into the `model` field in `settings.json`.
5. Save the file.

---

## Step 5: Launch Claude Code with the Free Model

1. Open a terminal in your project folder.
2. Launch Claude Code.
3. It should now display that it is using your chosen free model.
4. Send a test message to verify it is working.

---

## Step 6: Handle Rate Limits with the Free Models Router

1. If you see "too many requests" errors, the specific free model is overloaded.
2. Go back to OpenRouter's Models page and scroll to the bottom.
3. Find **Free Models Router** -- this automatically rotates between all available free models.
4. Copy the Free Models Router identifier.
5. Update your `settings.json` with the new model name.
6. Relaunch Claude Code -- requests will now route to whichever free model is available.

---

## Step 7: Upgrade to a Budget Model (Optional)

1. For better quality than free models, consider **MiniMax 2.5**:
   - Ranked #1 in programming category on OpenRouter
   - Cost: 30 cents per million input tokens, 95 cents per million output tokens
   - Compare: Opus 4.6 costs $5 / $25 per million tokens (input/output)
2. Copy the MiniMax 2.5 model name from OpenRouter.
3. Paste into `settings.json`.
4. You will need to add credits to your OpenRouter account for paid models.
5. You can also use Anthropic models (e.g., Claude Sonnet, Opus) through OpenRouter if you prefer.

---

## Key Takeaway

> "Using one API key from OpenRouter you can get access to hundreds of different AI models which also includes the free models." The free models router is the most reliable way to use Claude Code for free, while MiniMax 2.5 offers the best quality-to-cost ratio for those willing to spend a small amount.

*Guide derived from: Claude Code + OpenRouter = FREE Forever (No RAM Needed).txt*
