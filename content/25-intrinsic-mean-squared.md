---
tags: [contribution, mean-squared-bound, stochastic-contraction, curvature, cut-locus, coordinate-free]
---
# Intrinsic Mean-Squared Bound

**Prereq:** [[07-jacobi-equation]], [[08-hessian-comparison]], [[14-contraction-on-manifolds]], [[20-generator-on-manifolds]], [[22-force-vs-configuration-noise]], [[23-martingale-toolkit]], [[24-dani-stochastic-contraction]]; [[notation]].
**Goal:** re-run [[@daniObserverDesignStochastic2015]] Lemma 2 on a manifold with geodesic distance in place of the path integral, and see exactly which of its constants survive as curvature and which vanish.

This is **Contribution A** of [[00-study-plan]] Phase 5, so it is research and not exposition. Every step below is labelled *established* or *conjectural*.

## Setting

:::info[Definition — the comparison system]
$(M,g)$ complete, $\dim M=n$ (the dimension of the manifold the **process** lives on — for a mechanical system on $T^*G$ that is $n=2\dim G$; see [[notation]] § $n$). A deterministic nominal $\dot{\bar x}_t=X(\bar x_t,t)$ and a noisy trajectory
$$dX_t=X(X_t,t)\,dt+\textstyle\sum_{i=1}^d\sigma_i(X_t,t)\,dW^i_t \qquad\text{(Itô, in the sense of [[20-generator-on-manifolds]])},$$
under the standing hypothesis **(H0) $\nabla_{\sigma_i}\sigma_i=0$**, which collapses the drift correction $\tilde X=X+\tfrac12\sum_i\nabla_{\sigma_i}\sigma_i$ to $\tilde X=X$. Write $r(t)=d(X_t,\bar x_t)$ and $\Sigma(x,t)=\sum_i\|\sigma_i(x,t)\|_g^2$.
:::

**(H0) is exactly Case A** of [[22-force-vs-configuration-noise]]: force noise is vertical and fibrewise constant, carried by the flat connection $\mathfrak g^*$ has as a vector space, so it never sees the curvature of the base and **curvature enters at exactly one place — the distance function.** Under Case B the drift acquires a curvature correction and the argument below does not start. (H0) also holds in one Case-B situation used below: left-invariant $\sigma_i=\sigma E_i$ on a **bi-invariant** metric, where $\nabla_{E_i}E_i=\tfrac12[e_i,e_i]=0$. The apparent $-R\,dt$ of lesson 22's $SO(3)$ computation is the second fundamental form of the embedding, not an intrinsic drift.

## Substitution 1 — $V\to r^2$

Dani's energy is $V=\int_0^1(\partial x/\partial\mu)^\top M(\partial x/\partial\mu)\,d\mu$ over *an arbitrary connecting path*, then converted to a statement about $\|a-b\|$ only through $m\|a-b\|^2\le V$. Replace it by
$$V\;\rightsquigarrow\;r(t)^2=d(X_t,\bar x_t)^2 .$$

**Buys:** no arbitrary path (the infimum is taken), no chart, no $m=\inf\lambda_{\min}M$ conversion factor, and the conclusion is about the quantity actually of interest. **Costs:** $r$ is smooth only off $\{\bar x_t\}\cup\mathrm{Cut}(\bar x_t)$, and $r^2$ only on $B(\bar x_t,\mathrm{inj})$ ([[08-hessian-comparison]]). $V$ needed no such hypothesis, because a path integral is defined everywhere.

*Established, and not by us:* [[@phamStochasticContractionRiemannian2013]] already makes exactly this substitution (their §I explicitly criticises Dani for using straight lines rather than geodesics) and obtains $\mathbb E\,d^2_{M(T)}\le C/\lambda+e^{-2\lambda T}[\,\cdot\,]^+$ with $C=\sup\mathrm{tr}(\sigma^\top M\sigma)$ and **no** $\bar m_x,\bar m_{x^2}$ at all. Substitution 1 is therefore literature, not contribution. What is new below is where the curvature went.

## Substitution 2 — apply the generator; curvature replaces $\bar m_{x^2}$

