"""Minimal, public-safe noise helpers for demos."""

from typing import Sequence, List


def soft_floor(values: Sequence[float], floor: float = 0.0) -> List[float]:
    f = float(floor)
    return [max(float(v), f) for v in values]
