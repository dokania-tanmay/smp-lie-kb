---
tags: [contraction, riemannian-geometry, incremental-stability, coordinate-free, reference]
---
# Contraction theory on Riemannian manifolds (Simpson-Porco & Bullo, Systems & Control Letters 65, 2014)

The paper that puts contraction theory on an intrinsic footing: a contracting system is a quadruple $(\mathcal U, X, G, \lambda)$ satisfying one covariant-derivative inequality, and the main theorem turns that inequality into an exponential bound on Riemannian distance between any two trajectories. For this project it supplies the *nominal-trajectory* half of a tube: the contraction metric $G$ is the same species of object as the metric in which a tube radius is measured, and the paper's proof technique — differentiate $\|S\|_G^2$ along the flow using only metric compatibility of the Levi-Civita connection, never computing Christoffel symbols — is exactly the manipulation an intrinsic AMGF energy function will need. It is also a clean example of a bound whose constants ($\lambda$, $K$) are *not* chart-dependent, in contrast to [[@daniObserverDesignStochastic2015]].

**Which PDF.** Written from `refs/@simpson-porcoContractionTheoryRiemannian2014.pdf` — the published Elsevier version, *Systems & Control Letters* **65** (2014) 74–80, 7 pages, doi `10.1016/j.sysconle.2013.12.016`. The other file, `…2014a.pdf`, is the 9-page submitted preprint (June 2013, two-column Elsevier `elsarticle` style). The two are the same paper with **identical numbering** of every definition, theorem, proposition, lemma, corollary, example and equation used below; the published version adds a few references (cascade interconnections [5,6], mechanical-system controllers [32]), renumbers the bibliography, and names the appendix lemma `Lemma A.1` where the preprint calls it `Lemma 1`. Nothing cited by `refs/claude-gen-import/contraction-mech-RG.tex` as `[SB13]` moved.

## Notation

| Symbol | Meaning |
|---|---|
| $M$ | smooth manifold, $\dim M = n$; all objects smooth |
| $\Gamma^\infty(TM)$ | smooth vector fields; $X \in \Gamma^\infty(TM)$ is the system vector field |
| $\Phi_t(x)$ | flow of $X$; $t\mapsto\Phi_t(x)$ is the *maximal* integral curve through $x$ |
| $G$ | Riemannian metric (the **contraction metric**), $G = G_{ij}\,dx^i\otimes dx^j$ |
| $\langle\!\langle\cdot,\cdot\rangle\!\rangle_{G(x)}$, $\|\cdot\|_{G(x)}$ | inner product and norm induced by $G$ at $x$ |
| $\overset{G}{\nabla}$ | Levi-Civita connection of $G$; $\overset{G}{\nabla}_{v_x}X$ is the covariant derivative of $X$ along $v_x$ |
| $\Gamma^k_{ij}$ | Christoffel symbols of $\overset{G}{\nabla}$, eq. (1) |
| $G^\flat, G^\sharp$ | musical isomorphisms $T_xM \leftrightarrow T^*_xM$ |
| $\mathcal L_X G$ | Lie derivative of the metric, defined as $G^\flat(\overset{G}{\nabla}X)$ |
| $\ell_G(\gamma)$ | arclength $\int_J \sqrt{\langle\!\langle\gamma',\gamma'\rangle\!\rangle_{G(\gamma(t))}}\,dt$ |
| $d_G(x_1,x_2)$ | Riemannian distance, $\inf\{\ell_G(\gamma)\}$ over piecewise-smooth $\gamma\in\Omega(x_1,x_2)$ |
| $B_r(\bar x)$ | closed $r$-ball $\{x : d_G(x,\bar x)\le r\}$ |
| $\mathcal U$ | contraction region, a **connected** subset of $M$ |
| $\lambda>0$, $K\ge1$ | contraction rate; reachability constant |
| $\omega$ | canonical volume form of $(M,G)$; $\mathcal L_X\omega = \operatorname{div}(X)\,\omega$ |
| $S(s,t), T(s,t)$ | $\partial_s\Phi_t(\gamma(s))$ (transverse/variation field) and $\partial_t\Phi_t(\gamma(s))$ (velocity field) |
| $A\preccurlyeq B$ | for symmetric $(0,2)$-tensors: $B-A$ positive definite (footnote 1) |

