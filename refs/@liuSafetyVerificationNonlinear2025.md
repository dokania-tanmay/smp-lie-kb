---
tags: [reference, amgf, affine-martingale, probabilistic-tube, doob, set-erosion, safety-verification, contraction]
---
# Safety Verification of Nonlinear Stochastic Systems via Probabilistic Tube (Zishun Liu, Saber Jafarpour, Yongxin Chen — arXiv:2503.03328, 2025)

This is the paper that defines the two objects the sup-over-time branch of this project is built on: the **probabilistic tube** (Def. III.1) and the **affine martingale** (Def. IV.1), and it is where the AMGF energy function $\Phi_{n,\lambda}$ is shown to be an affine martingale for a general nonlinear SDE. The chain is: generator inequality on $\Phi_{n,\lambda}(X_t-x_t)$ $\Rightarrow$ affine-martingale coefficients $a_t,b_t$ $\Rightarrow$ Doob applied to a rescaled supermartingale $\Rightarrow$ $\mathbb P[\sup_{t\le T}\|X_t-x_t\|\le r_{\delta,t}]\ge1-\delta$ with $r_{\delta,t}=O(\sqrt{\log(1/\delta)})$. Everything is done in $\mathbb R^n$ with a global chart, an inner product, and averaging over $S^{n-1}$; those are exactly the pieces a manifold version has to replace. Contrast with [[@daniObserverDesignStochastic2015]], which gives only bound type (a) (mean-squared + Markov, hence fixed-$t$) and pays chart-dependent metric-derivative constants.

## Notation

| Symbol | Meaning |
|---|---|
| $X_t$, $x_t$ | stochastic trajectory of (1)/(2); **associated** deterministic trajectory of (3)/(4) — same $X_0=x_0$ and same $d_t$ at all times |
| $S_t = X_t-x_t$ | deviation process (a *difference of states*: $\mathbb R^n$-specific) |
| $d_t\in D\subseteq\mathbb R^p$ | bounded deterministic disturbance, statistics unknown |
| $g_t(X_t)\in\mathbb R^{n\times m}$, $W_t$ | diffusion coefficient, $m$-dim Wiener process |
| $\mu(A)$ | matrix measure, $\mu(A)=\lim_{\epsilon\to0^+}(\|I_n+\epsilon A\|-1)/\epsilon$ (Def. II.1) |
| $c$ | one-sided bound $\mu(D_xf)\le c$; $c<0$ = strictly contractive |
| $\sigma$ | diffusion bound, $g_tg_t^\top\preceq\sigma^2I_n$ (CT); also used as the sub-Gaussian proxy in the DT theorems |
| $L$ | Lipschitz constant of $f$ (DT); $L<1$ = contractive |
| $\vartheta_t^2$ | sub-Gaussian variance proxy of $w_t$ (DT) |
| $\Phi_{n,\lambda}(x)=\mathbb E_{\ell\sim S^{n-1}}[e^{\lambda\langle\ell,x\rangle}]$ | energy function of the AMGF |
| $r_{\delta,t}$ | radius of the probabilistic tube |
| $\varepsilon\in(0,1)$ | free tuning parameter; $\varepsilon_1=\dfrac{\log\frac{1}{1-\varepsilon^2}}{\varepsilon^2}$, $\varepsilon_2=\dfrac{2}{\varepsilon^2}$ (Eq. 9) |
| $A\ominus B$ | Minkowski difference $(A^c\oplus(-B))^c$; $\mathcal B_n(r,x_0)$ ball of radius $r$ |

Systems: CT $\;dX_t=f(X_t,d_t,t)\,dt+g_t(X_t)\,dW_t$ (1); DT $\;X_{t+1}=f(X_t,d_t,t)+w_t$ (2); deterministic counterparts $\dot x_t=f(x_t,d_t,t)$ (3), $x_{t+1}=f(x_t,d_t,t)$ (4).

## Standing assumptions

Standard Lipschitz + linear-growth conditions on (1) are assumed throughout for existence (Øksendal Thm 5.2.1), on top of:

:::info[Assumption 1 — CT]
There exist $c\in\mathbb R$ and $\sigma>0$ such that
1. $\mu(D_xf(x,d,t))\le c$ for all $t\ge0$, $d\in D$, $x\in\mathbb R^n$;
2. $g_t(x)g_t(x)^\top\preceq\sigma^2I_n$ for all $t\ge0$, $x\in\mathbb R^n$.

Note both are **global sup bounds over all of $\mathbb R^n$**, not local.
:::

:::info[Assumption 2 — DT Lipschitz]
There exists $L\ge0$ with $\|f(x,d,t)-f(y,d,t)\|\le L\|x-y\|$ for all $x,y\in\mathbb R^n$, $d\in D$.
:::

:::info[Assumption 3 — DT noise]
$w_t\sim\mathrm{subG}(\vartheta_t^2)$ and there exists $\vartheta<+\infty$ with $\vartheta_t\le\vartheta^2$ for every $t\ge0$. Here $X\sim\mathrm{subG}(\vartheta^2)$ (Def. II.2) means $\mathbb E X=0$ and $\mathbb E_X e^{\lambda\langle\ell,X\rangle}\le e^{\lambda^2\vartheta^2/2}$ for every $\ell\in S^{n-1}$ and all $\lambda\in\mathbb R$.
:::

:::warning[Open question]
The paper writes Assumption 3 as "$\vartheta_t\le\vartheta^2$" (mismatched squares — almost certainly meant $\vartheta_t^2\le\vartheta^2$), and then Propositions 2–3 and Theorems 4–5 all state the DT bounds with $\sigma$, never $\vartheta$. Read $\sigma$ in the DT results as the uniform sub-Gaussian variance proxy. This is a notation slip in the source, not an extraction failure.
:::

## Key definitions

:::info[Definition III.1 — Probabilistic Tube]
Given horizon $[0,T]$, level $\delta\in(0,1)$ and a curve $r_{\delta,t}:[0,T]\to\mathbb R_{\ge0}$, the set $\mathcal T=\{(t,y)\mid 0\le t\le T,\ \|y\|\le r_{\delta,t}\}$ is a **probabilistic tube (PT)** of the stochastic system if for *any* associated pair $(X_t,x_t)$,
$$\mathbb P\big((t,X_t-x_t)\in\mathcal T,\ \forall t\le T\big)=\mathbb P\big(\|X_t-x_t\|\le r_{\delta,t},\ \forall t\le T\big)\ge1-\delta.$$
This is trajectory-level ("$\forall t\le T$"), not state-level at a fixed $t$.
:::

:::info[Definition IV.1 — CT Affine Martingale]
For a CT process $\{v_t\}$, a nonnegative $M(v,t):\mathbb R^n\times[0,T]\to\mathbb R_{\ge0}$ is an **affine martingale (AM)** if there exist $a_t,b_t\in\mathbb R$ with
$$\frac{\mathbb E\big(M(v_{t+dt},t+dt)\mid v_t\big)-M(v_t,t)}{dt}\le a_tM(v_t,t)+b_t\qquad\text{for all }t.$$
Degenerations: $a_t\equiv0$ gives the classical **$c$-martingale**; $a_t,b_t\equiv0$ gives a **supermartingale**.
:::

:::info[Definition VI.1 — DT Affine Martingale]
$\mathbb E(M(v_{t+1},t+1)\mid v_t)\le a_tM(v_t,t)+b_t$. Degenerations shift by one: $a_t\equiv1$ gives the DT $c$-martingale, and additionally $b_t\equiv0$ gives a supermartingale.
:::

:::info[Definition IV.2 — AMGF and its energy function]
$\mathbb E_X(\Phi_{n,\lambda}(X)):=\mathbb E_X\,\mathbb E_{\ell\sim S^{n-1}}\big[e^{\lambda\langle\ell,X\rangle}\big]$ is the **averaged moment generating function**; $\Phi_{n,\lambda}(x)=\mathbb E_{\ell\sim S^{n-1}}[e^{\lambda\langle\ell,x\rangle}]$ is its **energy function**. Due to Altschuler–Talwar (Langevin sampling); used for reachability in [[@jafarpourProbabilisticReachabilityAnalysis2024]] and [[@liuProbabilisticReachabilityDiscreteTime2024]].
:::

