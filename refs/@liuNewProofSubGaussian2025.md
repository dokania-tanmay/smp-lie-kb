---
tags: [reference, amgf, concentration, sub-gaussian, probability]
---
# A New Proof of Sub-Gaussian Norm Concentration Inequality (Zishun Liu, Sam Power, Yongxin Chen; arXiv:2503.14347v2, May 2025)

Six-page note that re-proves the sub-Gaussian norm concentration inequality $\mathbb P(\|X\|\le\sigma\sqrt{C_1 n + C_2\log(1/\delta)})\ge 1-\delta$ **without** an $\varepsilon$-net or a union bound, by introducing the *averaged moment generating function* (AMGF) $\Phi_X(\lambda)=\mathbb E_X\big[\mathbb E_{\ell\sim S^{n-1}}e^{\lambda\langle\ell,X\rangle}\big]$ and its **energy function** $\Phi_n$. This is the canonical reference for the object this project wants to make intrinsic: $\Phi_n$ is rotation-invariant and a function of $\|X\|$ alone, so replacing $\|x\|\mapsto d(x,\bar x)$ and $S^{n-1}\mapsto$ unit sphere in $T_xM$ is the forced generalization. Everything the AMGF is *for* is here in miniature: an upper bound inherited from the one-dimensional sub-Gaussian MGF (no cost for the average), a lower bound that is exponential in the norm, and Markov in between. Same skeleton as the affine-martingale + Doob route to sup-over-time tubes, minus the time dimension — the martingale machinery lives in the companion papers [[@liuSafetyVerificationStochastic2024a]], [[@liuProbabilisticReachabilityDiscreteTime2024]], [[@liuSafetyVerificationNonlinear2025]], [[@liuConcentrationStochasticSystem2026]].

## Notation

| Symbol | Meaning |
|---|---|
| $X\in\mathbb R^n$ | random vector, sub-Gaussian with variance proxy $\sigma^2$ |
| $S^{n-1}$ | $\{x\in\mathbb R^n:\|x\|=1\}$, Euclidean unit sphere; $\ell\sim S^{n-1}$ means uniform on it |
| $\Phi_X(\lambda)$ | AMGF of $X$: $\mathbb E_X[\Phi_n(\lambda X)]$ |
| $\Phi_n(\lambda X)$ | **energy function**, $\mathbb E_{\ell\sim S^{n-1}}[e^{\lambda\langle\ell,X\rangle}]$ |
| $\varphi_n(z)$ | radial profile: $\Phi_n(\lambda X)=\varphi_n(\|\lambda X\|)$ |
| $I_\nu$ | modified Bessel function of the first kind, order $\nu$ |
| $\Gamma$ | Gamma function |
| $\varepsilon\in(0,1)$ | free parameter of the lower bound (Lemma 2.1); *not* an $\varepsilon$-net radius |
| $\delta\in(0,1)$ | failure probability |
| $A\in\mathbb R^{m\times n}$, $\|A\|$ | random matrix and its **operator** norm |
| $\Phi_{m,n}(\lambda A)$ | matrix energy function, $\mathbb E_{u\sim S^{m-1},v\sim S^{n-1}}[e^{\lambda u^\top Av}]$ |

## Key definitions

:::info[Definition — sub-Gaussian vector, Def. 1.1]
$X\in\mathbb R$ is sub-Gaussian with variance proxy $\sigma^2>0$ if $\mathbb E_X[e^{\lambda X}]\le e^{\lambda^2\sigma^2/2}$ for all $\lambda\in\mathbb R$. A vector $X\in\mathbb R^n$ is sub-Gaussian with variance proxy $\sigma^2$ if $\langle\ell,X\rangle$ is, for **every** unit $\ell$:
$$\mathbb E_X\big[e^{\lambda\langle\ell,X\rangle}\big]\le e^{\lambda^2\sigma^2/2},\qquad\forall\lambda\in\mathbb R,\ \forall\ell\in S^{n-1}.$$
:::

