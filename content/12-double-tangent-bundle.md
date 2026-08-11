---
tags: [mechanics, bundles, connection, sode, spray, lie-groups]
---
# The Double Tangent Bundle, the Horizontal/Vertical Splitting, and Second-Order Systems

**Prereq:** [[mechanical-systems-on-lie-groups]], [[riemannian-geometry]] (bundles, sections, parallel transport), [[notation]], [[02-trivialization-of-tg]] (left trivialization $TG\cong G\times\mathfrak g$), [[03-levi-civita-left-invariant]] ($\nabla_\xi\xi=-\widetilde{\mathrm{ad}}_\xi\xi$), [[07-jacobi-equation]] (covariant differentiation of a field *along a map*)
**Goal:** know why a second-order system is a vector field on $TM$, split $T_v(TM)$ into horizontal and vertical with the connector $K$, and recognise the SODE condition $J\Gamma=\Delta$ — then read the Euler–Poincaré equations off it on a Lie group.

:::info[Resolution of an open question]
This lesson answers the open question in [[mechanical-systems-on-lie-groups]] § *Double tangent bundle*: **"How do vector fields on $TG$ translate to a second-order ODE on $TTG$?"** Short version: they do not, in general. A vector field on $TG$ is a section of $TTG\to TG$ and is only a second-order ODE on $G$ when its two projections to $TG$ agree — the condition $d\pi\circ\Gamma=\mathrm{id}$, equivalently $J\Gamma=\Delta$, of the theorem below. The vector fields that fail it are honest flows on the $2n$-manifold $TG$ but are not the velocity flow of anything on $G$.
:::

**Two notation clashes, resolved here and not again.** $\Gamma$ is the semispray field; $\Gamma^k_{ij}$ with indices are Christoffel symbols. And $\Delta$ is the Liouville field *in this lesson only* — in [[notation]] $\Delta$ is Laplace–Beltrami, which does not occur here.

## Why $TTM$

A vector field on $M$ assigns a velocity to each point: a section of $\pi:TM\to M$. A second-order system prescribes an **acceleration** as a function of position *and* velocity, so its state is a point of $TM$ and its right-hand side is a vector field on the manifold $TM$ — a section of $\pi_{TM}:TTM\to TM$. There is no way around the double tangent bundle.

The mental picture that makes $TTM$ readable: a vector $\xi\in T_v(TM)$ is the velocity at $s=0$ of a **moving vector**

$$s\longmapsto v(s)\in T_{\gamma(s)}M,\qquad \gamma(0)=q,\ v(0)=v,$$

a tangent vector whose foot point $\gamma(s)$ is itself moving. Such a motion carries two independent pieces of first-order data, and $TTM$ correspondingly has **two** projections onto $TM$:

- $\pi_{TM}:TTM\to TM$ returns $v$, the point of $TM$ we sit at. Automatic — no choice involved.
- $T\pi=d\pi:TTM\to TM$ returns $\dot\gamma(0)\in T_qM$: how fast the **foot point** is moving.

They need not agree, and everything below is the demand that they do.

## The connector and the splitting

$d\pi$ alone cannot split $T_v(TM)$. Its kernel — motions with a stationary foot point, so the vector merely slides inside the fixed fibre $T_qM$ — is the **vertical** subspace $V_v$, and it is canonical. A complement is not: it needs extra data, and the connection supplies it.

:::info[Definition]
The **connector** (connection map) of $\nabla$ is $K:TTM\to TM$,
$$K(\xi) \;=\; \frac{D v}{ds}\Big|_{s=0} \;=\; \nabla_{\dot\gamma}v\big|_{s=0}\;\in\;T_qM,$$
the covariant derivative *along the curve $\gamma$* of the moving vector $v(s)$ representing $\xi$ — the machinery of [[07-jacobi-equation]]. It is well defined (independent of the representing curve) because $\tfrac{D}{ds}$ depends on $v(s)$ only through its $1$-jet.
:::

