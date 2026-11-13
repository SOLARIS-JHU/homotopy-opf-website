"""Reproduce explanatory vector assets for the Homotopy OPF project page.

Sources: arXiv:2511.11677v1, Secs. III–IV and Appendix A.
These are conceptual diagrams, not measured optimization trajectories.
Run: python scripts/generate_figures.py
Optional PNG export: python scripts/generate_figures.py --png
PNG rendering requires Inkscape on PATH (or its standard Windows install).
"""
from pathlib import Path
from html import escape
import argparse
import shutil
import subprocess

ROOT = Path(__file__).resolve().parents[1]
ASSETS = ROOT / 'assets'
BLUE = '#002d72'
SKY = '#68ace5'
INK = '#1a1f2b'
MUTED = '#5b6470'
BORDER = '#dfe3ea'
BG = '#fbfbfd'


def text(x, y, value, size=18, fill=INK, weight=400, anchor='start', family='Inter, Arial, sans-serif'):
    value = escape(value)
    for token, base, sub in [('λH', 'λ', 'H'), ('πΘ', 'π', 'Θ'), ('Pd', 'P', 'd'),
                             ('Qd', 'Q', 'd'), ('Pg', 'P', 'g'), ('Qg', 'Q', 'g')]:
        value = value.replace(token, f'{base}<tspan font-size="70%" baseline-shift="sub">{sub}</tspan>')
    return f'<text x="{x}" y="{y}" font-family="{family}" font-size="{size}" font-weight="{weight}" fill="{fill}" text-anchor="{anchor}">{value}</text>'


def rect(x, y, w, h, fill='white', stroke=BORDER, radius=14):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{radius}" fill="{fill}" stroke="{stroke}"/>'


def path(d, color=BLUE, arrow=True, width=2):
    end = ' marker-end="url(#arrow)"' if arrow else ''
    return f'<path d="{d}" fill="none" stroke="{color}" stroke-width="{width}" stroke-linecap="round" stroke-linejoin="round"{end}/>'


def start(width, height, title, desc):
    return [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" width="{width}" height="{height}" role="img" aria-labelledby="title desc">',
            f'<title id="title">{escape(title)}</title><desc id="desc">{escape(desc)}</desc>',
            f'<defs><marker id="arrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M 0 0 L 10 5 L 0 10 z" fill="{BLUE}"/></marker></defs>',
            rect(0.5, 0.5, width-1, height-1, BG)]


def method():
    s = start(1100, 650, 'Homotopy-guided self-supervised learning for AC optimal power flow',
        'Offline training maps sampled load profiles through a neural policy to predicted voltages and generator powers. A homotopy schedule changes the objective and constraint penalties from an easier problem to the original problem. Automatic differentiation updates the neural policy. The generation pull-up penalty stays fixed along the homotopy. At inference, new loads pass through the trained policy with fixed weights to produce approximate decisions; no feasibility guarantee is implied.')
    s += [text(40, 43, 'Learn the solution map, gradually', 30, BLUE, 600, family='Georgia, serif'),
          text(40, 73, 'Homotopy changes the training problem; the neural policy learns across stages.', 18, MUTED),
          rect(24, 96, 1052, 405),
          text(48, 126, 'OFFLINE TRAINING', 14, BLUE, 600),
          rect(48, 146, 1004, 77, '#f0f5fb', '#e3ebf5', 10),
          text(70, 176, 'Easier problem', 17, BLUE, 600),
          text(1030, 176, 'Original problem', 17, BLUE, 600, 'end'),
          path('M 244 170 H 852'),
          text(550, 162, 'λH = 0    →    …    →    1', 19, BLUE, 500, 'middle'),
          text(550, 205, 'Train at fixed λH  ·  carry Θ forward  ·  increase λH', 17, MUTED, 400, 'middle'),
          path('M 976 223 V 259'),
          path('M 138 260 V 244 H 704 V 259', width=1.6),
          text(520, 240, 'ξ', 16, BLUE, 400, 'middle', 'Georgia, serif'),
          rect(48, 260, 180, 116),
          text(138, 290, 'Load profiles', 18, INK, 600, 'middle'),
          text(138, 325, 'ξ = (Pd, Qd)', 24, BLUE, 500, 'middle', 'Georgia, serif'),
          text(138, 355, 'sampled conditions', 15, MUTED, 400, 'middle'),
          path('M 228 318 H 256'),
          rect(258, 260, 190, 116, '#f0f5fb', '#c5d7ec'),
          text(353, 290, 'Neural policy', 18, INK, 600, 'middle'),
          text(353, 330, 'πΘ(ξ)', 30, BLUE, 500, 'middle', 'Georgia, serif'),
          text(353, 355, 'trainable weights Θ', 15, MUTED, 400, 'middle'),
          path('M 448 318 H 476'),
          rect(478, 260, 160, 116),
          text(558, 290, 'Predictions', 18, INK, 600, 'middle'),
          text(558, 330, 'V, Pg, Qg', 26, BLUE, 500, 'middle', 'Georgia, serif'),
          text(558, 355, 'decision variables', 15, MUTED, 400, 'middle'),
          path('M 638 318 H 666'),
          rect(668, 260, 384, 116, '#f0f5fb', '#c5d7ec'),
          text(860, 290, 'Homotopy training loss', 18, INK, 600, 'middle'),
          text(860, 320, 'objective + equality / inequality penalties', 16, BLUE, 500, 'middle'),
          text(860, 350, '+ Pg pull-up penalty (unchanged)', 16, MUTED, 400, 'middle'),
          path('M 860 376 V 448 H 353 V 378'),
          text(606, 429, 'Automatic differentiation · update Θ', 18, BLUE, 500, 'middle'),
          text(48, 482, 'No optimal-solution labels required. Penalties encourage constraint satisfaction.', 16, MUTED),
          rect(24, 520, 1052, 106, '#f0f5fb', '#dfe7f1'),
          text(48, 548, 'INFERENCE', 14, BLUE, 600),
          text(48, 583, 'New load profile', 18, INK, 500),
          path('M 210 577 H 291'),
          text(315, 583, 'Trained policy · fixed Θ', 18, BLUE, 600),
          path('M 560 577 H 651'),
          text(677, 579, 'Approximate AC-OPF decisions', 18, INK, 600),
          text(677, 604, 'Original operating problem · λH = 1', 15, MUTED),
          '</svg>']
    return '\n'.join(s)