## Key definitions

:::info[Definition — contracting system, Def. 2.1]

A **contracting system** is a quadruple $(\mathcal U, X, G, \lambda)$ where

- $\mathcal U\subset M$ is a **connected** set (the *contraction region*),
- $X\in\Gamma^\infty(TM)$ is a vector field,
- $G$ is a Riemannian metric (the *contraction metric*),
- $\lambda>0$ is the *contraction rate*,

such that **for each $x\in\mathcal U$ and each $v_x\in T_xM$**
$$\big\langle\!\big\langle \overset{G}{\nabla}_{v_x} X,\; v_x \big\rangle\!\big\rangle_{G(x)} \;\le\; -\lambda\,\|v_x\|^2_{G(x)}. \tag{4}$$
$X$ is then said to be *infinitesimally contracting on $\mathcal U$ with respect to $G$*.

Note the quantifier structure: the base point ranges over $\mathcal U$ only, but $v_x$ ranges over **all** of $T_xM$ (not a subspace, not unit vectors only — though homogeneity makes unit vectors equivalent). $X$ and $G$ are defined on all of $M$; only the inequality is localised to $\mathcal U$.
:::

Equivalent form stated immediately after Def. 2.1: $\langle\!\langle v_x,v_x\rangle\!\rangle_{\mathcal L_X G(x)} \le -2\lambda\|v_x\|^2_{G(x)}$ — i.e. $\mathcal L_X G \preccurlyeq -2\lambda G$. The paper prefers form (4).

:::info[Definition — $K$-reachable set, Def. 2.2]

Let $(M,G)$ be a Riemannian manifold. For $K\ge 1$, a set $\mathcal U\subseteq M$ is **$K$-reachable** if for **any** two points $x_0,x_1\in\mathcal U$ there exists a **continuously differentiable** curve $\gamma:[0,1]\to\mathcal U$ with $\gamma(0)=x_0$, $\gamma(1)=x_1$, and
$$\ell_G(\gamma)\;\le\;K\,d_G(x_0,x_1).$$
:::

Three things are easy to get wrong here: (i) the curve must stay **inside $\mathcal U$**; (ii) it must be $C^1$, not merely piecewise smooth (the distance $d_G$ itself is defined via piecewise-smooth curves, so the constant $K$ absorbs both the detour and the smoothing); (iii) $d_G$ is the distance in $(M,G)$, *not* the intrinsic distance of $\mathcal U$. The paper's stated purpose for this definition: it weakens the requirement that the contraction region be **geodesically convex** (cf. Kobayashi–Nomizu Thm 4.1, cited as [38]) in exchange for a weaker convergence estimate; in $\mathbb R^n$ it relaxes convexity of the contraction region. Geodesically convex $\Rightarrow$ $1$-reachable.

## Main results

:::tip[Theorem — contraction theorem, Thm. 2.3]

Let $M$ be a manifold, $X\in\Gamma^\infty(TM)$ with flow $\Phi_t$. Suppose there exist a Riemannian metric $G$, constants $\lambda, K>0$, and a set $\mathcal U\subseteq M$ such that

1. $(\mathcal U,X,G,\lambda)$ is a contracting system (Def. 2.1),
2. $\mathcal U$ is a $K$-reachable, **forward $X$-invariant** set, and
3. $X$ is **forward complete** on $\mathcal U$.

Then for each pair $x_0,x_1\in\mathcal U$ and each $t\ge0$,
$$d_G(\Phi_t(x_0),\Phi_t(x_1)) \;\le\; K e^{-\lambda t}\, d_G(x_0,x_1). \tag{5}$$
:::

