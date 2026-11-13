# Homotopy-Guided AC Optimal Power Flow

Dedicated SOLARIS research project website for **Homotopy-Guided Self-Supervised Learning of Parametric Solutions for AC Optimal Power Flow**, by Shimiao Li, Aaron Tuor, Draguna Vrabie, Larry Pileggi, and Jan Drgona.

- [Project website](https://solaris-jhu.github.io/homotopy-opf-website/)
- [Website repository](https://github.com/SOLARIS-JHU/homotopy-opf-website)
- [IEEE publication](https://ieeexplore.ieee.org/document/11693405/)
- [arXiv manuscript, version 1](https://arxiv.org/abs/2511.11677v1)
- DOI: [10.1109/PESGM58988.2026.11693405](https://doi.org/10.1109/PESGM58988.2026.11693405)

Published in the **2026 IEEE Power & Energy Society General Meeting (PESGM)**. The scientific exposition and reported experiment values on this page use arXiv v1, including its appendix; bibliographic status is checked against IEEE. This repository contains the website, not the research implementation.

## Local preview

The site is plain HTML, CSS, and JavaScript. Node.js 22 or newer runs the dependency-free validation and preview helpers; no package installation is required.

```sh
node scripts/build.mjs
node scripts/serve.mjs
```

Open `http://127.0.0.1:4173/homotopy-opf-website/`. The preview deliberately includes the repository prefix used by GitHub Pages. Set the `PORT` environment variable if that port is occupied. Re-run the build and refresh the browser after an edit.

For validation without staging a build:

```sh
node scripts/validate.mjs
```

## Files and maintenance

- `index.html`: research content, accessible page structure, resource links, and scholarly metadata.
- `style.css`: TQPNet-based SOLARIS typography, colors, spacing, and responsive layouts.
- `main.js`: lightweight page interactions.
- `assets/`: locally served diagrams, illustrations, logos, fonts, and other page assets as included.
- `scripts/generate_figures.py`: reproducible generation of the new explanatory SVGs.
- `scripts/validate.mjs`: checks local resource paths, internal anchor targets, duplicate IDs, image alternative attributes, metadata, JSON-LD, and SVG well-formedness.
- `scripts/build.mjs`: validates and stages only public site files in `dist/`.
- `.github/workflows/pages.yml`: validates pull requests and deploys successful pushes to `main` using GitHub Pages.
- `LICENSE` and `NOTICE`: code license and template/asset attribution.

The repository also contains an internal source map and asset provenance record. Consult them before changing scientific claims, numerical results, equations, figures, or bibliographic metadata. Keep explanatory animations clearly distinguished from measured experiments. Preserve baselines, units, and the meaning of standard deviations when editing result tables. Recheck source-version differences before replacing manuscript-derived content with the final publication.

When editing, validate the source, inspect a local desktop and mobile preview, check keyboard operation and reduced-motion behavior, then commit to `main`. The build stages `index.html`, `style.css`, `main.js`, `assets/`, and attribution/citation files if present. Research notes, scripts, and other internal material are not included in the deployed artifact.

## Deployment

In repository **Settings → Pages**, select **GitHub Actions** as the publishing source. The workflow uses the official `configure-pages`, `upload-pages-artifact`, and `deploy-pages` actions. It validates before upload, deploys with the `github-pages` environment, and exposes the deployed URL in the workflow run. Pull requests run validation and staging but do not publish.

A green commit or completed upload is insufficient: inspect the deployment job and open the live URL to verify the published page and assets. GitHub Pages may take a short time to serve a new deployment.

## Design and rights

The visual foundation is the [TQPNet website](https://solaris-jhu.github.io/TQPNet/): Fraunces display headings, Inter body text, JHU blue, restrained cards, rounded resource buttons, and responsive scientific figures. Adapted code is distributed under Apache-2.0 with attribution in `NOTICE`. Paper figures and institutional/laboratory marks retain their original rights; see the asset provenance record. The website license does not relicense those assets.
