---
tags: [brownian-motion, stochastics, lie-groups, riemannian-geometry, mean-curvature]
---
# Brownian Motion on a Manifold and on a Lie Group

**Prereq:** [[19-ito-vs-stratonovich]], [[20-generator-on-manifolds]], [[03-levi-civita-left-invariant]], [[04-unimodularity]], [[riemannian-geometry]] (orthonormal frames, parallel transport)
**Goal:** write down Brownian motion on $M$, on $G$, and on an embedded $G$, and say exactly why the *same* process carries drift $0$ in one description and $\tfrac12H$ in another.

Everything here is [[@leeGeometricInterpretationBrownian2025]], reorganised. Its numbering is used: Thm 4 (manifold), Thm 5 (Lie group), Cor 1 (unimodular), Thm 7 (embedded).

*Symbol clash.* $\Delta$ is Laplace–Beltrami throughout, per [[notation]]. The $\Delta$ of [[04-unimodularity]] is the modular function; the two never appear together, and only the modular *statement* $\Delta\equiv1$ is imported.

## The definition

:::info[Definition — Brownian motion]
Brownian motion on a Riemannian manifold $(M,\mathbb G)$ is the diffusion whose generator is $\tfrac12\Delta$, $\Delta=\mathrm{div}\circ\mathrm{grad}$ the Laplace–Beltrami operator. That is the **only** axiom. Every SDE below is reverse-engineered from it, using the generator formula of [[20-generator-on-manifolds]].
:::

There is no "$dW$ on a manifold" to write down directly — $M$ has no linear structure to add increments in. So one injects unit-intensity scalar noise along each leg of an orthonormal frame $\{E_i\}_{i=1}^n$ and then *solves for the drift* that makes the generator come out to $\tfrac12\Delta$. The frame formula
$$\Delta f=\sum_i\big(E_i[E_i[f]]-(\nabla_{E_i}E_i)[f]\big)=\sum_i\mathrm{Hess}_f(E_i,E_i)$$
([[@leeGeometricInterpretationBrownian2025]] Prop. 1, eqs. 35–36) is frame-independent, so the answer does not depend on which orthonormal frame is chosen.

:::tip[Theorem 4 — Brownian motion on a manifold]
For an orthonormal frame $\{E_i\}_{i=1}^n$ on $M$,
$$dx=-\tfrac12\sum_i\nabla_{E_i}E_i\,dt+\sum_iE_i\circ dW_i
\qquad\Longleftrightarrow\qquad
dx=\sum_iE_i\,dW_i,$$
and both have generator $\tfrac12\Delta$. ([[@leeGeometricInterpretationBrownian2025]] eqs. 39–40.)
:::

*Why.* Itô–Stratonovich conversion on $M$ ([[19-ito-vs-stratonovich]], [[20-generator-on-manifolds]]) is $\tilde X=X+\tfrac12\sum_i\nabla_{\sigma_i}\sigma_i$. With $\sigma_i=E_i$ the Stratonovich drift $-\tfrac12\sum_i\nabla_{E_i}E_i$ is exactly minus the correction, so the Itô drift is $0$. Feeding $X=-\tfrac12\sum\nabla_{E_i}E_i$ into $\mathcal Af=X[f]+\tfrac12\sum_i E_i[E_i[f]]$ reproduces the frame formula above. $\square$

Read the two forms as a statement about the frame: **the Stratonovich drift measures the failure of $\{E_i\}$ to be parallel.** A parallel frame ($\nabla_{E_i}E_i=0$) makes both forms driftless; a non-parallel one does not. The Itô form is driftless *whatever the frame*, because $\nabla$ has been used to write it — that is the whole content of "written intrinsically".

## On a Lie group

