---
tags: [amgf, concentration, sub-gaussian, probability, euclidean]
---
# The Euclidean AMGF

**Prereq:** [[23-martingale-toolkit]], [[notation]], [[probability-on-manifolds]] (MGFs, Markov, Fubini)
**Goal:** define the averaged MGF and its energy function, know the three properties that make it work, and be able to say — quantitatively — why it beats the naive $\mathbb E[e^{\lambda\|X\|}]$.

Everything here is [[@liuNewProofSubGaussian2025]], reorganised. Purely Euclidean, purely static: **no manifold, no time, no martingale.** One random vector, one inequality. That is deliberate — this is the object lesson 28 has to make intrinsic, and it is easier to see what is essential about it with the dynamics stripped out.

*Dimension symbol.* Throughout the AMGF lessons $n$ is **the dimension of the space the sphere average runs over** — the *state* dimension, written $N$ in [[notation]]. It is **not** $\dim G$. On $T^*G$ the state is $(g,\mu)$, so $n=N=2\dim G$; on $G$ alone $n=\dim G$. Say which every time.

## Definitions

:::info[Definition — energy function and AMGF, [[@liuNewProofSubGaussian2025]] Def. 2.1]
For $x\in\mathbb R^n$, $\lambda\in\mathbb R$, the **energy function** and the **AMGF** of a random vector $X$ are
$$\Phi_{n,\lambda}(x)=\mathbb E_{\ell\sim S^{n-1}}\big[e^{\lambda\langle\ell,x\rangle}\big],
\qquad
\Phi_X(\lambda)=\mathbb E_X\big[\Phi_{n,\lambda}(X)\big],$$
$\ell$ uniform on the Euclidean unit sphere. The source writes $\Phi_n(\lambda X)$ for $\Phi_{n,\lambda}(X)$; same object.
:::

It is the MGF **averaged over the unit sphere** instead of evaluated along one fixed direction. Read the other way: an ordinary MGF whose exponential energy has been pre-averaged.

:::info[Definition — sub-Gaussian vector, Def. 1.1]
$X\in\mathbb R^n$ is sub-Gaussian with variance proxy $\sigma^2$ if every scalar projection is:
$$\mathbb E_X\big[e^{\lambda\langle\ell,X\rangle}\big]\le e^{\lambda^2\sigma^2/2}\qquad\forall\lambda\in\mathbb R,\ \forall\ell\in S^{n-1}.$$
A single $\sigma$ for all $\ell$ — the variance proxy is isotropic, and anisotropy is not exploited anywhere below.
:::

## Radiality — the reason lesson 28 is forced

The uniform measure on $S^{n-1}$ is rotation-invariant, so for any $R\in O(n)$, $\Phi_{n,\lambda}(Rx)=\Phi_{n,\lambda}(x)$. Hence $\Phi_{n,\lambda}$ **depends on $x$ only through $\|x\|$**:

:::info[Definition — radial profile, eq. (6)]
$$\Phi_{n,\lambda}(x)=\varphi_n(\|\lambda x\|),\qquad
\varphi_1(z)=\cosh z,\qquad
\varphi_n(z)=\Gamma(n/2)\Big(\tfrac2z\Big)^{(n-2)/2}I_{(n-2)/2}(z)\ \ (n\ge2),$$
$I_\nu$ the modified Bessel function of the first kind. $\varphi_n(0)=1$ for every $n$.
:::

This is the whole reason the AMGF is the object this project wants. The only two ingredients in the definition are the inner product and the uniform measure on the unit sphere — **no chart, no basis, no coordinates**. So the manifold version is not invented, it is read off: replace $\|x\|$ by $d(x,\bar x)$ and $S^{n-1}$ by the unit sphere in $T_xM$ with the measure induced by $g_x$. Flagged forward to [[28-intrinsic-amgf]]; contrast with $e^{\lambda\|x\|}$, which is radial too but has no such average behind it and, as below, no usable upper bound.

## Worked example — computing $\varphi_n$ directly

