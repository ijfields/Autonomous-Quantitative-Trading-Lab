# Step-by-Step Guide: This Is the Most Underrated Feature of Claude Code

**Source:** Mark Kashef (YouTube)
**Video ID:** 04zBiBqzKQA
**Upload Date:** 2026-03-13

---

## What This Guide Covers

How to use the built-in Claude Code Guide sub-agent across five progressive levels -- from basic questions to diagnosing broken hooks and building custom slash commands -- so you never need to leave your session to consult external documentation.

---

## Step 1: Invoke the Claude Code Guide for Basic Questions (Level 1)

1. Open a Claude Code session in your terminal.
2. Tag the Claude Code Guide sub-agent in your prompt (it is a built-in sub-agent, not a plugin).
3. Ask any question about Claude Code features. For example: "How do I change my model mid-session?"
4. The sub-agent spins up, fetches relevant documentation pages, and returns a concise answer (e.g., use the `/model` command to switch from Sonnet to Opus).
5. You can also ask conceptual questions such as: "How do CLAUDE.md files work? Can I have a global one and then folder-level and local versions? Explain it like I'm 10 years old."

**Key point:** The sub-agent runs in its own thread and does not consume your main context window.

---

## Step 2: Diagnose Your CLAUDE.md Configuration (Level 2)

1. Tag the Claude Code Guide sub-agent.
2. Also tag your actual CLAUDE.md file from your project folder (drag and drop or use the `@` reference).
3. Describe the problem: "I keep having to repeat myself to Claude about how I want my code formatted and where to save things. Why isn't my CLAUDE.md helping me? What's missing?"
4. The guide will analyze your CLAUDE.md and diagnose issues such as:
   - It reads like a README with no actionable instructions.
   - Missing code formatting rules (indentation style, naming conventions).
   - Missing file organization rules.
   - No do/don't pattern examples (positive and negative prompting).
5. It will provide a restructured CLAUDE.md template with specific sections for formatting preferences, file organization, and behavioral rules.

---

## Step 3: Understand All Available Hook Event Types (Level 3)

1. Tag the Claude Code Guide sub-agent.
2. Ask: "What types of hooks are available in Claude Code? I want to understand what actions I can attach to automations. Can I trigger something every time a file is created, when a session starts, or when Claude edits something? Walk me through what's possible."
3. The guide will list all 17 hook event types, including:
   - Session start / session end
   - Pre-tool-use / post-tool-use
   - Pre-compact
   - Pre-prompt-submit
   - And more
4. It explains the JSON structure needed for each hook configuration.
5. Use this knowledge to plan which hooks would benefit your workflow before building them.

---

## Step 4: Build a Custom Slash Command and Hook (Level 4)

1. Tag the Claude Code Guide sub-agent.
2. Describe what you want built: "I want to create a custom slash command called `/standup` that looks at what I worked on in my last session and writes a three-bullet summary I can copy and paste into my team's standup chat. Show me how to create the file for this. Actually, do it yourself and set up a relevant hook."
3. The guide will:
   - Create the slash command file with the proper structure.
   - Create a session-start hook (e.g., a Mac OS notification that fires every time a new session begins).
   - Write the settings.json entries needed.
4. Verify the hook works by opening a new terminal session and confirming the notification appears.

---

## Step 5: Debug Broken Hooks and Fix Plan File Naming (Level 5)

1. Start a Claude Code session -- if you see a hook error on startup, this is the problem to fix.
2. Click "Continue without these settings" to enter the session despite the error.
3. Tag the Claude Code Guide sub-agent.
4. Drag and drop the broken hook file(s) and any related directories (e.g., a `past_plans/` folder) into the prompt.
5. Describe the issue: "My archive hook saves plans with random names like 'dizzy-purple-flamingo' and 'jumpy-velvet-penguin'. I want plans archived with a short description of what they're about (e.g., 'add-user-auth') and organized by date."
6. The guide will:
   - Read the documentation on hooks and plan files.
   - Diagnose the broken hook (e.g., missing shell wrapper, incorrect path in settings.json).
   - Fix the settings.json file.
   - Rename all existing plan files from animal names to meaningful descriptions based on their content.
   - Sort them by date.
7. Verify the fix by opening a new terminal session -- the hook error should be gone.

---

## Key Takeaway

> The Claude Code Guide sub-agent is like having a concierge who knows every slash command, every hook event, and every configuration option in the latest version. Instead of Googling or watching tutorials, tag it with your files and let it diagnose, explain, build, and fix things directly inside your session.

*Guide derived from: This Is the Most Underrated Feature of Claude Code.txt*
