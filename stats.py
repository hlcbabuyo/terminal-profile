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

# 2. Timing & Animation Engine (20-second infinite loop)
current_pct = 0.02
dur = "20s"

def get_anim(delay=0.03):
    """Handles the line-by-line pop-up effect."""
    global current_pct
    start = round(current_pct, 3)
    current_pct += delay
    return f'<animate attributeName="opacity" values="0;0;1;1;0;0" keyTimes="0;{start};{start+0.001};0.95;0.951;1" dur="{dur}" repeatCount="indefinite" />'

def get_typing_anim(cmd_length, delay_after=0.03, type_time=0.06):
    """Calculates the sliding 'cover rect' to create a character-by-character typing effect."""
    global current_pct
    start = round(current_pct, 3)
    end_type = round(start + type_time, 3)
    current_pct = end_type + delay_after
    
    # Math to calculate how far the cursor should move based on string length
    start_x = 185
    end_x = start_x + (cmd_length * 8.4)
    
    # 1. Shows the text and the cover rect
    t_anim = f'<animate attributeName="opacity" values="0;0;1;1;0;0" keyTimes="0;{start};{start+0.001};0.95;0.951;1" dur="{dur}" repeatCount="indefinite" />'
    # 2. Slides the cover rect to the right to reveal the text
    c_anim = f'<animate attributeName="x" values="{start_x};{start_x};{end_x};{end_x};{start_x};{start_x}" keyTimes="0;{start};{end_type};0.95;0.951;1" dur="{dur}" repeatCount="indefinite" />'
    # 3. Moves the "█" cursor along with the cover rect
    cx_anim = f'<animate attributeName="x" values="{start_x};{start_x};{end_x};{end_x};{start_x};{start_x}" keyTimes="0;{start};{end_type};0.95;0.951;1" dur="{dur}" repeatCount="indefinite" />'
    # 4. Hides the moving cursor when typing finishes
    co_anim = f'<animate attributeName="opacity" values="0;0;1;1;0;0" keyTimes="0;{start};{start+0.001};{end_type};{end_type+0.001};1" dur="{dur}" repeatCount="indefinite" />'
    
    return t_anim, c_anim, cx_anim, co_anim

# --- Generating the Commands with Typing Effects ---

t1, c1, cx1, co1 = get_typing_anim(len("github-stats --user hlcbabuyo"))
cmd1 = f'''<text x="0" y="60" class="text" opacity="0"><tspan class="prompt">hlcbabuyo@github</tspan> ~&gt; github-stats --user hlcbabuyo{t1}</text>
<rect x="185" y="45" width="450" height="20" class="bg" opacity="0">{t1}{c1}</rect>
<text x="185" y="60" class="text" opacity="0">█{cx1}{co1}</text>'''

t2, c2, cx2, co2 = get_typing_anim(len("cat skills.txt"))
cmd2 = f'''<text x="0" y="280" class="text" opacity="0"><tspan class="prompt">hlcbabuyo@github</tspan> ~&gt; cat skills.txt{t2}</text>
<rect x="185" y="265" width="450" height="20" class="bg" opacity="0">{t2}{c2}</rect>
<text x="185" y="280" class="text" opacity="0">█{cx2}{co2}</text>'''

t3, c3, cx3, co3 = get_typing_anim(len("echo 'Thanks for visiting my profile!'"))
cmd3 = f'''<text x="0" y="520" class="text" opacity="0"><tspan class="prompt">hlcbabuyo@github</tspan> ~&gt; echo 'Thanks for visiting my profile!'{t3}</text>
<rect x="185" y="505" width="450" height="20" class="bg" opacity="0">{t3}{c3}</rect>
<text x="185" y="520" class="text" opacity="0">█{cx3}{co3}</text>'''