**$n=1$.** $S^0=\{+1,-1\}$ with the uniform measure putting $\tfrac12$ on each, so from the definition alone
$$\varphi_1(z)=\tfrac12e^{z\cdot(+1)}+\tfrac12e^{z\cdot(-1)}=\cosh z .$$
Cross-check against the Bessel form, which does extend to $n=1$ with $\nu=-\tfrac12$: $I_{-1/2}(z)=\sqrt{2/(\pi z)}\cosh z$, so $\Gamma(\tfrac12)(2/z)^{-1/2}I_{-1/2}(z)=\sqrt\pi\cdot\sqrt{z/2}\cdot\sqrt{2/(\pi z)}\cosh z=\cosh z$. ✓

**$n=3$.** Fix $\eta\in S^2$ and write $\langle\ell,z\eta\rangle=z\cos\theta$. The uniform measure on $S^2$ pushes forward to $\tfrac12\sin\theta\,d\theta$ on $\theta\in[0,\pi]$ (Archimedes: $u=\cos\theta$ is uniform on $[-1,1]$), so
$$\varphi_3(z)=\tfrac12\int_{-1}^{1}e^{zu}\,du=\frac{e^z-e^{-z}}{2z}=\frac{\sinh z}{z}.$$
Bessel check: $\Gamma(\tfrac32)=\tfrac{\sqrt\pi}2$, $I_{1/2}(z)=\sqrt{2/(\pi z)}\sinh z$, and $\tfrac{\sqrt\pi}{2}(2/z)^{1/2}\sqrt{2/(\pi z)}\sinh z=\sinh z/z$. ✓

Both have $\varphi_n(z)\to1$ as $z\to0$ — immediate from the definition, since $e^0=1$ pointwise in $\ell$, in **every** dimension.

## The three properties

:::tip[Lemma — properties of the energy function, Lemma 2.1 + §2]
1. **Rotation invariance.** $\Phi_{n,\lambda}(Rx)=\Phi_{n,\lambda}(x)$ for $R\in O(n)$; equivalently $\Phi_{n,\lambda}(x)=\varphi_n(\|\lambda x\|)$. *Role:* it is what makes $\Phi$ a function of a **distance**, hence transportable to a manifold at all.
2. **Monotonicity.** $\varphi_n$ is even and increasing on $z\ge0$, with $\varphi_n\ge1$. *Role:* a sublevel set of $\Phi$ **is** a ball, so the final inversion step is well posed.
3. **Exponential growth from below.** For every $\varepsilon\in(0,1)$,
$$\Phi_{n,\lambda}(x)\ \ge\ (1-\varepsilon^2)^{n/2}\,e^{\varepsilon\|\lambda x\|}\qquad\text{(eq. (7))}.$$
*Role:* the surrogate is at least as big as a genuine exponential in the norm, at rate $\varepsilon$ arbitrarily close to $1$ — so an upper bound on $\Phi$ really does bound $\|x\|$.
:::

Property 3 is the entire technical content. Its proof ([[@liuNewProofSubGaussian2025]] §2) is $\tfrac{d}{dz}\log\varphi_n=I_{n/2}/I_{n/2-1}$, then Amos' 1974 lower bound on that Bessel ratio, then convexity: linearise $\log\varphi_n$ at $z_0=\varepsilon n/(1-\varepsilon^2)$, chosen so the slope is exactly $\varepsilon$.

## Why $\Phi$ and not $\mathbb E[e^{\lambda\|X\|}]$

**The crux in one line.** $\|X\|=\sup_{\ell\in S^{n-1}}\langle\ell,X\rangle$, and $\sup$ does **not** commute with $\mathbb E$. The AMGF replaces that $\sup$ by an *average*, and average **does** commute, by Fubini:

:::tip[Proposition — the averaging is free, eq. (16)]
$$\Phi_X(\lambda)=\mathbb E_X\mathbb E_{\ell}\big[e^{\lambda\langle\ell,X\rangle}\big]
=\mathbb E_{\ell}\mathbb E_X\big[e^{\lambda\langle\ell,X\rangle}\big]\le e^{\lambda^2\sigma^2/2}.$$
The AMGF obeys **exactly** the scalar sub-Gaussian bound of a single fixed projection — the sphere average costs nothing. Combined with property 3, with $t=\varepsilon|\lambda|$ (eq. (20)):
$$\mathbb E_X\big[e^{t\|X\|}\big]\ \le\ (1-\varepsilon^2)^{-n/2}\exp\!\Big(\frac{\sigma^2t^2}{2\varepsilon^2}\Big).$$
:::