:::tip[Proposition — the splitting]
$$T_v(TM) \;=\; H_v\oplus V_v,\qquad H_v=\ker K,\quad V_v=\ker d\pi,$$
and $\xi\mapsto(d\pi\,\xi,\,K\xi)$ is a linear isomorphism $T_v(TM)\xrightarrow{\ \sim\ }T_qM\oplus T_qM$. Restricted, $d\pi|_{H_v}$ and $K|_{V_v}$ are isomorphisms onto $T_qM$.
:::

In words: **horizontal** $=$ "the foot moves and the vector is parallel-transported along" ($K\xi=0$); **vertical** $=$ "the foot stays put and the vector slides" ($d\pi\,\xi=0$). Dimension count: $\dim T_v(TM)=2n$ and both maps are onto $T_qM$, so the isomorphism follows once $H_v\cap V_v=0$, which the coordinate formulas below make immediate.

**The asymmetry is the point.** $V_v$ is canonical — it exists on any vector bundle with no extra structure. $H_v$ is *the connection*, repackaged: a smoothly and linearly varying horizontal complement in $T(TM)$ is exactly the same data as $\nabla$. So the splitting is chart-independent but connection-dependent, and on a Lie group the two candidate splittings — Levi-Civita versus the flat $\nabla^-$ of [[notation]] — differ. Here it is Levi-Civita.

## Lifts, and the coordinate dictionary

Inverting the isomorphism gives the two **lifts** of $X\in T_qM$ to the point $v$:

$$X^h\in H_v:\ d\pi(X^h)=X,\ K(X^h)=0;
\qquad
X^v = \frac{d}{ds}\Big|_{0}(v+sX)\in V_v:\ d\pi(X^v)=0,\ K(X^v)=X.$$

Take coordinates $(x^i)$ on $M$ and the induced $(x^i,y^i)$ on $TM$, where the point $(x,y)$ **is** the vector $v=y^i\partial_{x^i}|_x$. A tangent vector to $TM$ is $a^i\partial_{x^i}+b^i\partial_{y^i}$, and

$$d\pi\big(a^i\partial_{x^i}+b^i\partial_{y^i}\big)=a^i\partial_{x^i},
\qquad
K\big(a^i\partial_{x^i}+b^i\partial_{y^i}\big)=\big(b^k+\Gamma^k_{ij}y^ia^j\big)\partial_{x^k},$$
$$(\partial_{x^i})^h = \partial_{x^i}-\Gamma^k_{ij}\,y^j\,\partial_{y^k},
\qquad
(\partial_{x^i})^v = \partial_{y^i}.$$

The Christoffel symbols appear in $K$ and in $X^h$ but *not* in $d\pi$ or in $X^v$ — exactly the statement that the vertical space is free and the horizontal one is bought with a connection.

:::info[Definition]
The **Liouville** (dilation, Euler) **field** is $\Delta_v = v^v$, the vertical lift of $v$ at $v$ itself; in coordinates $\Delta = y^i\partial_{y^i}$. Its flow is fibrewise scaling $v\mapsto e^sv$.

The **vertical endomorphism** $J:T(TM)\to T(TM)$ takes the horizontal shadow of a vector and reinjects it vertically, $J\xi=(d\pi\,\xi)^v$; in coordinates $J=\partial_{y^i}\otimes dx^i$, i.e. $J(a^i\partial_{x^i}+b^i\partial_{y^i})=a^i\partial_{y^i}$. Hence $JX^h=X^v$, $JX^v=0$, $J^2=0$.
:::

Both are canonical — $\Delta$ and $J$ need no connection, only the vector-space structure of the fibres. (Check: $J(\partial_{x^i})^h=J(\partial_{x^i}-\Gamma^k_{ij}y^j\partial_{y^k})=\partial_{y^i}=(\partial_{x^i})^v$, the Christoffels cancelling because $J$ kills $\partial_{y^k}$.)

## Second-order systems

:::tip[Theorem — SODE / semispray]
For a vector field $\Gamma$ on $TM$ the following are equivalent.

1. $d\pi\circ\Gamma=\mathrm{id}_{TM}$, i.e. the two projections of $TTM$ agree on $\Gamma$.
2. $J\Gamma=\Delta$.
3. In induced coordinates $\Gamma = y^i\partial_{x^i}+F^i(x,y)\,\partial_{y^i}$ for some $F$.