def social():
    s = start(1200, 630, 'Homotopy-guided self-supervised AC optimal power flow',
              'Research project preview. A progression from easier training problems to the original AC optimal power flow problem guides a self-supervised neural solution map.')
    s += [rect(0,0,1200,10,BLUE,BLUE,0),
          text(64, 69, 'SOLARIS  /  PESGM 2026', 20, BLUE, 600),
          text(64, 146, 'Homotopy-Guided', 49, BLUE, 600, family='Georgia, serif'),
          text(64, 206, 'Self-Supervised Learning', 49, BLUE, 600, family='Georgia, serif'),
          text(64, 266, 'for AC Optimal Power Flow', 49, BLUE, 600, family='Georgia, serif'),
          text(64, 318, 'Learning parametric solutions through easier training problems', 24, MUTED),
          rect(64, 376, 280, 128, 'white'),
          text(204, 421, 'Easier problem', 24, BLUE, 600, 'middle'),
          text(204, 464, 'λH = 0', 30, BLUE, 400, 'middle', 'Georgia, serif'),
          path('M 344 440 H 438', width=3),
          rect(450, 376, 300, 128, '#eff5fc', '#c5d7ec'),
          text(600, 421, 'Warm-start training', 23, BLUE, 600, 'middle'),
          text(600, 464, 'carry Θ forward', 24, MUTED, 400, 'middle'),
          path('M 750 440 H 844', width=3),
          rect(856, 376, 280, 128, 'white'),
          text(996, 421, 'Original AC-OPF', 24, BLUE, 600, 'middle'),
          text(996, 464, 'λH = 1', 30, BLUE, 400, 'middle', 'Georgia, serif'),
          text(64, 568, 'Shimiao Li · Aaron Tuor · Draguna Vrabie · Larry Pileggi · Jan Drgona', 20, MUTED),
          '</svg>']
    return '\n'.join(s)


