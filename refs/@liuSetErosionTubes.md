---
tags: [set-erosion, amgf, probabilistic-tube, concentration-inequality, contraction, safety-verification, reference]
---
# Set Erosion and Probabilistic Tubes (Liu et al.)

Two papers from Yongxin Chen's group at Georgia Tech that together supply the *entire* Euclidean template this project wants to make intrinsic. [[@liuSafetyVerificationStochastic2024a]] (*Safety Verification of Stochastic Systems: A Set-Erosion Approach*, arXiv:2410.02107, IEEE L-CSS vol. 8 pp. 2859–2864, 2024) supplies the **reduction**: a stochastic system is safe on $\mathcal C$ with probability $1-\delta$ if the associated *deterministic* system stays in the eroded set $\mathcal C\ominus B^n(r_{\delta,t},0)$. [[@liuConcentrationStochasticSystem2026]] (*Concentration of Stochastic System Trajectories with Time-varying Contraction Conditions*, arXiv:2604.01403 [math.OC], Apr 2026; Liu, Ma, Yu, Chen) supplies the **radius**: continuous-time, contraction-metric-weighted, sup-over-time bounds built from the AMGF and an affine martingale. The second paper is where $\sup_{t\le T}$ and "tight" both get their precise meaning; the first is where a tube becomes a safety certificate.

## The two papers

| | [[@liuSafetyVerificationStochastic2024a]] | [[@liuConcentrationStochasticSystem2026]] |
|---|---|---|
| Time | **Discrete**: $X_{t+1}=f(X_t,d_t,t)+w_t$ | **Continuous** Itô: $dX_t=f(X_t,u_t)\,dt+g_t(X_t)\,dW_t$ |
| Regularity hypothesis | Global Lipschitz constant $L_t$ | Time-varying **contraction** $c_t$ with metric $M_t$ (may be negative) |
| Noise | Additive sub-Gaussian $w_t\sim\mathrm{subG}(\sigma_t^2)$ | State-dependent diffusion, $g_tg_t^{\mathsf T}\preceq\sigma^2 I$ |
| Distance | Euclidean $\|X_t-x_t\|$ | Weighted $\|X_t-x_t\|_{M_t}$ (ellipsoidal tube) |
| $\sup_t$ mechanism | **Union bound** over $t=1,\dots,T$ ⇒ $\log(T/\delta)$ | **Affine martingale + Doob** ⇒ $\log(1/\delta)$ only |
| Contributes | Set-erosion theorem; barrier-function instantiations (TV-RBF, TV-EBF) | Single-time bound (Thm 1), trajectory bound (Thm 2), sharpened trajectory bound for strongly contracting systems (Thm 3) |
| AMGF | Not used explicitly — inherits its bound from [[@liuProbabilisticReachabilityDiscreteTime2024]] | AMGF is the central object |

Read the 2024 paper as the *narrower, earlier* result (discrete time, Lipschitz only, union bound over the horizon) and the 2026 paper as the *later, broader* one (continuous time, time-varying contraction metric, martingale in place of the union bound, and an explicit split-interval refinement). The 2026 paper cites the 2024 one as "[21]" and uses set erosion off-the-shelf in its case study.

## Notation

| Symbol | Meaning |
|---|---|
| $X_t$ / $x_t$ | stochastic trajectory / *associated* deterministic trajectory — same $x_0=X_0$, same input |
| $\mathcal C$ | safe set; $\mathcal C\ominus B$ Minkowski difference, $\mathcal A\oplus\mathcal B$ Minkowski sum |
| $B^n(r,y)$ | closed Euclidean ball $\{x:\|x-y\|\le r\}$ |
| $r_{\delta,t}$ | tube radius / erosion depth |
| $L_t,\ \sigma_t$ | (2024) Lipschitz constant, sub-Gaussian variance proxy at step $t$ |
| $\psi_t,\ \Psi_t$ | accumulated growth / accumulated noise — **defined differently in each paper**, see below |
| $c_t,\ M_t$ | (2026) contraction rate, contraction metric (SPD); $m_t=\lambda_{\max}(M_t)$, $\bar\sigma_t=\sqrt{m_t}\,\sigma$ |
| $\varepsilon\in(0,1)$ | free tuning parameter; $\varepsilon_1,\varepsilon_2$ derived from it |
| $\lambda$ | AMGF parameter, optimized away |
| $n$ | state dimension |