## Main results

:::tip[Lemma IV.1 — AM $\Rightarrow$ sublevel-set probability (Doob)]
Let $M(v,t)$ be an AM of $\{v_t\}$ on $[0,T]$ with coefficients $a_t,b_t$. Put
$$\psi_t=e^{\int_t^Ta_\tau\,d\tau},\qquad \widetilde M(v_t,t)=M(v_t,t)\,\psi_t+\int_t^Tb_\tau\psi_\tau\,d\tau.$$
Then for any $M>0$ and $\mathcal V_t=\{v:\widetilde M(v_t,t)\le M\}$,
$$\mathbb P(v_t\in\mathcal V_t,\ \forall t\le T)\ \ge\ 1-\frac{M(v_0,0)\psi_0+\int_0^Tb_\tau\psi_\tau\,d\tau}{M}.$$
Proof technique: the discounting by $\psi_t$ plus the $b$-integral turns the AM into an honest supermartingale ($d\mathbb E\widetilde M/dt\le0$), then Doob's maximal inequality. So $a_t$ enters as an exponential *discount factor* $\psi$ and $b_t$ as an additive integrated drift.
:::

:::tip[Lemma VI.1 — DT counterpart]
With $\phi_t=\prod_{\tau=t}^{T-1}a_\tau$ ($\phi_T=1$) and $\widetilde M(v_t,t)=M(v_t,t)\phi_t+\sum_{\tau=t}^{T-1}b_\tau\phi_{\tau+1}$ for $t<T$, $\widetilde M(v_T,T)=M(v_T,T)$:
$$\mathbb P(v_t\in\mathcal V_t,\ \forall t\le T)\ \ge\ 1-\frac{\mathbb E(M(v_0,0))\,\phi_0+\sum_{\tau=0}^{T-1}b_\tau\phi_{\tau+1}}{M}.$$
:::

:::tip[Lemma IV.2 — properties of $\Phi_{n,\lambda}$]
1. **Rotation invariance.** For any $x\in\mathbb R^n$ and any $\ell\in S^{n-1}$: $\Phi_{n,\lambda}(x)=\Phi_{n,\lambda}(\|x\|\cdot\ell)$ — i.e. $\Phi$ is a function of $\|x\|$ alone.
2. **Monotonicity.** $\|x\|\le\|y\|\ \Rightarrow\ 1\le\Phi_{n,\lambda}(x)\le\Phi_{n,\lambda}(y)$.
3. **Exponential growth.** For every $n$, every $x\in\mathbb R^n$, every $\varepsilon\in(0,1)$: $\Phi_{n,\lambda}(x)\ge(1-\varepsilon^2)^{n/2}e^{\varepsilon\|\lambda x\|}$.
4. **Sub-Gaussian decoupling.** For $x\in\mathbb R^n$ and $w\sim\mathrm{subG}(\vartheta^2)$: $\mathbb E_w(\Phi_{n,\lambda}(x+w))\le e^{\lambda^2\vartheta^2/2}\,\Phi_{n,\lambda}(x)$.

Proofs of 1–2 in [[@jafarpourProbabilisticReachabilityAnalysis2024]] §V.B, of 3 in [[@liuNewProofSubGaussian2025]], of 4 in [[@liuProbabilisticReachabilityDiscreteTime2024]] §4.2.
:::

:::tip[Theorem 1 — set-erosion strategy]
If the PT radius $r_{\delta,t}$ of Def. III.1 satisfies $x_t\in\mathcal C\ominus\mathcal B_n(r_{\delta,t},0)$ for all $t\le T$ (for every deterministic trajectory from $\mathcal X_0$, every $d_t\in D$), then the stochastic system is safe on $\mathcal C$ with $1-\delta$ guarantee on $[0,T]$: $\mathbb P(X_t\in\mathcal C,\forall t\le T)\ge1-\delta$. Reduces stochastic verification to deterministic verification on an eroded, time-varying set. Applications: Prop. 4 (reachable-set version, $\mathcal R_t\subset\mathcal C\ominus\mathcal B_n(r_{\delta,t},0)$) and Eq. (58) (MPC safety constraint on the deterministic trajectory only).
:::

