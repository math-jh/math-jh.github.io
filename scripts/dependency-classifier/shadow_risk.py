#!/usr/bin/env python3
"""Step 2: the risk that a Step 1 judgment will not survive, and the flag.

Until enough judgments have a final outcome the flag is a plain rule: a
boundary answer, a self-contradiction, a missing boundary explanation, or an
evidence quote that does not match the source.  Once there are enough outcomes
(``MIN_OUTCOMES`` per stage, with some overturned among them) a logistic
regression over the Step 1 answers and the link's objective features replaces
the rule, and the flag goes to the riskiest ``FLAG_SHARE`` of judgments.  A
share rather than a probability cut is used on purpose: early fits are poorly
calibrated, but their ranking is already useful, and the share is what fixes
the cost of Step 3–4.

The outcome of a judgment is whether the stage's Step 1 relation equals the
link's final relation (unanimous vote, human ruling, or audit correction).
"""
from __future__ import annotations

import math
import os
import time

import numpy as np

import shadow_store as store

MIN_OUTCOMES = int(os.environ.get("DEPENDENCY_SHADOW_MIN_OUTCOMES", "300"))
MIN_OVERTURNED = 15
FLAG_SHARE = float(os.environ.get("DEPENDENCY_SHADOW_FLAG_SHARE", "0.25"))
QUOTE_FLOOR = 0.6
KINDS = ("definition", "proposition", "theorem", "lemma", "corollary", "example",
         "remark", "section", "post")
BASES = ("forward", "required_meaning", "required_step", "weak_verify", "weak_other", "boundary")


def vector(row: dict, f: dict) -> list[float]:
    v = [
        float(row["boundary"]), float(row["inconsistent"]), float(row["missing_boundary_text"]),
        float(row.get("quote_score", 1.0)), float(row.get("quote_score", 1.0) < 0.8),
        float(row["preview"]),
    ]
    v += [float(row["basis"] == b) for b in BASES]
    v += [float(row["relation"] == r) for r in ("required", "weak", "forward")]
    v += [float(bool(f.get(k))) for k in ("same_page", "in_proof", "in_box_statement",
                                         "in_footnote", "in_paren", "in_heading",
                                         "target_post_earlier")]
    v.append({True: 1.0, False: 0.0}.get(f.get("target_before"), 0.5))
    v += [float(f.get("target_kind") == k) for k in KINDS]
    v.append(float((f.get("pair_size") or 1) > 1))
    v.append(math.log1p(f.get("article_links") or 0))
    return v


def rule_flag(row: dict) -> tuple[bool, list[str]]:
    reasons = []
    if row["boundary"]:
        reasons.append("boundary")
    if row["inconsistent"]:
        reasons.append("inconsistent")
    if row["missing_boundary_text"]:
        reasons.append("missing_boundary_text")
    if row.get("quote_score", 1.0) < QUOTE_FLOOR:
        reasons.append("quote")
    return bool(reasons), reasons


def load_model() -> dict:
    return store.read_json(store.CALIBRATION_PATH, {})


def score(stage: str, row: dict, f: dict, model: dict | None = None) -> dict:
    """Risk and flag for one judgment.  ``model`` is load_model(), passed in bulk."""
    model = load_model() if model is None else model
    fit = model.get(stage)
    flagged, reasons = rule_flag(row)
    if not fit:
        return {"risk": None, "flagged": flagged, "reasons": reasons, "by": "rule"}
    x = np.array(vector(row, f))
    z = float(np.dot(np.array(fit["weights"]), (x - np.array(fit["mean"])) / np.array(fit["scale"]))
              + fit["bias"])
    risk = 1 / (1 + math.exp(-z))
    by_model = risk >= fit["threshold"]
    # The rule's reasons stay as hard triggers: a self-contradiction or a missing
    # boundary explanation always gets a second look, whatever the fit says.
    hard = [r for r in reasons if r in ("inconsistent", "missing_boundary_text")]
    return {"risk": round(risk, 4), "flagged": by_model or bool(hard),
            "reasons": (["model"] if by_model else []) + hard, "by": "model"}


def _fit_logistic(X: np.ndarray, y: np.ndarray, l2: float = 1.0, steps: int = 3000,
                  lr: float = 0.1) -> tuple[np.ndarray, float]:
    w = np.zeros(X.shape[1])
    b = 0.0
    n = len(y)
    for _ in range(steps):
        p = 1 / (1 + np.exp(-(X @ w + b)))
        grad_w = X.T @ (p - y) / n + l2 * w / n
        grad_b = float(np.sum(p - y) / n)
        w -= lr * grad_w
        b -= lr * grad_b
    return w, b


def fit(outcomes: dict[str, list[tuple[list[float], int]]]) -> dict:
    """outcomes[stage] = [(vector, overturned)].  Writes and returns the model."""
    model = {}
    for stage, rows in outcomes.items():
        y = np.array([o for _, o in rows], dtype=float)
        if len(rows) < MIN_OUTCOMES or y.sum() < MIN_OVERTURNED:
            continue
        X = np.array([v for v, _ in rows], dtype=float)
        mean = X.mean(axis=0)
        scale = X.std(axis=0)
        scale[scale == 0] = 1.0
        Xs = (X - mean) / scale
        w, b = _fit_logistic(Xs, y)
        risks = 1 / (1 + np.exp(-(Xs @ w + b)))
        threshold = float(np.quantile(risks, 1 - FLAG_SHARE))
        model[stage] = {"weights": w.tolist(), "bias": b, "mean": mean.tolist(),
                        "scale": scale.tolist(), "threshold": threshold,
                        "n": len(rows), "overturned": int(y.sum()),
                        "fitted_at": int(time.time())}
    store.write_json(store.CALIBRATION_PATH, model)
    return model
