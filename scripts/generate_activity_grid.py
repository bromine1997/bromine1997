"""Generate assets/activity-grid.svg: a PCB-styled GitHub contribution grid.

Fetches real contribution data from a public, auth-free API and renders it as
a grid of via-style pads (brightness = contribution intensity) with an
animated current pulse running along a bus trace beneath it, matching the
circuit-board visual language used across this README's other assets.
"""

import json
import sys
import urllib.request
from datetime import date

USERNAME = "bromine1997"
API_URL = f"https://github-contributions-api.jogruber.de/v4/{USERNAME}?y=last"
OUT_PATH = "assets/activity-grid.svg"

VIEW_W = 880
LEFT = 40
RIGHT_MARGIN = 40
TOP_GRID = 46
ROWS = 7
BUS_GAP = 16
CAPTION_GAP = 26

LEVEL_COLORS = {
    0: "#161b22",
    1: "#16303a",
    2: "#1c4b5c",
    3: "#2f9dbd",
    4: "#58e6ff",
}
LEVEL_STROKE = {
    0: "#2a3644",
    1: "#204152",
    2: "#2a6d84",
    3: "#4cc2e0",
    4: "#58e6ff",
}

MONTH_ABBR = ["Jan", "Feb", "Mar", "Apr", "May", "Jun",
              "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]


def fetch_contributions():
    with urllib.request.urlopen(API_URL, timeout=20) as resp:
        payload = json.load(resp)
    days = payload["contributions"]
    total = payload["total"].get("lastYear", sum(d["count"] for d in days))
    return days, total


def build_grid(days):
    first_date = date.fromisoformat(days[0]["date"])
    sun0_weekday = (first_date.weekday() + 1) % 7  # Sunday=0 .. Saturday=6
    cols = -(-(sun0_weekday + len(days)) // ROWS)  # ceil div

    cells = []  # (col, row, level, date_str, count)
    month_labels = []  # (col, label)
    last_month = None
    for i, d in enumerate(days):
        idx = i + sun0_weekday
        col, row = idx // ROWS, idx % ROWS
        cells.append((col, row, d["level"], d["date"], d["count"]))
        dt = date.fromisoformat(d["date"])
        if dt.day <= 7 and dt.month != last_month:
            month_labels.append((col, MONTH_ABBR[dt.month - 1]))
            last_month = dt.month
    return cells, cols, month_labels


def render_svg(cells, cols, month_labels, total):
    avail = VIEW_W - LEFT - RIGHT_MARGIN
    pitch = avail / cols
    size = pitch * 0.72
    radius = min(2.2, size * 0.3)

    grid_h = ROWS * pitch
    bus_y = TOP_GRID + grid_h + BUS_GAP
    caption_y = bus_y + CAPTION_GAP
    view_h = caption_y + 14

    bus_x0 = LEFT
    bus_x1 = LEFT + cols * pitch - (pitch - size)

    parts = []
    parts.append(
        f'<svg viewBox="0 0 {VIEW_W} {view_h:.1f}" width="{VIEW_W}" '
        f'height="{view_h:.1f}" xmlns="http://www.w3.org/2000/svg" role="img" '
        f'aria-label="GitHub contribution activity grid — {total} contributions in the last year">'
    )
    parts.append(f'''
  <defs>
    <pattern id="dotsGrid" width="22" height="22" patternUnits="userSpaceOnUse">
      <circle cx="2" cy="2" r="1" fill="#1b232e"/>
    </pattern>
    <filter id="padGlow" x="-120%" y="-120%" width="340%" height="340%">
      <feGaussianBlur stdDeviation="1.6" result="b"/>
      <feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge>
    </filter>
    <path id="actBus" d="M{bus_x0:.1f} {bus_y:.1f} L{bus_x1:.1f} {bus_y:.1f}"/>
    <path id="actBusR" d="M{bus_x1:.1f} {bus_y:.1f} L{bus_x0:.1f} {bus_y:.1f}"/>
  </defs>
  <style>
    .silks {{ font-family:'Cascadia Code','JetBrains Mono',Consolas,'Malgun Gothic',monospace; }}
    .trace {{ fill:none; stroke:#5a4426; stroke-width:2; stroke-linecap:round; }}
    .p  {{ fill:none; stroke-width:2.2; stroke-linecap:round; stroke-dasharray:26 1000; stroke-dashoffset:1026; animation:flow linear infinite; }}
    .pg {{ stroke-width:7; opacity:.2; }}
    @keyframes flow {{ to {{ stroke-dashoffset:0; }} }}
    .amber {{ stroke:#ffc861; }} .cyan {{ stroke:#58e6ff; }}
    @media (prefers-reduced-motion: reduce){{ *{{ animation:none !important; }} }}
  </style>

  <rect x="1" y="1" width="{VIEW_W - 2}" height="{view_h - 2:.1f}" rx="14" fill="#0d1117" stroke="#30363d" stroke-width="2"/>
  <rect x="1" y="1" width="{VIEW_W - 2}" height="{view_h - 2:.1f}" rx="14" fill="url(#dotsGrid)"/>

  <g stroke="#2a3644" stroke-width="1.5" fill="none">
    <circle cx="24" cy="24" r="6"/><path d="M24 15v18M15 24h18"/>
    <circle cx="{VIEW_W - 24}" cy="24" r="6"/><path d="M{VIEW_W - 24} 15v18M{VIEW_W - 33} 24h18"/>
    <circle cx="24" cy="{view_h - 24:.1f}" r="6"/><path d="M24 {view_h - 33:.1f}v18M15 {view_h - 24:.1f}h18"/>
    <circle cx="{VIEW_W - 24}" cy="{view_h - 24:.1f}" r="6"/><path d="M{VIEW_W - 24} {view_h - 33:.1f}v18M{VIEW_W - 33} {view_h - 24:.1f}h18"/>
  </g>

  <text x="{LEFT}" y="26" class="silks" font-size="10" fill="#4d5966" letter-spacing="2">── ACTIVITY GRID // 365D ─────────</text>
''')

    # month labels
    for col, label in month_labels:
        x = LEFT + col * pitch
        parts.append(f'  <text x="{x:.1f}" y="{TOP_GRID - 8:.1f}" class="silks" font-size="8" fill="#4d5966">{label}</text>\n')

    # pads
    parts.append('  <g>\n')
    for col, row, level, dstr, count in cells:
        x = LEFT + col * pitch
        y = TOP_GRID + row * pitch
        fill = LEVEL_COLORS[level]
        stroke = LEVEL_STROKE[level]
        glow = ' filter="url(#padGlow)"' if level == 4 else ''
        parts.append(
            f'    <rect x="{x:.2f}" y="{y:.2f}" width="{size:.2f}" height="{size:.2f}" '
            f'rx="{radius:.2f}" fill="{fill}" stroke="{stroke}" stroke-width="1"{glow}>'
            f'<title>{dstr} · {count} contribution{"s" if count != 1 else ""}</title></rect>\n'
        )
    parts.append('  </g>\n')

    # legend (LOW -> HIGH), top-right of grid
    lx0 = VIEW_W - RIGHT_MARGIN - 5 * 12 - 34
    parts.append(f'  <text x="{lx0 - 6:.1f}" y="26" text-anchor="end" class="silks" font-size="8" fill="#4d5966">LOW</text>\n')
    for i in range(5):
        parts.append(
            f'  <rect x="{lx0 + i * 12:.1f}" y="19" width="8" height="8" rx="1.5" '
            f'fill="{LEVEL_COLORS[min(i,4)]}" stroke="{LEVEL_STROKE[min(i,4)]}" stroke-width="0.8"/>\n'
        )
    parts.append(f'  <text x="{lx0 + 5 * 12 + 6:.1f}" y="26" class="silks" font-size="8" fill="#4d5966">HIGH</text>\n')

    # bus (current flowing beneath the grid)
    parts.append(f'''
  <use href="#actBus" class="trace"/>
  <use href="#actBus" class="p pg amber"/><use href="#actBus" class="p amber"/>
  <use href="#actBusR" class="p pg cyan" style="animation-duration:4.6s"/><use href="#actBusR" class="p cyan" style="animation-duration:4.6s"/>
  <g fill="#0d1117" stroke="#b58b3c" stroke-width="2">
    <circle cx="{bus_x0:.1f}" cy="{bus_y:.1f}" r="4"/><circle cx="{bus_x1:.1f}" cy="{bus_y:.1f}" r="4"/>
  </g>
''')

    parts.append(
        f'  <text x="{LEFT}" y="{caption_y:.1f}" class="silks" font-size="8.5" fill="#4d5966" letter-spacing="1">'
        f'{total} CONTRIBUTIONS · LAST 365 DAYS · CURRENT FLOWING · AUTO-SYNCED DAILY</text>\n'
    )

    parts.append('</svg>\n')
    return "".join(parts)


def main():
    try:
        days, total = fetch_contributions()
    except Exception as exc:  # network/API failure — fail loudly, keep prior file
        print(f"failed to fetch contributions: {exc}", file=sys.stderr)
        sys.exit(1)

    cells, cols, month_labels = build_grid(days)
    svg = render_svg(cells, cols, month_labels, total)

    with open(OUT_PATH, "w", encoding="utf-8", newline="\n") as f:
        f.write(svg)
    print(f"wrote {OUT_PATH} ({cols} cols, {total} contributions)")


if __name__ == "__main__":
    main()
