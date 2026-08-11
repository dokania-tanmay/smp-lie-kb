---
tags: [amgf, probabilistic-tube, curvature, comparison-geometry, generator, contribution]
---
# The Intrinsic AMGF

**Prereq:** [[26-euclidean-amgf]] (radial profile $\varphi_N$, Bessel form, the $(1-\varepsilon^2)^{N/2}$ lower bound), [[27-set-erosion-tubes]] (tube $\Rightarrow$ safety), [[23-martingale-toolkit]] (affine martingale + Doob), [[20-generator-on-manifolds]] ($\mathcal A$), [[08-hessian-comparison]] ($\Delta r$, cut locus), [[22-force-vs-configuration-noise]] (Case A), [[14-contraction-on-manifolds]], [[notation]].
**Goal:** define the AMGF on a Riemannian manifold, compute $\mathcal A\Phi_\lambda$ exactly, and say precisely which steps of the Euclidean tube proof survive.

**This is Contribution B — research, not exposition.** Nothing below is in the literature. Per [[notation]], $N=\dim M$ throughout: the sphere average runs over $T_xM$, so $N$ is the dimension of the *state* manifold, $N=2n$ on $T^*G$ — **not** $\dim G$.

## The definition is forced, not invented

[[26-euclidean-amgf]] establishes that the Euclidean energy function is *already* radial and isotropic: $\Phi_{N,\lambda}(x)=\mathbb E_{\ell\sim S^{N-1}}[e^{\lambda\langle\ell,x\rangle}]=\varphi_N(\lambda\|x\|)$ ([[@liuNewProofSubGaussian2025]] eq. (6)). The only two ingredients are an inner product and a rotation-invariant probability measure on the unit sphere. **Both exist canonically on $T_xM$ and nowhere else is a choice needed** — so the lift is determined, not designed.

:::info[Definition — intrinsic AMGF energy function]
Let $(M,\mathbb G)$ be complete, $\bar x\in M$, $r(x)=d(x,\bar x)$ the Riemannian distance. Let $S(T_xM)=\{\ell\in T_xM:\|\ell\|_x=1\}$ with its unique $O(T_xM,\mathbb G_x)$-invariant probability measure. With $\log_x$ the **Riemannian** log at $x$ (not $\log_G$ — see [[notation]]),
$$\Phi_\lambda(x)\;=\;\mathbb E_{\ell\sim S(T_xM)}\Big[e^{\lambda\langle\ell,\,-\log_x\bar x\rangle_x}\Big].$$
:::

:::tip[Proposition — collapse to the Euclidean profile]
For $x\in B(\bar x,\mathrm{inj}(\bar x))$, $\ \Phi_\lambda(x)=\varphi_N(\lambda r(x))$, with **exactly** the $\varphi_N$ of [[26-euclidean-amgf]]: $\varphi_1(z)=\cosh z$, $\varphi_N(z)=\Gamma(N/2)(2/z)^{(N-2)/2}I_{(N-2)/2}(z)$.
:::

*Proof.* $-\log_x\bar x=r(x)\,\mathrm{grad}\,r|_x$: the geodesic from $x$ to $\bar x$ has initial velocity $\log_x\bar x$ of norm $r$, and $\mathrm{grad}\,r|_x$ is the terminal velocity of the reversed geodesic ([[08-hessian-comparison]]). So the exponent is $\lambda r\langle\ell,\mathrm{grad}\,r\rangle$, and by invariance of the measure the average depends only on $\lambda r$. $(T_xM,\mathbb G_x)$ **is** a Euclidean space, so the value is the Euclidean one. $\square$

Note $\varphi_N$ is even and analytic, so $\Phi_\lambda$ is a smooth function of $r^2$ — smooth on the whole ball $B(\bar x,\mathrm{inj})$ including at $\bar x$, where $r$ itself is not.

## What survives verbatim

Everything **pointwise** in [[26-euclidean-amgf]] transfers with no argument, because $T_xM$ is an inner-product space and the sphere in it is a genuine round $S^{N-1}$: the Bessel closed form, $\varphi_N(0)=1$, radiality, monotonicity, convexity, $0\le\varphi_N'/\varphi_N=I_{N/2}/I_{N/2-1}<1$, and the exponential-growth lemma
$$\Phi_\lambda(x)\;\ge\;(1-\varepsilon^2)^{N/2}e^{\varepsilon\lambda r(x)},\qquad\varepsilon\in(0,1).$$
Lesson 26 flagged this level-set lemma as the cleanest piece to carry over — **confirmed**: it is deterministic, pointwise, and involves no derivative of $\varphi_N$ along $M$. Converting a sublevel set of $\Phi_\lambda$ into a distance ball costs exactly what it costs in $\mathbb R^N$.

