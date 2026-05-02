// Sample data for IMC Prosperity Visualizer

window.BACKTEST_DATA = [
    {
        id: "run_001",
        trader: "trader_adin_v3",
        round: "R5",
        day: "D0",
        final_pnl: 142520,
        max_dd: -3210,
        sharpe: 2.84,
        status: "GREEN",
        readiness: 95,
        history: Array.from({ length: 100 }, (_, i) => ({
            tick: i,
            pnl: 1000 * i + Math.random() * 5000,
            products: {
                "HYDROGEL": 400 * i + Math.random() * 2000,
                "VFE": 600 * i + Math.random() * 3000
            }
        }))
    },
    {
        id: "run_002",
        trader: "trader_adin_v2",
        round: "R5",
        day: "D0",
        final_pnl: 98400,
        max_dd: -5400,
        sharpe: 1.95,
        status: "AMBER",
        readiness: 82,
        history: Array.from({ length: 100 }, (_, i) => ({
            tick: i,
            pnl: 800 * i + Math.random() * 4000,
            products: {
                "HYDROGEL": 300 * i + Math.random() * 1500,
                "VFE": 500 * i + Math.random() * 2500
            }
        }))
    },
    {
        id: "run_003",
        trader: "trader_phi",
        round: "R5",
        day: "D0",
        final_pnl: 45200,
        max_dd: -1200,
        sharpe: 2.10,
        status: "GREEN",
        readiness: 88,
        history: Array.from({ length: 100 }, (_, i) => ({
            tick: i,
            pnl: 400 * i + Math.random() * 2000,
            products: {
                "HYDROGEL": 150 * i + Math.random() * 1000,
                "VFE": 250 * i + Math.random() * 1000
            }
        }))
    }
];

window.I4BT_DATA = [
    {
        id: "i4bt_001",
        trader: "trader_adin_v3",
        round: "R5",
        day: "D0",
        final_pnl: 138000,
        history: Array.from({ length: 100 }, (_, i) => ({
            tick: i,
            pnl: 950 * i + Math.random() * 4800
        }))
    }
];

window.LIVE_LOG_DATA = [
    {
        id: "live_001",
        trader: "trader_adin_v3",
        round: "R5",
        day: "D0",
        final_pnl: 145000,
        history: Array.from({ length: 100 }, (_, i) => ({
            tick: i,
            pnl: 1020 * i + Math.random() * 5200
        }))
    }
];