## Key definitions

:::info[Definition — sub-Gaussian, [[@liuSafetyVerificationStochastic2024a]] Def. 2.1]
$X\in\mathbb R^n$ is $\mathrm{subG}(\sigma^2)$ if $\mathbb E X=0$ and for every $\ell\in S^{n-1}$, $\mathbb E_X e^{\lambda\langle\ell,X\rangle}\le e^{\lambda^2\sigma^2/2}$ for all $\lambda\in\mathbb R$. Covers Gaussian, uniform, and any zero-mean bounded-support law.
:::

Note the definition is already stated *per direction $\ell\in S^{n-1}$* — this is exactly the object the AMGF averages over.

:::info[Definition — AMGF, [[@liuConcentrationStochasticSystem2026]] Def. 2]
For $X\in\mathbb R^n$, the **averaged moment generating function** is $\mathbb E_X\Phi(X)=\mathbb E_X\,\mathbb E_{\ell\in S^{n-1}}e^{\lambda\langle\ell,X\rangle}$, where $\Phi(X)=\mathbb E_{\ell\in S^{n-1}}e^{\lambda\langle\ell,X\rangle}$ is the **energy function**. The weighted version is $\Phi_M(X)=\Phi(M^{1/2}X)$ for $M$ SPD.
:::

:::info[Definition — contracting system, [[@liuConcentrationStochasticSystem2026]] Def. 1]
The deterministic system $\dot x_t=f(x_t,u_t)$ is $c_t$-**contracting** if there exist $c_t\in\mathbb R$ and SPD $M_t$ with
$$\Big(\tfrac{\partial f}{\partial x_t}\Big)^{\!\mathsf T}M_t+M_t\tfrac{\partial f}{\partial x_t}+\dot M_t\ \preceq\ 2c_t M_t .$$
**Strongly contracting** means $c_t<0$ for all $t$. Assumption 2 of the paper is that such $c_t,M_t$ exist on $[0,T]$.
:::

:::info[Definition — affine martingale, [[@liuConcentrationStochasticSystem2026]] Def. 3 (from [[@liuSafetyVerificationNonlinear2025]])]
A nonnegative differentiable $B(Y,t):\mathbb R^n\times[0,T]\to\mathbb R_{\ge0}$ is an **affine martingale (AM)** of the process $Y_t$ if there exist $a_t\in\mathbb R$, $b_t\in\mathbb R_{\ge0}$ with
$$\lim_{dt\to0}\frac{\mathbb E\big(B(Y_{t+dt},t+dt)\mid Y_t\big)-B(Y_t,t)}{dt}\ \le\ a_tB(Y_t,t)+b_t .$$
Generalizes Kushner's semi-martingale condition to time-varying $a_t,b_t$.
:::

:::info[Definition — TV-RBF / TV-EBF, [[@liuSafetyVerificationStochastic2024a]] Def. 5.1, 5.2]
Time-varying reciprocal / exponential barrier functions for the *deterministic* system on the time-varying set $\tilde{\mathcal C}_t=\{x:h(x,t)\ge0\}$. TV-RBF: $\alpha_1(h)^{-1}\le B\le\alpha_2(h)^{-1}$ and $B(f(x,d,t),t+1)-B(x,t)\le\alpha_3(h(x,t))$ for extended class-$\mathcal K$ $\alpha_i$. TV-EBF: $\exists\gamma\in(0,1]$ with $h(f(x,d,t),t+1)\ge(1-\gamma)h(x,t)$ on $\tilde{\mathcal C}_t$, for all $d\in D$.
:::

## Main results

:::tip[Theorem — set-erosion strategy, [[@liuSafetyVerificationStochastic2024a]] Thm 1]
Consider $X_{t+1}=f(X_t,d_t,t)+w_t$ and its associated deterministic system $x_{t+1}=f(x_t,d_t,t)$. Given an initial set $\mathcal X_0$, a safe set $\mathcal C\subseteq\mathbb R^n$ and terminal time $T$, suppose there exists $r_{\delta,t}$ such that for every trajectory pair starting in $\mathcal X_0$:

