---
tags: [stochastics, generator, sde, ito-stratonovich, manifolds, foundations]
---
# The Generator of a Diffusion on a Manifold

**Prereq:** [[19-ito-vs-stratonovich]] (quadratic variation, the non-tensorial Itô correction), [[08-hessian-comparison]] ($\mathrm{Hess}$, $\Delta$, $r=d(p,\cdot)$), [[03-levi-civita-left-invariant]] ($\nabla$ on a left-invariant metric), [[probability-on-manifolds]] (backward Kolmogorov), [[notation]].
**Goal:** write down the generator $\mathcal A$ of an SDE on $M$ in both Stratonovich and Itô form, prove the two agree, and know why $\mathcal A$ — not the drift — is the invariant of the diffusion.

This is **pathway step 3**. Everything in Phase 5 is "apply $\mathcal A$ to a function of $d(X_t,\bar x_t)$"; this lesson is the licence to do that coordinate-free.

## The equation

:::info[Definition — Stratonovich SDE on a manifold]
Let $X,\sigma_1,\dots,\sigma_m\in\mathfrak X(M)$ be smooth vector fields and $W_1,\dots,W_m$ independent scalar Wiener processes. The Stratonovich SDE is
$$dx=X(x)\,dt+\sum_{i=1}^m\sigma_i(x)\circ dW_i .$$
:::

Nothing here needs a chart. Both $dt$ and $\circ\,dW_i$ multiply genuine vector fields, and Stratonovich calculus obeys the ordinary chain rule ([[19-ito-vs-stratonovich]]), so pushing the equation through a diffeomorphism $\phi$ just pushes forward $X$ and the $\sigma_i$. **The Stratonovich form is the geometric one and is where every SDE in this project is written.** The Itô form is derived from it, never posited.

## Itô–Stratonovich on a manifold

:::tip[Theorem 1 — Itô–Stratonovich conversion, [[@leeGeometricInterpretationBrownian2025]] Thm 1, eq. (22)]
The Stratonovich SDE above is equivalent to the Itô SDE $dx=\tilde X(x)\,dt+\sum_i\sigma_i(x)\,dW_i$ with
$$\tilde X=X+\frac12\sum_{i=1}^m\nabla_{\sigma_i}\sigma_i ,$$
$\nabla$ the Levi-Civita connection of the metric.
:::

The correction is a **covariant** derivative, and that is the whole content. In a chart,
$$(\nabla_{\sigma}\sigma)^k=\sigma^j\partial_j\sigma^k+\Gamma^k_{ij}\sigma^i\sigma^j .$$
The first term is precisely lesson 19's Euclidean correction — the $\tfrac12\partial^2\phi\,(\sigma\sigma^\top)$ term seen from the other side, $\tfrac12\sigma\sigma'$ in one dimension. **Neither term is tensorial on its own**: under a change of chart $\sigma^j\partial_j\sigma^k$ picks up a second-derivative-of-transition term, and $\Gamma^k_{ij}\sigma^i\sigma^j$ picks up exactly its negative. The sum is a vector field. So the Christoffel part is not decoration: it is what turns lesson 19's chart artifact into a geometric object.

Consequently $\tilde X$ *is* a vector field — but only once a connection has been supplied. Writing $dx^k=b^k\,dt+\sigma^k_i\,dW_i$ in a chart and calling $b$ "the drift" defines nothing intrinsic; $b$ does not transform as a vector.

## The generator

:::info[Definition — generator]
$$\mathcal Af(x)=\lim_{t\downarrow0}\frac{\mathbb E\big[f(x_t)\mid x_0=x\big]-f(x)}{t},\qquad f\in C^\infty(M).$$
$\mathcal A$ and the $\mathcal L$ of [[19-ito-vs-stratonovich]] are the same operator; [[notation]] allows either symbol, and $\mathcal A$ is used from here on to match [[@leeGeometricInterpretationBrownian2025]].
:::

