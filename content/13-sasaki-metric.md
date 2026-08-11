---
tags: [riemannian, curvature, tangent-bundle, sasaki, so3]
---
# The Sasaki Metric on $TM$ and Its Curvature

**Prereq:** [[05-riemann-tensor]], [[06-curvature-left-invariant-metrics]], [[12-double-tangent-bundle]], [[notation]]
**Goal:** write down the obvious metric on $TM$, state its sectional curvatures, and compute the body angular velocity at which the horizontal curvature of $T\,SO(3)$ goes negative even though the base is a round $\mathbb{RP}^3$.

This lesson answers the last open question in [[mechanical-systems-on-lie-groups]] — *"How does the curvature of $TG$ in the Sasaki metric look?"* — and it is listed in [[00-study-plan]] row 13 as a potential result of the project. The short answer: **worse than the base, quadratically worse in speed, and almost never nice.**

## Definition

[[12-double-tangent-bundle]] gives the splitting of $T_{(p,u)}(TM)$ into horizontal and vertical parts through the pair of maps $\xi\mapsto(d\pi\,\xi,\ K\xi)$, with $\pi:TM\to M$ the projection and $K$ the connector of the Levi-Civita connection. Horizontal $=\ker K$, vertical $=\ker d\pi$, and both are isomorphic to $T_pM$.

:::info[Definition — Sasaki metric]
For $\xi,\eta\in T_{(p,u)}(TM)$,
$$g_S(\xi,\eta) \;=\; g\big(d\pi\,\xi,\ d\pi\,\eta\big) \;+\; g\big(K\xi,\ K\eta\big).$$
Equivalently, $g_S$ is the unique metric on $TM$ for which the horizontal and vertical subspaces are orthogonal and both lifts are isometries: for $X,Y\in T_pM$,
$$g_S(X^h,Y^h)=g(X,Y),\qquad g_S(X^v,Y^v)=g(X,Y),\qquad g_S(X^h,Y^v)=0 .$$
:::

There is no choice being made here beyond the connection. Split the tangent space in the only canonical way available, then apply $g$ to each factor and add. In mechanics language it is *kinetic energy plus configuration length* with unit weights: the block-diagonal metric $\mathrm{diag}(g,g)$ in the $(q,v)$ splitting.

That is precisely why what follows is a cautionary tale. The construction looks like it cannot cost anything, and it does.

## Kowalski's sectional curvatures

Stated, **not derived**. The derivation (Kowalski 1971) is the Koszul formula applied to the six bracket combinations of horizontal and vertical lifts, then $R$ expanded term by term; it runs several pages, is entirely mechanical, and produces no idea that the statement does not already carry. What matters downstream is the shape of the answer.

:::tip[Theorem — Kowalski 1971]
Let $(p,u)\in TM$ and let $X,Y\in T_pM$ be $g$-orthonormal. Then for the Sasaki metric,
$$\mathrm{Sec}\big(X^h,Y^h\big)=\mathrm{Sec}(X,Y)-\tfrac34\big\|R(X,Y)u\big\|^2,$$
$$\mathrm{Sec}\big(X^h,Y^v\big)=\tfrac14\big\|R(u,Y)X\big\|^2,\qquad
\mathrm{Sec}\big(X^v,Y^v\big)=0 .$$
All norms are $g$-norms at $p$; every lift is taken at $(p,u)$.
:::

Three remarks, in order of how easy they are to get wrong.

