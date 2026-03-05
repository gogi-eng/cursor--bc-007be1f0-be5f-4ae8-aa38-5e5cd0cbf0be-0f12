from __future__ import annotations

from dataclasses import dataclass
from typing import Protocol


@dataclass(frozen=True, slots=True)
class Market:
    symbol: str
    base: str | None = None
    quote: str | None = None
    contract: bool | None = None
    linear: bool | None = None
    inverse: bool | None = None
    settle: str | None = None
    precision_price: int | None = None
    precision_amount: int | None = None
    min_amount: float | None = None
    min_cost: float | None = None


@dataclass(frozen=True, slots=True)
class OrderRequest:
    symbol: str
    side: str  # "buy" | "sell"
    type: str  # "market" | "limit"
    amount: float
    price: float | None = None
    reduce_only: bool = False
    post_only: bool = False
    client_order_id: str | None = None


@dataclass(frozen=True, slots=True)
class OrderAck:
    order_id: str
    client_order_id: str | None = None
    status: str | None = None


class ExecutionConnector(Protocol):
    """
    Minimal execution interface for CEX connectors.
    Keep this intentionally small; extend in your own app layer.
    """

    name: str

    def load_markets(self) -> dict[str, Market]: ...

    def place_order(self, req: OrderRequest) -> OrderAck: ...

    def cancel_order(self, symbol: str, order_id: str) -> None: ...

