"""Public-safe helpers for building demo sensory modes."""

from typing import Dict


def build_mode(name: str, lam: float, snr: float, coverage: float, cost: float) -> Dict:
    return {
        "name": name,
        "lambda": float(lam),
        "snr": float(snr),
        "coverage": float(coverage),
        "cost": float(cost),
    }
