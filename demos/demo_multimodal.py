# Jackson Universal Sensory Optima Law — Multimodal Demo (Codex Public)
#
#   • builds a small synthetic environment (audio / visual / tactile / vestibular)
#   • calls engine.compute_optima(env)
#   • prints the result
#   • (optionally) draws a simple bar chart of mode scores
#
# Requirements:
#   pip install matplotlib

from pathlib import Path

from engine.optima_core import compute_optima
from engine.modes import build_mode

try:
    import matplotlib.pyplot as plt
except Exception:
    plt = None


def build_demo_env():
    modes = [
        build_mode("audio", lam=0.35, snr=0.82, coverage=0.55, cost=0.18),
        build_mode("visual", lam=0.60, snr=0.92, coverage=0.90, cost=0.45),
        build_mode("tactile", lam=0.25, snr=0.60, coverage=0.40, cost=0.12),
        build_mode("vestibular", lam=0.40, snr=0.70, coverage=0.50, cost=0.30),
    ]
    return {"modes": modes}


def main():
    env = build_demo_env()
    out = compute_optima(env)

    print("=== Jackson Universal Sensory Optima Law — Demo ===")
    print("Mode*: ", out["mode_star"])
    print("λ*:    ", out["lambda_star"])
    if out["score_star"] is not None:
        print("Score*: {:.4f}".format(out["score_star"]))
    else:
        print("Score*: None")
    print("ΔΦ(H7):", out["delta_phi"])
    print("Align: ", out["alignment"])
    print("Triad:", out["triad"])

    print("Ranking:")
    for name, score in out["ranking"]:
        print("  - {:10s} : {:.4f}".format(name, score))

    if plt is None:
        print("\\n[info] matplotlib not available; skipping visual plot.")
        return

    names = [name for name, _ in out["ranking"]]
    scores = [score for _, score in out["ranking"]]

    fig, ax = plt.subplots(figsize=(5, 3))
    ax.bar(names, scores)
    ax.set_ylabel("Score")
    ax.set_title("Sensory Optima — Mode Scores (Public Demo)")
    fig.tight_layout()

    visuals_dir = Path(__file__).resolve().parent.parent / "visuals"
    visuals_dir.mkdir(parents=True, exist_ok=True)
    out_path = visuals_dir / "sensory_optima_demo_scores_v1.png"
    fig.savefig(out_path, dpi=200)
    print(f"[info] Saved demo plot to: {out_path}")


if __name__ == "__main__":
    main()
