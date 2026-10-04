# FUTX Model Specification — v0.1

## Product objective
FUTX is a benchmark, not a stats site. It should become a reference point for European football in the same way a market index is a reference point in finance.

### Coverage
- Eligible players: players contracted to clubs in the Premier League, La Liga, Serie A, Bundesliga, or Ligue 1, plus an explicit Lionel Messi exception.
- Player matches counted: all club competitions, internationals, and friendlies.
- Team matches counted: competitive club matches only; no friendlies.
- Published universes:
  - Top 100 players overall
  - Top 100 by broad position
  - Top 10 by curated archetype
  - Top 50 teams
- Europe-wide rankings only; no league-specific ranking products.

## Ranking products
1. Best Performer — isolated performance window/gameweek; no carryover.
2. Best Player Right Now — current-season realised performance with hindsight from the season to date.
3. Seasonal Player Index — full-season ranking.
4. Team Index — broader team benchmark.
5. TOTW / TOTM / TOTS.
6. Fan Index — separate community ranking; never blended into official FUTX.

## Score scale
- Absolute 0–100 scale.
- No public labels attached to score bands.
- Historical interpretation should make 90+ over a full season extraordinarily rare.
- Scores should be comparable across seasons.
- Published historical snapshots are immutable.
- Every published snapshot stores the model version that generated it.

## Time treatment
- Current-season performances have equal weight; no recency decay.
- Injury does not directly penalise a player. It only stops new evidence accumulating.
- Per-90 efficiency and total volume both matter, with different sensitivities.
- No hard minimum-minutes threshold.
- Minutes increase evidence/confidence and sustained-performance weight; they are not a simple additive bonus.

## Position and role
Broad positions:
- GK
- CB
- FB/WB
- DM
- CM
- AM
- Winger
- ST

Every player also receives one curated tactical archetype describing how they actually play. Archetypes are:
- AI-assisted first pass from public tactical/scouting information
- analyst approved
- stable over time
- changed only after a sustained tactical shift

Do not tag a new archetype every match.

## Human input
Human analysts do not directly add subjective points.
They may:
- curate/approve archetypes
- approve entry into the published Top 100
- fix bad/missing data
- review weekly output
- publish rankings manually

## Player scoring principles
- Bottom-up positive contribution model.
- Ordinary mistakes/turnovers do not create negative marking.
- Cards are the explicit exception:
  - yellow cards reduce weekly/seasonal score
  - one red = two yellows
  - fouls without cards do not matter
- Team win/loss does not directly affect a player's score.
- Clean sheets matter for defenders and goalkeepers.
- Clean-sheet credit is binary for an appearance, not pro-rated by minutes.
- Set pieces are absorbed into normal metrics; no special set-piece bonus.
- MOTM awards and external ratings (Sofascore/FotMob/Fantasy) are not model inputs.
- Use raw per-90 statistics; no possession-context adjustment.

### Attacking
- Goals, assists, xG, xA all matter.
- G-xG / xG over- or under-performance is part of attacking evaluation, not a separate bonus.
- Penalty scored has lower weight than open-play goal.
- Penalty won carries more weight than penalty scored.
- If the same player wins and scores the penalty, both event contributions count.
- Assists use the normal/official assist definition.
- Dribbling/take-ons/carries:
  - very important for wingers and attacking mids
  - moderate for strikers/fullbacks
  - low for CBs/DMs/GKs

### Progression
Relative importance:
1. Midfielders
2. Defenders
3. Goalkeepers
4. Attackers

### Defensive/pressing contribution
- Attackers: pressing
- Midfielders: pressing + defensive contribution
- Defenders: defensive contribution
- Goalkeepers: save-related output primarily

### Defenders
- CB attacking output is edge-only in defender ranking.
- FB/WB attacking output matters materially.
- Defender attacking output may help in the overall player index.

### Goalkeepers
- Primary shot-stopping input: PSxG prevented / goals prevented.
- Save percentage is supporting context.
- Distribution/ball-playing matters secondarily.

## Match context
### Opponent strength
No opponent-strength adjustment. FUTX judges what happened against the opponent actually faced.

### Knockout matches
All knockout matches get the same stakes boost.
- R16 = QF = SF = Final for the multiplier
- applies to domestic cups, UEFA knockouts, and international knockouts

### League strength
League strength only affects broader seasonal/Best Player Right Now scores, and contributes at most 5% of the final score.
- Weekly Best Performer does not use league strength.
- Domestic cups, European competitions, and internationals are neutral.
- Domestic league matches may receive the league coefficient.
- Coefficients update objectively each season.
- Strength should be based on aggregate European performance of all clubs from a league.
- UCL/UEL/UECL progress counts equally; no prestige multiplier by competition.

## Prime and historical profile
- Age does not affect the main index.
- Separate age-based views may exist (e.g. U21).
- "Prime" is a profile badge only.
- Prime begins after roughly 2–3 seasons of elite output that represents a sustained step-up from the player's prior baseline.
- Prime ends after two consecutive below-prime seasons.
- A player can re-enter prime later.
- Show only whether the player is currently in prime.
- Player profile also shows Peak Season: highest-rated career season.

## Team index
- Top 50 teams Europe-wide.
- Competitive matches only.
- Inputs include results and xG/xGA performance.
- No opponent-strength adjustment.
- Same league-strength framework as players.
- Updates weekly in congested fixture periods and monthly when fixtures are sparse.

## Publishing
- Seasonal backtest first.
- Weekly product later.
- Weekly target: Sunday midnight.
- Monday matches roll into the previous gameweek tally.
- Manual refresh and manual publish for v1.
- Rank movement vs prior published snapshot is displayed.
- Past public rankings are immutable.

## Product surfaces (later)
- App first, shared iOS/Android codebase (React Native/Expo).
- Working website alongside it (Next.js).
- Supabase/Postgres for central backend/database/auth.
- Python for ranking, data ingestion, and backtesting.
- Core rankings open without login.
- Login for comparisons, watchlists, Fan Index and other extras.
- Comparison supports many players but focuses on FUTX overalls/categories rather than becoming a raw-stat database.
- Public profiles for Top 100 only in v1.
- Player detailed-analysis page can contain rating history.
- Team profile pages included.
- Private admin dashboard controls archetypes, approvals, weights/formulas, fixes and publishing.
- Metric weights and role formulas should be editable rather than hard-coded.

## Initial backtest plan
Primary quantitative backtest window: 2014/15 onward where free xG-style data is more consistently available.
Earlier seasons may later use a thinner legacy model if data cannot support model parity.

First milestone:
**Generate a reproducible FUTX 2024/25 Top 100 Player ranking and FUTX Team 50 ranking as files, then audit the football plausibility before building UI.**
