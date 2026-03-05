## Architecture (suggested)

Core boundaries:

- `connectors/`: CEX OMS/execution (CCXT + per-venue adapters).
- `dex/`: perps DEX clients (Hyperliquid, dYdX v4) and EVM swap adapters.
- `marketdata/`: raw data ingestion (WS/REST), normalization, storage hooks.
- `orderbook/`: local book model + microstructure features.
- `strategies/`: pure decision logic producing `Signal`s.
- `risk/`: pure risk checks, sizing, circuit breakers.
- `backtest/`: adapters for research engines (vectorbt/backtrader/etc.).
- `analytics/`: metrics + reporting.

Recommended layering:

`marketdata` + `connectors/dex` -> app runtime -> `strategies` -> `risk` -> execution -> `analytics`.

