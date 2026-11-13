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

Original arXiv image: assets/paper-l2o.png from https://arxiv.org/html/2511.11677v1/figures/L2Ofig.png (Figure 1). Unmodified author figure, reproduced on this author-requested project site; retains original rights. Paper Figure 2 was removed at the author\'s request in favor of the existing SOLARIS graphical abstract.

New method overview (desktop/mobile) and social preview: scripts/generate_figures.py. Case30 error-bar plot: scripts/generate_results.py using data/case30.json, exact Table I transcription. These new explanatory/data visualizations are separately distinguishable from the original paper artwork.

## SOLARIS graphical abstract, revision 13

The hero reuses the exact AC-OPF artwork and animation from the [SOLARIS papers page](https://solaris-jhu.github.io/solaris-website/papers.html), retrieved 2026-11-13 from repository commit `90d8817e9b10621ef2edc189e5290c47465d2c2f`.

- `assets/solaris-acopf.svg`: unchanged bytes from `static/images/papers/v13/arxiv-2511.11677.svg`; source blob `86d965975e6d1e4d7eeeb9f1c6bf9f59dfa140a4`.
- `assets/solaris-acopf-animation.js`: the exact `v10-acopf` updater extracted from `static/js/paper-abstracts-v13.js`; source blob `ad22efa8b90b6bd40580744a7e9c1626ce8f447a`. Only the wrapper/export changed; geometry and update math did not.
- `main.js` provides page-specific play/pause and restart controls, pauses off-screen and hidden-tab updates, and starts paused for reduced-motion preferences. The external SVG remains a static fallback without JavaScript.
- The updater's sample arrays and trajectory motion are explanatory illustration from the SOLARIS page. They are not measured Table I/II data, physical-grid experiments, or a convergence guarantee. The caption makes this distinction explicit.

This reuse is explicitly requested by the author. Original SOLARIS contributors retain their rights; no new claim of ownership is made.

## Additional university marks

- `assets/logos/buffalo.svg`: existing Adobe Illustrator vector copy of the blue UB interlocking monogram with stacked university-name lockup (360 x 266 viewBox), retrieved unchanged from [KNITPhoenix/knitphoenix.github.io](https://github.com/KNITPhoenix/knitphoenix.github.io/blob/d7766b321d5051702189ddd7582ab1a54c871cda/assets/logos/University_at_Buffalo_logo.svg), blob `b7c903e0711cfdda1f5845a436a7f5d9faf390f0`. Official identity reference: https://www.buffalo.edu/brand/identity/university-logo-and-marks.html (stacked University Lockup).
- `assets/logos/cmu-wordmark.svg`: existing red horizontal university wordmark, converted from `cmu-wordmark-horizontal-r.eps`, retrieved unchanged from [cmudco/dare-backend](https://github.com/cmudco/dare-backend/blob/3fb4dd2dbc0e6f6216998d69fd71dda07dc875c7/cmu-quiver/shared/assets/cmu-wordmark.svg), blob `b27c1c02cb57158deb70d800e4a007b59277b87a`. Official identity reference: https://brand.cmu.edu/visual-identity/carnegie-mellon-trademarks/wordmarks.

These are existing vector marks, not recreated text or generated logos. Their copied-file sources are recorded separately from the official identity references; the university download portals were not used. Preserve their proportions. The surrounding page applies the established SOLARIS grayscale treatment with original color on hover or keyboard focus. Trademark rights remain with the universities.
