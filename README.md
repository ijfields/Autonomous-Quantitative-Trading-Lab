# 🤖 Autonomous Quantitative Trading Laboratory

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.12+-blue?style=for-the-badge&logo=python" alt="Python">
  <img src="https://img.shields.io/badge/Next.js-14-black?style=for-the-badge&logo=next.js" alt="Next.js">
  <img src="https://img.shields.io/badge/PostgreSQL-pgvector-336791?style=for-the-badge&logo=postgresql" alt="PostgreSQL">
  <img src="https://img.shields.io/badge/AI-Gemini%203-4285F4?style=for-the-badge&logo=google" alt="Gemini">
</p>

An **end-to-end autonomous system** that discovers alpha in academic papers, GitHub repositories, and trading forums, then rigorously backtests strategies using a professional event-driven engine.

---

## 🚀 Quick Start Guide

 Follow these steps to get running in 5 minutes.

### 1. Prerequisites
*   **Docker Desktop** (or Engine) installed and running.
*   **Conda** (Miniconda or Anaconda) installed.
*   **Google AI Studio API Keys** (Free tier works).

### 2. Clone & Configure
```bash
git clone <your-repo-url>
cd research_backtesting_agents-Project

# Create .env from template
cp .env.example .env

# Edit .env and paste your Google API Keys
nano .env 
```

### 3. Start Infrastructure (Database + Search)
Runs PostgreSQL (with pgvector) and SearXNG (Meta-Search Engine).
```bash
docker compose up -d
```

### 4. Setup Python Environment (The Agents)
```bash
# Create Environment
conda create -n pydantic_ai_env python=3.12 -y
conda activate pydantic_ai_env

# Install Dependencies
pip install -r requirements.txt

# Initialize Database
python -c "from research_backtesting_agentsV2.src.common.database import init_db; import asyncio; asyncio.run(init_db())"
```

### 5. Launch the Dashboard (Optional but Recommended)
```bash
cd research_backtesting_dashboard
npm install
npm run build
npm start
```
*   Access at: `http://localhost:3000`

---

## 🏃 Autonomous Mode (CLI)

Run the agents directly if you don't want to use the dashboard controls.

**Mode A: Deep Research (Scout & Sniper)**
Auto-discovers strategies 24/7.
```bash
# Make sure you are in the root directory
conda activate pydantic_ai_env
python research_backtesting_agentsV2/research_main.py
```

**Mode B: Backtesting Pipeline**
Picks up discovered strategies and tests them.
```bash
python research_backtesting_agentsV2/backtest_main.py
```

---

## 📂 Project Structure

```
.
├── .env                     # Global Configuration (Secrets, Ports)
├── docker-compose.yml       # Infrastructure (DB, SearXNG)
├── research_backtesting_agentsV2/   # 🧠 Python Agents
│   ├── research_main.py     # Research Loop
│   ├── backtest_main.py     # Backtest Loop
│   └── src/                 # Core Logic
└── research_backtesting_dashboard/  # 📊 Next.js UI
```

---

## 🐛 Troubleshooting

*   **Database Connection Failed?** Check if Docker is running (`docker ps`).
*   **API Quota Errors?** Add more keys to `RESEARCH_KEYS` in `.env`.
*   **Connection Issues?** Run the diagnostic tool:
    ```bash
    python check_connection.py
    ```

---

## 📜 License
MIT License. See [LICENSE](LICENSE) for details.