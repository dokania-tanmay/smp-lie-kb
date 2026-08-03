---
tags: [reference, stochastic-contraction, mean-squared-bound, observer-design, chart-dependence, euclidean-template]
---
# Observer Design for Stochastic Nonlinear Systems via Contraction-Based Incremental Stability (Dani, Chung, Hutchinson — IEEE TAC 60(3), March 2015)

Designs an observer for Itô stochastic nonlinear systems in state-dependent coefficient (SDC) form, with the observer gain synthesised by an LMI-SDARE convex program. The transferable mathematical content for this project is **not** the observer: it is **Lemma 2 (Stochastic Contraction Lemma)**, which upgrades [[@phamContractionTheoryApproach2008]] from a *state-independent* metric $M(t)$ to a *state-dependent* metric $M(x,t)$ and yields an exponentially decaying bound on $\mathbb E\|a(t)-b(t)\|^2$ between two trajectories of the same drift driven by independent Wiener processes. That is exactly the Euclidean template for bound type (a) — generator inequality $\mathcal L V \le -2\gamma_1 V + C$ plus a Grönwall-type lemma. It is simultaneously the motivating example of the conservatism this project exists to remove: the price of allowing $M$ to depend on $x$ is Assumption 1's $\bar m_x$ and $\bar m_{x^2}$, sup-norms of first and second derivatives of the **metric components in a chart**, which enter both the decay rate and the asymptotic radius.

## Notation

| Symbol | Meaning |
|---|---|
| $x(t)\in\mathbb R^n$ | state; $\dot x = f(x,t)$ is the nominal deterministic system, eq. (1) |
| $dx = f(x,t)dt + B(x,t)dW$ | Itô system, eq. (6); $B:\mathbb R^n\times\mathbb R\to\mathbb R^{n\times d}$, $W$ a $d$-dim Wiener process |
| $M(x,t)$ | symmetric, uniformly positive definite state-dependent (Riemannian) metric |
| $\gamma$ | deterministic contraction rate, defined by (3) |
| $\gamma_1$ | *degraded* stochastic contraction rate appearing in Lemma 2 |
| $m$ | $\inf_{t\ge0}\lambda_{\min} M(x(\mu,t),t)$ (Assumption 2) |
| $\bar m_x$ | $\sup_{t\ge0,i,j}\|(M_{ij}(x,t))_x\|$ — sup over $t,i,j$ of the first $x$-derivative of a metric **component** |
| $\bar m_{x^2}$ | $\sup_{t\ge0,i,j}\|\partial^2 (M_{ij}(x,t))/\partial x^2\|$ — same for the second derivative |
| $C_1, C_2$ | noise-intensity bounds, $\operatorname{tr}(B_i^T M B_i)\le C_i$ |
| $\beta_1,\beta_2$ | $\beta_1=\|B_1\|_F$, $\beta_2=\|B_2\|_F$ |
| $\varepsilon>0$ | free Young-inequality parameter, tuned in §III.A |
| $C$ | the additive constant in $\mathcal LV\le-2\gamma_1V+C$ |
| $a(t),b(t)$ | the two trajectories being compared; $x(\mu,t)$ is a path with $x(0,t)=a$, $x(1,t)=b$ |
| $\delta x$ | infinitesimal virtual displacement; $\delta z=\Theta\delta x$, $\Theta^T\Theta=M$ |
| $A(\ell,x,t),C(\eta,x,t)$ | convex combinations of SDC parametrisations, eqs. (26)–(27) |
| $P(\hat x,t)$, $K=PC^TR^{-1}$ | Riccati solution (34) and observer gain (33); the observer's metric is $P^{-1}$ |
| $\bar p_x,\bar p_{x^2},\bar b$ | Assumption 6: the $P^{-1}$ analogues of $\bar m_x,\bar m_{x^2}$, and $\|B\|_F\le\bar b$ |

Paper convention: $(A_{ij})_a$ = partial derivative of the entry w.r.t. vector $a$; $(A_{ij})_{a_ia_j}$ = double partial derivative.

## Key definitions

:::info[Definition — contraction in a state-dependent metric, eq. (3)]
$\dot x=f(x,t)$ is *contracting with rate $\gamma>0$* in $M(x,t)$ if
$$\frac{\partial f}{\partial x}^{T}M(x,t)+\dot M(x,t)+M(x,t)\frac{\partial f}{\partial x}\;\le\;-2\gamma M(x,t)\qquad\forall t,\forall x .$$
This is obtained from $\frac{d}{dt}(\delta x^TM\delta x)=\delta x^T\big[(\partial f/\partial x)^TM+\dot M+M(\partial f/\partial x)\big]\delta x$, eq. (2).
:::

