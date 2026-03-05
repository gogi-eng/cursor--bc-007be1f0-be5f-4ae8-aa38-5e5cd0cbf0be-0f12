from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class BacktestResult:
    stats: dict


def run_vectorbt_signals(price_series, entries, exits, init_cash: float = 10_000.0) -> BacktestResult:
    """
    Minimal adapter around vectorbt Portfolio. Keep import local to keep base install lean.
    """

    import vectorbt as vbt

    pf = vbt.Portfolio.from_signals(price_series, entries, exits, init_cash=init_cash)
    return BacktestResult(stats=pf.stats().to_dict())

