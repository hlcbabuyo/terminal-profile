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

# 2. Timing system
LOOP = 20.0
FADE_OUT = 19.0

def pct(t):
    return round(t / LOOP, 4)

def type_dur(text, cps=55):
    return max(0.3, len(text) / cps)

# 3. Line builder with typing effect (clipPath reveal)
uid_counter = [0]
defs_list = []
elements_list = []

def add_line(x, y, parts, t_start, cps=70, glow=False):
    """
    parts = list of (text, color_hex_or_css_class)
    Returns t_end so you can chain calls.
    """
    full_text = "".join(p[0] for p in parts)
    dur = type_dur(full_text, cps)
    t_end = t_start + dur

    uid_counter[0] += 1
    uid = uid_counter[0]
    clip_id = f"c{uid}"

    p0     = pct(0)
    p_s    = pct(t_start)
    p_e    = pct(t_end)
    p_fo   = pct(FADE_OUT)
    p1     = pct(LOOP)

    char_w = 8.6
    full_w = len(full_text) * char_w + 20

    # clipPath def
    defs_list.append(f"""
    <clipPath id="{clip_id}">
      <rect x="{x}" y="{y - 16}" height="22" width="0">
        <animate attributeName="width"
          values="0;0;{full_w}"
          keyTimes="{p0};{p_s};{p_e}"
          dur="{LOOP}s" repeatCount="indefinite" calcMode="linear"/>
      </rect>
    </clipPath>""")

    # build tspans
    tspans = ""
    for txt, cls in parts:
        safe = txt.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;').replace('"', '&quot;')
        if cls.startswith("#"):
            tspans += f'<tspan fill="{cls}">{safe}</tspan>'
        else:
            tspans += f'<tspan class="{cls}">{safe}</tspan>'

    filter_str = 'filter="url(#glow)"' if glow else ""

    elements_list.append(f"""
  <g opacity="0">
    <animate attributeName="opacity"
      values="0;0;1;1;0;0"
      keyTimes="{p0};{p_s};{p_s + 0.0005};{p_fo};{p_fo + 0.001};{p1}"
      dur="{LOOP}s" repeatCount="indefinite"/>
    <text x="{x}" y="{y}" class="text" clip-path="url(#{clip_id})" {filter_str}>{tspans}</text>
  </g>""")

    return t_end

# ── Define all lines ──────────────────────────────────────────
X = 24
t = 0.1

# Boot
t = add_line(X, 48,  [("Initializing terminal...", "#4A4A4A")], t, cps=80)
t = add_line(X, 68,  [("[  OK  ] ", "green"), ("Session started · ", "#555"), ("hlcbabuyo", "cyan")], t + 0.1, cps=80)
t = add_line(X, 88,  [("─" * 60, "#2A2A2A")], t + 0.05, cps=300)

t += 0.35

# Command 1
t = add_line(X, 126, [
    ("hlcbabuyo", "prompt"), ("@github", "prompt"),
    (":", "#333"), ("~", "blue"), ("$ ", "#555"),
    ("github-stats --user hlcbabuyo", "#CCCCCC")
], t, cps=42)

t += 0.25

# Stats
t = add_line(X, 162, [("=== GitHub Stats for hlcbabuyo ===", "cyan")], t, cps=90, glow=True)
t = add_line(X, 182, [("  Name      ", "orange"), (f"Harvie Lorenz C. Babuyo", "#CCCCCC")], t + 0.04, cps=90)
t = add_line(X, 202, [("  Role      ", "orange"), ("Backend Systems Engineer", "#CCCCCC")], t + 0.04, cps=90)
t = add_line(X, 222, [("  Location  ", "orange"), ("Tagoloan, Misamis Oriental, PH", "#CCCCCC")], t + 0.04, cps=90)
t = add_line(X, 242, [("  Goal      ", "orange"), ("240-Hour OJT  (June 2026)", "#CCCCCC")], t + 0.04, cps=90)
t = add_line(X, 262, [("  Repos     ", "orange"), (str(repos), "green")], t + 0.04, cps=90)
t = add_line(X, 282, [("  Followers ", "orange"), (str(followers), "green")], t + 0.04, cps=90)
t = add_line(X, 302, [("=" * 34, "cyan")], t + 0.08, cps=300, glow=True)

t += 0.4

# Command 2
t = add_line(X, 340, [
    ("hlcbabuyo", "prompt"), ("@github", "prompt"),
    (":", "#333"), ("~", "blue"), ("$ ", "#555"),
    ("cat skills.txt", "#CCCCCC")
], t, cps=42)

t += 0.25