## Applying the generator — where curvature enters

The engine of the flat proof is that $\Phi_\lambda$ is a $\Delta$-eigenfunction: $\Delta_{\mathbb R^N}e^{\lambda\langle\ell,x\rangle}=\lambda^2e^{\lambda\langle\ell,x\rangle}$, hence $\Delta\Phi_\lambda=\lambda^2\Phi_\lambda$, which is where $a_t=\lambda^2\sigma^2/2$ in [[@liuSetErosionTubes]] Thm 2 comes from. Radially this is the modified-Bessel ODE
$$\varphi_N''(z)+\tfrac{N-1}{z}\varphi_N'(z)=\varphi_N(z).$$

:::tip[Proposition — the master identity]
Wherever $r$ is smooth, with $z=\lambda r$ and the **curvature defect** $\mathcal D(r):=r\,\Delta r-(N-1)$,
$$\boxed{\ \Delta_M\Phi_\lambda\;=\;\lambda^2\Phi_\lambda\;+\;\frac{\lambda\,\varphi_N'(z)}{r}\,\mathcal D(r)\ }$$
and for a diffusion with Itô drift $\tilde X$ and diffusion tensor $\Sigma=\sum_i\sigma_i\otimes\sigma_i$,
$$\mathcal A\Phi_\lambda=\lambda\varphi_N'(z)\,\langle\tilde X,\mathrm{grad}\,r\rangle+\tfrac12\lambda^2\varphi_N''(z)\,\Sigma(\mathrm{grad}\,r,\mathrm{grad}\,r)+\tfrac12\lambda\varphi_N'(z)\,\langle\Sigma,\mathrm{Hess}\,r\rangle .$$
:::

*Proof.* Chain rule on $\Phi_\lambda=\varphi_N\circ(\lambda r)$: $\mathrm{grad}\,\Phi_\lambda=\lambda\varphi_N'\,\mathrm{grad}\,r$ and $\mathrm{Hess}\,\Phi_\lambda=\lambda^2\varphi_N''\,dr\otimes dr+\lambda\varphi_N'\,\mathrm{Hess}\,r$. Feed into $\mathcal Af=\tilde X[f]+\tfrac12\sum_i\mathrm{Hess}_f(\sigma_i,\sigma_i)$ ([[20-generator-on-manifolds]] Thm 2). For the boxed line take $\Sigma=\mathbb G^\sharp$, use $\|\mathrm{grad}\,r\|=1$ (Gauss lemma) so $\Delta\Phi_\lambda=\lambda^2\varphi_N''+\lambda\varphi_N'\Delta r$, and eliminate $\varphi_N''$ with the Bessel ODE. $\square$

**Curvature enters through $\mathcal D$ and nowhere else.** In $\mathbb R^N$, $\Delta r=(N-1)/r$ so $\mathcal D\equiv0$ and the identity is the flat eigenfunction property. By the Laplacian comparison of [[08-hessian-comparison]], $\mathrm{Ric}\ge(N-1)\kappa\,\mathbb G$ gives $\Delta r\le(N-1)\mathrm{ct}_\kappa(r)$, hence
$$\mathcal D(r)\le(N-1)\big(r\,\mathrm{ct}_\kappa(r)-1\big),\qquad \frac{\mathcal D(r)}{r}\le(N-1)\big(\mathrm{ct}_\kappa(r)-\tfrac1r\big)\le(N-1)\sqrt{|\kappa|}\ \ (\kappa<0),$$
and $\mathcal D\le0$ for $\kappa\ge0$. No $\sup|\partial^2 g_{ij}|$ appears anywhere — this is the substitution the thesis asks for, made explicit.

### Is it an affine martingale?

The obstruction is the drift term. Contraction gives $\langle\tilde X,\mathrm{grad}\,r\rangle\le c\,r$, so that term is $\le c\,z\varphi_N'(z)$, and $z\varphi_N'(z)$ is **not** a constant multiple of $\varphi_N(z)$ — the best two-sided ratios are $0\le z\varphi_N'/\varphi_N<z$. For $c<0$ the useful direction needs a lower bound, and Amos' bound gives $z\varphi_N'/\varphi_N\ge\sqrt{z^2+N^2/4}-N/2$, which is state-dependent. So **the drift term is affine only after $c$ is scaled away**, exactly as in the Euclidean proof. The scaling can be done on the distance function rather than on the state (see the first callout below), and then:

:::tip[Proposition — intrinsic affine martingale]
Let $\bar x_t$ be the deterministic trajectory of a field that is $c_t$-contracting ([[14-contraction-on-manifolds]]) on a geodesically convex region containing the tube; $\psi_t=\int_0^tc_\tau d\tau$; $\Sigma\preceq\sigma^2\mathbb G^\sharp$; $\mathrm{Ric}\ge(N-1)\kappa\,\mathbb G$. Let $\tau$ be the exit time from $\{r<\mathrm{inj}\}$ and set $\hat r_t=e^{-\psi_t}d(X_t,\bar x_t)$. Then on $t<\tau$, $B(X_t,t)=\varphi_N(\lambda\hat r_t)$ is an affine martingale with $b_t=0$ and
$$a_t=\tfrac12\lambda^2\sigma^2e^{-2\psi_t}\;+\;\tfrac12\lambda\sigma^2e^{-\psi_t}(N-1)\sqrt{|\kappa|}\cdot\mathbf 1_{\kappa<0}.$$
For $\kappa\ge0$ the second term is absent and $a_t=\lambda^2\hat\sigma_t^2/2$ — **identical to [[@liuSetErosionTubes]] Thm 2**, with $\hat\sigma_t=\sigma e^{-\psi_t}$.
:::

*Proof sketch.* Two ingredients. (i) *Radial contraction.* Along the unit-speed minimising geodesic $\gamma$ from $\bar x_t$ to $x$, $\tfrac{d}{ds}\langle X\circ\gamma,\gamma'\rangle=\langle\nabla_{\gamma'}X,\gamma'\rangle\le c_t$ since $\nabla_{\gamma'}\gamma'=0$; integrating and using the first variation of arc length, $\partial_tr+\langle\tilde X,\mathrm{grad}\,r\rangle\le c_t r$, so $\partial_t\hat r+\langle\tilde X,\mathrm{grad}\,\hat r\rangle\le0$ and, since $\varphi_N'\ge0$, the drift term is $\le0$. (ii) The master identity applied to $\hat r$, with $\varphi_N'\le\varphi_N$ used to absorb $\mathcal D/r$ into $a_t$. $\square$

