---
tags: [plan, moc]
---
# Study Plan

Derived by diffing three things: the [[README|pathway]], my notes ([[riemannian-geometry]], [[probability-on-manifolds]], [[mechanical-systems-on-lie-groups]]), and the machinery the drafts in `refs/claude-gen-import/` already lean on.

**Baseline.** The notes cover the *smooth* and *metric* layers: groups, manifolds, brackets, connections, left-invariant metrics, the exp/log split, bundles, parallel transport, normal coordinates, Gauss lemma, Haar measure, means, forms, symplectic form, tautological one-form, Kolmogorov/Fokker–Planck. Everything below is assumed **not** understood yet.

**The drafts are not a foundation.** They are unverified attempts; `contraction-mech-RG.tex` §"Audit of claims" lists what needs independent checking, and `stoch-contraction-RG.tex` closes with open conventions. Every phase below ends with a *verify* task against a specific numbered claim. That is the point of the exercise, not a formality.

---

## Phase 0 — Lie algebra bookkeeping

Nothing downstream parses without this. Highest priority.

| # | Lesson | Delivers |
|---|---|---|
| 01 | `ad`, `Ad`, `ad*`, `Ad*`; hat/vee on $\mathfrak{so}(3)$; the pairing $\langle\mathrm{ad}^*_\xi\mu,\eta\rangle=\langle\mu,\mathrm{ad}_\xi\eta\rangle$ | Why momenta live in $\mathfrak g^*$ and why the dual operator appears |
| 02 | Left/right trivialization $TG\cong G\times\mathfrak g$, $T^*G\cong G\times\mathfrak g^*$; body vs spatial velocity | The state $(g,\xi)$ and the reconstruction/dynamics split |
| 03 | Koszul → Levi-Civita of a left-invariant metric: $\nabla_\xi\eta=\tfrac12([\xi,\eta]-\widetilde{\mathrm{ad}}_\xi\eta-\widetilde{\mathrm{ad}}_\eta\xi)$, metric adjoint $\widetilde{\mathrm{ad}}=\mathbb I^{-1}\mathrm{ad}^*\mathbb I$ | **Answers the exp/log question in my notes**: bi-invariant ⟹ $\nabla_\xi\xi=0$ ⟹ the two exponentials agree; otherwise $\nabla_\xi\xi=-\widetilde{\mathrm{ad}}_\xi\xi\neq0$ measures the gap |
| 04 | Unimodularity: $\mathrm{tr}\,\mathrm{ad}_\eta=0 \iff \sum_i\mathrm{ad}^*_{e_i}e_i=0$ | The hypothesis that makes Lie-group Brownian motion drift-free |

*Verify:* Lemma "Levi-Civita connection of a left-invariant metric" in `rigid-body-contraction-RG.tex` — rederive from Koszul, then specialise to $SO(3)$ with $\mathbb J=j\,\mathrm{id}$ and with $\mathbb J$ asymmetric.

## Phase 1 — Curvature

| # | Lesson | Delivers |
|---|---|---|
| 05 | Riemann tensor, sign conventions, the symmetries; sectional curvature | Every formula downstream is convention-sensitive; fix one now |
| 06 | Curvature of left-invariant metrics; bi-invariant case $\mathrm{Sec}(X,Y)=\tfrac14\|[X,Y]\|^2\ge0$ | Why $SO(3)$ with symmetric inertia is benign and asymmetric inertia is not — some sectional curvatures go negative |
| 07 | Jacobi equation, geodesic deviation, tidal operator $\mathrm{Jac}_v(u)=R(u,v)v$ | The variational equation of the unforced system *is* the Jacobi equation; this is the curvature term in every contraction estimate |
| 08 | $\mathrm{grad}$, $\mathrm{Hess}^\sharp$, Hessian of the distance function, comparison theorems | Prereq for any AMGF-style distance function (pathway step 4) |

## Phase 2 — Mechanics on $T^*G$ — *pathway step 1*

| # | Lesson | Delivers |
|---|---|---|
| 09 | Legendre transform, hyperregularity, $H=\tfrac12\|\alpha\|^2_{\mathbb G^{-1}}+V$; $\iota_{X_H}\omega_0=dH$; Cartan's magic formula; Liouville volume | $\mathcal L_{X_H}\omega_0=0$ and $\mathrm{div}_\Lambda X_H=0$ — the structure the feedback must break |
| 10 | Euler–Poincaré from constrained variations $\delta\xi=\dot\eta+\mathrm{ad}_\xi\eta$; Lie–Poisson; forced version $\dot\mu=\mathrm{ad}^*_\xi\mu+f$ | Hamiltonian dynamics on Lie groups — the pathway's first deliverable |
| 11 | Left-trivialised $\omega_0=\langle\nu_2,\eta_1\rangle-\langle\nu_1,\eta_2\rangle+\langle\mu,[\eta_1,\eta_2]\rangle$; the two splittings (Levi-Civita vs flat left-invariant $\nabla^-$, torsion $-[\cdot,\cdot]$) | **Answers the symplectic question in my notes**: the bracket term *is* the torsion of the other connection. Conflating the two splittings is the easiest way to get a wrong sign |
| 12 | Connector $K$, horizontal/vertical splitting of $T(TG)$, lifts, Liouville field $\Delta$, vertical endomorphism $J$; SODE $J\Gamma=\Delta$; spray $[\Delta,S]=S$ | **Answers "how do vector fields on $TG$ become a second-order ODE on $TTG$"** |
| 13 | Sasaki metric; Kowalski's sectional curvatures $\mathrm{Sec}(X^h,Y^h)=\mathrm{Sec}(X,Y)-\tfrac34\|R(X,Y)u\|^2$, $\mathrm{Sec}(X^h,Y^v)=\tfrac14\|R(u,Y)X\|^2$, vertical $=0$; $\mathrm{Scal}$ drops by $\tfrac14\|R_\xi\|^2$ | **Answers "curvature of $TG$ in the Sasaki metric"** — a listed potential result |

