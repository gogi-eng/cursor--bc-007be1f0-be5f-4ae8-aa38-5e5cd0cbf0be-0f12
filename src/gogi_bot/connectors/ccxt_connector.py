from __future__ import annotations

from dataclasses import asdict

from gogi_bot.connectors.base import Market, OrderAck, OrderRequest


class CcxtConnector:
    """
    Thin wrapper around CCXT.

    This module is intentionally a stub: it shows a clean boundary and the
    minimum translation you typically need (markets normalization + idempotent order IDs).
    """

    def __init__(self, exchange: object, name: str | None = None) -> None:
        self._exchange = exchange
        self.name = name or getattr(exchange, "id", "ccxt")

    def load_markets(self) -> dict[str, Market]:
        markets_raw: dict = self._exchange.load_markets()
        out: dict[str, Market] = {}
        for symbol, m in markets_raw.items():
            out[symbol] = Market(
                symbol=symbol,
                base=m.get("base"),
                quote=m.get("quote"),
                contract=m.get("contract"),
                linear=m.get("linear"),
                inverse=m.get("inverse"),
                settle=m.get("settle"),
                precision_price=(m.get("precision") or {}).get("price"),
                precision_amount=(m.get("precision") or {}).get("amount"),
                min_amount=((m.get("limits") or {}).get("amount") or {}).get("min"),
                min_cost=((m.get("limits") or {}).get("cost") or {}).get("min"),
            )
        return out

    def place_order(self, req: OrderRequest) -> OrderAck:
        params: dict = {}
        if req.reduce_only:
            params["reduceOnly"] = True
        if req.post_only:
            params["postOnly"] = True
        if req.client_order_id:
            # Many exchanges map this differently; adjust per venue.
            params["clientOrderId"] = req.client_order_id

        if req.type == "market":
            res = self._exchange.create_order(req.symbol, "market", req.side, req.amount, None, params)
        elif req.type == "limit":
            if req.price is None:
                raise ValueError("limit order requires price")
            res = self._exchange.create_order(req.symbol, "limit", req.side, req.amount, req.price, params)
        else:
            raise ValueError(f"unsupported order type: {req.type}")

        return OrderAck(
            order_id=str(res.get("id")),
            client_order_id=res.get("clientOrderId") or req.client_order_id,
            status=res.get("status"),
        )

    def cancel_order(self, symbol: str, order_id: str) -> None:
        self._exchange.cancel_order(order_id, symbol)

    def debug_dump_order_request(self, req: OrderRequest) -> dict:
        return asdict(req)

