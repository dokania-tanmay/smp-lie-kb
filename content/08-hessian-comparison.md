---
tags: [riemannian, curvature, comparison-geometry, distance-function, foundations]
---
# Hessian of the Distance Function, Comparison, Cut Locus

**Prereq:** [[riemannian-geometry]] (Gauss lemma, normal coordinates, parallel transport); notation fixed in [[notation]]. Lessons 05–07 (curvature conventions, Jacobi fields).
**Goal:** bound $\mathrm{Hess}\,r$ and $\Delta r$ for $r=d(p,\cdot)$ using a sectional-curvature bound alone, and know exactly where that bound stops being available.

Everything here exists because the tube arguments (lessons 25, 28) apply a generator to a function of $d(X_t,\bar x_t)$. Itô produces $\mathrm{Hess}$; the only intrinsic way to control it is comparison geometry.

## Gradient and Hessian

:::info[Definition]
For $\psi\in C^\infty(M)$, the **gradient** is $\mathrm{grad}\,\psi=\mathbb G^\sharp d\psi$, i.e. the unique vector field with $\langle\mathrm{grad}\,\psi,v\rangle=d\psi(v)$ for all $v$. The **Hessian** is the $(0,2)$-tensor
$$\mathrm{Hess}\,\psi(u,w)=\langle u,\nabla_w\,\mathrm{grad}\,\psi\rangle ,$$
and $\mathrm{Hess}^\sharp\psi=\nabla\,\mathrm{grad}\,\psi$ is the associated $(1,1)$-tensor (a field of self-adjoint endomorphisms). The **Laplace–Beltrami operator** is $\Delta\psi=\mathrm{tr}_{\mathbb G}\,\mathrm{Hess}\,\psi=\mathrm{tr}\,\mathrm{Hess}^\sharp\psi$.
:::

Both are intrinsic (category 1 of [content/CLAUDE.md](CLAUDE.md) § standing question): $\mathrm{grad}$ needs the metric, $\mathrm{Hess}$ needs the Levi-Civita connection, neither needs a chart. Note $\mathrm{Hess}\,\psi\ne\partial^2\psi$ in any chart — the difference is $-\Gamma^k_{ij}\partial_k\psi$, and it is exactly that Christoffel correction that makes the object a tensor.

:::tip[Lemma]
$\mathrm{Hess}\,\psi$ is symmetric.
:::

Expand $\langle u,\nabla_w\,\mathrm{grad}\,\psi\rangle=w(u\psi)-(\nabla_w u)\psi$ using metric compatibility. Antisymmetrising, $w(u\psi)-u(w\psi)=[w,u]\psi$ and $\nabla_w u-\nabla_u w=[w,u]$ because $\nabla$ is **torsion-free**, so the two cancel. Symmetry is a property of $\nabla$, not of $\psi$: for the flat left-invariant $\nabla^-$ of [[notation]] it fails.

## The distance function

Fix $p\in M$ ($M$ complete) and set $r(x)=d(p,x)$, the Riemannian distance — **not** $\|\log_G(p^{-1}x)\|$, which is a different function unless the metric is bi-invariant.

:::tip[Proposition]
Wherever $r$ is smooth, $\|\mathrm{grad}\,r\|=1$, and $\mathrm{grad}\,r|_x=\dot\gamma(r(x))$ is the terminal velocity of the unique minimising unit-speed geodesic $\gamma$ from $p$ to $x$. Consequently
$$\mathrm{Hess}\,r(\mathrm{grad}\,r,\cdot)=0 .$$
:::

$\|\mathrm{grad}\,r\|=1$ is the Gauss lemma — already in [[riemannian-geometry]] § Gauss lemma, not reproved here. The second claim follows in one line (problem 3): differentiate $\langle\mathrm{grad}\,r,\mathrm{grad}\,r\rangle\equiv1$. Geometrically, $\nabla_{\partial_r}\partial_r=0$ because the integral curves of $\mathrm{grad}\,r$ are geodesics. So $\mathrm{Hess}\,r$ lives entirely on the $(n-1)$-dimensional **radial-orthogonal** distribution $\ker dr$, and its natural comparison object is the projected metric $g-dr\otimes dr$, which is positive semidefinite with kernel $\mathrm{span}(\mathrm{grad}\,r)$.