1. $\mathbb P\big(\|X_t-x_t\|\le r_{\delta,t},\ \forall t\le T\big)\ge1-\delta$;
2. $x_t\in\mathcal C\ominus B^n(r_{\delta,t},0)$ for all $t\le T$.

Then the stochastic system is safe with $1-\delta$ guarantee during $t\le T$, i.e. $\mathbb P(X_t\in\mathcal C,\ \forall t\le T)\ge1-\delta$.

Two-line proof: condition 1 says $X_t\in\{x_t\}\oplus B^n(r_{\delta,t},0)$ for all $t\le T$ w.p. $\ge1-\delta$; condition 2 puts that Minkowski sum inside $\mathcal C$.
:::

Note what hypothesis 1 *is*: precisely the sup-over-time tube statement this project targets. Set erosion is the cheap half; everything hard is in producing $r_{\delta,t}$. Note also that the theorem itself needs **no** assumption on $f$ or $w_t$ — Assumptions 1–2 enter only through the construction of $r_{\delta,t}$.

:::tip[Proposition — stochastic deviation at a single time, [[@liuSafetyVerificationStochastic2024a]] Prop. 1 (imported from [[@liuProbabilisticReachabilityDiscreteTime2024]])]
Under Assumption 1 ($\|f(x,d,t)-f(y,d,t)\|\le L_t\|x-y\|$ for all $x,y,d$) and Assumption 2 ($w_t\sim\mathrm{subG}(\sigma_t^2)$, $\sigma_t>0$ finite), for each fixed $t\ge0$ and any $\delta,\varepsilon\in(0,1)$,
$$\|X_t-x_t\|\ \le\ \sqrt{\Psi_t\big(\varepsilon_1 n+\varepsilon_2\log(1/\delta)\big)}$$
with probability $\ge1-\delta$, where
$$\Psi_t=\psi_{t-1}\sum_{k=0}^{t-1}\sigma_k^2\psi_k^{-1},\qquad \psi_t=\prod_{k=0}^{t}L_k^2,\qquad \varepsilon_1=\frac{2\log(1+2/\varepsilon)}{(1-\varepsilon)^2},\quad \varepsilon_2=\frac{2}{(1-\varepsilon)^2}.$$
Remark 4.1: these $\varepsilon_1,\varepsilon_2$ are not optimal; for $n=1$, Hoeffding gives the better $\varepsilon_1=2\log2$, $\varepsilon_2=2$.
:::

:::tip[Theorem — stochastic trajectory gap, [[@liuSafetyVerificationStochastic2024a]] Thm 2]
Under the same Assumptions 1–2, for any $\delta\in(0,1]$ and $\varepsilon\in(0,1)$, setting
$$r_{\delta,t}=\sqrt{\Psi_t\big(\varepsilon_1 n+\varepsilon_2\log(T/\delta)\big)}$$
gives $\mathbb P(\|X_t-x_t\|\le r_{\delta,t},\ \forall t\le T)\ge1-\delta$. Technique: Prop. 1 at level $\delta/T$ per step, then a **union bound** over $t=1,\dots,T$.
:::

For $L_t\equiv L$, $\sigma_t\equiv\sigma$ this collapses to $\Psi_t=\sigma^2\frac{L^{2t}-1}{L^2-1}$, i.e.
$$r_{\delta,t}=\sigma\sqrt{\tfrac{L^{2t}-1}{L^2-1}\big(\varepsilon_1n+\varepsilon_2\log(T/\delta)\big)}.$$

:::tip[Proposition — worst-case comparison, [[@liuSafetyVerificationStochastic2024a]] §IV-B, eq. (13)–(14)]
Treating $w_t$ as a bounded disturbance ($\|w_t\|\le b_t$ w.p. $1-\delta$ with $b_t\ge\sqrt{\sigma_t^2(\varepsilon_1n+\varepsilon_2\log(T/\delta))}$) and iterating the triangle inequality gives
$$\|X_t-x_t\|\ \le\ \sqrt{\psi_{t-1}}\sum_{k=0}^{t-1}\sigma_k\sqrt{\psi_k^{-1}\big(\varepsilon_1n+\varepsilon_2\log(T/\delta)\big)} .$$
Since $\sqrt{\Psi_t}\le\sqrt{\psi_{t-1}}\sum_k\sigma_k\sqrt{\psi_k^{-1}}$, the worst-case bound is **always** worse than Thm 2 — it is the $\ell^1$ rather than $\ell^2$ accumulation of noise. Constant-coefficient version: $\frac{L^t-1}{L-1}\sqrt{\sigma^2(\varepsilon_1n+\varepsilon_2\log(t/\delta))}$, dramatically worse when $L\approx1$ or $L\ge1$.
:::