Property 3 says the average is nearly as large as the sup anyway. So the AMGF is the unique-looking compromise: **large enough to see $\|X\|$, small enough for the definition to bound it.** The sub-Gaussian hypothesis gives no handle on $\mathbb E[e^{\lambda\|X\|}]$ directly — the literature usually runs the deduction the other way, getting it *from* norm concentration.

Markov on the displayed bound, optimised in $t$, gives the payoff:

:::tip[Theorem 2 — $\varepsilon$-parameterised concentration, eq. (17)]
For any $\delta\in(0,1)$ and any $\varepsilon\in(0,1)$,
$$\mathbb P\Big(\|X\|\le\sigma\sqrt{C_1n+C_2\log\tfrac1\delta}\Big)\ge1-\delta,
\qquad C_1=\frac{\log\frac1{1-\varepsilon^2}}{\varepsilon^2},\quad C_2=\frac2{\varepsilon^2}.$$
Optimising over $\varepsilon$ *before* Markov removes the parameter entirely (**Theorem 3**, eq. (24)):
$$\mathbb P\Big(\|X\|\le\sigma\big(\sqrt n+\sqrt{2\log(1/\delta)}\big)\Big)\ge1-\delta .$$
:::

**Against the $\varepsilon$-net route.** The classical proof covers $S^{n-1}$ by a net of radius $1-\varepsilon$ (so $|\mathcal N|\le(1+\tfrac2{1-\varepsilon})^n$ and $\|X\|\le\tfrac1\varepsilon\max_{\mathcal N}\langle\ell,X\rangle$), applies the scalar bound at each net point, and pays a union bound. That yields the same $C_2=2/\varepsilon^2$ but $C_1=2\log(1+\tfrac2{1-\varepsilon})/\varepsilon^2$, strictly worse for every $\varepsilon\in(0,1)$. **At $\varepsilon=\tfrac12$: AMGF $C_1=4\log\tfrac43\approx1.15$ against the net's $8\log5\approx12.9$** — a factor $\approx11$ in $C_1$, i.e. $\approx3.3$ in the radius whenever the $n$ term dominates. The AMGF also needs no independence assumption in the matrix version (Theorem 4).

*Two source-side numerals, carried forward not resolved.* (i) [[@liuNewProofSubGaussian2025]] writes "$C_1=8\log5\approx16$" after eq. (4), but $8\log5\approx12.88$; the symbolic form is what should be quoted, and which numeral is intended is unresolved. (ii) Theorem 4's second constant renders as $4\log\frac1\delta$ in the PDF text while its own proof (eq. (36)) inverts to $2/\varepsilon^4$. Do not quote either without checking the typeset paper.

## Where the dimension enters, and what transports

**All** dimension dependence sits in the prefactor $(1-\varepsilon^2)^{n/2}$ of property 3 — an additive $\tfrac n2\log\tfrac1{1-\varepsilon^2}$ in the exponent, the $C_1n$ term in Theorem 2, and finally the additive $\sigma\sqrt n$ in Theorem 3. The $\log(1/\delta)$ term is **dimension-free**. So on a Lie group it is the $\sigma\sqrt n$ term that becomes $\sigma\sqrt{\dim G}$ for a tube on $G$, or $\sigma\sqrt{2\dim G}$ for one on $T^*G$; the confidence term does not move. Nothing here is worse than $\sqrt n$, which is the sanity bar lesson 28's constants must clear.

**The step that transports cleanly.** Property 3 converts a level set of $\Phi$ back into a level set of $\|x\|$, and it contains **no probability at all** — it is a deterministic, pointwise inequality between two functions on $\mathbb R^n$. The probabilistic half (Fubini + sub-Gaussianity) and the geometric half are completely separated. On a manifold the probabilistic half is replaced by an affine-martingale/generator argument ([[23-martingale-toolkit]]), and property 3 is the piece that carries over verbatim *if* $\varphi_n$'s curved analogue can be controlled.