:::info[Definition — generalized squared length, Lemma 2]
For a path $\mu\mapsto x(\mu,t)$ with $x(0,t)=a$, $x(1,t)=b$,
$$V(x,\delta x,t)=\int_0^1\Big(\frac{\partial x}{\partial\mu}\Big)^{T}M\big(x(\mu,t),t\big)\Big(\frac{\partial x}{\partial\mu}\Big)\,d\mu ,\qquad m\|a-b\|^2\le V(x,\delta x,t).$$
This is the squared *path* length in the metric (not the geodesic distance — the lemma is stated for the path used to connect $a$ to $b$).
:::

:::info[Assumption 1 (§III)]
$$\operatorname{tr}\!\big(B_1(a,t)^TM(x(a,t),t)B_1(a,t)\big)\le C_1,\qquad \operatorname{tr}\!\big(B_2(b,t)^TM(x(b,t),t)B_2(b,t)\big)\le C_2,$$
$$\bar m_x=\sup_{t\ge0,\,i,j}\big\|(M_{ij}(x,t))_x\big\|,\qquad \bar m_{x^2}=\sup_{t\ge0,\,i,j}\big\|\partial^2 (M_{ij}(x,t))/\partial x^2\big\| ,$$
where $C_1,C_2,\bar m_x,\bar m_{x^2}$ are constants.
:::

:::info[Assumption 2 (§III)]
The nominal deterministic system (1) is contracting in $M(x(\mu,t),t)$ in the sense of (3), and $M$ satisfies $m\triangleq\inf_{t\ge0}(\lambda_{\min}M)>0$. $f$ and $M$ are the same as in (1) and (3).
:::

The comparison system is eq. (8): two copies of the same drift $f$ driven by **independent** Wiener processes $\bar W_1,\bar W_2$, stacked as $z=(a^T,b^T)^T\in\mathbb R^{2n}$, with $B_1(a,t)=B(x(0,t),t)$, $B_2(b,t)=B(x(1,t),t)$. Existence/uniqueness is imposed by the usual global Lipschitz + linear growth conditions (7).

## Main results

:::tip[Lemma 1 — Robustness of contracting dynamics, §II.A (quoted from Lohmiller–Slotine)]
Let $T_1$ be a trajectory of the globally contracting system (1) and $T_2$ a trajectory of the perturbed system $\dot x=f(x,t)+d(x,t)$ with $d$ bounded. With $S(t)\triangleq\int_{T_1}^{T_2}\|\delta z\|$, $\delta z=\Theta(x,t)\delta x$, $\Theta^T\Theta=M$:
$$S(t)\le S(t_0)e^{-\gamma(t-t_0)}+\frac{1-e^{-\gamma(t-t_0)}}{\gamma}\sup_{x,t}\|\Theta d\|\quad\forall t\ge t_0,\qquad S(\infty)\le\frac{\sup_{x,t}\|\Theta d\|}{\gamma}.$$
Proof: $\dot S+\gamma S\le\|\Theta d\|$ then the comparison lemma. This is the *deterministic* template; Lemma 2 is its stochastic counterpart.
:::

:::tip[Lemma 2 — Stochastic Contraction Lemma, §III]
Let $V$ be the generalized squared length above with $m\|a-b\|^2\le V$. If **Assumptions 1 and 2** hold, and the initial conditions of $a,b$ (distributed as $p(a_0,b_0)$) are independent of $d\hat W_1,d\hat W_2$, then
$$\mathbb E\big[\|a(t)-b(t)\|^2\big]\;\le\;\frac1m\left(\frac{C}{2\gamma_1}+\mathbb E\big[V(x(0),\delta x(0),0)\big]e^{-2\gamma_1 t}\right)\tag{9}$$
where, for some $\varepsilon>0$,
$$\boxed{\;\gamma_1=\gamma-\frac{\beta_1^2+\beta_2^2}{2m}\Big(\varepsilon\,\bar m_x+\frac{\bar m_{x^2}}{2}\Big)>0,\qquad C=C_1+C_2+\frac{\bar m_x}{\varepsilon}\big(\beta_1^2+\beta_2^2\big),\;}$$
$\beta_1=\|B_1\|_F$, $\beta_2=\|B_2\|_F$, $\gamma$ the rate in (3).

