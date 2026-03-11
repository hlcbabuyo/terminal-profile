import time
import urllib.request
import json
import sys

# 1. Fetch live GitHub stats
try:
    url = "https://api.github.com/users/hlcbabuyo"
    req = urllib.request.Request(url)
    with urllib.request.urlopen(req) as response:
        data = json.loads(response.read().decode())
        repos = data.get('public_repos', 0)
        followers = data.get('followers', 0)
except Exception:
    repos = "N/A"
    followers = "N/A"

# 2. Terminal Boot-up Animation
def type_text(text, delay=0.03):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

print()
type_text("\033[32m>_ Initializing backend connection...\033[0m")
type_text("\033[32m>_ Fetching metrics from GitHub API...\033[0m")
type_text("\033[32m>_ Rendering UI...\033[0m")
time.sleep(0.5)

# 3. The Custom ASCII Art & Tech Stack
ascii_layout = f"""
\033[36m    .---------------------------.
    |  \033[32m>_ hlcbabuyo@server\033[36m      |   \033[1;37m=== Harvie Lorenz C. Babuyo ===\033[0m
    |                           |   \033[90mRole:      \033[37mBackend Systems Engineer\033[0m
    |  \033[33mRepos: \033[37m{str(repos).ljust(4)}\033[36m             |   \033[90mLocation:  \033[37mTagoloan, Philippines\033[0m
    |  \033[35mFollowers: \033[37m{str(followers).ljust(4)}\033[36m         |   \033[90mGoal:      \033[37m240-Hour OJT (June 2026)\033[0m
    |                           |
    |___________________________|   \033[1;37m=== Tech Stack ===\033[0m
         _[_______]_                \033[90mBackend:     \033[32mPython, FastAPI, SQLAlchemy, Pydantic\033[0m
         \          /                 \033[90mDatabase:    \033[34mPostgreSQL, PostGIS, Redis\033[0m
          \________/                  \033[90mCloud:       \033[33mAWS (S3, EC2, RDS, IAM)\033[0m
                                    \033[90mDevOps:      \033[35mDocker, Git, GitHub Actions\033[0m
                                    \033[90mProcessing:  \033[36mCelery, BeautifulSoup\033[0m
                                    \033[90mTools:       \033[31mReportLab, QRCode, boto3, Postman\033[0m
                                    \033[90mLanguages:   \033[93mPython, SQL\033[0m
"""

print(ascii_layout)
print("\033[32m>_ System ready. Type 'help' for commands.\033[0m")
time.sleep(5)