$r^2$ is time-dependent through $\bar x_t$, so Dynkin reads $\tfrac{d}{dt}\mathbb E[r^2]=\mathbb E\big[\partial_t r^2+\mathcal A_t r^2\big]$ with $\mathcal A_tf=X[f]+\tfrac12\sum_i\mathrm{Hess}\,f(\sigma_i,\sigma_i)$ from [[20-generator-on-manifolds]]. The Hessian term is the whole of the curvature dependence. Using $\mathrm{Hess}\,r^2=2r\,\mathrm{Hess}\,r+2\,dr\otimes dr$ and the **lower**-curvature side of the comparison theorem ($\mathrm{Sec}\ge\kappa\Rightarrow\mathrm{Hess}\,r\le\mathrm{ct}_\kappa(r)(g-dr\otimes dr)$, [[08-hessian-comparison]]), off the cut locus:

$$\tfrac12\sum_i\mathrm{Hess}\,r^2(\sigma_i,\sigma_i)\;\le\;\sum_i\Big[r\,\mathrm{ct}_\kappa(r)\big(\|\sigma_i\|^2-\langle\sigma_i,\mathrm{grad}\,r\rangle^2\big)+\langle\sigma_i,\mathrm{grad}\,r\rangle^2\Big]\;\le\;\Sigma\cdot\max\{1,\;r\,\mathrm{ct}_\kappa(r)\}. \tag{$\ast$}$$

The isotropic special case is $\tfrac{\sigma^2}{2}\Delta r^2\le\sigma^2\big((n-1)r\,\mathrm{ct}_\kappa(r)+1\big)$, i.e. lesson 08's $\Delta r^2\le2(n-1)r\,\mathrm{ct}_\kappa(r)+2$. The sign of $\kappa$ decides everything, since $r\,\mathrm{ct}_\kappa(r)\le1\iff\kappa\ge0$:

- $\kappa\ge0$: $(\ast)$ gives $\Sigma$ — **the flat value, with no degradation at all.** Positive curvature strictly helps.
- $\kappa<0$: $\sqrt{|\kappa|}\,r\coth(\sqrt{|\kappa|}\,r)\le1+\sqrt{|\kappa|}\,r$, so $(\ast)\le\Sigma+\Sigma\sqrt{|\kappa|}\,r$, and the second piece **grows linearly in $r$** — it cannot be absorbed into a constant. Young's inequality $\Sigma\sqrt{|\kappa|}\,r\le\varepsilon r^2+\Sigma^2|\kappa|/(4\varepsilon)$ splits it, charging $\varepsilon$ against the rate and $\Sigma^2|\kappa|/(4\varepsilon)$ against the offset.

That $\varepsilon$-split is structurally identical to Dani's — the *same* free parameter appearing in *both* the rate and the constant — but it is driven by $\sqrt{|\kappa|}$ instead of $\bar m_x$, and it disappears identically when $\kappa\ge0$. **This is the intrinsic replacement for $\bar m_{x^2}$, and it is established** (comparison theorem plus Young, no gaps).

## Substitution 3 — contraction, first variation, index form

Dani's Assumption 2 is $(\partial f/\partial x)^\top M+\dot M+M(\partial f/\partial x)\le-2\gamma M$. Intrinsically that *is* [[14-contraction-on-manifolds]]'s $\langle\nabla_wX,w\rangle_g\le-\lambda\|w\|_g^2$, with the $\dot M$ term absorbed into $\nabla$. The drift and the moving centre combine into the **first variation of arc length** along the minimising unit-speed geodesic $\gamma$ from $\bar x_t$ to $X_t$:

$$X[r^2]+\partial_t r^2\;=\;2r\Big(\big\langle\dot\gamma(r),X(X_t,t)\big\rangle-\big\langle\dot\gamma(0),X(\bar x_t,t)\big\rangle\Big)\;=\;2r\int_0^r\!\tfrac{d}{ds}\langle\dot\gamma(s),X\rangle\,ds\;\le\;-2\lambda r^2,$$

the last step being $\tfrac{d}{ds}\langle\dot\gamma,X\rangle=\langle\dot\gamma,\nabla_{\dot\gamma}X\rangle\le-\lambda$ on a unit-speed geodesic lying in the contraction region $\mathcal U$. **So the moving centre is not an extra term — it is the second endpoint of the variation**, and it is handled for free provided $\gamma\subset\mathcal U$ (i.e. $\mathcal U$ geodesically convex, or $1$-reachable in the sense of lesson 14; a general $K$ would put $K^2$ in front of the initial-condition term).

