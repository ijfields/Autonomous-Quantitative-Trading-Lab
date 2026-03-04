# How Top Engineers Stop AI Agents From Writing Slop - Complete Transcript Analysis

**Video Title:** How Top Engineers Stop AI Agents From Writing Slop
**Channel:** Jaymin West
**Video ID:** 88FC685v7ac
**Upload Date:** 2026-03-02
**Duration:** ~12m05s
**Speaker:** Jaymin West (agentic engineer, public builder on GitHub)
**Platform:** YouTube

---

## EXECUTIVE SUMMARY

A comprehensive overview of anti-slop tools and techniques for running AI coding agents (particularly Claude Code) in production codebases. Jaymin West covers the mindset shift ("LLM slop is an engineering problem, not an LLM problem"), then walks through 6 tools (hooks, quality gates, anti-mocking testing, standardization, per-agent isolation, hard blocks) and 6 techniques (traceability, task decomposition, pit of success, specs, multi-agent workflows, agent scope). The core philosophy is "one agent, one task, one prompt" (credited to Indie Dev Dan) and "never fix bad output -- diagnose, reset, and rerun." References Stripe's article on using agents in production. No trading strategies -- this is an agentic engineering best practices guide.

---

## KEY TOPICS

### Mindset Shift
- **"LLM code ≠ slop"** -- if agents write bad code, it's an engineering problem
- Models are capable enough to write high-quality code
- **Rule #1: Never fix bad output** -- diagnose the root cause, scrap the run, fix the issue, rerun from scratch
- Don't accumulate technical debt from agents -- reset and try again

### Tools (6)

#### 1. Hooks
- First layer of defense for agentic engineering
- Pre-commit hooks: run tests, check linting before any commit
- Custom harnesses around agents for logging and destructive change prevention
- Closely related to hard blocks (hooks enforce hard blocks as code)

#### 2. Quality Gates
- **Strictest possible linting** -- LLMs can handle strict rules better than humans
- **Strictest possible type-checking** -- enforce types at the strictest level
- **100% test pass rate** -- every test must pass before moving to next agent or pushing to remote
- Shift from "relaxed for humans" to "strict for agents"

#### 3. Anti-Mocking Testing Philosophy
- Guiding principle: **"Never mock, which you can use for real"**
- LLMs love to mock things in tests -- the tests end up not testing actual code
- Bake anti-mocking philosophy into every agent's instructions
- High coverage rate required
- 100% pass rate -- fix immediately or scrap the agent run

#### 4. Standardization
- Issues tracked in one location
- Agent learnings stored in one location (avoid 600 markdown files scattered across project)
- Standardize where agents do their work
- Standardize how work is reviewed (other agents? human PR review?)

#### 5. Per-Agent Isolation
- **"An isolated agent is a safe agent"**
- Always run agents in **worktrees** -- prevents agents from overwriting each other
- Critical for swarms and multi-agent workflows
- Becomes more important as agent count scales

#### 6. Hard Blocks
- Define what agents should **never** be allowed to do
- Example: **always block `git push`** -- no pushing to remote without human verification
- Tool restrictions by agent role: scout agents can only read files, not write
- Force correct behavior -- catch agents that go off-task early and reset them
- Implemented via hooks (hard blocks as code)

### Techniques (6)

#### 1. Traceability
- Track: what agent made what changes, when, and where
- Hooks enable tracing every single action of every agent
- Essential for debugging and accountability

#### 2. Task Decomposition
- **"One agent, one task, one prompt"** (credited to Indie Dev Dan)
- **"A focused agent is a correct agent"**
- One prompt should carry the agent all the way to task completion
- When success rate goes up with this approach, you can place more trust in agents

#### 3. Pit of Success
- Long-standing software engineering concept, amplified for agents
- Input tokens essentially "finetune" the LLM for your project
- **Garbage in → garbage out** -- if your codebase is clean, agents write cleaner code
- **Recursive loop**: higher quality code → agents produce higher quality code → even better code

