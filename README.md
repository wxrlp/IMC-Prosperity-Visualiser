# ProsperityX Visualizer

Browser-native strategy visualizer for IMC Prosperity. Interactive PnL charts, multi-strategy comparison, and product attribution — zero build step, just open `index.html`.

[![Live Demo](https://img.shields.io/badge/Live-Demo-00ff9d?style=for-the-badge)](https://wxrlp.github.io/IMC-Prosperity-Visualiser/)

## Features

- **Overlay** — Equity curve, KPI cards (PnL / Drawdown / Sharpe), product exposure gauges, and a strategy leaderboard
- **Compare** — Overlay two strategies and visualize the alpha (PnL diff) between them
- **Attribution** — Product-level PnL breakdown with contribution percentages
- **Playback** — Scrub through session ticks to see how metrics evolve over time
- **Multi-source** — Switch between Backtest, Live, I4BT, Real-world, Scenario, and Stress test data

## Quick Start

**Option 1 — GitHub Pages (no install)**

Visit the [live demo](https://wxrlp.github.io/IMC-Prosperity-Visualiser/).

**Option 2 — Local**

```bash
# Clone and open
git clone https://github.com/wxrlp/IMC-Prosperity-Visualiser.git
open IMC-Prosperity-Visualiser/index.html
```

**Option 3 — With the data server** (for dynamic log parsing)

```bash
python3 tools_v2/visualizer_loader_server.py
# Then visit http://127.0.0.1:8765/
```

## Data Format

Drop a `backtest_comparison.js` file alongside `index.html` defining:

```js
const BACKTEST_DATA = {
  "run_id": {
    "trader": "my_trader",
    "day": 0,
    "round": 3,
    "final_pnl": 15000,
    "final_pnl_by_product": { "PRODUCT_A": 10000, "PRODUCT_B": 5000 },
    "history": [{ "ts": 0, "symbol": "PRODUCT_A", "pnl": 0 }, ...]
  }
};
```

Or use `sample_data.js` as a reference.

## Tech

Vanilla JS + [ApexCharts](https://apexcharts.com/) + CSS. No framework, no build step, no transpiler.