:::tip[Lemma — AMGF properties, [[@liuConcentrationStochasticSystem2026]] Lemma 1 (assembled from [[@jafarpourProbabilisticReachabilityAnalysis2024]] Lem. 5.2, 5.4 and [[@liuSafetyVerificationNonlinear2025]] Lem. 4.2)]
For $\Phi_M(X)=\Phi(M^{1/2}X)$ with $M$ SPD:
1. $\Phi_M(X)$ depends on $X$ **only through $\|X\|_M$** (radial / isotropic);
2. monotone: $\Phi_{M_1}(X_1)\le\Phi_{M_2}(X_2)$ whenever $\|X_1\|_{M_1}\le\|X_2\|_{M_2}$;
3. for any $\varepsilon\in(0,1)$: $\Phi_M(X)\ \ge\ (1-\varepsilon^2)^{n/2}e^{\varepsilon\|\lambda X\|_M}$;
4. if $X$ is random with $\mathbb E_X\Phi_M\le e^{\lambda^2\vartheta^2/2}$ for all $\lambda\in\mathbb R$, then for any $\delta,\varepsilon\in(0,1)$
   $$\mathbb P\Big(\|X\|_M\le\vartheta\sqrt{\varepsilon_1n+\varepsilon_2\log(1/\delta)}\Big)\ge1-\delta,\qquad \varepsilon_1=\frac{\log\frac{1}{1-\varepsilon^2}}{\varepsilon^2},\ \ \varepsilon_2=\frac{2}{\varepsilon^2}.$$
:::

Property 1 is the hook for this project: the AMGF is already a radial function of $\|X\|_M$, so the manifold generalization is forced rather than invented. Property 3 is where the dimension $n$ enters, and it is *tighter* than the $\varepsilon$-net constant $\varepsilon_1$ of the 2024 discrete paper.

:::tip[Lemma — affine martingale ⇒ sup-over-time, [[@liuConcentrationStochasticSystem2026]] Lemma 2 (proved in [[@liuSafetyVerificationNonlinear2025]] Lem. 4.1)]
Let $B(Y,t)$ be an AM of $Y_t$ with coefficients $a_t$, $b_t\ge0$. Put $\xi_t=e^{\int_t^Ta_\tau d\tau}$ and $\widetilde B(Y_t,t)=B(Y_t,t)\xi_t+\int_t^Tb_\tau\xi_\tau d\tau$. Then for any $\mathsf B>0$ and $\mathcal Y_t=\{Y:\widetilde B(Y,t)\le \mathsf B\}$,
$$\mathbb P(Y_t\in\mathcal Y_t,\ \forall t\le T)\ \ge\ 1-\frac{B(Y_0,0)\xi_0+\int_0^Tb_\tau\xi_\tau d\tau}{\mathsf B}.$$
This is the Doob/Ville step: $\widetilde B$ is a supermartingale and the sublevel set becomes the tube.
:::

