# CLAUDE.md

Knowledge base for proving probabilistic tube guarantees on Lie groups / Riemannian manifolds.
Read [README.md](README.md) for the research pathway and target results. This file is conventions only.

## The thesis

**Goal: tight probabilistic tubes for noisy mechanical systems on Lie groups, obtained coordinate-free.**

**Two bound types are in scope, both of them.** (a) *mean-squared*, $\mathbb E\,d(X_t,\bar x_t)^2\le\cdots$, via a generator inequality and Grönwall — the [[@daniObserverDesignStochastic2015]] shape; (b) *sup-over-time high probability*, $\mathbb P[\sup_{t\le T} d \le r_{\delta,t}]\ge1-\delta$, via an affine martingale and Doob. Neither subsumes the other: (a) plus Markov gives a probability only at a fixed $t$, and upgrading it to $\sup_t$ is the lossy step (b) exists to avoid. Do not silently collapse the two — say which is being proved.

The tool for (b) is the **AMGF** (averaged moment generating function) of Zishun Liu and Yongxin Chen's group — $\Phi_{n,\lambda}(x) = \mathbb E_{\ell\sim S^{n-1}}\big[e^{\lambda\langle\ell,x\rangle}\big]$. Its energy function is an *affine martingale*, and Doob's inequality then converts a sublevel set into a probabilistic tube. See [content/00-study-plan.md](content/00-study-plan.md) Phase 5.

Why it is the right object to make intrinsic: $\Phi_{n,\lambda}$ is **rotation-invariant and depends only on $\|x\|$**. It is already a radial, isotropic function — so the manifold generalization is forced and natural: replace $\|x\|$ with Riemannian distance and the $S^{n-1}$ average with an average over the unit sphere in $T_xM$. Nothing chart-dependent has to be invented.

**The contrast that motivates all of this.** [[@daniObserverDesignStochastic2015]] proves a stochastic contraction bound using a *state-dependent metric* $M(x,t)$ — a coordinate-dependent treatment. Its Assumption 1 requires $\bar m_x = \sup|\partial M_{ij}/\partial x|$ and $\bar m_{x^2} = \sup|\partial^2 M_{ij}/\partial x^2|$: sup bounds on derivatives of the **metric components in a chart**. Those constants enter the bound, so the tube inflates with how much the chart's metric varies rather than with anything intrinsic. That is where the conservatism comes from.

A coordinate-free treatment should replace those metric-derivative bounds with **curvature** — the intrinsic content of $\partial^2 g$ — and nothing else. When writing anything in `content/`, that is the standard to hold results to. The critique applies to **both** bound types: a manifold AMGF written naively in a chart would pick up the same kind of constants.

:::warning[What the lessons actually found — read before repeating the claim above]
[[29-tightness-comparison]] tested this and the headline form is **not supported**. Ranked by radius, the sources of conservatism are: worst-case norms $\approx80\times$; bound type $14$–$269\times$; looseness even in the best bound $\approx3.5\times$; **chart-dependence $\approx2.5\times$**; the $T^*Q\to Q$ projection $\approx1.13\times$. Chart-dependence is the *smallest*, and only the first is what going intrinsic removes — sources (b)–(e) survive a fully coordinate-free treatment untouched.

**The defensible claim is different, and stronger in its own way: going intrinsic does not reduce the bias, it removes the variance.** Chart-dependence is the only source that is *unbounded and arbitrary* — [[24-dani-stochastic-contraction]] exhibits two charts, related by an isometry, where one certifies rate 1 and the other certifies nothing at all. $2.5\times$ is the typical case in a chart someone would actually pick; the worst case has no bound.

Two corrections to the framing above:
- The load-bearing chart artifact is **conditioning**, not derivative bounds. In Euler angles $\bar m_x$ stays $=1$ (and $\to0$ at gimbal lock); what diverges is $m=\inf\lambda_{\min}M\to0$, and the bound carries $\bar m_x/m$, $\bar m_{x^2}/m^2$ and an overall $1/m$.
- $SE(3)$ with block-diagonal $\mathbb I$ is isometric to $SO(3)_{\mathbb J}\times\mathbb R^3$, so absence of a bi-invariant metric does **not** by itself give mixed-sign curvature — that needs rotation–translation coupling.

