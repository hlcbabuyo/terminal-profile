# 💻 Terminal Profile Generator

<div align="center">
  <img src="https://raw.githubusercontent.com/hlcbabuyo/terminal-profile/main/terminal.svg?v=1" alt="Harvie's Terminal Setup">
</div>

<br>

## 🚀 Overview

This repository contains the source code that generates the dynamic, animated terminal SVG displayed on my GitHub profile. 

Instead of relying on third-party stat cards, I built a custom Python script that interfaces with the GitHub API to fetch live metrics and injects them directly into a raw SVG file. The result is a lightweight, zero-dependency, fully animated "hacker terminal" aesthetic complete with a spinning 3D Orbital Data Core.

## ✨ Features

* **Dynamic Data:** Fetches live follower and public repository counts via the GitHub REST API.
* **Pure SVG & CSS Animation:** The typing effects, blinking cursor, and rotating tech globe are powered entirely by native SVG `<animate>` and `<animateTransform>` tags—no external CSS or JavaScript required.
* **Zero Dependencies:** The generator script (`stats.py`) uses only Python's standard library (`urllib`, `json`), making it fast and secure.
* **Fully Automated:** Runs on a cron schedule using GitHub Actions to ensure the profile stats are always up to date.

## 🛠️ How It Works

1. **`stats.py`** executes and sends a request to the GitHub API.
2. The script parses the JSON response to extract the latest stats.
3. It dynamically constructs an SVG string, injecting the stats and calculating staggered animation delays for the "line-by-line" typing effect.
4. The final output is written to `terminal.svg`.
5. A GitHub Action commits and pushes the updated SVG back to the repository.

## ⚙️ Tech Stack

* **Language:** Python 3
* **Format:** SVG, XML
* **Automation:** GitHub Actions, CRON
* **API:** GitHub REST API

## 📝 Usage

If you want to fork this for your own profile:
1. Fork this repository.
2. Update the `url` in `stats.py` to point to your GitHub username.
3. Modify the text lines inside the `svg_content` string to match your own tech stack and bio.
4. Run the script locally with `python stats.py` to test your changes.
5. Enable GitHub Actions in your fork to automate the updates.

---
*Designed and engineered by Harvie Lorenz C. Babuyo.*