:::tip[Theorem 2 — generator of an SDE on a manifold, [[@leeGeometricInterpretationBrownian2025]] Thm 2, eqs. (26)–(28)]
$$\mathcal Af=X[f]+\frac12\sum_{i=1}^m\sigma_i\big[\sigma_i[f]\big]
\;=\;\tilde X[f]+\frac12\sum_{i=1}^m\mathrm{Hess}_f(\sigma_i,\sigma_i),$$
where $\mathrm{Hess}_f(Y,Z)=Y\big[Z[f]\big]-(\nabla_YZ)[f]$ is the Hessian of [[08-hessian-comparison]] and $Y[f]=df(Y)$.
:::

The two forms agree in one line. By Theorem 1, $\tilde X[f]=X[f]+\tfrac12\sum_i(\nabla_{\sigma_i}\sigma_i)[f]$, and by the definition of $\mathrm{Hess}$, $\tfrac12\sum_i\mathrm{Hess}_f(\sigma_i,\sigma_i)=\tfrac12\sum_i\sigma_i[\sigma_i[f]]-\tfrac12\sum_i(\nabla_{\sigma_i}\sigma_i)[f]$. **The $\nabla_{\sigma_i}\sigma_i$ terms cancel** — the drift correction adds exactly what the Hessian subtracts. Note the first form has no $\nabla$ in it at all: $\sigma_i[\sigma_i[f]]$ is iterated directional differentiation, defined on any smooth manifold. The connection enters only when you insist on splitting $\mathcal A$ into "drift" and "second-order" pieces, and the split is what depends on it.

## The point

:::tip[The generator is the invariant — [[@leeGeometricInterpretationBrownian2025]] §II-C and Remark 1]
A single diffusion admits many SDE descriptions — different charts, Itô versus Stratonovich, different frames — but **two SDEs define the same process in law iff they have the same generator**. $\mathcal A$ is a genuine invariant of the diffusion; no drift field is.
:::

This is prose and a remark in the source, not a numbered theorem — cite it that way. Three consequences that the rest of the project runs on:

1. When lesson 19 said *the drift is not a geometric object*, $\mathcal A$ is the object that is. The Stratonovich drift $X$ is a vector field but is **not** determined by the process (problem 4); the chart coefficient $b$ of an Itô SDE is not even a vector field.
2. Any two descriptions of the same diffusion give the same $\mathcal A f$, so **an estimate obtained by applying $\mathcal A$ to a function survives every change of chart, frame and convention.** That is the only step in the tube arguments that has to survive one.
3. Frames are free: since only $\mathcal A$ matters, one may pick whatever orthonormal frame makes a computation cleanest — e.g. a radial frame at $\bar x_t$ in lesson 28 — without changing the process.

Tying back to [[probability-on-manifolds]]: with $u(x,t)=\mathbb E[f(x_T)\mid x_{T-t}=x]$, the **backward Kolmogorov equation** is $\partial_tu=\mathcal Au$. That is the equation built from the generator, and the reason the pathway wants $\mathcal A$ applied to a distance function: $\mathcal A f\le\alpha f+\beta$ pointwise is exactly a supermartingale/affine-martingale certificate for $f(x_t)$ (lesson 23).

:::info[Standing question — classification]
$\mathcal A$ is **kind 1: intrinsic.** So is $\mathrm{Hess}_f$, and so is $\tilde X$ once $\nabla$ is fixed. The payoff: a bound derived by applying $\mathcal A$ to $d(X_t,\bar x_t)$ **inherits no chart-dependence from the stochastic calculus**. Any chart-dependent constant appearing downstream must have come from the metric or from the distance function instead — i.e. from lesson 08's territory, where it is answerable by curvature and injectivity radius. This is what removes one whole source of [[@daniObserverDesignStochastic2015]]'s $\bar m_x,\bar m_{x^2}$ from the discussion.
:::

## Worked example — $\mathcal A$ on a squared distance

