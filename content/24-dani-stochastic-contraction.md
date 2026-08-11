---
tags: [stochastic-contraction, mean-squared-bound, chart-dependence, euclidean-template, track-a]
---
# Dani's Stochastic Contraction Lemma, and Where Its Conservatism Lives

**Prereq:** [[14-contraction-on-manifolds]] (contraction in a chosen metric, rate $\lambda$), [[20-generator-on-manifolds]] (the generator $\mathcal L$ is the invariant, the drift is not), [[23-martingale-toolkit]] (the Grönwall + Chebyshev route, and why it is not the Doob route), [[notation]].
**Goal:** state the Euclidean mean-squared template — track A of the study plan — exactly, and then trace, term by term, how two sup-norms of chart-metric derivatives get into both its decay rate and its asymptotic radius, to the point of destroying the certificate outright.

Everything here is [[@daniObserverDesignStochastic2015]] §III, converted to this repo's notation. This is **bound type (a)** only: $\mathbb E\|a(t)-b(t)\|^2\le\cdots$ at each fixed $t$. It says nothing about $\sup_{t\le T}$, and §"Remark 8" below explains that this is not an oversight.

## Setup

Two trajectories of the **same** drift driven by **independent** Wiener processes (eq. (8)), stacked as $z=(a^\top,b^\top)^\top\in\mathbb R^{2n}$:

$$da = f(a,t)\,dt + B_1(a,t)\,d\bar W_1,\qquad db = f(b,t)\,dt + B_2(b,t)\,d\bar W_2 .$$

Comparing a noisy trajectory to a deterministic nominal is the degenerate case $B_2=0$, not the stated setting. Global Lipschitz and linear growth are imposed on $f,B$ (eq. (7)).

:::info[Definition — generalised squared length]
Fix a symmetric, uniformly positive-definite $M(x,t)$ and a path $\mu\mapsto x(\mu,t)$ with $x(0,t)=a(t)$, $x(1,t)=b(t)$. Then

$$V(x,\delta x,t)=\int_0^1\Big(\frac{\partial x}{\partial\mu}\Big)^{\!\top}M\big(x(\mu,t),t\big)\Big(\frac{\partial x}{\partial\mu}\Big)\,d\mu ,\qquad m\|a-b\|^2\le V .$$
:::

**$\mu\in[0,1]$ parametrises a path between the two trajectories, so $V$ is a path *energy*, not a geodesic distance.** No minimisation over paths is performed anywhere in the proof; the connection to distance is only through the one-sided $m\|a-b\|^2\le V$. Replacing $V$ by $d(a,b)^2$ — at which point the second variation of arc length, not $\partial^2M_{ij}$, supplies the curvature — is lesson 25's job.

:::info[Assumption 1]
There are constants $C_1,C_2,\bar m_x,\bar m_{x^2}$ with
$$\operatorname{tr}\!\big(B_1^\top M(x(a,t),t)B_1\big)\le C_1,\qquad \operatorname{tr}\!\big(B_2^\top M(x(b,t),t)B_2\big)\le C_2,$$
$$\bar m_x=\sup_{t\ge0,\,i,j}\big\|\partial M_{ij}(x,t)/\partial x\big\| ,\qquad \bar m_{x^2}=\sup_{t\ge0,\,i,j}\big\|\partial^2 M_{ij}(x,t)/\partial x^2\big\| .$$
Write $\beta_1=\|B_1\|_F$, $\beta_2=\|B_2\|_F$.
:::

The first line is a genuine noise-intensity bound. The second line is two **componentwise sup-norms of derivatives of the metric in the chosen chart** — category 3 in the sense of [content/CLAUDE.md](CLAUDE.md): chart-dependent and load-bearing.

:::info[Assumption 2]
The nominal deterministic system $\dot x=f(x,t)$ is contracting in $M$ with rate $\gamma>0$, i.e. $\big(\partial f/\partial x\big)^\top M+\dot M+M\big(\partial f/\partial x\big)\le-2\gamma M$ for all $x,t$; and $m\triangleq\inf_{t\ge0}\lambda_{\min}M>0$.
:::

