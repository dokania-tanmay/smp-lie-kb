---
tags: [contraction, riemannian-geometry, incremental-stability, coordinate-free]
---
# Contraction on a Riemannian Manifold

**Prereq:** [[riemannian-geometry]] (Levi-Civita connection, metric compatibility, arclength, Riemannian distance), [[notation]], [[07-jacobi-equation]] (variation fields, covariant differentiation along a two-parameter map, $\tfrac{D}{ds}\partial_t\gamma=\tfrac{D}{dt}\partial_s\gamma$)
**Goal:** state the contraction condition and $K$-reachability with the quantifiers right, derive the single identity that makes the theory computable *without ever forming the Christoffel symbols of the certifying metric*, and see on the damped oscillator why that metric must carry a position–velocity cross term.

Everything here is [[@simpson-porcoContractionTheoryRiemannian2014]] §2, transcribed into this repo's notation.

## The two definitions

Throughout, $M$ is a smooth $n$-manifold, $X\in\Gamma^\infty(TM)$ a vector field with flow $\Phi_t$, and $G$ a Riemannian metric on $M$ with Levi-Civita connection $\nabla^G$, arclength $\ell_G$, distance $d_G$.

:::info[Definition — contracting system, Def. 2.1]
A **contracting system** is a quadruple $(\mathcal U,X,G,\lambda)$ — $\mathcal U\subseteq M$ connected (the *contraction region*), $X$ the system field, $G$ the *contraction metric*, $\lambda>0$ the *rate* — such that

$$\big\langle \nabla^G_{w_x}X,\; w_x\big\rangle_{G(x)} \;\le\; -\lambda\,\|w_x\|^2_{G(x)}
\qquad\text{for each } x\in\mathcal U \text{ and each } w_x\in T_xM. \tag{4}$$
:::

Read the quantifiers exactly: the **base point** is restricted to $\mathcal U$, the **tangent vector is not** — $w_x$ ranges over all of $T_xM$, not a distinguished subspace, not just unit vectors (though (4) is homogeneous of degree 2, so unit vectors suffice). $X$ and $G$ live on all of $M$; only the inequality is localised.

Equivalently $\mathcal L_XG\preceq-2\lambda G$, since $\langle w_x,w_x\rangle_{\mathcal L_XG}=2\langle\nabla^G_{w_x}X,w_x\rangle_G$.

**$G$ is a design choice, and it is not the metric the system came with.** For a mechanical system on a Lie group the state manifold is $TG\cong G\times\mathfrak g$ (see [[02-trivialization-of-tg]]) and the physics supplies the kinetic-energy metric $\mathbb G$ of [[notation]] on $G$ — a metric on the *configuration* manifold. $G$ here is a metric on the *state* manifold, chosen by whoever is writing the certificate. Nothing forces it to be the Sasaki lift of $\mathbb G$, and lesson 16 is entirely about why it must not be. Consequently **"this system is contracting" is not a statement** until $G$ is named; Problem 4 makes that concrete.

:::info[Definition — $K$-reachable set, Def. 2.2]
For $K\ge1$, a set $\mathcal U\subseteq M$ is **$K$-reachable** if for **any** $x_0,x_1\in\mathcal U$ there is a $C^1$ curve $\gamma:[0,1]\to\mathcal U$ with $\gamma(0)=x_0$, $\gamma(1)=x_1$, and
$$\ell_G(\gamma)\;\le\;K\,d_G(x_0,x_1).$$
:::

Three traps. (i) The curve must **stay inside $\mathcal U$**. (ii) It must be $C^1$, whereas $d_G$ is an infimum over merely piecewise-smooth curves — so $K$ absorbs both the detour and the corner-smoothing. (iii) $d_G$ is the distance in $(M,G)$, *not* the induced length metric of $\mathcal U$.

Why it is needed: the contraction estimate (4) is only known to hold at points of $\mathcal U$, so the proof can only transport a curve that lies in $\mathcal U$. The minimising geodesic between two points of $\mathcal U$ may leave $\mathcal U$ entirely — think of a thin horseshoe — and along the excursion nothing is assumed. $K$-reachability is the price of admission, and it is the right relaxation of geodesic convexity (geodesically convex $\Rightarrow$ $1$-reachable; a geodesic ball $B_r\subset\mathcal U$ is $1$-reachable).

## The theorem

