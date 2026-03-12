import urllib.request
import json

# 1. Fetch live GitHub stats
try:
    url = "https://api.github.com/users/hlcbabuyo"
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    with urllib.request.urlopen(req) as response:
        data = json.loads(response.read().decode())
        repos = data.get('public_repos', 0)
        followers = data.get('followers', 0)
except Exception:
    repos = "5"
    followers = "11"

# 2. Timing & Animation Config
dur = "24s"
current_pct = 0.01

def get_anim(delay=0.02):
    """Line-by-line popup animation for output lines."""
    global current_pct
    start = round(current_pct, 3)
    current_pct += delay
    # Visible from 'start' to 95%, then disappears for loop reset
    return f'<animate attributeName="opacity" values="0;0;1;1;0;0" keyTimes="0;{start};{start+0.001};0.95;0.951;1" dur="{dur}" repeatCount="indefinite" />'

def get_typing_anim(text, x_offset=185, type_speed=0.004):
    """Creates a character-by-character typing reveal with a moving cursor."""
    global current_pct
    start = round(current_pct, 3)
    text_len = len(text)
    type_end = round(start + (text_len * type_speed), 3)
    current_pct = type_end + 0.02
    
    char_w = 9.1 # Approximate width of Consolas characters
    cursor_start = x_offset
    cursor_end = x_offset + (text_len * char_w)

    # 1. Reveal the text line
    t_anim = f'<animate attributeName="opacity" values="0;0;1;1;0;0" keyTimes="0;{start};{start+0.001};0.95;0.951;1" dur="{dur}" repeatCount="indefinite" />'
    # 2. Move the black "mask" rectangle to reveal characters
    m_anim = f'<animate attributeName="width" values="{text_len*char_w};{text_len*char_w};0;0;{text_len*char_w};{text_len*char_w}" keyTimes="0;{start};{type_end};0.95;0.951;1" dur="{dur}" repeatCount="indefinite" />'
    # 3. Move the typing cursor
    c_anim = f'<animate attributeName="x" values="{cursor_start};{cursor_start};{cursor_end};{cursor_end};{cursor_start};{cursor_start}" keyTimes="0;{start};{type_end};0.95;0.951;1" dur="{dur}" repeatCount="indefinite" />'
    # 4. Hide the cursor when not typing
    co_anim = f'<animate attributeName="opacity" values="0;0;1;1;0;0;0" keyTimes="0;{start};{start+0.001};{type_end};{type_end+0.001};0.95;1" dur="{dur}" repeatCount="indefinite" />'
    
    return t_anim, m_anim, c_anim, co_anim