#### 4. Specs
- **"Specs should leave no ambiguity to the agent"**
- Don't let agents infer anything about your intent
- Include: exact line numbers, exact file names, code snippets
- More detailed spec = better agent output
- Spec writing is a skill that takes practice

#### 5. Multi-Agent Workflows / Swarms
- Series of agents: decomposing tasks → building → reviewing → integrating
- **Quality checks at every handoff** -- tests, linting, type-checking must pass before passing work to the next agent
- By the time code reaches the coordinator/orchestration agent, every step has been quality-checked
- No slop in the chain

#### 6. Agent Scope
- **What files should the agent work on?** Define explicitly.
- **What is outside scope?** Agent should leave out-of-scope problems for other agents.
- Reduce ambiguity: agent must know "this is the only thing I should be working on"
- Ties together specs, task decomposition, and hard blocks

### Standardization (Technique)
- Agent output should **never surprise you**
- Prompt structure, tool usage, output format -- all standardized
- **Chain of command** in swarms: when does the developer need to come back into the loop?
- Decision points for escalation are vital

---

## TOOLS & PLATFORMS MENTIONED

| Tool | Purpose |
|------|---------|
| Claude Code | Primary AI coding agent |
| Git worktrees | Per-agent isolation (prevent overwriting) |
| Pre-commit hooks | Quality gates (tests, linting) |
| Strict linting/type-checking | Quality enforcement |
| Stripe (article) | Reference for agents in production at scale |
| Promptra | Jaymin West's community for agentic engineering |
| GitHub (Jaymin West) | Public repositories with anti-slop patterns |

---

## ANTI-SLOP CHECKLIST (Summary)

| Category | Item | Implementation |
|----------|------|----------------|
| **Mindset** | LLM slop = engineering problem | Fix the system, not the output |
| **Rule #1** | Never fix bad output | Diagnose → reset → fix root cause → rerun |
| **Tool** | Hooks | Pre-commit: tests, linting, type-checking |
| **Tool** | Quality gates | Strictest linting + type-checking + 100% test pass |
| **Tool** | Anti-mocking tests | Never mock what you can use for real |
| **Tool** | Standardization | One location for issues, learnings, work |
| **Tool** | Per-agent isolation | Always use worktrees |
| **Tool** | Hard blocks | Block git push, restrict tools per agent role |
| **Technique** | Traceability | Log every agent action via hooks |
| **Technique** | Task decomposition | One agent, one task, one prompt |
| **Technique** | Pit of success | Clean codebase → clean agent output (recursive) |
| **Technique** | Specs | No ambiguity; exact files, lines, snippets |
| **Technique** | Multi-agent workflows | Quality checks at every handoff |
| **Technique** | Agent scope | Define what's in/out of scope per agent |
| **Technique** | Standardization | Agents should never surprise you |

---

## ACTIONABLE TAKEAWAYS

1. **"One agent, one task, one prompt"** -- the single most important principle for preventing slop
2. **Never fix bad output** -- diagnose, scrap, fix root cause, rerun from scratch
3. **Use worktrees** for agent isolation -- prevents agents from stepping on each other
4. **Block `git push`** -- always review agent work before it reaches remote
5. **Strict linting + type-checking** -- LLMs handle strict rules better than humans do
6. **Anti-mocking in tests** -- explicitly instruct agents to never mock what can be tested for real
7. **Detailed specs** with exact file names, line numbers, and code snippets produce dramatically better agent output
8. **Quality checks at every handoff** in multi-agent chains -- no step passes without tests/linting/types passing
9. **Pit of success is recursive** -- investing in codebase quality pays compound returns through better agent output
10. **Standardize everything** -- prompts, output formats, tool usage, chain of command, escalation points

*Analyzed from: How Top Engineers Stop AI Agents From Writing Slop.txt*
