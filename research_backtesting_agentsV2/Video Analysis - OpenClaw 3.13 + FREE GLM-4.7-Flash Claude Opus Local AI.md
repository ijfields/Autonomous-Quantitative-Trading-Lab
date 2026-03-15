# Video Analysis: OpenClaw 3.13 + FREE GLM-4.7-Flash Claude Opus Local AI

**Speaker:** Julian Goldie
**Channel:** Julian Goldie SEO
**Video ID:** 70MEfCwuyZA
**Upload Date:** 2026-03-14
**Duration:** 20 min 47 sec

---

## Summary

Julian Goldie covers two distinct topics in this video. The first half walks through the OpenClaw 3.13 update (released March 13, 2026), detailing all the new features and fixes. The headline feature is live Chrome session attachment, which allows the AI agent to browse the web using your real browser with your logged-in accounts -- Gmail, dashboards, and tools -- rather than an empty ghost browser. Two new browser profiles are included: "Profile User" (your real signed-in browser) and "Chrome Relay" (a special extension for smoother connections). Additional updates include a complete Android app redesign, iOS welcome screen improvements, Docker timezone configuration via the `openclaw_tz` environment variable, Windows gateway stability fixes, security improvements, and Ollama local model fixes where internal reasoning thoughts no longer leak into chat responses.

The second half introduces GLM-4.7-Flash distilled with Claude Opus 4.5 high reasoning -- a free, open-source model available on Hugging Face that attempts to bring Claude Opus-level reasoning to local hardware. Julian explains knowledge distillation: 250 examples of Claude Opus 4.5 working through hard problems at maximum reasoning were used to train GLM-4.7-Flash to think similarly. He demonstrates running the model via LM Studio on a Mac Studio. While he is candid that it is not as good as the real Claude Opus 4.5, he notes it is useful for privacy-sensitive tasks, high-volume repetitive tasks, and experimentation. He introduces the "Distilled Edge Framework" for deciding when to use local models versus cloud models, and mentions that local models can power OpenClaw agents directly.

## Key Topics

- OpenClaw 3.13 release changelog and new features
- Live Chrome session attachment (real logged-in browser access)
- Browser profiles: Profile User and Chrome Relay
- Android and iOS app redesigns
- Docker timezone configuration (`openclaw_tz`)
- Windows gateway stability fixes
- Ollama/local model internal thinking leak fix
- GLM-4.7-Flash distilled with Claude Opus 4.5 high reasoning
- Knowledge distillation process (250 training examples)
- LM Studio for running local models
- Distilled Edge Framework: when to use local vs. cloud models
- Mixture of Experts (MoE) architecture in GLM-4.7 (30B parameters)

## Tools & Technologies Mentioned

- OpenClaw 3.13 (free open-source AI agent platform)
- Chrome DevTools Protocol (for live browser attachment)
- Docker (container deployment with timezone support)
- Ollama (local model runtime)
- LM Studio (desktop app for running Hugging Face models locally)
- GLM-4.7-Flash (ZhipuAI base model, 30B parameters, MoE architecture)
- Claude Opus 4.5 (source of distilled reasoning)
- Hugging Face (model repository)
- Mac Studio (hardware used for demo)
- Telegram, Discord, Slack, iMessage (OpenClaw communication channels)
- GenSpark Claw, Manis, MaxClaw, KimClaw (hosted OpenClaw alternatives)

## Strategies Found

No specific trading strategies with concrete entry/exit rules were presented.

## Notable Quotes / Insights

- "The Lobster doesn't just see the web anymore. It walks right in, logged in, signed in, and ready to work."
- On the distilled model: "Do I think this is as good as something like Claude Opus 4.5? No. But it is very interesting to see how powerful local models like this are developing."
- The Distilled Edge Framework: Local models are best for privacy-sensitive data, high-volume repetitive tasks, speed over quality, and experimentation. Cloud models are best for highest-quality output, complex multi-step reasoning, and tasks requiring real-time web access.
- "Local models respond to the same prompting principles as cloud models, but they reward clarity even more."

## Actionable Takeaways

1. Update OpenClaw to 3.13 by typing "update" inside the chat -- no manual reinstallation needed.
2. Enable live Chrome session attachment to let your AI agent browse the web using your logged-in accounts (via Chrome DevTools Protocol toggle).
3. Set the `openclaw_tz` environment variable in Docker to fix timezone-related bugs in scheduled tasks and logs.
4. Download LM Studio to run GLM-4.7-Flash locally for free -- the 18 GB model is available on Hugging Face with various quantization options.
5. Use the Distilled Edge Framework to decide task routing: send privacy-sensitive or high-volume tasks to local models, and reserve cloud models for complex reasoning chains.
6. Local models can be used to power OpenClaw agents directly via Ollama integration.