:::tip[Lemma 2 — Stochastic Contraction Lemma]
Under Assumptions 1–2, with $(a_0,b_0)$ independent of the driving noises, for **some** $\varepsilon>0$,

$$\mathbb E\big[\|a(t)-b(t)\|^2\big]\;\le\;\frac1m\Big(\frac{C}{2\gamma_1}+\mathbb E\big[V(0)\big]\,e^{-2\gamma_1 t}\Big),$$

$$\gamma_1=\gamma-\frac{\beta_1^2+\beta_2^2}{2m}\Big(\varepsilon\,\bar m_x+\frac{\bar m_{x^2}}{2}\Big)>0,\qquad C=C_1+C_2+\frac{\bar m_x}{\varepsilon}\big(\beta_1^2+\beta_2^2\big).$$

Proof: Itô/Dynkin on $V$; bound the three second-order terms; get $\mathcal LV\le-2\gamma_1V+C$; apply the Grönwall-type comparison lemma of [[23-martingale-toolkit]]; divide by $m$.
:::

The rest of the paper — Theorems 1–2 and Corollary 1 — designs a specific observer whose metric is $P^{-1}$ for an SDARE solution $P$, synthesised by an LMI; it reproduces Lemma 2's structure one level down with $\bar p_x,\bar p_{x^2}$ in place of $\bar m_x,\bar m_{x^2}$, and is not the transferable part.

## The conservatism trace

$\mathcal LV$ splits into the contraction term $-2\gamma V$ plus exactly three Itô second-order terms, bounded separately ([[@daniObserverDesignStochastic2015]] eqs. (13)–(15)):

| term | what it contains | bound |
|---|---|---|
| (13) | $M_{ij}$, **no derivative** | $\le C_1+C_2$ |
| (15) | $\partial M_{ij}/\partial x_k$ — a cross term $M'\cdot\tfrac{\partial x}{\partial\mu}\cdot B\tfrac{\partial B}{\partial\mu}^{\!\top}$ | $\le\bar m_x(\beta_1^2+\beta_2^2)\big(\varepsilon\!\int_0^1\|\tfrac{\partial x}{\partial\mu}\|^2d\mu+\tfrac1\varepsilon\big)$, by $2ab\le\varepsilon a^2+\varepsilon^{-1}b^2$ |
| (14) | $\partial^2M_{kl}/\partial x_i\partial x_j$ | $\le\tfrac12\bar m_{x^2}(\beta_1^2+\beta_2^2)\int_0^1\|\tfrac{\partial x}{\partial\mu}\|^2d\mu$ |

Only (13) is genuine noise intensity; it survives any coordinate-free rewrite. Now Assumption 2 converts $\int_0^1\|\partial x/\partial\mu\|^2d\mu\le V/m$, and the $\|\cdot\|^2$ pieces become *rate* charges while the loose $1/\varepsilon$ becomes a *constant* charge:

$$\mathcal LV\;\le\;\underbrace{-2\gamma V}_{\text{Assn. 2}}+\underbrace{\frac{\varepsilon\bar m_x(\beta_1^2+\beta_2^2)}{m}V}_{(15)}+\underbrace{\frac{\bar m_{x^2}(\beta_1^2+\beta_2^2)}{2m}V}_{(14)}+\underbrace{\frac{\bar m_x(\beta_1^2+\beta_2^2)}{\varepsilon}}_{(15)}+\underbrace{C_1+C_2}_{(13)} .$$

