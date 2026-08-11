---
tags: [probabilistic-tube, set-erosion, amgf, safety-verification, concentration-inequality, contraction]
---
# Set Erosion and the Probabilistic Tube

**Prereq:** [[23-martingale-toolkit]] (affine martingale, Doob/Ville, and the two routes A/B), [[26-euclidean-amgf]] ($\Phi_{N,\lambda}$, its radial form and the $(1-\varepsilon^2)^{N/2}e^{\varepsilon\lambda\|x\|}$ lower bound); notation fixed in [[notation]].
**Goal:** know how the tube radius $r_{\delta,t}$ is actually built, in what precise sense it is *tight*, and which steps of the construction are $\mathbb R^N$-specific — so that [[28-intrinsic-amgf]] knows exactly what it has to replace.

:::warning[Dimension symbol — $n$ vs $N$]
The sources ([[@liuSafetyVerificationNonlinear2025]], [[@liuSetErosionTubes]]) write $n$ for the **state** dimension, and [[26-euclidean-amgf]] keeps their $n$ so that $\Phi_{n,\lambda}$ matches the literature verbatim. [[notation]] reserves $n=\dim G$ for the *configuration* dimension. Since this lesson quotes bounds that will be evaluated on $T^*G$, it writes $N$ everywhere the papers write $n$: $\Phi_{N,\lambda}$, $S^{N-1}$, $\varepsilon_1N$. On $T^*G$, $N=2\dim G$. Every formula below is quoted with the substitution already made.
:::

## The decomposition: a deterministic curve plus a radius

Fix the continuous-time system and its **associated** deterministic trajectory — same initial condition, same input/disturbance realisation, noise deleted:
$$dX_t=f(X_t,d_t,t)\,dt+g_t(X_t)\,dW_t,\qquad \dot x_t=f(x_t,d_t,t),\qquad X_0=x_0 .$$

:::info[Definition III.1 — probabilistic tube, [[@liuSafetyVerificationNonlinear2025]]]
Given $T>0$, $\delta\in(0,1)$ and a curve $r_{\delta,\cdot}:[0,T]\to\mathbb R_{\ge0}$, the set
$$\mathcal T=\{(t,y)\ :\ 0\le t\le T,\ \|y\|\le r_{\delta,t}\}$$
is a **probabilistic tube** if for *every* associated pair $(X_t,x_t)$,
$$\mathbb P\big[(t,X_t-x_t)\in\mathcal T\ \ \forall t\le T\big]=\mathbb P\big[\|X_t-x_t\|\le r_{\delta,t}\ \ \forall t\le T\big]\ \ge\ 1-\delta .$$
The quantifier is inside the probability: one $\delta$-budget for the **whole trajectory**, not per time instant.
:::

The structural content is the split of the reachable envelope into

$$\underbrace{x_t}_{\text{deterministic, plannable}}\quad\oplus\quad\underbrace{B(r_{\delta,t})}_{\text{stochastic, certified once}} .$$

Why this is the useful factorisation: $x_t$ is an ordinary ODE trajectory, so it can be handed to a trajectory optimiser, an MPC solver or a barrier-function argument with no probability anywhere in the loop; $r_{\delta,t}$ is a *certificate* computed offline from $(c,\sigma,N,\delta,T)$ alone and never re-solved. The stochastic problem is thereby paid for exactly once. This is the shape the deterministic surrogate of lesson 30 needs.

## Set erosion: all the work is in the radius

:::tip[Theorem — set-erosion strategy, [[@liuSafetyVerificationStochastic2024a]] Thm 1 / [[@liuSafetyVerificationNonlinear2025]] Thm 1]
Let $\mathcal C$ be a safe set and $\mathcal T$ a probabilistic tube with radius $r_{\delta,t}$. If the deterministic trajectory satisfies
$$x_t\in\mathcal C\ominus B(r_{\delta,t},0)\qquad\text{for all }t\le T,$$
then $\mathbb P\big[X_t\in\mathcal C\ \ \forall t\le T\big]\ge1-\delta$.
:::

*Proof.* On the tube event, $X_t\in\{x_t\}\oplus B(r_{\delta,t},0)$ for every $t\le T$. The erosion hypothesis says exactly that this Minkowski sum lies in $\mathcal C$. The tube event has probability $\ge1-\delta$. $\square$

