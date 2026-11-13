# Scientific source map and audit record

Last checked: 2026-11-13. This is an internal maintenance record. It is deliberately ASCII-safe; mathematical symbols use LaTeX commands or spelled-out names.

## Primary sources and version policy

- **Primary scientific source:** The user-provided published five-page IEEE PESGM 2026 paper, *Homotopy-Guided Self-Supervised Learning of Parametric Solutions for AC Optimal Power Flow*, DOI 10.1109/PESGM58988.2026.11693405. Read in full, including Appendix A on pages 4-5, on 2026-11-13.
- **Open companion:** [arXiv:2511.11677v1](https://arxiv.org/abs/2511.11677v1), submitted 11 November 2025. Its [PDF](https://arxiv.org/pdf/2511.11677v1) and [HTML](https://arxiv.org/html/2511.11677v1) provide public links to the corresponding sections.
- **Publication metadata:** [IEEE Xplore document 11693405](https://ieeexplore.ieee.org/document/11693405/), DOI [10.1109/PESGM58988.2026.11693405](https://doi.org/10.1109/PESGM58988.2026.11693405). The rendered publisher record was read in the browser. It identifies the 2026 IEEE Power & Energy Society General Meeting (PESGM), 19-23 July 2026, Montreal, QC, Canada; added to IEEE Xplore 24 September 2026.
- Published-version audit: the supplied IEEE PDF confirms the current title, author order, affiliation mapping, Eqs. (1)-(12), all displayed Table I values, selected n=100 Table II results, and training settings. No substantive change to these website claims was required. Scientific content now follows the published version; the previous publisher-full-text access limitation is resolved by the supplied PDF.
- arXiv still says submitted, and the first author's publication page says forthcoming. Those status labels are stale relative to the verified IEEE record. The website uses published conference status and 2026 citation metadata.
- The publisher abstract qualifies the absence of external solvers as **during training**. Do not generalize that statement to all evaluation or possible implementations.
- The earlier OpenReview manuscript, *Homotopy Learning of Parametric Solutions to Constrained Optimization Problems*, is related historical work. Do not silently import its results, authorship order or assets.

## Identity and bibliography

Exact title: **Homotopy-Guided Self-Supervised Learning of Parametric Solutions for AC Optimal Power Flow**.

| Order | Author name in paper | Affiliation | Verified resource |
|---|---|---|---|
| 1 | Shimiao Li | University at Buffalo | https://www.shimiaoli.com/ |
| 2 | Aaron Tuor | Pacific Northwest National Laboratory | https://www.pnnl.gov/people/aaron-tuor |
| 3 | Draguna Vrabie | Pacific Northwest National Laboratory | https://www.pnnl.gov/people/draguna-vrabie-phd |
| 4 | Larry Pileggi | Carnegie Mellon University | https://ece.cmu.edu/directory/bios/pileggi-larry.html |
| 5 | Jan Drgona | Johns Hopkins University | https://drgona.github.io/ |

Both the published and arXiv title blocks use unaccented Jan Drgona. JHU's official profile supports the accented spelling (LaTeX: J\'an Drgo\v{n}a). Affiliation superscripts are Li 1; Tuor 2; Vrabie 2; Pileggi 3; Drgona 4. The PDF has institution-name typos (Pacific Northwestern National Lab and John Hopkins University); the website uses correct institutional names.

Supporting official sources: https://energyinstitute.jhu.edu/people/jan-drgona/ (paper and DOI), https://www.shimiaoli.com/publications.html (conference), https://www.shimiaoli.com/ and https://drgona.github.io/news/ (acceptance announcements). Citation omits page numbers not independently verified from the publisher. This is a conference publication, not a journal article. `citation.bib`, visible BibTeX, citation meta tags and JSON-LD must agree.

## Website claim-to-source map

| Website item | Source | Qualifications |
|---|---|---|
| Exact title, order, affiliations | PDF page 1; IEEE record; official author resources | Correct institutional typos without changing affiliation mapping |
| Hero: approximate solution map from changing loads | Sections I and IV-A, Eqs. (2)-(3) | Approximation, not exact optimization |
| Easier training problems and retained network weights | Section IV-B, Eqs. (4)-(5), following paragraph | Offline heuristic, not a physical control trajectory |
| Self-supervised objective and constraint penalties | Section IV-A, Eq. (3) | No solver-generated optimal labels; still uses sampled parameter data |
| Two families of homotopy transformations | Sections IV-C and IV-D | Choices can combine; not all are used in every experiment |
| Generation objective and complex power balance | Section III, Eq. (1a)-(1f) | Includes voltage and generation bounds and reference bus; no displayed thermal-line constraint |
| Policy `x = pi_Theta(xi)` and homotopy loss | Eqs. (2b), (5) | Automatic differentiation through neural predictions; soft penalties |
| Train at fixed lambda_H, advance, reuse weights | Section IV-B paragraph after Eq. (5) | lambda_H schedules training; xi remains the policy input |
| CObj, SBnds, GPen, SaS descriptions | Section IV-C, Eqs. (6)-(9) | GPen changes penalty strength, not the exact feasible set for positive lambda_H |
| Load stepping and Tx stepping | Section IV-D, Eqs. (10)-(11) | No certified feasible initial full problem or continuation path |
| Generation pull-up note and diagram block | Appendix A | Sum(P_g)-Sum(P_d) >= epsilon; epsilon=0.01; soft penalty unchanged along schedule |
| All six case30 configurations improve reported mean/max equality residuals | Section V-A, Table I | 100 test instances; averages of per-instance metrics, no feasibility percentage |
| Full case30 table and chart | Table I, PDF page 4; Section V for $/h | Preserve printed values and standard deviations; residual units unspecified |
| Dataset, architecture, batch size, weights and schedules | Appendix A | No reported hardware, runtime or matched-compute comparison |
| Synthetic n=100 trade-off and adverse configuration | Section V-B Eq. (12), Table II | SaS+SBnds improves residual with higher objective; SaS+GPen worsens residual |
| Scope: empirical evidence without formal guarantees | Method and results | No theorem, certificate, physical deployment or measured inference-speed benchmark |
| Funding | Acknowledgments, PDF page 4 | PNNL DMC and JHU ROSEI |

## Essential algorithm and equations

Offline: sample load parameters `xi=(P_d,Q_d)`; compute policy predictions `x=pi_Theta(xi)=(V,P_g,Q_g)`; evaluate the stage-dependent objective and equality/inequality penalties using both x and xi; add the unchanged generation pull-up penalty; differentiate the loss and update Theta. At fixed lambda_H, train for multiple epochs. Then advance lambda_H and retain previous weights, ending at lambda_H=1.

Inference: a new load profile enters the fixed trained policy and produces approximate voltage/generation decisions. The paper supplies no output projection, solver-refinement stage, exact-feasibility certificate or physical closed-loop experiment. Do not invent those in a diagram.

The displayed loss follows Eq. (5), with policy Eq. (2b):

```tex
x = \pi_\Theta(\xi)
\mathcal L_{\lambda_H}(\Theta)
 = f_{\lambda_H}(x,\xi)
 + \sum_i w_i p_i(h_{\lambda_H,i}(x,\xi))
 + \sum_i w_i p_i(g_{\lambda_H,i}(x,\xi))
```

The paper offers squared equality residuals and ReLU inequality penalties as examples; no corresponding public code was verified to settle every implementation convention. Appendix A adds the pull-up term.

The original objective and complex balance displayed on the page come from Eq. (1). Tx stepping is Eq. (11): `Y_lambda=(1-lambda_H)Y_0+lambda_H Y_bus`, where Y_0 is the nearly shorted network. Load stepping multiplies active/reactive demands by lambda_H in Eq. (10).

The equality illustration comes from Eq. (9):

```tex
-\epsilon_{\lambda_H} \le h(x,\xi) \le \epsilon_{\lambda_H},
\epsilon_{\lambda_H}=(1-\lambda_H)\epsilon_H+\lambda_H\epsilon_L.
```

AC-OPF Appendix A supplies epsilon_H=0.01, epsilon_L=0, delta lambda_H=0.05. Slider positions correspond to lambda_H=0,0.05,...,1. The SVG displays the tolerance interval on the residual axis; it is neither a learned trajectory nor experimental data. Zero scheduled tolerance does not guarantee zero achieved residual.

## Exact case30 data audit

Table I: case30, 100 test instances. Constraint entries are average (standard deviation) across instances, not across training seeds. Objective unit is $/h (Section V). Residual units are unspecified. Rounded zero is not exact-feasibility evidence.

| Method | Objective ($/h) | Mean eq. | Max eq. | Mean ineq. | Max ineq. |
|---|---:|---|---|---|---|
| SaS, SBnds | 666 | 0.0027 (0.0015) | 0.010 (0.005) | 0.0000 (0.0000) | 0.000 (0.001) |
| SaS, GPen | 666 | 0.0023 (0.0014) | 0.008 (0.005) | 0.0000 (0.0000) | 0.000 (0.000) |
| Tx-stepping, SBnds | 665 | 0.0024 (0.0013) | 0.008 (0.005) | 0.0000 (0.0000) | 0.000 (0.000) |
| Tx-stepping, GPen | 665 | 0.0017 (0.0009) | 0.006 (0.003) | 0.0000 (0.0000) | 0.000 (0.000) |
| Load-stepping, SBnds | 666 | 0.0020 (0.0012) | 0.007 (0.004) | 0.0000 (0.0000) | 0.000 (0.000) |
| Load-stepping, GPen | 667 | 0.0024 (0.0016) | 0.009 (0.005) | 0.0000 (0.0000) | 0.000 (0.000) |
| Original penalty | 673 | 0.0036 (0.0027) | 0.013 (0.010) | 0.0000 (0.0000) | 0.001 (0.003) |

`data/case30.json` preserves printed decimals as strings. `scripts/generate_results.py` reads it and writes `assets/case30-residuals.svg` using Python's standard library. Dots represent the average reported mean-equality metric; bars extend one standard deviation on either side. No fitting, inferred observations or generated experimental data are used. The HTML table and alt text were checked against these values. Tx+GPen is highlighted because it has the smallest reported average mean-equality residual in Table I; this is not a feasibility rate or a significance result.

## Synthetic comparison audit

Section V-B Eq. (12) minimizes `sum_i [(1-x_i)^2 + 2(x_(i+1)-x_i^2)^2]` subject to `Ax <= b+Cxi`. It has n variables and n random linear constraints; n=5,25,50,100 and parameter dimension round(0.4n). Table II reports 100 test instances.

The site's n=100 numbers are exact:

| Method | Objective | Mean inequality violation (std) | Max inequality violation (std) |
|---|---:|---|---|
| SaS, SBnds | 272.36 | 0.0002 (0.0009) | 0.0180 (0.0711) |
| SaS, GPen | 447.32 | 0.0031 (0.0067) | 0.1990 (0.3583) |
| Original penalty | 208.71 | 0.0015 (0.0023) | 0.1249 (0.1877) |

The n=100 table heading specifies delta lambda_H=0.005 and inequality weight 500. Other columns use delta lambda_H=0.05. Appendix A's generic synthetic settings say weight 50 and fixed hyperparameters; preserve the explicit table-specific exception for n=100. Lower objective from an infeasible prediction does not establish a better feasible solution. Do not claim every configuration improves residuals.

## Training details

Appendix A AC-OPF settings:

- 50,000 sampled load profiles, 8:1:1 train/validation/test split. Loads are 75%-150% of base load. Table I reports only 100 test instances; do not relabel these statistics as all 5,000 held-out samples.
- Batch size 1024; cylinder NN with 2 layers and hidden size 200; PyTorch and Adam. Preserve the paper's layer-count wording.
- Equality weight 10^5; inequality weight 10^6; warm homotopy loss weight 10^6; generation pull-up weight 10^6 and epsilon=0.01.
- Homotopy increment 0.05; SaS epsilon_H=0.01 and epsilon_L=0; SBnds epsilon+=1 and epsilon-=0.
- Original penalty: 1000 epochs, warmup 50, patience 200. Homotopy: 100 epochs per stage, warmup 50, patience 50. Early stopping can reduce the actual counts.
- StepLR step 100, gamma 0.1, minimum learning rate 10^-5, applied only at the final stage for homotopy.
- The warm homotopy loss is distinct from retaining weights between stages. Do not confuse its weight with a penalty on optimizer warm-starting.
- No hardware, inference timing, repeated-seed uncertainty or matched-total-computation comparison is reported.

## Website assets and reproductions

| Repository item | Source / derivation | Maintenance restriction |
|---|---|---|
| `assets/paper-l2o.png` | Original paper Figure 1 from arXiv HTML | Preserve diagram content and caption |
| `assets/solaris-acopf.svg` and `assets/solaris-acopf-animation.js` | Existing SOLARIS papers-page revision 13 AC-OPF graphical abstract and original updater | Explanatory motion, not measured experimental results; pause/restart, static fallback and reduced-motion support |
| `assets/method-overview.svg` | Earlier website redraw of Sections IV-A-D and Appendix A, generated by `scripts/generate_figures.py` | Retained as a source asset; removed from the public method section as redundant with the SOLARIS graphical abstract |
| `assets/case30-residuals.svg` | Table I -> `data/case30.json` -> `scripts/generate_results.py` | Preserve all seven configurations, uncertainty meaning and units caveat |
| `assets/social-preview.png` | Website-generated project preview | Explanatory visual, not experimental evidence |

Institutional logo and template sources are recorded separately in the asset provenance documentation. Design references establish appearance, not scientific claims about this paper.

## Discrepancies and excluded claims

1. Abstract/contribution prose refers to feasibility rates, multiple IEEE benchmarks and full-solver-comparable objectives. The presented AC-OPF table shows case30, residual metrics and a neural penalty baseline only. It reports no feasibility percentage, full-solver objective row or speedup. Public claims follow the narrower numerical evidence.
2. No theorem or certificate establishes exact feasibility, global optimality or convergence. A soft penalty or zero tolerance target is not a guarantee.
3. Eq. (1) does not include thermal line-flow limits despite broad introduction text mentioning transmission limits. Do not insert those into the studied formulation without additional evidence.
4. Eq. (10)'s zero-voltage/zero-generation intuition is not a full-constraint guarantee: it need not satisfy positive voltage bounds or the unchanged pull-up margin. Describe load stepping as easing power-balance learning, with other relaxations available.
5. GPen changes the training loss, not the exact feasible set for positive lambda_H. The removed equality-tolerance demonstration must not be confused with the reused SOLARIS graphical abstract.
6. The textual equality-metric formula lacks an absolute value. Without code verification, retain the reported metric label rather than asserting a different precise residual definition.
7. Table II contains adverse configurations, including SaS+GPen at n=100; benefits depend on transformation choice.
8. No physical-grid deployment or energy-saving result is presented; generalization beyond the sampled loads is not established.

## Code and supplementary search

No paper-specific public code/data link was located in the paper, arXiv record, author home/publication pages, SOLARIS papers list or GitHub searches for title and homotopy/learning/OPF, including SOLARIS-JHU, pnnl and drgona. First-author account `ohCindy` has GridWarm, FDIAModelling and LAV-SE-synthetic-data, which concern other papers. The pnnl/neuromancer tree at commit `3f71d76088711e181624d01d3063af38c5565260` had no path containing homotopy or opf. This bounded search does not prove no implementation exists.

The public page consequently omits a Code button and makes no code-version audit claim. Do not present generic Neuromancer as this paper's released code. No experimental video or supplementary benchmark asset was identified. Future maintainers should verify any new code's relationship to arXiv v1 or the proceedings version before incorporating claims or results.

## Method prose revision, 2026-11-13

The duplicate redrawn method figure was replaced by a reading guide to the existing SOLARIS graphical abstract and a four-step algorithm description. The network, homotopy stages, AC-OPF grid and objective/constraint loss-feedback loop are explained in prose. Sections IV-A-D and Appendix A support the algorithm: sample load profiles, train at fixed lambda_H through automatic differentiation, advance lambda_H while retaining weights, and infer with fixed final weights. The unchanged generation pull-up penalty and approximate status of predictions remain explicit. The abstract lists network data alongside loads; the text clarifies that the reported AC-OPF experiment varies loads on a fixed network. Stylized landscapes and moving states are explanatory, not measured experimental data.