:::info[Definition — AMGF, Def. 2.1]
$$\Phi_X(\lambda)=\mathbb E_X\big[\Phi_n(\lambda X)\big],\qquad \Phi_n(\lambda X)=\mathbb E_{\ell\sim S^{n-1}}\big[e^{\lambda\langle\ell,X\rangle}\big].$$
Read either way: an average of the MGF of the projection $\langle\ell,X\rangle$ over $\ell$, or an MGF whose exponential energy $e^{\lambda\langle\ell,X\rangle}$ has been replaced by its spherical average $\Phi_n$. Credited to Altschuler–Talwar (arXiv:2212.12629, "Concentration of the Langevin algorithm's stationary distribution"), where it was introduced for sampling; **not** in `refs/`.
:::

:::info[Definition — energy function is radial, eq. (6), §2]
$\Phi_n(\lambda X)=\varphi_n(\|\lambda X\|)$ where $\varphi_n(z)=\mathbb E_{\ell\sim S^{n-1}}[e^{\langle \ell, z\eta\rangle}]$ for any fixed $\eta\in S^{n-1}$ (well-defined precisely because the uniform measure on $S^{n-1}$ is rotation-invariant). Closed forms:
$$\varphi_1(z)=\cosh z,\qquad \varphi_n(z)=\Gamma(n/2)\,(2/z)^{(n-2)/2}\,I_{(n-2)/2}(z)\quad (n\ge2).$$
Also $\varphi_n(0)=1$.
:::

## Main results

:::tip[Theorem 1 — the target statement, §1]
For sub-Gaussian $X\in\mathbb R^n$ with variance proxy $\sigma^2$ there exist $C_1,C_2$ with, for any $\delta\in(0,1)$,
$$\mathbb P\Big(\|X\|\le\sigma\sqrt{C_1 n + C_2\log\tfrac1\delta}\Big)\ge1-\delta.$$
Baseline constants from the $\varepsilon$-net proof (eq. (4)), valid for any net radius $\varepsilon\in(0,1)$:
$$C_1=\frac{2\log\!\big(1+\tfrac{2}{1-\varepsilon}\big)}{\varepsilon^2},\qquad C_2=\frac{2}{\varepsilon^2}.$$
At $\varepsilon=\tfrac12$ the paper writes $C_1=8\log5\approx16$, $C_2=8$ (the numeral $16$ looks wrong — $8\log5\approx12.9$; see caveats).
:::

:::tip[Lemma 2.1 — exponential-growth lower bound on the energy function, §2, eq. (7)]
For any $X\in\mathbb R^n$, any $\lambda$, and **any** $\varepsilon\in(0,1)$,
$$\Phi_n(\lambda X)\ \ge\ (1-\varepsilon^2)^{n/2}\,e^{\varepsilon\|\lambda X\|}.$$
This is the whole trick: $\Phi_n$ grows like a genuine exponential in the norm, at rate $\varepsilon$ arbitrarily close to $1$, paid for by the prefactor $(1-\varepsilon^2)^{n/2}$ which is where **all** the dimension dependence enters.

*Proof technique.* $n=1$: convexity of $\log\cosh z-\log(\sqrt{1-\varepsilon^2}e^{\varepsilon z})$. $n\ge2$: the identity (eq. (10))
$$\frac{d}{dz}\log\varphi_n(z)=\frac{I_{n/2}(z)}{I_{n/2-1}(z)},$$
then Amos' (1974) lower bound on the Bessel ratio (eq. (11))
$$\frac{I_{n/2}(z)}{I_{n/2-1}(z)}\ \ge\ \sqrt{1+\Big(\frac{n}{2z}\Big)^2}-\frac{n}{2z}\ =:\ g(z),$$
so $\log\varphi_n(z)\ge G(z):=\int_0^z g$. $g$ is increasing on $z>0$, hence $G$ is convex, hence $G(z)\ge g(z_0)(z-z_0)+G(z_0)$; the choice $z_0=\dfrac{\varepsilon n}{1-\varepsilon^2}$ gives $g(z_0)=\varepsilon$ and $G(z_0)=\dfrac{n\varepsilon^2}{1-\varepsilon^2}+\dfrac n2\log(1-\varepsilon^2)$, yielding $\log\varphi_n(z)\ge\varepsilon z+\tfrac n2\log(1-\varepsilon^2)$ (eq. (15)).
:::