Take $G$ with a left-invariant metric $\mathbb G$ built from $\langle\cdot,\cdot\rangle_{\mathbb I}$, and the left-translated frame $E_i(g)=ge_i$ with $\{e_i\}$ orthonormal in $\mathfrak g$. This frame is **global** — the reason Lie groups dodge the "orthonormal frames are only local" problem. Lesson [[03-levi-civita-left-invariant]] gives $\nabla_\xi\xi=-\widetilde{\mathrm{ad}}_\xi\xi$, hence $\nabla_{E_i}E_i=-g\,\widetilde{\mathrm{ad}}_{e_i}e_i$.

:::tip[Theorem 5 — Brownian motion on a Lie group]
$$g^{-1}dg=\tfrac12\sum_i\widetilde{\mathrm{ad}}_{e_i}e_i\,dt+\sum_ie_i\circ dW_i
\qquad\Longleftrightarrow\qquad
g^{-1}dg=\sum_ie_i\,dW_i,$$
both with generator $\tfrac12\Delta$. ([[@leeGeometricInterpretationBrownian2025]] eqs. 45–46, via eq. 48.) The Stratonovich drift is $\tfrac12J$ with $J=\sum_i\widetilde{\mathrm{ad}}_{e_i}e_i$, the adjoint-trace vector of [[04-unimodularity]].
:::

**Type discipline.** The source writes $\sum_i\mathrm{ad}^*_{e_i}e_i$ because it has already identified $\mathfrak g^*\cong\mathfrak g$ through $\langle\cdot,\cdot\rangle_{\mathbb I}$. As written that does not type-check: $\mathrm{ad}^*_\xi:\mathfrak g^*\to\mathfrak g^*$. The honest object is $\widetilde{\mathrm{ad}}_{e_i}e_i=\mathbb I^{-1}\mathrm{ad}^*_{e_i}(\mathbb I e_i)$ — see [[notation]]. This matters here and not merely notationally: $\chi=-\mathrm{tr}\,\mathrm{ad}\in\mathfrak g^*$ is metric-free, $J=\mathbb I^{-1}\chi$ is not, so *whether* the drift vanishes is intrinsic while its *size* is a metric choice.

:::tip[Corollary 1 — unimodular groups]
$G$ unimodular $\Rightarrow J=0$ $\Rightarrow$ the Stratonovich form collapses to $g^{-1}dg=\sum_ie_i\circ dW_i$ ([[@leeGeometricInterpretationBrownian2025]] eq. 49).
:::

This is the payoff [[04-unimodularity]] promised: $\langle J,\eta\rangle_{\mathbb I}=-\mathrm{tr}\,\mathrm{ad}_\eta$, so $\mathrm{tr}\,\mathrm{ad}=0$ deletes the drift. $SO(3)$ and $SE(3)$ are both unimodular, so on both, "isotropic left-invariant Stratonovich noise" *is* Brownian motion, with nothing to correct. $\mathrm{Aff}(\mathbb R)$ is not (Problem 4).

## Embedded: where the pinning drift comes from

Now put $M^n\subset\mathbb R^{\bar n}$, let $P(x)$ be orthogonal projection onto $T_xM$, and use the **pseudo-frame** $\{P(x)e_i\}_{i=1}^{\bar n}$ built from the ambient standard basis — redundant and non-orthonormal, but globally defined, and it computes traces correctly.

:::tip[Theorem 7 — embedded case]
$$dx=-\tfrac12\sum_{i=1}^{\bar n}\nabla_{Pe_i}Pe_i\,dt+\sum_{i=1}^{\bar n}Pe_i\circ dW_i
\qquad\Longleftrightarrow\qquad
dx=\tfrac12H\,dt+\sum_{i=1}^{\bar n}Pe_i\,dW_i,$$
$H=\sum_i\mathrm{II}(E_i,E_i)$ the mean curvature vector (no $1/n$ — [[notation]]). Both have generator $\tfrac12\Delta$. ([[@leeGeometricInterpretationBrownian2025]] eqs. 64–65; $\bar n$ Wiener processes are needed.)
:::