:::tip[Theorem 2 — CT probabilistic tube, general $c$]
Under Assumption 1, for $\delta\in(0,1)$, $\varepsilon\in(0,1)$,
$$r_{\delta,t}=e^{ct}\sigma\sqrt{\frac{1-e^{-2cT}}{2c}\big(\varepsilon_1n+\varepsilon_2\log(1/\delta)\big)}\quad\Longrightarrow\quad\mathbb P(\|X_t-x_t\|\le r_{\delta,t},\forall t\le T)\ge1-\delta.$$
Proof skeleton (worth reproducing intrinsically): for $c=0$, Itô/Fokker–Planck gives
$$\tfrac{d}{dt}\mathbb E\Phi=\langle\nabla\Phi_{n,\lambda}(S_t),\beta_t\rangle+\tfrac12\langle\nabla^2\Phi_{n,\lambda}(S_t),g_tg_t^\top\rangle,\quad \beta_t=f(X_t,d_t,t)-f(x_t,d_t,t);$$
the drift term is $\le0$ by $\mathbb E_\ell[e^{\lambda\langle\ell,S_t\rangle}\lambda\ell^\top\beta_t]\le0$ ([[@jafarpourProbabilisticReachabilityAnalysis2024]] Lemma V.3, i.e. one-sided Lipschitz with $c=0$), and the diffusion term is $\le\frac{\lambda^2\sigma^2}{2}\Phi$ using Hölder and $\mathrm{trace}(\ell\ell^\top)=1$. Hence $\Phi_{n,\lambda}(S_t)$ is an **AM with $a_t\equiv\lambda^2\sigma^2/2$, $b_t\equiv0$**. Lemma IV.1 + Lemma IV.2-(1,2,3) give
$$\mathbb P(\|S_t\|\le r,\forall t\le T)\ge1-(1-\varepsilon^2)^{-n/2}e^{-\varepsilon^2r^2/(2\sigma^2T)},$$
optimized at $\lambda^*=\varepsilon r/(\sigma^2T)$; choosing $r=\sqrt{\frac{2\sigma^2T}{\varepsilon^2}\big(\frac n2\log\frac{1}{1-\varepsilon^2}+\log(1/\delta)\big)}$ gives the $c=0$ case. General $c$ follows by the rescaling $\tilde X_t=e^{-ct}X_t$, under which $\tilde f=-c\tilde x+e^{-ct}f(e^{ct}\tilde x,d,t)$ satisfies Assumption 1 with $\tilde c=0$ and $\tilde\sigma_t^2=e^{-2ct}\sigma^2$.
:::

Tightness discussion after Thm 2: when $c=0$, $r_{\delta,t}=\sigma\sqrt{T(\varepsilon_1n+\varepsilon_2\log(1/\delta))}$ is constant in $t$ and *equals* the fixed-time bound of Prop. 1 — a trajectory-level bound for the price of a state-level one; with $f\equiv0$, $g\equiv1$, $n=1$ it recovers the reflection principle. Tight for $c\ge0$; conservative for $c<0$ with $t\ll T$, where the coefficient $e^{ct}\sqrt{(1-e^{-2cT})/2c}$ blows up like $O(e^{-cT})$.

:::tip[Theorem 3 — modified CT tube for contractive systems ($c<0$)]
For $\delta\in(0,1)$, $\Delta t\in(0,T)$, $\varepsilon\in(0,1)$,
$$r_{\delta,t}=\frac{\sigma\big(\sqrt{1-e^{2ct}}+\sqrt{e^{-2c\Delta t}-1}\big)}{\sqrt{-2c}}\sqrt{\varepsilon_1n+\varepsilon_2\log\frac{2T}{\delta\,\Delta t}}$$
gives $\mathbb P(\|X_t-x_t\|\le r_{\delta,t},\forall t\le T)\ge1-\delta$. Technique: split $[0,T]$ into $N=T/\Delta t$ windows; endpoint bounds from Prop. 1 with budget $\delta/2N$; within each window restart a deterministic trajectory $y^{(k)}$ from $X_{k\Delta t}$ and apply Thm 2 over $\Delta t$ with budget $\delta/2N$; contraction gives $\|x_t-y^{(k)}_t\|\le\|X_{k\Delta t}-x_{k\Delta t}\|$; union bound. Trades $O(e^{-cT})$ for $O(e^{-c\Delta t}+\sqrt{\log(T/\Delta t)})$.
:::