:::tip[Theorem — Thm. 2.3]
Suppose (i) $(\mathcal U,X,G,\lambda)$ is a contracting system; (ii) $\mathcal U$ is $K$-reachable and forward $X$-invariant; (iii) $X$ is forward complete on $\mathcal U$. Then for all $x_0,x_1\in\mathcal U$ and $t\ge0$,
$$d_G\big(\Phi_t(x_0),\Phi_t(x_1)\big)\;\le\;K\,e^{-\lambda t}\,d_G(x_0,x_1). \tag{5}$$
:::

## The mechanism — why this is usable

This is the real content of the lesson. Take the $K$-reachable curve $\gamma$ from $x_0$ to $x_1$ and push it along the flow: $\Gamma(s,t)=\Phi_t(\gamma(s))$, a two-parameter map exactly as in [[07-jacobi-equation]]. Write

$$S(s,t)=\partial_s\Gamma \ \ (\text{the \textbf{variation field}}),\qquad T(s,t)=\partial_t\Gamma = X(\Gamma(s,t)),$$

and $L(t)=\int_0^1\|S(s,t)\|_{G}\,ds$, the $G$-length of the transported curve. Then

$$\frac{d}{dt}\|S\|_G^2
\;\overset{\text{(a)}}{=}\; 2\big\langle \tfrac{D}{dt}S,\,S\big\rangle_G
\;\overset{\text{(b)}}{=}\; 2\big\langle \tfrac{D}{ds}T,\,S\big\rangle_G
\;\overset{\text{(c)}}{=}\; 2\big\langle \nabla^G_{S}X,\,S\big\rangle_G
\;\overset{\text{(4)}}{\le}\; -2\lambda\,\|S\|_G^2 . \tag{8}$$

(a) is metric compatibility of $\nabla^G$; (b) is torsion-freeness applied to $\partial_s,\partial_t$, whose bracket vanishes — the *same* lemma that produced the Jacobi equation; (c) is $T=X\circ\Gamma$ and forward invariance of $\mathcal U$, which is what puts the base point where (4) is known. Then $\dot L\le-\lambda L$, Grönwall gives $L(t)\le e^{-\lambda t}L(0)$, and $d_G(\Phi_tx_0,\Phi_tx_1)\le L(t)$ with $L(0)\le K\,d_G(x_0,x_1)$ closes (5).

:::tip[Proposition — the equivalence worth remembering]
Condition (4) holds on $\mathcal U$ **iff** every variation field along every trajectory in $\mathcal U$ decays as $\|S(s,t)\|_G\le e^{-\lambda t}\|S(s,0)\|_G$.
:::

That equivalence is the whole reason the theory is workable. Chain (8) uses **only** metric compatibility and torsion-freeness. **No Christoffel symbol of $G$ is ever computed** — which matters enormously downstream, because the state manifold of a mechanical system on a Lie group is $2n$-dimensional and $G$ will be a $g$-natural metric with cross terms, whose $\nabla^G$ nobody wants to write out. Every later contraction lesson exploits this: you check a pointwise inequality in $\nabla^G_wX$, not a connection.

For completeness, the chart translation (Prop. 2.4): (4) $\iff$ $\big[G_{ki}\partial_\ell X^k+G_{k\ell}\partial_iX^k+X^j\partial_jG_{i\ell}\big]\preceq-2\lambda[G_{i\ell}]$ **in every admissible chart simultaneously**, which is the generalised Demidovich condition and reduces to "symmetric part of the Jacobian negative definite" for Euclidean $G$ on $\mathbb R^n$.

## Consequences (Prop. 2.5)

Assume additionally that $(\mathcal U,d_G)$ is a complete metric space, $\mathcal U$ forward invariant and $K$-reachable, $X$ forward complete.

- **(i) Fixed point.** $X$ has a unique zero $\bar x\in\mathcal U$ and $\Phi_t(x)\to\bar x$ exponentially for every $x\in\mathcal U$. *(Pick $\tau$ with $Ke^{-\lambda\tau}<1$; $\Phi_\tau$ is a Banach contraction.)* It need not be the only zero of $X$ on $M$.
- **(ii) Krasovskii function.** $V(x)=\|X(x)\|^2_{G(x)}$ is a strict Lyapunov function: put $w_x=X(x)$ in (4) to get $\dot V\le-2\lambda V$.
- **(iii) Incremental Lyapunov function.** $x\mapsto d_G(x,\bar x)$ works *locally* — only locally, because $d_G(\cdot,\bar x)$ loses smoothness at the cut locus ([[08-hessian-comparison]]), which on $SO(3)$ is the antipodal set. On any $B_r(\bar x)\subset\mathcal U$ the system is contracting with $K=1$ and $B_r(\bar x)$ is forward invariant.
- **(iv) Volume.** $\operatorname{div}_GX\le-n\lambda$, so $\operatorname{Vol}(\Phi_t(B_r(x)))\to0$ exponentially. [[15-symplectic-not-contracting]] turns this into an obstruction.