Proof technique: Itô/Dynkin on $V$; the generator is expanded (11)–(12), the three Itô second-order terms bounded by (13)–(15), giving $\mathcal LV\le-2\gamma_1V+C$ (17); then Fubini + the Grönwall-type Lemma 3 gives (19), and $m\,\mathbb E\|a-b\|^2\le\mathbb E[V]$ gives (9). The stochastic integral is a martingale by a stopping-time argument.
:::

:::tip[Lemma 3 — Grönwall-type lemma, Appendix A (from Pham, arXiv:0704.0922)]
If $g:[0,\infty)\to\mathbb R$ is continuous, $\lambda>0$, and $g(t)-g(u)\le\int_u^t(-\lambda g(s)+C)\,ds$ for all $0\le u\le t$, then
$$g(t)\le\frac{C}{\lambda}+\Big[g(0)-\frac{C}{\lambda}\Big]^{+}e^{-\lambda t},\qquad [\cdot]^+=\max(0,\cdot).$$
:::

**§III.A — optimal $\varepsilon$.** Minimising $F(\varepsilon)=C/(2m\gamma_1)$ with $L=\bar m_x(\beta_1^2+\beta_2^2)$, the paper states $dF/d\varepsilon=0$ gives
$$(C_1+C_2)(\beta_1^2+\beta_2^2)\bar m_x\varepsilon^2+2L(\beta_1^2+\beta_2^2)\bar m_x\varepsilon-2Lm\gamma+L(\beta_1^2+\beta_2^2)\tfrac{\bar m_{x^2}}{2}=0 .$$

:::warning[Open question — a factor of 2 I could not reconcile]
Differentiating $F$ directly gives the $\varepsilon^1$ coefficient as $L(\beta_1^2+\beta_2^2)\bar m_x$, i.e. **without** the leading 2; all three other coefficients match. Either the printed equation carries a typo or my reading of the two-column extraction is off. Do not rely on this quadratic without re-checking the PDF; the constants in $\gamma_1$ and $C$ themselves are unambiguous and were cross-verified against the proof steps (13)–(16).
:::

**Remark 1.** (9) reduces to the [[@phamContractionTheoryApproach2008]] bound when $M=M(t)$ or $M=$ const, because the $(M_i)_{x_j}$ and $(M_{kl})_{x_ix_j}$ terms in (12) vanish — i.e. **$\bar m_x$ and $\bar m_{x^2}$ are exactly the price of state-dependence.**

### The observer results (LMI-SDARE) — not the transferable part

