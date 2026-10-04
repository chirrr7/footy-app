# FUTX

FUTX is a football benchmark/index project designed to answer two questions:

1. Who are the best players in Europe's top five leagues?
2. Which are the best teams in Europe's top five leagues?

The first build target is **seasonal backtesting**, not the consumer app.

## V0.1 milestone
Produce:
- FUTX Player 100 for a historical season
- FUTX Team 50 for the same season
- absolute 0-100 scores
- reproducible outputs from raw match/season data

## Development order
1. Historical seasonal data ingestion
2. Player index v0.1
3. Team index v0.1
4. Backtest and calibrate
5. Match-level / weekly index
6. Supabase + app/web product

See `docs/MODEL_SPEC.md` for locked product/model decisions.