:::warning[Topological hard stop — contractibility]
A contraction region is **contractible**: after a time reparametrisation, $\mathrm{id}_{\mathcal U}$ is homotopic to the constant map $x\mapsto\bar x$. By Bhat–Bernstein's topological obstruction (cited in the source), **there is no globally contracting vector field on a compact manifold.** So every $SO(3)$ or $SE(3)$ contraction result is *regional by topology*, not by weakness of proof: $\mathcal U$ must be a proper, contractible, forward-invariant, $K$-reachable subset. A tube claim phrased globally on a compact group is wrong before any analysis begins.
:::

## Worked example — the damped oscillator needs a cross term

Source Example 1. $M=\mathbb R^2$, positive constants $m,k,b$, damping ratio $\zeta=b/(2\sqrt{km})$, and
$$X=y\,\partial_x-\Big(\tfrac km x+\tfrac bm y\Big)\partial_y,\qquad\text{i.e. } A=DX=\begin{pmatrix}0&1\\-k/m&-b/m\end{pmatrix}.$$

Take $G$ **constant** in these coordinates, so $\Gamma^i_{jk}=0$ and $\nabla^G_wX=Aw$ exactly. Condition (4) becomes the matrix inequality $\operatorname{sym}(PA)\preceq-\lambda P$, where $P=[G_{i\ell}]$.

**Attempt 1 — the mechanical energy metric.** $P_0=\operatorname{diag}(k/2,\,m/2)$, i.e. $\|w\|^2_{G}=\tfrac12kw_1^2+\tfrac12mw_2^2$. Then
$$P_0A=\begin{pmatrix}0&k/2\\-k/2&-b/2\end{pmatrix},\qquad \operatorname{sym}(P_0A)=\begin{pmatrix}0&0\\0&-b/2\end{pmatrix}.$$
The off-diagonal entries cancel *exactly* — that cancellation is the statement that the undamped field is Killing for the energy metric. The result is negative **semi**definite: at $w=(1,0)$ (a pure position perturbation) $\langle\nabla^G_wX,w\rangle_G=0$. So $\lambda=0$: Lyapunov stability, no contraction. Energy alone certifies nothing.

**Attempt 2 — add a cross term.** $\|w\|_G^2=\tfrac12kw_1^2+b\varepsilon\,w_1w_2+\tfrac12mw_2^2$, i.e.
$$P_\varepsilon=\begin{pmatrix}k/2 & b\varepsilon/2\\ b\varepsilon/2 & m/2\end{pmatrix},\qquad
\operatorname{sym}(P_\varepsilon A)=-\begin{pmatrix}\dfrac{b\varepsilon k}{2m} & \dfrac{b^2\varepsilon}{4m}\\[4pt] \dfrac{b^2\varepsilon}{4m} & \dfrac{b(1-\varepsilon)}{2}\end{pmatrix}.$$
Negative definiteness needs $\varepsilon>0$ and positive determinant:
$$\frac{b^2\varepsilon k(1-\varepsilon)}{4m}-\frac{b^4\varepsilon^2}{16m^2}>0
\iff k(1-\varepsilon)>\frac{b^2\varepsilon}{4m}
\iff \varepsilon<\frac{1}{1+\zeta^2}.$$
So for every $\varepsilon\in\big(0,\tfrac1{1+\zeta^2}\big)$ the system is contracting on **all of $\mathbb R^2$** (convex, hence $1$-reachable), with some $\lambda>0$, and $V=\tfrac12kx^2+\tfrac12my^2+\varepsilon bxy$ is the strict Lyapunov function of Prop. 2.5(iii).

**The moral, and it is the motivation for lessons 16–17:** the $\varepsilon$ term is a *position–velocity coupling in the metric*. Block-diagonal metrics — [[13-sasaki-metric|Sasaki lifts]], total-energy metrics — put a zero exactly where the damped oscillator needs a negative number. One degree of freedom already shows it.

## Where this sits in the standing question

**Intrinsic — kind 1.** The constants in (5) are $\lambda$, defined by the tensorial inequality (4), and $K$, a pure metric-space quantity from Def. 2.2. Neither is a sup-norm of metric components or their derivatives: **no $\sup|\partial G_{ij}|$ or $\sup|\partial^2G_{ij}|$ appears anywhere in the paper.** Christoffel symbols occur only in the chart *translation* (Prop. 2.4), never inside a bound — and Prop. 2.4 says that formula holds in every chart at once precisely because (4) is tensorial. The verified rewrite [[@simpson-porcoContractionTheoryRiemannian2014]] confirms this line by line.

