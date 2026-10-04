from __future__ import annotations

import pandas as pd


def per90(series: pd.Series, minutes: pd.Series) -> pd.Series:
    """Convert an event count to a per-90 rate without imposing a minutes threshold."""
    safe_minutes = minutes.where(minutes > 0)
    return (series / safe_minutes) * 90.0


def clamp_score(score: pd.Series, lower: float = 0.0, upper: float = 100.0) -> pd.Series:
    """Clamp published FUTX scores to the absolute 0-100 range."""
    return score.clip(lower=lower, upper=upper)


def build_player_index(frame: pd.DataFrame) -> pd.DataFrame:
    """Placeholder for FUTX Player Index v0.1.

    This deliberately fails until the first real metric schema and calibrated
    weights are agreed from the historical dataset.
    """
    raise NotImplementedError("Player scoring model not calibrated yet.")


def build_team_index(frame: pd.DataFrame) -> pd.DataFrame:
    """Placeholder for FUTX Team Index v0.1."""
    raise NotImplementedError("Team scoring model not calibrated yet.")
