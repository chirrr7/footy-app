from __future__ import annotations

import argparse
from pathlib import Path

from futx.ingestion.understat import (
    aggregate_player_transfers,
    filter_top5_season,
    load_player_history,
    load_team_history,
)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Prepare one FUTX historical season.")
    parser.add_argument("--year", type=int, default=2024, help="Season start year.")
    parser.add_argument("--output-dir", default="outputs/prepared", help="Output folder.")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    output = Path(args.output_dir)
    output.mkdir(parents=True, exist_ok=True)

    players_raw = filter_top5_season(load_player_history(), args.year)
    players = aggregate_player_transfers(players_raw)
    teams = filter_top5_season(load_team_history(), args.year)

    season_label = f"{args.year}_{str(args.year + 1)[-2:]}"
    players_path = output / f"players_{season_label}.csv"
    teams_path = output / f"teams_{season_label}.csv"

    players.to_csv(players_path, index=False)
    teams.to_csv(teams_path, index=False)

    print(f"Prepared {len(players):,} player-season rows -> {players_path}")
    print(f"Prepared {len(teams):,} team-season rows -> {teams_path}")


if __name__ == "__main__":
    main()
