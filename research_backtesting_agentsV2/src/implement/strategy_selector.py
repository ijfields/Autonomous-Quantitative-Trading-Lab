"""
Strategy Selector
==================
Selects the best performing strategies from the database for live trading.

This module:
1. Queries BacktestResult for profitable strategies
2. Ranks by Sharpe Ratio and consistency across assets
3. Returns deployment-ready strategy configs
"""

import logging
from typing import List, Dict, Any, Optional
from sqlalchemy import select, desc
from sqlalchemy.orm import selectinload

from src.common.database import get_session
from src.common.models import Strategy, BacktestResult, StrategyResult, StrategyStatus

logger = logging.getLogger("StrategySelector")


async def get_top_strategies(
    min_sharpe: float = 1.0,
    min_win_rate: float = 50.0,
    limit: int = 5
) -> List[Dict[str, Any]]:
    """
    Fetches the top performing strategies from the database.
    
    Args:
        min_sharpe: Minimum Sharpe ratio threshold
        min_win_rate: Minimum win rate percentage
        limit: Maximum number of strategies to return
        
    Returns:
        List of strategy configs ready for deployment
    """
    async for session in get_session():
        # Query for COMPLETED strategies with PROFITABLE results
        stmt = (
            select(BacktestResult)
            .join(Strategy)
            .where(Strategy.status == StrategyStatus.COMPLETED)
            .where(BacktestResult.result_rating == StrategyResult.PROFITABLE)
            .where(BacktestResult.sharpe_ratio >= min_sharpe)
            .where(BacktestResult.win_rate >= min_win_rate)
            .order_by(desc(BacktestResult.sharpe_ratio))
            .limit(limit)
        )
        
        result = await session.execute(stmt)
        backtest_results = result.scalars().all()
        
        if not backtest_results:
            logger.warning("⚠️ No profitable strategies found matching criteria.")
            return []
        
        # Build deployment configs
        deployment_configs = []
        for bt in backtest_results:
            config = {
                "strategy_id": bt.strategy_id,
                "symbol": bt.symbol,
                "timeframe": bt.timeframe,
                "code": bt.code,
                "optimized_params": bt.optimized_params or {},
                "sharpe_ratio": bt.sharpe_ratio,
                "win_rate": bt.win_rate,
                "total_return_pct": bt.total_return_pct,
                "max_drawdown_pct": bt.max_drawdown_pct,
            }
            deployment_configs.append(config)
            logger.info(f"✅ Selected Strategy {bt.strategy_id} | {bt.symbol} ({bt.timeframe}) | Sharpe: {bt.sharpe_ratio:.2f}")
        
        return deployment_configs


async def get_strategy_by_id(strategy_id: int) -> Optional[Dict[str, Any]]:
    """
    Fetches a specific strategy's best backtest result for deployment.
    """
    async for session in get_session():
        stmt = (
            select(BacktestResult)
            .where(BacktestResult.strategy_id == strategy_id)
            .order_by(desc(BacktestResult.sharpe_ratio))
            .limit(1)
        )
        
        result = await session.execute(stmt)
        bt = result.scalars().first()
        
        if not bt:
            logger.warning(f"⚠️ No backtest results found for strategy {strategy_id}")
            return None
        
        return {
            "strategy_id": bt.strategy_id,
            "symbol": bt.symbol,
            "timeframe": bt.timeframe,
            "code": bt.code,
            "optimized_params": bt.optimized_params or {},
            "sharpe_ratio": bt.sharpe_ratio,
            "win_rate": bt.win_rate,
        }