# Skills
t = add_line(X, 376, [("=== Tech Stack ===", "cyan")], t, cps=90, glow=True)
t = add_line(X, 396, [("  Backend   ", "blue"), ("Python · FastAPI · SQLAlchemy · Pydantic", "#CCCCCC")], t + 0.04, cps=90)
t = add_line(X, 416, [("  Database  ", "blue"), ("PostgreSQL · PostGIS · Redis", "#CCCCCC")], t + 0.04, cps=90)
t = add_line(X, 436, [("  Cloud     ", "blue"), ("AWS  S3 · EC2 · RDS · IAM", "#CCCCCC")], t + 0.04, cps=90)
t = add_line(X, 456, [("  DevOps    ", "blue"), ("Docker · Git · GitHub Actions", "#CCCCCC")], t + 0.04, cps=90)
t = add_line(X, 476, [("  Tools     ", "blue"), ("Celery · ReportLab · QRCode · boto3", "#CCCCCC")], t + 0.04, cps=90)
t = add_line(X, 496, [("  Languages ", "blue"), ("Python · SQL", "#CCCCCC")], t + 0.04, cps=90)
t = add_line(X, 516, [("=" * 18, "cyan")], t + 0.08, cps=300, glow=True)

t += 0.4

# Command 3
t = add_line(X, 554, [
    ("hlcbabuyo", "prompt"), ("@github", "prompt"),
    (":", "#333"), ("~", "blue"), ("$ ", "#555"),
    ('echo "Thanks for visiting my profile!"', "#CCCCCC")
], t, cps=42)
t = add_line(X, 574, [("Thanks for visiting my profile!", "green")], t + 0.1, cps=80, glow=True)

t += 0.3

# Final blinking cursor
p_s  = pct(t)
p_fo = pct(FADE_OUT)
p1   = pct(LOOP)
final_cursor = f"""
  <g opacity="0">
    <animate attributeName="opacity"
      values="0;0;1;1;0;0"
      keyTimes="0;{p_s};{p_s + 0.0005};{p_fo};{p_fo + 0.001};{p1}"
      dur="{LOOP}s" repeatCount="indefinite"/>
    <text x="{X}" y="612" class="text">
      <tspan class="prompt">hlcbabuyo</tspan><tspan class="prompt">@github</tspan><tspan fill="#333">:</tspan><tspan class="blue">~</tspan><tspan fill="#555">$ </tspan><tspan fill="#4EC9D4"><animate attributeName="opacity" values="1;0;1" keyTimes="0;0.5;1" dur="1.1s" repeatCount="indefinite"/>█</tspan>
    </text>
  </g>"""

# ── Assemble SVG ─────────────────────────────────────────────
all_defs  = "\n".join(defs_list)
all_elems = "\n".join(elements_list)

svg_content = f"""<svg width="800" height="640" viewBox="0 0 800 640" xmlns="http://www.w3.org/2000/svg">
  <defs>
    {all_defs}

    <!-- Scanline pattern -->
    <pattern id="scanlines" width="800" height="3" patternUnits="userSpaceOnUse">
      <rect width="800" height="1" y="2" fill="rgba(0,0,0,0.13)"/>
    </pattern>

    <!-- Vignette -->
    <radialGradient id="vignette" cx="50%" cy="50%" r="72%">
      <stop offset="55%" stop-color="transparent"/>
      <stop offset="100%" stop-color="rgba(0,0,0,0.55)"/>
    </radialGradient>

    <!-- Glow filter for headers -->
    <filter id="glow" x="-15%" y="-40%" width="130%" height="180%">
      <feGaussianBlur stdDeviation="2.2" result="blur"/>
      <feMerge>
        <feMergeNode in="blur"/>
        <feMergeNode in="SourceGraphic"/>
      </feMerge>
    </filter>
  </defs>

  <style>
    .text   {{ font-family: 'Cascadia Code', 'Fira Code', Consolas, 'Courier New', monospace; font-size: 14px; fill: #CCCCCC; }}
    .prompt {{ fill: #E06C75; }}
    .cyan   {{ fill: #4EC9D4; }}
    .green  {{ fill: #89D185; }}
    .orange {{ fill: #CE9178; }}
    .blue   {{ fill: #569CD6; }}
  </style>

  <!-- Background -->
  <rect width="800" height="640" fill="#0D0D0D"/>

  <!-- Terminal lines -->
  {all_elems}
  {final_cursor}

  <!-- CRT scanlines overlay -->
  <rect width="800" height="640" fill="url(#scanlines)" opacity="0.35" pointer-events="none"/>
  <!-- Vignette overlay -->
  <rect width="800" height="640" fill="url(#vignette)" pointer-events="none"/>
</svg>"""

with open("terminal.svg", "w", encoding="utf-8") as f:
    f.write(svg_content)

print(f"Done! ({t:.1f}s of content in a {LOOP}s loop)")
