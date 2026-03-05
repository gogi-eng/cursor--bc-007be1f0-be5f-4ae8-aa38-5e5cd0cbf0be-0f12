# Python Crypto Bot Skeleton (CEX+DEX, Perps)

Repository skeleton for building a **Python-only** trading bot codebase with clean module boundaries:

- `connectors/`: CEX connectivity/execution (CCXT + exchange-specific SDK adapters)
- `dex/`: DEX perps + EVM swap execution
- `marketdata/`: ingestion/normalization (WS/REST)
- `orderbook/`: snapshot+delta book + microstructure features
- `strategies/`: strategy interfaces + example stubs
- `risk/`: risk guards, sizing, circuit breakers
- `backtest/`: research/backtest adapters (vectorbt/backtrader/etc.)
- `analytics/`: performance metrics + reports

## Quick start

Create venv, install in editable mode:

`python -m venv .venv && source .venv/bin/activate && pip install -U pip && pip install -e ".[dev]"`

Run tests:

`pytest -q`

## Notes

- This repo intentionally ships **interfaces and minimal stubs**. Add credentials via env vars / secret manager.
- Prefer optional extras (`.[cex]`, `.[dex]`, `.[marketdata]`, `.[backtest]`, `.[analytics]`) to keep installs lean.