:::tip[Theorem 4 / Theorem 5 — DT counterparts]
Thm 4 (Assumptions 2–3, general $L$): $r_{\delta,t}=L^t\sigma\sqrt{\dfrac{L^{-2T}-1}{L^{-2}-1}\big(\varepsilon_1n+\varepsilon_2\log(1/\delta)\big)}$. Proof: for $L=1$, Lemma IV.2-4 gives $\mathbb E(\Phi_{n,\lambda}(S_{t+1})\mid S_t)\le e^{\lambda^2\sigma^2/2}\Phi_{n,\lambda}(S_t)$ — a DT AM with $a_t=e^{\lambda^2\sigma^2/2}$, $b_t=0$; general $L$ by the rescaling $\tilde X_t=L^{-t}X_t$.

Thm 5 (Assumptions 2–3 with $L<1$, $\Delta t\in\{1,\dots,T\}$):
$$r_{\delta,t}=\sigma\left(\sqrt{\frac{L^{2t}-1}{L^2-1}}+\sqrt{\frac{L^{-2(\Delta t-1)}-1}{L^{-2}-1}}\right)\sqrt{\varepsilon_1n+\varepsilon_2\log\frac{2T}{\delta\,\Delta t}}.$$
At $\Delta t=1$ this collapses to the pure union-bound tube of [[@liuSafetyVerificationStochastic2024a]] (Prop. 3 here), $r_{\delta,t}=\sqrt{\frac{\sigma^2(L^{2t}-1)}{L^2-1}(\varepsilon_1n+\varepsilon_2\log(T/\delta))}$; empirically $\Delta t=1$ is near-optimal but not always optimal.
:::

For reference, the fixed-time (state-level) results this builds on: Prop. 1 = [[@jafarpourProbabilisticReachabilityAnalysis2024]] Thm 1, $\|X_t-x_t\|\le\sqrt{\frac{\sigma^2(e^{2ct}-1)}{2c}(\varepsilon_1n+\varepsilon_2\log(1/\delta))}$ w.p. $\ge1-\delta$; Prop. 2 = [[@liuProbabilisticReachabilityDiscreteTime2024]] Thm 1, same with $\frac{\sigma^2(L^{2t}-1)}{L^2-1}$.

## What this gives the project

- **The exact target statement for bound type (b).** Def. III.1 is the object to port: a time-varying radius $r_{\delta,t}$ with a single $1-\delta$ budget spent over the whole horizon. On a manifold, $\|X_t-x_t\|$ becomes $d(X_t,\bar x_t)$ and the tube becomes a sublevel set of the distance to the reference curve.
- **The AM $\to$ Doob template (Lemma IV.1) is chart-free as stated.** It only needs a nonnegative $M(v,t)$ on the state space and a generator inequality $\mathcal LM\le a_tM+b_t$. Nothing in it uses $\mathbb R^n$. This is the piece that transfers verbatim once $M$ is defined intrinsically.
- **Lemma IV.2-1 is the licence for the intrinsic construction.** $\Phi_{n,\lambda}$ depends on $x$ only through $\|x\|$, so the manifold replacement $\Phi(x)=\mathbb E_{\ell\sim S(T_{\bar x}M)}[e^{\lambda\langle\ell,\log_{\bar x}x\rangle}]$ (or a radial function of $d(x,\bar x)$) is forced rather than invented. Properties 2 and 3 are statements about a radial profile and should survive; property 4 is where sub-Gaussian noise on a manifold needs a definition.
- **Where the two constants come from.** In Thm 2 the *only* two inputs are $c$ (one-sided Lipschitz / matrix measure) and $\sigma$ (diffusion bound). No metric-derivative sups appear — because the metric is flat. The manifold version's extra cost should be a curvature/Hessian-comparison term entering the diffusion step, not $\sup|\partial g_{ij}|$ as in [[@daniObserverDesignStochastic2015]].
- **The two-step generator computation is the thing to redo.** Drift term $\langle\nabla\Phi,\beta_t\rangle\le0$ and diffusion term $\frac12\langle\nabla^2\Phi,gg^\top\rangle\le\frac{\lambda^2\sigma^2}{2}\Phi$. Intrinsically these become a first-order comparison along $\log_{\bar x}$ and a Hessian-comparison bound on $\Delta\Phi$ — the second is exactly where curvature must enter.
- **Set erosion + interval splitting are recipes, not obstacles.** Thm 3's split-and-union trick needs only contraction of the deterministic flow and a restart of the reference trajectory from $X_{k\Delta t}$ — both available on a manifold, though "restart the deterministic trajectory at the stochastic state" uses that $f$ is defined at every state, fine, while $\|x_t-y_t^{(k)}\|\le\dots$ requires an intrinsic incremental-stability estimate.