:::tip[Theorem — single-time concentration, [[@liuConcentrationStochasticSystem2026]] Thm 1]
Under Assumption 1 ($g_t(X_t)g_t(X_t)^{\mathsf T}\preceq\sigma^2I$) and Assumption 2 ($c_t$-contracting with metric $M_t$ on $[0,T]$), define
$$m_t=\lambda_{\max}(M_t),\quad \bar\sigma_t=\sqrt{m_t}\,\sigma,\quad \psi_t=\int_0^tc_\tau\,d\tau,\quad \Psi_t=\int_0^t\bar\sigma_\tau^2e^{-2\psi_\tau}\,d\tau .$$
Then for any $t\in[0,T]$, $\delta,\varepsilon\in(0,1)$,
$$\|X_t-x_t\|_{M_t}\ \le\ \sqrt{e^{2\psi_t}\Psi_t\big(\varepsilon_1n+\varepsilon_2\log(1/\delta)\big)}$$
with probability $\ge1-\delta$, $\varepsilon_1,\varepsilon_2$ as in Lemma 1(4). Technique: path-length integral over geodesics of the (flat, at frozen $t$) metric $M_t$, Itô on the energy $\mathcal E(l_t^*)=\Phi_{M_t}(X_t-x_t)$, then the time-rescaling $\tilde X_t=e^{-\psi_t}X_t$ to reduce $c_t\ne0$ to $c_t=0$.
:::

:::tip[Theorem — trajectory-level concentration, [[@liuConcentrationStochasticSystem2026]] Thm 2]
Same hypotheses. For terminal time $T$, $\delta,\varepsilon\in(0,1)$, define
$$r_{\delta,t}=\sqrt{e^{2\psi_t}\,\Psi_T\big(\varepsilon_1n+\varepsilon_2\log(1/\delta)\big)}\qquad(\text{note }\Psi_T,\text{ not }\Psi_t).$$
Then $\mathbb P(\|X_t-x_t\|_{M_t}\le r_{\delta,t},\ \forall t\le T)\ge1-\delta$. Technique: $\Phi_{M_t}(X_t-x_t)$ is an affine martingale with $a_t=\lambda^2\bar\sigma_t^2/2$, $b_t\equiv0$; apply Lemma 2, lower-bound $\Phi(r\eta)$ by Lemma 1(3), then optimize over $\lambda$.
:::

The $\lambda$-optimization is explicit and worth recording. The Doob step gives
$$\mathbb P\big(\|X_t-x_t\|_{M_t}\le r,\ \forall t\le T\big)\ \ge\ 1-(1-\varepsilon^2)^{-n/2}\exp\Big(\tfrac{\lambda^2}{2}\!\int_0^T\!\bar\sigma_\tau^2d\tau-\varepsilon\lambda r\Big),$$
minimized at $\lambda^*=\varepsilon r\big/\!\int_0^T\bar\sigma_\tau^2d\tau$, and setting the right side to $\delta$ yields
$$r=\sqrt{\frac{2\int_0^T\bar\sigma_\tau^2\,d\tau}{\varepsilon^2}\Big(\tfrac n2\log\tfrac1{1-\varepsilon^2}+\log(1/\delta)\Big)}\ =\ \sqrt{\Psi_T\big(\varepsilon_1n+\varepsilon_2\log(1/\delta)\big)}\quad(c_t\equiv0).$$

:::tip[Theorem — sharpened tube for strongly contracting systems, [[@liuConcentrationStochasticSystem2026]] Thm 3]
Assume additionally $c_t<0$. Given $\Delta t>0$, let $k=\lceil t/\Delta t\rceil$ and $\Psi^{\Delta t}_t=\int_{k\Delta t}^{(k+1)\Delta t}\bar\sigma_\tau^2e^{-2\psi_\tau}\,d\tau$. Then
$$r_{\delta,t}=\Big(\sqrt{e^{2\psi_t}\Psi^{\Delta t}_t}+\sqrt{\Psi_t}\Big)\sqrt{\varepsilon_1n+\varepsilon_2\log\tfrac{2T}{\delta\Delta t}}$$
satisfies $\mathbb P(\|X_t-x_t\|_{M_t}\le r_{\delta,t},\ \forall t\le T)\ge1-\delta$. Technique: split $[0,T]$ into $N=T/\Delta t$ intervals; Thm 1 at the $N$ endpoints at level $\delta/2N$, Thm 2 inside each interval at level $\delta/2N$, union bound over the $2N$ events.
:::

## The tube radius

Everything the project cares about is in these formulas. In both papers the radius has the same shape,
$$r_{\delta,t}\ =\ \underbrace{\sqrt{(\text{accumulated noise, discounted by contraction})}}_{\text{system}}\ \times\ \underbrace{\sqrt{\varepsilon_1n+\varepsilon_2\log(\cdot/\delta)}}_{\text{concentration}},$$
with the two factors completely decoupled.

