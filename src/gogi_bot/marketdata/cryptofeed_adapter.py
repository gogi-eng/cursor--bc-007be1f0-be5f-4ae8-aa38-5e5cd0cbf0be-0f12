from __future__ import annotations

from dataclasses import dataclass
from typing import Callable, Protocol


@dataclass(frozen=True, slots=True)
class Trade:
    exchange: str
    symbol: str
    price: float
    size: float
    ts: float


class TradeSink(Protocol):
    def __call__(self, trade: Trade) -> None: ...


class CryptofeedAdapter:
    """
    Adapter boundary for `cryptofeed` feed handlers and callbacks.

    In production, you typically:
    - normalize exchange symbols
    - route to a queue / DB writer
    - keep callbacks lightweight (no heavy CPU in the event loop)
    """

    def __init__(self, trade_sink: TradeSink) -> None:
        self._trade_sink = trade_sink

    def on_trade(self, trade_obj: object, receipt_ts: float) -> None:
        # cryptofeed trade object has exchange-specific attributes; do best-effort extraction.
        ex = getattr(trade_obj, "exchange", None) or getattr(trade_obj, "feed", None) or "unknown"
        symbol = getattr(trade_obj, "symbol", None) or getattr(trade_obj, "pair", None) or "unknown"
        price = float(getattr(trade_obj, "price", 0.0))
        size = float(getattr(trade_obj, "amount", getattr(trade_obj, "size", 0.0)))
        ts = float(getattr(trade_obj, "timestamp", receipt_ts))
        self._trade_sink(Trade(exchange=str(ex), symbol=str(symbol), price=price, size=size, ts=ts))


def list_to_sink(buf: list[Trade]) -> Callable[[Trade], None]:
    def _sink(t: Trade) -> None:
        buf.append(t)

    return _sink

