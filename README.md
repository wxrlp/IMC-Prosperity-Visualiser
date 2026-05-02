# IMC Prosperity Visualizer | Premium Edition

A high-performance, aesthetically pleasing visualizer for analyzing and comparing IMC Prosperity trading strategies.

![Visualizer Preview](https://img.shields.io/badge/Aesthetics-Premium-blue)
![Tech Stack](https://img.shields.io/badge/Tech-React%20%7C%20Tailwind%20%7C%20ApexCharts-emerald)
[![Live Demo](https://img.shields.io/badge/Live-Demo-brightgreen)](https://adin.github.io/IMC-Prosperity-Visualiser/)

## 🌐 Live Demo

You can view the visualizer live at: **[https://adin.github.io/IMC-Prosperity-Visualiser/](https://adin.github.io/IMC-Prosperity-Visualiser/)**

*(Note: Replace `adin` with your GitHub username if it's different)*

## Features

- **OVERLAY**: Multi-trader leaderboard and portfolio PnL curves.
- **COMPARE**: Synchronized charts to compare Backtest results with Live log performance.
- **ATTRIBUTION**: Product-level PnL breakdown to identify alpha sources.
- **STABILITY**: Heatmaps showing performance consistency across multiple days and rounds.
- **Interactive Filtering**: Real-time filtering by Source, Round, and Day.

## Getting Started

1. **Open the Visualizer**: Simply open `visualizer.html` in any modern web browser.
2. **Data Integration**: The visualizer looks for the following files in the same directory:
   - `backtest_comparison.js`: Your backtest results.
   - `i4bt_comparison.js`: Results from the i4bt backtester.
   - `live_comparison.js`: Live trading logs.
3. **Sample Data**: If no comparison files are found, the visualizer will automatically load `sample_data.js` to demonstrate its capabilities.

## Data Format

To use your own data, ensure your `.js` files define the following global variables:

### Backtest Data (`backtest_comparison.js`)
```javascript
window.BACKTEST_DATA = [
    {
        id: "unique_run_id",
        trader: "trader_name",
        round: "R5",
        day: "D0",
        final_pnl: 150000,
        max_dd: -2000,
        sharpe: 3.1,
        status: "GREEN",
        history: [
            { tick: 0, pnl: 0, products: { "PRODUCT_A": 0, "PRODUCT_B": 0 } },
            // ... more ticks
        ]
    }
];
```

### Live Data (`live_comparison.js`)
```javascript
window.LIVE_LOG_DATA = [
    {
        trader: "trader_name", // Must match backtest trader name for comparison
        round: "R5",
        day: "D0",
        final_pnl: 148000,
        history: [
            { tick: 0, pnl: 0 },
            // ... more ticks
        ]
    }
];
```

## Tech Stack

- **React 18**: UI logic and state management.
- **Tailwind CSS**: Modern, utility-first styling with glassmorphism.
- **ApexCharts**: High-performance, interactive charting.
- **Lucide Icons**: Crisp, professional iconography.

---
*Built for the IMC Prosperity Challenge.*