## Comparison

:::info[Definition]
The **generalised cotangent** $\mathrm{ct}_\kappa:(0,\ell_\kappa)\to\mathbb R$, $\ell_\kappa=\pi/\sqrt\kappa$ for $\kappa>0$ and $\infty$ otherwise:
$$\mathrm{ct}_\kappa(r)=\begin{cases}\sqrt\kappa\,\cot(\sqrt\kappa\,r), & \kappa>0\\[2pt] 1/r, & \kappa=0\\[2pt] \sqrt{|\kappa|}\,\coth(\sqrt{|\kappa|}\,r), & \kappa<0.\end{cases}$$
Equivalently $\mathrm{ct}_\kappa=\mathrm{sn}_\kappa'/\mathrm{sn}_\kappa$, where $\mathrm{sn}_\kappa$ solves $\mathrm{sn}''+\kappa\,\mathrm{sn}=0$, $\mathrm{sn}_\kappa(0)=0$, $\mathrm{sn}_\kappa'(0)=1$. In all three cases $\mathrm{ct}_\kappa(r)\to+\infty$ as $r\to0^+$ and $\mathrm{ct}_\kappa$ is strictly decreasing in $r$ and in $\kappa$.
:::

:::tip[Theorem — Hessian comparison]
Let $(M,g)$ be complete, $p\in M$, $r=d(p,\cdot)$, and let $x\in M\setminus(\{p\}\cup\mathrm{Cut}(p))$, so $r$ is smooth near $x$ and there is a unique minimising unit-speed geodesic $\gamma:[0,r(x)]\to M$ from $p$ to $x$.

1. If $\mathrm{Sec}(\Pi)\le\kappa$ for every $2$-plane $\Pi$ containing $\dot\gamma$ along $\gamma$, **and** $r(x)<\pi/\sqrt\kappa$ when $\kappa>0$, then at $x$
$$\mathrm{Hess}\,r\;\ge\;\mathrm{ct}_\kappa(r)\,\big(g-dr\otimes dr\big).$$
2. If $\mathrm{Sec}(\Pi)\ge\kappa$ for every such plane, then at $x$
$$\mathrm{Hess}\,r\;\le\;\mathrm{ct}_\kappa(r)\,\big(g-dr\otimes dr\big).$$

Inequalities are between symmetric bilinear forms. The range hypothesis in (1) is genuine: with $\kappa>0$ an upper curvature bound does not stop $r$ from exceeding $\pi/\sqrt\kappa$ (hyperbolic space has $\mathrm{Sec}\le1$ and unbounded $r$). In (2) no range hypothesis is needed — for $\kappa>0$, Bonnet–Myers already forces $r(x)<\pi/\sqrt\kappa$ off the cut locus.
:::

Direction check: an **upper** curvature bound gives a **lower** Hessian bound. Curvature focuses geodesics, so more curvature means the level sets of $r$ bend less, i.e. smaller $\mathrm{Hess}\,r$. The proof is the Riccati/index-form comparison for the Jacobi fields of lesson 07; not reproved here.

:::tip[Corollary — Laplacian comparison]
Taking $\mathrm{tr}_{\mathbb G}$ and using $\mathrm{tr}_{\mathbb G}(g-dr\otimes dr)=n-1$ together with $\mathrm{Hess}\,r(\mathrm{grad}\,r,\cdot)=0$:
$$\mathrm{Sec}\le\kappa\ \Rightarrow\ \Delta r\ge(n-1)\,\mathrm{ct}_\kappa(r),\qquad
\mathrm{Ric}\ge(n-1)\kappa\,g\ \Rightarrow\ \Delta r\le(n-1)\,\mathrm{ct}_\kappa(r).$$
The upper bound needs only a **Ricci** lower bound — a trace condition, strictly weaker than $\mathrm{Sec}\ge\kappa$. Since $\mathrm{Hess}\,r^2=2r\,\mathrm{Hess}\,r+2\,dr\otimes dr$,
$$\Delta r^2\;=\;2r\,\Delta r+2\;\le\;2(n-1)\,r\,\mathrm{ct}_\kappa(r)+2 ,$$
which extends across $p$ (where $r$ is not smooth but $r^2$ is), because $r\,\mathrm{ct}_\kappa(r)\to1$ as $r\to0$ and the right side tends to $2n$ — the Euclidean value of $\Delta\|x\|^2$.
:::

