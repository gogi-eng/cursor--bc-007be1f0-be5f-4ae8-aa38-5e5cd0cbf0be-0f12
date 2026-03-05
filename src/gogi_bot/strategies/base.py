from __future__ import annotations

from dataclasses import dataclass
from typing import Protocol


@dataclass(frozen=True, slots=True)
class Signal:
    """
    Strategy output: desired action.
    In production, expand this with target position, order type, brackets, etc.
    """

    action: str  # "enter_long" | "enter_short" | "exit" | "hold"
    reason: str


class Strategy(Protocol):
    name: str

    def on_tick(self, ctx: object) -> Signal: ...

