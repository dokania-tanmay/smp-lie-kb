---
tags: [plan, moc]
---
# Study Plan

Derived by diffing three things: the [[README|pathway]], my notes ([[riemannian-geometry]], [[probability-on-manifolds]], [[mechanical-systems-on-lie-groups]]), and the machinery the drafts in `refs/claude-gen-import/` already lean on.

**Baseline.** The notes cover the *smooth* and *metric* layers: groups, manifolds, brackets, connections, left-invariant metrics, the exp/log split, bundles, parallel transport, normal coordinates, Gauss lemma, Haar measure, means, forms, symplectic form, tautological one-form, Kolmogorov/Fokker–Planck. Everything below is assumed **not** understood yet.

**The drafts are not a foundation.** They are unverified attempts; `contraction-mech-RG.tex` §"Audit of claims" lists what needs independent checking, and `stoch-contraction-RG.tex` closes with open conventions. Every phase below ends with a *verify* task against a specific numbered claim. That is the point of the exercise, not a formality.

**Written.** [[notation]] (the notation contract — read it before any lesson) and lessons **01–30**. All six phases complete; ~3,900 lines, 120 problems.

:::warning[Track A and track B are not independent — a structural correction]
The fork below presents A and B as parallel. [[25-intrinsic-mean-squared]] shows they are not: track A's confinement hypothesis (H4), keeping the process where $r$ is smooth, can only be closed by an exit-time probability $\mathbb P[\tau_\rho\le T]$ — a $\sup_t$ statement, i.e. **track B**. A depends on B to justify its own domain of validity. Order of attack still A-first (its template is in hand), but A cannot be *finished* alone.
:::

Three results from Phases 0–1 are worth knowing before continuing, because later lessons depend on them:

- [[03-levi-civita-left-invariant]] resolves the exp/log open question quantitatively: $d(\exp_G(t\xi),\exp_e(t\xi))=\tfrac12t^2\|\widetilde{\mathrm{ad}}_\xi\xi\|_{\mathbb I}+O(t^3)$. A $t$-uniform bound still needs curvature.
- [[06-curvature-left-invariant-metrics]] and [[07-jacobi-equation]] independently derive $R(X,Y)Z=-\tfrac14[[X,Y],Z]$ for bi-invariant metrics under this repo's sign convention — **minus**, where do Carmo-convention sources print $+$. The minus is what makes $\mathrm{Sec}=\tfrac14\|[X,Y]\|^2$ positive.
- [[08-hessian-comparison]] sharpens the thesis: $\bar m_{x^2}$ has an intrinsic counterpart (curvature), but **$\bar m_x$ has none** — normal coordinates give $\partial_kg_{ij}(p)=0$, so a first-derivative bound is a pure chart artifact. And injectivity radius is an irreducible third hypothesis, invisible to curvature (flat torus: $\mathrm{Sec}\equiv0$, $\mathrm{inj}=L/2$ arbitrarily small).

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
| 08 | $\mathrm{grad}$, $\mathrm{Hess}^\sharp$, Hessian of the distance function, comparison theorems, cut locus / injectivity radius | **On the critical path.** These are the intrinsic constants meant to replace Dani's $\sup|\partial M_{ij}|$, $\sup|\partial^2 M_{ij}|$ — see Phase 5 |

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

:::tip[Verification outcome — done in [[17-curvature-corrected-stiffness]]]
**The constant reproduces exactly** and both consistency checks pass. The draft's headline theorem survives independent reconstruction.

Two corrections to the draft were found elsewhere in Phase 3, both in [[16-cross-term-metrics]]: its linear-shadow identity $\mathcal A^\top P+P\mathcal A=\mathrm{diag}(0,-2M^{-1}DM^{-1})$ holds **only in Hamiltonian variables** ($p=M\dot q$), not in $(q,\dot q)$; and the obstruction proposition is *stronger* than stated — the hypothesis $\pm\alpha_q\in\mathcal W$ is unnecessary whenever $\mathcal W$ contains the closed-loop equilibrium, since that is itself a zero covector. [[15-symplectic-not-contracting]] also replaced the draft's Darboux-dependent spectral argument with a direct one.
:::

:::warning[A second source of conservatism — not chart-dependence]
[[17-curvature-corrected-stiffness]] finds the certified rate running ~2 orders of magnitude below the damping ($\lambda\approx0.030\,\mathrm{s^{-1}}$ at $d=2.5$). The cause is that $\kappa\le(\sigma-\mu)/2$ is a **uniform worst-case norm** which cannot exploit the anisotropy of $\mathrm{Jac}_v$ — an operator that annihilates $v$ outright. And $\sigma$ itself grows like $|\mathrm{Sec}|\sup\|v\|^2$, so required damping diverges from both ends as the region approaches the velocity cap.

