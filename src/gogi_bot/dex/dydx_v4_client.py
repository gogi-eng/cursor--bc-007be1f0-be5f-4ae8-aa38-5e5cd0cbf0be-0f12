from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class DyDxOrder:
    market: str
    side: str  # "BUY" | "SELL"
    type: str  # "MARKET" | "LIMIT"
    size: str
    price: str | None = None
    reduce_only: bool = False
    client_id: str | None = None


class DyDxV4Client:
    """
    Minimal adapter around `dydx-v4-client` (from dydxprotocol/v4-clients).

    Keep your strategy/risk/backtest code independent of the generated SDK structure.
    """

    def __init__(self, client: object) -> None:
        self._client = client

    async def place_order(self, order: DyDxOrder) -> dict:
        # The concrete call shape depends on the SDK version; keep this as a stub boundary.
        payload = {
            "market": order.market,
            "side": order.side,
            "type": order.type,
            "size": order.size,
            "price": order.price,
            "reduceOnly": order.reduce_only,
            "clientId": order.client_id,
        }
        return await self._client.place_order(payload)

