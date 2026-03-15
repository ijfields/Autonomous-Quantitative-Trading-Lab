# Step-by-Step Guide: Your Guide To Local AI -- Hardware, Setup and Models

**Source:** Syntax (YouTube)
**Video ID:** QKdKcFjjZhE
**Upload Date:** 2026-03-12

---

## What This Guide Covers
How to select hardware, install an OS, configure GPU memory, set up Llama CPP, download models, and use local AI for prompting, coding, and agentic workflows.

---

## Step 1: Understand Key Concepts
1. **Inference**: Taking a pre-trained model and passing in new text to predict output. This is what you are doing when using local AI.
2. **VRAM requirements**: Models must fit entirely into VRAM for fast processing. A 70B parameter model at full (16-bit) precision needs 140GB; at 4-bit quantization, approximately 30-35GB.
3. **Key-value cache**: In addition to model size, you need extra VRAM for the KV cache (pre-calculated vectors for prompt processing). More VRAM = longer context windows.
4. **Quantization**: Reducing model precision (16-bit to 8-bit to 4-bit) makes models smaller and faster at the cost of slight quality reduction.

## Step 2: Choose Your Hardware
1. **Option A -- Discrete GPU**: An RTX 6000 with 48GB VRAM costs approximately $7,000; an RTX Pro 6000 with 96GB costs approximately $10,000. Best performance but most expensive.
2. **Option B -- Nvidia DGX Spark**: 128GB unified memory, approximately $4,000. A dedicated local AI machine from Nvidia.
3. **Option C -- AMD Strix Halo** (recommended by CJ): GMK Tech Evo X2 with Ryzen AI 395 processor, 128GB unified memory, approximately $2,100-$2,500. Best value.
4. **Option D -- Apple Silicon Mac**: Mac Studio with 128GB+ unified memory. Similar capability but typically $1,000+ more than AMD Strix Halo machines.
5. Key consideration: Mac locks you to macOS; AMD/Intel PCs can run Linux for broader community support and packages.

## Step 3: Install and Configure the OS
1. Boot the machine (it may come with Windows pre-installed).
2. Create a USB drive with the Fedora installer.
3. Enter BIOS and update settings:
   - Enable performance mode
   - Allocate maximum memory to the GPU (for Strix Halo: up to 108GB for GPU, leaving 20GB for OS/system)
   - Apply recommended settings from community forums/wikis
4. Install Fedora (or Ubuntu if preferred).
5. Enable the Cockpit web dashboard during install for remote administration via browser.
6. Configure GTT settings to allocate GPU memory (108GB for GPU, stable; more may cause kernel panics).

## Step 4: Set Up the Model Runtime
1. **Recommended: Llama CPP** (fastest in benchmarks, pioneered the GGUF format).
2. For AMD Strix Halo, use the Strix Halo Toolbox by Kuzo:
   - Install the toolbox CLI
   - Run one command to spin up the ROCm toolbox (ROCm outperforms Vulkan in tests)
   - Llama CPP is pre-compiled and optimized inside the toolbox
3. Alternative runtimes: Ollama (CLI-based, easy to use), LM Studio (desktop app with chat interface), vLLM (for clustering/scaling).

## Step 5: Download and Run Models
1. Install the Hugging Face CLI for model downloads.
2. Go to the Hugging Face models page and filter by "Llama CPP" compatibility.
3. Recommended starting models:
   - **Qwen 3 Coder 30B A3B Instruct** (4-bit quant is under 20GB, leaves plenty of room for context)
   - **Qwen 3.5** (strong general-purpose model)
   - **MiniMax M2.5** (3-bit quant at 101GB -- fits but limited context window)
4. Download the model using `hf` CLI commands.
5. Run the model via Llama CPP inside the toolbox.

## Step 6: Use Local AI for Basic Tasks
1. Set up Open WebUI and connect it to your Llama server.
2. Enable the web search tool so prompts can search the web for grounded answers.
3. Use for: basic question-answering, web summarization, CLI command generation, JavaScript/Python questions.
4. This setup can fully replace ChatGPT/Claude/Gemini subscriptions for basic prompting.

## Step 7: Use Local AI for Coding
1. **VS Code**: Install the Continue extension, point it at your local model endpoint. Works like Copilot but uses your local AI. Note: agentic workflows require VS Code Insiders (pre-release version).
2. **Open Code**: Best option for agentic workflows. Supports sub-agents, web-based dashboard, and tool integrations.
3. For best results with local models in coding:
   - Use spec-driven development (write specs before coding)
   - Create extensive test suites for self-verification
   - Enable linting and type checking
   - Use sub-agent orchestration (e.g., Beads for task management, Spec Kit for design)
   - Have the model work on isolated pieces of work at a time
4. Local models need more structure and guard rails than cloud models like Claude Opus 4.6 for complex projects.

## Step 8: Ongoing Model Updates
1. New open-weight models are released frequently (monthly).
2. Each new release can provide better capabilities on the same hardware.
3. Monitor Unsloth, Hugging Face trending models, and community forums for new releases.
4. Keep your cloud subscription for complex projects while expanding local usage over time.

---

## Key Takeaway

> A $2,100 mini PC with 128GB unified memory and an AMD Strix Halo processor can fully replace cloud AI for basic prompting and web search, but complex agentic coding still benefits from cloud models like Claude Opus 4.6 -- the gap is closing with every new model release.

*Guide derived from: You Guide To Local AI | Hardware, Setup and Models [QKdKcFjjZhE].en.vtt*
