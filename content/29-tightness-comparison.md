---
tags: [thesis, comparison, chart-dependence, curvature, conservatism, so3, se3, amgf]
---
# Curvature vs Metric-Derivative Constants — Are the Intrinsic Bounds Tighter?

**Prereq:** [[06-curvature-left-invariant-metrics]], [[08-hessian-comparison]], [[17-curvature-corrected-stiffness]], [[23-martingale-toolkit]], [[24-dani-stochastic-contraction]], [[25-intrinsic-mean-squared]], [[27-set-erosion-tubes]], [[28-intrinsic-amgf]], [[notation]]
**Goal:** put the chart-dependent and intrinsic constants side by side on two groups, attribute every factor to its actual cause, and say plainly what the thesis does and does not buy.

## 1. The claim under test

| Dani (chart) | intrinsic replacement | status |
|---|---|---|
| $\bar m_x=\sup\lvert\partial M_{ij}/\partial x\rvert$ | — | **none.** $\partial_kg_{ij}(p)=0$ in normal coordinates at $p$: a pure chart artifact ([[08-hessian-comparison]]) |
| $\bar m_{x^2}=\sup\lvert\partial^2M_{ij}/\partial x^2\rvert$ | $\mathrm{Sec}\ge\kappa$ | genuine — and **inert when $\kappa\ge0$** ([[25-intrinsic-mean-squared]]) |
| $m=\inf\lambda_{\min}M$ | — | chart conditioning; gone, since the bound is already in $d$ |
| — | $\mathrm{inj}(M)$, and (H4) | an **extra** hypothesis the chart route never states |

## 2. Sources of conservatism — the analytical spine

Every factor below is labelled. **Only (a) is what the thesis attacks.**

| | source | typical | worst case | removed by going intrinsic? |
|---|---|---|---|---|
| **(a)** | chart-dependence ($\bar m_x,\bar m_{x^2},m$) | $2.5\times$ in radius | **unbounded** | **yes** |
| **(b)** | worst-case operator norms | $\approx80\times$ | — | no — already intrinsic, already loose |
| **(c)** | bound type (A vs B) | $14$–$32\times$ | $269\times$ at $\delta=10^{-6}$ | no |
| **(d)** | residual looseness of B itself | $3.5\times$ | — | no |
| **(e)** | $T^*G\to G$ projection | $1.13\times$ | — | no |

(b) is [[17-curvature-corrected-stiffness]]: $\kappa\le(\sigma-\mu)/2$ is a uniform norm blind to the fact that $\mathrm{Jac}_v$ annihilates $v$, giving $\lambda\approx0.030\,\mathrm{s^{-1}}$ against damping $d=2.5$. (c) is [[23-martingale-toolkit]] / [[27-set-erosion-tubes]]: $O(\sqrt{1/\delta})$ against $O(\sqrt{\log(1/\delta)})$. (d) is [[23-martingale-toolkit]]'s Monte Carlo — $4\times10^4$ OU paths, $\gamma=\sigma=1$, $T=10$, $\delta=0.05$: truth $2.44$, route B $8.59$. (e) is [[30-deterministic-surrogate]]'s $c_\pi=\lambda_{\min}(\mathcal P)^{-1/2}\approx1.13$.

**If a gain from (b)–(e) is booked against (a), the thesis is not supported.**

## 3. Test case 1 — $SO(3)$, bi-invariant, $\mathbb J=\mathrm{id}$

$\mathrm{Sec}\equiv\kappa=\tfrac14$, $N=3$, $\mathrm{inj}=\pi$, $d(I,R)=\theta$. Isotropic noise $\sigma E_i$ (Case A, so (H0) holds), $\gamma$-contracting drift.

### The two charts — the choice *is* the arbitrariness at issue

**(i) Exponential coordinates**, $R=\exp_G\hat x$, $\theta=|x|<\pi$, $h(\theta)=2(1-\cos\theta)/\theta^2$:
$$g_{ij}=h\,\delta_{ij}+(1-h)\tfrac{x_ix_j}{\theta^2},\qquad \bar m_x=\sup|h'|\approx0.271,\quad \bar m_{x^2}\approx\tfrac16,\quad m=h(\pi)=\tfrac4{\pi^2}\approx0.405 .$$
Because the metric is bi-invariant this chart *is* normal coordinates at $I$, so $g_{ij}=\delta_{ij}-\tfrac{\kappa}3(\theta^2\delta_{ij}-x_ix_j)$ and $\bar m_{x^2}=\tfrac23\kappa$ **exactly** at the origin. In the best possible chart the second-derivative bound already *is* curvature; $\bar m_x\ne0$ only because it is a sup over a chart that is normal at one point.

