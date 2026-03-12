import urllib.request
import json

def fetch_github_stats(username):
    try:
        url = f"https://api.github.com/users/{username}"
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req) as response:
            data = json.loads(response.read().decode())
            return {
                'repos': data.get('public_repos', 'N/A'),
                'followers': data.get('followers', 'N/A'),
            }
    except Exception as e:
        print(f"Could not fetch GitHub stats: {e}")
        return {'repos': 'N/A', 'followers': 'N/A'}


DUR = "32s"


def char_by_char(cmd_text, start_pct, char_delay=0.002):
    spans = []
    t = start_pct
    for ch in cmd_text:
        safe = ch.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')
        anim = (f'<animate attributeName="opacity" values="0;0;1;1;0;0" '
                f'keyTimes="0;{round(t,4)};{round(t+0.0001,4)};0.95;0.951;1" '
                f'dur="{DUR}" repeatCount="indefinite"/>')
        spans.append(f'<tspan opacity="0">{safe}{anim}</tspan>')
        t += char_delay
    return spans, round(t, 4)


def cmd_line(y, cmd_text, start_pct, char_delay=0.002):
    spans, end_pct = char_by_char(cmd_text, start_pct, char_delay)
    prompt_anim = (f'<animate attributeName="opacity" values="0;0;1;1;0;0" '
                   f'keyTimes="0;{round(start_pct,4)};{round(start_pct+0.0001,4)};0.95;0.951;1" '
                   f'dur="{DUR}" repeatCount="indefinite"/>')
    svg = (f'    <text x="0" y="{y}" class="text" opacity="0">'
           f'<tspan class="prompt">hlcbabuyo@github ~&gt;</tspan>'
           f'{"".join(spans)}'
           f'{prompt_anim}</text>')
    return svg, end_pct


def line_svg(content, start_pct):
    s = round(start_pct, 4)
    anim = (f'<animate attributeName="opacity" values="0;0;1;1;0;0" '
            f'keyTimes="0;{s};{round(s+0.001,4)};0.95;0.951;1" '
            f'dur="{DUR}" repeatCount="indefinite"/>')
    return f'{content}{anim}', round(s + 0.02, 4)


