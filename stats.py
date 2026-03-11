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
current_pct = 0.02
def get_anim(delay=0.03):
    global current_pct
    start = round(current_pct, 3)
    current_pct += delay
    return f'<animate attributeName="opacity" values="0;0;1;1;0;0" keyTimes="0;{start};{start+0.001};0.95;0.951;1" dur="20s" repeatCount="indefinite" />'

# 3. Build the Animated SVG
svg_content = f"""<svg width="100%" height="620" viewBox="0 0 1200 620" preserveAspectRatio="xMidYMid meet" xmlns="http://www.w3.org/2000/svg">
  <style>
    .bg {{ fill: #0A0A0A; }}
    .text {{ font-family: Consolas, 'Courier New', monospace; font-size: 15px; fill: #CCCCCC; }}
    .prompt {{ fill: #E06C75; }}
    .cyan {{ fill: #56B6C2; }}
    .green {{ fill: #98C379; }}
    .orange {{ fill: #D19A66; }}
    .blue {{ fill: #61AFEF; }}
  </style>

  <rect width="100%" height="100%" class="bg"/>

  <g transform="translate(20, 30)">
    
    <text x="0" y="0" class="text" opacity="0">Initializing terminal...{get_anim(0.04)}</text>
    <text x="0" y="20" class="text" opacity="0"><tspan class="green">[OK]</tspan> System ready{get_anim(0.06)}</text>

    <text x="0" y="60" class="text" opacity="0"><tspan class="prompt">hlcbabuyo@github</tspan> ~&gt; github-stats --user hlcbabuyo{get_anim(0.04)}</text>
    
    <text x="0" y="100" class="text cyan" opacity="0">=== GitHub Stats for hlcbabuyo ==={get_anim()}</text>
    <text x="0" y="120" class="text" opacity="0"><tspan class="orange">Name:</tspan>        Harvie Lorenz C. Babuyo{get_anim()}</text>
    <text x="0" y="140" class="text" opacity="0"><tspan class="orange">Role:</tspan>        Backend Systems Engineer{get_anim()}</text>
    <text x="0" y="160" class="text opacity="0"><tspan class="orange">Location:</tspan>    Tagoloan, Misamis Oriental, Philippines{get_anim()}</text>
    <text x="0" y="180" class="text opacity="0"><tspan class="orange">Goal:</tspan>        240-Hour OJT (June 2026){get_anim()}</text>
    <text x="0" y="200" class="text opacity="0"><tspan class="orange">Repos:</tspan>       {repos}{get_anim()}</text>
    <text x="0" y="220" class="text opacity="0"><tspan class="orange">Followers:</tspan>   {followers}{get_anim()}</text>
    <text x="0" y="240" class="text cyan" opacity="0">=================================={get_anim(0.06)}</text>

    <text x="0" y="280" class="text opacity="0"><tspan class="prompt">hlcbabuyo@github</tspan> ~&gt; cat skills.txt{get_anim(0.04)}</text>
    
    <text x="0" y="320" class="text cyan" opacity="0">=== Tech Stack ==={get_anim()}</text>
    <text x="0" y="340" class="text opacity="0"><tspan class="blue">Backend:</tspan>     Python, FastAPI, SQLAlchemy, Pydantic{get_anim()}</text>
    <text x="0" y="360" class="text opacity="0"><tspan class="blue">Database:</tspan>    PostgreSQL, PostGIS, Redis{get_anim()}</text>
    <text x="0" y="380" class="text opacity="0"><tspan class="blue">Cloud:</tspan>       AWS (S3, EC2, RDS, IAM){get_anim()}</text>
    <text x="0" y="400" class="text opacity="0"><tspan class="blue">DevOps:</tspan>      Docker, Git, GitHub Actions{get_anim()}</text>
    <text x="0" y="420" class="text opacity="0"><tspan class="blue">Processing:</tspan>  Celery, BeautifulSoup{get_anim()}</text>
    <text x="0" y="440" class="text opacity="0"><tspan class="blue">Tools:</tspan>       ReportLab, QRCode, boto3, Postman{get_anim()}</text>
    <text x="0" y="460" class="text opacity="0"><tspan class="blue">Languages:</tspan>   Python, SQL{get_anim()}</text>
    <text x="0" y="480" class="text cyan" opacity="0">=================={get_anim(0.06)}</text>

    <text x="0" y="520" class="text opacity="0"><tspan class="prompt">hlcbabuyo@github</tspan> ~&gt; echo 'Thanks for visiting my profile!'{get_anim(0.04)}</text>
    <text x="0" y="540" class="text green" opacity="0">Thanks for visiting my profile!{get_anim(0.06)}</text>

    <text x="0" y="580" class="text opacity="0"><tspan class="prompt">hlcbabuyo@github</tspan> ~&gt; <tspan fill="#CCCCCC"><animate attributeName="opacity" values="1;0" keyTimes="0;0.5" dur="1s" repeatCount="indefinite" />█</tspan>{get_anim(0)}</text>
  </g>

  <g transform="translate(880, 310)">
    
    <circle cx="0" cy="0" r="220" fill="none" stroke="#56B6C2" stroke-width="1.5" stroke-dasharray="10 20" opacity="0.4">
      <animateTransform attributeName="transform" type="rotate" from="0" to="360" dur="40s" repeatCount="indefinite"/>
    </circle>
    
    <circle cx="0" cy="0" r="180" fill="none" stroke="#61AFEF" stroke-width="2" stroke-dasharray="15 15 5 15" opacity="0.3">
      <animateTransform attributeName="transform" type="rotate" from="360" to="0" dur="25s" repeatCount="indefinite"/>
    </circle>
    
    <ellipse cx="0" cy="0" rx="120" ry="240" fill="none" stroke="#E06C75" stroke-width="1" opacity="0.3">
      <animateTransform attributeName="transform" type="rotate" from="0" to="360" dur="20s" repeatCount="indefinite"/>
    </ellipse>
    <ellipse cx="0" cy="0" rx="120" ry="240" fill="none" stroke="#98C379" stroke-width="1" opacity="0.3">
      <animateTransform attributeName="transform" type="rotate" from="60" to="420" dur="20s" repeatCount="indefinite"/>
    </ellipse>
    <ellipse cx="0" cy="0" rx="120" ry="240" fill="none" stroke="#D19A66" stroke-width="1" opacity="0.3">
      <animateTransform attributeName="transform" type="rotate" from="120" to="480" dur="20s" repeatCount="indefinite"/>
    </ellipse>

    <circle cx="0" cy="0" r="45" fill="#1E222A" stroke="#61AFEF" stroke-width="3">
       <animate attributeName="r" values="40;50;40" dur="4s" repeatCount="indefinite"/>
       <animate attributeName="stroke" values="#61AFEF;#56B6C2;#61AFEF" dur="4s" repeatCount="indefinite"/>
    </circle>
    
    <circle cx="0" cy="0" r="15" fill="#98C379">
        <animate attributeName="opacity" values="0.4;1;0.4" dur="2s" repeatCount="indefinite"/>
    </circle>

    <g>
      <animateTransform attributeName="transform" type="rotate" from="0" to="360" dur="8s" repeatCount="indefinite"/>
      <circle cx="0" cy="-180" r="6" fill="#98C379" />
      <circle cx="180" cy="0" r="4" fill="#E06C75" />
    </g>
    <g>
      <animateTransform attributeName="transform" type="rotate" from="360" to="0" dur="12s" repeatCount="indefinite"/>
      <circle cx="0" cy="220" r="5" fill="#56B6C2" />
      <circle cx="-220" cy="0" r="7" fill="#D19A66" />
    </g>
    
  </g>
</svg>"""

with open("terminal.svg", "w", encoding="utf-8") as file:
    file.write(svg_content)

print("Line-by-line animated SVG with Orbital Tech Core generated successfully!")