# 3. Build the Masterpiece SVG
svg_content = f"""<svg width="850" height="620" viewBox="0 0 850 620" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <!-- Retro Glow Filter -->
    <filter id="glow" x="-20%" y="-20%" width="140%" height="140%">
      <feGaussianBlur stdDeviation="2.5" result="blur" />
      <feComposite in="SourceGraphic" in2="blur" operator="over" />
    </filter>
  </defs>

  <style>
    .bg {{ fill: #050505; }}
    .text {{ 
        font-family: Consolas, 'Courier New', monospace; 
        font-size: 16px; 
        fill: #D0D0D0; 
        filter: url(#glow); 
    }}
    .prompt {{ fill: #FF5C5C; font-weight: bold; }}
    .cyan {{ fill: #70FFFF; }}
    .green {{ fill: #5CFF5C; }}
    .orange {{ fill: #FFB86C; }}
    .blue {{ fill: #6272A4; }}
    .blink {{ animation: blinker 1s step-end infinite; }}
    @keyframes blinker {{ 50% {{ opacity: 0; }} }}
  </style>

  <!-- Solid Black Background -->
  <rect width="100%" height="100%" class="bg"/>

  <g transform="translate(30, 40)">
    <!-- Boot -->
    <text x="0" y="0" class="text" opacity="0">Initializing HLC-OS...{get_anim(0.04)}</text>
    <text x="0" y="25" class="text" opacity="0"><tspan class="green">[READY]</tspan> System established.{get_anim(0.06)}</text>

    <!-- Command 1: Typing github-stats -->
    <g opacity="0">
        {{ "get_typing_anim('github-stats --user hlcbabuyo')[0]" }}
        <text x="0" y="70" class="text"><tspan class="prompt">hlcbabuyo@server</tspan> ~&gt; github-stats --user hlcbabuyo</text>
        <rect x="185" y="52" width="400" height="22" class="bg">
            {{ "get_typing_anim('github-stats --user hlcbabuyo')[1]" }}
        </rect>
        <text x="185" y="70" class="text">█
            {{ "get_typing_anim('github-stats --user hlcbabuyo')[2]" }}
            {{ "get_typing_anim('github-stats --user hlcbabuyo')[3]" }}
        </text>
    </g>

    <!-- Stats Output -->
    <text x="0" y="110" class="text cyan" opacity="0">=== GITHUB ANALYTICS ==={get_anim()}</text>
    <text x="0" y="135" class="text" opacity="0"><tspan class="orange">NAME:</tspan>       Harvie Lorenz C. Babuyo{get_anim()}</text>
    <text x="0" y="160" class="text" opacity="0"><tspan class="orange">ROLE:</tspan>       Backend Systems Engineer{get_anim()}</text>
    <text x="0" y="185" class="text" opacity="0"><tspan class="orange">LOC:</tspan>        Tagoloan, Philippines{get_anim()}</text>
    <text x="0" y="210" class="text" opacity="0"><tspan class="orange">REPOS:</tspan>      {repos}{get_anim()}</text>
    <text x="0" y="235" class="text" opacity="0"><tspan class="orange">FOLLOWERS:</tspan>  {followers}{get_anim(0.08)}</text>

    <!-- Command 2: Typing cat skills.txt -->
    <g opacity="0">
        {{ "get_typing_anim('cat skills.txt')[0]" }}
        <text x="0" y="285" class="text"><tspan class="prompt">hlcbabuyo@server</tspan> ~&gt; cat skills.txt</text>
        <rect x="185" y="267" width="200" height="22" class="bg">
            {{ "get_typing_anim('cat skills.txt')[1]" }}
        </rect>
        <text x="185" y="285" class="text">█
            {{ "get_typing_anim('cat skills.txt')[2]" }}
            {{ "get_typing_anim('cat skills.txt')[3]" }}
        </text>
    </g>

    <!-- Skills Output -->
    <text x="0" y="325" class="text cyan" opacity="0">=== TECH STACK ==={get_anim()}</text>
    <text x="0" y="350" class="text" opacity="0"><tspan class="blue">BACKEND</tspan>     Python, FastAPI, SQLAlchemy{get_anim()}</text>
    <text x="0" y="375" class="text" opacity="0"><tspan class="blue">DATABASE</tspan>    PostgreSQL, PostGIS, Redis{get_anim()}</text>
    <text x="0" y="400" class="text" opacity="0"><tspan class="blue">CLOUD</tspan>       AWS (S3, EC2, RDS, IAM){get_anim()}</text>
    <text x="0" y="425" class="text" opacity="0"><tspan class="blue">DEVOPS</tspan>      Docker, Git, GitHub Actions{get_anim()}</text>
    <text x="0" y="450" class="text" opacity="0"><tspan class="blue">PROCESSING</tspan>  Celery, BeautifulSoup{get_anim()}</text>
    <text x="0" y="475" class="text cyan" opacity="0">=================={get_anim(0.08)}</text>

    <!-- Outro -->
    <g opacity="0">
        {{ "get_typing_anim('echo Logout...')[0]" }}
        <text x="0" y="525" class="text"><tspan class="prompt">hlcbabuyo@server</tspan> ~&gt; echo Logout...</text>
        <rect x="185" y="507" width="200" height="22" class="bg">
            {{ "get_typing_anim('echo Logout...')[1]" }}
        </rect>
    </g>
    <text x="0" y="555" class="text green" opacity="0">Session terminated. Thanks for visiting!{get_anim(0.04)}</text>

    <!-- Final Idle Cursor -->
    <g opacity="0">
        <animate attributeName="opacity" values="0;0;1;1;0;0" keyTimes="0;{current_pct};{current_pct+0.001};0.95;0.951;1" dur="{dur}" repeatCount="indefinite" />
        <text x="0" y="595" class="text"><tspan class="prompt">hlcbabuyo@server</tspan> ~&gt; <tspan class="blink">█</tspan></text>
    </g>
  </g>
</svg>"""

# Fix curly brace conflict for Python f-strings
svg_content = svg_content.replace('{{ "get_typing_anim(\'github-stats --user hlcbabuyo\')[0]" }}', get_typing_anim('github-stats --user hlcbabuyo')[0])
svg_content = svg_content.replace('{{ "get_typing_anim(\'github-stats --user hlcbabuyo\')[1]" }}', get_typing_anim('github-stats --user hlcbabuyo', type_speed=0.004)[1])
svg_content = svg_content.replace('{{ "get_typing_anim(\'github-stats --user hlcbabuyo\')[2]" }}', get_typing_anim('github-stats --user hlcbabuyo')[2])
svg_content = svg_content.replace('{{ "get_typing_anim(\'github-stats --user hlcbabuyo\')[3]" }}', get_typing_anim('github-stats --user hlcbabuyo')[3])

svg_content = svg_content.replace('{{ "get_typing_anim(\'cat skills.txt\')[0]" }}', get_typing_anim('cat skills.txt')[0])
svg_content = svg_content.replace('{{ "get_typing_anim(\'cat skills.txt\')[1]" }}', get_typing_anim('cat skills.txt')[1])
svg_content = svg_content.replace('{{ "get_typing_anim(\'cat skills.txt\')[2]" }}', get_typing_anim('cat skills.txt')[2])
svg_content = svg_content.replace('{{ "get_typing_anim(\'cat skills.txt\')[3]" }}', get_typing_anim('cat skills.txt')[3])

svg_content = svg_content.replace('{{ "get_typing_anim(\'echo Logout...\')[0]" }}', get_typing_anim('echo Logout...')[0])
svg_content = svg_content.replace('{{ "get_typing_anim(\'echo Logout...\')[1]" }}', get_typing_anim('echo Logout...')[1])

with open("terminal.svg", "w", encoding="utf-8") as file:
    file.write(svg_content)

print("Retro-Glow Animated SVG generated successfully!")