The **second** variation is where $\mathrm{Jac}_v$ of [[07-jacobi-equation]] enters, through the index form $I(u,u)=\int_0^r\big(\|\tfrac{Du}{ds}\|^2-\langle\mathrm{Jac}_{\dot\gamma}u,u\rangle\big)ds$. But note: $\mathrm{Hess}\,r(u,u)=I(J,J)$ for the Jacobi field $J$ matching $u$, and Hessian comparison *is* index-form comparison — so substitutions 2 and 3 draw on **one** curvature object, not two. There is no separate second-variation constant to carry.

And $\bar m_x$? [[08-hessian-comparison]] found it has **no intrinsic counterpart** — $\partial g$ is gauged away in normal coordinates. The claim here is therefore that it should simply *disappear*, not be replaced. [[@phamStochasticContractionRiemannian2013]]'s constant, which has no first-derivative term, is independent evidence that this is right.

## The bound

:::tip[Proposition — intrinsic mean-squared tube]
Assume: **(H1)** $(M,g)$ complete, $\mathrm{Sec}\ge\kappa$ on the region of interest; **(H2)** (H0) holds and $\Sigma=\sum_i\|\sigma_i\|^2\le\bar\Sigma$ uniformly; **(H3)** $(\mathcal U,X,g,\lambda)$ contracting (lesson 14) with $\mathcal U$ geodesically convex and forward $X$-invariant; **(H4)** *confinement:* $X_t,\bar x_t\in\mathcal U$ and $r(t)<\rho<\mathrm{inj}(M)$ for all $t$ considered, with the minimising geodesic unique. Then with a free $\varepsilon>0$ (take $\varepsilon\to0$ when $\kappa\ge0$),
$$\gamma=\lambda-\tfrac{\varepsilon}{2},\qquad C_{\mathrm{noise}}=\bar\Sigma+\frac{\bar\Sigma^2|\kappa|^-}{4\varepsilon}\quad(|\kappa|^-=\max(0,-\kappa)),$$
$$\mathcal A_t r^2+\partial_tr^2\le-2\gamma r^2+C_{\mathrm{noise}}
\quad\Longrightarrow\quad
\boxed{\ \mathbb E\,d(X_t,\bar x_t)^2\;\le\;\frac{C_{\mathrm{noise}}}{2\gamma}+\Big[\mathbb E[d_0^2]-\frac{C_{\mathrm{noise}}}{2\gamma}\Big]^{\!+}e^{-2\gamma t}\ }$$
by [[@daniObserverDesignStochastic2015]] Lemma 3 (the Grönwall comparison lemma, which is manifold-agnostic; see [[23-martingale-toolkit]]). No $\bar m_x$, no $\bar m_{x^2}$, no $m$, no chart.
:::

**Established:** the generator inequality itself — every step of substitutions 2 and 3, under (H1)–(H4). Consistency check: for $\kappa\ge0$ it reads $\mathbb E\,r^2\le\bar\Sigma/(2\lambda)+\cdots$, which is exactly [[@phamStochasticContractionRiemannian2013]] Theorem 2 with their Remark 3.1 halving of $C$ (noisy vs noise-free pair). Two independent routes, same constant.

:::warning[Open question — is (H4) legitimate, or circular?]
(H4) *assumes* what the bound is supposed to establish. Three honest options, none yet carried out here:
1. **Stopping time.** Prove the inequality for $t<\tau_\rho=\inf\{t:r(t)\ge\rho\}$; then Grönwall bounds $\mathbb E[r^2_{t\wedge\tau_\rho}]$ only, and a separate estimate of $\mathbb P[\tau_\rho\le T]$ is needed. That estimate is a $\sup_t$ statement — i.e. it needs **track B**, so track A cannot close itself. This is a real structural finding, not a technicality.
2. **Markov, at a fixed $t$.** $\mathbb P[r(t)\ge\rho]\le\mathbb E[r^2]/\rho^2$ gives a one-time-instant self-consistency check, which is all bound type (a) can ever give (see [../CLAUDE.md](../CLAUDE.md) § The thesis).
3. **Barrier / viscosity.** Past $\mathrm{Cut}(\bar x_t)$, $r$ is semiconcave and its distributional Laplacian has a **non-positive** singular part. Our comparison is an *upper* bound on $\mathrm{Hess}\,r$, so it plausibly survives in the support/barrier sense (Calabi's trick; Kendall's Itô formula for $d$ on manifolds) — while the *contraction* step does not, since the geodesic realising $r$ is no longer unique. **Conjectural.** No source in `refs/` establishes it, and it would need Kendall 1987, which is not fetched.
:::

