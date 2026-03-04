# Step-by-Step Guide: Anti-Slop Framework for AI Coding Agents

**Source:** Jaymin West (YouTube)
**Video ID:** 88FC685v7ac
**Upload Date:** 2026-03-02

---

## What This Guide Covers

A comprehensive framework for preventing AI coding agents (Claude Code, etc.) from writing low-quality code ("slop") in your codebase. Covers 6 tools and 6 techniques used by top agentic engineers, including patterns from Stripe's production agent workflows.

**Core philosophy:** "One agent, one task, one prompt." A focused agent is a correct agent.

---

## Mindset Shift

Before implementing any tools or techniques:

1. **Stop assuming LLM code = slop.** The models are capable of high-quality code.
2. **If agents write bad code, it's an engineering problem**, not an LLM problem. Fix the system.
3. **Rule #1: Never fix bad output.** If an agent produces bad results:
   - Diagnose what went wrong
   - Reset/scrap the agent run
   - Fix the root cause (prompt, spec, configuration)
   - Rerun from scratch
   - Do NOT patch bad code -- it creates technical debt

---

## Tools (Set Up These First)

### Tool 1: Hooks

**What:** Automated checks that run at specific points in the agent workflow.

**How to implement:**
1. Set up **pre-commit hooks** (e.g., via `pre-commit` framework or Claude Code hooks):
   - Run all tests
   - Run linter
   - Run type checker
2. Set up **Claude Code hooks** in `.claude/settings.json`:
   - Log every tool call
   - Block destructive commands before they execute
   - Custom validation on file writes

### Tool 2: Quality Gates

**What:** Enforce the strictest possible code quality standards.

**How to implement:**
1. Configure your linter at the **strictest level** (LLMs handle strict rules better than humans)
2. Enable the **strictest type-checking** (e.g., `strict: true` in tsconfig, `mypy --strict` for Python)
3. Require **100% test pass rate** -- no exceptions, no skipping
4. All gates must pass before:
   - Agent work is passed to the next agent
   - Code is pushed to remote
   - Any PR is created

### Tool 3: Anti-Mocking Testing

**What:** Prevent agents from writing tests that mock everything (and thus test nothing).

**How to implement:**
1. Add to your CLAUDE.md / agent instructions: **"Never mock what you can use for real"**
2. Require integration tests over unit tests with mocks
3. Set a **high coverage threshold** (80%+ recommended)
4. Require **100% pass rate** -- fix immediately or scrap the run
5. Review generated tests to ensure they actually test real behavior

### Tool 4: Standardization

**What:** Keep all agent artifacts organized in predictable locations.

**How to implement:**
1. Define **one location** for issues/tasks (e.g., GitHub Issues, not scattered TODOs)
2. Define **one location** for agent learnings/notes (e.g., `.claude/` directory)
3. Define **one location** for work output (prevent 600 random markdown files)
4. Define **review process**: who reviews agent work? (other agents? human PR review?)

### Tool 5: Per-Agent Isolation (Worktrees)

**What:** Each agent works in its own isolated copy of the repo.

**How to implement:**
1. Always run agents in **git worktrees** (`git worktree add`)
2. In Claude Code: use the worktree feature or Task tool with `isolation: "worktree"`
3. **"An isolated agent is a safe agent"** -- prevents agents from overwriting each other
4. Critical when running swarms or multi-agent workflows
5. Merge worktree changes via PR after human review

### Tool 6: Hard Blocks

**What:** Define what agents are NEVER allowed to do.

**How to implement:**
1. **Always block `git push`** -- no pushing to remote without human verification
2. Define **tool restrictions per agent role**:
   - Scout agents: read-only (no file writes)
   - Build agents: write + test (no deploy)
   - Review agents: read + comment (no write)
3. Block destructive commands: `rm -rf`, `git reset --hard`, `DROP TABLE`, etc.
4. Implement via hooks (hard blocks as code)

---

## Techniques (Apply These to Your Workflow)

### Technique 1: Traceability

Track every agent action:
- What agent made what changes
- When the changes were made
- Where the changes were made
- Implement via hooks that log all tool calls

### Technique 2: Task Decomposition

**"One agent, one task, one prompt"** (credited to Indie Dev Dan)

1. Break complex tasks into single-purpose units
2. Each agent gets exactly one prompt that carries it to completion
3. Do NOT give an agent multiple unrelated tasks
4. A focused agent is a correct agent
5. When single-task success rate is high, you can trust agents more

### Technique 3: Pit of Success

1. Input tokens essentially "finetune" the LLM for your project
2. **Garbage in → garbage out**: if your codebase has slop, agents write more slop
3. **Recursive improvement**: cleaner code → agents write cleaner code → even cleaner code
4. Invest upfront in codebase quality -- it pays compound returns via agent output

### Technique 4: Specs (No Ambiguity)

1. Specs should leave **zero ambiguity** for the agent
2. Never let agents infer your intent
3. Include in specs:
   - Exact file paths and line numbers
   - Exact function/class names
   - Code snippets where relevant
   - Expected behavior and edge cases
   - What is explicitly out of scope
4. More detail = better results
5. Spec writing is a skill -- improves with practice

### Technique 5: Multi-Agent Workflows

1. Chain agents: decompose → build → test → review → integrate
2. **Quality checks at every handoff**:
   - After build agent: tests + linting + types must pass
   - After review agent: issues flagged and resolved
   - At coordinator level: everything has been checked at every step
3. No slop should survive the chain

### Technique 6: Agent Scope

1. Explicitly define **what files** the agent should work on
2. Explicitly define **what is out of scope** (leave for other agents)
3. Reduce ambiguity: agent must know "this is the ONLY thing I should work on"
4. If an agent encounters out-of-scope problems, it should report them, not fix them

---

## Quick Reference Checklist

```
BEFORE RUNNING AGENTS:
[ ] CLAUDE.md / system prompt is detailed and project-specific
[ ] Linting configured at strictest level
[ ] Type-checking at strictest level
[ ] Pre-commit hooks running tests + lint + types
[ ] Anti-mocking instruction in agent prompts
[ ] git push blocked for agents
[ ] Worktree isolation enabled
[ ] Agent roles defined with tool restrictions

FOR EACH AGENT RUN:
[ ] One agent, one task, one prompt
[ ] Spec is unambiguous (exact files, lines, behavior)
[ ] Agent scope is clearly defined (in-scope and out-of-scope)
[ ] Quality gates pass before handoff to next agent

AFTER AGENT COMPLETES:
[ ] All tests passing (100%)
[ ] Linting passing
[ ] Type-checking passing
[ ] Human review via PR
[ ] Traceability: changes logged and attributed

IF AGENT PRODUCES BAD OUTPUT:
[ ] Do NOT fix the output
[ ] Diagnose root cause
[ ] Scrap the run
[ ] Fix the root cause (prompt, spec, config)
[ ] Rerun from scratch
```

*Guide derived from: How Top Engineers Stop AI Agents From Writing Slop.txt*