$H$ is normal-valued, so $\tfrac12H$ is **purely normal to $M$**. It therefore annihilates any function that is constant along the normal directions (Problem 3), and cannot enter the generator on intrinsic observables. What it does instead is exactly what a constraint force does: an ambient Itô integrator takes straight steps, which leave $M$ at second order, and $\tfrac12H\,dt$ is the second-order correction that pins the path back. Curvature of the embedding is the amount of pinning required.

## Worked example — $SO(3)$

Frame $E_i(R)=R\hat e_i$; inner product $\langle\eta,\zeta\rangle=\tfrac12\mathrm{tr}(\eta^\top\zeta)$ so that $\{\hat e_i\}$ is orthonormal ([[notation]]). $SO(3)$ is compact hence unimodular, and this metric is bi-invariant, so $\nabla_{E_i}E_i=0$ and Cor. 1 gives the **drift-free Stratonovich** form
$$dR=\sum_{i=1}^3R\hat e_i\circ dW_i.$$

**(i) Ambient Itô form via $H$.** Extend $E_i$ to $\bar E_i(X)=X\hat e_i$, linear on $\mathbb R^{3\times3}$; the flat ambient derivative in direction $X\hat e_i$ is $\bar\nabla_{\bar E_i}\bar E_i=X\hat e_i^2$. Since $\nabla_{E_i}E_i=0$, the Gauss formula gives $\mathrm{II}(E_i,E_i)=R\hat e_i^2$ outright, and with $\hat a^2=aa^\top-|a|^2I$,
$$\sum_{i=1}^3\hat e_i^2=\sum_i\big(e_ie_i^\top-I\big)=I-3I=-2I
\quad\Longrightarrow\quad H=R\sum_i\hat e_i^2=-2R .$$
Each $R\hat e_i^2$ has symmetric right factor, so $H\in R\cdot\mathrm{Sym}(3)$: normal, as required. Then Thm 7 reads
$$\boxed{\ dR=-R\,dt+\sum_{i=1}^3R\hat e_i\,dW_i\ }$$
([[@leeGeometricInterpretationBrownian2025]] §V-F, eqs. 104–105 — **not** Corollary 2, which is the general embedded-unimodular statement.) The $-2$ is locked to the $\tfrac12\mathrm{tr}$ scaling: under the plain Frobenius metric the orthonormal frame is $R\hat e_i/\sqrt2$ and $H=-R$.

**(ii) Independent check — the constraint.** Postulate $dR=A\,dt+\sum_iR\hat e_i\,dW_i$ and demand $d(R^\top R)=0$ in Itô calculus. The product rule keeps the quadratic term:
$$d(R^\top R)=(dR)^\top R+R^\top dR+(dR)^\top(dR).$$
Noise part: $\sum_i(\hat e_i^\top R^\top R+R^\top R\hat e_i)dW_i=\sum_i(-\hat e_i+\hat e_i)dW_i=0$ — the noise respects the constraint on its own. Quadratic part: $\sum_i\hat e_i^\top R^\top R\hat e_i\,dt=-\sum_i\hat e_i^2\,dt=2I\,dt$. So
$$A^\top R+R^\top A+2I=0,\qquad A=-R:\quad -I-I+2I=0.\ \checkmark$$

:::tip[Verification outcome — Phase 4 *verify* task]
Both computations agree, and they agree for a reason worth stating. The constraint fixes only $\mathrm{sym}(R^\top A)=-I$, i.e. the **normal** part of the drift — which is precisely $\tfrac12H=-R$. Any tangential addition $R\Omega$, $\Omega$ skew, still satisfies $d(R^\top R)=0$; it is ruled out separately by demanding the generator be $\tfrac12\Delta$, which is what Cor. 1 supplies. So "$\tfrac12H$ is the pinning drift" is not a coincidence of $SO(3)$: staying on $M$ determines the normal drift, and being Brownian determines the tangential one.
:::

