from __future__ import annotations


def basic_stats(returns_series) -> dict:
    """
    Minimal performance stats. Prefer empyrical/quantstats in real reporting.
    """

    import numpy as np

    r = np.asarray(returns_series, dtype=float)
    if r.size == 0:
        return {"count": 0}
    return {
        "count": int(r.size),
        "mean": float(r.mean()),
        "std": float(r.std(ddof=1)) if r.size > 1 else 0.0,
        "min": float(r.min()),
        "max": float(r.max()),
    }

