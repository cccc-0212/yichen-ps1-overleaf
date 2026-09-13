"""Deterministic adaptive-tax repeated game used in Yichen Shen's PS1.

The outputs are programmed demonstrations, not evidence about real taxpayers.
"""
from dataclasses import asdict, dataclass, field
from typing import Iterable, Mapping

MAX_ROUNDS = 8
INITIAL_TRUST = 50

# (taxpayer payoff, authority payoff, trust change)
RULES: Mapping[tuple[str, str], tuple[int, int, int]] = {
    ("C", "T"): (3, 3, 10),
    ("C", "O"): (0, 4, -15),
    ("A", "T"): (4, 0, -10),
    ("A", "O"): (1, 1, -10),
}

PRESET_PATHS: Mapping[str, tuple[tuple[str, str], ...]] = {
    "transparent_cooperation": (("C", "T"),) * 8,
    "opaque_breakdown": (("C", "O"),) + (("A", "O"),) * 7,
    "mixed_recovery": (
        ("C", "T"), ("C", "T"), ("A", "T"), ("A", "O"),
        ("C", "T"), ("C", "T"), ("C", "T"), ("C", "T"),
    ),
}


@dataclass
class GameState:
    round: int = 1
    trust: int = INITIAL_TRUST
    taxpayer_payoff: int = 0
    authority_payoff: int = 0
    event_log: list[dict] = field(default_factory=list)

    def snapshot(self) -> dict:
        return asdict(self)


def _normalize(value: str, allowed: Mapping[str, str], label: str) -> str:
    key = value.strip().lower()
    if key not in allowed:
        raise ValueError(f"invalid {label} action: {value!r}")
    return allowed[key]


def step(state: GameState, taxpayer_action: str, authority_action: str) -> GameState:
    """Apply one simultaneous action pair and append a fully auditable event."""
    if state.round > MAX_ROUNDS:
        raise ValueError(f"the game is limited to {MAX_ROUNDS} rounds")
    taxpayer = _normalize(
        taxpayer_action, {"c": "C", "comply": "C", "a": "A", "avoid": "A"}, "taxpayer"
    )
    authority = _normalize(
        authority_action, {"t": "T", "transparent": "T", "o": "O", "opaque": "O"}, "authority"
    )
    taxpayer_delta, authority_delta, trust_delta = RULES[(taxpayer, authority)]
    prior_trust = state.trust
    state.taxpayer_payoff += taxpayer_delta
    state.authority_payoff += authority_delta
    state.trust = min(100, max(0, state.trust + trust_delta))
    state.event_log.append({
        "round": state.round,
        "taxpayer_action": taxpayer,
        "authority_action": authority,
        "taxpayer_payoff_delta": taxpayer_delta,
        "authority_payoff_delta": authority_delta,
        "trust_before": prior_trust,
        "trust_delta": trust_delta,
        "trust_after": state.trust,
    })
    state.round += 1
    return state


def run_path(path: Iterable[tuple[str, str]], initial_trust: int = INITIAL_TRUST) -> GameState:
    """Run one path from a clean state."""
    if not 0 <= initial_trust <= 100:
        raise ValueError("initial_trust must be between 0 and 100")
    state = GameState(trust=initial_trust)
    for taxpayer, authority in path:
        step(state, taxpayer, authority)
    return state


def preset_results() -> dict[str, dict]:
    """Return the three PS1 verification records."""
    results = {}
    for name, path in PRESET_PATHS.items():
        state = run_path(path)
        results[name] = {
            "path": ["/".join(actions) for actions in path],
            "rounds_completed": len(state.event_log),
            "taxpayer_payoff": state.taxpayer_payoff,
            "authority_payoff": state.authority_payoff,
            "final_trust": state.trust,
            "complete_log": len(state.event_log) == MAX_ROUNDS,
            "evidence_class": "programmed demonstration",
        }
    return results


def one_shot_benchmark() -> dict:
    """Check strict dominance and report the one-shot Nash benchmark."""
    taxpayer_avoid_dominates = (
        RULES[("A", "T")][0] > RULES[("C", "T")][0]
        and RULES[("A", "O")][0] > RULES[("C", "O")][0]
    )
    authority_opaque_dominates = (
        RULES[("C", "O")][1] > RULES[("C", "T")][1]
        and RULES[("A", "O")][1] > RULES[("A", "T")][1]
    )
    return {
        "taxpayer_avoid_strictly_dominant": taxpayer_avoid_dominates,
        "authority_opaque_strictly_dominant": authority_opaque_dominates,
        "unique_one_shot_nash": "A/O" if taxpayer_avoid_dominates and authority_opaque_dominates else None,
        "pareto_superior_profile": "C/T",
    }
