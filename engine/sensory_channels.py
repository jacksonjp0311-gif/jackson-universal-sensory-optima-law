"""Public-safe helper functions for sensory channel handling."""

from typing import Sequence, List


def normalize(values: Sequence[float]) -> List[float]:
    vals = [float(v) for v in values]
    if not vals:
        return []
    max_val = max(vals)
    if max_val <= 0.0:
        return [0.0 for _ in vals]
    return [v / max_val for v in vals]
