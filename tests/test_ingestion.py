import pandas as pd

from futx.ingestion.understat import aggregate_player_transfers, filter_top5_season


def test_filter_top5_season():
    frame = pd.DataFrame(
        {
            "year": [2024, 2024, 2023],
            "league": ["EPL", "RFPL", "La_Liga"],
        }
    )
    result = filter_top5_season(frame, 2024)
    assert result["league"].tolist() == ["EPL"]


def test_aggregate_player_transfers_uses_dominant_row_and_sums():
    frame = pd.DataFrame(
        [
            {
                "id": 1,
                "player_name": "Example",
                "year": 2024,
                "season": "2024/25",
                "team_title": "Club A",
                "league": "EPL",
                "position": "F",
                "primary_position": "F",
                "games": 10,
                "time": 800,
                "goals": 5,
                "xG": 4.0,
                "npg": 4,
                "npxG": 3.2,
                "assists": 2,
                "xA": 1.8,
                "shots": 30,
                "key_passes": 15,
                "yellow_cards": 1,
                "red_cards": 0,
                "xGChain": 6.0,
                "xGBuildup": 2.0,
            },
            {
                "id": 1,
                "player_name": "Example",
                "year": 2024,
                "season": "2024/25",
                "team_title": "Club B",
                "league": "Serie_A",
                "position": "F",
                "primary_position": "F",
                "games": 5,
                "time": 200,
                "goals": 2,
                "xG": 1.5,
                "npg": 2,
                "npxG": 1.5,
                "assists": 1,
                "xA": 0.8,
                "shots": 10,
                "key_passes": 5,
                "yellow_cards": 0,
                "red_cards": 0,
                "xGChain": 2.0,
                "xGBuildup": 1.0,
            },
        ]
    )

    result = aggregate_player_transfers(frame).iloc[0]

    assert result["team_title"] == "Club A"
    assert result["league"] == "EPL"
    assert result["time"] == 1000
    assert result["goals"] == 7
    assert result["clubs"] == "Club A / Club B"
    assert round(result["goals_p90"], 3) == 0.63