:::warning[Open question]
The Bessel closed form and Amos' ratio bound both use the average being over a **flat** $S^{n-1}$ — the pushforward of the uniform measure onto $\langle\ell,\eta\rangle$ is exactly the flat one. Move the average to the unit sphere in $T_xM$ with $\Phi$ evaluated on $d(x,\bar x)$ and neither derivation applies as written: the profile is no longer a Bessel function, and whether an $(1-\varepsilon^2)^{n/2}e^{\varepsilon z}$-shaped bound survives — with what curvature-dependent correction — is exactly [[28-intrinsic-amgf]]'s problem. Flagging it as open, not assuming it.
:::

## Problems

1. **Recall.** State $\Phi_{n,\lambda}$ and $\Phi_X$ from memory, and the three properties of the energy function with the role each plays. Then: in $\mathbb P(\|X\|\le\sigma(\sqrt n+\sqrt{2\log(1/\delta)}))\ge1-\delta$, which term carries the dimension, and what is $n$ if the state is a point of $T^*SO(3)$?

2. **Compute.** (a) Derive $\varphi_2(z)=\tfrac1{2\pi}\int_0^{2\pi}e^{z\cos\theta}d\theta$ from the definition and identify it with the Bessel form. (b) Verify $\varphi_n(0)=1$ for every $n$ directly from the definition, and confirm the $n=3$ closed form gives $\sinh(z)/z\to1$.

3. **Prove.** (a) Show $\Phi_{n,\lambda}(x)\ge1$ for all $x,\lambda,n$ in one line. (b) Show $\varphi_n$ is even and increasing on $z\ge0$, hence $\|x\|\mapsto\Phi_{n,\lambda}(x)$ is monotone. *Hint for both:* use the symmetry $\ell\mapsto-\ell$ of the uniform measure.

4. **Break it.** Run the $\varepsilon$-net argument yourself and locate the loss. (a) Using $\|X\|\le\tfrac1\varepsilon\max_{\ell\in\mathcal N}\langle\ell,X\rangle$ for a net of radius $1-\varepsilon$, with $|\mathcal N|\le(1+\tfrac2{1-\varepsilon})^n$, derive $C_1=2\log(1+\tfrac2{1-\varepsilon})/\varepsilon^2$, $C_2=2/\varepsilon^2$. (b) Say exactly which step is absent from the AMGF proof, and why $\mathbb E[e^{\lambda\|X\|}]$ cannot be bounded by the sub-Gaussian definition without it. (c) Compare $C_1$ at $\varepsilon=\tfrac12$ and give the resulting ratio of tube radii for large $n$ at fixed $\delta$. Is the gain a constant factor or does it worsen with $n$?

---

## Solutions

**1.** Definitions as above. Properties: rotation invariance ⟹ $\Phi$ is a function of a distance, so it transports to a manifold; monotonicity ⟹ sublevel sets of $\Phi$ are balls, so the inversion is well posed; exponential lower bound ⟹ an upper bound on $\Phi$ genuinely bounds $\|X\|$. The dimension sits in $\sigma\sqrt n$; $\log(1/\delta)$ is dimension-free. $\dim SO(3)=3$, so $T^*SO(3)$ has $n=N=6$.

**2.** (a) For $n=2$ take $\eta=e_1$ and parameterise $\ell=(\cos\theta,\sin\theta)$ with $\theta$ uniform on $[0,2\pi)$; then $\langle\ell,z\eta\rangle=z\cos\theta$ and $\varphi_2(z)=\tfrac1{2\pi}\int_0^{2\pi}e^{z\cos\theta}d\theta$, which is the standard integral representation of $I_0(z)$. The formula gives $\Gamma(1)(2/z)^0I_0(z)=I_0(z)$. ✓ (b) At $z=0$ the integrand is $e^0=1$ for every $\ell$, so the average is $1$ regardless of $n$ — no Bessel needed. And $\sinh(z)/z=1+z^2/6+O(z^4)\to1$.

