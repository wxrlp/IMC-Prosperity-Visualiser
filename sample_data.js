// --- Unified IMC Prosperity Visualizer Sample Data ---

window.BACKTEST_DATA = [
    {
        id: "bt_adin_v3_r5_d2",
        trader: "Adin_V3",
        round: "R5",
        day: "D2",
        status: "ACCEPTED",
        final_pnl: 12450.5,
        max_dd: 450.0,
        sharpe: 2.1,
        history: Array.from({length: 100}, (_, i) => ({ pnl: 12450.5 * (i/100) + Math.random() * 500, products: { "OSMIUM": 8000 * (i/100), "PEPPER": 4450.5 * (i/100) } }))
    },
    {
        id: "bt_phi_r5_d2",
        trader: "Phi_V1",
        round: "R5",
        day: "D2",
        status: "REJECTED",
        final_pnl: -2300.0,
        max_dd: 3100.0,
        sharpe: -0.4,
        history: Array.from({length: 100}, (_, i) => ({ pnl: -2300 * (i/100) + Math.random() * 200, products: { "OSMIUM": -1000 * (i/100), "PEPPER": -1300 * (i/100) } }))
    }
];

window.LIVE_LOG_DATA = [
    {
        id: "live_adin_v3",
        trader: "Adin_V3",
        round: "R5",
        day: "D2",
        status: "LIVE",
        final_pnl: 11800.0,
        max_dd: 600.0,
        sharpe: 1.8,
        history: Array.from({length: 100}, (_, i) => ({ pnl: 11800 * (i/100) + Math.random() * 400, products: { "OSMIUM": 7500 * (i/100), "PEPPER": 4300 * (i/100) } }))
    }
];

window.I4BT_DATA = [
    {
        id: "i4bt_adin_v3",
        trader: "Adin_V3",
        round: "R5",
        day: "D2",
        final_pnl: 12100.0,
        history: Array.from({length: 100}, (_, i) => ({ pnl: 12100 * (i/100) + Math.random() * 300 }))
    }
];

// New Source Types
window.REAL_DATA_RESULTS = [
    {
        id: "real_yf_corn",
        trader: "Adin_V3",
        source: "YF_CORN",
        final_pnl: 4500.0,
        history: Array.from({length: 100}, (_, i) => ({ pnl: 4500 * (i/100) + Math.random() * 100 }))
    }
];

window.SCENARIO_RESULTS = [
    {
        id: "scenario_crash",
        trader: "Adin_V3",
        regime: "CRASH",
        final_pnl: 800.0,
        history: Array.from({length: 100}, (_, i) => ({ pnl: (i < 40 ? 2000 * (i/40) : (i < 60 ? 2000 - 3000 * (i-40)/20 : -1000 + 1800 * (i-60)/40)) }))
    }
];

window.STRESS_RESULTS = [
    {
        id: "stress_adin_v3",
        trader: "Adin_V3",
        latency: [0, 1, 2],
        slippage: [0, 0.05, 0.1],
        results: [
            { latency: 0, slippage: 0, pnl: 12000 },
            { latency: 1, slippage: 0, pnl: 8000 },
            { latency: 2, slippage: 0, pnl: 3000 },
            { latency: 0, slippage: 0.05, pnl: 9000 },
            { latency: 0, slippage: 0.1, pnl: 5000 }
        ]
    }
];