Such a $\Gamma$ is a **second-order differential equation** (SODE), or **semispray**. Its integral curves $V(s)$ satisfy $V=\dot\gamma$ for $\gamma=\pi\circ V$, so $\dot V=\Gamma(V)$ is the second-order equation $\ddot\gamma=F(\gamma,\dot\gamma)$ on $M$.
:::

*Proof.* (1)$\Leftrightarrow$(2): $J\Gamma(v)=(d\pi\,\Gamma(v))^v$ and $\Delta_v=v^v$; the vertical lift $T_qM\to V_v$ is injective, so $J\Gamma=\Delta$ iff $d\pi\,\Gamma(v)=v$ for every $v$. (1)$\Leftrightarrow$(3): writing $\Gamma=A^i\partial_{x^i}+F^i\partial_{y^i}$ gives $d\pi\,\Gamma=A^i\partial_{x^i}$, while the point $\Gamma$ sits at is $v=y^i\partial_{x^i}$; equality forces $A^i=y^i$ — the $\partial_{x^i}$-coefficients are not a modelling choice. Second order, unwound: let $\dot V=\Gamma(V)$ and $\gamma=\pi\circ V$, so that $\dot\gamma=d\pi(\dot V)=d\pi(\Gamma(V))\overset{(1)}{=}V$ and the curve in $TM$ **is the velocity of its own base projection**. In coordinates $\dot x^i=y^i$, $\dot y^i=F^i(x,y)$, i.e. $\ddot x^i=F^i(x,\dot x)$. $\square$

That is the whole content of the notes' open question: a general vector field on $TG$ gives $\dot x^i=A^i(x,y)$, $\dot y^i=F^i(x,y)$ — a first-order system on a $2n$-manifold, with $y$ an auxiliary variable bearing no relation to $\dot x$. Only when $A^i=y^i$ does $y$ deserve the name "velocity".

## Sprays

:::info[Definition]
A semispray $S$ is a **spray** if $F$ is homogeneous of degree $2$ in the fibre variable — quadratic in velocity. Invariantly, $[\Delta,S]=S$.
:::

The equivalence is Euler's homogeneity theorem: for $\Gamma=y^i\partial_{x^i}+F^k\partial_{y^k}$ one computes $[\Delta,\Gamma]=y^i\partial_{x^i}+(\Delta F^k-F^k)\partial_{y^k}$, so $[\Delta,\Gamma]=\Gamma$ iff $y^j\partial_{y^j}F^k=2F^k$. The model is the **geodesic spray** of $\nabla$,

$$S \;=\; y^i\partial_{x^i}-\Gamma^k_{ij}\,y^iy^j\,\partial_{y^k},$$

whose integral curves are $\ddot x^k+\Gamma^k_{ij}\dot x^i\dot x^j=0$. Invariantly $S(v)=v^h$: the geodesic spray at $v$ is the *horizontal* lift of $v$, just as $\Delta_v=v^v$ is the vertical one — the geodesic flow is the horizontal of the two things one can do with $v$ at $v$. Degree-$2$ homogeneity is exactly what makes geodesics closed under **affine** reparametrisation $t\mapsto ct+d$: rescaling $\dot\gamma$ by $c$ rescales the acceleration by $c^2$, which is what the equation demands.

Adding a potential or an external force changes only $F$, i.e. perturbs $\Gamma$ **vertically**, leaving $d\pi\circ\Gamma=\mathrm{id}$ untouched — so a forced mechanical system is still a genuine SODE, just no longer a spray once the force has a velocity-independent or linear-in-velocity part. Lesson 13 puts the Sasaki metric on $TM$ using this same splitting; this lesson is the splitting only.

## Worked example: the geodesic spray on a Lie group is Euler–Poincaré

Left-trivialise $TG\cong G\times\mathfrak g$ by $v\mapsto(g,\xi)$, $\xi=g^{-1}v$ ([[02-trivialization-of-tg]]). A vector field on $TG$ is then a pair

$$\Gamma(g,\xi)=\big(A(g,\xi),\,B(g,\xi)\big)\in T_gG\oplus\mathfrak g,$$