That last line is the form the generator will actually consume: $\tfrac12\Delta d(\cdot,\bar x)^2$ is the Itô correction in track A, and $\Delta$ applied to $\Phi_\lambda(r)$ in track B expands into $\Phi''_\lambda\|\mathrm{grad}\,r\|^2+\Phi'_\lambda\Delta r$ — the first term is $1$ by Gauss, the second is what comparison bounds.

## Worked example: the three model spaces

In geodesic polar coordinates about $p$, the constant-curvature model $M^n_\kappa$ has metric $g=dr^2+\mathrm{sn}_\kappa(r)^2\,g_{S^{n-1}}$ on $0<r<\ell_\kappa$. Let $X,Y$ be tangent to the spherical factor, so $Xr=Yr=0$. Then
$$\mathrm{Hess}\,r(X,Y)=X(Yr)-(\nabla_XY)r=-\langle\nabla_XY,\,\mathrm{grad}\,r\rangle=\langle Y,\nabla_X\partial_r\rangle,$$
and the warped-product connection gives $\nabla_X\partial_r=\dfrac{\mathrm{sn}_\kappa'(r)}{\mathrm{sn}_\kappa(r)}X=\mathrm{ct}_\kappa(r)X$. Hence, together with $\mathrm{Hess}\,r(\partial_r,\cdot)=0$,
$$\boxed{\ \mathrm{Hess}\,r=\mathrm{ct}_\kappa(r)\,(g-dr\otimes dr)\ }\qquad\text{on }M^n_\kappa .$$
Concretely: $\mathbb R^n$ ($\kappa=0$, $\mathrm{sn}_0=r$) gives $\tfrac1r(g-dr\otimes dr)$; $S^n_\kappa$ ($\mathrm{sn}_\kappa=\sin(\sqrt\kappa r)/\sqrt\kappa$) gives $\sqrt\kappa\cot(\sqrt\kappa r)$; $H^n_\kappa$ gives $\sqrt{|\kappa|}\coth(\sqrt{|\kappa|}r)$. Direct check in $\mathbb R^n$ with $p=0$: $\mathrm{grad}\,r=x/\|x\|$ and $\partial_i(x_j/\|x\|)=\delta_{ij}/r-x_ix_j/r^3$, i.e. $\tfrac1r(I-\hat x\hat x^\top)$ — the same thing.

**Both inequalities of the comparison theorem are equalities here.** That is precisely what makes these the comparison models: the bound is attained, so it cannot be improved by any argument using only a curvature bound.

## Cut locus and injectivity radius

:::info[Definition]
For a unit $v\in T_pM$ let $\gamma_v(t)=\exp_p(tv)$ (**Riemannian** exponential). The **cut time** is $t_{\mathrm{cut}}(v)=\sup\{t>0:\ d(p,\gamma_v(t))=t\}$ — the last time $\gamma_v$ is still minimising. If finite, $\gamma_v(t_{\mathrm{cut}}(v))$ is the **cut point** of $p$ along $v$, and
$$\mathrm{Cut}(p)=\{\gamma_v(t_{\mathrm{cut}}(v)):\ \|v\|=1,\ t_{\mathrm{cut}}(v)<\infty\}.$$
The **injectivity radius** is $\mathrm{inj}(p)=d(p,\mathrm{Cut}(p))=\inf_{\|v\|=1}t_{\mathrm{cut}}(v)$ and $\mathrm{inj}(M)=\inf_{p\in M}\mathrm{inj}(p)$.
:::

Facts used throughout:

- $r$ is smooth **exactly** on $M\setminus(\{p\}\cup\mathrm{Cut}(p))$. At $p$ it fails (cone point: $\|\mathrm{grad}\,r\|=1$ cannot extend continuously); on $\mathrm{Cut}(p)$ it fails because either two minimising geodesics arrive (so $r$ has a corner) or $\exp_p$ is singular (a conjugate point).
- $r^2$ **is** smooth on the whole ball $B(p,\mathrm{inj}(p))$, including at $p$, since $r^2(x)=\|\exp_p^{-1}x\|^2$ there. This is why every bound below is written for $r^2$ or for $\Phi_\lambda(r)$ with $\Phi_\lambda$ even.
- $\exp_p$ is a diffeomorphism from the open ball of radius $\mathrm{inj}(p)$ in $T_pM$ onto $B(p,\mathrm{inj}(p))$: **normal coordinates are valid exactly inside the injectivity radius**, and not one step further.
- Round sphere of radius $R$ (so $\kappa=1/R^2$): $\mathrm{Cut}(p)=\{-p\}$ and $\mathrm{inj}=\pi R=\pi/\sqrt\kappa$.
- $SO(3)$ with the bi-invariant metric of [[notation]] has $\mathrm{Sec}\equiv\tfrac14$ (constant, since $\mathrm{Sec}=\tfrac14\|[\hat e_i,\hat e_j]\|^2=\tfrac14$), $d(I,R)=\|\log_G R\|=$ the rotation angle $\theta\in[0,\pi]$, $\mathrm{Cut}(I)=\{\text{rotations by }\pi\}\cong\mathbb{RP}^2$, and $\mathrm{inj}(SO(3))=\pi$ — **half** the $2\pi$ that $\kappa=\tfrac14$ would give for a sphere, because $SO(3)\cong\mathbb{RP}^3$.

That last discrepancy is the point: **the injectivity radius is not a function of the curvature bounds.** Any tube of radius exceeding $\mathrm{inj}$ contains points where $r$ is not differentiable and where the comparison theorem has no content; such a tube needs separate treatment (a barrier/viscosity argument, or a stopping time at $\mathrm{Cut}$), not a sharper constant.

## What this replaces

[[@daniObserverDesignStochastic2015]] Assumption 1 carries $\bar m_x=\sup_{t,i,j}|\partial M_{ij}/\partial x|$ and $\bar m_{x^2}=\sup_{t,i,j}|\partial^2M_{ij}/\partial x^2|$, and its §"where the chart-dependence enters" traces them into both the rate $\gamma_1$ and the offset $C$; the bound goes vacuous once $(\beta_1^2+\beta_2^2)(\varepsilon\bar m_x+\bar m_{x^2}/2)\ge2m\gamma$. Both are category-3 quantities — componentwise sup-norms of $\partial g$ and $\partial^2 g$, not tensors, and both vanish at a point in normal coordinates.

The intrinsic replacements are exactly the three constants of this lesson:

| Dani (chart) | intrinsic replacement |
|---|---|
| $\bar m_x=\sup\lvert\partial M_{ij}/\partial x\rvert$ | **nothing** — $\partial g$ has no pointwise intrinsic content; it is gauged away in normal coordinates |
| $\bar m_{x^2}=\sup\lvert\partial^2M_{ij}/\partial x^2\rvert$ | a **sectional-curvature bound** $\kappa$ (or $\mathrm{Ric}\ge(n-1)\kappa$ for the Laplacian form) |
| — (absent; silently assumed by using one chart) | the **injectivity radius** $\mathrm{inj}(M)$, bounding the region where $r^2$ is smooth |
| — | the **Hessian-comparison constant** $(n-1)\,\mathrm{ct}_\kappa(r)$ that the two above produce |

:::warning[Open question]
That the curvature bound is the *right* replacement is settled — it is what $\partial^2g$ intrinsically is. That it gives a *tighter* constant is not. $\mathrm{ct}_\kappa$ is attained with equality in the model spaces, so the comparison step loses nothing, but the constant then propagates through a Grönwall (track A) or a Doob (track B) step, and it is entirely possible that a well-chosen chart on a specific group gives a smaller $\bar m_{x^2}$ than $(n-1)\mathrm{ct}_\kappa$ does. The honest claim so far is *chart-independent*, not *tighter*. Lesson 29 has to settle it on the two worked cases: $SO(3)$ bi-invariant ($\mathrm{Sec}\equiv\tfrac14$, $\mathrm{inj}=\pi$) against $SE(3)$ left-invariant (no bi-invariant metric, mixed-sign curvature, $\mathrm{inj}$ not constant).
:::

## Problems

1. **Recall.** Without looking: define $\mathrm{Hess}\,\psi$ and $\Delta\psi$; define the cut time, cut locus and injectivity radius; write $\mathrm{ct}_\kappa$ in all three cases. Then state the Hessian comparison theorem including *every* hypothesis, and say which of the two directions needs a restriction on the range of $r$ and why.

2. **Compute.** (a) On $S^n_\kappa$ compute $\mathrm{Hess}\,r$, $\Delta r$ and $\Delta r^2$, and check $\Delta r^2\to2n$ as $r\to0$. (b) Specialise to $SO(3)$ with the bi-invariant metric ($n=3$, $\mathrm{Sec}\equiv\tfrac14$, $r=$ rotation angle): give $\Delta r$ and $\Delta r^2$ explicitly, and evaluate $\Delta r^2$ at $r=\pi/2$ and as $r\to\pi$.

3. **Prove.** (a) From $\|\mathrm{grad}\,r\|\equiv1$ deduce $\mathrm{Hess}\,r(\mathrm{grad}\,r,\cdot)=0$, in two lines. (b) Show $\mathrm{Hess}\,r^2=2r\,\mathrm{Hess}\,r+2\,dr\otimes dr$ for any $M$, and deduce that in $\mathbb R^n$, $\mathrm{Hess}\,r^2=2g$ everywhere — including at $p$, where $\mathrm{Hess}\,r$ does not exist.

4. **Break it.** (a) On the round sphere of radius $R$ with $p$ fixed, show $r$ is not differentiable at the antipode $-p$ by exhibiting the family of minimising geodesics, and show $\Delta r\to-\infty$ as $r\to\pi R$. Conclude that any bound proportional to $\sup_{r\le\rho}|\Delta r|$ blows up as the tube radius $\rho\uparrow\mathrm{inj}$. (b) Take the flat torus $T=\mathbb R^2/\mathbb Z^2$, $\mathrm{Sec}\equiv0$. Compute $\mathrm{Cut}(p)$ and $\mathrm{inj}(T)$. The model-space computation gives $\mathrm{Hess}\,r=\tfrac1r(g-dr\otimes dr)$ for **all** $r>0$ in $\mathbb R^2$; show it fails on $T$ at $r=\tfrac12$, identify which hypothesis of the comparison theorem is violated, and conclude that no two-sided curvature bound whatsoever can detect it.

---

## Solutions

**1.** Definitions as stated above. Range restriction: only direction (1), $\mathrm{Sec}\le\kappa$ with $\kappa>0$, needs $r<\pi/\sqrt\kappa$ — because $\mathrm{ct}_\kappa$ is only defined (and the comparison Jacobi field $\mathrm{sn}_\kappa$ only positive) on $(0,\pi/\sqrt\kappa)$, and an *upper* curvature bound places no ceiling on $r$ (hyperbolic space satisfies $\mathrm{Sec}\le1$ with $r$ unbounded). Direction (2) needs none: $\mathrm{Sec}\ge\kappa>0$ gives $\mathrm{diam}\le\pi/\sqrt\kappa$ by Bonnet–Myers, so the range is automatic.

**2(a).** $\mathrm{Hess}\,r=\sqrt\kappa\cot(\sqrt\kappa r)(g-dr\otimes dr)$, so $\Delta r=(n-1)\sqrt\kappa\cot(\sqrt\kappa r)$ and
$$\Delta r^2=2r\Delta r+2=2(n-1)\sqrt\kappa\,r\cot(\sqrt\kappa r)+2 .$$
As $r\to0$, $\sqrt\kappa r\cot(\sqrt\kappa r)\to1$, giving $2(n-1)+2=2n$. ✓ (Curvature is invisible to leading order at the centre — the manifold looks Euclidean there, as it must.)

**2(b).** $\kappa=\tfrac14$, $\sqrt\kappa=\tfrac12$, $n=3$: $\Delta r=2\cdot\tfrac12\cot(r/2)=\cot(r/2)$ and $\Delta r^2=2r\cot(r/2)+2$. At $r=\pi/2$: $\cot(\pi/4)=1$, so $\Delta r=1$ and $\Delta r^2=\pi+2\approx5.14$ (versus the Euclidean $2n=6$ — positive curvature *reduces* it). As $r\to\pi$ (the cut locus), $\cot(r/2)\to0$, so $\Delta r\to0$ and $\Delta r^2\to2$: the level sets of $r$ shrink back to the $\mathbb{RP}^2$ of $\pi$-rotations, and their mean curvature passes through zero.

**3(a).** Differentiate the constant function $\langle\mathrm{grad}\,r,\mathrm{grad}\,r\rangle\equiv1$ along any $w$: metric compatibility gives $0=2\langle\nabla_w\mathrm{grad}\,r,\mathrm{grad}\,r\rangle=2\,\mathrm{Hess}\,r(\mathrm{grad}\,r,w)$. By symmetry the other slot vanishes too.

**3(b).** $\mathrm{grad}\,r^2=2r\,\mathrm{grad}\,r$, so
$$\mathrm{Hess}\,r^2(u,w)=\langle u,\nabla_w(2r\,\mathrm{grad}\,r)\rangle=2(wr)\langle u,\mathrm{grad}\,r\rangle+2r\langle u,\nabla_w\mathrm{grad}\,r\rangle=2\,dr(u)dr(w)+2r\,\mathrm{Hess}\,r(u,w).$$
In $\mathbb R^n$, $\mathrm{Hess}\,r=\tfrac1r(g-dr\otimes dr)$, so $\mathrm{Hess}\,r^2=2(g-dr\otimes dr)+2\,dr\otimes dr=2g$. The $1/r$ singularity cancels against the factor $r$ — which is exactly why $r^2$ extends smoothly through $p$ while $r$ does not.

**4(a).** Every unit $v\in T_pS^n$ gives a great circle through $p$ reaching $-p$ at arclength $\pi R$, and all of them are minimising: an $(n-1)$-sphere's worth of minimising geodesics arrive at $-p$. Their terminal velocities disagree, so $\mathrm{grad}\,r$ has no single limit at $-p$ and $r$ is not differentiable there (in fact $r$ has a strict maximum at $-p$, and a smooth function's gradient would vanish there, contradicting $\|\mathrm{grad}\,r\|=1$). With $\kappa=1/R^2$, $\Delta r=(n-1)R^{-1}\cot(r/R)\to-\infty$ as $r\to\pi R^-$. So $\sup_{r\le\rho}|\Delta r|=\Theta\big((\pi R-\rho)^{-1}\big)$ diverges as $\rho\uparrow\mathrm{inj}=\pi R$: an estimate whose constant is $\sup|\Delta r|$ over the tube is useless for tubes approaching the injectivity radius, no matter how good the curvature bound is.