- **Dependence on $\delta$**: $O(\sqrt{\log(1/\delta)})$ in all four bounds. This is the headline. Traditional incremental-stability analysis (ISA) — bounding $\mathbb E\|X_t-x_t\|_{M_t}^2$ and applying Markov, i.e. the [[@daniObserverDesignStochastic2015]] / [[@phamContractionTheoryApproach2008]] route — gives only $O(\sqrt{1/\delta})$, which is catastrophic at $\delta=10^{-3}$ or below.
- **Dependence on noise**: through $\Psi_t$ only, linearly in $\sigma$ (i.e. $\sqrt{\Psi_t}\propto\sigma$). Discrete: $\Psi_t=\psi_{t-1}\sum_{k<t}\sigma_k^2\psi_k^{-1}$ — an $\ell^2$ accumulation. Continuous: $\Psi_t=\int_0^t\bar\sigma_\tau^2e^{-2\psi_\tau}d\tau$ with $\bar\sigma_\tau=\sqrt{\lambda_{\max}(M_\tau)}\,\sigma$.
- **Dependence on contraction**: through $e^{2\psi_t}\Psi_t$ with $\psi_t=\int_0^tc_\tau d\tau$. For $c_t\equiv c<0$ this saturates: $e^{2\psi_t}\Psi_t\to\bar\sigma^2/(2|c|)$, a bounded tube. For $c>0$ (or $L>1$) it grows like $e^{2ct}$. This is the exact analogue of the Grönwall factor, but it multiplies an $\ell^2$-accumulated noise term rather than an $\ell^1$ one.
- **Dependence on $n$**: always as $\sqrt{\varepsilon_1n+\cdots}$, i.e. $r_{\delta,t}=O(\sqrt n)$ — which is the correct scaling (the norm of an $n$-dimensional Gaussian concentrates at $\sigma\sqrt n$), not an artifact. The constant differs by paper: $\varepsilon_1=2\log(1+2/\varepsilon)/(1-\varepsilon)^2$ in the 2024 discrete paper (an $\varepsilon$-net covering-number constant, $(1+2/\varepsilon)^n$ balls) versus $\varepsilon_1=\log\frac1{1-\varepsilon^2}/\varepsilon^2$ in the 2026 paper (from the AMGF's own radial lower bound, Lemma 1(3)). The AMGF constant is the smaller one — this is precisely the improvement the AMGF buys over a naive net argument.
- **Optimization over $\lambda$**: $\lambda$ never appears in the final radius. In Thm 2 of [[@liuConcentrationStochasticSystem2026]] it is eliminated in closed form, $\lambda^*=\varepsilon r/\!\int_0^T\bar\sigma_\tau^2d\tau$. The residual free parameter is $\varepsilon\in(0,1)$, trading $\varepsilon_1$ against $\varepsilon_2$ — i.e. trading the $n$ cost against the $\log(1/\delta)$ cost. Experiments use $\varepsilon=1/16$, $15/16$, $0.9$ in different places, so it is genuinely tuned per problem.
- **Cost of the $\sup_t$ upgrade**: in [[@liuSafetyVerificationStochastic2024a]] the union bound costs $\log(T/\delta)$ instead of $\log(1/\delta)$ — an additive $O(\sqrt{\log T})$ in the radius. In [[@liuConcentrationStochasticSystem2026]] Thm 2 the martingale route costs **nothing** in $\delta$ ($\log(1/\delta)$ is preserved) but replaces $\Psi_t$ by $\Psi_T$, which is the wrong trade for strongly contracting systems over long horizons — hence Thm 3, which restores locality at the price of $\log\frac{2T}{\delta\Delta t}$.

**Tightness claims, verbatim in substance.** [[@liuSafetyVerificationStochastic2024a]] §IV-A: the single-time bound (Prop. 1) "is proved to be tight for the stochastic system (1), and is exact for linear systems" ([[@liuProbabilisticReachabilityDiscreteTime2024]] §4.4); therefore $r_{\delta,t}$ of Thm 2 is sharp up to the $O(\sqrt{\log T})$ union-bound term. [[@liuConcentrationStochasticSystem2026]] §III: "following [[@jafarpourProbabilisticReachabilityAnalysis2024]] Section V-E, it can be shown that our derived $r_{\delta,t}$ is **the tightest obtainable bound under Assumptions 1 and 2**". Empirical comparisons: the 2024 paper's Fig. 2 puts its curve against $3\times10^6$ Monte-Carlo samples and against Cosner–Culbertson–Ames (Freedman's inequality with discrete-time CBFs), beating the latter substantially at small $\delta$ and long $T$; the 2026 PVTOL case study reports a projected tube radius of $\max_t r_{\delta,t}=0.54$ at $\delta=10^{-4}$ where the standard ISA bound is $>10$ (literally unplottable).