**(ii) ZYX Euler angles** — the adversarial choice: $g=\begin{pmatrix}1&0&-\sin\vartheta\\0&1&0\\-\sin\vartheta&0&1\end{pmatrix}$.

:::tip[Proposition — what gimbal lock actually breaks]
Euler angles do **not** blow up $\bar m_x$: it stays $=1$, and $\partial_\vartheta g_{13}=-\cos\vartheta\to0$ at gimbal lock. What diverges is the **conditioning** $m=1-|\sin\vartheta|\to0$. Since Dani's rate carries $\bar m_x/m$ and $\bar m_{x^2}/m^2$ and the conclusion carries an overall $1/m$, every chart constant blows up together and Lemma 2 is vacuous near $\vartheta=\pm\pi/2$ at **any** noise level. Nothing intrinsic changes: $\mathrm{Sec}\equiv\tfrac14$, $\mathrm{inj}=\pi$ there as everywhere.
:::

`CLAUDE.md` names $\bar m_x,\bar m_{x^2}$ as the load-bearing artifacts. On the chart an engineer would actually reach for, the load-bearing artifact is $m$. Same mechanism as [[24-dani-stochastic-contraction]]'s two-chart example, where $m$ drops to $(1-a)^2$ while $\bar m_x,\bar m_{x^2}$ grow like $a\omega,a\omega^2$ — and there the conclusion is starker: **the two charts are related by an isometry, and chart 1 certifies rate $1$ while chart 2 certifies nothing at all.**

### Track A — the numbers

[[25-intrinsic-mean-squared]]'s Proposition at $\kappa=\tfrac14>0$: the $\varepsilon$-split vanishes identically, $\gamma=\lambda$, $C_{\mathrm{noise}}=\bar\Sigma=3\sigma^2$, so
$$\boxed{\ \limsup_t\mathbb E\,d(X_t,\bar x_t)^2\ \le\ \tfrac{3\sigma^2}{2\gamma}\ }$$
— the flat value, with **no rate degradation and no route to vacuity**. Dani in the exponential chart, with $\beta^2\le3\sigma^2/m$:
$$\gamma_1=\gamma-\tfrac{3\sigma^2}{2m^2}\big(\varepsilon\bar m_x+\tfrac{\bar m_{x^2}}2\big),\quad C=3\sigma^2+\tfrac{3\sigma^2\bar m_x}{\varepsilon m},\quad \mathbb E\|a-b\|^2\le\tfrac{C}{2m\gamma_1}.$$
At $\gamma=1,\sigma^2=0.1$, optimal $\varepsilon\approx1.05$: **$0.915$ against $0.15$ — a factor $6.1$ in $\mathbb Ed^2$, $2.5\times$ in radius, all source (a).** As $\sigma^2\to0$ the ratio tends to $1/m\approx2.47$ (residual gap = chart conditioning, still (a)); and Dani dies outright once $3\sigma^2\bar m_{x^2}/(4m^2)\ge\gamma$, i.e. $\sigma^2\ge1.31\gamma$.

Two deflations. [[25-intrinsic-mean-squared]] records that **[[@phamStochasticContractionRiemannian2013]] already made this substitution in 2013** and already carries no $\bar m_x,\bar m_{x^2}$ — so the $6.1\times$ is a real gain over Dani but not a new one. And its **(H4) is circular for track A alone**: closing it needs $\mathbb P[\tau_\rho\le T]$, a $\sup_t$ statement, i.e. track B. Track A cannot certify its own region of validity.

### Track B — what curvature costs the AMGF

[[28-intrinsic-amgf]]'s master identity $\Delta\Phi_\lambda=\lambda^2\Phi_\lambda+\tfrac{\lambda\varphi_N'(\lambda r)}{r}\mathcal D(r)$, $\mathcal D=r\Delta r-(N-1)$, gives $\mathcal D\le0$ for $\kappa\ge0$: on $SO(3)$ the affine-martingale coefficient is unchanged and the Euclidean radius $r_{\delta,t}=\sqrt{e^{2\psi_t}\Psi_T(\varepsilon_1N+\varepsilon_2\log\tfrac1\delta)}$ transfers **verbatim**.

