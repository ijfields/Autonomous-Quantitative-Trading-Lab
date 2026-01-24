"""
Base Broker Adapter
===================
Abstract base class for exchange/broker integrations.

Subclasses should implement concrete adapters for:
- Hyperliquid (Crypto)
- Alpaca (Stocks)
- Interactive Brokers (Multi-asset)
"""

from abc import ABC, abstractmethod
from typing import Dict, Any, Optional, List
from dataclasses import dataclass
from enum import Enum
import logging

logger = logging.getLogger("BrokerAdapter")


class OrderSide(Enum):
    BUY = "buy"
    SELL = "sell"


class OrderType(Enum):
    MARKET = "market"
    LIMIT = "limit"


@dataclass
class Position:
    """Represents an open position."""
    symbol: str
    size: float
    entry_price: float
    unrealized_pnl: float
    is_long: bool


@dataclass  
class Order:
    """Represents an order."""
    order_id: str
    symbol: str
    side: OrderSide
    size: float
    price: Optional[float]
    order_type: OrderType
    status: str


class BaseBrokerAdapter(ABC):
    """
    Abstract base class for broker/exchange adapters.
    
    Implementations:
    - HyperliquidAdapter (crypto perpetuals)
    - AlpacaAdapter (US stocks)
    - IBKRAdapter (multi-asset)
    """
    
    def __init__(self, api_key: str, api_secret: Optional[str] = None):
        self.api_key = api_key
        self.api_secret = api_secret
        self.is_connected = False
    
    @abstractmethod
    async def connect(self) -> bool:
        """Establish connection to the broker."""
        pass
    
    @abstractmethod
    async def disconnect(self) -> None:
        """Close connection to the broker."""
        pass
    
    @abstractmethod
    async def get_account_balance(self) -> Dict[str, float]:
        """Get account balance/equity."""
        pass
    
    @abstractmethod
    async def get_positions(self) -> List[Position]:
        """Get all open positions."""
        pass
    
    @abstractmethod
    async def get_position(self, symbol: str) -> Optional[Position]:
        """Get position for a specific symbol."""
        pass
    
    @abstractmethod
    async def place_order(
        self,
        symbol: str,
        side: OrderSide,
        size: float,
        order_type: OrderType = OrderType.MARKET,
        price: Optional[float] = None,
        stop_loss: Optional[float] = None,
        take_profit: Optional[float] = None
    ) -> Order:
        """Place an order."""
        pass
    
    @abstractmethod
    async def cancel_order(self, order_id: str) -> bool:
        """Cancel an order."""
        pass
    
    @abstractmethod
    async def close_position(self, symbol: str) -> bool:
        """Close a position."""
        pass
    
    @abstractmethod
    async def get_current_price(self, symbol: str) -> float:
        """Get current market price for a symbol."""
        pass


class PaperTradingAdapter(BaseBrokerAdapter):
    """
    Paper trading adapter for testing strategies without real money.
    Simulates order execution and position tracking.
    """
    
    def __init__(self, initial_balance: float = 100_000):
        super().__init__(api_key="paper")
        self.balance = initial_balance
        self.positions: Dict[str, Position] = {}
        self.orders: List[Order] = []
        self.order_counter = 0
    
    async def connect(self) -> bool:
        logger.info("📄 Paper Trading Mode - Connected")
        self.is_connected = True
        return True
    
    async def disconnect(self) -> None:
        logger.info("📄 Paper Trading Mode - Disconnected")
        self.is_connected = False
    
    async def get_account_balance(self) -> Dict[str, float]:
        return {
            "balance": self.balance,
            "equity": self.balance + sum(p.unrealized_pnl for p in self.positions.values())
        }
    
    async def get_positions(self) -> List[Position]:
        return list(self.positions.values())
    
    async def get_position(self, symbol: str) -> Optional[Position]:
        return self.positions.get(symbol)
    
    async def place_order(
        self,
        symbol: str,
        side: OrderSide,
        size: float,
        order_type: OrderType = OrderType.MARKET,
        price: Optional[float] = None,
        stop_loss: Optional[float] = None,
        take_profit: Optional[float] = None
    ) -> Order:
        self.order_counter += 1
        order_id = f"PAPER-{self.order_counter}"
        
        # For paper trading, immediately "fill" market orders
        order = Order(
            order_id=order_id,
            symbol=symbol,
            side=side,
            size=size,
            price=price or 0,  # Would fetch real price in live mode
            order_type=order_type,
            status="filled" if order_type == OrderType.MARKET else "pending"
        )
        
        self.orders.append(order)
        logger.info(f"📄 Paper Order Placed: {side.value.upper()} {size} {symbol}")
        
        # Simulate position creation for market orders
        if order_type == OrderType.MARKET:
            self.positions[symbol] = Position(
                symbol=symbol,
                size=size if side == OrderSide.BUY else -size,
                entry_price=price or 0,
                unrealized_pnl=0,
                is_long=side == OrderSide.BUY
            )
        
        return order
    
    async def cancel_order(self, order_id: str) -> bool:
        for order in self.orders:
            if order.order_id == order_id:
                order.status = "cancelled"
                logger.info(f"📄 Paper Order Cancelled: {order_id}")
                return True
        return False
    
    async def close_position(self, symbol: str) -> bool:
        if symbol in self.positions:
            del self.positions[symbol]
            logger.info(f"📄 Paper Position Closed: {symbol}")
            return True
        return False
    
    async def get_current_price(self, symbol: str) -> float:
        # In paper mode, return placeholder
        # Real implementation would fetch from exchange
        return 0.0
