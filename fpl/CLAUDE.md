# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Running the Application

```bash
# Install dependencies
pip install -r requirements.txt

# Run development server (with hot reload)
python app.py
```

App runs at `http://localhost:5000` with `debug=True`.

**Production deployment:** Heroku via `Procfile`. Currently set to `npm start` — the original working command was `gunicorn app:app`.

```bash
# Deploy a local branch to Heroku
git push heroku <branch-name>:main

# Example: deploy longterm_planning branch
git push heroku longterm_planning:main

# Amend the last commit without changing the message
git commit --amend --no-edit
```

## Architecture Overview

This is a **Flask web app** that aggregates data from the [FPL official API](https://fantasy.premierleague.com/api/) and presents analytics for Fantasy Premier League managers.

### Data Flow

```
FPL API (fantasy.premierleague.com/api/bootstrap-static/)
FBRef (fbref.com) — scraped for xG/xA stats
    ↓
Python data modules (fetched at module import time, not lazily)
    ↓
Flask routes in app.py → Jinja2 templates or JSON responses
```

### Core Modules

| Module                  | Purpose                                                              |
| ----------------------- | -------------------------------------------------------------------- |
| `fpl.py`                | Player data, differentials, transfers, dream team, formations        |
| `fixture_difficulty.py` | FDR calculations, player dataset, best players by position/budget    |
| `livescores.py`         | Live gameweek scores, stadium info, player photo lookups             |
| `gameweek_info.py`      | Deadline, chip usage stats, most captained players                   |
| `team_stats.py`         | xG/xA from FBRef scraping, league table                              |
| `bible.py`              | Returns a random Bible verse displayed on pages                      |
| `setpieceinfo.py`       | Set piece notes per team                                             |
| `manager_info.py`       | Manager lookup by PIN (currently disabled, redirects to coming soon) |

**Important:** All data modules fetch from external APIs at import time (module-level globals). This means the data is fetched once when Flask starts, not on each request.

### Routes

| Route                     | Feature                                                                                   |
| ------------------------- | ----------------------------------------------------------------------------------------- |
| `/`                       | Homepage — gameweek info, FDR table, differentials, transfers                             |
| `/livescore`              | Live scores for current gameweek                                                          |
| `/formations`             | Best-value teams for 6 formations. Accepts `?mode=short` or `?mode=long` (default `long`) |
| `/api/formation/<name>`   | JSON: formation data (names: `442`, `451`, `433`, `532`, `352`, `343`, `dream`). Accepts `?mode=` param |
| `/news`                   | Latest player injury/price change news                                                    |
| `/player_comparison`      | Interactive player comparison tool                                                        |
| `/api/players`            | JSON: full player dataset from `fixture_difficulty.get_dataset()`                         |
| `/stats`, `/manager_info` | Disabled — redirect to `/coming_soon`                                                     |

### Templates & Static Assets

- Templates use **Jinja2** and live in `templates/`. Active templates are named `*1.html` (e.g. `home1.html`, `livescore1.html`). The `old_template/` subdirectory contains legacy/unused templates.
- CSS lives in `static/css/`. `style_2025.css` is the current stylesheet; others may be legacy.
- Player photos and team badges are served from `static/images/`.

## Key Implementation Details

- **Formation algorithm** (`fpl.py`): Selects best-value XI per formation shape using `ranking_score = w_form × norm(form×ICT) + w_fixture × norm(fixture_ease)`. Two modes pre-computed at startup:
  - **Short term** (`mode=short`): next 1 game difficulty, weights 85% form / 15% fixture
  - **Long term** (`mode=long`): avg difficulty over next 6 games, weights 65% form / 35% fixture
  - Both datasets live in `_datasets` dict in `fpl.py`; getter functions (`get_442`, etc.) accept a `mode` param.
- **FDR data** (`fixture_difficulty.py`): Looks ahead up to 10 gameweeks; `next_game_difficulty` is the next fixture's raw FPL difficulty (1–5); `next_7` is the full list used for long-term averaging.
- **Team name/badge mappings** are hardcoded and duplicated across `fpl.py` and `livescores.py` — update both if Premier League teams change.
- **No test suite** and no linter configuration exist in this project.