## What is $\mathbb R^n$-specific (needs intrinsic replacement)

- $S_t=X_t-x_t$: subtraction of states. Must become $\log_{\bar x_t}(X_t)\in T_{\bar x_t}M$ or just $d(X_t,\bar x_t)$; the SDE $dS_t=\beta_t\,dt+g_t\,dW_t$ has no direct analogue (the tangent space moves).
- The rescalings $\tilde X_t=e^{-ct}X_t$ (CT) and $L^{-t}X_t$ (DT), used to reduce general $c$/$L$ to $c=0$/$L=1$. These are scalar multiplication of states — no analogue on a manifold. The general-$c$ case will need a different argument (e.g. a time-varying $\lambda_t$ inside the AM).
- $\langle\ell,x\rangle$ with $\ell\in S^{n-1}$ globally fixed and independent of the base point: needs an average over the unit sphere of $T_{\bar x}M$, which moves with $\bar x$.
- $\mathrm{trace}(\ell\ell^\top)=1$ and $\|g g^\top\|\le\sigma^2$ in the Hessian step — a flat-space Hessian identity.
- $\mu(D_xf)\le c$ globally: a matrix measure of a Jacobian in a fixed chart. Intrinsically this is a bound on the symmetrized covariant derivative of the vector field, and Assumption 1 asks for it uniformly over the whole space.
- Minkowski difference $\mathcal C\ominus\mathcal B_n(r,0)$ in Theorem 1: erosion by a ball. Intrinsically this is $\{x\in\mathcal C: d(x,\partial\mathcal C)\ge r\}$ — fine, but the Minkowski algebra it relies on is not.

## Caveats / limitations

- Assumption 1 is **global and uniform**: $\mu(D_xf)\le c$ over all of $\mathbb R^n$ and $g g^\top\preceq\sigma^2I_n$ everywhere. No localization to a tube or a compact region.
- The diffusion bound is **isotropic and state-independent** ($\sigma^2I_n$). Anisotropic or degenerate noise is only handled through its worst direction, so $\sigma$ can be very loose for e.g. actuator noise on a mechanical system.
- Thm 2 is **conservative for contractive systems** ($c<0$) at $t\ll T$ — the authors say so explicitly and Thm 3 exists to fix it, at the price of reintroducing a union bound and a hyperparameter $\Delta t$ (whose optimum is found numerically, Fig. 5–6).
- $\varepsilon$ is a free tuning parameter with no closed-form optimum given; the experiments use $\varepsilon=1/16$ throughout, except §VII-A which sets $\varepsilon_1=2\log2$, $\varepsilon_2=2$ directly — those two values are not jointly consistent with Eq. (9) for any single $\varepsilon$ (they would need $\varepsilon^2=1/2$ and $\varepsilon^2=1$ respectively), so treat that one numerical choice with suspicion.
- Dimension dependence is $\varepsilon_1n$ inside the square root, so $r_{\delta,t}=O(\sqrt n)$ — attractive, but the $n$ is the ambient dimension of the global chart.
- The tube is centered on the *associated* deterministic trajectory sharing the same $d_t$, so the guarantee is per-disturbance-realization; safety statements quantify over $d_t\in D$ separately.
- Authors flag performance analysis of the safe-synthesis framework (dependence on the cost and $\mathcal C$) as future work; no converse/lower bound is proved for the contractive case.