# 3. Assemble the final SVG
svg_content = f"""<svg width="800" height="620" viewBox="0 0 800 620" xmlns="http://www.w3.org/2000/svg">
  <style>
    .bg {{ fill: #0A0A0A; }}
    .text {{ font-family: Consolas, 'Courier New', monospace; font-size: 15px; fill: #CCCCCC; }}
    .prompt {{ fill: #E06C75; }}
    .cyan {{ fill: #56B6C2; }}
    .green {{ fill: #98C379; }}
    .orange {{ fill: #D19A66; }}
    .blue {{ fill: #61AFEF; }}
    .blink {{ animation: blinker 1s step-end infinite; }}
    @keyframes blinker {{ 50% {{ opacity: 0; }} }}
  </style>

  <rect width="100%" height="100%" class="bg"/>

  <g transform="translate(20, 30)">
    
    <!-- Boot Sequence -->
    <text x="0" y="0" class="text" opacity="0">Initializing terminal...{get_anim(0.04)}</text>
    <text x="0" y="20" class="text" opacity="0"><tspan class="green">[OK]</tspan> System ready{get_anim(0.06)}</text>

    <!-- Command 1: GitHub Stats -->
    {cmd1}
    <text x="0" y="100" class="text cyan" opacity="0">=== GitHub Stats for hlcbabuyo ==={get_anim(0.02)}</text>
    <text x="0" y="120" class="text" opacity="0"><tspan class="orange">Name:</tspan>        Harvie Lorenz C. Babuyo{get_anim(0.02)}</text>
    <text x="0" y="140" class="text" opacity="0"><tspan class="orange">Role:</tspan>        Backend Systems Engineer{get_anim(0.02)}</text>
    <text x="0" y="160" class="text" opacity="0"><tspan class="orange">Location:</tspan>    Tagoloan, Misamis Oriental, Philippines{get_anim(0.02)}</text>
    <text x="0" y="180" class="text" opacity="0"><tspan class="orange">Goal:</tspan>        240-Hour OJT (June 2026){get_anim(0.02)}</text>
    <text x="0" y="200" class="text" opacity="0"><tspan class="orange">Repos:</tspan>       {repos}{get_anim(0.02)}</text>
    <text x="0" y="220" class="text" opacity="0"><tspan class="orange">Followers:</tspan>   {followers}{get_anim(0.02)}</text>
    <text x="0" y="240" class="text cyan" opacity="0">=================================={get_anim(0.06)}</text>

    <!-- Command 2: Tech Stack -->
    {cmd2}
    <text x="0" y="320" class="text cyan" opacity="0">=== Tech Stack ==={get_anim(0.02)}</text>
    <text x="0" y="340" class="text" opacity="0"><tspan class="blue">Backend:</tspan>     Python, FastAPI, SQLAlchemy, Pydantic{get_anim(0.02)}</text>
    <text x="0" y="360" class="text" opacity="0"><tspan class="blue">Database:</tspan>    PostgreSQL, PostGIS, Redis{get_anim(0.02)}</text>
    <text x="0" y="380" class="text" opacity="0"><tspan class="blue">Cloud:</tspan>       AWS (S3, EC2, RDS, IAM){get_anim(0.02)}</text>
    <text x="0" y="400" class="text" opacity="0"><tspan class="blue">DevOps:</tspan>      Docker, Git, GitHub Actions{get_anim(0.02)}</text>
    <text x="0" y="420" class="text" opacity="0"><tspan class="blue">Processing:</tspan>  Celery, BeautifulSoup{get_anim(0.02)}</text>
    <text x="0" y="440" class="text" opacity="0"><tspan class="blue">Tools:</tspan>       ReportLab, QRCode, boto3, Postman{get_anim(0.02)}</text>
    <text x="0" y="460" class="text" opacity="0"><tspan class="blue">Languages:</tspan>   Python, SQL{get_anim(0.02)}</text>
    <text x="0" y="480" class="text cyan" opacity="0">=================={get_anim(0.06)}</text>

    <!-- Command 3: The Outro -->
    {cmd3}
    <text x="0" y="540" class="text green" opacity="0">Thanks for visiting my profile!{get_anim(0.06)}</text>

    <!-- Final Prompt with Blinking Cursor -->
    <g opacity="0">
        <animate attributeName="opacity" values="0;0;1;1;0;0" keyTimes="0;{current_pct};{current_pct+0.001};0.95;0.951;1" dur="{dur}" repeatCount="indefinite" />
        <text x="0" y="580" class="text"><tspan class="prompt">hlcbabuyo@github</tspan> ~&gt; <tspan class="blink">█</tspan></text>
    </g>
    
  </g>
</svg>"""

with open("terminal.svg", "w", encoding="utf-8") as file:
    file.write(svg_content)

print("Masterpiece SVG generated successfully!")