**3.** (a) $\mathbb E_\ell[\ell]=0$ by the symmetry $\ell\mapsto-\ell$, so Jensen on the convex function $e^{(\cdot)}$ gives $\mathbb E_\ell[e^{\lambda\langle\ell,x\rangle}]\ge e^{\lambda\langle\mathbb E_\ell[\ell],x\rangle}=e^0=1$.
(b) The same symmetry lets one pair $\ell$ with $-\ell$: writing $u=\langle\ell,\eta\rangle$ for a fixed unit $\eta$,
$$\varphi_n(z)=\mathbb E_\ell\big[\tfrac12(e^{zu}+e^{-zu})\big]=\mathbb E_\ell\big[\cosh(zu)\big].$$
$\cosh$ is even, so $\varphi_n(-z)=\varphi_n(z)$; and $\cosh(zu)$ is nondecreasing in $z\ge0$ for each fixed $u$ (since $|zu|$ is), so the expectation is too — strictly increasing unless $u\equiv0$, which fails for $n\ge1$. Then $\Phi_{n,\lambda}(x)=\varphi_n(|\lambda|\,\|x\|)$ is nondecreasing in $\|x\|$. (a) also follows from $\cosh\ge1$.

**4.** (a) Standard: $|\mathcal N|\le(1+2/\rho)^n$ for a $\rho$-net of $S^{n-1}$, here $\rho=1-\varepsilon$. For each fixed $\ell$, sub-Gaussianity plus Chernoff gives $\mathbb P(\langle\ell,X\rangle>s)\le e^{-s^2/2\sigma^2}$. Union bound over the net:
$$\mathbb P\big(\max_{\mathcal N}\langle\ell,X\rangle>s\big)\le|\mathcal N|e^{-s^2/2\sigma^2}\le\exp\Big(n\log\big(1+\tfrac2{1-\varepsilon}\big)-\tfrac{s^2}{2\sigma^2}\Big).$$
Setting the right side to $\delta$ gives $s=\sigma\sqrt{2n\log(1+\tfrac2{1-\varepsilon})+2\log\tfrac1\delta}$, and $\|X\|\le s/\varepsilon$ produces exactly $C_1=2\log(1+\tfrac2{1-\varepsilon})/\varepsilon^2$, $C_2=2/\varepsilon^2$.
(b) The missing step is the **union bound**, and behind it the discretisation of the sup. It is forced because $\|X\|=\sup_\ell\langle\ell,X\rangle$ and $\mathbb E[e^{\lambda\sup_\ell(\cdot)}]\ne\sup_\ell\mathbb E[e^{\lambda(\cdot)}]$: the sub-Gaussian definition controls each direction *separately*, one $\ell$ at a time, and nothing in it controls the supremum. So the sup must be approximated by finitely many directions, and each one costs a factor in the union bound. The AMGF replaces the sup by an average, which commutes with $\mathbb E$ by Fubini — no discretisation, no union bound, no net constant. The price is that the average is smaller than the sup, and property 3 is what shows the price is only $(1-\varepsilon^2)^{n/2}$.
(c) $\varepsilon=\tfrac12$: net $C_1=8\log5\approx12.88$ (the paper's "$\approx16$" is a slip — flagged above), AMGF $C_1=4\log\tfrac43\approx1.15$. For large $n$ at fixed $\delta$ the radius is $\approx\sigma\sqrt{C_1n}$, so the ratio is $\sqrt{12.88/1.15}\approx3.3$. **It is a constant factor, not a widening one** — both bounds are $\Theta(\sqrt n)$, and Theorem 3 ($\sigma\sqrt n$, i.e. $C_1=1$) shows $\sqrt n$ is not improvable in order. So the gain is in the constant, exactly the kind of "the standard proof's constants are artifacts of the proof, not of the problem" that this project runs on the chart-dependent constants of [[@daniObserverDesignStochastic2015]]. Worth noting for lesson 29: a factor $3.3$ in radius is the *same order* as the conservatism being chased there, so the two must not be double-counted.
