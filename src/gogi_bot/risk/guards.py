from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class RiskLimits:
    max_leverage: float = 10.0
    max_notional_usd: float = 1_000.0
    max_daily_loss_pct: float = 0.05
    max_open_positions: int = 3


class RiskGuard:
    """
    Centralized risk checks (pre-trade and runtime).
    Keep state in a higher-level component; this object is pure and easy to test.
    """

    def __init__(self, limits: RiskLimits) -> None:
        self._limits = limits

    def check_leverage(self, leverage: float) -> None:
        if leverage > self._limits.max_leverage:
            raise ValueError(f"leverage {leverage} exceeds max {self._limits.max_leverage}")

    def check_notional(self, notional_usd: float) -> None:
        if notional_usd > self._limits.max_notional_usd:
            raise ValueError(f"notional {notional_usd} exceeds max {self._limits.max_notional_usd}")

