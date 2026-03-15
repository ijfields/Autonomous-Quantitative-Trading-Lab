# Step-by-Step Guide: This Is the Most Underrated Feature of Claude Code

**Source:** Mark Kashef (YouTube)
**Video ID:** 04zBiBqzKQA
**Upload Date:** 2026-03-13

---

## What This Guide Covers
How to use the built-in Claude Code Guide sub-agent across five levels -- from basic questions to autonomous diagnosis and repair of broken Claude Code configurations.

---

## Step 1: Access the Claude Code Guide (Level 1 -- Basic Q&A)
1. Open a Claude Code session in your terminal.
2. In the prompt area, tag the Claude Code Guide by typing its reference (e.g., mentioning the claude code guide).
3. Ask a simple question such as "How do I change my model mid-session?"
4. The guide spins up a sub-agent that searches the official documentation without consuming your main context window.
5. Review the response -- it will provide the exact command (e.g., `/model` to switch between Sonnet and Opus).
6. Try conceptual questions like "How do CLAUDE.md files work? Can I have a global one and folder-level ones?"

## Step 2: Diagnose Your CLAUDE.md (Level 2 -- Configuration Audit)
1. Tag the Claude Code Guide in your prompt.
2. Also tag your local `CLAUDE.md` file by referencing its path.
3. Write a prompt like: "I keep having to repeat myself to Claude about how I want my code formatted and where to save things. Why isn't my CLAUDE.md helping me? What's missing?"
4. The guide will read your CLAUDE.md and diagnose issues such as:
   - Lack of code formatting instructions
   - Missing file organization rules
   - Absence of do/don't patterns (positive and negative prompting)
5. Apply the suggested improvements to your CLAUDE.md.

## Step 3: Understand the Hooks System (Level 3 -- Deep Mechanics)
1. Tag the Claude Code Guide again.
2. Ask: "What types of hooks are available in Claude Code? I want to understand what actions I can attach to automations."
3. Review the 17 hook event types returned, including:
   - Session start / session end
   - Pre-compact / pre-submit
   - Pre-tool-use / post-tool-use
   - File creation events
4. Study the JSON structure required for each hook type.

## Step 4: Build Custom Commands and Hooks (Level 4 -- Creation)
1. Tag the Claude Code Guide.
2. Provide a prompt like: "I want to create a custom slash command called /standup that looks at what I worked on in my last session and writes a three-bullet summary. Also set up a relevant hook. Actually do it yourself."
3. The guide will:
   - Create the slash command file in the appropriate directory
   - Set up a hook (e.g., session-start notification)
   - Configure the settings.json properly
4. Verify the hook fires by opening a new terminal session.

## Step 5: Fix Broken Configurations (Level 5 -- Autonomous Repair)
1. Open Claude Code and note any hook errors displayed at startup.
2. Tag the Claude Code Guide.
3. Drag and drop (or reference) the broken files into your prompt.
4. Describe the problem, e.g.: "My archive hook saves plans with random names. I want plans named with a short description of what they are about and organized by date."
5. The guide will:
   - Read the documentation for the latest hook and plan file conventions
   - Diagnose missing wrappers, commands, or paths in your hook configuration
   - Fix the settings.json file
   - Rename existing plan files from random names to meaningful descriptions
6. Verify the fix by opening a new terminal -- the hook error should be gone.

---

## Key Takeaway

> The Claude Code Guide is a built-in sub-agent that can answer questions, audit configurations, build custom commands, and autonomously fix broken setups -- all without leaving your Claude Code session or consuming your main context window.

*Guide derived from: This Is the Most Underrated Feature of Claude Code [04zBiBqzKQA].en.vtt*