Proof technique (worth keeping, it is the reusable part). Take the $K$-reachable curve $\gamma$ joining $x_0,x_1$ and let $L(t)=\int_0^1\|\partial_s\Phi_t(\gamma(s))\|_{G}\,ds$ (eq. 6). With $S=\partial_s\Phi_t(\gamma(s))$, $T=\partial_t\Phi_t(\gamma(s))$, the key chain is eq. (8):
$$\frac{d}{dt}\|S(s,t)\|_G^2 = 2\big\langle\!\big\langle\overset{G}{\nabla}_{T}S,\,S\big\rangle\!\big\rangle_G = 2\big\langle\!\big\langle\overset{G}{\nabla}_{S}T,\,S\big\rangle\!\big\rangle_G = 2\big\langle\!\big\langle\overset{G}{\nabla}_{S}X(\Phi_t(\gamma(s))),\,S\big\rangle\!\big\rangle_G \le -2\lambda\langle\!\langle S,S\rangle\!\rangle_G .$$
Equality 1 is metric compatibility (eq. 2); equality 2 is symmetry of the Levi-Civita connection together with $[\tilde S,\tilde T]=0$ (Lemma A.1, proved by equality of mixed partials); equality 3 is $T=X\circ\Phi$; the inequality is Def. 2.1 plus forward invariance of $\mathcal U$. Substituting into $\dot L$ (eq. 7) gives $\dot L\le-\lambda L$, then Bellman–Grönwall, then $d_G(\Phi_t x_0,\Phi_t x_1)\le L(t)$ and $L(0)\le K d_G(x_0,x_1)$. **No Christoffel symbols are ever computed** — the whole argument runs on the two defining properties of $\overset{G}{\nabla}$.

:::tip[Proposition — coordinate description of contraction, Prop. 2.4]

The following are equivalent: (i) the contraction condition (4) holds; (ii) for every $x\in\mathcal U$ and in **every** set of admissible coordinates $(x^1,\dots,x^n)$ on a neighbourhood $V$ of $x$,
$$\Big[\,G_{ki}\frac{\partial X^k}{\partial x^\ell} + \frac{\partial X^k}{\partial x^i}G_{k\ell} + \frac{\partial G_{i\ell}}{\partial x^j}X^j\,\Big] \;\preccurlyeq\; -2\lambda\,[G_{i\ell}]. \tag{9}$$
:::

The bracketed matrix is exactly $(\mathcal L_XG)_{i\ell}$. Eq. (9) is called the *generalized Demidovich condition*; with $M=\mathbb R^n$ and $G$ Euclidean it reduces to Krasovskii's condition that the symmetric part of the Jacobian be negative definite. The unsymmetrised intermediate step is eq. (10): $\big(G_{k\ell}\tfrac{\partial X^k}{\partial x^i} + G_{k\ell}\Gamma^k_{ij}X^j\big)v^iv^\ell \le -\lambda G_{i\ell}v^iv^\ell$.

:::tip[Proposition — properties of contracting systems, Prop. 2.5]

Let $(\mathcal U,X,G,\lambda)$ be a contracting system. Then:

**(i) Existence of a stable fixed point.** If $(\mathcal U,d_G)$ is a **complete metric space**, $X$ is forward complete, and $\mathcal U$ is a forward $X$-invariant **$K$-reachable** set, then $X$ has a unique fixed point $\bar x\in\mathcal U$, and for each $x\in\mathcal U$, $\Phi_t(x)\to\bar x$ exponentially fast as $t\to+\infty$. *(Proof: pick $\tau$ with $Ke^{-\lambda\tau}<1$, so $\Phi_\tau$ is a contraction mapping; Banach fixed point theorem.)*

**(ii) Krasovskii's method.** If (i) holds, then $V(x)\triangleq\|X(x)\|^2_{G(x)}$ is a strict Lyapunov function for $\bar x$. *(Apply (4) with $v_x=X(x)$: $\mathcal L_XV\le-2\lambda V$.)*