Fix an orthonormal frame $\{E_i\}_{i=1}^n$ and take isotropic noise of intensity $\varepsilon$ around a control field $u$:
$$dx=\Big(u-\tfrac{\varepsilon^2}{2}\sum_i\nabla_{E_i}E_i\Big)dt+\varepsilon\sum_iE_i\circ dW_i
\quad\Longleftrightarrow\quad dx=u\,dt+\varepsilon\sum_iE_i\,dW_i .$$
The Stratonovich drift was chosen so that Theorem 1 makes the Itô drift exactly $u$. Theorem 2 then gives, using $\sum_i\mathrm{Hess}_f(E_i,E_i)=\mathrm{tr}_{\mathbb G}\mathrm{Hess}_f=\Delta f$,
$$\mathcal Af=\langle u,\mathrm{grad}\,f\rangle+\frac{\varepsilon^2}{2}\Delta f .$$
Now put $\bar x$ fixed, $r=d(\bar x,\cdot)$, $f=\tfrac12r^2$ — smooth on $B(\bar x,\mathrm{inj}(\bar x))$ by lesson 08. There $\mathrm{grad}\,f=r\,\mathrm{grad}\,r$ and $\Delta f=\tfrac12\Delta r^2=1+r\Delta r$, so
$$\mathcal A\big(\tfrac12r^2\big)=r\,\langle u,\mathrm{grad}\,r\rangle+\frac{\varepsilon^2}{2}\big(1+r\,\Delta r\big)
\;\le\;r\,\langle u,\mathrm{grad}\,r\rangle+\frac{\varepsilon^2}{2}\big(1+(n-1)\,r\,\mathrm{ct}_\kappa(r)\big)$$
whenever $\mathrm{Ric}\ge(n-1)\kappa\,\mathbb G$, by the Laplacian comparison of [[08-hessian-comparison]]. **This is the whole shape of a track-A bound**: the first term is the contraction rate, the second is the noise offset, and Grönwall finishes it. Sanity check in $\mathbb R^n$ ($\kappa=0$, $\mathrm{ct}_0(r)=1/r$): the offset is $\tfrac{\varepsilon^2}{2}\,n$, which is $\tfrac12\mathrm{tr}(\sigma\sigma^\top)$ with $\sigma=\varepsilon I$. ✓

On $SO(3)$ with the bi-invariant metric ($n=3$, $\mathrm{Sec}\equiv\tfrac14$, so $\kappa=\tfrac14$ two-sidedly and the comparison is an equality), $\Delta r=\cot(r/2)$ and the offset is $\tfrac{\varepsilon^2}{2}\big(1+r\cot(r/2)\big)$ — equal to $\tfrac32\varepsilon^2$ as $r\to0$ and strictly decreasing to $\tfrac12\varepsilon^2$ at $r\to\pi$. Positive curvature *shrinks* the noise offset, and the constant is a curvature, not a $\sup|\partial^2g_{ij}|$.

:::warning[Open question — where $\mathcal A f$ stops being defined]
Theorem 2 needs $f\in C^2$. $r^2$ is $C^\infty$ only inside $\mathrm{inj}(\bar x)$; on $\mathrm{Cut}(\bar x)$ it has a corner and $\mathcal A(\tfrac12r^2)$ is undefined, not merely large. Nothing in [[@leeGeometricInterpretationBrownian2025]] addresses this — the paper states no regularity hypotheses at all. Lessons 25 and 28 must supply a stopping time at $\mathrm{Cut}$ or a viscosity/barrier argument. Also, $\bar x_t$ moving makes $f$ time-dependent and adds $\partial_tf$ to $\mathcal A$; that is deferred.
:::

## Problems

1. **Recall.** State Theorem 1 and both forms of Theorem 2 from memory, including the definition $\mathrm{Hess}_f(Y,Z)=Y[Z[f]]-(\nabla_YZ)[f]$. Then answer in one sentence each: why is the Stratonovich form chart-free by construction, and what exactly is the claim "the generator is the invariant"?

2. **Compute.** On $SO(3)$ with the bi-invariant metric of [[notation]], take $\Omega\in\mathfrak{so}(3)$ constant and
$$R^{-1}dR=\Omega\,dt+\varepsilon\sum_{i=1}^3\hat e_i\circ dW_i .$$
(a) Show the Itô drift equals the Stratonovich drift here, and name the two independent reasons. (b) Write $\mathcal A f$. (c) Evaluate it on $f=\tfrac12r^2$ with $r=d(I,R)$ the rotation angle, and give the noise offset at $r=\pi/2$.

