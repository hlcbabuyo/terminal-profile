# 💻 Terminal Profile Generator

<div align="center">
  <img src="https://raw.githubusercontent.com/hlcbabuyo/terminal-profile/main/terminal.svg?v=1" alt="Harvie's Terminal Setup">
</div>

<br>

## 🚀 Overview

This repository generates the dynamic, animated terminal SVG displayed on my GitHub profile. Rather than relying on third-party stat cards, a custom Python script interfaces directly with the GitHub REST API to fetch live metrics and injects them into a raw SVG file — no external dependencies, no third-party services.

The result is a fully self-contained, auto-updating terminal animation that runs on a daily schedule via GitHub Actions.

---

## ✨ Features

- **Live GitHub Stats** — Fetches real-time follower and public repository counts via the GitHub REST API on every run.
- **Animated Typing Effect** — Each line of text appears character-by-character using staggered SVG `<animate>` keyframe timing, simulating a real terminal session.
- **Pure SVG & CSS** — All animation (typing, blinking cursor, fade-in/out loop) is driven entirely by native SVG `<animate>` and `<animateTransform>` tags. No JavaScript or external CSS required.
- **Zero Python Dependencies** — `stats.py` uses only the Python standard library (`urllib`, `json`). No `pip install` needed.
- **Fully Automated** — GitHub Actions runs the generator on a daily cron schedule and commits the updated SVG back to the repository automatically.

---

## 🛠️ How It Works

```
GitHub Actions Cron → stats.py → GitHub REST API → terminal.svg → Git Commit & Push
```

1. **`stats.py` runs** and sends a request to `https://api.github.com/users/{username}`.
2. The script **parses the JSON response** to extract `public_repos` and `followers`.
3. It **dynamically constructs an SVG string**, injecting the live stats and calculating precise keyframe percentages for each character's animation delay, creating a staggered "line-by-line" typing effect.
4. The final SVG is **written to `terminal.svg`**.
5. The **GitHub Actions workflow** detects the change, commits it with `[skip ci]`, rebases, and pushes it back to `main`.

---

## 📁 Repository Structure

```
terminal-profile/
├── .github/
│   └── workflows/
│       └── build.yml       # GitHub Actions workflow (daily cron + manual trigger)
├── stats.py                # SVG generator script
├── terminal.svg            # Auto-generated output (do not edit manually)
└── README.md               # This file
```

---

## ⚙️ Tech Stack

| Layer | Technology |
|---|---|
| Language | Python 3 (stdlib only) |
| Output Format | SVG / XML |
| Animation | Native SVG `<animate>` tags |
| Automation | GitHub Actions + CRON |
| Data Source | GitHub REST API |

---

## 🔧 Animation Architecture

The SVG animation runs on a **32-second looping cycle** (`dur="32s"`). All timing is expressed as decimal fractions of that cycle (e.g., `0.09` = ~2.9 seconds into the loop).

The generator uses three helper functions to build the SVG programmatically:

| Function | Purpose |
|---|---|
| `char_by_char(text, start_pct)` | Wraps each character in a `<tspan>` with an `<animate>` that reveals it one-by-one |
| `cmd_line(y, text, start_pct)` | Renders a full prompt line (`hlcbabuyo@github ~>`) followed by animated command text |
| `line_svg(content, start_pct)` | Renders a single output line that fades in at the given time offset |

Each call returns both the SVG markup and the updated time offset, so all elements chain naturally without manual timing calculations.

---

## 📝 Forking for Your Own Profile

1. **Fork** this repository.
2. In `stats.py`, update the `username` argument in the `generate()` call at the bottom of the file:
   ```python
   if __name__ == "__main__":
       generate(username="your-github-username")
   ```
3. **Customize the content** — edit the `cmd_line` and `line_svg` calls inside `generate()` to reflect your own name, role, tech stack, and bio.
4. **Test locally** by running:
   ```bash
   python stats.py
   ```
   This writes a `terminal.svg` file you can open in any browser to preview the animation.
5. In your `README.md`, update the `<img>` `src` to point to your fork's raw SVG URL:
   ```
   https://raw.githubusercontent.com/YOUR_USERNAME/terminal-profile/main/terminal.svg
   ```
6. **Enable GitHub Actions** in your fork. The workflow runs automatically every day at midnight UTC, or you can trigger it manually from the Actions tab.

### Adjusting Animation Timing

- `DUR` (default `"32s"`) — total loop duration. Increase it if you add many more lines and run out of timing budget.
- `char_delay` (default `0.002`) — fraction of the loop each character takes to appear. Increase for slower typing.
- The script prints `Total time used: X / 0.95` after each run. Keep this below `0.95` to avoid timing overflow.

---

## 🔄 GitHub Actions Workflow

The workflow in `.github/workflows/build.yml` handles two triggers:

- **Scheduled** — runs daily at `00:00 UTC` via cron (`0 0 * * *`).
- **Manual** — can be triggered at any time from the GitHub Actions tab (`workflow_dispatch`).

After regenerating the SVG, it commits with the message `Update terminal SVG [skip ci]` (to prevent recursive workflow triggers) and rebases before pushing to handle any concurrent updates cleanly.

---

## 🌐 API Reference

The script calls the GitHub Users API:

```
GET https://api.github.com/users/{username}
```

Fields used from the response:

| Field | Used As |
|---|---|
| `public_repos` | Repository count displayed in the terminal |
| `followers` | Follower count displayed in the terminal |

No authentication token is required for public user data, though unauthenticated requests are subject to GitHub's rate limit of 60 requests per hour — well within the daily schedule's needs.

---

*Designed and engineered by Harvie Lorenz C. Babuyo.*