def method_mobile():
    s = start(480, 1100, 'Homotopy-guided AC optimal power flow: training and inference',
        'Portrait version of the method overview. Sampled load profiles enter a neural policy. Predicted voltages and generator powers enter a homotopy loss that also receives load parameters and the homotopy stage. Automatic differentiation updates policy weights. The generation pull-up penalty is unchanged. The schedule advances from easier to original problems, carrying weights forward. Inference uses fixed weights to predict approximate decisions.')
    s += [text(30, 39, 'Learn the solution map,', 29, BLUE, 600, family='Georgia, serif'),
          text(30, 76, 'gradually', 29, BLUE, 600, family='Georgia, serif'),
          rect(16, 96, 448, 730),
          text(38, 126, 'OFFLINE TRAINING', 17, BLUE, 600),
          rect(38, 145, 404, 105, '#f0f5fb', '#e3ebf5', 10),
          text(58, 174, 'Easier', 21, BLUE, 600),
          text(422, 174, 'Original', 21, BLUE, 600, 'end'),
          path('M 138 168 H 323'),
          text(240, 199, 'λH = 0 → … → 1', 24, BLUE, 500, 'middle', 'Georgia, serif'),
          text(240, 231, 'Train · carry Θ forward · increase λH', 18, MUTED, 400, 'middle'),
          path('M 438 250 V 718 H 402', width=1.6),
          rect(80, 280, 320, 76),
          text(240, 309, 'Sampled load profiles', 21, INK, 600, 'middle'),
          text(240, 340, 'ξ = (Pd, Qd)', 26, BLUE, 500, 'middle', 'Georgia, serif'),
          path('M 240 356 V 392'),
          path('M 400 318 H 438', arrow=False, width=1.6),
          f'<circle cx="438" cy="318" r="3" fill="{BLUE}"/>',
          '<g transform="translate(426 605) rotate(-90)">',
          text(0, 0, 'Problem context: λH, ξ', 18, BLUE, 500),
          '</g>',
          rect(80, 394, 320, 76, '#f0f5fb', '#c5d7ec'),
          text(240, 423, 'Neural policy', 21, INK, 600, 'middle'),
          text(240, 454, 'πΘ(ξ)', 28, BLUE, 500, 'middle', 'Georgia, serif'),
          path('M 240 470 V 506'),
          rect(80, 508, 320, 76),
          text(240, 537, 'Predicted decisions', 21, INK, 600, 'middle'),
          text(240, 568, 'V, Pg, Qg', 28, BLUE, 500, 'middle', 'Georgia, serif'),
          path('M 240 584 V 620'),
          rect(80, 622, 320, 124, '#f0f5fb', '#c5d7ec'),
          text(240, 652, 'Homotopy loss', 22, INK, 600, 'middle'),
          text(240, 682, 'Objective + constraint penalties', 18, BLUE, 500, 'middle'),
          text(240, 710, '+ Pg pull-up penalty', 20, MUTED, 400, 'middle'),
          text(240, 735, '(unchanged along the schedule)', 18, MUTED, 400, 'middle'),
          path('M 80 694 H 48 V 432 H 78'),
          '<g transform="translate(34 650) rotate(-90)">',
          text(0, 0, 'Autodiff · update Θ', 18, BLUE, 500),
          '</g>',
          text(240, 782, 'No optimal-solution labels required.', 20, MUTED, 400, 'middle'),
          text(240, 809, 'Penalties encourage feasibility.', 20, MUTED, 400, 'middle'),
          rect(16, 848, 448, 235, '#f0f5fb', '#dfe7f1'),
          text(38, 879, 'INFERENCE', 17, BLUE, 600),
          text(240, 913, 'New load profile', 21, INK, 500, 'middle'),
          path('M 240 926 V 945'),
          text(240, 975, 'Trained policy · fixed Θ', 22, BLUE, 600, 'middle'),
          path('M 240 988 V 1007'),
          text(240, 1038, 'Approximate AC-OPF decisions', 21, INK, 600, 'middle'),
          text(240, 1067, 'Original operating problem · λH = 1', 18, MUTED, 400, 'middle'),
          '</svg>']
    return '\n'.join(s)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--png', action='store_true')
    args = parser.parse_args()
    ASSETS.mkdir(parents=True, exist_ok=True)
    for name, content in [('method-overview', method()), ('method-overview-mobile', method_mobile()), ('social-preview', social())]:
        svg = ASSETS / (name + '.svg')
        svg.write_text(content, encoding='utf-8')
        print(svg)
        if args.png:
            inkscape = shutil.which('inkscape')
            windows = Path(r'C:\Program Files\Inkscape\bin\inkscape.exe')
            if not inkscape and windows.exists():
                inkscape = str(windows)
            if not inkscape:
                raise SystemExit('Inkscape is required for --png.')
            subprocess.run([inkscape, str(svg), '--export-type=png',
                            f'--export-filename={svg.with_suffix(".png")}'], check=True)


if __name__ == '__main__':
    main()