3. **Prove.** (a) Show the two expressions in Theorem 2 are equal. (b) Show $\mathcal A$ annihilates constants and satisfies the **diffusion property**
$$\mathcal A(fg)=f\,\mathcal Ag+g\,\mathcal Af+\Gamma(f,g),\qquad \Gamma(f,g):=\sum_i\sigma_i[f]\,\sigma_i[g],$$
and argue $\Gamma$ is intrinsic even though the individual $\sigma_i$ are not determined by the process.

4. **Break it.** Exhibit different drifts with the same generator, twice.
   (a) On $\mathbb R$, $\sigma(x)=x$: compare the Stratonovich SDE $dx=x\circ dW$ (drift $0$) with its Itô form. Show the drifts differ but the generators agree. Conclude that "the drift" is not even well defined until a convention is named.
   (b) Worse — fix the convention and it is *still* not determined. On $\mathbb R^2$ (flat, $\nabla=\partial$) put $u(x)=(\cos x_1,\sin x_1)$, $v(x)=(-\sin x_1,\cos x_1)$. Compute $\nabla_uu+\nabla_vv$. Then show the two **Stratonovich** SDEs
$$\text{(A)}\ \ dx=e_1\circ dW_1+e_2\circ dW_2,\qquad
\text{(B)}\ \ dx=-\tfrac12e_2\,dt+u\circ dW_1+v\circ dW_2$$
have the same generator, hence define the same process in law, despite different drift *and* different diffusion fields.

---

## Solutions

**1.** Statements as above. Chart-free: Stratonovich obeys the ordinary chain rule, so $X$ and the $\sigma_i$ transform as vector fields under a diffeomorphism and the equation pushes forward intact; no second-derivative term appears. The invariance claim: two SDEs induce the same law iff their generators are equal as operators on $C^\infty(M)$ — so $\mathcal A$ is a complete invariant of the diffusion, while the drift is not an invariant at all.

**2(a).** $E_i=R\hat e_i$ is an orthonormal frame ([[notation]]: $\langle\eta,\xi\rangle=\tfrac12\mathrm{tr}[\eta^\top\xi]$ makes $\{\hat e_i\}$ orthonormal). First reason: the metric is bi-invariant, so $\nabla_\xi\xi=0$ for every left-invariant $\xi$ ([[03-levi-civita-left-invariant]]), hence $\nabla_{E_i}E_i=0$ termwise. Second, weaker but sufficient: $SO(3)$ is unimodular, so $\sum_i\nabla_{E_i}E_i=-R\,J=-R\sum_i\widetilde{\mathrm{ad}}_{e_i}e_i=0$ by [[04-unimodularity]] (which records both the identity and $J=0$) — note the metric adjoint $\widetilde{\mathrm{ad}}$, not $\mathrm{ad}^*$, per [[notation]]; the sum vanishes even when the individual terms would not. Either way $\tilde X=X$ by Theorem 1.

**2(b).** Writing $X_\Omega(R)=R\Omega$ for the drift field, $\varepsilon^2\sum_i\mathrm{Hess}_f(E_i,E_i)=\varepsilon^2\Delta f$, so
$$\mathcal Af=X_\Omega[f]+\frac{\varepsilon^2}{2}\Delta f .$$

**2(c).** With $f=\tfrac12r^2$: $\Delta f=\tfrac12\Delta r^2=1+r\cot(r/2)$ from [[08-hessian-comparison]] (there $\Delta r^2=2r\cot(r/2)+2$), so
$$\mathcal A\big(\tfrac12r^2\big)=r\,\langle R\Omega,\mathrm{grad}\,r\rangle+\frac{\varepsilon^2}{2}\big(1+r\cot(r/2)\big).$$
At $r=\pi/2$: $\cot(\pi/4)=1$, offset $=\tfrac{\varepsilon^2}{2}(1+\pi/2)\approx1.285\,\varepsilon^2$, against the Euclidean $\tfrac32\varepsilon^2$.

