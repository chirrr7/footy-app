from typing import Literal

from pydantic import BaseModel, Field


BroadPosition = Literal["GK", "CB", "FB/WB", "DM", "CM", "AM", "Winger", "ST"]


class PlayerSeasonRecord(BaseModel):
    player_id: str
    player_name: str
    season: str
    club: str
    league: str
    broad_position: BroadPosition
    archetype: str | None = None
    minutes: float = Field(ge=0)
    goals: float = Field(default=0, ge=0)
    assists: float = Field(default=0, ge=0)
    xg: float | None = Field(default=None, ge=0)
    xa: float | None = Field(default=None, ge=0)


class TeamSeasonRecord(BaseModel):
    team_id: str
    team_name: str
    season: str
    league: str
    matches: int = Field(ge=0)
    wins: int = Field(ge=0)
    draws: int = Field(ge=0)
    losses: int = Field(ge=0)
    goals_for: float = Field(ge=0)
    goals_against: float = Field(ge=0)
    xg_for: float | None = Field(default=None, ge=0)
    xg_against: float | None = Field(default=None, ge=0)