**The asymmetry.** $\bar m_{x^2}$ hits **only the rate**, subtracting $\tfrac{(\beta_1^2+\beta_2^2)\bar m_{x^2}}{4m}$ from $\gamma$. $\bar m_x$ hits **both** — subtracting $\tfrac{\varepsilon(\beta_1^2+\beta_2^2)\bar m_x}{2m}$ from $\gamma$ *and* adding $\tfrac{\bar m_x(\beta_1^2+\beta_2^2)}{\varepsilon}$ to $C$. Since $\varepsilon$ appears once in the numerator and once in the denominator, **no choice of $\varepsilon$ kills both**; the free parameter only trades one against the other. The asymptotic radius is

$$\lim_{t\to\infty}\mathbb E\|a-b\|^2\;\le\;\frac{C}{2m\gamma_1}=\frac{C_1+C_2+\tfrac{\bar m_x}{\varepsilon}(\beta_1^2+\beta_2^2)}{2m\Big[\gamma-\tfrac{\beta_1^2+\beta_2^2}{2m}\big(\varepsilon\bar m_x+\tfrac{\bar m_{x^2}}{2}\big)\Big]} .$$

:::warning[The bound goes vacuous]
There is **no** admissible $\varepsilon$ — hence no statement at all — once
$$\big(\beta_1^2+\beta_2^2\big)\Big(\varepsilon\,\bar m_x+\frac{\bar m_{x^2}}{2}\Big)\;\ge\;2m\gamma ,$$
and letting $\varepsilon\downarrow0$ shows the $\bar m_{x^2}$ half alone suffices: $(\beta_1^2+\beta_2^2)\bar m_{x^2}\ge4m\gamma$ kills the certificate. Nothing about the system, the noise, or the geometry has to change — only how fast the metric's *components* vary in the chart being used.
:::

**Remark 1** is the cleanest statement of the gap: with $M=M(t)$ or $M$ constant, the $\partial M$ and $\partial^2M$ terms in the generator vanish identically and Lemma 2 collapses to [[@phamContractionTheoryApproach2008]]'s bound. So $\bar m_x,\bar m_{x^2}$ are *exactly* the price of state-dependence — and on $SO(3)$ or $SE(3)$ the Euclidean escape hatch (just use a constant metric) does not exist.

### Remark 8 — why track B is not a refinement of track A

The authors state that $V$ is **not** a supermartingale when the noise does not vanish: $\mathcal LV\le-2\gamma_1V+C$ has a strictly positive $C$, so $\mathcal LV\le0$ fails on the sublevel set $\{V<C/2\gamma_1\}$, exactly where the interesting behaviour is. Consequently the supermartingale inequality cannot be applied, and **no almost-sure statement and no $\sup_{t\le T}$ statement is reachable by this route** — only mean-squared, at each fixed $t$.

This is the textual justification for the two-route split in [[23-martingale-toolkit]]. Track A ends here; getting $\mathbb P[\sup_{t\le T}d\le r]$ requires a nonnegative object whose drift inequality is *affine* rather than merely dissipative, plus Doob — which is track B. Feeding Lemma 2 into Chebyshev gives a probability at one $t$ and then a union bound over a time grid, which is precisely the lossy step track B exists to avoid.

## Worked example — two charts, one system, two different certificates

Take $z=(x_1,x_2)^\top\in\mathbb R^2$ and the system

$$dx_1=-\gamma x_1\,dt+\sigma\,dW,\qquad dx_2=-\gamma x_2\,dt ,$$

so the noise lives entirely in the $x_1$ direction and $x_2$ is noise-free.

**Chart 1**, coordinates $x$, metric $M^{(1)}=I_2$. Then $(\partial f/\partial x)^\top M+M(\partial f/\partial x)=-2\gamma I=-2\gamma M$, so Assumption 2 holds with exactly $\gamma$ and $m=1$; $\bar m_x=\bar m_{x^2}=0$; $\beta_1=\beta_2=\sigma$; $C_1=C_2=\sigma^2$. Lemma 2 gives $\gamma_1=\gamma$, $C=2\sigma^2$, asymptotic radius $\sigma^2/\gamma$.