## What this gives the project

- **The reduction is metric-agnostic.** [[@liuSafetyVerificationStochastic2024a]] Thm 1 assumes nothing about $f$ or $w$; it is pure set algebra ($\oplus$, $\ominus$) plus hypothesis 1. On a manifold the Minkowski sum has an obvious replacement — $\{x_t\}\oplus B^n(r,0)\rightsquigarrow$ the metric ball $B(x_t,r)\subset M$, and erosion becomes $\{x:\ \overline{B}(x,r)\subset\mathcal C\}$. That part should transfer essentially unchanged; the theorem is the licence.
- **The target statement's exact form.** Hypothesis 1 of Thm 1 *is* $\mathbb P[\sup_{t\le T}d(X_t,\bar x_t)\le r_{\delta,t}]\ge1-\delta$. Proving the intrinsic version of [[@liuConcentrationStochasticSystem2026]] Thm 2 is therefore sufficient for intrinsic set erosion.
- **The AMGF is already radial** (Lemma 1(1)–(2)): $\Phi_M(X)$ depends only on $\|X\|_M$ and is monotone in it. Replacing $\|X\|_{M_t}$ by $d(X_t,\bar x_t)$ and $\mathbb E_{\ell\in S^{n-1}}$ by an average over the unit sphere in $T_{x}M$ is the natural lift, and Lemma 1(3) — the $(1-\varepsilon^2)^{n/2}e^{\varepsilon\lambda\|X\|_M}$ lower bound — is the one inequality that must be re-derived intrinsically.
- **The proof technique is already half-geometric.** [[@liuConcentrationStochasticSystem2026]] Thm 1 argues along *geodesics* $l_t^*(s)$ of the metric $M_t$ with energy density $V(s,t)=\Phi_{M_t}(v_t(s))$ and total energy $\mathcal E(l_t)=\int_0^1V\,ds$ — a path-length-integral / contraction argument in the sense of [[@singhRobustOnlineMotion2017]] and [[@tsukamotoContractionTheoryNonlinear2021a]]. The Euclidean shortcut used, stated explicitly, is that *at frozen $t$*, $M_t$ is a **flat** metric so $l_t^*$ is a straight line, $v_t^*(s)=X_t-x_t$, and $\mathcal E(l_t^*)=\Phi_{M_t}(X_t-x_t)$. This is precisely the step that a curved manifold breaks and where curvature must enter.
- **The two-bound distinction is theirs too.** Their Problem 1 (fixed $t$) vs Problem 2 (whole trajectory) is exactly this repo's (a)/(b) split, and their Fig. 1 illustrates it. Thm 1 does not imply Thm 2; the martingale is what closes the gap without a $\sqrt{T}$ or union-bound loss.
- **A benchmark for "how conservative".** Any intrinsic bound this project produces can be compared against $r_{\delta,t}$ above in the flat case; if it does not reduce to these constants when curvature $\to0$, something has been lost.

## Caveats / limitations