**4(b).** $T=\mathbb R^2/\mathbb Z^2$ is flat, so $\mathrm{Sec}\equiv0$ and every curvature bound is two-sided sharp with $\kappa=0$. Taking $p=[0,0]$, a point $[x]$ has $r([x])=\min_{k\in\mathbb Z^2}\|x-k\|$, and the minimiser stops being unique on the boundary of the fundamental Voronoi square $[-\tfrac12,\tfrac12]^2$: $\mathrm{Cut}(p)$ is the union of the two circles $\{x_1=\tfrac12\}$ and $\{x_2=\tfrac12\}$ (a wedge of two circles), and $\mathrm{inj}(T)=\tfrac12$, half the shortest closed geodesic. At the point $[\tfrac12,0]$, i.e. $r=\tfrac12$, the two lifts $(\tfrac12,0)$ and $(-\tfrac12,0)$ are both minimising, $r$ has a corner (it is $\tfrac12-|s|+O(s^2)$ along the $x_1$ direction), so $\mathrm{Hess}\,r$ does not exist and the Euclidean formula $\tfrac1r(g-dr\otimes dr)$ — which would predict $\mathrm{Hess}\,r$ finite and positive semidefinite there — fails. The violated hypothesis is $x\notin\mathrm{Cut}(p)$: nothing about the curvature. Since $\mathrm{Sec}\equiv0$ exactly matches $\mathbb R^2$, no curvature bound of any kind distinguishes $T$ from $\mathbb R^2$, yet $\mathrm{inj}(\mathbb R^2)=\infty$ and $\mathrm{inj}(T)=\tfrac12$. The injectivity radius is therefore a genuinely independent intrinsic constant, and must be listed as a hypothesis in its own right in any tube bound. (Scaling the torus to $\mathbb R^2/(L\mathbb Z)^2$ makes $\mathrm{inj}=L/2$ arbitrarily small at fixed zero curvature — so it cannot even be bounded below by curvature plus a diameter bound in the wrong direction.)