**Chart 2**, coordinates $y$ defined by $y_1=x_1$ and $x_2=\psi(y_2)\triangleq y_2+\tfrac a\omega\sin(\omega y_2)$ with $0<a<1$, so $\psi'=1+a\cos\omega y_2\in[1-a,1+a]$ and $\psi$ is a global diffeomorphism of $\mathbb R$. Because the noise has no $x_2$-component and $y_1=x_1$, **the Itô correction vanishes** — the SDE in $y$ has drift $\big(-\gamma y_1,\;-\gamma\psi(y_2)/\psi'(y_2)\big)$ and the same $B=(\sigma,0)^\top$. Push $M^{(1)}$ forward:

$$M^{(2)}(y)=\operatorname{diag}\big(1,\;(1+a\cos\omega y_2)^2\big) .$$

This is the *same Riemannian metric*, so the contraction condition — which is the tensorial statement $\mathcal L_fM\preceq-2\gamma M$ — still holds with the *same* $\gamma$. And $\beta_1=\beta_2=\sigma$, $C_1=C_2=\sigma^2$ are unchanged too, since $M^{(2)}_{11}=1$. But

$$m=(1-a)^2,\qquad \bar m_x\ \ge\ \big|\partial_{y_2}M^{(2)}_{22}\big|_{\omega y_2=\pi/2}=2a\omega,\qquad \bar m_{x^2}\ \ge\ \big|\partial^2_{y_2}M^{(2)}_{22}\big|_{y_2=0}=2a\omega^2(1+a).$$

Take $\gamma=\sigma=1$, $a=\tfrac12$, $\omega=2$: then $m=\tfrac14$, $\bar m_x\ge2$, $\bar m_{x^2}\ge6$, $\beta_1^2+\beta_2^2=2$, and

$$\gamma_1\;\le\;1-\frac{2}{2\cdot\frac14}\Big(2\varepsilon+3\Big)\;=\;-11-8\varepsilon\;<\;0\qquad\text{for every }\varepsilon>0 .$$

**Chart 1 certifies rate $1$; chart 2 certifies nothing at all.** Every intrinsic quantity is identical in the two descriptions — both are flat, $\mathrm{Sec}\equiv0$, $\mathrm{inj}=\infty$, $V$ itself is chart-independent (it is $\int_0^1\|\dot c\|_g^2$), and $y\mapsto x$ is an isometry. Only $\bar m_x,\bar m_{x^2}$ and $m$ moved, and only $\bar m_x,\bar m_{x^2}$ moved *without bound*: they scale like $a\omega$ and $a\omega^2$ while $\gamma,\beta_i,C_i$ do not depend on $\omega$ at all.

:::warning[Open question — what lesson 25 has to replace]
The target is to run this same skeleton with $V=d(X_t,\bar x_t)^2$ and the manifold generator of [[20-generator-on-manifolds]], and have the three constants come out as: a **sectional/Ricci curvature bound** in place of $\bar m_{x^2}$, an **injectivity radius** condition making $d^2$ smooth on the tube, and the **Hessian-comparison constant** those two produce — all from [[08-hessian-comparison]].

The sharpened claim from [[08-hessian-comparison]] is that $\bar m_x$ has **no intrinsic counterpart at all**: normal coordinates give $\partial_kg_{ij}(p)=0$ at any chosen $p$, so a first-derivative bound on the metric is a pure chart artifact and can always be gauged away pointwise. If that is right, the entire $\varepsilon$-splitting — the one degree of freedom Lemma 2 offers, and the reason $\bar m_x$ pollutes both $\gamma_1$ and $C$ — is an artifact of bounding a cross term (15) that has no coordinate-free existence, and should simply be absent. Provisional read: (15) couples $\partial M$ to $\partial B/\partial\mu$ because the derivative taken is not metric-compatible; (14) is the term with genuine curvature content. Whether the intrinsic constant is actually *tighter* — not merely chart-independent — is lesson 29's question, not settled here.
:::

## Problems