:::tip[Proposition — the AMGF inherits the scalar sub-Gaussian bound, eq. (16), §2]
By Fubini (swap $\mathbb E_X$ and $\mathbb E_\ell$) and Def. 1.1,
$$\Phi_X(\lambda)=\mathbb E_X\mathbb E_{\ell\sim S^{n-1}}\big[e^{\lambda\langle\ell,X\rangle}\big]=\mathbb E_{\ell}\mathbb E_X\big[e^{\lambda\langle\ell,X\rangle}\big]\le e^{\lambda^2\sigma^2/2}.$$
**The averaging is free**: the AMGF obeys exactly the same bound as a single fixed projection's MGF. Combined with Lemma 2.1 this converts into the bound one actually wanted but could not get directly (eq. (20), with $t=\varepsilon|\lambda|$):
$$\mathbb E_X\big[e^{t\|X\|}\big]\ \le\ (1-\varepsilon^2)^{-n/2}\exp\!\Big(\frac{\sigma^2t^2}{2\varepsilon^2}\Big).$$
:::

:::tip[Theorem 2 — $\varepsilon$-parameterized concentration, §2, eq. (17)]
$X\in\mathbb R^n$ sub-Gaussian with variance proxy $\sigma^2$. Then for any $\delta\in(0,1)$ and any $\varepsilon\in(0,1)$,
$$\mathbb P\left(\|X\|\le\sigma\sqrt{\frac{\log\frac{1}{1-\varepsilon^2}}{\varepsilon^2}\,n+\frac{2}{\varepsilon^2}\log\frac1\delta}\right)\ \ge\ 1-\delta,$$
i.e. Theorem 1 with (eq. (23))
$$C_1=\frac{\log\frac{1}{1-\varepsilon^2}}{\varepsilon^2},\qquad C_2=\frac{2}{\varepsilon^2}.$$
*Proof technique.* Lemma 2.1 + eq. (16) $\Rightarrow$ eq. (20); Markov on $e^{t\|X\|}$; minimize $\frac{\sigma^2t^2}{2\varepsilon^2}-rt$ over $t$ (minimum $-\frac{\varepsilon^2r^2}{2\sigma^2}$ at $t=\varepsilon^2 r/\sigma^2$); set $\delta=(1-\varepsilon^2)^{-n/2}e^{-\varepsilon^2r^2/(2\sigma^2)}$ and solve for $r$.

**Comparison with the $\varepsilon$-net constants (4).** Same $C_2=2/\varepsilon^2$; $C_1$ is strictly smaller for every $\varepsilon\in(0,1)$, since $2\log(1+\tfrac2{1-\varepsilon})>\log\frac1{1-\varepsilon^2}$. At $\varepsilon=\tfrac12$: AMGF gives $C_1=4\log\frac43\approx1.15$ against the net's $8\log5\approx12.9$.
:::

:::tip[Theorem 3 — $\varepsilon$-free concentration, §2, eq. (24)]
$X\in\mathbb R^n$ sub-Gaussian with variance proxy $\sigma^2$. Then for any $\delta\in(0,1)$,
$$\mathbb P\Big(\|X\|\le\sigma\big(\sqrt n+\sqrt{2\log(1/\delta)}\big)\Big)\ \ge\ 1-\delta.$$
*Proof technique.* Optimize eq. (20) over $\varepsilon$ before applying Markov. Use $\log(1-\varepsilon^2)\ge\frac{\varepsilon^2}{\varepsilon^2-1}$ to get
$$\mathbb E_X\big[e^{t\|X\|}\big]\le\min_{\varepsilon\in(0,1)}\exp\Big(\frac{n\varepsilon^2}{2(1-\varepsilon^2)}+\frac{\sigma^2t^2}{2\varepsilon^2}\Big)\quad\text{(eq. (25))},$$
then Cauchy–Schwarz gives the exact minimum $\exp\big(\tfrac12(\sqrt n+\sigma t)^2-\tfrac n2\big)$ at $\varepsilon_*=\sqrt{\frac{\sigma t}{\sigma t+\sqrt n}}$ (eq. (26)). Markov then gives $\mathbb P(\|X\|\ge\sigma(\sqrt n+r))\le\exp(\tfrac12\sigma^2t^2-\sigma rt)$, and $t=r/\sigma$ yields $e^{-r^2/2}$.