Theorems 1–2 and Corollary 1 are about the *specific* observer (31)–(34) with gain $K=PC^TR^{-1}$, $P$ solving the state-dependent differential Riccati equation (34), and they hold under **Assumptions 3–6** (uniform observability of $(A(\ell,\cdot),C(\eta,\cdot))$; state confined to a compact $D$ with $\|\Delta_1\|\le\delta_1,\|\Delta_2\|\le\delta_2,\underline\delta_3\le\|C\|\le\bar\delta_3$; $\underline p I\le P^{-1}\le\bar p I$; and Assumption 6's $\bar p_x,\bar p_{x^2},\bar b$).

:::tip[Theorem 1 (Deterministic stability)]
Under Assumptions 3–5, the virtual system $\dot q=A(\ell,q,t)q+K(\hat x,t)(C(\eta,x,t)x-C(\eta,q,t)q)$ is contracting in the metric $P^{-1}(q,t)$, giving $\|\delta q(t)\|\le\sqrt{\bar p/\underline p}\,\|\delta q(0)\|e^{-\alpha_1 t}$ with $\alpha<\alpha_1$ subject to the gain condition $\kappa_1-\kappa_2\le\kappa+(\alpha-\alpha_1)\underline p$, where $\kappa_1=\bar p\delta_1+(\bar p/\bar r\underline p)\bar\delta_3\delta_2$. Proof: partial contraction theory on $P^{-1}$.
:::

:::tip[Theorem 2 (Stochastic stability)]
Under Assumptions 3–6, $\;\mathbb E\|x-\hat x\|^2\le\frac1{\underline p}\big(\mathbb E[V(q(0),\delta q(0),0)]e^{-2\alpha_3 t}+\frac{\delta_4}{2\alpha_3}\big)$, with
$$\alpha_3=\alpha_1-\frac{\kappa_P}{2\underline p}\Big(\varepsilon_1\bar p_x+\frac{\bar p_{x^2}}{2}\Big)>0,\qquad \kappa_P=\bar b^2+\frac{\bar\delta_3^2\bar r}{\underline r^{\,2}}\operatorname{tr}\big(P^2(\hat x,t)\big),$$
$$\delta_4\;\ge\;\frac{\bar p_x}{\varepsilon_1}\,\kappa_P\;+\;\bar p\,\bar b^2+\frac{\bar\delta_3^2\bar r}{\underline r^{\,2}}\operatorname{tr}\big(P(\hat x,t)\big).$$
Proved as a special case of Lemma 2 with $M\rightsquigarrow P^{-1}$, $\bar m_x\rightsquigarrow\bar p_x$, $\bar m_{x^2}\rightsquigarrow\bar p_{x^2}$, $m\rightsquigarrow\underline p$.
:::

:::warning[Open question — over/underbars in Theorem 2 constants]
`pdftotext` loses over/underbars. In eq. (48)/(50) the $R$-bounds $\bar r I\ge R\ge\underline r I$ and the split between $\operatorname{tr}(P)$ and $\operatorname{tr}(P^2)$ are my reconstruction from the surrounding proof (the derivative terms carry $\operatorname{tr}(P^2)$ via $\kappa_P$; the first trace bound $\operatorname{tr}((KD)^TP^{-1}KD)\le(\bar\delta_3^2\bar r/\underline r^2)\operatorname{tr}(P)$ carries $\operatorname{tr}(P)$). Verify against the PDF before quoting $\delta_4$ numerically.
:::

:::tip[Corollary 1 ($L_2$ robustness)]
Under Assumptions 3–6, for $g=L(t)x$ with $L^TL\le\bar\ell I$:
$$\mathbb E_{q_0}\!\!\int_0^t\!\|g-\hat g\|^2 d\tau\le\frac{\bar\ell\,\|x(0)-\hat x(0)\|^2_{P^{-1}(0)}}{\xi_1}+\frac{\bar\ell}{\xi_1}\mathbb E_{q_0}\!\!\int_0^t\!\big(\xi_2\|d(x,\tau)\|^2+\delta_4\big)d\tau,$$
$\xi_1=(1-\theta)2\alpha_3\underline p$, $\xi_2=\bar p/\varepsilon_2$, $0<\theta=\varepsilon_2\bar p/(2\alpha_3\underline p)<1$. (The body text at §IV calls this "Theorem 3"; the numbered statement in the paper is Corollary 1.)
:::

**Synthesis machinery, in one paragraph (not what we need).** $f(x,t)=A(x,t)x$, $h(x,t)=C(x,t)x$ is the non-unique SDC parametrisation; a convex combination $A(\ell,\cdot)=\sum\ell_iA_i$, $C(\eta,\cdot)=\sum\eta_iC_i$ is used to preserve observability and to buy design freedom. Setting $\dot P=0$ in (34) gives an algebraic Riccati *inequality* (56), converted by Schur complement to a BMI (64) and then, by Shor's relaxation with lifting variables $\eta_{l_{ij}}=\eta_i\eta_j$, to an LMI (57)–(62) in $Q=P^{-1}$. A convex objective (66) trades off $\operatorname{tr}(Q^{-1})$, $\kappa$, $\alpha\lambda_{\min}(Q)$, $\lambda_{\max}(Q)$ to shrink $\delta_4/(2\underline p\alpha_3)$. CSDRE (fixed $\ell,\eta$, integrate/solve the Riccati) and Fixed-SDARE (constant $A,C$ from bounds on $D$, offline gain) are cheaper variants. Simulations: 2D robot pose + landmark SLAM, and a Lorenz oscillator; beats EKF and SDDRE on RMSE/peak error.

## Where the chart-dependence enters

The propagation is fully traceable through the proof. $\mathcal LV$ splits (eqs. (11)–(12)) into the contraction term plus $V_b$, the collection of Itô second-order terms, and $V_b$ has exactly three pieces, bounded by (13), (15), (14) respectively:

1. **Zeroth derivative of $M$** (13): $\displaystyle\int_0^1\sum_{i,j}M_{ij}\Big(\tfrac{\partial B}{\partial\mu}\tfrac{\partial B}{\partial\mu}^T\Big)_{ij}d\mu\le\operatorname{tr}(M(a,t)B_1B_1^T)+\operatorname{tr}(M(b,t)B_2B_2^T)\le C_1+C_2$. Genuine noise intensity — this term is intrinsic-looking and survives any coordinate-free rewrite.
2. **First derivative $(M_i)_{x_j}$** (15): $\displaystyle\int_0^1 2\sum_{i,j}(M_i)_{x_j}\tfrac{\partial x}{\partial\mu}\big(B\tfrac{\partial B}{\partial\mu}^T\big)_{ij}d\mu\;\le\;2\bar m_x(\beta_1^2+\beta_2^2)\int_0^1\big\|\tfrac{\partial x}{\partial\mu}\big\|d\mu\;\le\;\bar m_x(\beta_1^2+\beta_2^2)\Big(\varepsilon\!\int_0^1\big\|\tfrac{\partial x}{\partial\mu}\big\|^2d\mu+\tfrac1\varepsilon\Big)$, using $2ab\le\varepsilon^{-1}a^2+\varepsilon b^2$.
3. **Second derivative $(M_{kl})_{x_ix_j}$** (14): $\displaystyle\tfrac12\int_0^1\sum_{i,j,k,l}(M_{kl})_{x_ix_j}\tfrac{\partial x_k}{\partial\mu}\tfrac{\partial x_l}{\partial\mu}(BB^T)_{ij}d\mu\;\le\;\tfrac12\bar m_{x^2}(\beta_1^2+\beta_2^2)\int_0^1\big\|\tfrac{\partial x}{\partial\mu}\big\|^2d\mu$.

Assumption 2's $m=\inf\lambda_{\min}M$ then converts $\int_0^1\|\partial x/\partial\mu\|^2d\mu\le V/m$, so the $\|\cdot\|^2$ pieces of (2) and (3) are *charged against the contraction rate* and the $1/\varepsilon$ piece of (2) is *charged against the residual constant*:

$$\mathcal LV\;\le\;\underbrace{-2\gamma V}_{\text{(3)}}\;+\;\underbrace{\frac{\varepsilon\bar m_x(\beta_1^2+\beta_2^2)}{m}V}_{\text{from (15)}}\;+\;\underbrace{\frac{\bar m_{x^2}(\beta_1^2+\beta_2^2)}{2m}V}_{\text{from (14)}}\;+\;\underbrace{\frac{\bar m_x(\beta_1^2+\beta_2^2)}{\varepsilon}}_{\text{from (15)}}\;+\;\underbrace{C_1+C_2}_{\text{from (13)}}$$

which is (16)–(17), $\mathcal LV\le-2\gamma_1V+C$. So, exactly:

- $\bar m_{x^2}$ enters **only** the rate, subtracting $\frac{(\beta_1^2+\beta_2^2)\bar m_{x^2}}{4m}$ from $\gamma$.
- $\bar m_x$ enters **twice**: subtracting $\frac{\varepsilon(\beta_1^2+\beta_2^2)\bar m_x}{2m}$ from $\gamma$, *and* adding $\frac{\bar m_x(\beta_1^2+\beta_2^2)}{\varepsilon}$ to $C$. No choice of $\varepsilon$ removes both.
- The asymptotic tube radius in (9) is therefore
$$\lim_{t\to\infty}\mathbb E\|a-b\|^2\;\le\;\frac{C}{2m\gamma_1}=\frac{C_1+C_2+\frac{\bar m_x}{\varepsilon}(\beta_1^2+\beta_2^2)}{2m\Big[\gamma-\frac{\beta_1^2+\beta_2^2}{2m}\big(\varepsilon\bar m_x+\frac{\bar m_{x^2}}{2}\big)\Big]} .$$
- The bound is **vacuous** whenever $(\beta_1^2+\beta_2^2)\big(\varepsilon\bar m_x+\bar m_{x^2}/2\big)\ge2m\gamma$: a metric whose components merely *vary fast enough in the chosen chart* destroys the contraction certificate outright, independently of the geometry.
- Theorem 2 reproduces the identical structure one level down, with $\bar p_x,\bar p_{x^2}$ (derivatives of $P^{-1}_{ij}$) in place of $\bar m_x,\bar m_{x^2}$ and $\underline p$ in place of $m$.

:::warning[Open question — what should replace $\bar m_x$ and $\bar m_{x^2}$]
$\bar m_x$ and $\bar m_{x^2}$ are componentwise sup-norms of $\partial g_{ij}$ and $\partial^2 g_{ij}$: not tensors, changeable by a change of chart, and vanishing identically in normal coordinates at a point. The intrinsic content of $\partial^2 g$ is **curvature**; the intrinsic content of $\partial g$ at a point is **nothing** (it can always be gauged away). So the target statement is a rate degradation controlled by a sectional/Ricci curvature bound (via Hessian comparison for $d(\cdot,\bar x)^2$, cf. the Itô-correction term $\tfrac12\operatorname{tr}\nabla^2 d^2$), together with an injectivity-radius condition to make $d^2$ smooth on the region of interest — and no first-derivative term at all. Whether the $\varepsilon$-splitting that produces $\bar m_x$ in *both* $\gamma_1$ and $C$ survives at all in the intrinsic version, or whether it is a pure artifact of bounding a cross term that has no coordinate-free counterpart, is the open question. Provisional read: the $\bar m_x$ cross term (15) couples $\partial M$ to $\partial B/\partial\mu$ and looks like a chart artifact of not using a metric-compatible connection; the $\bar m_{x^2}$ term (14) is the one with genuine curvature content.
:::

## What this gives the project

- **The template for bound type (a).** The proof skeleton — Itô on the path energy $V$, bound the three second-order terms, get $\mathcal LV\le-2\gamma_1V+C$, apply the Grönwall-type Lemma 3, divide by $m$ — is exactly the argument to be re-run intrinsically with $V=d(X_t,\bar x_t)^2$ and $\mathcal L$ the manifold generator.
- **Lemma 3 verbatim** is the comparison lemma to reuse; it is sharp enough (the $[\cdot]^+$ keeps the transient from ever inflating the steady-state term) and is manifold-agnostic.
- **The precise conservatism ledger** above is the "before" column for the thesis's central claim. Any intrinsic result should be compared against $C/(2m\gamma_1)$ with the $\bar m_x,\bar m_{x^2}$ terms exhibited.
- **Remark 1 is the cleanest statement of the gap**: with a state-independent metric the extra constants vanish entirely. The whole difficulty is that a genuinely curved / state-dependent metric is unavoidable on $SO(3)$, $SE(3)$ — so the Euclidean fix (use a constant metric) is not available and something intrinsic must take its place.
- **Remark 8 is the reason bound type (b) is separately needed**: the authors state explicitly that $V$ is *not* a supermartingale when noise does not vanish, so the supermartingale inequality cannot give almost-sure or $\sup_t$ statements. That is precisely the gap the AMGF/Doob route fills.
- $V$ is a **path** energy, not $d(a,b)^2$ — the connection to geodesic distance is only through $m\|a-b\|^2\le V$. Making this a genuine Riemannian distance bound is a step the paper never takes.

## Caveats / limitations

- **Global Lipschitz + linear growth** (7) on $f$ and $B$; state confined to a compact $D$ (Assumption 4) for the observer results.
- $M$ is assumed to satisfy (3) *globally in $x$ and $t$* with a single $\gamma$, and $\bar m_x,\bar m_{x^2}$ are *global* sups over $t$, $i$, $j$ — no localisation, no dependence on how far apart $a$ and $b$ are.
- The comparison in Lemma 2 is between two systems with the **same drift** driven by **independent** noises. Comparing a noisy trajectory to a deterministic nominal is a degenerate special case ($B_2=0$), not the stated setting.
- **Remark 8 (authors' own):** $V$ need not be a supermartingale, so no almost-sure stability, no $\sup_{t\le T}$ statement — only mean-squared.
- $V$ bounds the Euclidean distance $\|a-b\|$ via $m$, so the tube is measured in $\|\cdot\|$, not in the metric $M$; the ratio $\lambda_{\max}M/m$ is silently absorbed.
- Assumption 5 ($\underline p I\le P^{-1}\le\bar p I$) is *assumed*, justified only by a pointer (Remark 4) to uniform-observability results; the Shor relaxation of (64) drops rank-1 constraints, so the LMI is a relaxation and $\ell,\eta$ recovery is not exact.
- Constant recorded with a caveat: the optimal-$\varepsilon$ quadratic in §III.A (see the open-question callout above).