This conservatism is **not** the chart-dependence the thesis attacks, and a fully intrinsic treatment would leave it untouched. Lesson 29 must separate the two sources or it will credit the coordinate-free formulation with a gain it did not produce.
:::

:::warning[Open — an algebraic loop in the quadrotor interconnection]
[[18-hierarchical-contraction]] found that the draft's $SE(3)$ decomposition does not satisfy the interconnection theorem's hypotheses. The theorem needs output maps $h_i:M_i\to\mathbb R^k$, but the attitude block consumes $\dot F_{\mathrm{des}}$, which contains $\dot e_v=(\Delta-k_ve_v-k_xe_x)/m$, which contains $\Delta$, hence $b_3$ — **the attitude state**. So the attitude block's input depends on its own state: an algebraic loop the draft does not notice. Separately, the source theorem is stated for time-invariant fields while both blocks here are tracking-error systems around time-varying references.

Also noted: the theorem yields only a *block-diagonal* product metric — exactly the structure [[16-cross-term-metrics]] shows is too weak for a single mechanical system. The small-gain condition is presumably sufficient but not necessary, and an honest off-diagonal $G_{12}$ should relax it. No source builds one.
:::

## Phase 4 — Stochastics on manifolds — *pathway step 3*

| # | Lesson | Delivers |
|---|---|---|
| 19 | Itô vs Stratonovich; Itô's lemma under $y=\phi(x)$ and the non-tensorial $\tfrac12\partial^2\phi\,(\sigma\sigma^\top)$ term; quadratic variation | The single mechanism separating the two noise models |
| 20 | SDEs on manifolds: $\tilde X=X+\tfrac12\sum\nabla_{\sigma_i}\sigma_i$; generator $Af=Xf+\tfrac12\sum\sigma_i[\sigma_i[f]]$ | The generator is the invariant; the drift is not. **Pathway step 3** |
| 21 | Brownian motion on a manifold ($\tfrac12\Delta$), development along an orthonormal frame, $g^{-1}dg=\sum e_i\circ dW_i$; embedded version with mean curvature $\tfrac12 H$ and the second fundamental form | Why the frame bundle in my notes matters, and where a "pinning" drift comes from |
| 22 | Case A (force noise) vs Case B (configuration noise) | **Directly the potential results**: force noise puts the quadratic variation in the flat fibre ⟹ no curvature correction, drift is tensorial; configuration noise puts it in the curved base ⟹ chart-dependent drift |

*Verify:* the $SO(3)$ computation $\sum_i\hat e_i^2=-2I \Rightarrow dR=-R\,dt+\sum_i R\hat e_i dW_i$, and that this drift is exactly $\tfrac12 H$ enforcing $d(R^\top R)=0$.

:::warning[Correction — already found]
Checking `stoch-contraction-RG.tex` against [[@leeGeometricInterpretationBrownian2025]] turned up a misdirected citation: **Corollary 2 is not "$H=-2R$ on $SO(3)$"**. Corollary 2 is the general embedded-unimodular-group result; the $H=-2R$ computation is example **§V-F**, eqs. (104)–(105). The claim is right, the pointer is wrong. Two smaller ones: "the generator is the invariant" is §II-C prose + Remark 1, not Theorem 2; and Theorem 6 is a quoted Gauss formula, not a contribution.

Theorems 1, 2, 4, 5 and Corollary 1 were confirmed at the numbers the draft uses.
:::