Matches Zhivotovskiy (EJP 2024, Remark 6) via the variational principle. Slightly weaker than Hsu–Kakade–Zhang (ECP 2012, Thm 1), $\mathbb P\big(\|X\|\ge\sigma\sqrt{n+2\sqrt{n\log(1/\delta)}+2\log(1/\delta)}\big)\le\delta$ — whose proof averages the MGF over $\ell\sim\mathcal N(0,I)$ instead of uniform on $S^{n-1}$.
:::

:::tip[Lemma 3.1 + Theorem 4 — matrix operator norm, §3]
$A\in\mathbb R^{m\times n}$ is sub-Gaussian with variance proxy $\sigma^2$ if $\mathbb E A=0$ and $\mathbb E_A[e^{\lambda u^\top Av}]\le e^{\lambda^2\sigma^2/2}$ for all $\lambda\in\mathbb R$, $u\in S^{m-1}$, $v\in S^{n-1}$ (eq. (28)). With $\Phi_{m,n}(\lambda A)=\mathbb E_{u,v}[e^{\lambda u^\top Av}]$:

**Lemma 3.1 (eq. (30)).** For any $\varepsilon\in(0,1)$, $\ \Phi_{m,n}(\lambda A)\ge(1-\varepsilon^2)^{\frac{m+n}{2}}e^{\varepsilon^2\|\lambda A\|}$ — note the rate is $\varepsilon^{\mathbf 2}$, not $\varepsilon$, because Lemma 2.1 is applied twice (once in $u$, once in $v$, via the SVD $A=U\Sigma V$ and $\|\Sigma v\|\ge\sigma_1v_1=\|A\|\langle\ell_1,v\rangle$).

**Theorem 4.** For any $\delta\in(0,1)$ and $\varepsilon\in(0,1)$,
$$\mathbb P\left(\|A\|\le\sigma\sqrt{\frac{\log\frac{1}{1-\varepsilon^2}}{\varepsilon^4}(m+n)+\frac{2}{\varepsilon^4}\log\frac1\delta}\right)\ge1-\delta.$$
(Second constant reconstructed from the proof; the typeset display may read $4/\varepsilon^4$ — see caveats.) Same technique, with $t=\varepsilon^4r/\sigma^2$ minimizing $\frac{\sigma^2t^2}{2\varepsilon^4}-rt$. **The entries of $A$ are not assumed independent**, unlike the $\varepsilon$-net proof (Vershynin, Ch. 4).
:::

## What this gives the project

- **The exact object to make intrinsic.** $\Phi_n(\lambda X)=\varphi_n(\|\lambda X\|)$ (eq. (6)) is rotation-invariant and radial *by construction*: the only inputs are the inner product $\langle\ell,X\rangle$ and the uniform measure on $S^{n-1}$. On a manifold, $\ell\sim S^{n-1}\subset T_xM$ (normalized measure from $g_x$) and $\langle\ell,\cdot\rangle$ replaced by e.g. $\langle\ell,\log_{\bar x}x\rangle$ or $d(x,\bar x)$ — no chart enters the *definition*, which is the point.
- **The two-sided sandwich is the reusable template.** Upper: $\Phi_X(\lambda)\le e^{\lambda^2\sigma^2/2}$, free by Fubini. Lower: $\Phi_n\ge(1-\varepsilon^2)^{n/2}e^{\varepsilon\|\lambda X\|}$. Markov in between. For a sup-over-time tube, the upper bound is what an affine-martingale/generator argument must supply for $\Phi$; Lemma 2.1 is what converts a level set of $\Phi$ back into a level set of distance, and it is *purely deterministic and pointwise* — so it transports to a manifold as soon as $\varphi_n$'s manifold analogue is controlled.
- **Dimension dependence is isolated in one place.** $n$ appears only through the prefactor $(1-\varepsilon^2)^{n/2}$ in Lemma 2.1, i.e. an additive $\frac n2\log\frac1{1-\varepsilon^2}$ in the exponent, giving the $C_1n$ term and ultimately the additive $\sigma\sqrt n$ in Theorem 3. The $\log(1/\delta)$ term is dimension-free. The optimal linearization point $z_0=\varepsilon n/(1-\varepsilon^2)$ scales linearly in $n$, and $\varepsilon_*=\sqrt{\sigma t/(\sigma t+\sqrt n)}\to0$ as $n\to\infty$ at fixed $t$. Nothing here blows up worse than $\sqrt n$ — for a manifold version, $n=\dim M$ and this is the constant to watch.
- **Why not just $\mathbb E[e^{\lambda\|X\|}]$.** The paper says it plainly (§2): the sub-Gaussian definition gives no handle on $\mathbb E[e^{\lambda\|X\|}]$ — literature usually goes the other way, deducing it *from* norm concentration. AMGF is the surrogate that is simultaneously (i) bounded above by the definition, and (ii) exponentially large in $\|X\|$. This is exactly the substitution the tube proof needs, and it is why the intrinsic version should carry $\Phi$ rather than $e^{\lambda d}$.
- **No union bound, no net.** The $\varepsilon$-net proof pays $\log(1+\frac{2}{1-\varepsilon})$ per net point and needs independence in the matrix case. Removing both is a strict tightening — the same style of conservatism removal this project runs on the chart-dependent constants of [[@daniObserverDesignStochastic2015]], and worth citing as precedent for "the standard proof's constants are artifacts of the proof, not of the problem".
- **Bessel machinery is where the geometry will bite.** The lower bound is nothing but Amos' bound on $I_{n/2}/I_{n/2-1}$ plus convexity. Any curved-space analogue of $\varphi_n$ will need the corresponding spherical-average asymptotics; the Bessel closed form only holds for the flat $S^{n-1}$ average.

