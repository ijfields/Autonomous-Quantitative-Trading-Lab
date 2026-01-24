# Contributing to the Autonomous Trading Laboratory

Thank you for your interest in contributing! This project is an ambitious attempt to create a self-improving quantitative trading system.

## 🤝 How to Contribute

### 1. Reporting Bugs
- Use the **Issues** tab.
- detailed description of the error.
- Include logs from `research_backtesting_agentsV2/logs/` if relevant.

### 2. Feature Requests
- We welcome ideas for new:
    - **Research Niches:** New areas for the agent to scout.
    - **Alpha Signals:** Improved mathematical models.
    - **Dashboard Visualizations:** Better ways to view backtest results.

### 3. Pull Requests
1. **Fork** the repo.
2. Create a new branch: `git checkout -b feature/amazing-idea`.
3. Commit changes.
4. Push to your fork.
5. Submit a **Pull Request**.

## 🛠️ Development Setup

1. **Environment:**
   - Python 3.12+ (Anaconda recommended)
   - Node.js 18+ (for Dashboard)
   - Docker (for Database/SearXNG)

2. **First Run:**
   ```bash
   cp .env.example .env
   docker compose up -d
   conda activate pydantic_ai_env
   python research_backtesting_agentsV2/research_main.py
   ```

## 🧪 Testing
- Run `python research_backtesting_agentsV2/analyze_crashes.py` to check for regression errors in backtests.
- Ensure the Dashboard builds: `cd research_backtesting_dashboard && npm run build`.

## 📜 Code Style
- **Python:** Follow PEP 8.
- **TypeScript:** Use the existing ESLint configuration.

Happy Coding! 🚀
