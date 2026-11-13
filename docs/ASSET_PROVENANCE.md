# Asset and template provenance

Verified 2026-11-13. Research content and paper figure provenance are documented separately in SOURCE_MAP.md. Design references are not scientific evidence for this paper.

## Visual foundation

The page adapts the TQPNet project-page visual language from [SOLARIS-JHU/TQPNet/website](https://github.com/SOLARIS-JHU/TQPNet/tree/main/website): Fraunces display headings, Inter body text, JHU Heritage Blue (#002d72), pale background (#fbfbfd), restrained 14px corner radii, pill resource buttons, a 1100px content width, responsive grids and muted institution logos.

The inspected CSS blob was `3cfd222665f81386d365a1c310aaf5f516741de1`; the HTML blob was `a692a0aeb83213e1d925de1e164f0be14bc59538`. The TQPNet repository is Apache-2.0 licensed (LICENSE blob `9af26733803db7bc5df30233b591b62c2066ccfd`). The present page replaces its scientific content and makes paper-specific layout and interaction changes. Preserve the Apache-2.0 license for adapted source; institution marks and paper figures retain their owners' rights.

All nine supplied reference pages were opened and inspected as rendered desktop pages: TQPNet, MI-DPC-UPHES, SD-DPC, Mixed-Integer DPC, PDE Control with DPC, CINOC, SCORE, Chiller Plant MI-DPC and Neural DAEs. TQPNet remains the single selected visual foundation.

## Locally hosted institution and lab marks

| Asset | Retrieved source | Source Git blob |
| --- | --- | --- |
| `assets/logos/jhu-whiting.svg` | [TQPNet JHU Whiting SVG](https://github.com/SOLARIS-JHU/TQPNet/blob/main/website/static/logos/jhu-whiting.svg) | `b02d08417d5e3983cfdb7fa0ffedbc04394344d1` |
| `assets/logos/solaris.png` | [TQPNet SOLARIS mark](https://github.com/SOLARIS-JHU/TQPNet/blob/main/website/static/logos/solaris.png) | `c217b3fae21f8b381842c5f289484f79a3acf4ee` |
| `assets/logos/pnnl.jpg` | [NeuralDAEs PNNL mark](https://github.com/drgona/NeuralDAEs/blob/main/static/images/PNNL_logo.jpg) | `7ad92301eedaff66bb9169c38819a7b06cef1697` |

These existing institution/lab marks identify the participating organizations and link to their resources. They are not newly generated logos and must not be represented as Apache-licensed original artwork. No claim of trademark ownership or unrestricted reuse is made.

## Typography source

TQPNet's original font declaration is:

`https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,500;9..144,600&family=Inter:wght@400;500;600&display=swap`

Required template faces are Fraunces normal 500/600 and Inter normal 400/500/600. Reference fallback stacks are Fraunces/Georgia/Times New Roman/serif and Inter/system-ui/Segoe UI/Roboto/sans-serif. If font binaries are locally hosted, include their original license notices and record the exact retrieved URLs with the font assets.

## New explanatory artwork

New graphical abstracts and animation should be treated as explanatory illustrations, not measured experiment output. Their generation scripts and scientific source mapping belong in this repository. Original paper figures retain axes, units, legends and experiment context; do not recolor or replot them in ways that change their meaning.

## Local typography and math runtime

Fraunces and Inter Latin variable WOFF2 files are hosted in assets/fonts, with exact Google Fonts download URLs in assets/fonts/sources.json and original SIL Open Font License notices alongside them. fonts.css retains the requested weights and unicode range.

KaTeX 0.16.22 is vendored from https://cdn.jsdelivr.net/npm/katex@0.16.22/ (dist/katex.min.js, dist/contrib/auto-render.min.js, dist/katex.min.css, dist/fonts/*.woff2). Its MIT LICENSE is retained in assets/vendor/katex/LICENSE. CSS font source lists were reduced to WOFF2; font bytes and JavaScript are otherwise unchanged. Page assets do not require a runtime CDN connection.

Original arXiv images: assets/paper-l2o.png from https://arxiv.org/html/2511.11677v1/figures/L2Ofig.png (Figure 1); assets/paper-homotopy-path.png from https://arxiv.org/html/2511.11677v1/figures/homo_path.png (Figure 2). Unmodified author figures, reproduced on this author-requested project site; retain original rights.

New method overview (desktop/mobile) and social preview: scripts/generate_figures.py. Case30 error-bar plot: scripts/generate_results.py using data/case30.json, exact Table I transcription. These new explanatory/data visualizations are separately distinguishable from the original paper artwork.
