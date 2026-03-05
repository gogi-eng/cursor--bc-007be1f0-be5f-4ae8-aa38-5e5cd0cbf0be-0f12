from __future__ import annotations

from dataclasses import dataclass

from gogi_bot.strategies.base import Signal


@dataclass(slots=True)
class SimpleSpreadReversion:
    """
    Example stub strategy:
    - works on best bid/ask spread regimes
    - intended as a placeholder for perps market-making / taker logic
    """

    name: str = "simple_spread_reversion"
    max_spread: float = 1.0

    def on_tick(self, ctx: object) -> Signal:
        # ctx is intentionally untyped in the skeleton.
        s = getattr(ctx, "spread", None)
        if s is None:
            return Signal(action="hold", reason="no_spread")
        if s > self.max_spread:
            return Signal(action="exit", reason="spread_too_wide")
        return Signal(action="hold", reason="ok")