**3(a).** $\tilde X[f]+\tfrac12\sum_i\mathrm{Hess}_f(\sigma_i,\sigma_i)
=\big(X[f]+\tfrac12\sum_i(\nabla_{\sigma_i}\sigma_i)[f]\big)+\tfrac12\sum_i\big(\sigma_i[\sigma_i[f]]-(\nabla_{\sigma_i}\sigma_i)[f]\big)=X[f]+\tfrac12\sum_i\sigma_i[\sigma_i[f]]$. The covariant terms cancel identically, for any connection — torsion-freeness and metric compatibility are not used.

**3(b).** $Y[1]=0$ for every vector field, so $\mathcal A1=0$ from the first form. For the product, $\sigma[fg]=f\,\sigma[g]+g\,\sigma[f]$, and applying $\sigma$ again,
$$\sigma\big[\sigma[fg]\big]=f\,\sigma[\sigma[g]]+g\,\sigma[\sigma[f]]+2\,\sigma[f]\,\sigma[g].$$
Also $X[fg]=fX[g]+gX[f]$. Summing with the $\tfrac12$ gives the claim, with $\Gamma(f,g)=\sum_i\sigma_i[f]\sigma_i[g]$. $\Gamma$ is intrinsic because it is recovered from $\mathcal A$ alone: $\Gamma(f,g)=\mathcal A(fg)-f\mathcal Ag-g\mathcal Af$. So although problem 4(b) shows the individual $\sigma_i$ are not determined by the process, the quadratic form they build is — it is the principal symbol of $\mathcal A$, i.e. the diffusion tensor $\sum_i\sigma_i\otimes\sigma_i$.

**4(a).** Stratonovich drift $X=0$; Theorem 1 gives $\tilde X=\tfrac12\nabla_\sigma\sigma=\tfrac12\sigma\sigma'=\tfrac12x$, so the Itô form is $dx=\tfrac12x\,dt+x\,dW$ — geometric Brownian motion. Generators: first form $\tfrac12\sigma[\sigma[f]]=\tfrac12x(xf')'=\tfrac12xf'+\tfrac12x^2f''$; second form $\tfrac12xf'+\tfrac12x^2f''$ since $\mathrm{Hess}_f=f''$ on flat $\mathbb R$. Equal. ✓ Drift $0$ versus drift $\tfrac12x$, one process. Naming a drift without naming the convention names nothing.

**4(b).** Since $\partial_ju=(\partial_j x_1)\,v=\delta_{j1}v$ and $\partial_jv=-\delta_{j1}u$,
$$\nabla_uu=(u\!\cdot\!e_1)v=\cos x_1\,v,\qquad \nabla_vv=-(v\!\cdot\!e_1)u=\sin x_1\,u,$$
$$\nabla_uu+\nabla_vv=\cos x_1(-\sin x_1,\cos x_1)+\sin x_1(\cos x_1,\sin x_1)=(0,1)=e_2 .$$
$\{u,v\}$ is an orthonormal frame at every point, so for **either** frame $\sum_i\mathrm{Hess}_f(\cdot,\cdot)=\Delta f$. (A) has zero drift and generator $\tfrac12\Delta f$. For (B), Theorem 1 gives Itô drift $\tilde X=-\tfrac12e_2+\tfrac12(\nabla_uu+\nabla_vv)=-\tfrac12e_2+\tfrac12e_2=0$, so by Theorem 2, $\mathcal Af=0+\tfrac12\Delta f$. Same generator, hence same law: both are standard Brownian motion on $\mathbb R^2$. Independent check: the Itô form of (B) is $dx=Q(x_1)\,dW$ with $Q=[u\ v]$ orthogonal, and $QQ^\top=I$, so the diffusion matrix is the identity too.

The moral is sharper than (a). Even after fixing the convention *and* the connection, the Stratonovich drift ($0$ versus $-\tfrac12e_2$) and the diffusion fields ($\{e_1,e_2\}$ versus $\{u,v\}$) both differ while the process does not. Only the combination that assembles into $\mathcal A$ — here $\tfrac12\Delta$ — carries information. Any bound whose constants read off a drift field is measuring the description; a bound obtained by applying $\mathcal A$ is measuring the diffusion.