:::warning[Open question — a possible gap in [[@phamStochasticContractionRiemannian2013]]]
Their Proposition 2 perturbs the connecting geodesic by an **ambient straight line**, $\Gamma_\eta(u)=\Gamma(u)+(1-u)\sigma(a)\eta_1+u\sigma(b)\eta_2$, and then discards the cross term $2\int(\sigma(b)\eta_2-\sigma(a)\eta_1)^\top M\,\partial_u\Gamma\,du$ as mean-zero. But $M$ is evaluated along $\Gamma_\eta$, which itself depends on $\eta$ — so the term is not obviously centred. In intrinsic language their step asserts $\mathrm{Hess}\,r^2\le2g$, which by $(\ast)$ is true **iff $\mathrm{Sec}\ge0$**. Provisional read: their curvature-free constant is correct in non-negative curvature and *understates* the noise term when $\mathrm{Sec}<0$, where $(\ast)$ grows linearly in $r$. Verify against the published version before relying on this; it is a reading of a `pdftotext` extraction.
:::

## Worked example — $SO(3)$, bi-invariant metric

Attitude kinematics only, $M=SO(3)$ (**not** $T^*SO(3)$ — see the caveat below). $\mathbb J=I$, so $\mathrm{Sec}\equiv\tfrac14$ ([[06-curvature-left-invariant-metrics]]), $n=3$, $\mathrm{inj}=\pi$, $d(I,R)=$ rotation angle ([[08-hessian-comparison]]). Take $\kappa=\tfrac14>0$: the $\varepsilon$-split vanishes, $\gamma=\lambda$ exactly. Isotropic left-invariant noise $\sigma_i=\sigma E_i$ satisfies (H0) by bi-invariance and gives $\bar\Sigma=3\sigma^2$. With $\lambda=2\,\mathrm{s^{-1}}$ and $\sigma=0.1\,\mathrm{rad\,s^{-1/2}}$:

$$\gamma=2\,\mathrm{s^{-1}},\qquad C_{\mathrm{noise}}=3(0.1)^2=0.03\,\mathrm{rad^2\,s^{-1}},\qquad \lim_{t\to\infty}\mathbb E\,r^2\le\frac{0.03}{4}=7.5\times10^{-3}\,\mathrm{rad^2},$$

i.e. RMS angular error $\le0.0866\,\mathrm{rad}=4.96^\circ$. **Radius of validity:** (H4) needs $\rho<\mathrm{inj}=\pi$; Markov at fixed $t$ gives $\mathbb P[r(t)\ge\pi]\le7.5\times10^{-3}/\pi^2=7.6\times10^{-4}$. Sharper: to certify $\rho=\pi/2$ (well inside the injectivity radius, and where lesson 08 computed $\Delta r^2=\pi+2<6$) requires $\mathbb E r^2/\rho^2=3.0\times10^{-3}$, so noise up to $\sigma\approx0.63\,\mathrm{rad\,s^{-1/2}}$ still keeps the fixed-$t$ violation probability under $12\%$. The $\sup_t$ version of that statement is exactly what lesson 28 must supply.

Note what did *not* appear: any sup-norm of $\partial g_{ij}$ or $\partial^2g_{ij}$ in exponential coordinates on $SO(3)$ — both are nonzero there and both would have eaten into $\gamma$ in Dani's Lemma 2. Quantifying that gap is lesson 29's job, not this one.

:::warning[Open question — the honest mechanical case is worse than this]
The example above is a *kinematic* attitude system, so the process lives on $SO(3)$ and the certifying metric is the bi-invariant one. A genuine mechanical system lives on $T^*SO(3)$, $n=6$, and then (H1) is a curvature bound for the **certifying metric of lesson 16** (with its position–velocity cross terms), not for $\mathbb G$ — a metric whose sectional curvatures nobody has computed, and which lesson 13's Sasaki formulas do not cover. Worse, [[22-force-vs-configuration-noise]]'s degeneracy warning applies: force noise has zero base block, so $\Sigma$ counts only fibre directions and the diffusion is hypoelliptic. The Proposition remains formally valid — a degenerate $\sigma$ only shrinks $\bar\Sigma$ — but whether $\kappa$ for that metric is anywhere near $\tfrac14$, or even non-negative, is open. Do not read the $4.96^\circ$ above as a rigid-body result.
:::