## The standing question

The same process — one law, one generator $\tfrac12\Delta$ — has Itô drift $0$ written intrinsically (Thm 4) and $\tfrac12H$ written in the ambient space (Thm 7); Stratonovich drift $0$ on $SO(3)$ (Cor. 1) and $\tfrac12J\ne0$ on $\mathrm{Aff}(\mathbb R)$. **The drift is representation-dependent; the generator is not.** In the standing-question classification: $\Delta$, $H$, $J=0$-or-not are class 1 (intrinsic); the drift *value* is class 2 (chart- or embedding-dependent but provably consistent, since all descriptions share a generator); $\|J\|_{\mathbb I}$ on a non-unimodular group is the first thing here that risks class 3, because it enters a bound and depends on $\mathbb I$.

This is the mechanism of [[19-ito-vs-stratonovich]] made geometric — the non-tensorial $\tfrac12\partial^2\phi(\sigma\sigma^\top)$ term reappears as $\nabla_{E_i}E_i$, as $\widetilde{\mathrm{ad}}_{e_i}e_i$, and as $\mathrm{II}(E_i,E_i)$ in the three settings. Lesson 22 uses exactly this to separate force noise (quadratic variation in the flat fibre, no correction) from configuration noise (quadratic variation in the curved base).

:::warning[Open question]
Thm 4's frame is generally only local, and Thm 7's escape costs $\bar n$ Wiener processes for an $n$-dimensional manifold. Neither is a problem for a tube bound, since only the generator is used — but any *simulation* check of a tube inherits the choice, and the $\bar n$-noise construction is not the same pathwise process as an $n$-noise intrinsic one. Whether the tube estimates in Phase 5 should be validated against a Stratonovich intrinsic scheme or an ambient projected one is unsettled.
:::

## Problems

1. **Recall.** State the definition of Brownian motion on $(M,\mathbb G)$ and both forms of Thm 4 from memory. Then answer: which term vanishes if the frame is parallel, and which vanishes regardless of frame? Classify the drift of each of Thms 4, 5, 7 as intrinsic / representation-dependent.

2. **Compute.** (a) Prove $\sum_{i=1}^3\hat e_i^2=-2I$ from $\hat a\hat b=ba^\top-(a^\top b)I$. (b) With $dR=A\,dt+\sum_iR\hat e_i\,dW_i$, run the Itô computation of $d(R^\top R)$ and solve for $A$'s normal part. Which part of $A$ does the constraint leave undetermined, and what determines it?

3. **Prove.** Let $M\subset\mathbb R^{\bar n}$ and let $b(x)\perp T_xM$ for every $x$. Show that adding $b\,dt$ to an ambient Itô SDE changes nothing about the generator acting on intrinsic observables. (Take $\bar f=f\circ\pi$ with $\pi$ nearest-point projection, defined on a tubular neighbourhood.) Deduce Remark 5: $\tfrac12H$ in Thm 7 is invisible to $\mathcal A$.

4. **Break it.** On $\mathrm{Aff}(\mathbb R)$, $[E_1,E_2]=E_2$ with $\{E_1,E_2\}$ declared orthonormal, [[04-unimodularity]] computed $J=-E_1$. Suppose someone writes down $g^{-1}dg=\sum_iE_i\circ dW_i$ and calls it Brownian motion. (a) Compute its Itô drift. (b) Compute its generator. (c) Say precisely what it is instead, and what breaks in a tube estimate that assumed $\mathcal A=\tfrac12\Delta$.

---

## Solutions

**1.** Brownian motion = the diffusion with generator $\tfrac12\Delta$. Thm 4: $dx=-\tfrac12\sum_i\nabla_{E_i}E_i\,dt+\sum_iE_i\circ dW_i\iff dx=\sum_iE_i\,dW_i$. The Stratonovich drift vanishes iff the frame is parallel; the Itô drift vanishes for every orthonormal frame. Classification: Thm 4's Itô drift $0$ and Thm 5's $J=0$-or-not are intrinsic statements; the *values* $-\tfrac12\sum\nabla_{E_i}E_i$, $\tfrac12J$, $\tfrac12H$ are representation-dependent — frame, metric-identification, and embedding respectively. All three descriptions share the generator, which is the invariant.

