# FUTX Agent Instructions

## Mission
Build FUTX as a football benchmark/index. The current phase is model validation through historical seasonal backtests, not consumer UI development.

## Priority order
1. Reliable historical data ingestion
2. Clean normalized season datasets
3. Player Index v0.1
4. Team Index v0.1
5. Backtest across multiple seasons
6. Calibrate absolute 0-100 scale
7. Only then move to match-level/weekly rankings
8. Supabase/app/web come later

## Non-negotiable product rules
Read `docs/MODEL_SPEC.md` before making modelling decisions.

Important:
- Do not invent product rules that conflict with the spec.
- Do not hard-code player-specific adjustments.
- Do not tune the model merely to force famous players into expected ranks.
- Explain anomalous rankings through metrics/weights and fix systemic issues only.
- Keep weights/config outside core code where practical.
- Keep all published-model logic versionable.
- Preserve raw source fields before transformations.
- Use stable IDs, not player names, for joins.
- Mid-season transfers must aggregate correctly.
- No hard minimum-minutes cutoff.
- Per-90 efficiency and total volume must both remain available.
- External composite ratings (Sofascore/FotMob/Fantasy) are not FUTX score inputs.
- Exact FUTX formula is private; code may contain it, public-facing docs should not expose it.

## Data source policy for prototype
Free/public sources are acceptable for research and prototyping.
Do not bypass authentication, paywalls, CAPTCHA, bot protection, or access controls.
Record provenance for every imported field.
Do not assume prototype data licensing is suitable for commercial redistribution.

## Current milestone
Prepare 2024/25 Top-5-league player and team datasets and generate:
- FUTX Player Top 100 seasonal ranking
- FUTX Team Top 50 seasonal ranking

The first ranking can be labelled Model v0.1 and is expected to be imperfect. Produce diagnostic output showing why each top-ranked player scored highly so weights can be reviewed.

## Engineering
- Python 3.11+
- pandas/numpy for modelling
- pytest for tests
- ruff for lint
- CSV/Parquet for prototype data
- Supabase is planned later, not needed for the first backtest

## Definition of done for each change
- tests pass
- ruff passes
- no secrets committed
- data provenance documented
- output reproducible from a clean checkout
