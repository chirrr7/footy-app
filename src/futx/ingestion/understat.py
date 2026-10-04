from __future__ import annotations

from collections.abc import Iterable

import pandas as pd

TOP5_LEAGUES = ("EPL", "La_Liga", "Bundesliga", "Serie_A", "Ligue_1")

PLAYER_HISTORY_URL = (
    "https://raw.githubusercontent.com/vibedatascience/"
    "understat_players_aggregated/main/understat_players_aggregated_2014_2024.csv"
)
TEAM_HISTORY_URL = (
    "https://raw.githubusercontent.com/vibedatascience/"
    "understat_teams_aggregated/main/understat_teams_aggregated_2014_2024.csv"
)

PLAYER_ADDITIVE_COLUMNS = (
    "games",
    "time",
    "goals",
    "xG",
    "npg",
    "npxG",
    "assists",
    "xA",
    "shots",
    "key_passes",
    "yellow_cards",
    "red_cards",
    "xGChain",
    "xGBuildup",
)


def load_player_history(url: str = PLAYER_HISTORY_URL) -> pd.DataFrame:
    return pd.read_csv(url)


def load_team_history(url: str = TEAM_HISTORY_URL) -> pd.DataFrame:
    return pd.read_csv(url)


def filter_top5_season(
    frame: pd.DataFrame,
    year: int,
    leagues: Iterable[str] = TOP5_LEAGUES,
) -> pd.DataFrame:
    allowed = set(leagues)
    return frame[(frame["year"] == year) & frame["league"].isin(allowed)].copy()


def _dominant_row(group: pd.DataFrame) -> pd.Series:
    """Return the row representing the club/league with most minutes."""
    return group.loc[group["time"].astype(float).idxmax()]


def aggregate_player_transfers(frame: pd.DataFrame) -> pd.DataFrame:
    """Collapse multiple club rows for the same player-season."""
    if frame.empty:
        return frame.copy()

    rows: list[dict[str, object]] = []
    for (player_id, year), group in frame.groupby(["id", "year"], sort=False):
        dominant = _dominant_row(group)
        row: dict[str, object] = {
            "id": player_id,
            "player_name": dominant["player_name"],
            "year": year,
            "season": dominant["season"],
            "team_title": dominant["team_title"],
            "league": dominant["league"],
            "position": dominant["position"],
            "primary_position": dominant["primary_position"],
            "clubs": " / ".join(dict.fromkeys(group["team_title"].astype(str))),
            "leagues": " / ".join(dict.fromkeys(group["league"].astype(str))),
        }
        for column in PLAYER_ADDITIVE_COLUMNS:
            row[column] = pd.to_numeric(group[column], errors="coerce").fillna(0).sum()
        rows.append(row)

    return add_per90_columns(pd.DataFrame(rows))


def add_per90_columns(frame: pd.DataFrame) -> pd.DataFrame:
    result = frame.copy()
    minutes = pd.to_numeric(result["time"], errors="coerce").replace(0, pd.NA)

    for column in (
        "goals",
        "xG",
        "npg",
        "npxG",
        "assists",
        "xA",
        "shots",
        "key_passes",
        "xGChain",
        "xGBuildup",
    ):
        result[f"{column}_p90"] = (
            pd.to_numeric(result[column], errors="coerce") / minutes * 90.0
        ).fillna(0.0)

    return result