$A$ the motion of the foot point, $B$ that of the body velocity. Since $\pi(g,\xi)=g$ we have $d\pi\,\Gamma=A$, so the SODE condition $d\pi\circ\Gamma=\mathrm{id}_{TG}$ reads $A(g,\xi)=v=g\xi$ — i.e. $\dot g=g\xi$.

**The reconstruction equation *is* the SODE self-consistency condition.** It is not an extra modelling assumption and it is not dynamics; it is the statement that $\xi$ is entitled to be called a velocity, transported to $G\times\mathfrak g$ by the trivialization.

The dynamics is $B$, and the geodesic spray is the choice $K\Gamma=0$. Along a curve with body velocity $\xi(s)$ the trivialized covariant derivative of $g\xi$ is $g(\dot\xi+\nabla_\xi\xi)$ ([[03-levi-civita-left-invariant]]), so $K\Gamma=B+\nabla_\xi\xi=B-\widetilde{\mathrm{ad}}_\xi\xi$, and $K\Gamma=0$ gives $B=\widetilde{\mathrm{ad}}_\xi\xi=\mathbb I^{-1}\mathrm{ad}^*_\xi\mathbb I\xi$. So

$$S(g,\xi)=\big(g\xi,\ \mathbb I^{-1}\mathrm{ad}^*_\xi\mathbb I\xi\big),
\qquad\text{integral curves}\qquad
\dot g=g\xi,\quad \boxed{\ \mathbb I\dot\xi=\mathrm{ad}^*_\xi\mathbb I\xi\ }$$

— the **Euler–Poincaré / Euler–Arnold** equations ([[10-euler-poincare]]), here obtained purely as "the horizontal lift of $v$ at $v$, written in body coordinates". $B$ is quadratic in $\xi$ and $\Delta=(0,\xi)$ in this trivialization, so $[\Delta,S]=S$: it is a spray, as it must be. On $SO(3)$ with $\xi=\hat\Omega$, $\mathbb I=\mathbb J$: $\dot R=R\hat\Omega$, $\mathbb J\dot\Omega=\mathbb J\Omega\times\Omega$. A control torque $\tau$ adds $(0,\mathbb J^{-1}\tau)$ — vertical, so still a SODE.

**Which of the three kinds is this?** The splitting, $\Delta$, $J$ and the SODE condition are all intrinsic (kind 1) — $\Delta$ and $J$ need not even a connection. The Christoffel symbols in the coordinate formula for $K$ are kind 2: chart-dependent components assembling into the chart-free $\nabla$. No sup-norm enters, so nothing here contributes conservatism; the chart-dependence question reopens in lesson 13, where a *metric* on $TM$ is chosen.

## Problems

1. **Recall.** State the two projections $TTM\to TM$ and say which one is automatic. Define the connector $K$, the vertical and horizontal subspaces, the Liouville field and the vertical endomorphism. Which of these four objects require a connection and which do not? State the SODE condition in both forms.

2. **Compute.** In induced coordinates $(x^i,y^i)$: (a) verify $J S=\Delta$ for the geodesic spray $S=y^i\partial_{x^i}-\Gamma^k_{ij}y^iy^j\partial_{y^k}$, and verify $KS=0$ (so $S(v)=v^h$), using $\Gamma^k_{ij}=\Gamma^k_{ji}$. (b) For a general $\Gamma=y^i\partial_{x^i}+F^k(x,y)\partial_{y^k}$ compute $[\Delta,\Gamma]$ and deduce $[\Delta,\Gamma]=\Gamma\iff F$ is homogeneous of degree $2$ in $y$. (c) Confirm $[\Delta,S]=S$ for the geodesic spray directly.

3. **Prove.** (a) $J^2=0$, and $\ker J=\operatorname{im}J=V_v$. (b) $J\Delta=0$; deduce that a semispray is nowhere vertical, and in particular that $\Delta$ itself is never a semispray on a manifold of dimension $\ge1$. (c) Show that if $\Gamma_1,\Gamma_2$ are semisprays then $\Gamma_1-\Gamma_2$ is vertical, and conclude that the set of semisprays is an affine space modelled on vertical vector fields — this is the precise sense in which "forces act vertically".