**(iii) Incremental Lyapunov function.** If (i) holds, then $x\mapsto d_G(x,\bar x)$ serves **locally** as a strict Lyapunov function for $\bar x$. Moreover, for any $r>0$ with $B_r(\bar x)\subset\mathcal U$, the system $(B_r(\bar x),X,G,\lambda)$ is contracting and the ball $B_r(\bar x)$ is forward $X$-invariant and **$1$-reachable** (geodesic balls are strongly convex).

**(iv) Contraction of volume.** For any $r>0$ and $x\in\mathcal U$ with $B_r(x)\subset\mathcal U$, $\operatorname{Vol}(\Phi_t(B_r(x)))\to0$ exponentially fast. *(Via $\tfrac{d}{dt}\operatorname{Vol} = \int\operatorname{div}X\,\omega$ and $\operatorname{div}X\le-n\lambda$ from (10).)*
:::

Remark following Prop. 2.5: the fixed point is unique **in $\mathcal U$** but need not be the only fixed point of $X$ on $M$. Moreover **the contraction region is contractible** — after a reparameterization of time, $\mathrm{id}:x\mapsto x$ is homotopic to the constant map $x\mapsto\bar x$ — and consequently **there are no globally contracting vector fields on compact manifolds**, citing Bhat & Bernstein's topological-obstruction paper [41]. This is the obstruction that bites on $SO(3)$ and any compact Lie group.

:::tip[Lemma — interconnections, Lem. 3.1 / Lem. 3.2]

$(\mathcal U,X,G,\lambda,\mathbb R^k)$ is a *contracting system with inputs* if $(\mathcal U,X(\cdot,u),G,\lambda)$ is contracting **for every** $u\in\mathbb R^k$ (uniform in $u$).

**Lem. 3.1 (cascade).** Cascade of a contracting $(\mathcal U_1,X_1,G_1,\lambda_1)$ with smooth output $h_1$ into a contracting-with-inputs $(\mathcal U_2,X_2,G_2,\lambda_2,\mathbb R^k)$, with $\mathcal U_1,\mathcal U_2$ **compact**: there exists a metric $G$ on $M_1\times M_2$ making the closed loop contracting on $\mathcal U_1\times\mathcal U_2$. *(Proof omitted in the paper.)*

**Lem. 3.2 (feedback, small gain).** Two contracting systems with inputs $(\mathcal U_i,X_i,G_i,\lambda_i,\mathbb R^{k_i})$ with outputs $h_i:M_i\to\mathbb R^{k_{(3-i)}}$, $\mathcal U_1,\mathcal U_2$ **compact**, with induced input–output gains defined by eq. (11) (as printed, including a factor $\tfrac12$):
$$\gamma_1 \triangleq \max_{x_1\in\mathcal U_1}\max_{w_{x_2}\in T\mathcal U_2} \tfrac12\frac{\big\|\tfrac{\partial X_1}{\partial u_1}\circ(Th_2)w_{x_2}\big\|_{G_1}}{\|w_{x_2}\|_{G_2}}<\infty,\qquad \gamma_2 \triangleq \max_{x_2\in\mathcal U_2}\max_{v_{x_1}\in T\mathcal U_1} \tfrac12\frac{\big\|\tfrac{\partial X_2}{\partial u_2}\circ(Th_1)v_{x_1}\big\|_{G_2}}{\|v_{x_1}\|_{G_1}}<\infty.$$
If $\gamma_1\gamma_2<\lambda_1\lambda_2$ (eq. 12) then a **block-diagonal** metric $\langle\!\langle v_x,v_x'\rangle\!\rangle_G=\alpha_1\langle\!\langle\cdot\rangle\!\rangle_{G_1}+\alpha_2\langle\!\langle\cdot\rangle\!\rangle_{G_2}$ with $\alpha_1/\alpha_2=z^*=\gamma_2/\gamma_1$ makes the closed loop contracting on $\mathcal U_1\times\mathcal U_2$. The intermediate positive-definiteness condition is eq. (13): $\lambda_1\lambda_2-\gamma_1\gamma_2/2>(z\gamma_1^2+\gamma_2^2/z)/4$, whose RHS is convex in $z>0$ with minimum $\gamma_1\gamma_2/2$ at $z^*$.
:::

