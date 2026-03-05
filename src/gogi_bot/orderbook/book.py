from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class L2Level:
    price: float
    size: float


@dataclass(frozen=True, slots=True)
class L2Book:
    bids: tuple[L2Level, ...]
    asks: tuple[L2Level, ...]
    ts: float

    def best_bid(self) -> L2Level | None:
        return self.bids[0] if self.bids else None

    def best_ask(self) -> L2Level | None:
        return self.asks[0] if self.asks else None

    def mid(self) -> float | None:
        bb = self.best_bid()
        ba = self.best_ask()
        if not bb or not ba:
            return None
        return (bb.price + ba.price) / 2.0