4. **Break it.** On $M=\mathbb R^2$ with the flat connection ($\Gamma^k_{ij}=0$), so $TM=\mathbb R^2\times\mathbb R^2$ with coordinates $(x^1,x^2,y^1,y^2)$:
   (a) Let $X=\partial_{y^1}$. Show $X$ is a perfectly good complete vector field on $TM$, compute its integral curves, and show they violate $V=\dot\gamma$. Conclude that no second-order ODE on $M$ has these as its velocity curves. Which of the three equivalent SODE conditions fails, and how?
   (b) Let $Y=-y^i\partial_{x^i}$. Show $d\pi\circ Y=-\mathrm{id}\ne\mathrm{id}$, so $Y$ is not a semispray either, and identify what $Y$'s integral curves *do* look like — the failure here is not qualitative but a sign, which is exactly why "the two projections agree" has to be stated as an equality and not as "both are onto".
   (c) Now take the genuine semispray $\Gamma=y^i\partial_{x^i}-y^i\partial_{y^i}$ (linear drag). Show $[\Delta,\Gamma]\ne\Gamma$, so it is not a spray, and exhibit an affine reparametrisation $t=c\tau$ under which its solutions are not carried to solutions.

---

## Solutions

**1.** $\pi_{TM}(\xi)=v$ (the foot point of $\xi$ in $TM$) is automatic — it is just where $\xi$ lives. $d\pi=T\pi$ sends $\xi$ to $\dot\gamma(0)$, the velocity of the foot point of the moving vector. $K\xi=\nabla_{\dot\gamma}v|_0$; $V_v=\ker d\pi$, $H_v=\ker K$; $\Delta_v=v^v$; $J\xi=(d\pi\,\xi)^v$. Only $K$ — and therefore $H_v$ and the horizontal lift — needs a connection. $V_v$, $\Delta$, $J$, $d\pi$ and the vertical lift are canonical on any tangent (indeed vector) bundle. SODE: $d\pi\circ\Gamma=\mathrm{id}_{TM}$, equivalently $J\Gamma=\Delta$.

**2.** (a) $J$ reads off the $\partial_{x^i}$-coefficients and re-labels them as $\partial_{y^i}$-coefficients, so $JS=y^i\partial_{y^i}=\Delta$. For $K$: with $a^i=y^i$, $b^k=-\Gamma^k_{ij}y^iy^j$,
$KS=(b^k+\Gamma^k_{ij}y^ia^j)\partial_{x^k}=(-\Gamma^k_{ij}y^iy^j+\Gamma^k_{ij}y^iy^j)\partial_{x^k}=0$ (the second term is $\Gamma^k_{ml}y^my^l$ after relabelling, equal to the first by symmetry of $\Gamma^k_{ml}$). Together with $d\pi\,S=y^i\partial_{x^i}=v$ this says $S(v)=v^h$.
(b) $\Delta=y^a\partial_{y^a}$ has coefficients $(0,y^k)$ and $\Gamma$ has $(y^i,F^k)$, so with $\Gamma(y^k)=F^k$,
$$[\Delta,\Gamma]=\big(\Delta(y^i)-\Gamma(0)\big)\partial_{x^i}+\big(\Delta(F^k)-\Gamma(y^k)\big)\partial_{y^k}=y^i\partial_{x^i}+\big(y^a\partial_{y^a}F^k-F^k\big)\partial_{y^k}.$$
Since the $\partial_{x^i}$-parts already agree, $[\Delta,\Gamma]=\Gamma$ iff $y^a\partial_{y^a}F^k=2F^k$, which by Euler's theorem is homogeneity of degree $2$.
(c) $F^k=-\Gamma^k_{ij}y^iy^j$ is a quadratic form in $y$, so $y^a\partial_{y^a}F^k=2F^k$ and $[\Delta,S]=S$.