:::tip[Resolved — the eq. (11) $\tfrac12$ was an extraction artifact]

**Closed by [[18-hierarchical-contraction]].** Deriving the two-block interconnection condition from scratch reproduces the source's eq. (13) exactly, with **no** $\tfrac12$ in the gain definition: minimising $\tfrac14(z\gamma_{12}^2+\gamma_{21}^2/z)$ over the weight ratio $z$ gives $\tfrac12\gamma_{12}\gamma_{21}$ at $z^*=\gamma_{21}/\gamma_{12}$, which lands on $\lambda_1\lambda_2>\gamma_{12}\gamma_{21}$ as printed in eq. (12). The transcription below is the render, not the paper's intent; use eq. (12)/(13) as stated.

The original concern, kept for the record: the $\tfrac12$ prefactor in (11) is what `pdftotext -layout` renders, and the preprint shows the same glyph pattern, but it could **not** be reconciled with the cross-term bound in the proof of Lemma 3.2 (which bounds $2\alpha_1\langle v_{x_1},\tfrac{\partial X_1}{\partial u_1}\circ(Th_2)w_{x_2}\rangle_{G_1}+2\alpha_2\langle\cdots\rangle_{G_2}$ by $(\alpha_1\gamma_1+\alpha_2\gamma_2)\|v_{x_1}\|_{G_1}\|w_{x_2}\|_{G_2}$ — a factor of $2$ off either way). If Lemma 3.2's constants are ever load-bearing, re-derive from the PDF rather than trusting this transcription. Def. 2.1, Def. 2.2, Thm. 2.3, Prop. 2.4, Prop. 2.5 and Example 1 came out of the extraction cleanly and are transcribed exactly.
:::

:::tip[Proposition — monotone vector fields, Prop. 4.1]

$X$ is *strongly monotone* on $\mathcal U$ with parameter $\lambda>0$ if for any geodesic $\gamma$ joining two points of $\mathcal U$, $\phi(t)\triangleq\langle\!\langle\gamma'(t),X(\gamma(t))\rangle\!\rangle_G+\lambda t\langle\!\langle\gamma'(0),\gamma'(0)\rangle\!\rangle_G$ is monotone decreasing. Then: $X$ strongly monotone on $\mathcal U$ with parameter $\lambda$ $\iff$ $(\mathcal U,X,G,\lambda)$ is a contracting system with $\mathcal U$ **geodesically convex**.
:::

:::tip[Corollary — gradient systems, Cor. 5.1]

For $X=-\operatorname{grad}\psi=-G^\sharp(d\psi)$: let $\bar x$ be a critical, **nondegenerate zero** of $\psi\in C^\infty(M)$, and $L\in[0,L_{\mathrm{cpt,reg}}(\psi,\bar x))$. If there is $\lambda>0$ with
$$\operatorname{Hess}\psi(x)\succcurlyeq\lambda G(x)\qquad\text{for each }x\in\psi^{-1}(\le L,\bar x), \tag{15}$$
then Theorem 2.3 holds with $\mathcal U=\psi^{-1}(\le L,\bar x)$, $K=1$, metric $G$, $X=-\operatorname{grad}\psi$. Here $\operatorname{Hess}\psi(x)\cdot(v_x,w_x)\triangleq\langle\!\langle v_x,\nabla_{w_x}\operatorname{grad}\psi\rangle\!\rangle_{G(x)}$, in coordinates $(\operatorname{Hess}\psi)_{ij}=\partial^2\psi/\partial x^i\partial x^j-(\partial\psi/\partial x^k)\Gamma^k_{ij}$ (eq. 14). $K=1$ because (15) makes $\psi$ strongly convex on $\mathcal U$, hence $1$-reachable.
:::

## Worked examples