:::warning[The curvature dividend evaporates at the operating point]
[[28-intrinsic-amgf]] computes the strict gain over flat: $\eta=12.4\%$ at $\lambda=1,r=\pi/2$, but only $2.6\%$ at $\lambda=10$, since $\eta=O(|\mathcal D|/z)$. The proof optimises $\lambda^*=\varepsilon r/\!\int_0^T\bar\sigma^2$, which is **large exactly in the small-$\delta$ regime the method exists for**. So the intrinsic track-B bound is not "tighter than Euclidean" in any useful sense — it is *equal* to it, and newly *applicable* on a curved $Q$. Nor is there a chart-dependent competitor: [[@liuConcentrationStochasticSystem2026]] avoids $\bar m_x,\bar m_{x^2}$ by restricting to a state-**independent** $M_t$, not by being intrinsic.
:::

### Track A against track B — reconciled

Both radii share one expression, $\text{ratio}=\sqrt{N/\delta}\big/\sqrt{\varepsilon_1N+\varepsilon_2\log(1/\delta)}$ (at $\varepsilon=0.9$):

| $N$, $\delta$ | A | B | ratio | source |
|---|---|---|---|---|
| $6$, $10^{-3}$ | $5.09$ | $0.356$ | $14.3$ | [[27-set-erosion-tubes]] worked example |
| $3$, $10^{-4}$ | $173$ | $5.38$ | $32.2$ | here |
| —, $10^{-6}$ | — | — | $269$ | [[27-set-erosion-tubes]] problem 4(a), pure $\delta$-rate |

Consistent — the same formula at different $(N,\delta)$. The ratio **grows without bound as $\delta\to0$**: a rate difference, not a constant, so no sharpening of A's second moment can close it. Against simulated truth ([[23-martingale-toolkit]]) even B is $3.5\times$ loose, while A+union at $N=1000$ nodes is $41\times$ loose and still proves no $\sup_t$ statement.

## 4. Test case 2 — $SE(3)$, left-invariant

:::tip[Proposition — "no bi-invariant metric" does **not** imply mixed-sign curvature]
For $\mathbb I=\mathrm{diag}(\mathbb J,m\,\mathrm{id})$ the metric is $\|(\Omega,R^\top\dot p)\|^2=\Omega^\top\mathbb J\Omega+m|\dot p|^2$, i.e. isometric to the **Riemannian product** $SO(3)_{\mathbb J}\times\mathbb R^3$. Verified numerically: $\mathbb J=\mathrm{id}$ gives $\mathrm{Sec}\in[0,\tfrac14]$ — *nonnegative*; $\mathbb J=\mathrm{diag}(1,2,3)$ reproduces exactly the $SO(3)$ values $\{-\tfrac13,+\tfrac13\}$ on rotational planes and $0$ elsewhere. **Mixed sign on $SE(3)$ requires a rotation–translation coupling** (a screw metric): $\mathbb I=\begin{pmatrix}\mathrm{id}&\tfrac12\mathrm{id}\\\tfrac12\mathrm{id}&\mathrm{id}\end{pmatrix}$ gives $\mathrm{Sec}\in[-0.24,0.25]$.
:::

This corrects the study plan's premise that $SE(3)$ is automatically the mixed-sign test case. Chart side: the natural chart is Euler angles $\times$ Cartesian $p$, metric $\mathrm{diag}(E^\top E,m\,\mathrm{id})$, so §3's gimbal-lock degeneracy transfers unchanged. Intrinsic side at $\kappa=-0.24$, $N=6$: track A pays [[25-intrinsic-mean-squared]]'s $\varepsilon$-split; track B pays [[28-intrinsic-amgf]]'s additive $\tfrac12\lambda\sigma^2(N-1)\sqrt{|\kappa|}$ in $a_t$. Both finite, both chart-free, neither small. Also $\mathrm{inj}(SE(3))\le\pi$ — the closed geodesic $t\mapsto\exp_G(t\hat e_1)$ has length $2\pi$.

## 5. The verdict

