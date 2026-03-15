# Step-by-Step Guide: Your Guide To Local AI -- Hardware, Setup and Models

**Source:** Syntax (YouTube)
**Video ID:** QKdKcFjjZhE
**Upload Date:** 2026-03-12

---

## What This Guide Covers

A complete walkthrough of running LLMs locally: hardware selection, Linux setup, inference engine installation, model selection, and practical usage patterns for Q&A, web search, and coding workflows.

---

## Step 1: Understand the Basics

1. **Inference** = taking a trained model and running new text through it to get predictions. This is what you do when you chat with an LLM. Training/fine-tuning is a separate (harder) task.
2. **GPUs are required** because LLMs are large matrices of numbers that benefit enormously from parallel processing.
3. **VRAM is the bottleneck.** A 70B parameter model at full (16-bit) precision needs ~140 GB of VRAM. The entire model must fit in VRAM for fast inference.
4. **Quantization** reduces model precision (16-bit to 8-bit or 4-bit), dramatically shrinking memory requirements. A 70B model at 4-bit quantization needs ~30 GB. Quality decreases slightly with lower precision.
5. You also need VRAM for the **key-value cache** (vectorized prompt history), so plan for model size + cache headroom.

---

## Step 2: Choose Your Hardware

**Option A: Dedicated GPU**
- Nvidia RTX 6000 (48 GB VRAM): ~$7,000 for the card alone.
- Nvidia RTX Pro 6000 (96 GB VRAM): ~$10,000.
- AMD GPUs may be cheaper for similar VRAM but have compatibility tradeoffs.
- You still need CPU, RAM, motherboard, etc. on top of the GPU cost.

**Option B: Unified Memory Platforms (recommended for most users)**
- **Nvidia DGX Spark:** 128 GB unified memory, ~$4,000. Good option but relatively new.
- **AMD Strix Halo (Ryzen AI 395):** 128 GB unified memory. Available in multiple form factors:
  - GMK Tech Evo X2: ~$2,500 (the choice in this video).
  - Framework Desktop, Minis Forum, HP machines: slightly more expensive.
- **Apple Mac Studio:** 128 GB (or 256/512 GB) unified memory. Apple was first with unified architecture (M1 in 2020). More expensive than AMD options. Limited to macOS.

**The video's choice:** GMK Tech Evo X2 with AMD Strix Halo, 128 GB unified memory, purchased for $2,100 (prices have since risen to ~$2,500).

---

## Step 3: Set Up the Operating System

1. The GMK Tech Evo X2 ships with Windows, but **Fedora Linux** is recommended for best compatibility with local AI tooling.
2. Create a USB drive with the Fedora installer.
3. Boot from USB, go through BIOS settings:
   - Set performance mode.
   - Allocate memory for the GPU.
   - Check the Strix Halo wiki and forums for recommended BIOS settings.
4. Install Fedora. Enable the administration tools option during install.
5. On first boot, Fedora's **Cockpit** web dashboard is available -- access it from any browser on your network to manage the machine remotely (terminal, status, configuration).
6. **Configure GTT (memory allocation):**
   - Allocate up to 108 GB for the GPU (Jeff Geerling's guide helps, but Strix Halo has different options).
   - Keep ~20 GB for the OS and other processes.
   - Going above 108 GB can cause kernel panics.

---

## Step 4: Install the Inference Engine

Several options exist:
- **Ollama:** Popular CLI tool, easy model downloads, good for beginners.
- **LM Studio:** Desktop app with ChatGPT-like interface, also has CLI.
- **VLLM:** For clustering/networking multiple machines at scale.
- **Llama.cpp:** Fastest in benchmarks, pioneered the GGUF format. **Recommended.**

**Recommended: Llama.cpp via the AMD Strix Halo Toolbox**
1. Install the Toolbox CLI (community project by Kuzo).
2. The toolbox uses Docker/Podman to package pre-compiled Llama.cpp with all required AMD drivers.
3. Two options: **Vulkan** (open-source AMD drivers) or **ROCm** (proprietary drivers). ROCm gives better performance.
4. Run one command to spin up the toolbox environment.
5. Llama.cpp is ready to go inside the toolbox -- fully optimized, no manual compilation needed.

---

## Step 5: Select and Download Models

1. Install the Hugging Face CLI: `pip install huggingface-hub` (gives you the `hf` command).
2. Go to the Hugging Face models page and filter by "Llama.cpp" to see compatible models.
3. **Check model sizes** against your available VRAM:
   - Kimmy K2.5 at full precision: 2 TB (way too large).
   - Minimax M2.5 at 3-bit quant: 101 GB (fits but limits context size).
   - **Qwen 3 Coder 30B at 4-bit quant: under 20 GB** (plenty of room for large context windows). **Recommended starting point.**
   - Qwen 3.5: also excellent for general use.
4. Download with: `huggingface-cli download [model-repo] --local-dir [path]`
5. **Unsloth** provides many pre-quantized models with setup guides -- a great resource for finding the right model/quantization combo.

---

## Step 6: Set Up User Interfaces

**For basic Q&A and web search:**
1. Install **Open Web UI** and connect it to your Llama.cpp server.
2. Enable the web search tool so the model can ground answers in real-time web results.
3. This replaces ChatGPT/Claude/Gemini for basic question-answering and web-grounded summarization.

**For coding (agentic workflows):**
1. Install **VS Code Insider** (the pre-release version -- required for agentic workflows with local models).
2. Install the **Continue** extension (Copilot replacement). Point it at your local Llama.cpp endpoint.
3. Alternatively, use **Open Code** for the best local AI coding experience -- it supports sub-agents, has a web-based dashboard, and integrates with tools like Beads (task management) and Spec Kit (spec-driven development).

---

## Step 7: Get the Best Results from Local Models

Local models are less capable than cloud models like Claude Opus 4.6. Compensate with structure:

1. **Spec-driven development:** Write detailed specs before coding. Do not give vague prompts.
2. **Sub-agent workflows:** Use tools that break tasks into smaller, isolated units of work.
3. **Extensive test suites:** Let the model verify its own work via tests, linting, and type checking.
4. **Isolated work units:** Have the model work on one thing at a time in a try-things-test-repeat cycle.
5. **Be specific:** Local models reward clarity even more than cloud models.

**What works well locally:** Basic Q&A, CLI command generation, simple code questions, web search and summarization, privacy-sensitive prompts.

**What still needs cloud models:** Complex multi-step reasoning, unguided project creation from vague prompts, tasks requiring maximum quality.

---

## Step 8: Evaluate the Tradeoffs

**Advantages of local AI:**
- One-time hardware cost instead of monthly subscription.
- No data sent to AI companies (complete privacy).
- Models improve over time -- new releases make the same hardware more capable.
- Unlimited usage with no token costs.

**Disadvantages:**
- Requires more setup and maintenance than cloud services.
- Complex coding tasks need significantly more guard rails and handholding.
- Initial hardware investment is $2,000-$4,000+.
- Cannot fully replace Claude Opus 4.6 or equivalent for advanced work (yet).

---

## Key Takeaway

> Local AI has reached the point where it fully replaces cloud subscriptions for basic Q&A, web search, and privacy-sensitive prompts. For serious coding work, it requires structured workflows with specs, tests, and sub-agents to stay on track. The exciting part is that the hardware you buy today will only get more capable as new models release -- and the models are getting smaller and better every month.

*Guide derived from: You Guide To Local AI | Hardware, Setup and Models.txt*
