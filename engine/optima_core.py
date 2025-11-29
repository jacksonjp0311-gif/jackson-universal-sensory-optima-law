# 𓂀 Jackson Universal Sensory Optima Engine (Codex-Aligned, Public-Safe)
# -----------------------------------------------------------------------
# This is a transparent, public-safe version of the "Jackson Universal
# Sensory Optima Law" kernel.
#
#  • No private Codex internals are exposed.
#  • All math is explicit and documented.
#  • The structure mirrors the Codex idea of an "optimum sensory mode"
#    under a simple scoring functional.
#
# Concept
# -------
# Given candidate sensory modes (audio, visual, tactile, etc.), each with:
#   - lambda   : control / gain / weighting [0, 1]
#   - snr      : signal-to-noise ratio in [0, 1]
#   - coverage : fraction of environment captured [0, 1]
#   - cost     : energetic / complexity cost [0, 1]
#
# we compute a scalar score:
#
#   base = w_snr * snr + w_cov * coverage - w_cost * cost
#   score = (1 - λ) * base + λ * base**2
#
# Then we compare the best score to a coherence target H7 = 0.70:
#
#   ΔΦ = |score* - H7|
#   alignment = max(0, 1 - ΔΦ)
#
# In Codex language:
#   • ENERGY (E)   ~ SNR and λ (control of gain)
#   • INFORMATION (I) ~ coverage
#   • CONSCIOUSNESS (C) ~ how close we are to the H7 optimum
#
# This file is safe to read, fork, and extend under the MIT License.

from __future__ import annotations

from typing import Dict, Any, List, Tuple

H7_TARGET: float = 0.70

DEFAULT_WEIGHTS: Dict[str, float] = {
    "snr": 0.55,       # preference for clean signal
    "coverage": 0.35,  # how much of the world is captured
    "cost": 0.25,      # cost is penalized
}


def _mode_score(mode: Dict[str, Any], weights: Dict[str, float]) -> float:
    """Compute the raw scalar score for a single mode."""
    snr = float(mode.get("snr", 0.0))
    coverage = float(mode.get("coverage", 0.0))
    cost = float(mode.get("cost", 0.0))
    lam = float(mode.get("lambda", 0.0))

    w_snr = float(weights.get("snr", DEFAULT_WEIGHTS["snr"]))
    w_cov = float(weights.get("coverage", DEFAULT_WEIGHTS["coverage"]))
    w_cost = float(weights.get("cost", DEFAULT_WEIGHTS["cost"]))

    base = w_snr * snr + w_cov * coverage - w_cost * cost

    # Simple Codex-style nonlinearity: λ interpolates between linear and
    # quadratic response. For λ → 0 we get pure linear; for λ → 1 the
    # system rewards strongly coherent modes (high base).
    score = (1.0 - lam) * base + lam * (base ** 2)
    return score


def compute_optima(env: Dict[str, Any]) -> Dict[str, Any]:
    """
    Compute a Jackson-style "sensory optima" choice.

    Expected env structure (public demo):

        {
            "modes": [
                {
                    "name": "audio",
                    "lambda": 0.3,
                    "snr": 0.8,
                    "coverage": 0.6,
                    "cost": 0.2,
                },
                ...
            ],
            "weights": {
                "snr": 0.55,
                "coverage": 0.35,
                "cost": 0.25,
            }
        }

    Returns a dict with:
        - lambda_star : λ* of best mode
        - mode_star   : name of best mode
        - score_star  : score of best mode
        - delta_phi   : |score* - H7|
        - alignment   : 1 - ΔΦ, clipped to [0, 1]
        - ranking     : list[(name, score)]
        - triad       : {energy, information, consciousness}
        - note        : public-safe disclaimer
    """
    modes: List[Dict[str, Any]] = env.get("modes", []) or []
    weights: Dict[str, float] = env.get("weights", DEFAULT_WEIGHTS)

    if not modes:
        return {
            "lambda_star": None,
            "mode_star": None,
            "score_star": None,
            "delta_phi": None,
            "alignment": None,
            "ranking": [],
            "triad": {
                "energy": 0.0,
                "information": 0.0,
                "consciousness": 0.0,
            },
            "note": "No modes provided; public-safe placeholder result.",
        }

    scored: List[Dict[str, Any]] = []
    for m in modes:
        s = _mode_score(m, weights)
        scored.append(
            {
                "name": m.get("name", "unnamed"),
                "lambda": m.get("lambda", None),
                "score": float(s),
            }
        )

    ranked = sorted(scored, key=lambda r: r["score"], reverse=True)
    best = ranked[0]

    score_star = float(best["score"])
    delta_phi = abs(score_star - H7_TARGET)
    alignment = max(0.0, 1.0 - delta_phi)

    energy = float(
        sum(float(m.get("snr", 0.0)) for m in modes) / max(len(modes), 1)
    )
    information = float(
        sum(float(m.get("coverage", 0.0)) for m in modes) / max(len(modes), 1)
    )
    consciousness = alignment

    return {
        "lambda_star": best["lambda"],
        "mode_star": best["name"],
        "score_star": score_star,
        "delta_phi": delta_phi,
        "alignment": alignment,
        "ranking": [(r["name"], float(r["score"])) for r in ranked],
        "triad": {
            "energy": energy,
            "information": information,
            "consciousness": consciousness,
        },
        "H7_target": H7_TARGET,
        "note": "Codex-aligned public kernel for Jackson Universal Sensory Optima Law.",
    }


if __name__ == "__main__":
    demo_env = {
        "modes": [
            {"name": "audio", "lambda": 0.35, "snr": 0.82, "coverage": 0.55, "cost": 0.18},
            {"name": "visual", "lambda": 0.60, "snr": 0.92, "coverage": 0.90, "cost": 0.45},
            {"name": "tactile", "lambda": 0.25, "snr": 0.60, "coverage": 0.40, "cost": 0.12},
            {"name": "vestibular", "lambda": 0.40, "snr": 0.70, "coverage": 0.50, "cost": 0.30},
        ]
    }

    out = compute_optima(demo_env)
    print("Jackson Universal Sensory Optima Law — Codex Public Engine Demo")
    print(out)