## Ledger

| Dani (chart) | here |
|---|---|
| $V$, path integral over an arbitrary path | $r^2=d(X_t,\bar x_t)^2$ |
| $m=\inf\lambda_{\min}M$ | gone — the bound is already in $d$ |
| $\bar m_x$ | **gone** (no intrinsic counterpart) |
| $\bar m_{x^2}$ | $\mathrm{Sec}\ge\kappa$, via $(\ast)$; inert when $\kappa\ge0$ |
| $C_1+C_2$ | $\bar\Sigma=\sum_i\|\sigma_i\|^2$ |
| $\varepsilon$-split (always present) | $\varepsilon$-split **only if $\kappa<0$** |
| — (silently assumed) | $\mathrm{inj}(M)$, and (H4) |

## Problems

1. **Recall.** State the three substitutions and, for each, one thing it buys and one thing it costs. Then say why $\bar m_x$ is claimed to vanish rather than to be replaced, and what would have to be true for that claim to be wrong.

2. **Compute.** On the model space $M^n_\kappa$ with isotropic noise $\sigma_i=\sigma E_i$ ($\{E_i\}$ orthonormal), compute $\mathcal A\,r^2$ exactly (not as an inequality) for $\kappa>0$, $\kappa=0$, $\kappa<0$, taking $X\equiv0$. For $\kappa<0$, find the value of $r$ at which the noise term is twice its Euclidean value.

3. **Prove.** Show the Proposition specialises at $\kappa=0$, $M=\mathbb R^n$ to $\mathbb E\|X_t-\bar x_t\|^2\le\bar\Sigma/(2\lambda)+[\cdot]^+e^{-2\lambda t}$, and check this against [[@daniObserverDesignStochastic2015]] Lemma 2 with $M=I$ (so $m=1$, $\bar m_x=\bar m_{x^2}=0$, $\beta_2=0$).

4. **Break it.** On $SO(3)$ (bi-invariant, $\mathrm{inj}=\pi$), suppose the process reaches $\mathrm{Cut}(\bar x_t)$, the set of rotations at angle $\pi$ from $\bar x_t$. (a) Which hypothesis of the Hessian comparison theorem fails, and what does $r$ look like there? (b) Give two *independent* reasons the Proposition cannot simply be extended to $\rho>\mathrm{inj}$ — one about $r$, one about $\mathcal U$. (c) Why is a bound with $C_{\mathrm{noise}}/2\gamma>\pi^2$ vacuous on $SO(3)$?

---

## Solutions

**1.** (i) $V\to r^2$: buys the elimination of the arbitrary path, the chart and the factor $1/m$; costs smoothness — $r^2$ is smooth only inside $\mathrm{inj}$. (ii) Generator + Hessian comparison: buys a curvature-only constant that is *sharp* (equality in the model spaces); costs the requirement of a two-sided-usable curvature bound and $x\notin\mathrm{Cut}$. (iii) Contraction via first variation: buys the moving centre for free (it is the other endpoint of the variation) and unifies the second-variation curvature with (ii) through the index form; costs geodesic convexity of $\mathcal U$ (or a factor $K^2$). $\bar m_x$ vanishes because $\partial g$ at a point is pure gauge — normal coordinates set it to zero — so no chart-independent quantity can dominate it. The claim would be wrong if the correct intrinsic estimate needed $\partial g$ *along a curve* rather than at a point, i.e. if some genuinely non-tensorial holonomy-type object entered; nothing in the derivation above produces one.