:::warning[The decisive caveat — neither track has a $\kappa$ on the state manifold]
Every number in §3 is for the **kinematic** problem on $SO(3)$, $N=3$. A mechanical system's tube lives on $T^*SO(3)$, $N=6$, certified by the cross-term metric of [[16-cross-term-metrics]] — whose sectional curvature nobody has computed, which [[13-sasaki-metric]] shows is **sign-indefinite and grows with $\|u\|^2$** (sign flip at $|\Omega|\approx2.31\,\mathrm{rad/s}$), and for which no $\mathrm{inj}$ is known. [[28-intrinsic-amgf]] deliberately quotes no number there; [[25-intrinsic-mean-squared]] warns its $4.96^\circ$ is not a rigid-body result. **So (i) and (ii) below hold for the kinematic case only.** The chart route is blocked identically — it needs $\bar m_x,\bar m_{x^2}$ for the same unknown metric — so this favours neither side; it means the headline comparison is not yet available on the object the project actually targets.
:::

**(i) Mean-squared: yes, but modestly, and not novel.** $6.1\times$ in $\mathbb Ed^2$ on $SO(3)$, plus the qualitative win that $\gamma_1=\gamma$ for $\kappa\ge0$ so the bound can never go vacuous. Source (a). But [[@phamStochasticContractionRiemannian2013]] had it in 2013, and (H4) means track A cannot stand alone.

**(ii) Sup-$t$: not tighter — newly applicable.** Constants identical to Euclidean for $\kappa\ge0$; the strict dividend is $\le12.4\%$, decaying to $2.6\%$ at the $\lambda$ the method actually uses.

**(iii) A loses $14$–$32\times$ to B**, unboundedly as $\delta\to0$, and does not deliver the $\sup_t$ statement at all.

:::warning[The thesis survives as a robustness claim, not a tightness claim]
By *magnitude*: **(b) $80\times$ > (c) $14$–$269\times$ > (d) $3.5\times$ > (a) $2.5\times$ > (e) $1.13\times$**. So `CLAUDE.md`'s "that is where the conservatism comes from" is **not supported** — chart-dependence is among the smallest contributors.

But (a) is the only source that is **unbounded and arbitrary**. [[24-dani-stochastic-contraction]]'s two charts differ by an isometry and give rate $1$ versus *no certificate*; ZYX Euler angles do the same on $SO(3)$ near gimbal lock. The honest restatement: **going intrinsic does not reduce the bias, it removes the variance** — it makes the answer independent of a choice for which no principled selection rule exists. That is worth having, and it is a different claim from "tighter". The largest *actionable* tightening is (c), then (b), and neither is geometric.
:::

## 6. What would settle the rest

1. **Compute $\mathrm{Sec}$ and $\mathrm{inj}$ for the cross-term metric on $T^*SO(3)$.** The single blocking computation: without it neither track has a number on the real state manifold. [[13-sasaki-metric]] gives the horizontal/vertical pieces; the cross term $b$ is what is missing.
2. **Attack (b).** Redo [[17-curvature-corrected-stiffness]] with state-dependent $a,b,c$ so $\kappa$ tracks the anisotropy of $\mathrm{Jac}_v$. If $\lambda$ reaches within $2\times$ of $d$, the ranking changes.
3. **Attack (d).** [[23-martingale-toolkit]]'s $3.5\times$ comes from discarding the drift in the AM; a time-varying $\lambda_t=\lambda_0e^{\gamma t}$ should recover it.
4. **Is $\bar m_{x^2}\ge c\,|\kappa|$ in *every* chart?** It equalled $\tfrac23\kappa$ here only because exponential $=$ normal coordinates. A general lower bound would upgrade "curvature is the replacement" to a theorem.

## Problems

1. **Recall.** Name the five sources of conservatism with one number each, say which the thesis addresses, and explain in two sentences why the magnitude ranking and the robustness argument reach different verdicts on it.

2. **Compute.** On $SO(3)$, $\mathbb J=\mathrm{id}$: find $\bar m_x$ and $m$ in (a) exponential coordinates and (b) ZYX Euler angles, from the two metrics in §3. Which quantity degrades at gimbal lock, and which of $\bar m_x/m$, $\bar m_{x^2}/m^2$, $1/m$ diverge there?

3. **Prove.** (a) From $g_{ij}(x)=\delta_{ij}-\tfrac13R_{ikjl}x^kx^l+O(|x|^3)$ show $\partial_kg_{ij}(p)=0$ in normal coordinates at $p$. (b) Deduce $\bar m_x$ can be zeroed at any *single* point, but $\partial g\equiv0$ on an open set forces $R\equiv0$ there — so $\bar m_x=0$ on a neighbourhood iff flat.