*Convention trap:* $H=-2R$ is locked to the scaling $\langle\eta,\xi\rangle_{\mathfrak{so}(3)}=\tfrac12\mathrm{tr}[\eta^T\xi]$, and $H$ carries no $1/n$ (the authors flag do Carmo's differing convention). $\mathrm{ad}^*$ there is the plain dual, no sign flip.

## Phase 5 — AMGF tubes — *pathway steps 4–6*

**This is the thesis** (see [../CLAUDE.md](../CLAUDE.md) § The thesis). Nothing here is drafted. Everything above exists to make this phase possible.

### The target object

:::info[Definition]
**AMGF** (averaged moment generating function), [[@liuNewProofSubGaussian2025]] Def. 2.1, [[@liuSafetyVerificationNonlinear2025]] Def. IV.2:
$$\Phi_{n,\lambda}(x) \;=\; \mathbb E_{\ell\sim S^{n-1}}\big[e^{\lambda\langle\ell,x\rangle}\big],
\qquad \Phi_X(\lambda) = \mathbb E_X\big[\Phi_{n,\lambda}(X)\big].$$
The MGF averaged over the unit sphere rather than evaluated along one direction. It depends only on $\|x\|$: $\Phi_{n,\lambda}(x)=\varphi_n(\|\lambda x\|)$ with $\varphi_1(z)=\cosh z$ and $\varphi_n(z)=\Gamma(n/2)(2/z)^{(n-2)/2}I_{(n-2)/2}(z)$ for $n\ge2$ ($I$ = modified Bessel, first kind).

Properties ([[@liuSafetyVerificationNonlinear2025]] Lemma IV.2): **rotation invariance**, monotonicity in $\|x\|$, exponential growth $\Phi_{n,\lambda}(x)\ge(1-\varepsilon^2)^{n/2}e^{\varepsilon\|\lambda x\|}$.
:::

:::tip[Theorem]
**Affine martingale (AM)**, [[@liuSafetyVerificationNonlinear2025]] Def. IV.1: $M(v,t)\ge0$ is an AM of $\{v_t\}$ if for some $a_t,b_t\in\mathbb R$
$$\frac{\mathbb E\big(M(v_{t+dt},t+dt)\mid v_t\big)-M(v_t,t)}{dt} \;\le\; a_t M(v_t,t)+b_t .$$
$a_t\equiv0$ gives a $c$-martingale; $a_t,b_t\equiv0$ gives a supermartingale. The AMGF energy function is an AM for general nonlinear stochastic systems, and Doob's inequality then turns its sublevel set into a **probabilistic tube** $\mathcal T=\{(t,y): \|y\|\le r_{\delta,t}\}$ ([[@liuSafetyVerificationNonlinear2025]] Def. III.1).
:::


### Why the AMGF is the right thing to make intrinsic

$\Phi_{n,\lambda}$ is **rotation-invariant and a function of $\|x\|$ alone**. It is already radial and isotropic, so the manifold version is forced rather than invented: replace $\|x\|$ by Riemannian distance $d(\cdot,\cdot)$ and the $S^{n-1}$ average by an average over the unit sphere in $T_xM$. No chart enters the definition at any point.

This is where Phase 1 pays off. Applying $\mathcal L$ to $\Phi_\lambda(d(X_t,\bar x_t))$ needs exactly: $\|\nabla r\|=1$ (Gauss lemma), $\mathrm{Hess}\,r$ (comparison theorems, lesson 08), and the cut locus where $r$ stops being smooth.

### The conservatism being removed

:::warning[Open question]
[[@daniObserverDesignStochastic2015]] Lemma 2 is the closest existing template — rate from contraction, offset from noise intensity, written against a Riemannian metric $M$ and the path-integral squared length $V=\int_0^1(\partial x/\partial\mu)^{T}M(\partial x/\partial\mu)d\mu$:
$$\mathbb E\|a(t)-b(t)\|^2 \le \tfrac1m\Big(\tfrac{C}{2\gamma_1}+\mathbb E[V(0)]e^{-2\gamma_1t}\Big).$$

But its Assumption 1 carries $\bar m_x=\sup_{t,i,j}|\partial M_{ij}/\partial x|$ and $\bar m_{x^2}=\sup_{t,i,j}|\partial^2 M_{ij}/\partial x^2|$ — **sup bounds on derivatives of the metric components in a chart**, which feed the constant $C$. The tube then inflates with how much the chart's metric varies, not with anything intrinsic. That is the conservatism.

**The claim to prove: those metric-derivative bounds should be replaceable by curvature alone** — the intrinsic content of $\partial^2 g$. Whether the resulting constant is genuinely tighter, and on which groups, is the open question.
:::

### Two bounds, both wanted

We are after **both** forms, not one:

| | **A. Mean-squared** | **B. Sup-over-time, high probability** |
|---|---|---|
| Statement | $\mathbb E\,d(X_t,\bar x_t)^2 \le \cdots$ | $\mathbb P\big[\sup_{t\le T} d(X_t,\bar x_t) \le r_{\delta,t}\big]\ge 1-\delta$ |
| Template | [[@daniObserverDesignStochastic2015]] Lemma 2 | [[@liuSafetyVerificationNonlinear2025]] via AMGF |
| Route | generator inequality + Grönwall; Markov/Chebyshev for a probability | affine martingale + Doob/Ville |
| Gives | one time instant, moments only | the whole trajectory at once — an actual tube |

They are not interchangeable and neither subsumes the other. A mean-squared bound plus Markov gives a probability statement **at a fixed $t$**; upgrading it to $\sup_t$ through a union bound or a crude Doob step is exactly the lossy move the AMGF is designed to avoid. Conversely A is cheaper, needs no $\lambda$ to optimize, and is the natural output of a contraction argument — it is the right sanity check on B.

Both tracks share lesson 23 and both terminate in the same comparison (29). **The chart-dependence critique applies identically to both**: Dani's $\bar m_x,\bar m_{x^2}$ sit in track A, but any naive manifold AMGF written in a chart would acquire the same kind of constants.

| # | Lesson | Track | Delivers |
|---|---|---|---|
| 23 | Supermartingales, $c$-martingales, affine martingales; Doob/Ville maximal inequality **vs** the Grönwall + Chebyshev moment route | shared | The two mechanisms for turning a pointwise generator inequality into a bound, and precisely what each costs. [[@liuSafetyVerificationNonlinear2025]] §IV, [[@phamTightEstimatesExit2019]] |
| 24 | Dani's stochastic contraction lemma end to end: Lemma 2, Assumptions 1–2, and exactly where $\bar m_x,\bar m_{x^2}$ enter the constant $C$ | A | The Euclidean mean-squared template, and a precise account of its conservatism |
| 25 | Intrinsic mean-squared bound: replace the path-integral $V$ with geodesic distance; second variation of arc length / index form | A | **Contribution A.** The curvature term arrives through the index form rather than through $\partial^2 M_{ij}$ |
| 26 | Euclidean AMGF: definition, Bessel closed form, rotation invariance, why $\Phi$ beats $e^{\lambda\|X\|}$, sub-Gaussian concentration | B | [[@liuNewProofSubGaussian2025]] end to end. Short and self-contained — do it **before** any manifold version |
| 27 | Set erosion and the probabilistic-tube formulation | B | [[@liuSafetyVerificationStochastic2024a]], [[@liuConcentrationStochasticSystem2026]] — what "tight" means, and the deterministic-trajectory-plus-radius decomposition |
| 28 | Intrinsic AMGF: $\Phi_\lambda(d(x,\bar x))$ with the sphere average in $T_xM$; apply $\mathcal L$ | B | **Contribution B.** Needs Gauss lemma, $\mathrm{Hess}\,r$ comparison (08), the generator (20), cut locus |
| 29 | Curvature vs metric-derivative constants — are the intrinsic bounds actually tighter, in **both** forms? | shared | Settles the thesis. Worked case: $SO(3)$ bi-invariant (positive curvature) vs $SE(3)$ left-invariant. Also: how much does A lose against B on the same system? |
| 30 | Deterministic surrogate for trajectory optimization on a manifold | shared | **Pathway step 6** |

---

## Critical path

Shared trunk: `01 → 02 → 03 → 05 → 07 → 08 → 10 → 19 → 20 → 23`.

Then it forks, and both forks are wanted:

- **Track A** (mean-squared): `23 → 24 → 25`
- **Track B** (sup-$t$ tube): `23 → 26 → 27 → 28`

Both rejoin at **29**, which is the lesson that actually settles the thesis — and it needs *both* branches finished, since half of its content is how much A gives up against B on the same system.

**08** (Hessian comparison, cut locus) is on the trunk and not optional: those are the intrinsic constants meant to replace Dani's $\bar m_x,\bar m_{x^2}$, in **both** tracks. Phase 3 contraction (14–18) is *off* the critical path — it supplies the nominal trajectory the tube is drawn around, so it runs in parallel.

**Order of attack.** Track A first: it is shorter, its template (24) is already in hand, and a working mean-squared bound on $SO(3)$ is the sanity check that makes track B's constants believable. Then B. Within B, 26 is a short self-contained paper and makes 28 writable.

## Housekeeping

- `refs/claude-gen-import/partial-contraction-RG.tex` and `rigid-body-contraction-RG.tex` are byte-identical. Delete one.
- `refs/@simpson-porcoContractionTheoryRiemannian2014a.pdf` is the 2013 preprint of `...2014.pdf` (published, *Systems & Control Letters* **65**). **All result numbers are identical in both**, so citations are unambiguous; keep the published one, the preprint is redundant.
- Six papers now have `refs/@citekey.md` rewrites: Dani, Lee, Simpson-Porco, and the three Liu items (the two tube papers share [[@liuSetErosionTubes]]). Still unread: [[@hsuStochasticAnalysisManifolds2002]] (a book — needs a chapter-scoped pass, not one file), [[@phamTightEstimatesExit2019]], [[@khanMeansRandomVariables2025]], and the trajectory-optimization set.
- The drafts cite real sources not yet in `refs/`: Bullo & Lewis 2004 (*Geometric Control of Mechanical Systems*), Simpson-Porco & Bullo 2013 (*Contraction Theory on Riemannian Manifolds*), Lohmiller & Slotine 1998, Lee & Chirikjian `arXiv:2510.19991`, Kowalski 1971, Musso–Tricerri 1988. The arXiv one is a one-liner: `python tools/fetch.py arxiv 2510.19991 --key leeBrownianMotionLie2025`.