1. **Recall.** Without looking: state Assumptions 1 and 2 in full and write down Lemma 2 with both $\gamma_1$ and $C$. Then classify each of $C_1,C_2,\beta_1,\beta_2,m,\gamma,\bar m_x,\bar m_{x^2}$ as intrinsic, chart-dependent-but-harmless, or chart-dependent-and-load-bearing.

2. **Compute.** Take $M(x)=\big(2+\sin(\omega x_1)\big)I_2$ on $\mathbb R^2$, with $\gamma=1$, $\beta_1^2+\beta_2^2=1$, $C_1+C_2=1$. (a) Give $m,\bar m_x,\bar m_{x^2}$. (b) Find the largest $\omega$ for which *some* $\varepsilon>0$ makes $\gamma_1>0$. (c) At $\omega=1$, minimise $F(\varepsilon)=C/(2m\gamma_1)$ over $\varepsilon$ and compare with the radius $\big(C_1+C_2\big)/(2m\gamma)$ that a constant metric would give.

3. **Prove.** Show that if $M$ does not depend on $x$ (constant, or $M=M(t)$) then $\bar m_x=\bar m_{x^2}=0$, and deduce that Lemma 2 becomes $\mathbb E\|a-b\|^2\le\frac1m\big(\frac{C_1+C_2}{2\gamma}+\mathbb E[V(0)]e^{-2\gamma t}\big)$ with no $\varepsilon$ anywhere. Then show the converse direction of the vacuousness threshold is never triggered in this case, i.e. Assumption 2 alone certifies the bound.

4. **Break it.** Using the worked example's two charts: (a) list which of $\gamma,\ \beta_1,\ C_1,\ m,\ \bar m_x,\ \bar m_{x^2}$ depend on $\omega$, and show $\sup_\omega$ of the certified rate ratio between the charts is $+\infty$. (b) Verify directly that $V$ takes the same value on corresponding paths in the two charts, and that the Riemannian distance between $a$ and $b$ is the same — so nothing being *bounded* changed. (c) Exhibit a third chart in which the certified rate is again exactly $\gamma$, and conclude in one sentence what the quality of Lemma 2's bound is actually a property of.

---

## Solutions

**1.** Statements as above. Classification: $\gamma$ is **intrinsic** — the contraction condition is $\mathcal L_fM\preceq-2\gamma M$, an inequality between two symmetric $(0,2)$-tensors, so $\gamma$ is unchanged by any diffeomorphism. $C_1,C_2$ are intrinsic: $\operatorname{tr}(B^\top MB)$ is the squared $M$-norm of the noise vector fields, a scalar. $\beta_1,\beta_2=\|B\|_F$ are **chart-dependent** (they use the Euclidean, not the $M$-, norm) but appear only as an overall multiplier and stay bounded under any bi-Lipschitz change. $m=\inf\lambda_{\min}M$ compares $M$ to the chart's Euclidean structure — chart-dependent, but so is the $\|a-b\|^2$ on the left, so its appearance is at least consistent. $\bar m_x,\bar m_{x^2}$ are **category 3**: componentwise sup-norms of $\partial g$ and $\partial^2g$, not tensors, and both zero at a point in normal coordinates.