**3.** (a) $J\xi=(d\pi\,\xi)^v$ is vertical, and $d\pi$ annihilates vertical vectors, so $J(J\xi)=(d\pi\,J\xi)^v=0^v=0$. $\operatorname{im}J\subseteq V_v$; conversely any $W\in V_v$ is $X^v$ for $X=K W$, and $X^v=J(X^h)$, so $\operatorname{im}J=V_v$. And $J\xi=0$ iff $(d\pi\,\xi)^v=0$ iff $d\pi\,\xi=0$ (vertical lift is injective) iff $\xi\in V_v$.
(b) $\Delta$ is vertical, so $J\Delta=0$ by (a). If $\Gamma$ were vertical at some $v\ne0$ then $J\Gamma=0\ne\Delta_v$, contradicting $J\Gamma=\Delta$; equivalently $d\pi\,\Gamma(v)=v\ne0$ shows $\Gamma(v)\notin V_v$. For $\Delta$ itself: $J\Delta=0\ne\Delta$ wherever $v\ne0$.
(c) $d\pi(\Gamma_1-\Gamma_2)=\mathrm{id}-\mathrm{id}=0$, so the difference lies in $\ker d\pi=V$. Conversely if $\Gamma$ is a semispray and $Z$ is vertical then $d\pi(\Gamma+Z)=\mathrm{id}$, so $\Gamma+Z$ is a semispray. Hence the semisprays form an affine space over the vector space of vertical fields — in coordinates, $F^i$ is arbitrary while $A^i=y^i$ is fixed. Adding a potential gradient or a control force adds a vertical field; that is why forcing never destroys second-orderness.

**4.** (a) $X=\partial_{y^1}$ is a constant coefficient field on $\mathbb R^4$, complete, with flow $(x^1,x^2,y^1,y^2)\mapsto(x^1,x^2,y^1+s,y^2)$. So the curve in $TM$ is $V(s)=\big(x_0,\,(y^1_0+s,y^2_0)\big)$ and its base projection is $\gamma(s)\equiv x_0$, giving $\dot\gamma=0$. But $V(s)\ne0$ as soon as $y_0\ne0$, so $V\ne\dot\gamma$: the "velocity" coordinate evolves while the point does not move. Condition (1) fails as $d\pi\,X=0\ne\mathrm{id}$; equivalently (3) fails because the $\partial_{x^i}$-coefficients are $0$ rather than $y^i$; equivalently (2) fails because $JX=0\ne\Delta$. Since $\gamma$ is constant, any second-order ODE on $M$ with this base curve would force $\dot\gamma\equiv0$, so no $F$ reproduces the flow — $X$ is a flow on $TM$ but not the velocity flow of anything on $M$.
(b) $d\pi\,Y=-y^i\partial_{x^i}=-v$, so $d\pi\circ Y=-\mathrm{id}$: onto, and an isomorphism at every point, yet not the identity. Integral curves: $\dot y=0$ so $y\equiv y_0$, and $\dot x=-y_0$, giving $x(s)=x_0-sy_0$. The base curve is a straight line with velocity $-y_0$ while the fibre coordinate reads $+y_0$ — the state is *minus* the velocity of its own base curve. Reversing the sign of $y$ would fix it, but the vector field as written is not a semispray, and the theorem's proof used the equality $A^i=y^i$, not merely invertibility of $A$. (Equivalently, $JY=-y^i\partial_{y^i}=-\Delta\ne\Delta$.)
(c) $F^k=-y^k$ is homogeneous of degree $1$, so by 2(b) $[\Delta,\Gamma]=y^i\partial_{x^i}+(-y^k+y^k)\partial_{y^k}=y^i\partial_{x^i}\ne\Gamma$ (they differ by the nonzero vertical field $-y^i\partial_{y^i}$). The base equation is $\ddot x=-\dot x$. Put $t=c\tau$ and $\tilde x(\tau)=x(c\tau)$: then $\tilde x''=c^2\ddot x=-c^2\dot x=-c\,\tilde x'$, which is $\ddot{\tilde x}=-c\,\tilde x'$ — the same equation only if $c=1$. So $x(t)=x_0+y_0(1-e^{-t})$ reparametrised is not a solution: linear damping picks out a preferred time scale, which is exactly what degree-$2$ homogeneity forbids. Geodesics have no such scale, which is why "geodesic" is a property of the unparametrised curve plus an affine parameter.
