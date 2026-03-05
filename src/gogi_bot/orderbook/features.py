from __future__ import annotations

from gogi_bot.orderbook.book import L2Book


def spread(book: L2Book) -> float | None:
    bb = book.best_bid()
    ba = book.best_ask()
    if not bb or not ba:
        return None
    return ba.price - bb.price


def imbalance(book: L2Book, depth: int = 10) -> float | None:
    if depth <= 0:
        raise ValueError("depth must be positive")
    bids = book.bids[:depth]
    asks = book.asks[:depth]
    if not bids or not asks:
        return None
    bid_sz = sum(l.size for l in bids)
    ask_sz = sum(l.size for l in asks)
    denom = bid_sz + ask_sz
    if denom == 0:
        return None
    return (bid_sz - ask_sz) / denom