**2.** With $X=0$ and $\{E_i\}$ orthonormal, $\mathcal A r^2=\tfrac{\sigma^2}{2}\Delta r^2=\sigma^2\big((n-1)r\,\mathrm{ct}_\kappa(r)+1\big)$, and on the model spaces this is an **equality** (lesson 08 computes $\mathrm{Hess}\,r=\mathrm{ct}_\kappa(r)(g-dr\otimes dr)$ there exactly). So
$$\kappa>0:\ \sigma^2\big((n-1)\sqrt\kappa\,r\cot(\sqrt\kappa r)+1\big);\quad \kappa=0:\ \sigma^2 n;\quad \kappa<0:\ \sigma^2\big((n-1)\sqrt{|\kappa|}\,r\coth(\sqrt{|\kappa|}r)+1\big).$$
Positive curvature strictly reduces it (and drives it to $\sigma^2$ as $r\to\pi/\sqrt\kappa$); negative curvature increases it without bound, growing like $\sigma^2(n-1)\sqrt{|\kappa|}\,r$. Setting the $\kappa<0$ value to $2\sigma^2n$: need $(n-1)z\coth z=2n-1$ with $z=\sqrt{|\kappa|}r$; for large $z$, $\coth z\to1$, so $z\approx(2n-1)/(n-1)$, i.e. $r\approx\frac{2n-1}{(n-1)\sqrt{|\kappa|}}$ (for $n=3$, $z\approx2.5$, and $z\coth z=2.5$ at $z\approx2.49$ — the approximation is already good).

**3.** $\kappa=0$: $r\,\mathrm{ct}_0(r)=1$ identically, so $(\ast)$ gives exactly $\bar\Sigma$, $|\kappa|^-=0$, hence $\varepsilon\to0$, $\gamma=\lambda$, $C_{\mathrm{noise}}=\bar\Sigma$, and $\mathrm{Hess}\,r^2=2g$ everywhere (lesson 08, problem 3b) so no cut-locus restriction survives — $\mathrm{inj}(\mathbb R^n)=\infty$. The bound is $\mathbb E\|X_t-\bar x_t\|^2\le\bar\Sigma/(2\lambda)+[\cdot]^+e^{-2\lambda t}$. Dani with $M=I$: $m=1$, $\bar m_x=\bar m_{x^2}=0$ so $\gamma_1=\gamma=\lambda$; $\beta_2=0$ (nominal is noiseless) so $C=C_1=\mathrm{tr}(B_1^\top B_1)=\sum_i\|\sigma_i\|^2=\bar\Sigma$; and $V(0)=\|x_0-\bar x_0\|^2$. Identical. The two bounds are the *same theorem* whenever the metric is flat and constant — which is Dani's own Remark 1, and confirms that everything the intrinsic version does is confined to the curved case.

**4.** (a) The hypothesis $x\notin\mathrm{Cut}(\bar x_t)$. At an angle-$\pi$ rotation an $\mathbb{RP}^2$'s worth of minimising geodesics arrive from $\bar x_t$ (lesson 08), $\mathrm{grad}\,r$ has no limit, and $r$ has a concave corner — $r$ attains its maximum $\pi$ there, so a smooth $r$ would need $\mathrm{grad}\,r=0$, contradicting $\|\mathrm{grad}\,r\|=1$. $\mathrm{Hess}\,r$ does not exist and the comparison inequality has no content. (b) First, about $r$: $\mathcal A r^2$ is undefined on $\mathrm{Cut}$, so the generator inequality — the *only* input to Grönwall — is not available; at best one gets a distributional/barrier statement, which is conjectural (see the open-question callout). Second, about $\mathcal U$: a contraction region is contractible (lesson 17), so no contracting $\mathcal U$ can be all of $SO(3)\cong\mathbb{RP}^3$; substitution 3 needs the connecting geodesic to lie in $\mathcal U$, and once $\rho>\mathrm{inj}$ the minimiser is neither unique nor guaranteed to stay in $\mathcal U$. These are genuinely independent: the first would still bite on a contractible manifold with small injectivity radius (the flat torus of lesson 08 problem 4b), the second would still bite on a manifold with $\mathrm{inj}=\infty$. (c) $\mathrm{diam}(SO(3))=\pi$, so $r\le\pi$ and $\mathbb E r^2\le\pi^2$ holds trivially with no hypotheses at all. Any certified bound exceeding $\pi^2$ carries zero information — which is the compact-manifold analogue of Dani's bound going vacuous when $(\beta_1^2+\beta_2^2)(\varepsilon\bar m_x+\bar m_{x^2}/2)\ge2m\gamma$, and a reminder that on a compact group the interesting regime is $C_{\mathrm{noise}}/2\gamma\ll\mathrm{inj}^2$.