**Example 1 (damped oscillator) — the archetype for why block-diagonal metrics fail.** For positive constants $k,m,b$, take $M=\mathbb R^2$ and
$$X = y\frac{\partial}{\partial x} - \Big(\frac{k}{m}x+\frac{b}{m}y\Big)\frac{\partial}{\partial y}.$$
With the damping ratio $\zeta\triangleq b/(2\sqrt{km})$, for every $\varepsilon\in\,]0,\,1/(1+\zeta^2)[$ the field $X$ is infinitesimally contracting on **all of** $M$ with respect to
$$G = \tfrac12 k\,dx\otimes dx + b\varepsilon\,dx\otimes dy + \tfrac12 m\,dy\otimes dy.$$
The origin is the unique globally exponentially stable fixed point, and Prop. 2.5(iii) gives the strict Lyapunov function $V(x,y)=\tfrac12kx^2+\tfrac12my^2+\varepsilon b xy$. (The paper notes the Prop. 2.5(ii) Lyapunov function is "less insightful".) The point for us: the **cross term $b\varepsilon\,dx\otimes dy$ is essential** — the mechanical energy metric $\tfrac12k\,dx^2+\tfrac12m\,dy^2$ is only *Killing* for the undamped field (Remark 1), giving $\lambda=0$, i.e. Lyapunov stability but no contraction. Position–velocity coupling in the metric is what buys exponential decay.

*(The symbol for the damping ratio extracts as $\xi$ in the published PDF and $\zeta$ in the preprint — same quantity $b/(2\sqrt{km})$; the glyph is cosmetic.)*

**Example 2 (forced oscillator on $S^1$).** $X=(\tfrac12-\sin\theta)\partial_\theta$, $\Delta\triangleq\,]-\pi/2,\pi/2[$ forward invariant, $G=\cos\theta\,d\theta\otimes d\theta$ positive definite on $\Delta$. Contracting on any $\mathcal U\subset\,]\arcsin\frac{1-\sqrt{97}}{12},\arcsin\frac{1+\sqrt{97}}{12}[\,\subset\Delta$; if $\pi/6\in\mathcal U$ all of Thm. 2.3's hypotheses hold. The chosen $G$ does **not** capture the whole basin of attraction of $\theta=\pi/6$ — contraction regions are conservative estimates of basins.

**Remark 1 (Killing fields).** The $\lambda\to0^+$ limit of everything above. If $(\mathcal U,X,G,\lambda)$ is contracting then so is $(\mathcal U,X+Y,G,\lambda)$ for **any** Killing field $Y$ of $(M,G)$ — the contraction condition is blind to the isometry group. Prop. 2.5(iv) degenerates to Liouville volume preservation.

## What this gives the project

- **The nominal-trajectory bound in the exact form a tube needs.** Eq. (5), $d_G(\Phi_t(x_0),\Phi_t(x_1))\le Ke^{-\lambda t}d_G(x_0,x_1)$, is the deterministic backbone; a probabilistic tube is what you add to it once noise is switched on. Compare with the stochastic analogue in [[@phamStochasticContractionRiemannian2013]], and with the mean-squared bound shape of [[@daniObserverDesignStochastic2015]].
- **Eq. (8) is the reusable computational trick.** $\tfrac{d}{dt}\|S\|_G^2 = 2\langle\!\langle\overset{G}{\nabla}_SX,S\rangle\!\rangle_G$ needs only metric compatibility, torsion-freeness, and $[\tilde S,\tilde T]=0$. The same three facts are what let an intrinsic AMGF energy function be differentiated along the flow without ever writing $\partial g_{ij}$.
- **A clean statement of what "coordinate-free" buys.** Prop. 2.4 makes explicit that the chart formula (9) holds *in every admissible chart simultaneously* precisely because (4) is tensorial. That is the template for the claim the project wants to make about the AMGF.
- **A topological hard stop.** "No globally contracting vector fields on compact manifolds" (Bhat–Bernstein) means any $SO(3)$ or $SE(3)$ result must be **regional**: a $K$-reachable, forward-invariant $\mathcal U$, never all of $G$. Any tube claim phrased globally on a compact group is wrong for topological reasons before any analysis.
- **$K$-reachability is the right relaxation of convexity to carry over.** Geodesic convexity of a region in $SO(3)$ is restrictive; $K$-reachability costs only a multiplicative $K$ in the tube radius at $t=0$ and is checkable via geodesic balls (Prop. 2.5(iii) gives $K=1$ on $B_r$ when $B_r\subset\mathcal U$).
- **Numbering for the unverified draft.** `refs/claude-gen-import/contraction-mech-RG.tex` cites `[SB13]` Def. 2.1, Def. 2.2, Thm. 2.3, eq. (8), Prop. 2.5, Example 1 — all confirmed present with those exact numbers in both PDFs, and transcribed above.

## Caveats / limitations

- **Autonomous only.** The whole paper treats $X\in\Gamma^\infty(TM)$ time-invariant. Time-varying vector fields (which is what a tracking error system around a nominal trajectory is) are not covered; the proof of Thm. 2.3 uses that $T(s,t)$ is the maximal integral curve of a *fixed* $X$. Extending to $X(x,t)$ is routine but is not done here.
- **Constants are intrinsic — this paper is on the right side of the project's thesis.** The only constants in (5) are $\lambda$ (from the tensorial inequality (4)) and $K$ (a purely metric-space quantity from Def. 2.2). Neither is a sup-norm of metric components or their derivatives. Christoffel symbols appear only in the chart *translation* (eqs. 1, 3, 9, 10, 14), never in a bound. So the conservatism critique aimed at [[@daniObserverDesignStochastic2015]] does **not** apply here — this is the standard to hold the stochastic extension to.
- **Curvature is invoked rhetorically, not quantitatively.** Three appearances only: (a) the remark after Thm. 2.3 that (4) "describes intrinsically how the vector field and the curvature of $(M,G)$ must interact"; (b) $\mathcal L_XS\ge2\lambda S$ for the scalar curvature $S$ in the homothetic (equality) case, §4; (c) "curvature of the function $\psi$" in the Cor. 5.1 discussion, meaning the Hessian, not Riemannian curvature. **No curvature bound, no sectional-curvature hypothesis, no injectivity radius appears anywhere.** The deterministic theory does not need them; the stochastic version will (Itô corrections and comparison theorems), so this paper is not a source for those.
- **Interconnection lemmas assume compact $\mathcal U_i$** and produce only a **block-diagonal** product metric — which is exactly the structure Example 1 shows is inadequate for a single damped mechanical system. Cascades/feedback of already-certified subsystems, not a construction of $G$ for a mechanical system.
- **Footnote 1's definition of $\preccurlyeq$ is sloppy**: "$A\preccurlyeq B$ if $B-A$ is a positive definite symmetric $(0,2)$ tensor" is stated for *positive definite* $A,B$, yet (9) and (15) apply it with $B=-2\lambda[G_{i\ell}]$ (negative definite). Read it as the obvious order relation on symmetric tensors.
- **Prop. 2.5(iii) claims only local Lyapunov behaviour** for $x\mapsto d_G(x,\bar x)$ — $d_G(\cdot,\bar x)$ is not smooth beyond the cut locus, and the paper does not discuss the cut locus at all. On $SO(3)$ that is the antipodal set and it matters.

:::warning[Open question — stated by the authors, §6 Conclusions]

"While the application of contraction theory to mechanical systems is complicated by the existence of first integrals, a problem which to our knowledge remains open is that of **finding succinct and meaningful conditions for a dissipative mechanical system to exhibit contracting behavior**." The authors also flag the unexplored relationship between contraction and Rantzer's dual-Lyapunov / density-function approach and Koopman theory.

This is precisely the project's setting — simple mechanical systems on Lie groups — so the natural first-order structure ($T G$ or $G\times\mathfrak g$, kinetic-energy metric plus dissipation) has no off-the-shelf contraction certificate from this paper. Example 1 is the $n=1$ hint: the certificate needed a position–velocity cross term $b\varepsilon\,dx\otimes dy$, i.e. **not** the Sasaki-type block-diagonal lift of the kinetic energy metric.
:::
