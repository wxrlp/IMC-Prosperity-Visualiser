import os
import sys
import json
import numpy as np
import pandas as pd
from pathlib import Path
from typing import Dict, List, Any, Optional
from dataclasses import dataclass

# Path setup for datamodel
SCRIPT_DIR = Path(__file__).resolve().parent
PROJECT_ROOT = SCRIPT_DIR.parent
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from datamodel import Listing, OrderDepth, TradingState, Observation, Order

@dataclass
class BacktestResult:
    final_pnl: float
    sharpe: float
    max_drawdown: float
    history: List[Dict[str, Any]]
    final_pnl_by_product: Dict[str, float]

class AdvancedMatchingEngine:
    def __init__(self, latency_ticks: int = 0, slippage_prob: float = 0.0):
        self.latency_ticks = latency_ticks
        self.slippage_prob = slippage_prob
        self.limits = {
            "ASH_COATED_OSMIUM": 80, 
            "INTARIAN_PEPPER_ROOT": 80,
            "HYDROGEL_PACK": 80,
            "VELVETFRUIT_EXTRACT": 80
        }
        
    def run_backtest(self, trader_file: str, data_file: str) -> BacktestResult:
        # Load trader
        import importlib.util
        spec = importlib.util.spec_from_file_location("trader_bt", trader_file)
        trader_mod = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(trader_mod)
        trader = trader_mod.Trader()

        # Load data
        df = pd.read_csv(data_file, sep=";")
        df = df.sort_values("timestamp")
        
        cash = 0
        positions = {p: 0 for p in self.limits}
        pnl_history = []
        trader_state_data = ""
        
        listings = {p: Listing(p, p, "XIRECS") for p in self.limits}
        
        # Order buffer for latency simulation
        order_queue = [] # List of (timestamp_to_execute, orders)

        for ts, group in df.groupby("timestamp"):
            order_depths = {}
            for _, row in group.iterrows():
                p = row['product']
                if p not in self.limits: continue
                depth = OrderDepth()
                for i in range(1, 4):
                    if not pd.isna(row[f'bid_price_{i}']): 
                        depth.buy_orders[int(row[f'bid_price_{i}'])] = int(row[f'bid_volume_{i}'])
                    if not pd.isna(row[f'ask_price_{i}']): 
                        depth.sell_orders[int(row[f'ask_price_{i}'])] = -int(row[f'ask_volume_{i}'])
                order_depths[p] = depth
            
            state = TradingState(
                timestamp=ts,
                traderData=trader_state_data,
                market_trades={},
                order_depths=order_depths,
                position=positions.copy(),
                own_trades={},
                listings=listings,
                observations=Observation({}, {})
            )
            
            # Run trader
            new_orders, _, trader_data = trader.run(state)
            trader_state_data = trader_data
            
            # Add to queue with latency
            execution_ts = ts + (self.latency_ticks * 100) # Assuming 100ms per tick
            order_queue.append((execution_ts, new_orders))
            
            # Execute orders that are ready
            ready_orders = [o for o in order_queue if o[0] <= ts]
            order_queue = [o for o in order_queue if o[0] > ts]
            
            for _, orders in ready_orders:
                for p, order_list in orders.items():
                    if p not in order_depths: continue
                    for o in order_list:
                        # Slippage check
                        if np.random.random() < self.slippage_prob:
                            continue
                            
                        if o.quantity > 0: # Buy
                            best_ask = min(order_depths[p].sell_orders.keys()) if order_depths[p].sell_orders else None
                            if best_ask is not None and o.price >= best_ask:
                                fill = min(o.quantity, abs(order_depths[p].sell_orders[best_ask]), self.limits[p] - positions[p])
                                if fill > 0:
                                    positions[p] += fill
                                    cash -= fill * best_ask
                        else: # Sell
                            best_bid = max(order_depths[p].buy_orders.keys()) if order_depths[p].buy_orders else None
                            if best_bid is not None and o.price <= best_bid:
                                fill = min(abs(o.quantity), order_depths[p].buy_orders[best_bid], positions[p] + self.limits[p])
                                if fill > 0:
                                    positions[p] -= fill
                                    cash += fill * best_bid
            
            # Calculate current PnL
            current_pnl = cash
            for p in positions:
                if p in order_depths and order_depths[p].buy_orders and order_depths[p].sell_orders:
                    mid = (max(order_depths[p].buy_orders.keys()) + min(order_depths[p].sell_orders.keys())) / 2
                    current_pnl += positions[p] * mid
            
            pnl_history.append(current_pnl)
            
        # Final calculations
        pnl_series = np.array(pnl_history)
        final_pnl = pnl_series[-1]
        
        # Max Drawdown
        running_max = np.maximum.accumulate(pnl_series)
        drawdowns = running_max - pnl_series
        max_dd = np.max(drawdowns)
        
        # Sharpe (simplified daily)
        returns = np.diff(pnl_series)
        sharpe = np.mean(returns) / np.std(returns) * np.sqrt(252) if np.std(returns) > 0 else 0
        
        return BacktestResult(
            final_pnl=final_pnl,
            sharpe=round(float(sharpe), 3),
            max_drawdown=round(float(max_dd), 2),
            history=[{"pnl": float(p)} for p in pnl_series[::100]], # Downsample for visualizer
            final_pnl_by_product={"ASH_COATED_OSMIUM": 0.0, "INTARIAN_PEPPER_ROOT": 0.0} # TODO: Track per product
        )