**The constants $-\tfrac34$ and $+\tfrac14$ are convention-independent.** Both correction terms are *squared norms*, so flipping the global sign of $R$ (this repo's $R$ is the negative of the do Carmo-convention one — see [[06-curvature-left-invariant-metrics]]) changes nothing in them, and swapping the two antisymmetric slots, $R(u,Y)\mapsto R(Y,u)$, only flips a sign inside a square. What *is* convention-locked is the leading term $\mathrm{Sec}(X,Y)$, and it is stated here against [[notation]], under which the round sphere has $\mathrm{Sec}>0$ and a bi-invariant metric has $\mathrm{Sec}=\tfrac14\|[X,Y]\|^2\ge0$. What is **not** free is *which slot $u$ sits in*: $R(X,Y)u$ and $R(u,Y)X$ are genuinely different tensor contractions, not related by any symmetry, and they carry different constants.

**Vertical planes are flat because the fibres are.** A fibre $T_pM$ with the induced metric is a Euclidean $\mathbb R^n$, and it is totally geodesic in $(TM,g_S)$ — its second fundamental form vanishes, so its intrinsic and induced curvatures agree, and both are $0$. Same for the zero section, which sits inside $TM$ as a totally geodesic isometric copy of $(M,g)$.

**The horizontal term is the whole story.** It is the only one that can be negative, and it decreases quadratically in $\|u\|$.

:::tip[Corollary — scalar curvature drop]
With $\|R_u\|^2:=\sum_{i,j}\|R(X_i,X_j)u\|^2$ over a $g$-orthonormal frame $\{X_i\}$ of $T_pM$,
$$\mathrm{Scal}\big(TM,g_S\big)\big|_{(p,u)}=\mathrm{Scal}(M,g)\big|_p-\tfrac14\big\|R_u\big\|^2 .$$
:::

The $\tfrac14$ is a residue: the horizontal planes contribute $-\tfrac34\|R_u\|^2$, the mixed planes give back $+\tfrac12\|R_u\|^2$ (the two families are exchanged by the pair symmetry (S4) of [[05-riemann-tensor]]), the vertical planes give nothing. So $TM$ loses scalar curvature quadratically as you move out along a fibre, and it never gains any.

## Rigidity

:::tip[Theorem — Kowalski 1971, Musso–Tricerri 1988]
For $(TM,g_S)$ over a Riemannian $(M,g)$:

1. $(TM,g_S)$ is **flat** $\iff$ $(M,g)$ is flat.
2. $(TM,g_S)$ is **locally symmetric** ($\nabla\mathrm{Rm}=0$) $\iff$ $(M,g)$ is flat $\iff$ $(TM,g_S)$ is flat.
3. $(TM,g_S)$ is **Einstein** $\iff$ $(M,g)$ is flat.
4. $(TM,g_S)$ **never** has constant sectional curvature $c\neq0$.
:::

Item 2 is the striking one: on $TM$ there is no middle ground between flat and not-even-locally-symmetric. Item 4 is a one-line consequence of the vertical formula (problem 3). Musso–Tricerri's own summary of this was that $g_S$ is "very rigid" — which is the polite version of *the obvious metric on $TM$ is almost never a metric you want*.

## Worked example — $T\,SO(3)$, bi-invariant base

Take $G=SO(3)$ with $\mathbb J=j\,\mathrm{id}$, so $\mathbb G$ is bi-invariant. [[06-curvature-left-invariant-metrics]] gives constant curvature $\kappa=1/(4j)$ — a round $\mathbb{RP}^3$ of radius $\rho=2\sqrt j$ — hence
$$R(X,Y)Z=\kappa\big(\langle Y,Z\rangle X-\langle X,Z\rangle Y\big).$$
(Check against the bracket form: with the frame $f_i$ of lesson 06, $\lambda_i=1/\sqrt j$, so $R(f_1,f_2)f_2=-\tfrac14[[f_1,f_2],f_2]=\tfrac14 f_1/j=\kappa f_1$. ✓)

Let $u\in\mathfrak{so}(3)$ be the left-trivialized velocity, $u=\hat\Omega$ with $\Omega$ the body angular velocity, so $\|u\|^2_{\mathbb I}=j|\Omega|^2$. For orthonormal $X,Y$ spanning $\sigma$,
$$R(X,Y)u=\kappa\big(\langle Y,u\rangle X-\langle X,u\rangle Y\big),\qquad
\big\|R(X,Y)u\big\|^2=\kappa^2\big\|P_\sigma u\big\|^2,$$
$P_\sigma$ the orthogonal projection onto $\sigma$. So the drop depends only on the component of the velocity lying *in the plane being measured*: a plane orthogonal to $u$ suffers nothing. The worst case is $u\in\sigma$, and there
$$\mathrm{Sec}\big(X^h,Y^h\big)=\kappa-\tfrac34\kappa^2\|u\|^2
=\frac{1}{4j}\Big(1-\frac{3\,|\Omega|^2}{16}\Big).$$

The $j$ cancels inside the bracket — the kinetic-energy metric makes $\|u\|^2$ scale like $j$ while $\kappa$ scales like $1/j$. So the sign change happens at a body rate that no choice of inertia can move:

$$\boxed{\ \mathrm{Sec}(X^h,Y^h)<0 \iff |\Omega|>\frac{4}{\sqrt3}\approx 2.31\ \mathrm{rad/s}\approx 22\ \mathrm{rpm}\ }$$

Twenty-two rpm. A hand-spun object clears it. In intrinsic terms the threshold is $\|u\|=2\rho/\sqrt3\approx1.15\,\rho$: once the trivialized speed exceeds the radius of curvature of the base per unit time, the Sasaki lift of a *positively curved* space has negatively curved horizontal planes.

## The sting

$\mathrm{Sec}(X^h,Y^h)$ decreases with $\|u\|$ and eventually goes negative whenever $R\neq0$, however positively curved the base is. Stack this against what is already known:

- [[06-curvature-left-invariant-metrics]] shows negative curvature is live on the **base** already, at $-\tfrac13$ for $\mathbb J=\mathrm{diag}(1,2,3)$ — no lifting required.
- [[00-study-plan]] lesson 17 records that negative curvature bounds any contraction region **in velocity**, through the tidal term $\mathrm{Jac}_v(u)=R(u,v)v$, and that damping does not repair it.

The Sasaki lift therefore does not fix that problem; it reproduces it one level up and makes it worse at speed, since the horizontal curvature degrades as $\|u\|^2$ exactly where the tidal term is already growing as $\|v\|^2$.

Flagging forward: [[00-study-plan]] lesson 16 shows that block-diagonal metrics on $TM$ — Sasaki and total-energy alike — cannot certify contraction **at all**, by a $\pm v$ symmetry argument that is independent of curvature. The cross-term $g$-natural metrics $a\|u\|^2+2b\langle u,\xi\rangle+c\|\xi\|^2$ exist for that reason.

:::warning[Open question — which metric on $TG$?]
On a Lie group there is a second natural metric on $TG$: $TG\cong G\ltimes\mathfrak g$ is itself a Lie group, and one can put a **left-invariant** metric on it built from *complete* lifts rather than horizontal ones. Its Levi-Civita connection carries extra $\mathrm{ad}^*$ terms that the Sasaki connection does not, and its curvature is not Kowalski's. So "the simple/natural metric on $TG$" is ambiguous — exactly the situation the repo's standing rule covers (cf. $\exp_G$ vs $\exp_p$ in [[notation]]). Any downstream bound must name which one it means. Open: whether the left-invariant lift has a better velocity dependence than $-\tfrac34\|R(X,Y)u\|^2$, or merely relocates the same defect.
:::

## Problems

1. **Recall.** State $g_S$ both ways (via $K$ and via the lift conditions). Write the three Kowalski sectional curvatures. Say which of the three is sensitive to the sign convention for $R$ and why the other two are not. Then say why $R(X,Y)u$ and $R(u,Y)X$ cannot be interchanged.

2. **Compute.** For $SO(3)$ with $\mathbb J=j\,\mathrm{id}$: show $\|R_u\|^2=4\kappa^2\|u\|^2$ and hence write $\mathrm{Scal}(T\,SO(3),g_S)$ as a function of $|\Omega|$. At what body rate does the *scalar* curvature of $T\,SO(3)$ turn negative? Compare it to the $4/\sqrt3$ above and explain the ordering.

3. **Prove.** (a) If $(TM,g_S)$ is flat then $(M,g)$ is flat — evaluate the horizontal formula on the zero section. (b) $(TM,g_S)$ never has constant sectional curvature $c\neq0$; this is one line. (c) If $R\neq0$ at $p$, show $\mathrm{Sec}(X^h,Y^h)$ is non-constant along the fibre over $p$, and say in one sentence why that makes item 2 of the rigidity theorem stronger than item 1.

4. **Break it.** One might hope that a positively curved base gives a positively curved $TM$ — "lift a good metric and keep the good property". Take $j=1$, so $SO(3)$ is round with $\mathrm{Sec}\equiv\tfrac14>0$ on *every* plane, strictly (lesson 06, Corollary). Exhibit a body angular velocity of magnitude $4$ rad/s and a plane $\sigma\ni u$, and compute $\mathrm{Sec}(X^h,Y^h)$. Then argue that no positively curved base can survive: the base term is fixed while the correction grows as $\|u\|^2$. State the moral in one sentence.

---

## Solutions

**1.** Definitions as stated. Only $\mathrm{Sec}(X^h,Y^h)$ is convention-sensitive, through its leading term $\mathrm{Sec}(X,Y)$; the correction terms $\|R(X,Y)u\|^2$ and $\|R(u,Y)X\|^2$ are squared norms, so a global sign flip $R\mapsto-R$, and equally a swap of the two antisymmetric slots, leaves them fixed. $R(X,Y)u$ and $R(u,Y)X$ are different contractions: the first has $u$ in the *acted-on* slot, the second in an antisymmetric slot. There is no symmetry of $\mathrm{Rm}$ carrying one to the other — (S4) relates $\mathrm{Rm}(X,Y,u,\cdot)$ to $\mathrm{Rm}(u,\cdot,X,Y)$, which is a different rearrangement again (and it is exactly that identity which produces the $\tfrac14$ in the scalar drop).

**2.** With $R(f_i,f_j)u=\kappa(u_jf_i-u_if_j)$ one gets $\|R(f_i,f_j)u\|^2=\kappa^2(u_i^2+u_j^2)$ for $i\neq j$ and $0$ for $i=j$. Summing over the six ordered pairs, $\|R_u\|^2=\kappa^2\sum_{i\neq j}(u_i^2+u_j^2)=\kappa^2\cdot2(n-1)\|u\|^2=4\kappa^2\|u\|^2$ at $n=3$. With $\mathrm{Scal}(M)=n(n-1)\kappa=6\kappa$,
$$\mathrm{Scal}(TM,g_S)=6\kappa-\kappa^2\|u\|^2=\frac{6}{4j}-\frac{j|\Omega|^2}{16j^2}=\frac1j\Big(\tfrac32-\tfrac{|\Omega|^2}{16}\Big),$$
again $j$-free in its sign. It vanishes at $|\Omega|=\sqrt{24}=2\sqrt6\approx4.90$ rad/s, roughly $47$ rpm — **later** than the $4/\sqrt3\approx2.31$ rad/s at which the worst horizontal plane flips. That ordering is forced: $\mathrm{Scal}$ averages over all $2n(2n-1)$ planes, most of which are vertical (identically $0$), mixed (non-negative), or horizontal planes nearly orthogonal to $u$ (small drop). The single worst plane goes negative long before the average does, and it is the worst plane, not the average, that enters a curvature-corrected stiffness.

**3.** (a) On the zero section $u=0$, so the correction vanishes and $\mathrm{Sec}(X^h,Y^h)=\mathrm{Sec}(X,Y)$ for every orthonormal pair in $T_pM$. Flatness of $TM$ forces all of these to be $0$, and sectional curvatures determine $R$ ([[05-riemann-tensor]], Proposition), so $R\equiv0$ on $M$. (b) Vertical planes have $\mathrm{Sec}(X^v,Y^v)=0$ at every point of $TM$ (for $n\ge2$ such planes exist everywhere), so constant curvature $c$ forces $c=0$. Hence $c\neq0$ is impossible. (c) If $R\neq0$ at $p$, pick $X,Y$ orthonormal with $R(X,Y)\neq0$ and $u_0$ with $R(X,Y)u_0\neq0$. Along $t\mapsto tu_0$ in the fibre, $\mathrm{Sec}(X^h,Y^h)=\mathrm{Sec}(X,Y)-\tfrac34t^2\|R(X,Y)u_0\|^2$ is a strictly decreasing non-constant function of $t^2$. A locally symmetric space has $\nabla\mathrm{Rm}=0$, so sectional curvature is invariant under parallel transport; the fibre direction here is a geodesic of $g_S$ (the fibres are totally geodesic and flat) along which the lifted plane is parallel, so non-constancy contradicts $\nabla\mathrm{Rm}=0$. Item 2 is stronger than item 1 because it rules out the entire class of locally symmetric metrics — including all the ones with $\mathrm{Sec}$ constant and negative, which is where one would go looking for a well-behaved $TM$ after item 4.

**4.** $j=1$ gives $\kappa=\tfrac14$. Take $\Omega=4e_1$, i.e. $u=4\hat e_1$, $\|u\|=4$, and $\sigma=\mathrm{span}(f_1,f_2)$ with $f_i=\hat e_i$, so $u=4f_1\in\sigma$. Then
$$\mathrm{Sec}(f_1^h,f_2^h)=\kappa-\tfrac34\kappa^2\|u\|^2=\tfrac14-\tfrac34\cdot\tfrac1{16}\cdot16=\tfrac14-\tfrac34=-\tfrac12 .$$
So a plane whose base curvature is $+\tfrac14$ lifts to a plane of curvature $-\tfrac12$: the sign is not merely lost, it is overshot by a factor of two, at a spin rate a person can produce by hand.

Nothing about positivity of the base helps. For any $(M,g)$ with $R\neq0$ at $p$, choose $X,Y$ with $R(X,Y)\neq0$ and $u$ in their span with $\|R(X,Y)u\|>0$; then $\mathrm{Sec}(X^h,Y^h)=\mathrm{Sec}(X,Y)-\tfrac34\|R(X,Y)u\|^2\to-\infty$ as $\|u\|\to\infty$, because the base term is a fixed number and the correction is quadratic. The only escape is $R\equiv0$, i.e. the flat case, which is rigidity item 1.

**Moral:** lifting a metric to $TM$ in the obvious way — same $g$ on both factors, no cross term — does not lift the property you wanted. It destroys it, quadratically in velocity, and the failure begins at speeds well inside the operating range of a tumbling rigid body.
