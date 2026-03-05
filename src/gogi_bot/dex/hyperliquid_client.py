from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class HlOrder:
    coin: str
    is_buy: bool
    sz: float
    limit_px: float | None = None
    reduce_only: bool = False
    cloid: str | None = None


class HyperliquidClient:
    """
    Minimal wrapper around `hyperliquid-python-sdk`.

    Use this as an adapter boundary so the rest of your codebase does not depend
    on a specific vendor SDK surface.
    """

    def __init__(self, info: object, exchange: object) -> None:
        self._info = info
        self._exchange = exchange

    def get_user_state(self, address: str) -> dict:
        return self._info.user_state(address)

    def place_order(self, order: HlOrder) -> dict:
        if order.limit_px is None:
            raise ValueError("only limit orders are modeled in this stub")
        return self._exchange.order(
            order.coin,
            order.is_buy,
            order.sz,
            order.limit_px,
            {"reduceOnly": order.reduce_only, "cloid": order.cloid},
        )