4. **Break it.** Flat torus $T=\mathbb R^3/(L\mathbb Z)^3$, $L=0.1$, same noisy contracting dynamics. Give $\kappa$, $\mathrm{inj}(T)$, and $\bar m_x,\bar m_{x^2},m$ in the covering chart. Show Dani's Lemma 2 applies unconditionally and is *exact*, while [[25-intrinsic-mean-squared]]'s (H4) restricts to $\rho<0.05$. State the moral in one line.

---

## Solutions

**1.** (a) chart-dependence, $2.5\times$ typical / unbounded worst; (b) worst-case norms, $80\times$; (c) bound type, $14$–$269\times$; (d) B's own slack, $3.5\times$; (e) projection, $1.13\times$. The thesis addresses (a) only. The verdicts differ because they measure different things: *magnitude* asks how much tighter the bound gets in a chart someone actually picked, and there (a) is the smallest term; *robustness* asks how far the bound can move under a change that alters nothing physical, and there (a) is the only unbounded term — [[24-dani-stochastic-contraction]] exhibits an isometry taking rate $1$ to no certificate at all. Removing (a) is variance reduction, not bias reduction.

**2.** (a) Along $x=(\theta,0,0)$: $g=\mathrm{diag}(1,h,h)$, $\partial_1g_{22}=h'(\theta)$ with the other derivatives of $g_{22}$ vanishing there, $g_{11}\equiv1$ along the ray so $\partial g_{11}=0$, and $\partial_2g_{12}=(1-h)/\theta\le0.19$. So $\bar m_x=\sup|h'|\approx0.271$ (near $\theta\approx2.65$) and $m=h(\pi)=4/\pi^2\approx0.405$. (b) $\partial_\vartheta g_{13}=-\cos\vartheta$ gives $\bar m_x=1$, and $\lambda_{\min}=1-|\sin\vartheta|$ gives $m=1-|\sin\vartheta|$. A factor $3.7$ in $\bar m_x$ between two charts carrying the *same* metric on the *same* manifold — the definition of a chart artifact. At $\vartheta\to\pm\pi/2$ the derivative bounds do **not** blow up ($\bar m_x\to0$, $\bar m_{x^2}\to1$) but $m\to0$, so all three of $\bar m_x/m$, $\bar m_{x^2}/m^2$ and $1/m$ diverge: $\gamma_1\to-\infty$ *and* the conclusion's prefactor $\to\infty$. Lemma 2 fails twice over, and neither failure is the one `CLAUDE.md` names.

**3.** (a) The displayed expansion has no term linear in $x$, so differentiating once at $x=0$ kills the quadratic term and the $O(|x|^3)$ remainder alike: $\partial_kg_{ij}(0)=0$. (b) Applying this at each $p$ in its own normal chart zeroes the *pointwise* value of $\partial g$; but $\bar m_x$ is a sup over a chart domain and a chart is normal at one point only, so this does not make $\bar m_x=0$. If instead $\partial_kg_{ij}\equiv0$ throughout an open $U$ in some chart, then $g$ is constant on $U$, all Christoffel symbols vanish, and $R\equiv0$ on $U$; conversely a flat $U$ admits coordinates with $g=\delta$. So $\bar m_x=0$ over a neighbourhood $\iff$ flat there: the first-derivative bound has no intrinsic content at a point and only the trivial content on a set.

**4.** $\mathrm{Sec}\equiv0$ so $\kappa=0$ and every curvature bound is two-sided sharp; $\mathrm{inj}(T)=L/2=0.05$ ([[08-hessian-comparison]] problem 4(b)). In the covering chart $M=I$, so $\bar m_x=\bar m_{x^2}=0$ and $m=1$: **the constants the thesis removes are already exactly zero**, $\gamma_1=\gamma$, $C=C_1+C_2$, and Lemma 2 reproduces the exact Ornstein–Uhlenbeck answer with no restriction on the tube radius. The intrinsic route needs $r^2$ smooth, i.e. (H4)'s $\rho<\mathrm{inj}=0.05$, and says nothing about a tube of radius $0.06$ — even though its curvature hypothesis is perfect, and even though no curvature bound of any kind distinguishes $T$ from $\mathbb R^3$ (where $\mathrm{inj}=\infty$). Moral: going intrinsic trades two chart constants for one curvature constant **plus a new topological hypothesis**, and on nearly-flat spaces with small injectivity radius that trade is a net loss.