- **$M_t$ is a state-*independent* metric.** Assumption 2 of [[@liuConcentrationStochasticSystem2026]] takes $M_t=M(t)$ only — no $x$-dependence. That is what makes the metric flat at frozen $t$ and the geodesic a straight line. So this paper does *not* incur the $\bar m_x,\bar m_{x^2}$ constants of [[@daniObserverDesignStochastic2015]]; it avoids them by restricting to state-independent metrics rather than by being intrinsic. A genuine state-dependent (let alone curved) version is exactly what is missing, and the flatness step is where the missing curvature terms belong.
- **Global Lipschitz / global contraction.** [[@liuSafetyVerificationStochastic2024a]] Assumption 1 is a *global* Lipschitz condition on $f$ over all of $\mathbb R^n$; [[@liuConcentrationStochasticSystem2026]] Assumption 2 asks the contraction LMI to hold along every trajectory of the deterministic system. Neither is a local or region-restricted hypothesis. On a compact Lie group the global statement may be easier; on $SE(3)$ with unbounded translations it will not be.
- **Uniformly bounded diffusion.** $g_tg_t^{\mathsf T}\preceq\sigma^2I$ — an ambient-Euclidean statement. The intrinsic replacement is presumably a bound on the trace/operator norm of the diffusion coefficient as a map $\mathbb R^m\to T_xM$, plus care about the difference between Itô and Stratonovich and the extra drift a manifold SDE carries.
- **Tube shape.** [[@liuConcentrationStochasticSystem2026]] yields an *ellipsoidal* tube $\|X_t-x_t\|_{M_t}\le r_{\delta,t}$, but set erosion in [[@liuSafetyVerificationStochastic2024a]] is stated for Euclidean balls $B^n(r,0)$. The case study bridges this by projecting the ellipsoid onto the planning plane and outer-approximating by a circle — a lossy step, and one that has no clean manifold analogue.
- **Additive noise in discrete time.** [[@liuSafetyVerificationStochastic2024a]] takes $w_t$ additive and independent of the state; the continuous-time paper allows $g_t(X_t)$ state-dependent. A discrete-time geometric integrator on a Lie group would have neither form exactly.
- **$\varepsilon$ is a free knob, not optimized.** Both papers leave $\varepsilon\in(0,1)$ to the user and admit the resulting $\varepsilon_1,\varepsilon_2$ are not optimal ([[@liuSafetyVerificationStochastic2024a]] Rmk 4.1). Any "tightness" claim is tightness of the *rate* in $\delta$ and $n$, not of the absolute constant.

:::warning[Open question — extraction gaps to verify against the PDFs]
Three items I could not resolve unambiguously from the text layer, all in [[@liuConcentrationStochasticSystem2026]]:

1. **Thm 3, eq. (20), second summand.** The text layer reads $\big(\sqrt{e^{2\psi_t}\Psi^{\Delta t}_t}+\sqrt{\Psi_t}\big)$, with no $e^{2\psi_t}$ on the second term. But that term comes from applying Thm 1 at the interval endpoint, which would give $\sqrt{e^{2\psi_{k\Delta t}}\Psi_{k\Delta t}}$ (and the proof's $r_{k\Delta t}$ does carry the exponential). Since $\psi_t\le0$ under $c_t<0$, the printed $\sqrt{\Psi_t}$ is a valid but looser relaxation. **Do not rely on the second term's exact form without checking the rendered PDF.**
2. **$\bar\sigma$ vs $\sigma$ in $\Psi^{\Delta t}_t$.** The overbar on $\sigma_\tau$ does not survive extraction reliably; Thm 1's $\Psi_t$ definitely uses $\bar\sigma_\tau=\sqrt{m_\tau}\sigma$, and $\Psi^{\Delta t}_t$ should match, but the glyph is ambiguous.
3. **Lemma 2's denominator integrand.** The text layer prints $\int_0^Tb_\tau\psi_\tau d\tau$ where $\int_0^Tb_\tau\xi_\tau d\tau$ is clearly meant (and $B(v_0,0)$ where $B(Y_0,0)$ is meant) — apparent typos in the paper, restated here in corrected form. In the results used ($b_t\equiv0$) this is moot.

Everything else — Thm 1 and 2 of both papers, both $(\varepsilon_1,\varepsilon_2)$ pairs, $\Psi_t$/$\psi_t$ in both conventions, and $\lambda^*$ — was cross-checked two ways: against the papers' own worked special cases (the $L,\sigma$ constant reduction (11) and the closed-form $\delta$-threshold (17) in [[@liuSafetyVerificationStochastic2024a]]; the explicit $r$ and $\tilde r_t$ in the proof of Thm 2 in [[@liuConcentrationStochasticSystem2026]]) and against `pdftotext -layout`.
:::
