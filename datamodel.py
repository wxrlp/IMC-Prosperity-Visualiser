import json
from typing import Dict, List, Any

class Order:
    def __init__(self, symbol: str, price: int, quantity: int) -> None:
        self.symbol = symbol
        self.price = price
        self.quantity = quantity
    def __repr__(self) -> str:
        return f"Order(symbol={self.symbol}, price={self.price}, quantity={self.quantity})"

class OrderDepth:
    def __init__(self) -> None:
        self.buy_orders: Dict[int, int] = {}
        self.sell_orders: Dict[int, int] = {}

class Listing:
    def __init__(self, symbol: str, product: str, denomination: str):
        self.symbol = symbol
        self.product = product
        self.denomination = denomination

class Trade:
    def __init__(self, symbol: str, price: int, quantity: int, buyer: str = "", seller: str = "", timestamp: int = 0) -> None:
        self.symbol = symbol
        self.price = price
        self.quantity = quantity
        self.buyer = buyer
        self.seller = seller
        self.timestamp = timestamp

class Observation:
    def __init__(self, plainValueObservations: Dict[str, int], conversionObservations: Dict[str, float]) -> None:
        self.plainValueObservations = plainValueObservations
        self.conversionObservations = conversionObservations

class TradingState:
    def __init__(self, traderData: str, timestamp: int, listings: Dict[str, Listing], order_depths: Dict[str, OrderDepth], own_trades: Dict[str, List[Trade]], market_trades: Dict[str, List[Trade]], position: Dict[str, int], observations: Observation):
        self.traderData = traderData
        self.timestamp = timestamp
        self.listings = listings
        self.order_depths = order_depths
        self.own_trades = own_trades
        self.market_trades = market_trades
        self.position = position
        self.observations = observations