So deterministic contraction theory is already on the **good** side of this project's conservatism critique, and is the standard the stochastic extension must be held to. The chart-dependence the thesis attacks — [[@daniObserverDesignStochastic2015]]'s $\bar m_x,\bar m_{x^2}$ — enters somewhere else: from the Itô correction and the path-integral surrogate for distance, not from contraction itself.

:::warning[Open question]
Curvature is invoked only rhetorically here — the source has no sectional-curvature hypothesis and no injectivity radius. That is fine deterministically. It cannot survive the addition of noise, where a second-order operator acts on $d_G$ and comparison theorems are unavoidable. Which curvature hypothesis is the minimal one to add to (4) is exactly what Phase 4–5 has to settle.
:::

## Problems

1. **Recall.** From memory, state Def. 2.1 and Def. 2.2. For Def. 2.1, say precisely what $x$ and what $w_x$ range over, and why $G$ cannot be inferred from the system. For Def. 2.2, name the three easy-to-miss requirements. Then list the three hypotheses of Thm. 2.3 and say which one each definition supplies.

2. **Compute.** On $M=\mathbb R^2$ take $X=Az$ with $A=\begin{pmatrix}-1&5\\0&-2\end{pmatrix}$ and the constant metric $G=dx\otimes dx+25\,dy\otimes dy$. (a) Explain why $\nabla^G_wX=Aw$ with no correction term. (b) Verify $(\mathbb R^2,X,G,\tfrac12)$ is a contracting system. (c) Find the largest $\lambda$ for which (4) holds with this $G$, and compare it to $-\max\operatorname{Re}\operatorname{spec}(A)$.

3. **Prove.** Let $(\mathcal U,X,G,\lambda)$ satisfy all three hypotheses of Thm. 2.3. (a) Show $X$ has **at most one** zero in $\mathcal U$, in three lines from (5). (b) Show directly from (8) that $V(x)=\|X(x)\|^2_{G(x)}$ obeys $\tfrac{d}{dt}V(\Phi_t x)\le-2\lambda V(\Phi_t x)$, and identify which choice of variation field makes $S=X$.

4. **Break it.** Two hypotheses, dropped one at a time.
   (a) *No metric named.* Same $A$ as Problem 2, now with the Euclidean metric $G_1=dx^2+dy^2$ on $\mathcal U=\mathbb R^2$. Show $(\mathbb R^2,X,G_1,\lambda)$ is contracting for **no** $\lambda>0$. Then, using $x_0=(0,0)$ and $x_1=(1,1)$, show $\tfrac{d}{dt}\big|_{t=0}d_{G_1}(\Phi_tx_0,\Phi_tx_1)^2>0$ — so the conclusion (5) fails outright with the $K=1$ that convexity of $\mathbb R^2$ supplies. Since $A$ is Hurwitz, both trajectories still converge. What exactly is the difference between "asymptotically stable" and "contracting", and what does this say about the phrase "the system is contracting"?
   (b) *No $K$-reachability.* Let $M=\mathbb R^2$ Euclidean and let $\mathcal U$ be the open unit disc minus the slit $\{0\}\times[-1,0]$. Show $\mathcal U$ is $K$-reachable for **no** finite $K$, by exhibiting a family of point pairs whose ratio $\ell_G(\gamma)/d_G$ is unbounded. Then say which single step of the proof of Thm. 2.3 fails, and why forward invariance alone does not rescue it.

---

## Solutions

**1.** Def. 2.1: $x$ ranges over $\mathcal U$ only; $w_x$ over *all* of $T_xM$ (homogeneity makes unit $w_x$ equivalent). $G$ is a free design variable: (4) is an inequality *relating* $X$ to $G$, so different $G$ give different verdicts on the same $X$; the kinetic-energy metric of the mechanics is a metric on the configuration manifold and has no privileged claim to be a certificate on the state manifold. Def. 2.2 traps: curve inside $\mathcal U$; $C^1$ not just piecewise smooth; $d_G$ measured in $(M,G)$, not in $\mathcal U$. Thm. 2.3 hypotheses: contraction (Def. 2.1); $K$-reachability (Def. 2.2) *and* forward $X$-invariance of $\mathcal U$; forward completeness.

