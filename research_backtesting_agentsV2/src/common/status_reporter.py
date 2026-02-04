"""
StatusReporter - Real-time agent status reporting for dashboard monitoring.

This module provides a StatusReporter class that writes agent status updates
to the AgentHeartbeat database table, enabling the dashboard to show:
- Current agent status (scouting, sniping, coding, backtesting, etc.)
- Current task description
- Recent errors (rate limits, parse failures, etc.)
- Heartbeat timestamps for liveness detection
"""

import logging
from datetime import datetime
from typing import Optional, List
from sqlalchemy.ext.asyncio import AsyncSession
from sqlmodel import select

from src.common.models import AgentHeartbeat, AgentStatus

logger = logging.getLogger(__name__)


class StatusReporter:
    """
    Reports agent status to the database for real-time dashboard monitoring.

    Usage:
        reporter = StatusReporter(instance_id=1, agent_type="research")
        await reporter.initialize(session)

        await reporter.update_status(AgentStatus.SCOUTING, "Exploring: Momentum Trading")
        await reporter.record_error("rate_limit", "429 Too Many Requests")
        await reporter.heartbeat()
        await reporter.cleanup_on_exit()
    """

    MAX_ERRORS = 10  # Keep only the last 10 errors

    def __init__(self, instance_id: int, agent_type: str):
        """
        Initialize the StatusReporter.

        Args:
            instance_id: Unique instance ID for this agent (1, 2, 3, etc.)
            agent_type: Either "research" or "backtest"
        """
        self.instance_id = instance_id
        self.agent_type = agent_type
        self._heartbeat_record: Optional[AgentHeartbeat] = None
        self._session: Optional[AsyncSession] = None

    async def initialize(self, session: AsyncSession) -> None:
        """
        Initialize or recover the heartbeat record for this agent.
        Creates a new record if none exists, or updates an existing one.

        Args:
            session: SQLAlchemy async session
        """
        self._session = session

        # Check if a record already exists for this instance
        stmt = select(AgentHeartbeat).where(
            AgentHeartbeat.instance_id == self.instance_id,
            AgentHeartbeat.agent_type == self.agent_type
        )
        result = await session.execute(stmt)
        existing = result.scalars().first()

        if existing:
            # Update existing record
            existing.status = AgentStatus.IDLE
            existing.current_task = None
            existing.current_niche = None
            existing.last_heartbeat = datetime.utcnow()
            existing.started_at = datetime.utcnow()
            existing.recent_errors = []
            existing.api_calls_today = 0
            existing.strategies_found_today = 0
            self._heartbeat_record = existing
            logger.info(f"Recovered heartbeat record for {self.agent_type} agent #{self.instance_id}")
        else:
            # Create new record
            self._heartbeat_record = AgentHeartbeat(
                instance_id=self.instance_id,
                agent_type=self.agent_type,
                status=AgentStatus.IDLE,
                started_at=datetime.utcnow(),
                last_heartbeat=datetime.utcnow()
            )
            session.add(self._heartbeat_record)
            logger.info(f"Created heartbeat record for {self.agent_type} agent #{self.instance_id}")

        await session.commit()

    async def update_status(
        self,
        status: AgentStatus,
        task: Optional[str] = None,
        niche: Optional[str] = None,
        session: Optional[AsyncSession] = None
    ) -> None:
        """
        Update the agent's current status.

        Args:
            status: New AgentStatus (SCOUTING, SNIPING, CODING, etc.)
            task: Optional task description (e.g., "Analyzing: RSI Divergence")
            niche: Optional niche being explored (research agents only)
            session: Optional session to use (uses stored session if not provided)
        """
        sess = session or self._session
        if not sess or not self._heartbeat_record:
            logger.warning("StatusReporter not initialized. Call initialize() first.")
            return

        try:
            # Refresh the record to avoid stale data
            await sess.refresh(self._heartbeat_record)

            self._heartbeat_record.status = status
            self._heartbeat_record.current_task = task
            self._heartbeat_record.current_niche = niche
            self._heartbeat_record.last_heartbeat = datetime.utcnow()

            await sess.commit()
            logger.debug(f"Status updated: {status.value} - {task}")
        except Exception as e:
            logger.error(f"Failed to update status: {e}")
            # Don't raise - status reporting should not break the main loop

    async def record_error(
        self,
        error_type: str,
        message: str,
        session: Optional[AsyncSession] = None
    ) -> None:
        """
        Record an error in the recent_errors buffer.

        Args:
            error_type: Type of error (e.g., "rate_limit", "json_parse", "api_error")
            message: Error message/description
            session: Optional session to use
        """
        sess = session or self._session
        if not sess or not self._heartbeat_record:
            logger.warning("StatusReporter not initialized. Call initialize() first.")
            return

        try:
            await sess.refresh(self._heartbeat_record)

            error_entry = {
                "type": error_type,
                "message": message[:500],  # Truncate long messages
                "timestamp": datetime.utcnow().isoformat()
            }

            # Get current errors and add new one
            errors = list(self._heartbeat_record.recent_errors or [])
            errors.append(error_entry)

            # Keep only last MAX_ERRORS
            if len(errors) > self.MAX_ERRORS:
                errors = errors[-self.MAX_ERRORS:]

            self._heartbeat_record.recent_errors = errors
            self._heartbeat_record.status = AgentStatus.ERROR
            self._heartbeat_record.last_heartbeat = datetime.utcnow()

            await sess.commit()
            logger.debug(f"Error recorded: {error_type} - {message[:50]}...")
        except Exception as e:
            logger.error(f"Failed to record error: {e}")

    async def heartbeat(self, session: Optional[AsyncSession] = None) -> None:
        """
        Update the heartbeat timestamp to indicate the agent is still alive.
        Call this at the end of each processing cycle.

        Args:
            session: Optional session to use
        """
        sess = session or self._session
        if not sess or not self._heartbeat_record:
            return

        try:
            await sess.refresh(self._heartbeat_record)
            self._heartbeat_record.last_heartbeat = datetime.utcnow()
            await sess.commit()
        except Exception as e:
            logger.error(f"Heartbeat failed: {e}")

    async def increment_api_calls(self, count: int = 1, session: Optional[AsyncSession] = None) -> None:
        """Increment the API calls counter."""
        sess = session or self._session
        if not sess or not self._heartbeat_record:
            return

        try:
            await sess.refresh(self._heartbeat_record)
            self._heartbeat_record.api_calls_today += count
            await sess.commit()
        except Exception as e:
            logger.error(f"Failed to increment API calls: {e}")

    async def increment_strategies_found(self, count: int = 1, session: Optional[AsyncSession] = None) -> None:
        """Increment the strategies found counter."""
        sess = session or self._session
        if not sess or not self._heartbeat_record:
            return

        try:
            await sess.refresh(self._heartbeat_record)
            self._heartbeat_record.strategies_found_today += count
            await sess.commit()
        except Exception as e:
            logger.error(f"Failed to increment strategies found: {e}")

    async def cleanup_on_exit(self, session: Optional[AsyncSession] = None) -> None:
        """
        Mark the agent as stopped on graceful shutdown.
        Call this in your signal handler or cleanup code.

        Args:
            session: Optional session to use
        """
        sess = session or self._session
        if not sess or not self._heartbeat_record:
            return

        try:
            await sess.refresh(self._heartbeat_record)
            self._heartbeat_record.status = AgentStatus.STOPPED
            self._heartbeat_record.current_task = "Shutdown"
            self._heartbeat_record.last_heartbeat = datetime.utcnow()
            await sess.commit()
            logger.info(f"Agent {self.agent_type} #{self.instance_id} marked as STOPPED")
        except Exception as e:
            logger.error(f"Cleanup failed: {e}")


# Convenience function to create a StatusReporter with a new session
async def create_status_reporter(
    instance_id: int,
    agent_type: str,
    session: AsyncSession
) -> StatusReporter:
    """
    Factory function to create and initialize a StatusReporter.

    Args:
        instance_id: Agent instance ID
        agent_type: "research" or "backtest"
        session: Database session

    Returns:
        Initialized StatusReporter instance
    """
    reporter = StatusReporter(instance_id, agent_type)
    await reporter.initialize(session)
    return reporter
