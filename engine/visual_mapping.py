"""Placeholder for mapping scores to visual encodings (public-safe)."""


def mode_score_to_descriptor(score: float) -> str:
    if score is None:
        return "undefined"
    s = float(score)
    if s > 0.7:
        return "high-optima"
    if s > 0.4:
        return "mid-optima"
    if s > 0.0:
        return "low-optima"
    return "suboptimal"