**2.** (a) $2+\sin\ge1$ so $m=1$; $\partial_{x_1}M_{ii}=\omega\cos\omega x_1$ gives $\bar m_x=\omega$; $\partial^2_{x_1}M_{ii}=-\omega^2\sin\omega x_1$ gives $\bar m_{x^2}=\omega^2$.
(b) $\gamma_1=1-\tfrac12\big(\varepsilon\omega+\tfrac{\omega^2}{2}\big)$. Taking $\varepsilon\downarrow0$, $\sup_\varepsilon\gamma_1=1-\omega^2/4$, so $\gamma_1>0$ is achievable iff $\omega<2$. (Note $\varepsilon=0$ is not admissible — the constant $C$ blows up — so the supremum is not attained; $\omega<2$ is the open condition.)
(c) At $\omega=1$: $\gamma_1=\tfrac34-\tfrac\varepsilon2$, $C=1+\tfrac1\varepsilon$, so $F(\varepsilon)=\dfrac{2(\varepsilon+1)}{\varepsilon(3-2\varepsilon)}$ on $(0,\tfrac32)$. Setting the numerator of $F'$ to zero: $2\varepsilon^2+4\varepsilon-3=0$, so $\varepsilon^\star=\tfrac{-2+\sqrt{10}}{2}\approx0.581$ and $F(\varepsilon^\star)\approx2.96$. A constant metric with the same $\gamma,m,C_1+C_2$ gives $1/(2\cdot1\cdot1)=0.5$. So the chart-metric variation inflates the certified asymptotic radius by a factor $\approx6$ — and, per part (b), by $\infty$ once $\omega\ge2$.

**3.** If $M_{ij}$ has no $x$-dependence then every $\partial M_{ij}/\partial x$ and $\partial^2M_{ij}/\partial x^2$ is identically zero, so the sups defining $\bar m_x,\bar m_{x^2}$ are $0$. Substituting: $\gamma_1=\gamma-\tfrac{\beta_1^2+\beta_2^2}{2m}(\varepsilon\cdot0+0)=\gamma$ and $C=C_1+C_2+\tfrac0\varepsilon(\beta_1^2+\beta_2^2)=C_1+C_2$, both independent of $\varepsilon$, which therefore drops out of the statement. This is exactly [[@phamContractionTheoryApproach2008]]'s bound. The vacuousness condition reads $(\beta_1^2+\beta_2^2)(\varepsilon\cdot0+0)\ge2m\gamma$, i.e. $0\ge2m\gamma$, which is false whenever $m>0$ and $\gamma>0$ — precisely Assumption 2. So under Assumption 2 the certificate always exists, with no side condition on the noise magnitude. Every obstruction in Lemma 2 beyond Assumption 2 is contributed by state-dependence of $M$.

**4.** (a) $\gamma$ (tensorial), $\beta_1=\sigma$ and $C_1=\sigma^2$ (the noise sits in $y_1=x_1$, where $M^{(2)}_{11}=1$) are all $\omega$-independent; $m=(1-a)^2$ depends on $a$ but not $\omega$; only $\bar m_x\asymp2a\omega$ and $\bar m_{x^2}\asymp2a(1+a)\omega^2$ grow. Chart 1 certifies $\gamma_1=\gamma$ for every $\omega$; chart 2 certifies $\gamma_1\le\gamma-\tfrac{a(1+a)\omega^2(\beta_1^2+\beta_2^2)}{2m}$, which is $<0$ for $\omega$ large, so the ratio of certified rates is unbounded and eventually meaningless (no certificate exists).
(b) $V=\int_0^1(\partial_\mu x)^\top M^{(1)}(\partial_\mu x)d\mu$ and its $y$-version are the same integral: $\partial_\mu y=(D\Psi)\partial_\mu x$ and $M^{(2)}=(D\Psi)^{-\top}M^{(1)}(D\Psi)^{-1}$, so the integrands agree pointwise in $\mu$. Likewise $d(a,b)=\inf_c\int\|\dot c\|_g$ is a metric-space quantity and the coordinate change is an isometry, so it is identical. (What *does* differ is the Euclidean $\|a-b\|$ on the left of Lemma 2 — which is why the honest comparison is between rates, and the rate comparison already fails.)
(c) Chart 1 itself qualifies; so does any chart differing from it by a Euclidean isometry, or more generally by $\psi$ with $\psi'\equiv$ const. In all of these $M\equiv$ const, hence $\bar m_x=\bar m_{x^2}=0$ and $\gamma_1=\gamma$ by Problem 3. **Conclusion: the quality of Lemma 2's bound is a property of the chart, not of the system, the noise, or the geometry** — which is the definition of a category-3 constant and the whole reason lessons 25 and 28 exist.