## Caveats / limitations

- **Purely Euclidean, purely static.** No manifold, no time, no martingale, no SDE. There is no process here at all — this is a one-shot inequality for a single random vector/matrix. The dynamic AMGF (affine martingale + Doob) lives in the companion Liu–Chen papers, not here.
- **Only sub-Gaussian.** Both the upper bound (16) and the final constants use $\mathbb E[e^{\lambda\langle\ell,X\rangle}]\le e^{\lambda^2\sigma^2/2}$ for *every* unit $\ell$ with a *single* $\sigma$ — i.e. isotropic variance proxy. Anisotropy is not exploited. The conclusion claims extension to sub-exponential distributions but does not carry it out.
- **$\varepsilon$ still has to be picked.** Theorem 2 is a one-parameter family; the paper says only "choose $\varepsilon$ according to $n$ and $\delta$". Theorem 3 removes $\varepsilon$ but is then not optimal for every $(n,\delta)$ — the two are incomparable in practice.
- **Not the tightest known.** Hsu–Kakade–Zhang (ECP 2012, Thm 1) is strictly better; the paper's claim is methodological (no union bound; handles dependent matrix entries), not that the constants are optimal.
- **Typo in Theorem 4's hypothesis.** Stated "for any $r>0$" although the displayed inequality is in terms of $\delta$; it should read "for any $\delta\in(0,1)$".

:::warning[Open question — two extraction gaps, flagged not guessed]
1. **Theorem 4's second constant.** `pdftotext` renders the display as containing "$+\,4\log\frac1\delta$", but the proof's own definition $\delta=(1-\varepsilon^2)^{-\frac{m+n}{2}}\exp(-\frac{\varepsilon^4r^2}{2\sigma^2})$ (eq. (36)) inverts to $C_2=2/\varepsilon^4$, not $4/\varepsilon^4$. I have written $2/\varepsilon^4$ above because it is what the proof yields; **verify against the typeset PDF before quoting this constant.** (The vector analogue, Theorem 2, is unambiguous: eq. (23) states $C_1,C_2$ separately and they match the proof.)
2. **"$C_1=8\log5\approx16$"** after eq. (4): $8\log5\approx12.88$, so either the numeral $16$ is a slip or a different rounding/convention is intended. The symbolic form $C_1=2\log(1+\frac{2}{1-\varepsilon})/\varepsilon^2$ extracted cleanly and is what should be quoted.
3. The garbled inequality chain immediately after eq. (23), which quantifies *by how much* AMGF's $C_1$ beats the net's, did not extract as a readable formula. Only the conclusion (strict improvement for all $\varepsilon\in(0,1)$, same $C_2$) is recorded above.
:::