*Verify:* the covariant Hamilton equations $\dot q=\mathbb G^\sharp\alpha$, $\tfrac{D}{dt}\alpha=-dV$ in `contraction-mech-RG.tex` Lemma 4.1 — the metric-compatibility cancellation is the whole proof.

## Phase 3 — Contraction — *pathway step 2*

| # | Lesson | Delivers |
|---|---|---|
| 14 | Contraction on Riemannian manifolds: $\langle\nabla_w X,w\rangle_G\le-\lambda\|w\|_G^2$; $K$-reachability; equivalence with decay of $\|w\|_G$ along variation fields | The definition, and the trick that avoids computing $\nabla^G$ on the $2n$-manifold |
| 15 | Divergence bound $\mathrm{div}_G X\le -N\lambda$; symplectic ⟹ never contracting; Hamiltonian spectra are symmetric about $0$ | Contraction is *not* structure-preserving — this reframes the whole design problem |
| 16 | Why block-diagonal (Sasaki, total-energy) metrics cannot certify — the $\pm v$ argument; cross-term / $g$-natural metrics $a\|u\|^2+2b\langle u,\xi\rangle+c\|\xi\|^2$ | **This is the "coupling term in the metric" in the potential results** |
| 17 | Curvature-corrected stiffness $\mathcal S_\alpha=\mathrm{Hess}^\sharp(V+\varphi)+\mathrm{Jac}_v$; the condition $d>(\sigma-\mu)/(2\sqrt\mu)$ | Positive curvature *helps*; negative curvature bounds the region **in velocity** and damping cannot repair it; contraction regions are contractible so never global on $SO(3)$ |
| 18 | Partial / hierarchical contraction; feedback interconnection vs cascade | The $SE(3)$ quadrotor decomposition, where full actuation fails |

*Verify:* Theorem "Contraction certificate" — in particular the constant in $d>(\sigma-\mu)/(2\sqrt\mu)$, and the two consistency checks the draft itself offers ($V\equiv0$ ⟹ Jacobi equation; $\sigma=\mu$ ⟹ any $d>0$).

## Phase 4 — Stochastics on manifolds — *pathway step 3*

| # | Lesson | Delivers |
|---|---|---|
| 19 | Itô vs Stratonovich; Itô's lemma under $y=\phi(x)$ and the non-tensorial $\tfrac12\partial^2\phi\,(\sigma\sigma^\top)$ term; quadratic variation | The single mechanism separating the two noise models |
| 20 | SDEs on manifolds: $\tilde X=X+\tfrac12\sum\nabla_{\sigma_i}\sigma_i$; generator $Af=Xf+\tfrac12\sum\sigma_i[\sigma_i[f]]$ | The generator is the invariant; the drift is not. **Pathway step 3** |
| 21 | Brownian motion on a manifold ($\tfrac12\Delta$), development along an orthonormal frame, $g^{-1}dg=\sum e_i\circ dW_i$; embedded version with mean curvature $\tfrac12 H$ and the second fundamental form | Why the frame bundle in my notes matters, and where a "pinning" drift comes from |
| 22 | Case A (force noise) vs Case B (configuration noise) | **Directly the potential results**: force noise puts the quadratic variation in the flat fibre ⟹ no curvature correction, drift is tensorial; configuration noise puts it in the curved base ⟹ chart-dependent drift |

*Verify:* the $SO(3)$ computation $\sum_i\hat e_i^2=-2I \Rightarrow dR=-R\,dt+\sum_i R\hat e_i dW_i$, and that this drift is exactly $\tfrac12 H$ enforcing $d(R^\top R)=0$.

## Phase 5 — Tubes — *pathway steps 4–6*

Nothing here is drafted yet. This is the actual research frontier.

| # | Lesson | Delivers |
|---|---|---|
| 23 | Martingales, supermartingales, optional stopping, Doob/Ville maximal inequality | $\mathcal L V\le0$ ⟹ supermartingale ⟹ $\mathbb P[\sup_t V\ge c]$ bound. The tube guarantee itself |
| 24 | AMGF-style coordinate-invariant distance functions; applying $\mathcal L$ to one | Where Gauss lemma ($\|\nabla r\|=1$) and Hessian comparison enter. **Pathway steps 4–5** |
| 25 | Deterministic surrogate for trajectory optimization on a manifold | **Pathway step 6** |

---

## Critical path

01 → 02 → 03 → 05 → 07 → 10 → 14 → 19 → 20 → 23.

Everything else is a branch off it. If time is short, 03 and 07 are the two that unlock the most: 03 settles the exp/log ambiguity that runs through every definition, and 07 is the curvature term that appears in both the contraction estimate and the generator.

## Housekeeping

- `refs/claude-gen-import/partial-contraction-RG.tex` and `rigid-body-contraction-RG.tex` are byte-identical. Delete one.
- The drafts cite real sources not yet in `refs/`: Bullo & Lewis 2004 (*Geometric Control of Mechanical Systems*), Simpson-Porco & Bullo 2013 (*Contraction Theory on Riemannian Manifolds*), Lohmiller & Slotine 1998, Lee & Chirikjian `arXiv:2510.19991`, Kowalski 1971, Musso–Tricerri 1988. The arXiv one is a one-liner: `python tools/fetch.py arxiv 2510.19991 --key leeBrownianMotionLie2025`.
