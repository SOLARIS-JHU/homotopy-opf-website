"""Generate the Table I case30 comparison, using Python's standard library.

Usage from the repository root: python scripts/generate_results.py
Input: data/case30.json; output: assets/case30-residuals.svg.
The SVG depicts the reported mean-equality metric and one standard deviation
across 100 test instances. It does not depict confidence intervals, training
curves, or repeated-seed uncertainty. No values are estimated or fitted.
"""
from pathlib import Path
from decimal import Decimal
from html import escape
import json
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
DATA = json.loads((ROOT / "data" / "case30.json").read_text(encoding="utf-8"))
WIDTH, HEIGHT = 1100, 490
X0, X1, XMAX = 330, 850, Decimal("0.007")
FIRST_Y, ROW_GAP, AXIS_Y = 110, 43, 398


def x(value):
    return X0 + float(Decimal(value) / XMAX) * (X1 - X0)


def text(px, py, value, size=18, fill="#1a1f2b", weight=400, anchor="start"):
    return (f'<text x="{px:g}" y="{py:g}" font-size="{size}" fill="{fill}" '
            f'font-weight="{weight}" text-anchor="{anchor}">{escape(value)}</text>')


def line(xa, ya, xb, yb, color, width=1):
    return (f'<line x1="{xa:.3f}" y1="{ya:.3f}" x2="{xb:.3f}" '
            f'y2="{yb:.3f}" stroke="{color}" stroke-width="{width}"/>')


def render():
    parts = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{WIDTH}" '
             f'height="{HEIGHT}" viewBox="0 0 {WIDTH} {HEIGHT}" '
             'role="img" aria-labelledby="title desc">',
             '<title id="title">Case30: reported mean equality violations</title>',
             '<desc id="desc">Table I, arXiv 2511.11677 version 1. Seven methods '
             'are compared over 100 test instances. Dots show the average of the '
             'reported mean equality-violation metric; bars extend one standard '
             'deviation on either side. Tx-stepping with GPen has average 0.0017 '
             'and standard deviation 0.0009; the original penalty baseline has '
             'average 0.0036 and standard deviation 0.0027. These are empirical '
             'residuals, not feasibility guarantees.</desc>',
             '<rect width="1100" height="490" rx="14" fill="#ffffff"/>',
             '<g font-family="Inter, DejaVu Sans, Arial, sans-serif">',
             text(28, 35, "Case30 | Equality-constraint residuals", 24, "#002d72", 600),
             text(28, 62, "100 test instances; dots = averages, bars = one standard deviation", 16, "#5b6470"),
             text(1065, 85, "Average (std)", 15, "#5b6470", 500, "end")]
    highlight_y = FIRST_Y + 3 * ROW_GAP
    parts.append(f'<rect x="18" y="{highlight_y - 20}" width="1064" height="40" rx="8" fill="#edf4fb"/>')
    for tick in range(8):
        tick_value = Decimal(tick) / 1000
        xp = x(tick_value)
        parts.append(line(xp, 90, xp, AXIS_Y, "#dfe3ea"))
        label = "0" if tick == 0 else f"{tick_value:.3f}"
        parts.append(text(xp, AXIS_Y + 24, label, 15, "#5b6470", anchor="middle"))
    for i, row in enumerate(DATA["rows"]):
        yp = FIRST_Y + ROW_GAP * i
        baseline = row["method"] == "Original penalty"
        selected = row["method"] == "Tx-stepping, GPen"
        color = "#697482" if baseline else "#001b45" if selected else "#285b91"
        weight = 600 if selected else 400
        mean, std = Decimal(row["mean_eq"]["mean"]), Decimal(row["mean_eq"]["std"])
        left, center, right = x(mean - std), x(mean), x(mean + std)
        parts.extend([
            text(28, yp + 6, row["method"], 18, color, weight),
            line(left, yp, right, yp, color, 2.4),
            line(left, yp - 6, left, yp + 6, color, 2.4),
            line(right, yp - 6, right, yp + 6, color, 2.4),
            f'<circle cx="{center:.3f}" cy="{yp}" r="6" fill="{color}"/>',
            text(1065, yp + 6, f'{row["mean_eq"]["mean"]} ({row["mean_eq"]["std"]})', 18, color, weight, "end")
        ])
    parts.extend([
        line(X0, AXIS_Y, X1, AXIS_Y, "#8a96a5"),
        text((X0 + X1) / 2, 451, "Reported mean equality violation", 18, "#1a1f2b", 500, "middle"),
        text(28, 478, "Source: Table I. Residual units are unspecified; bars are not confidence intervals.", 14, "#5b6470"),
        '</g></svg>'
    ])
    svg = "\n".join(parts) + "\n"
    ET.fromstring(svg)
    destination = ROOT / "assets" / "case30-residuals.svg"
    destination.parent.mkdir(parents=True, exist_ok=True)
    destination.write_text(svg, encoding="utf-8")
    print(destination)


if __name__ == "__main__":
    render()
