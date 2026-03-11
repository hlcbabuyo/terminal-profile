import urllib.request
import json

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

# 2. Dynamic Animation Generator
# This automatically calculates the delay for each line so they appear one by one!
current_pct = 0.02
def get_anim(delay=0.03):
    global current_pct
    start = round(current_pct, 3)
    current_pct += delay
    # Each line stays visible until 95% of the 20-second loop, then vanishes to restart.
    return f'<animate attributeName="opacity" values="0;0;1;1;0;0" keyTimes="0;{start};{start+0.001};0.95;0.951;1" dur="20s" repeatCount="indefinite" />'

# 3. Build the Animated SVG
svg_content = f"""<svg width="100%" height="620" viewBox="0 0 800 620" preserveAspectRatio="xMidYMid meet" xmlns="http://www.w3.org/2000/svg">
  <style>
    .bg {{ fill: #0A0A0A; }}
    .text {{ font-family: Consolas, 'Courier New', monospace; font-size: 15px; fill: #CCCCCC; }}
    .prompt {{ fill: #E06C75; }}
    .cyan {{ fill: #56B6C2; }}
    .green {{ fill: #98C379; }}
    .orange {{ fill: #D19A66; }}
    .blue {{ fill: #61AFEF; }}
  </style>

  <!-- Clean Black Terminal Background -->
  <rect width="100%" height="100%" class="bg"/>

  <!-- Terminal Content -->
  <g transform="translate(20, 30)">
    
    <!-- Boot Sequence -->
    <text x="0" y="0" class="text" opacity="0">Initializing terminal...{get_anim(0.04)}</text>
    <text x="0" y="20" class="text" opacity="0"><tspan class="green">[OK]</tspan> System ready{get_anim(0.06)}</text>

    <!-- Command 1: GitHub Stats -->
    <text x="0" y="60" class="text" opacity="0"><tspan class="prompt">hlcbabuyo@github</tspan> ~&gt; github-stats --user hlcbabuyo{get_anim(0.04)}</text>
    
    <text x="0" y="100" class="text cyan" opacity="0">=== GitHub Stats for hlcbabuyo ==={get_anim()}</text>
    <text x="0" y="120" class="text" opacity="0"><tspan class="orange">Name:</tspan>        Harvie Lorenz C. Babuyo{get_anim()}</text>
    <text x="0" y="140" class="text" opacity="0"><tspan class="orange">Role:</tspan>        Backend Systems Engineer{get_anim()}</text>
    <text x="0" y="160" class="text" opacity="0"><tspan class="orange">Location:</tspan>    Tagoloan, Misamis Oriental, Philippines{get_anim()}</text>
    <text x="0" y="180" class="text" opacity="0"><tspan class="orange">Goal:</tspan>        240-Hour OJT (June 2026){get_anim()}</text>
    <text x="0" y="200" class="text" opacity="0"><tspan class="orange">Repos:</tspan>       {repos}{get_anim()}</text>
    <text x="0" y="220" class="text" opacity="0"><tspan class="orange">Followers:</tspan>   {followers}{get_anim()}</text>
    <text x="0" y="240" class="text cyan" opacity="0">=================================={get_anim(0.06)}</text>

    <!-- Command 2: Tech Stack -->
    <text x="0" y="280" class="text" opacity="0"><tspan class="prompt">hlcbabuyo@github</tspan> ~&gt; cat skills.txt{get_anim(0.04)}</text>
    
    <text x="0" y="320" class="text cyan" opacity="0">=== Tech Stack ==={get_anim()}</text>
    <text x="0" y="340" class="text" opacity="0"><tspan class="blue">Backend:</tspan>     Python, FastAPI, SQLAlchemy, Pydantic{get_anim()}</text>
    <text x="0" y="360" class="text" opacity="0"><tspan class="blue">Database:</tspan>    PostgreSQL, PostGIS, Redis{get_anim()}</text>
    <text x="0" y="380" class="text" opacity="0"><tspan class="blue">Cloud:</tspan>       AWS (S3, EC2, RDS, IAM){get_anim()}</text>
    <text x="0" y="400" class="text" opacity="0"><tspan class="blue">DevOps:</tspan>      Docker, Git, GitHub Actions{get_anim()}</text>
    <text x="0" y="420" class="text" opacity="0"><tspan class="blue">Processing:</tspan>  Celery, BeautifulSoup{get_anim()}</text>
    <text x="0" y="440" class="text" opacity="0"><tspan class="blue">Tools:</tspan>       ReportLab, QRCode, boto3, Postman{get_anim()}</text>
    <text x="0" y="460" class="text" opacity="0"><tspan class="blue">Languages:</tspan>   Python, SQL{get_anim()}</text>
    <text x="0" y="480" class="text cyan" opacity="0">=================={get_anim(0.06)}</text>

    <!-- Command 3: The Outro -->
    <text x="0" y="520" class="text" opacity="0"><tspan class="prompt">hlcbabuyo@github</tspan> ~&gt; echo 'Thanks for visiting my profile!'{get_anim(0.04)}</text>
    <text x="0" y="540" class="text green" opacity="0">Thanks for visiting my profile!{get_anim(0.06)}</text>

    <!-- Final Prompt with Blinking Cursor -->
    <text x="0" y="580" class="text" opacity="0"><tspan class="prompt">hlcbabuyo@github</tspan> ~&gt; <tspan fill="#CCCCCC"><animate attributeName="opacity" values="1;0" keyTimes="0;0.5" dur="1s" repeatCount="indefinite" />█</tspan>{get_anim(0)}</text>
    
  </g>
</svg>"""

with open("terminal.svg", "w", encoding="utf-8") as file:
    file.write(svg_content)

print("Line-by-line animated SVG generated successfully!")
