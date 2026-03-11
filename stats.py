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

# Format variables to align perfectly
repos_str = str(repos).ljust(4)
followers_str = str(followers).ljust(4)

# 2. Build the SVG (Scalable Vector Graphic)
svg_content = f"""<svg width="850" height="460" viewBox="0 0 850 460" xmlns="http://www.w3.org/2000/svg">
  <style>
    .bg {{ fill: #0D1117; }}
    .text {{ font-family: 'Courier New', Consolas, monospace; font-size: 15px; }}
    .title {{ font-weight: bold; fill: #E6EDF3; }}
    .green {{ fill: #39D353; }}
    .blue {{ fill: #58A6FF; }}
    .yellow {{ fill: #D2A8FF; }}
    .cyan {{ fill: #388BFD; }}
    .purple {{ fill: #BC8CFF; }}
    .red {{ fill: #FF7B72; }}
    .white {{ fill: #C9D1D9; }}
    .gray {{ fill: #8B949E; }}
    .accent {{ fill: #F2CC60; }}
    
    /* The CSS Blinking Cursor Animation! */
    .blink {{ animation: blinker 1s linear infinite; }}
    @keyframes blinker {{ 50% {{ opacity: 0; }} }}
  </style>

  <!-- Terminal Window Background -->
  <rect width="100%" height="100%" rx="10" ry="10" class="bg" stroke="#30363D" stroke-width="2"/>

  <!-- macOS Window Buttons -->
  <circle cx="20" cy="20" r="6" fill="#FF5F56"/>
  <circle cx="40" cy="20" r="6" fill="#FFBD2E"/>
  <circle cx="60" cy="20" r="6" fill="#27C93F"/>

  <!-- Terminal Title -->
  <text x="425" y="24" class="text gray" text-anchor="middle" font-size="13px">hlcbabuyo — bash</text>

  <g transform="translate(30, 70)">
    <!-- ASCII Computer on the Left -->
    <text x="0" y="0" class="text cyan" xml:space="preserve">.-------------------------------.</text>
    <text x="0" y="20" class="text cyan" xml:space="preserve">|  <tspan class="green">&gt;_ hlcbabuyo@server</tspan>          |</text>
    <text x="0" y="40" class="text cyan" xml:space="preserve">|                               |</text>
    <text x="0" y="60" class="text cyan" xml:space="preserve">|  <tspan class="accent">Repos:</tspan>     <tspan class="white">{repos_str}</tspan>             |</text>
    <text x="0" y="80" class="text cyan" xml:space="preserve">|  <tspan class="purple">Followers:</tspan> <tspan class="white">{followers_str}</tspan>             |</text>
    <text x="0" y="100" class="text cyan" xml:space="preserve">|                               |</text>
    <text x="0" y="120" class="text cyan" xml:space="preserve">'-------------------------------'</text>
    <text x="0" y="140" class="text cyan" xml:space="preserve">     _[___________________]_</text>
    <text x="0" y="160" class="text cyan" xml:space="preserve">     \                     /</text>
    <text x="0" y="180" class="text cyan" xml:space="preserve">      \___________________/</text>

    <!-- Identity Section on the Right -->
    <text x="360" y="0" class="text title" xml:space="preserve">=== Harvie Lorenz C. Babuyo ===</text>
    <text x="360" y="25" class="text gray" xml:space="preserve">Role:      <tspan class="white">Backend Systems Engineer</tspan></text>
    <text x="360" y="45" class="text gray" xml:space="preserve">Location:  <tspan class="white">Tagoloan, Philippines</tspan></text>
    <text x="360" y="65" class="text gray" xml:space="preserve">Goal:      <tspan class="white">240-Hour OJT (June 2026)</tspan></text>

    <!-- Tech Stack Section on the Right -->
    <text x="360" y="110" class="text title" xml:space="preserve">=== Tech Stack ===</text>
    <text x="360" y="135" class="text gray" xml:space="preserve">Backend:     <tspan class="green">Python, FastAPI, SQLAlchemy, Pydantic</tspan></text>
    <text x="360" y="155" class="text gray" xml:space="preserve">Database:    <tspan class="purple">PostgreSQL, PostGIS, Redis</tspan></text>
    <text x="360" y="175" class="text gray" xml:space="preserve">Cloud:       <tspan class="accent">AWS (S3, EC2, RDS, IAM)</tspan></text>
    <text x="360" y="195" class="text gray" xml:space="preserve">DevOps:      <tspan class="red">Docker, Git, GitHub Actions</tspan></text>
    <text x="360" y="215" class="text gray" xml:space="preserve">Processing:  <tspan class="cyan">Celery, BeautifulSoup</tspan></text>
    <text x="360" y="235" class="text gray" xml:space="preserve">Tools:       <tspan class="blue">ReportLab, QRCode, boto3, Postman</tspan></text>
    <text x="360" y="255" class="text gray" xml:space="preserve">Languages:   <tspan class="accent">Python, SQL</tspan></text>

    <!-- Bottom Command with Blinking Cursor -->
    <text x="0" y="340" class="text green" xml:space="preserve">&gt;_ System ready. Type 'help' for commands. <tspan class="white blink">█</tspan></text>
  </g>
</svg>"""

with open("terminal.svg", "w", encoding="utf-8") as file:
    file.write(svg_content)

print("Pixel-perfect SVG generated successfully!")