def generate(username="hlcbabuyo", output="terminal.svg"):
    stats = fetch_github_stats(username)
    repos = stats['repos']
    followers = stats['followers']

    # ── Chain all timing ──────────────────────────────────────────────────────
    t = 0.02
    boot1_anim = f'<animate attributeName="opacity" values="0;0;1;1;0;0" keyTimes="0;{t};{t+0.001};0.95;0.951;1" dur="{DUR}" repeatCount="indefinite"/>'
    t = 0.05
    boot2_anim = f'<animate attributeName="opacity" values="0;0;1;1;0;0" keyTimes="0;{t};{t+0.001};0.95;0.951;1" dur="{DUR}" repeatCount="indefinite"/>'
    t = 0.09

    cmd1_svg, t = cmd_line(60,  " github-stats --user hlcbabuyo", t, 0.002)
    t += 0.015
    s0, t = line_svg('<tspan class="cyan">=== GitHub Stats for hlcbabuyo ===</tspan>', t)
    s1, t = line_svg(f'<tspan class="orange">Name:</tspan>        Harvie Lorenz C. Babuyo', t)
    s2, t = line_svg(f'<tspan class="orange">Role:</tspan>        Backend Systems Engineer', t)
    s3, t = line_svg(f'<tspan class="orange">Location:</tspan>    Tagoloan, Misamis Oriental, Philippines', t)
    s4, t = line_svg(f'<tspan class="orange">Goal:</tspan>        240-Hour OJT (June 2026)', t)
    s5, t = line_svg(f'<tspan class="orange">Repos:</tspan>       {repos}', t)
    s6, t = line_svg(f'<tspan class="orange">Followers:</tspan>   {followers}', t)
    s7, t = line_svg('<tspan class="cyan">==================================</tspan>', t)
    t += 0.025

    cmd2_svg, t = cmd_line(280, " cat skills.txt", t, 0.002)
    t += 0.015
    k0, t = line_svg('<tspan class="cyan">=== Tech Stack ===</tspan>', t)
    k1, t = line_svg('<tspan class="blue">Backend:</tspan>     Python, FastAPI, SQLAlchemy, Pydantic', t)
    k2, t = line_svg('<tspan class="blue">Database:</tspan>    PostgreSQL, PostGIS, Redis', t)
    k3, t = line_svg('<tspan class="blue">Cloud:</tspan>       AWS (S3, EC2, RDS, IAM)', t)
    k4, t = line_svg('<tspan class="blue">DevOps:</tspan>      Docker, Git, GitHub Actions', t)
    k5, t = line_svg('<tspan class="blue">Processing:</tspan>  Celery, BeautifulSoup', t)
    k6, t = line_svg('<tspan class="blue">Tools:</tspan>       ReportLab, QRCode, boto3, Postman', t)
    k7, t = line_svg('<tspan class="blue">Languages:</tspan>   Python, SQL', t)
    k8, t = line_svg('<tspan class="cyan">==================</tspan>', t)
    t += 0.025

    cmd3_svg, t = cmd_line(520, " echo 'Thanks for visiting my profile!'", t, 0.002)
    t += 0.015
    o1, t = line_svg('<tspan class="green">Thanks for visiting my profile!</tspan>', t)
    t += 0.025
    cursor_t = round(t, 4)

    print(f"Total time used: {cursor_t} / 0.95  ({'OK' if cursor_t < 0.95 else 'OVERFLOW'})")

    svg = f"""<svg width="100%" height="630" viewBox="0 0 800 630" preserveAspectRatio="xMidYMid meet" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <filter id="glow" x="-20%" y="-20%" width="140%" height="140%">
      <feGaussianBlur stdDeviation="2.5" result="blur" />
      <feComposite in="SourceGraphic" in2="blur" operator="over" />
    </filter>
  </defs>
  <style>
    .bg {{ fill: #0A0A0A; }}
    .text {{ font-family: Consolas, 'Courier New', monospace; font-size: 14px; fill: #CCCCCC; filter: url(#glow); }}
    .prompt {{ fill: #E06C75; }}
    .cyan {{ fill: #56B6C2; }}
    .green {{ fill: #98C379; }}
    .orange {{ fill: #D19A66; }}
    .blue {{ fill: #61AFEF; }}
  </style>

  <rect width="100%" height="100%" class="bg"/>
  <g transform="translate(20, 30)">

    <text x="0" y="0"   class="text" opacity="0">Initializing terminal...{boot1_anim}</text>
    <text x="0" y="20"  class="text" opacity="0"><tspan class="green">[OK]</tspan> System ready{boot2_anim}</text>

    {cmd1_svg}
    <text x="0" y="100" class="text" opacity="0">{s0}</text>
    <text x="0" y="120" class="text" opacity="0">{s1}</text>
    <text x="0" y="140" class="text" opacity="0">{s2}</text>
    <text x="0" y="160" class="text" opacity="0">{s3}</text>
    <text x="0" y="180" class="text" opacity="0">{s4}</text>
    <text x="0" y="200" class="text" opacity="0">{s5}</text>
    <text x="0" y="220" class="text" opacity="0">{s6}</text>
    <text x="0" y="240" class="text" opacity="0">{s7}</text>

    {cmd2_svg}
    <text x="0" y="320" class="text" opacity="0">{k0}</text>
    <text x="0" y="340" class="text" opacity="0">{k1}</text>
    <text x="0" y="360" class="text" opacity="0">{k2}</text>
    <text x="0" y="380" class="text" opacity="0">{k3}</text>
    <text x="0" y="400" class="text" opacity="0">{k4}</text>
    <text x="0" y="420" class="text" opacity="0">{k5}</text>
    <text x="0" y="440" class="text" opacity="0">{k6}</text>
    <text x="0" y="460" class="text" opacity="0">{k7}</text>
    <text x="0" y="480" class="text" opacity="0">{k8}</text>

    {cmd3_svg}
    <text x="0" y="540" class="text" opacity="0">{o1}</text>

    <text x="0" y="580" class="text" opacity="0">
      <tspan class="prompt">hlcbabuyo@github ~&gt;</tspan> <tspan fill="#CCCCCC"><animate attributeName="opacity" values="1;0" keyTimes="0;0.5" dur="1s" repeatCount="indefinite"/>█</tspan>
      <animate attributeName="opacity" values="0;0;1;1;0;0" keyTimes="0;{cursor_t};{cursor_t+0.001};0.95;0.951;1" dur="{DUR}" repeatCount="indefinite"/>
    </text>

  </g>
</svg>"""

    with open(output, "w", encoding="utf-8") as f:
        f.write(svg)
    print(f"Generated: {output}  (repos={repos}, followers={followers})")


if __name__ == "__main__":
    generate()