Feeding this into [[23-martingale-toolkit]]'s Doob step and the level-set lemma reproduces the Euclidean radius verbatim for $\kappa\ge0$:
$$r_{\delta,t}=\sqrt{e^{2\psi_t}\,\Psi_T\big(\varepsilon_1N+\varepsilon_2\log(1/\delta)\big)},\qquad \Psi_T=\int_0^T\sigma^2e^{-2\psi_\tau}d\tau .$$

## Worked example — $SO(3)$, bi-invariant

Configuration only: $N=3$, $\mathrm{Sec}\equiv\tfrac14$ ([[06-curvature-left-invariant-metrics]]), so $\kappa=\tfrac14$ **two-sidedly** and the comparison is an equality; $\mathrm{inj}=\pi$ ([[08-hessian-comparison]]); $r=$ rotation angle; $\Delta r=\cot(r/2)$. The profile is elementary:
$$\varphi_3(z)=\tfrac{\sqrt\pi}{2}(2/z)^{1/2}I_{1/2}(z)=\frac{\sinh z}{z},\qquad \frac{\varphi_3'(z)}{\varphi_3(z)}=\coth z-\frac1z .$$
The defect is **exact**, not a bound:
$$\mathcal D(r)=r\cot(r/2)-2\;\in\;(-2,\,0],\qquad \mathcal D(0^+)=0,\ \ \mathcal D(\tfrac\pi2)=\tfrac\pi2-2\approx-0.429,\ \ \mathcal D(\pi^-)=-2 .$$
So $\mathcal A\Phi_\lambda\le\frac{\lambda^2\sigma^2}{2}\Phi_\lambda\,(1-\eta)$ with a strictly positive curvature dividend
$$\eta(z,r)=\frac{\coth z-1/z}{z}\,\big|\mathcal D(r)\big| .$$
Numbers at $\lambda=1$: $\eta=12.4\%$ at $r=\pi/2$, $\eta=43.6\%$ at $r\to\pi$. At $\lambda=10$, $r=\pi/2$: $\eta=2.6\%$.

:::warning[Open question — the curvature dividend evaporates at the operating point]
$\eta=O(|\mathcal D|/z)$ because $\coth z-1/z\to1$. But the tube proof optimises $\lambda^*=\varepsilon r/\!\int_0^T\bar\sigma^2$, which is *large* precisely in the tight-tube, small-$\delta$ regime the method exists for. So positive curvature helps most where the bound is loosest. Whether the $O(1/z)$ gain ever beats the $\varepsilon_1N$ dimension cost is unsettled — this is lesson 29's job, and the honest reading so far is that on $SO(3)$ the intrinsic bound is *chart-free* but not obviously *tighter*.
:::

For the state manifold $T^*SO(3)$ we need $N=6$, and neither $\kappa$ nor $\mathrm{inj}$ is $\tfrac14$/$\pi$ any more: the relevant curvature is that of the Sasaki or cross-term metric ([[13-sasaki-metric]], [[16-cross-term-metrics]]), which is non-constant and has $\mathrm{Sec}(X^h,Y^h)=\mathrm{Sec}(X,Y)-\tfrac34\|R(X,Y)u\|^2$ — **sign-indefinite, growing with $\|u\|^2$**. No number is quoted here because none is honestly available.

## What breaks

:::warning[Open question — the rescaling reduction]
[[27-set-erosion-tubes]] records that the Euclidean proofs reduce $c_t\ne0$ to $c_t=0$ via $\tilde X_t=e^{-\psi_t}X_t$ — scalar multiplication of a state, meaningless on $M$. **Proposed replacement: rescale the distance function, $\hat r_t=e^{-\psi_t}r$, not the state.** It is a scalar function on $M$ and the computation above goes through. Two things are lost. (i) $\|\mathrm{grad}\,\hat r\|=e^{-\psi_t}\ne1$, so the Gauss-lemma normalisation must be carried explicitly. (ii) Read as a homothety $\mathbb G\mapsto e^{-2\psi_t}\mathbb G$ it makes the metric time-dependent, moving $\mathrm{Sec}\mapsto e^{2\psi_t}\mathrm{Sec}$ and $\mathrm{inj}\mapsto e^{-\psi_t}\mathrm{inj}$ — but $\mathcal D$ is **scale-invariant** (problem 4b), so the two readings agree. What is *not* checked is whether this remains legitimate when $c_t$ is only locally valid, i.e. when the contracting region is not geodesically convex.
:::

:::warning[Open question — the cut locus]
$\Phi_\lambda$ is smooth on $B(\bar x,\mathrm{inj})$ and nowhere past it; on $\mathrm{Cut}(\bar x)$ the function $r$ has a corner and $\Delta r$ acquires a singular part. The escape hatch is that this singular part is a **negative** measure (Calabi's barrier trick; problem 4a verifies it on the torus), and $\varphi_N'\ge0$ means we need only an *upper* bound on $\Delta r$ — so the comparison inequality plausibly holds distributionally across $\mathrm{Cut}$. Turning that into a supermartingale needs an Itô–Tanaka argument with a nonpositive local-time term at $\mathrm{Cut}$; **no source in `refs/` does this**, and [[20-generator-on-manifolds]] already flagged that [[@leeGeometricInterpretationBrownian2025]] states no regularity hypotheses at all. Until it is done, the Proposition above carries the stopping time $\tau$.

Cost on $SO(3)$: $\mathrm{inj}=\pi=\mathrm{diam}$, so the restriction $r<\mathrm{inj}$ excludes only the $\mathbb{RP}^2$ of $\pi$-rotations — geometrically almost nothing. But it means any $r_{\delta,t}\ge\pi$ is *vacuous* rather than conservative: on a compact group the tube saturates at the diameter and the bound stops carrying information. On $SE(3)$, $\mathrm{inj}$ is not even constant.
:::

:::warning[Open question — subtraction of states and the moving fibre]
$S_t=X_t-x_t$ has no meaning on $M$; the replacement $\log_{\bar x_t}X_t$ lives in the moving space $T_{\bar x_t}M$. **For this construction that turns out not to matter**: $\Phi_\lambda$ depends on $\log_x\bar x$ only through its norm, so radiality absorbs the whole problem and the martingale argument never differentiates a moving-fibre object — the time-dependence of $\bar x_t$ enters only as the scalar $\partial_tr$, handled by the first variation of arc length. The failure reappears the moment an **anisotropic** tube is wanted: $\|X_t-x_t\|_{M_t}$ requires a shape tensor $M_t$ along $\bar x_t$, which must be parallel-transported, and $\tfrac{D}{dt}M_t$ then enters the contraction LMI. The ellipsoidal tubes of [[@liuSetErosionTubes]] have no intrinsic analogue yet.
:::

:::tip[Proposition — metric erosion survives]
Replace $\mathcal C\ominus B^N(r,0)$ by the **metric erosion** $\mathcal C\ominus_{\mathbb G}r:=\{y\in M:\ \overline B(y,r)\subseteq\mathcal C\}$. If $\mathbb P[d(X_t,\bar x_t)\le r_{\delta,t}\ \forall t\le T]\ge1-\delta$ and $\bar x_t\in\mathcal C\ominus_{\mathbb G}r_{\delta,t}$ for all $t\le T$, then $\mathbb P[X_t\in\mathcal C\ \forall t\le T]\ge1-\delta$.
:::

*Proof.* On the $(1-\delta)$ event, $X_t\in\overline B(\bar x_t,r_{\delta,t})\subseteq\mathcal C$ by definition of the erosion. $\square$ — **Confirmed: it is set algebra, and no vector-space structure was used.** [[27-set-erosion-tubes]]'s assumption-free erosion theorem transfers unchanged. The obstruction is computational, not logical: there is no support-function calculus for $\ominus_{\mathbb G}$, so eroding a safe set on $SO(3)$ is a genuine geodesic-distance computation.

:::warning[Open question — dimension, and which $N$]
[[26-euclidean-amgf]] locates all dimension dependence in $(1-\varepsilon^2)^{N/2}$, giving $\varepsilon_1N$ inside the radius and an additive $\sigma\sqrt N$. Here $N=\dim M$, so on $T^*G$ it is $2\dim G$: **$N=6$ for $T^*SO(3)$, $N=12$ for $T^*SE(3)$** (against $3$ and $6$ for configuration only). At $\varepsilon=\tfrac12$ ($\varepsilon_1=4\log\tfrac43\approx1.15$, $\varepsilon_2=8$) the dimension budget is $\varepsilon_1N\approx6.9$ and $13.8$, versus $\varepsilon_2\log(1/\delta)\approx73.7$ at $\delta=10^{-4}$ — so doubling the dimension by lifting to $T^*G$ costs $\approx4\%$ in the radius, which is cheap. Unsettled: whether the degenerate Case-A noise (below) permits a *smaller* effective $N$, since the diffusion has rank $\le\dim G$ in the fibre and rank $0$ on the base.
:::

## Why Case A matters

[[22-force-vs-configuration-noise]] shows that under force noise the quadratic variation sits entirely in the **flat** momentum fibre, so the noise contributes no curvature correction of its own: Itô $=$ Stratonovich for the configuration, and no mean-curvature drift. That is what makes the master identity clean — curvature enters *only* through $\mathcal D(r)$, one scalar, bounded by one comparison theorem. Under Case B the diffusion fields themselves would move the base, the Stratonovich drift would pick up $\tfrac12\sum_i\widetilde{\mathrm{ad}}_{e_i}e_i$, and $\Sigma$ would have to be differentiated covariantly inside $\mathcal A$; the two curvature entry points would then mix, which is exactly the mixing [[@daniObserverDesignStochastic2015]] never separates.

The price, already flagged in lesson 22: Case A is **hypoelliptic**. $\Sigma(\mathrm{grad}\,r,\mathrm{grad}\,r)$ can be far below $\sigma^2$ when $\mathrm{grad}\,r$ has a large configuration component, so $\Sigma\preceq\sigma^2\mathbb G^\sharp$ is valid but slack. The Proposition is therefore *sound and conservative* under Case A, and recovering the lost tightness is open.

## Problems

1. **Recall.** State the intrinsic AMGF definition, saying which $\log$ and which measure. Then give the two-step argument for why the definition is forced rather than chosen, and prove $-\log_x\bar x=r(x)\,\mathrm{grad}\,r|_x$.

2. **Compute.** In the constant-curvature model $M^N_\kappa$: write $\mathcal D(r)$ in closed form for $\kappa>0$, $\kappa=0$, $\kappa<0$; give its sign and its limits as $r\to0$ and $r\to\ell_\kappa$; and write $\Delta_M\Phi_\lambda$ explicitly for $N=3$, $\kappa=\tfrac14$ (i.e. $SO(3)$), using $\varphi_3(z)=\sinh z/z$.

3. **Prove.** (a) Verify $\varphi_3(z)=\sinh z/z$ satisfies $\varphi''+\tfrac2z\varphi'=\varphi$. (b) Show that $\kappa=0$ with $\mathcal D\equiv0$ recovers [[26-euclidean-amgf]] *exactly*: $\Delta\Phi_\lambda=\lambda^2\Phi_\lambda$, hence $a_t=\lambda^2\sigma^2/2$, $b_t=0$, hence the Euclidean radius. (c) Deduce that positive Ricci curvature can only shrink the tube.

4. **Break it.** (a) On the flat torus $T=\mathbb R^2/\mathbb Z^2$ ($N=2$, $\mathrm{Sec}\equiv0$, $\mathrm{inj}=\tfrac12$), use $\int_T\Delta r\,dV=0$ to show the singular part of $\Delta r$ on $\mathrm{Cut}(p)$ is a **negative** measure, and say why that is the direction the AMGF argument needs. Then explain why the flat bound $r_{\delta,t}\propto\sigma\sqrt t$ is eventually absurd on $T$. (b) Show $\mathcal D$ is invariant under $\mathbb G\mapsto a^2\mathbb G$, and conclude that the rescaling reduction cannot remove the curvature defect, only relocate the rate.

---

## Solutions

**1.** Definition as stated: $\log_x$ is the **Riemannian** log, and the measure on $S(T_xM)$ is the unique probability measure invariant under $O(T_xM,\mathbb G_x)$. Forced because (i) the Euclidean energy function is already $\varphi_N(\lambda\|x\|)$ — rotation-invariant and radial — so nothing chart-dependent is being replaced, and (ii) its only two ingredients, an inner product and an invariant sphere measure, exist canonically on every $T_xM$ with no choice. For the identity: let $\gamma$ be the unit-speed minimising geodesic from $\bar x$ to $x$, so $\gamma(r)=x$ and $\mathrm{grad}\,r|_x=\dot\gamma(r)$ ([[08-hessian-comparison]]). The reversed geodesic $s\mapsto\gamma(r-s)$ runs from $x$ to $\bar x$ with initial velocity $-\dot\gamma(r)$ and length $r$, so $\log_x\bar x=-r\,\dot\gamma(r)=-r\,\mathrm{grad}\,r$.

**2.** $\Delta r=(N-1)\mathrm{ct}_\kappa(r)$ with equality in the model, so $\mathcal D(r)=(N-1)(r\,\mathrm{ct}_\kappa(r)-1)$:
$$\kappa>0:\ (N-1)\big(\sqrt\kappa r\cot(\sqrt\kappa r)-1\big)<0;\qquad \kappa=0:\ 0;\qquad \kappa<0:\ (N-1)\big(\sqrt{|\kappa|}r\coth(\sqrt{|\kappa|}r)-1\big)>0.$$
All three $\to0$ as $r\to0$ (the manifold is Euclidean to leading order at the centre). As $r\to\pi/\sqrt\kappa$ the $\kappa>0$ case $\to-(N-1)$; as $r\to\infty$ the $\kappa<0$ case grows like $(N-1)\sqrt{|\kappa|}r$, though $\mathcal D/r$ stays bounded by $(N-1)\sqrt{|\kappa|}$. For $SO(3)$: $\varphi_3'(z)=\frac{\cosh z}{z}-\frac{\sinh z}{z^2}$, so
$$\Delta_M\Phi_\lambda=\lambda^2\frac{\sinh\lambda r}{\lambda r}+\frac{\lambda}{r}\Big(\frac{\cosh\lambda r}{\lambda r}-\frac{\sinh\lambda r}{\lambda^2r^2}\Big)\big(r\cot(r/2)-2\big).$$

**3(a).** $\varphi=\sinh z/z$, $\varphi'=\frac{\cosh z}{z}-\frac{\sinh z}{z^2}$, $\varphi''=\frac{\sinh z}{z}-\frac{2\cosh z}{z^2}+\frac{2\sinh z}{z^3}$, and $\frac2z\varphi'=\frac{2\cosh z}{z^2}-\frac{2\sinh z}{z^3}$. The last two terms of each cancel pairwise, leaving $\sinh z/z=\varphi$. ✓

**(b)** $\mathcal D\equiv0$ kills the second term of the master identity, giving $\Delta\Phi_\lambda=\lambda^2\Phi_\lambda$. With isotropic noise $\Sigma=\sigma^2\mathbb G^\sharp$ and $c_t$ scaled away, $\mathcal A\Phi_\lambda=\tfrac{\sigma^2}{2}\Delta\Phi_\lambda=\tfrac{\lambda^2\sigma^2}{2}\Phi_\lambda$, i.e. an affine martingale with $a_t=\lambda^2\sigma^2/2$, $b_t=0$ — the coefficients of [[@liuSetErosionTubes]] Thm 2. Doob plus the level-set lemma then give $r=\sqrt{\Psi_T(\varepsilon_1N+\varepsilon_2\log\frac1\delta)}$ with the same $\varepsilon_1,\varepsilon_2$. Nothing is lost and nothing is gained: the construction is a strict generalisation.

**(c)** $\mathrm{Ric}\ge0$ gives $\Delta r\le(N-1)/r$, so $\mathcal D\le0$; since $\varphi_N'\ge0$ and $r>0$, the correction term $\frac{\lambda\varphi_N'}{r}\mathcal D\le0$, so $\Delta_M\Phi_\lambda\le\lambda^2\Phi_\lambda$ pointwise. Every subsequent step ($a_t$, Doob, $\lambda$-optimisation) is monotone in $a_t$, so the radius can only shrink.

**4(a).** $T$ is closed, so $\int_T\Delta r\,dV=0$ for any $r$ whose Laplacian is taken distributionally. Off $\mathrm{Cut}(p)\cup\{p\}$, $r$ is the Euclidean distance to the nearest lift and $\Delta r=(N-1)/r=1/r>0$, so $\int_{T\setminus\mathrm{Cut}}\Delta r\,dV>0$ strictly. The total must vanish, so the singular part supported on $\mathrm{Cut}(p)$ carries mass $-\int_{T\setminus\mathrm{Cut}}\tfrac1r\,dV<0$: it is a negative measure. That is exactly the direction the AMGF needs, because the master identity multiplies $\Delta r$ by $\varphi_N'\ge0$, so a negative singular contribution only *strengthens* $\mathcal A\Phi_\lambda\le a_t\Phi_\lambda$. (It does not by itself prove the supermartingale property — one still needs an Itô–Tanaka argument to show the local time at $\mathrm{Cut}$ contributes with the right sign.) The flat radius is absurd on $T$ because $\mathrm{diam}(T)=1/\sqrt2$: once $r_{\delta,t}>1/\sqrt2$ the tube is the whole torus and the statement is vacuous. Compactness caps the tube by the diameter, and no flat bound knows this — the identical statement holds on $SO(3)$ at $r=\pi$.

**4(b).** Under $\mathbb G\mapsto a^2\mathbb G$: $r\mapsto ar$, $\mathrm{Sec}\mapsto\mathrm{Sec}/a^2$, hence $\mathrm{ct}_\kappa(r)\mapsto\mathrm{ct}_{\kappa/a^2}(ar)=\tfrac1a\mathrm{ct}_\kappa(r)$ and $\Delta r\mapsto\tfrac1a\Delta r$. So
$$\mathcal D\mapsto (ar)\big(\tfrac1a\Delta r\big)-(N-1)=r\Delta r-(N-1)=\mathcal D .$$
$\mathcal D$ is dimensionless and scale-invariant. Consequently the time-dependent homothety that implements the rescaling reduction changes $\sigma^2\mapsto\sigma^2e^{-2\psi_t}$ and $\mathrm{inj}\mapsto e^{-\psi_t}\mathrm{inj}$ but leaves the curvature defect at each geometric point exactly where it was. The reduction converts a contraction rate into a growing noise intensity — the $\Psi_T=\int\sigma^2e^{-2\psi_\tau}d\tau$ of the Euclidean theorem — and buys nothing against curvature. Any hope that "rescaling flattens the manifold" is false: it flattens the *numerical* curvature but rescales $r$ by the same factor, and only the product enters.
