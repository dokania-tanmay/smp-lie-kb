---
tags: [stochastics, ito, stratonovich, quadratic-variation, foundations]
---
# Itô vs Stratonovich: the Non-Tensorial Correction

**Prereq:** [[probability-on-manifolds]] (generator, Kolmogorov backward/forward); the stochastics block of [[notation]] ($dW$ Itô, $\circ\,dW$ Stratonovich).
**Goal:** identify the *one* term that separates the two conventions, show it is what breaks the transformation law of the drift, and see that it is proportional to the quadratic covariation — so it is switched off in any direction carrying no noise.

Everything here happens in $\mathbb R^n$. No manifold appears, and that is the point: the chart-dependence the thesis attacks shows up **before** any curvature does. This lesson starts answering the open question left in [[probability-on-manifolds]] § Background on stochastic processes.

## Quadratic variation

:::info[Definition]
For a process $X$ on $[0,t]$ and partitions $\Pi=\{0=t_0<\cdots<t_N=t\}$,
$$[X,X]_t=\lim_{|\Pi|\to0}\sum_{j}\big(X_{t_{j+1}}-X_{t_j}\big)^2 ,\qquad
[X,Y]_t=\lim_{|\Pi|\to0}\sum_j\big(X_{t_{j+1}}-X_{t_j}\big)\big(Y_{t_{j+1}}-Y_{t_j}\big),$$
limits in probability. For a scalar Wiener process, $[W,W]_t=t$ and $[W_i,W_j]_t=\delta_{ij}t$; for any $C^1$ path, $[X,X]_t=0$.
:::

$\mathbb E\sum(W_{t_{j+1}}-W_{t_j})^2=\sum(t_{j+1}-t_j)=t$ exactly, and the variance of the sum is $O(|\Pi|\,t)$, so the limit is deterministic. That is the whole content of the shorthand
$$dW_i\,dW_j=\delta_{ij}\,dt,\qquad dW_i\,dt=0,\qquad dt\,dt=0 .$$
A Wiener path has finite quadratic variation and *infinite first variation* — and it is that second fact which forces a convention, since finite first variation would make the Riemann sums below converge to the same limit no matter where the integrand is sampled.

## The two integrals

:::info[Definition]
With $H$ adapted and $X$ a semimartingale,
$$\int_0^tH\,dX=\lim_{|\Pi|\to0}\sum_jH_{t_j}\big(X_{t_{j+1}}-X_{t_j}\big)\qquad\text{Itô — left endpoint,}$$
$$\int_0^tH\circ dX=\lim_{|\Pi|\to0}\sum_j\tfrac12\big(H_{t_j}+H_{t_{j+1}}\big)\big(X_{t_{j+1}}-X_{t_j}\big)\qquad\text{Stratonovich — trapezoidal.}$$
The midpoint rule $H_{(t_j+t_{j+1})/2}$ gives the same limit; [[@leeGeometricInterpretationBrownian2025]] uses the trapezoidal form.
:::

Subtracting the two sums leaves $\sum_j\tfrac12(H_{t_{j+1}}-H_{t_j})(X_{t_{j+1}}-X_{t_j})$, which is half a quadratic-covariation sum. Hence the **conversion**
$$\int_0^tH\circ dX=\int_0^tH\,dX+\tfrac12[H,X]_t ,\qquad\text{differentially}\quad H\circ dX=H\,dX+\tfrac12\,dH\,dX .$$

:::tip[Proposition — convention conversion in $\mathbb R^n$]
Apply this with $H=\sigma_i(x)$, $X=W_i$, using $d\sigma^k_i=\partial_l\sigma^k_i\,dx^l$ and $dx^l=\sigma^l_j\,dW_j+O(dt)$:
$$dx^k=b^k\,dt+\sigma^k_i\circ dW_i
\qquad\Longleftrightarrow\qquad
dx^k=\Big(b^k+\tfrac12\,\sigma^l_i\,\partial_l\sigma^k_i\Big)dt+\sigma^k_i\,dW_i .$$
The diffusion coefficients are **unchanged**; only the drift moves, by $\tfrac12\sum_i(\partial_{\sigma_i}\sigma_i)^k$. This is the flat-$\nabla$ case of [[@leeGeometricInterpretationBrownian2025]] Theorem 1, $\tilde X=X+\tfrac12\sum_i\nabla_{\sigma_i}\sigma_i$.
:::

## The transformation law

Let $y=\phi(x)$ be a diffeomorphism (a change of chart). Taylor-expand to second order and keep every term of order $dt$, remembering $dx^k dx^l=(\sigma\sigma^\top)^{kl}dt$:

:::tip[Theorem — Itô's lemma]
If $dx^k=\tilde b^k\,dt+\sigma^k_i\,dW_i$ (Itô) then
$$dy^a=\Big(\underbrace{\partial_k\phi^a\,\tilde b^k}_{\text{tensorial}}\;+\;\underbrace{\tfrac12\,\partial^2_{kl}\phi^a\,(\sigma\sigma^\top)^{kl}}_{\textbf{not tensorial}}\Big)dt\;+\;\partial_k\phi^a\,\sigma^k_i\,dW_i .$$
:::

Read the three pieces against how tensors are required to behave. A vector field $b$ pushes forward as $(\phi_*b)^a=\partial_k\phi^a\,b^k$ — that is the first drift term, and it is also exactly what happens to each diffusion column $\sigma_i$. So $\sigma_i$ *is* a vector field for each $i$, and $a:=\sigma\sigma^\top$ *is* a symmetric $(2,0)$-tensor. But $\partial^2_{kl}\phi^a$ is not a tensor — under a further change of chart it acquires first-derivative terms — and the second drift term has no pushforward interpretation at all.

:::tip[Corollary — the Itô drift is not a vector field]
Writing $\tilde b_{(x)}$ and $\tilde b_{(y)}$ for the Itô drift of the *same process* in the two charts,
$$\tilde b^a_{(y)}-\partial_k\phi^a\,\tilde b^k_{(x)}\;=\;\tfrac12\,a^{kl}\,\partial^2_{kl}\phi^a\;=\;\tfrac12\sum_i\partial^2\phi^a(\sigma_i,\sigma_i).$$
:::

## The organising principle

The last form is the one to remember. **The defect is the second derivative of the chart change evaluated only on the noise directions.** It is proportional to the quadratic covariation, so:

> In any set of directions where the noise coefficient vanishes — where the process has zero quadratic variation — the Itô drift transforms tensorially and picks up no correction at all, no matter how nonlinear $\phi$ is there.

Two sufficient conditions follow immediately: $\sigma\equiv0$ (an ODE — hence the ordinary chain rule, as it must be), and $\partial^2\phi(\sigma_i,\sigma_i)=0$, i.e. $\phi$ affine along the noise. The second is not a curiosity. On $T^*Q$ a change of configuration chart $q\mapsto\bar q(q)$ induces $\bar p_a=(\partial q^k/\partial\bar q^a)\,p_k$, which is **linear in the fibre coordinate** — so noise injected only into the momenta has $\partial^2\phi(\sigma_i,\sigma_i)=0$ identically. That is the Case A / Case B dichotomy that lesson 22 is built on: force noise puts the quadratic variation in a flat fibre and costs nothing; configuration noise puts it in the curved base and does not.

## Stratonovich obeys the chain rule

:::tip[Proposition]
If $dx^k=b^k\,dt+\sigma^k_i\circ dW_i$ then $dy^a=\partial_k\phi^a\circ dx^k$ — the ordinary chain rule, with no second-order term. Hence the Stratonovich drift and diffusion **both push forward as vector fields**, and a Stratonovich SDE is a chart-independent object: it can be written on a manifold with no extra structure, no connection, nothing chosen.
:::

That is the whole reason the geometric literature is written in Stratonovich form. The price is real, in both directions:

| | Itô | Stratonovich |
|---|---|---|
| chain rule | second-order correction | ordinary |
| drift under $y=\phi(x)$ | **not** a vector field | a vector field |
| $\int H\,dX$ with $X$ a martingale | martingale, mean zero | not a martingale; $\mathbb E\int H\circ dW=\tfrac12\mathbb E[H,W]\neq0$ |
| isometry | $\mathbb E\big(\int_0^tH\,dW\big)^2=\mathbb E\int_0^tH^2ds$ | fails |
| integrand regularity | adapted, measurable | needs $\sigma\in C^1$ (a semimartingale integrand) |
| physical noise limit | — | Wong–Zakai: smooth approximations of white noise converge here |

The mean-zero martingale property is not a nicety — it is what every bound in Phases 4–5 runs on. Grönwall (track A) needs $\mathbb E$ of the noise term to vanish; Doob (track B) needs a martingale to apply a maximal inequality to. So the working rule for the whole project: **transport in Stratonovich, estimate in Itô.** Convert at the last possible moment, and say which form is on the page.

## Worked example: a drift out of nothing

Take $dx=dW$ on $x>0$, started at $x_0=1$ and stopped when it hits $0$, so that $\phi(x)=x^2$ is a genuine chart change on the region in play. Then $\partial_x\phi=2x$, $\partial^2_x\phi=2$, $\sigma=1$:
$$dy=\underbrace{2x\,dW}_{\partial_x\phi\,\sigma\,dW}+\underbrace{\tfrac12\cdot2\cdot1\,dt}_{\tfrac12\partial^2\phi\,\sigma^2}
\;=\;dt+2x\,dW\;=\;dt+2\sqrt y\,dW .$$
A **driftless** process in the $x$-chart has drift $1$ in the $y$-chart. Sanity check without any calculus: $\mathbb E\,y_t=\mathbb E\,W_t^2=t$, so $\tfrac{d}{dt}\mathbb E\,y_t=1$, matching the drift. ✓

Now the same process in Stratonovich form. Since $\sigma\equiv1$ is state-independent, $dx=dW$ and $dx=\circ\,dW$ are the *same equation*, drift $0$. The chain rule gives $dy=2x\circ dW$, drift $0$ again — and $0=\phi_*0$, so the Stratonovich drift transformed correctly, as promised. Converting back closes the loop: $2x\circ dW=2x\,dW+\tfrac12\,d(2x)\,dW=2x\,dW+dt$. ✓

Note what happened to the noise on the way across: $\sigma=1$ was **additive** in $x$ and became $\sigma=2\sqrt y$, **multiplicative**, in $y$. "Additive noise" is not a property of the process either.

## Standing-question classification

Against the three categories in [content/CLAUDE.md](CLAUDE.md) § The standing question:

| Object | Category |
|---|---|
| diffusion fields $\sigma_i$, diffusion tensor $a=\sigma\sigma^\top$ | **2** — components chart-dependent, the object is not |
| Stratonovich drift $b$ | **2** — pushes forward as a vector field |
| **Itô drift $\tilde b$** | **3** — genuinely changes under a nonlinear change of variable, and it is what enters a Grönwall or Doob estimate |
| generator $\mathcal L=\tilde b^k\partial_k+\tfrac12a^{kl}\partial^2_{kl}$ | **1** — the two non-tensorial pieces cancel; lesson 20 makes this the invariant |

:::warning[Open question — "Itô" presupposes a connection]
The sharp statement is that an Itô SDE *in a chart* is written against that chart's **flat connection**, and the flat connection is chart data. [[@leeGeometricInterpretationBrownian2025]] Theorem 1 makes this explicit: the intrinsic conversion is $\tilde X=X+\tfrac12\sum_i\nabla_{\sigma_i}\sigma_i$, which is a vector field for *any* connection $\nabla$ — so "the Itô drift on a manifold" is well defined only after $\nabla$ is declared. Lesson 20 takes $\nabla$ Levi-Civita, which is a choice, not a theorem.

Consequence to check later: [[@daniObserverDesignStochastic2015]] writes its Itô SDE in one global chart and never revisits it. Some of its $\bar m_x$ (a first-derivative bound, which [[08-hessian-comparison]] argues has *no* intrinsic counterpart) may be bookkeeping for exactly this — the Christoffel symbols of the chart's flat connection, hiding in a drift. Not yet verified; lesson 24 has to trace it.
:::

## Problems

1. **Recall.** State: the definition of $[X,X]_t$; the left-endpoint and trapezoidal Riemann sums; the conversion $\int H\circ dX=\int H\,dX+\tfrac12[H,X]_t$; Itô's lemma for $y=\phi(x)$. Then say, without looking, which single term fails to transform tensorially and what it is proportional to.

2. **Compute.** (a) Find $[X,X]_t$ for $X_t=\int_0^ts\,dW_s$. (b) Geometric Brownian motion is given in Itô form as $dS=\mu S\,dt+\sigma S\,dW$ with $\mu,\sigma$ constant. Write its Stratonovich form. (c) Apply Itô's lemma to $y=\log S$ and, separately, the Stratonovich chain rule to the answer in (b); check the two results describe the same process.

3. **Prove.** (a) Show the Itô and Stratonovich drifts of the same process coincide in a given chart iff $\sigma^l_i\partial_l\sigma^k_i=0$ for every $k$ — in particular whenever $\sigma$ is state-independent (additive noise). (b) Now show that this is *not* preserved by a change of variable: give the general expression for the transformed $\sigma$ under $y=\phi(x)$ and exhibit the condition on $\phi$ under which additive noise stays additive. Conclude that "the conventions agree here" is a statement about a chart, not about a process.

4. **Break it.** Take $dx=dW$ on $\mathbb R$ and $\phi(x)=e^x$, a global diffeomorphism onto $(0,\infty)$. (a) Compute the Itô SDE satisfied by $y=e^x$ and observe that a driftless process has acquired a drift. (b) Write the same process in Stratonovich form in both charts and verify that the Stratonovich drift transforms as a vector field, i.e. that it is the pushforward of $0$. (c) Write the generator in both charts and verify they are the same operator by applying each to the coordinate function $x=\log y$. Then state the moral in one sentence.

---

## Solutions

**1.** As stated above. The offending term is $\tfrac12\partial^2_{kl}\phi^a(\sigma\sigma^\top)^{kl}=\tfrac12\sum_i\partial^2\phi^a(\sigma_i,\sigma_i)$; it is proportional to the quadratic covariation, so it lives only in the noise directions.

**2(a).** $dX=s\,dW$, so $d[X,X]_s=s^2\,ds$ and $[X,X]_t=\int_0^ts^2ds=t^3/3$. (Note $[X,X]$ is deterministic here because the integrand is; in general it is not.)

**2(b).** Going Itô $\to$ Stratonovich, subtract $\tfrac12\sigma\partial_S\sigma=\tfrac12\sigma S\cdot\sigma=\tfrac12\sigma^2S$ from the drift:
$$dS=\big(\mu-\tfrac12\sigma^2\big)S\,dt+\sigma S\circ dW .$$

**2(c).** Itô on $y=\log S$: $\partial_S\phi=1/S$, $\partial^2_S\phi=-1/S^2$, diffusion $\sigma S$, so
$$dy=\Big(\frac{\mu S}{S}+\tfrac12\Big(-\frac1{S^2}\Big)\sigma^2S^2\Big)dt+\frac{\sigma S}{S}dW=\big(\mu-\tfrac12\sigma^2\big)dt+\sigma\,dW .$$
Stratonovich chain rule on (b): $dy=\frac1S\circ dS=(\mu-\tfrac12\sigma^2)dt+\sigma\circ dW$. In the $y$-chart the diffusion coefficient $\sigma$ is constant, so $\circ\,dW$ and $dW$ agree and the two answers are literally the same equation. ✓ The $-\tfrac12\sigma^2$ is present in the Itô $\log$-drift and *absent* from the Stratonovich $S$-equation's relationship to it — it is a conversion artifact, not a feature of the process.

**3(a).** By the conversion Proposition the drifts differ by exactly $\tfrac12\sigma^l_i\partial_l\sigma^k_i$, so they agree iff that vanishes for every $k$. If $\sigma$ is constant in $x$ then $\partial_l\sigma^k_i=0$ and it vanishes. (The condition is weaker than additivity: e.g. $n=2$ with $\sigma_1=(0,\,x^1)^\top$ satisfies $\partial_{\sigma_1}\sigma_1=0$ while being state-dependent — noise that does not differentiate its own coefficient.)

**3(b).** Under $y=\phi(x)$ the new diffusion is $\hat\sigma^a_i(y)=\partial_k\phi^a\big(\phi^{-1}(y)\big)\,\sigma^k_i$. With $\sigma$ constant this is $y$-independent iff $\partial_k\phi^a$ is constant along the noise, i.e. $\partial^2\phi^a(\sigma_i,\cdot)=0$ — $\phi$ affine in the noise directions. The worked example is the minimal failure: $\sigma=1$ constant, $\phi=x^2$ not affine, $\hat\sigma=2\sqrt y$. So additive noise, and with it the agreement of the two conventions, is chart data.

**4(a).** $\partial_x\phi=\partial^2_x\phi=e^x$, $\sigma=1$, $\tilde b=0$:
$$dy=\tfrac12e^x\,dt+e^x\,dW=\tfrac12y\,dt+y\,dW .$$
Drift $\tfrac12y$ from a process whose drift was $0$.

**4(b).** In $x$: $\sigma\equiv1$ is constant, so $dx=\circ\,dW$ is the same equation, Stratonovich drift $0$. Chain rule: $dy=e^x\circ dW=y\circ dW$, Stratonovich drift $0$. And $\phi_*0=\partial_x\phi\cdot0=0$ ✓. Cross-check by converting $y\circ dW$ back to Itô: $y\,dW+\tfrac12\,dy\,dW=y\,dW+\tfrac12y\,dt$, reproducing (a). ✓

**4(c).** $x$-chart: $\mathcal L^{(x)}=\tfrac12\partial^2_x$. $y$-chart: $\mathcal L^{(y)}=\tfrac12y\,\partial_y+\tfrac12y^2\partial^2_y$. Apply each to the same *function on the state space* — the one that reads $x$ in the first chart and $\log y$ in the second:
$$\mathcal L^{(x)}x=0,\qquad
\mathcal L^{(y)}\log y=\tfrac12y\cdot\frac1y+\tfrac12y^2\cdot\Big(-\frac1{y^2}\Big)=\tfrac12-\tfrac12=0 .$$
Equal. The non-tensorial $\tfrac12a^{kl}\partial^2_{kl}$ piece of $\mathcal L$ and the non-tensorial part of the drift are the same defect with opposite signs, and cancel in the sum.

**Moral.** "The drift" of a diffusion is not a well-defined object: it is meaningless without saying *which convention* and *which chart* (equivalently, which flat connection). What survives both choices is the generator, and the second-order operator is therefore the thing every intrinsic argument must be phrased against — lesson 20.