**The blocking open problem**: every curvature number in the repo ($\mathrm{Sec}\equiv\tfrac14$, $\mathrm{inj}=\pi$) is for $SO(3)$, but the tube lives on $T^*SO(3)$ with the cross-term metric of [[16-cross-term-metrics]], whose curvature is uncomputed and which [[13-sasaki-metric]] shows is sign-indefinite and grows with $\|u\|^2$. **Neither track has a usable $\kappa$ or $\mathrm{inj}$ on the state manifold.** This blocks the chart route identically, so it favours neither side — but it means the headline comparison is not yet available on the object the project targets.
:::

## Layout

| Dir | Owner | Contents |
|---|---|---|
| `refs/` | tool-generated | Source papers (`@citekey.pdf`, `@citekey/` LaTeX tree) + a `@citekey.md` rewrite for cheap retrieval |
| `notes/` | **the user** | Their own understanding. Three monolithic files by subject — geometry, probability, mechanics. Deliberately not atomic |
| `content/` | Claude | Lessons + practice problems, plus `00-study-plan.md`. See [content/CLAUDE.md](content/CLAUDE.md) |
| `tools/` | Claude | `fetch.py` — arXiv LaTeX and Zotero PDFs |

## Rules

1. **Never edit `notes/` unless explicitly asked.** That folder is the record of what the user actually understands — it is the input that tells you where to start, not a scratchpad. Read it before writing any `content/`.
2. [content/00-study-plan.md](content/00-study-plan.md) is the backlog, ordered, with a critical path. When asked what to work on next, start there. Update it as lessons land.
3. In `content/`, new topic ⇒ new file. `notes/` is the exception: it stays three files, and sections get appended to the right one — only on explicit request.
4. Wikilinks only: `[[filename]]`, no path, no extension — this is an Obsidian vault and links resolve by basename. Keep basenames unique across the whole repo.
5. Cite sources as `[[@citekey]]` (Better BibTeX key, matching the file in `refs/`). Add a section pointer in prose: `[[@khanMeansRandomVariables2025]] §3.2`.
6. Callouts use the `:::` directive syntax with a bracketed title:

   | Use | Syntax |
   |---|---|
   | Definition, assumption | `:::info[Definition]` … `:::` |
   | Theorem, lemma, proposition, corollary | `:::tip[Theorem]` … `:::` (retitle as `[Lemma]`, `[Proposition]`, `[Corollary]` when apt) |
   | Anything unresolved | `:::warning[Open question]` … `:::` |

   In `refs/`, put the source pointer **in the title**: `:::tip[Theorem 2.3 — exponential distance bound, eq. (8)]`. That is what makes these files retrievable. Elsewhere the bare title is fine.

   Use the open-question callout freely — do not paper over a gap. Leave a blank line after the closing `:::`. The old ` ```ad-* ` fences are gone; do not reintroduce them.
7. Frontmatter is `tags:` only. No status fields, no dates.
8. Math in `$…$` / `$$…$$`. MathJax, not KaTeX.

## Mathematical conventions

- **Matrix Lie groups first.** Loosen to homogeneous manifolds, then Riemannian manifolds. Do not open with the general case.
- **Coordinate-based treatment of intrinsic objects.** Write things in a chart, but only claim results that are chart-independent.
- **Flag chart-dependent constants as conservatism.** Any bound whose constants are sup-norms of metric components or their derivatives ($\sup|\partial g_{ij}|$, $\sup|\partial^2 g_{ij}|$, Christoffel bounds) is a coordinate artifact. Say so, and name what the intrinsic replacement should be — usually a curvature bound, an injectivity radius, or a Hessian-comparison constant. Do not quietly reproduce a chart-dependent estimate as if it were the answer.
- When a construction has more than one source (most importantly `exp`/`log` — see [[riemannian-geometry]] § "Exp and log: two sources", resolved quantitatively in [[03-levi-civita-left-invariant]]), **state which one is meant**. Never silently pick.
- State simplifying assumptions inline at the point of use, not in a global preamble.
- Prefer $SO(3)$ / $SE(3)$ for worked examples: $SO(3)$ when bi-invariance is wanted, $SE(3)$ when its failure is the point.

## Tools

```bash
python tools/fetch.py arxiv 2503.12345 --key khanMeansRandomVariables2025
python tools/fetch.py zotero --tag lie-groups
```

Zotero needs `ZOTERO_API_KEY` and `ZOTERO_USER_ID` in the environment, and [pyzotero](https://github.com/urschrei/pyzotero) (already in the `everything` conda env; imported lazily so the arxiv path runs without it). The arXiv path is stdlib — keep it that way.

The tool downloads sources; **converting a paper to `refs/@citekey.md` is your job**, not the tool's. Rewrite it so the key definitions, theorem statements and notation are retrievable without re-reading the PDF.