**2.** (a) Setting $b=a$: $\hat a^2=aa^\top-|a|^2I$, so $\sum_i\hat e_i^2=\sum_ie_ie_i^\top-\sum_i I=I-3I=-2I$.
(b) $d(R^\top R)=(dR)^\top R+R^\top dR+(dR)^\top dR$. The $dW_i$ coefficient is $\hat e_i^\top R^\top R+R^\top R\hat e_i=-\hat e_i+\hat e_i=0$. The quadratic term is $\sum_i\hat e_i^\top\hat e_i\,dt=-\sum_i\hat e_i^2\,dt=2I\,dt$. Hence $A^\top R+R^\top A=-2I$, i.e. $\mathrm{sym}(R^\top A)=-I$, so $R^\top A=-I+\Omega$ with $\Omega$ arbitrary skew: the constraint fixes only the normal part $A_\perp=-R=\tfrac12H$. The tangential part $R\Omega$ is fixed to zero by requiring the generator equal $\tfrac12\Delta$ — Cor. 1, unimodularity.

**3.** For $f\in C^\infty(M)$ put $\bar f=f\circ\pi$; then $\bar f$ is constant along each normal fibre, so $d\bar f_x(v)=0$ for every $v\perp T_xM$. The added drift contributes $b(x)[\bar f]=d\bar f_x(b(x))=0$ to $\mathcal A\bar f$, and the diffusion term is untouched since $b$ enters no quadratic variation. So $\mathcal A$ agrees on all such $\bar f$, i.e. on all intrinsic observables. Applying this with $b=\tfrac12H$, which is normal-valued because $\mathrm{II}$ is, gives Remark 5: Thm 7's Itô drift does not affect the generator, even though it is essential for the sample path to remain on $M$.

**4.** (a) By Itô–Stratonovich conversion, $\tilde X=0+\tfrac12\sum_i\nabla_{E_i}E_i=-\tfrac12gJ=+\tfrac12gE_1$. So the Itô form is $g^{-1}dg=\tfrac12E_1\,dt+\sum_iE_i\,dW_i$ — not driftless, unlike Thm 4.
(b) With Stratonovich drift $X=0$ and $\sigma_i=E_i$, $\mathcal Af=\tfrac12\sum_iE_i[E_i[f]]$. Using the frame formula, $\sum_iE_i[E_i[f]]=\Delta f+\sum_i(\nabla_{E_i}E_i)[f]=\Delta f-(gJ)[f]=\Delta f+E_1[f]$. Hence
$$\mathcal A=\tfrac12\Delta+\tfrac12E_1\ \neq\ \tfrac12\Delta .$$
(c) It is Brownian motion *plus a deterministic left-invariant transport* at velocity $\tfrac12E_1$: integrating $\dot g=g(\tfrac12E_1)$ in coordinates $g=(a,b)$ gives $\dot a=a/2$, $\dot b=0$, so $a_t=a_0e^{t/2}$. The correct Brownian motion on $\mathrm{Aff}(\mathbb R)$ carries the *opposite* drift $\tfrac12J=-\tfrac12E_1$ (Thm 5); writing the driftless Stratonovich equation therefore misses the true motion by $E_1$, twice the drift, not zero. In a tube estimate the damage is first-order: the centre of the law separates from the nominal trajectory linearly in $t$, on top of the $\sqrt t$ spread, so a bound derived from $\mathcal A=\tfrac12\Delta$ is not merely loose — it is wrong. Unimodularity is exactly the hypothesis that licenses dropping the term, and it fails here.