**2.** (a) $G_{ij}$ is constant in these coordinates, so all $\partial_kG_{ij}=0$, so all $\Gamma^i_{jk}=0$, so $\nabla^G_wX=w^j\partial_jX=Aw$ — no correction. (b) With $P=\operatorname{diag}(1,25)$, $PA=\begin{pmatrix}-1&5\\0&-50\end{pmatrix}$ and $\operatorname{sym}(PA)=\begin{pmatrix}-1&5/2\\5/2&-50\end{pmatrix}$. Need $\operatorname{sym}(PA)+\lambda P\preceq0$: at $\lambda=\tfrac12$ this is $\begin{pmatrix}-1/2&5/2\\5/2&-75/2\end{pmatrix}$, with negative diagonal and determinant $\tfrac{75}{4}-\tfrac{25}{4}=\tfrac{50}4>0$ — negative definite. ✓ (c) In general the conditions are $\lambda<1$ and $(1-\lambda)(50-25\lambda)\ge\tfrac{25}4$, i.e. $25(1-\lambda)^2\ge\tfrac{25}{4}$, i.e. $\lambda\le\tfrac12$. So $\lambda_{\max}=\tfrac12$ for this $G$, strictly worse than the spectral rate $1$. Contraction rates are metric-dependent lower bounds on the asymptotic rate; a better $G$ pushes $\lambda$ towards $1$ but (4) is a *pointwise* condition and generally cannot attain it.

**3.** (a) Let $X(p)=X(q)=0$ with $p,q\in\mathcal U$. Then $\Phi_t(p)=p$ and $\Phi_t(q)=q$ for all $t\ge0$, so (5) reads $d_G(p,q)\le Ke^{-\lambda t}d_G(p,q)$ for every $t\ge0$. Let $t\to\infty$: $d_G(p,q)\le0$, hence $p=q$. (b) Take the variation $\Gamma(s,t)=\Phi_{t+s}(x)$; then $S=\partial_s\Gamma=X(\Gamma)$ and $T=\partial_t\Gamma=X(\Gamma)$, so $S=T=X$ along the trajectory and (8) gives $\tfrac{d}{dt}\|X\|_G^2=2\langle\nabla^G_XX,X\rangle_G\le-2\lambda\|X\|^2_G$. That is Prop. 2.5(ii): the Krasovskii function is the contraction condition evaluated on the flow direction itself.

**4(a).** Euclidean $G_1$ means $P=I$, so (4) requires $\operatorname{sym}(A)=\begin{pmatrix}-1&5/2\\5/2&-2\end{pmatrix}\preceq-\lambda I$. Its determinant is $2-\tfrac{25}4<0$, so it is indefinite and no $\lambda>0$ (indeed no $\lambda\ge0$) works. Concretely at $w=(1,1)$: $Aw=(4,-2)$ and $\langle Aw,w\rangle=4-2=2>0$. Now $x_0=(0,0)$ is an equilibrium, so $d_{G_1}(\Phi_tx_0,\Phi_tx_1)=\|z(t)\|$ where $z(0)=(1,1)$, and $\tfrac{d}{dt}\|z\|^2|_{t=0}=2z^\top Az=4>0$. Distance strictly increases, so (5) with $K=1$ fails immediately — even though $\operatorname{spec}(A)=\{-1,-2\}$ makes the origin globally exponentially stable. The difference: asymptotic stability is a statement about the *limit*, contraction is a statement about *every instant and every pair*. Transient growth in a badly chosen metric is compatible with the former and fatal to the latter. Hence "the system is contracting" is not a well-formed claim; only "$(\mathcal U,X,G,\lambda)$ is contracting" is. Problem 2 shows the very same $X$ is contracting once $G$ is chosen well — the metric is the certificate.

**4(b).** Take $x_\delta^\pm=(\pm\delta,-\tfrac12)$ for small $\delta>0$: points on either side of the slit. Then $d_G(x^+_\delta,x^-_\delta)=2\delta\to0$. Any curve inside $\mathcal U$ joining them cannot cross the slit, so it must pass around the slit tip at the origin; its length is at least $2\cdot\tfrac12=1$ (down to the tip and back). Hence $\ell_G(\gamma)/d_G\ge1/(2\delta)\to\infty$, and no finite $K$ works. The step that fails is the *initialisation* $L(0)\le K\,d_G(x_0,x_1)$: the flow-transport estimate $\dot L\le-\lambda L$ still holds for any admissible $\gamma\subset\mathcal U$ (that is where forward invariance is used, and it is used only to keep $\Gamma(s,t)$ inside $\mathcal U$ so that (4) applies at $t>0$), but there is no admissible starting curve whose length is controlled by $d_G(x_0,x_1)$. Forward invariance says the flow does not leave $\mathcal U$; it says nothing about whether $\mathcal U$ contains a short path between two of its points, which is a static, purely geometric property of the region.