:::tip[The point of the theorem]
**It assumes nothing about $f$ and nothing about $g$.** No Lipschitz constant, no contraction rate, no noise model, no regularity — those enter *only* through the construction of $r_{\delta,t}$. The theorem is pure set algebra plus hypothesis (1).
:::

So the reduction "stochastic safety on $\mathcal C$ $\Leftarrow$ deterministic safety on the eroded set" is free, and **the entire mathematical content of the programme sits in producing a small $r_{\delta,t}$**. That is the one structural fact to carry into [[28-intrinsic-amgf]]: an intrinsic tube radius is *sufficient* for intrinsic set erosion, because erosion transfers to a metric space verbatim ($\mathcal C\ominus B(r)\rightsquigarrow\{x:\overline B(x,r)\subset\mathcal C\}$).

## The radius, explicitly

**Discrete time** ([[@liuSafetyVerificationStochastic2024a]] Thm 2), $X_{t+1}=f(X_t,d_t,t)+w_t$ with $f$ $L_t$-Lipschitz and $w_t\sim\mathrm{subG}(\sigma_t^2)$:
$$r_{\delta,t}=\sqrt{\Psi_t\big(\varepsilon_1N+\varepsilon_2\log(T/\delta)\big)},\qquad \Psi_t=\psi_{t-1}\sum_{k=0}^{t-1}\sigma_k^2\psi_k^{-1},\quad \psi_t=\prod_{k=0}^{t}L_k^2,$$
with $\varepsilon_1=\dfrac{2\log(1+2/\varepsilon)}{(1-\varepsilon)^2}$, $\varepsilon_2=\dfrac{2}{(1-\varepsilon)^2}$ from an $\varepsilon$-net. The $\log(T/\delta)$ is the price of a **union bound** over the $T$ steps. (Beware: this $\varepsilon$ is the *net radius*, the complement of the $\varepsilon$ in the continuous-time constants below and in [[26-euclidean-amgf]]'s net comparison. Do not carry a numerical value across.)

**Continuous time** ([[@liuConcentrationStochasticSystem2026]] Thm 2), $\mu(D_xf)\le c_t$ and $g_tg_t^{\mathsf T}\preceq\sigma^2I$:
$$\boxed{\;r_{\delta,t}=\sqrt{e^{2\psi_t}\,\Psi_T\big(\varepsilon_1N+\varepsilon_2\log(1/\delta)\big)}\;},\qquad \psi_t=\int_0^tc_\tau d\tau,\quad \Psi_t=\int_0^t\bar\sigma_\tau^2e^{-2\psi_\tau}d\tau,$$
with $\bar\sigma_\tau=\sqrt{\lambda_{\max}(M_\tau)}\,\sigma$ and now $\varepsilon_1=\dfrac{\log\frac1{1-\varepsilon^2}}{\varepsilon^2}$, $\varepsilon_2=\dfrac{2}{\varepsilon^2}$ — the AMGF's own constants, smaller than the net's. Here the $\sup_t$ upgrade is done by the affine martingale of [[23-martingale-toolkit]] and costs **nothing in $\delta$**; it costs $\Psi_t\rightsquigarrow\Psi_T$ instead. ($\psi$ is overloaded across the two papers: here $\psi_t=\int c$, in Doob's step of [[@liuSafetyVerificationNonlinear2025]] it is the discount $e^{\int_t^Ta}$.)

| Ingredient | What it is | Where it enters |
|---|---|---|
| $c_t$ | contraction / one-sided-Lipschitz rate, $\mu(D_xf)\le c_t$; $c_t<0$ = contracting | $e^{2\psi_t}$, the Grönwall-type factor |
| $\sigma$ | noise intensity, $gg^{\mathsf T}\preceq\sigma^2I$ | linearly: $r\propto\sigma$ via $\sqrt{\Psi_T}$ |
| $N$ | state dimension | additively, as $\varepsilon_1N$ |
| $\delta$ | confidence | additively, as $\varepsilon_2\log(1/\delta)$ |
| $\varepsilon\in(0,1)$ | free knob trading $\varepsilon_1$ against $\varepsilon_2$ | both |
| $\lambda$ | AMGF parameter — **eliminated in closed form**, $\lambda^*=\varepsilon r/\!\int_0^T\bar\sigma_\tau^2d\tau$ | nowhere |

The two factors are completely decoupled: $r_{\delta,t}=\sqrt{\text{system}}\times\sqrt{\text{concentration}}$.

**Dimension.** $r_{\delta,t}=O(\sqrt N)$, and this is the *correct* scaling — the norm of an $N$-dimensional Gaussian concentrates at $\sigma\sqrt N$, so it is not conservatism. But on $T^*G$ we have $N=2\dim G$, so a rigid body ($\dim G=3$) already pays $\sqrt6$ and $SE(3)$ pays $\sqrt{12}$.

## Worked example — an OU system, and the price of route A

Take $dX_t=-X_t\,dt+\sigma\,dW_t$ on $\mathbb R^N$, so $D_xf=-I$ and $c=-1$; and set $\sigma=0.1$, $T=1$, $N=6$ (i.e. $T^*SO(3)$), $\delta=10^{-3}$, $\varepsilon=0.9$.

Constants: $\varepsilon_1=\log(1/0.19)/0.81=2.0503$, $\varepsilon_2=2/0.81=2.4691$, $\log(1/\delta)=6.9078$, so
$$\varepsilon_1N+\varepsilon_2\log(1/\delta)=12.302+17.056=29.358,\qquad \sqrt{\;\cdot\;}=5.418 .$$
System factor: $\psi_t=-t$, $\Psi_T=\sigma^2\int_0^1e^{2\tau}d\tau=0.01\cdot\tfrac{e^2-1}{2}=0.031945$, $\sqrt{\Psi_T}=0.17873$. Hence
$$r_{\delta,t}=e^{-t}\,(0.17873)(5.418)=0.968\,e^{-t},\qquad r_{\delta,T}=0.356 .$$

**Route A on the same system.** The OU covariance is exact: $\mathbb E\|X_t-x_t\|^2=N\sigma^2\frac{1-e^{-2t}}2$, giving $0.02594$ at $t=1$. Chebyshev/Markov at level $\delta$ gives $r_{\mathrm{Cheb}}=\sqrt{0.02594/10^{-3}}=5.09$.

$$\textbf{0.356 (route B, all }t\le T)\quad\text{versus}\quad\textbf{5.09 (route A, at }t=1\text{ only)} .$$

A factor $14$, and the comparison is *unfair in route A's favour*: 5.09 certifies one time instant with an exact second moment, while 0.356 certifies the whole horizon. This is the quantitative payoff of route B in [[23-martingale-toolkit]]. Note also where B is weak: $r_{\delta,0}=0.968$ though $X_0-x_0=0$ exactly — the $\Psi_t\rightsquigarrow\Psi_T$ trade is loose for $c<0$ at $t\ll T$, which is what [[@liuConcentrationStochasticSystem2026]] Thm 3 (interval splitting) exists to repair.

## In what sense it is tight

- **In $\delta$:** $O(\sqrt{\log(1/\delta)})$, against $O(\sqrt{1/\delta})$ for any Chebyshev/Markov-on-a-moment argument — the [[@daniObserverDesignStochastic2015]] route A. This is the headline and it is a *rate* claim, not a constant claim.
- **In the class:** [[@liuConcentrationStochasticSystem2026]] §III calls $r_{\delta,t}$ the tightest obtainable bound under its two assumptions (bounded diffusion, $c_t$-contraction), following [[@jafarpourProbabilisticReachabilityAnalysis2024]] §V-E; and the single-time bound is **exact for linear systems** (for $f\equiv0,g\equiv1,N=1$ it reproduces the reflection principle).
- **Empirically:** the PVTOL case study of [[@liuConcentrationStochasticSystem2026]] reports $\max_t r_{\delta,t}=0.54$ at $\delta=10^{-4}$ where the standard incremental-stability bound gives $>10$.
- **Not tight in:** the constant $\varepsilon_1,\varepsilon_2$ (both papers admit $\varepsilon$ is un-optimised), and the $c<0$, $t\ll T$ regime above.

:::warning[Open question — the four Euclidean steps lesson 28 must replace]
Every element of the construction above uses the vector-space structure of $\mathbb R^N$ somewhere:

1. **$S_t=X_t-x_t$ is a subtraction of states.** No such operation exists on $M$; the replacement is $\log_{\bar x_t}(X_t)\in T_{\bar x_t}M$ (the **Riemannian** $\log_p$, not $\log_G$ — see [[riemannian-geometry]]) or just $d(X_t,\bar x_t)$, and then $S_t$ does not satisfy an SDE in a fixed vector space, because the tangent space moves with $\bar x_t$.
2. **The rescaling $\tilde X_t=e^{-ct}X_t$** is how *both* papers reduce general $c$ to the case $c=0$. It is scalar multiplication of a state and has **no manifold analogue whatsoever**. General $c$ will need a different device — plausibly a time-varying $\lambda_t$ inside the affine martingale.
3. **The sphere $S^{N-1}$ is fixed and base-point independent** in $\Phi_{N,\lambda}(x)=\mathbb E_{\ell\sim S^{N-1}}e^{\lambda\langle\ell,x\rangle}$. Intrinsically the average must run over the unit sphere of $T_{\bar x_t}M$, which moves; whether the resulting object is still radial is the first thing to check.
4. **Minkowski erosion $\mathcal C\ominus B$** needs $\oplus$. The metric-ball replacement $\{x:\overline B(x,r)\subset\mathcal C\}$ makes the *theorem* survive, but its Minkowski algebra does not, and the ellipsoid-to-ball outer approximation the PVTOL study uses has no clean analogue.

Item 2 is the one with no proposed fix anywhere in the literature. Items 1, 3, 4 have candidate replacements; item 2 is an open construction.
:::

## Problems

1. **Recall.** State Definition III.1 and the set-erosion theorem. Then answer in one sentence each: (a) what regularity does the erosion theorem assume about $f$ and $g$? (b) where does the quantifier "$\forall t\le T$" sit relative to $\mathbb P$, and why does moving it out change the statement?

2. **Compute.** Pure Brownian motion, $dX_t=\sigma\,dW_t$ (so $c=0$, $f\equiv0$), with $\sigma=0.2$, $T=4$, $N=2$, $\delta=0.01$, $\varepsilon=0.9$. Compute $\Psi_T$ and $r_{\delta,t}$. Is $r_{\delta,t}$ increasing in $t$? Explain what your answer means about the cost of the $\sup_t$ upgrade in this case.

3. **Prove.** Prove the erosion theorem from Definition III.1 in two lines. Then prove the reachable-set corollary: if $\mathcal R_t$ denotes the reachable set of the *deterministic* system at time $t$ from $\mathcal X_0$ and $\mathcal R_t\subset\mathcal C\ominus B(r_{\delta,t},0)$ for all $t\le T$, then every stochastic trajectory from $\mathcal X_0$ is safe with probability $\ge1-\delta$.

4. **Break it.**
   (a) At $\delta=10^{-6}$, compute $\sqrt{\log(1/\delta)}$ and $\sqrt{1/\delta}$ and their ratio. A certification standard demands $\delta=10^{-6}$; state what the two numbers mean for whether route A can ever meet it by tightening constants.
   (b) Let $\mathcal C$ be a ball of radius $R=0.5$ in $\mathbb R^6$ and use the worked example's radius. Show the erosion hypothesis is unsatisfiable for $t$ below some $t^\ast$, compute $t^\ast$, and say what has gone wrong — is the *system* unsafe, or the *bound* vacuous?

---

## Solutions

**1.** Definition and theorem as stated above. (a) *Nothing*: no Lipschitz, no contraction, no noise model. All regularity lives in the construction of $r_{\delta,t}$, not in the erosion step. (b) Inside: $\mathbb P[\forall t\le T:\ \cdot\,]\ge1-\delta$. Moving it out gives $\forall t\le T:\ \mathbb P[\cdot]\ge1-\delta$, a family of *pointwise* statements which does not bound the probability of the union of the failure events; recovering the inside version from it costs a union bound (hence $\log(T/\delta)$, or in continuous time nothing finite at all). That gap is precisely why the affine martingale is used.

**2.** $\psi_t=0$, so $\Psi_T=\int_0^4\sigma^2d\tau=0.04\cdot4=0.16$ and $e^{2\psi_t}=1$. With $\varepsilon=0.9$: $\varepsilon_1=2.0503$, $\varepsilon_2=2.4691$, $\log(1/0.01)=4.6052$, so $\varepsilon_1N+\varepsilon_2\log(1/\delta)=4.101+11.369=15.470$. Hence $r_{\delta,t}=\sqrt{0.16\times15.470}=\sqrt{2.475}=1.573$, **constant in $t$** — not increasing. That constancy is the striking part: at $c=0$ the trajectory-level radius equals the fixed-time radius $\sqrt{\Psi_T(\cdots)}$ at $t=T$, so the $\sup_{t\le T}$ upgrade is obtained **for free** — no $\sqrt{\log T}$, no union bound, no inflation. This is exactly what route A cannot do.

**3.** Erosion: on the tube event (probability $\ge1-\delta$), $\|X_t-x_t\|\le r_{\delta,t}$ for all $t\le T$, i.e. $X_t\in\{x_t\}\oplus B(r_{\delta,t},0)$; the hypothesis $x_t\in\mathcal C\ominus B(r_{\delta,t},0)$ says $\{x_t\}\oplus B(r_{\delta,t},0)\subseteq\mathcal C$ by the definition of $\ominus$ as the largest set whose sum with $B$ stays in $\mathcal C$. Hence $X_t\in\mathcal C$ for all $t\le T$ on that event. Corollary: fix any $X_0=x_0\in\mathcal X_0$ and any admissible $d_\cdot$. Its associated deterministic trajectory satisfies $x_t\in\mathcal R_t\subset\mathcal C\ominus B(r_{\delta,t},0)$ by hypothesis, so the theorem applies to that pair. Since Definition III.1 quantifies over *all* associated pairs, the same $r_{\delta,t}$ works for every initial condition, and the bound is uniform over $\mathcal X_0$. (Note what is being used: the tube is a statement about pairs, so it composes with any deterministic over-approximation of $x_t$.)

**4(a).** $\log(10^6)=13.8155$, $\sqrt{\;}=3.717$; $\sqrt{10^6}=1000$. Ratio $269$. Route A's radius is $\sqrt{\mathbb E\|S_t\|^2/\delta}$ — the $\delta$-dependence is structural, coming from Markov's inequality, not from a loose constant. So no improvement of $\mathbb E\|S_t\|^2$ can close a factor of 269: to match route B at $\delta=10^{-6}$ route A would need a second-moment estimate $269^2\approx7\times10^4$ times smaller than the *exact* one, which is impossible. Route A is unusable at certification levels of $\delta$, and this is a defect of the *route*, not of the analysis. (A Chernoff-style route on $e^{\lambda\|S_t\|}$ would restore $\log(1/\delta)$, but $\|S_t\|$ is not the object with a clean generator inequality — that is what $\Phi_{N,\lambda}$ is for; see [[26-euclidean-amgf]].)

**(b)** Erosion requires $r_{\delta,t}<R$, else $\mathcal C\ominus B(r_{\delta,t},0)=\emptyset$ and no $x_t$ can satisfy the hypothesis. With $r_{\delta,t}=0.968e^{-t}$ and $R=0.5$: $0.968e^{-t}<0.5\iff t>\log(1.936)=0.661$. So for $t<t^\ast=0.661$ the eroded set is empty and the certificate says nothing at all — vacuously, not negatively. Nothing is wrong with the system: at $t=0$ the deviation is *identically zero*, while the bound claims only $\le0.968$. The failure is entirely in the $\Psi_t\rightsquigarrow\Psi_T$ step of Thm 2, which charges every $t$ the noise accumulated over the whole horizon. Two fixes: shrink $T$ (the radius scales with $\sqrt{\Psi_T}$), or use the split-interval Thm 3 of [[@liuConcentrationStochasticSystem2026]], which restores locality at the cost of $\log\frac{2T}{\delta\Delta t}$. The general lesson: an erosion-based certificate degrades to *vacuous*, never to *unsound* — the failure mode is silence, and one must check $r_{\delta,t}$ against the inradius of $\mathcal C$ before believing a "safe" verdict.
