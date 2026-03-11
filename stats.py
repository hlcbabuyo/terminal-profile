import gifos
from datetime import datetime
import os
import requests

# ============================================
# Terminal GIF with GitHub Stats
# ============================================
# 
# REQUIREMENTS:
# 1. Create a .env file in the project folder
# 2. Add: GITHUB_TOKEN=your_token_here
#
# To create the token:
# - Go to: https://github.com/settings/tokens
# - Click "Generate new token (classic)"
# - Select only: read:user
# - Copy the token and add it to .env
# ============================================

USERNAME = "hlcbabuyo"  # <- Your GitHub username

# Function to fetch real number of repos
def get_total_repos(username):
    try:
        response = requests.get(f"https://api.github.com/users/{username}")
        if response.status_code == 200:
            return response.json().get("public_repos", 0)
    except:
        pass
    return None

# Try to fetch GitHub statistics
try:
    github_stats = gifos.utils.fetch_github_stats(user_name=USERNAME)
    has_stats = github_stats is not None
    if not has_stats:
        print("Warning: Could not fetch GitHub stats")
        print("Configure GITHUB_TOKEN in .env file")
except Exception as e:
    print(f"Warning: Error fetching GitHub stats: {e}")
    print("Using example data...")
    has_stats = False
    github_stats = None

# Fetch real number of repos
total_repos = get_total_repos(USERNAME)

# Terminal settings (Widened to 850 so your skills fit perfectly)
t = gifos.Terminal(width=850, height=450, xpad=10, ypad=10)

# -- Initial prompt --
t.set_prompt(f"\x1b[91m{USERNAME}\x1b[0m@\x1b[93mgithub\x1b[0m ~> ")

# -- Boot sequence --
t.gen_text("Initializing terminal...", row_num=1)
t.clone_frame(5)
t.gen_text("\x1b[32m[OK]\x1b[0m System ready", row_num=2)
t.clone_frame(10)

# -- Command to view stats --
t.gen_prompt(row_num=3)
t.gen_typing_text("github-stats --user " + USERNAME, row_num=3, contin=True, speed=1)
t.clone_frame(5)

# -- Display statistics --
t.gen_text("", row_num=4)
t.gen_text(f"\x1b[96m=== GitHub Stats for {USERNAME} ===\x1b[0m", row_num=5)
t.clone_frame(3)

if has_stats:
    repos_count = total_repos if total_repos else github_stats.total_repo_contributions
    stats_lines = [
        f"\x1b[93mName:\x1b[0m        Harvie Lorenz C. Babuyo",
        f"\x1b[93mRole:\x1b[0m        Backend Systems Engineer",
        f"\x1b[93mLocation:\x1b[0m    Tagoloan, Misamis Oriental, Philippines",
        f"\x1b[93mGoal:\x1b[0m        240-Hour OJT (June 2026)",
        f"\x1b[93mRepos:\x1b[0m       {repos_count}",
        f"\x1b[93mFollowers:\x1b[0m   {github_stats.total_followers}",
    ]
else:
    # Example data fallback
    stats_lines = [
        f"\x1b[93mName:\x1b[0m        Harvie Lorenz C. Babuyo",
        f"\x1b[93mRole:\x1b[0m        Backend Systems Engineer",
        f"\x1b[93mLocation:\x1b[0m    Tagoloan, Misamis Oriental, Philippines",
        f"\x1b[93mGoal:\x1b[0m        240-Hour OJT (June 2026)",
        "\x1b[93mRepos:\x1b[0m       --",
        "\x1b[93mFollowers:\x1b[0m   --",
    ]

# Print stats line by line
for i, line in enumerate(stats_lines):
    t.gen_text(line, row_num=6+i)
    t.clone_frame(3)

t.clone_frame(10)
t.gen_text("\x1b[96m================================\x1b[0m", row_num=6+len(stats_lines))
t.clone_frame(15)

# -- Clear the screen --
t.gen_prompt(row_num=7+len(stats_lines))
t.gen_typing_text("clear", row_num=7+len(stats_lines), contin=True, speed=1)
t.clone_frame(5)
t.clear_frame()

# -- Command to view skills --
t.gen_prompt(row_num=1)
t.gen_typing_text("cat skills.txt", row_num=1, contin=True, speed=1)
t.clone_frame(5)

t.gen_text("", row_num=2)
t.gen_text("\x1b[96m=== Tech Stack ===\x1b[0m", row_num=3)
t.clone_frame(3)

# Your specific Tech Stack
skills = [
    ("\x1b[94mBackend:\x1b[0m     ", "Python, FastAPI, SQLAlchemy, Pydantic"),
    ("\x1b[94mDatabase:\x1b[0m    ", "PostgreSQL, PostGIS, Redis"),
    ("\x1b[94mCloud:\x1b[0m       ", "AWS (S3, EC2, RDS, IAM)"),
    ("\x1b[94mDevOps:\x1b[0m      ", "Docker, Git, GitHub Actions"),
    ("\x1b[94mProcessing:\x1b[0m  ", "Celery, BeautifulSoup"),
    ("\x1b[94mTools:\x1b[0m       ", "ReportLab, QRCode, boto3, Postman"),
    ("\x1b[94mLanguages:\x1b[0m   ", "Python, SQL"),
]

# Print skills line by line
for i, (label, value) in enumerate(skills):
    t.gen_text(f"{label}{value}", row_num=4+i)
    t.clone_frame(2)

t.clone_frame(10)
t.gen_text("\x1b[96m==================\x1b[0m", row_num=4+len(skills))
t.clone_frame(5)

# -- Final message --
final_row = 5 + len(skills)
t.gen_prompt(row_num=final_row)
t.gen_typing_text("echo 'Thanks for visiting my profile!'", row_num=final_row, contin=True, speed=1)
t.clone_frame(5)
t.gen_text("\x1b[92mThanks for visiting my profile!\x1b[0m", row_num=final_row+1)
t.clone_frame(40)

# Generate the GIF
t.gen_gif()

print("\n GIF generated: output.gif")
