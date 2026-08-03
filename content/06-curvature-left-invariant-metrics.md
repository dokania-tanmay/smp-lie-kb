---
tags: [curvature, lie-groups, left-invariant-metrics, so3]
---
# Curvature of Left-Invariant Metrics

**Prereq:** [[03-levi-civita-left-invariant]], [[05-riemann-tensor]], [[riemannian-geometry]], [[notation]]
**Goal:** compute the sectional curvature of a left-invariant metric from bracket data on $\mathfrak g$ alone, and exhibit a physically realisable rigid body whose configuration space has a negative sectional curvature.

## Why this is algebra, not analysis

A left-invariant metric is one inner product $\langle\cdot,\cdot\rangle_{\mathbb I}$ on $\mathfrak g$, translated everywhere. Lesson 03 turned that into a connection with **no derivatives left in it**,

$$\nabla_\xi\eta \;=\; \tfrac12\big([\xi,\eta] - \widetilde{\mathrm{ad}}_\xi\eta - \widetilde{\mathrm{ad}}_\eta\xi\big),
\qquad \widetilde{\mathrm{ad}}_\xi=\mathbb I^{-1}\mathrm{ad}^*_\xi\mathbb I ,$$

valid on left-invariant fields $\xi,\eta\in\mathfrak g$. Feeding this into the definition of $R$ from [[05-riemann-tensor]] gives a **bilinear expression in the structure constants**: curvature of a left-invariant metric is a finite algebraic computation on an $n$-dimensional vector space. No PDE, no chart, no Christoffel symbols.

That is a small instance of the project's thesis. The chart-dependent route to the same number would go through $\sup|\partial^2 g_{ij}|$ and produce a constant that depends on the chart; the intrinsic route produces the curvature itself, exactly, from the bracket.

The one identity used throughout — unfold the definition of $\mathrm{ad}^*$:

$$\big\langle \widetilde{\mathrm{ad}}_\xi\eta,\ \zeta\big\rangle_{\mathbb I} \;=\; \big\langle \eta,\ [\xi,\zeta]\big\rangle_{\mathbb I}
\qquad\text{for all }\xi,\eta,\zeta\in\mathfrak g. \tag{$\star$}$$

## The bi-invariant case, in full

:::info[Definition]
$\langle\cdot,\cdot\rangle_{\mathbb I}$ is **$\mathrm{Ad}$-invariant** (equivalently the metric $\mathbb G$ is bi-invariant) when every $\mathrm{ad}_\xi$ is skew-adjoint:
$$\big\langle[\xi,\eta],\zeta\big\rangle_{\mathbb I} + \big\langle\eta,[\xi,\zeta]\big\rangle_{\mathbb I} = 0 .$$
By $(\star)$ this says exactly $\widetilde{\mathrm{ad}}_\xi = -\mathrm{ad}_\xi$.
:::

Substituting $\widetilde{\mathrm{ad}}_\xi\eta=-[\xi,\eta]$ into the connection collapses it:
$\nabla_XY=\tfrac12([X,Y]+[X,Y]+[Y,X])=\tfrac12[X,Y]$.

:::tip[Theorem]
For a bi-invariant metric and $X,Y,Z\in\mathfrak g$,
$$\nabla_XY=\tfrac12[X,Y],\qquad R(X,Y)Z=-\tfrac14\big[[X,Y],Z\big],\qquad
\boxed{\ \mathrm{Sec}(X,Y)=\tfrac14\big\|[X,Y]\big\|^2_{\mathbb I}\ }$$
the last for $X,Y$ orthonormal.
:::

*Proof.* With $\nabla_XY=\tfrac12[X,Y]$,
$$R(X,Y)Z=\tfrac14\big[X,[Y,Z]\big]-\tfrac14\big[Y,[X,Z]\big]-\tfrac12\big[[X,Y],Z\big].$$
Jacobi gives $[X,[Y,Z]]-[Y,[X,Z]]=[[X,Y],Z]$, so the first two terms are $\tfrac14[[X,Y],Z]$ and the total is $-\tfrac14[[X,Y],Z]$. Now put $Z=Y$ and write $A=[X,Y]$. Skewness of $\mathrm{ad}_Y$ gives $\langle[Y,A],X\rangle=-\langle A,[Y,X]\rangle=\|A\|^2$, hence $\langle[A,Y],X\rangle=-\|A\|^2$ and
$\langle R(X,Y)Y,X\rangle=-\tfrac14\langle[A,Y],X\rangle=\tfrac14\|A\|^2$. The denominator of $\mathrm{Sec}$ is $1$ for an orthonormal pair. $\square$

:::tip[Corollary]
A bi-invariant metric has $\mathrm{Sec}\ge0$ everywhere, and $\mathrm{Sec}(X,Y)=0$ **iff** $[X,Y]=0$. So the flat 2-planes are exactly those spanned by commuting pairs, and $(G,\mathbb G)$ is flat iff $\mathfrak g$ is abelian. On $SO(3)$ every abelian subalgebra is $1$-dimensional, so the curvature is *strictly* positive.
:::

## The general left-invariant case — stated, not proved

Split the connection into its antisymmetric and symmetric parts, $\nabla_XY=\tfrac12[X,Y]+U(X,Y)$ with
$U(X,Y)=-\tfrac12(\widetilde{\mathrm{ad}}_XY+\widetilde{\mathrm{ad}}_YX)$. Bi-invariance is precisely $U\equiv0$.

:::tip[Proposition]
For any left-invariant metric and orthonormal $X,Y\in\mathfrak g$,
$$\mathrm{Sec}(X,Y)=\|U(X,Y)\|^2-\big\langle U(X,X),U(Y,Y)\big\rangle-\tfrac34\big\|[X,Y]\big\|^2
-\tfrac12\big\langle[[X,Y],Y],X\big\rangle-\tfrac12\big\langle[[Y,X],X],Y\big\rangle .$$
:::

This is **stated, not derived**. The derivation is expanding $\nabla_X\nabla_YY-\nabla_Y\nabla_XY-\nabla_{[X,Y]}Y$ with the split connection and repeatedly applying $(\star)$ — mechanical, about two pages, and it teaches nothing that the bi-invariant proof above did not. Setting $U=0$ recovers $\tfrac14\|[X,Y]\|^2$ (each of the last two brackets contributes $-\|[X,Y]\|^2$), which is the check worth doing.

The point that survives: **$\|U(X,Y)\|^2$ enters with a $+$ sign but $-\langle U(X,X),U(Y,Y)\rangle$ with a $-$, and there is nothing forcing the total to be non-negative.** Once bi-invariance fails, sectional curvatures can go negative.

## Worked example — $SO(3)$, both inertias

Use the notation contract: $\langle\hat a,\hat b\rangle_{\mathbb I}=a^\top\mathbb J\,b$ and $[\hat a,\hat b]=\widehat{a\times b}$. Orthonormal frame $f_i=\hat e_i/\sqrt{J_i}$, giving structure constants

$$[f_1,f_2]=\lambda_3 f_3,\quad [f_2,f_3]=\lambda_1 f_1,\quad [f_3,f_1]=\lambda_2 f_2,
\qquad \lambda_i=\frac{J_i}{\sqrt{J_1J_2J_3}} .$$

### (a) $\mathbb J=j\,\mathrm{id}$ — bi-invariant

$\mathrm{Ad}$-invariance holds because $a\!\cdot\!(b\times c)$ is fully antisymmetric. Take $X=f_1,Y=f_2$: $[X,Y]=\hat e_3/j$, so $\|[X,Y]\|^2_{\mathbb I}=j\cdot|e_3/j|^2=1/j$ and

$$\mathrm{Sec}=\tfrac14\cdot\tfrac1j=\frac{1}{4j}\quad\text{— the same for every plane.}$$

Constant positive curvature $1/(4j)$, i.e. $SO(3)$ is $\mathbb{RP}^3$ carrying the round metric of radius $2\sqrt j$. Sanity check without curvature: the closed geodesic $t\mapsto\exp_G(t\hat a)$, $|a|=1$, $t\in[0,2\pi]$ has length $2\pi\sqrt j$; closed geodesics of $\mathbb{RP}^3$ at radius $\rho$ have length $\pi\rho$, giving $\rho=2\sqrt j$ and $1/\rho^2=1/(4j)$. ✓

### (b) $\mathbb J=\mathrm{diag}(J_1,J_2,J_3)$ — asymmetric

Write $\mu_1=\tfrac12(-\lambda_1+\lambda_2+\lambda_3)$ and cyclically. Computing $\nabla$ in the frame $\{f_i\}$ gives the cyclic pattern $\nabla_{f_1}f_1=0$, $\nabla_{f_1}f_2=\mu_1f_3$, $\nabla_{f_2}f_3=\mu_2f_1$, $\nabla_{f_3}f_1=\mu_3f_2$ (each $f_i$ is a geodesic direction — the principal axes). Then

$$R(f_1,f_2)f_2=-\nabla_{f_2}(\mu_1f_3)-\nabla_{\lambda_3f_3}f_2=\big(\lambda_3\mu_3-\mu_1\mu_2\big)f_1,$$

$$\boxed{\ \mathrm{Sec}(f_1,f_2)=\lambda_3\mu_3-\mu_1\mu_2
=\frac{2J_3(J_1+J_2)-3J_3^2+(J_1-J_2)^2}{4\,J_1J_2J_3}\ }$$

with the other two planes obtained by cycling $J_1\to J_2\to J_3\to J_1$. (This is Milnor's normal form for $3$-dimensional unimodular groups; the Ricci check $\mathrm{Ric}(f_1)=2\mu_2\mu_3$ holds.)

**Take $\mathbb J=\mathrm{diag}(1,2,3)$.** Then $\sqrt{J_1J_2J_3}=\sqrt6$ and $\lambda=(1,2,3)/\sqrt6$, so $\mu_1=2/\sqrt6$, $\mu_2=1/\sqrt6$, $\mu_3=0$, and

$$\mathrm{Sec}(f_1,f_2)=0-\tfrac{2}{\sqrt6}\cdot\tfrac{1}{\sqrt6}=-\tfrac13,
\qquad \mathrm{Sec}(f_2,f_3)=\mathrm{Sec}(f_3,f_1)=+\tfrac13 .$$

The plane spanned by the two axes of *smallest* inertia is **negatively curved**, exactly $-1/3$. And $\mathbb J=\mathrm{diag}(1,2,3)$ satisfies the inertia triangle inequality $J_3\le J_1+J_2$ with equality — it is a genuine flat lamina, not a fictitious body. Asymmetric inertia is not an edge case.

:::warning[Open question]
Downstream this is the whole difficulty. The tidal operator $\mathrm{Jac}_v(u)=R(u,v)v$ scales as $\mathrm{Sec}\cdot\|v\|^2$, so a negative sectional curvature contributes a *destabilising* term growing with the square of the body angular velocity — it bounds any contraction region **in velocity**, and damping does not remove it (study plan lesson 17). It also flips the direction of Hessian comparison for $d(\cdot,\bar x)^2$, which is the constant meant to replace [[@daniObserverDesignStochastic2015]]'s $\bar m_{x^2}$. Open: whether the intrinsic bound on $SO(3)$ with $\mathbb J=\mathrm{diag}(1,2,3)$ is actually tighter than Dani's chart-dependent one, given that the curvature it must absorb is genuinely negative rather than merely conservatively estimated.
:::

## Problems

1. **Recall.** State the definition of $\widetilde{\mathrm{ad}}$ from [[notation]] and prove $(\star)$. Then show bi-invariance $\iff\widetilde{\mathrm{ad}}_\xi=-\mathrm{ad}_\xi$ for all $\xi$, and deduce $\nabla_\xi\xi=0$ in that case.

2. **Compute.** For $SO(3)$ with $\mathbb J=\mathrm{diag}(1,1,2)$: find $\lambda_1,\lambda_2,\lambda_3$ and $\mu_1,\mu_2,\mu_3$, then all three principal sectional curvatures from $\mathrm{Sec}(f_1,f_2)=\lambda_3\mu_3-\mu_1\mu_2$ and its cyclic images. Which plane is negative, and is this body physical?

3. **Prove.** Let $\mathbb G$ be bi-invariant. Show $R\equiv0$ iff $\mathfrak g$ is abelian, using only the boxed bi-invariant theorem. Then show that on a bi-invariant $G$ a $2$-plane $\mathrm{span}(X,Y)\subset\mathfrak g$ has $\mathrm{Sec}=0$ iff it is an abelian subalgebra, and conclude that $SO(3)$ with any bi-invariant metric has no flat planes at all.

4. **Break it.** A physical rigid body must satisfy $J_3\le J_1+J_2$. One might hope that this rules out negative curvature. Set $J_1=J_2=1$ and $J_3=J$; use the boxed closed form to get $\mathrm{Sec}(f_1,f_2)$ as a function of $J$, find the threshold at which it turns negative, and compare it to the physical ceiling $J\le2$. What fraction of the physically admissible range is negatively curved? State in one sentence what this costs in a contraction estimate.

---

## Solutions

**1.** $\widetilde{\mathrm{ad}}_\xi=\mathbb I^{-1}\mathrm{ad}^*_\xi\mathbb I$. Then
$\langle\widetilde{\mathrm{ad}}_\xi\eta,\zeta\rangle_{\mathbb I}=\langle\mathbb I\widetilde{\mathrm{ad}}_\xi\eta,\zeta\rangle=\langle\mathrm{ad}^*_\xi\mathbb I\eta,\zeta\rangle=\langle\mathbb I\eta,\mathrm{ad}_\xi\zeta\rangle=\langle\eta,[\xi,\zeta]\rangle_{\mathbb I}$,
using the plain-dual definition of $\mathrm{ad}^*$ and symmetry of $\mathbb I$. Bi-invariance says $\langle\eta,[\xi,\zeta]\rangle=-\langle[\xi,\eta],\zeta\rangle$ for all $\zeta$, i.e. $\widetilde{\mathrm{ad}}_\xi\eta=-[\xi,\eta]$. Then $\nabla_\xi\xi=\tfrac12(0+[\xi,\xi]+[\xi,\xi])=0$; equivalently $\nabla_\xi\xi=\tfrac12[\xi,\xi]=0$ from the collapsed connection. This is why $\exp_G=\exp_e$ exactly in the bi-invariant case.

**2.** $\sqrt{J_1J_2J_3}=\sqrt2$, so $\lambda=(1,1,2)/\sqrt2$. Then
$\mu_1=\tfrac12(-1+1+2)/\sqrt2=1/\sqrt2$, $\mu_2=\tfrac12(1-1+2)/\sqrt2=1/\sqrt2$, $\mu_3=\tfrac12(1+1-2)/\sqrt2=0$.
$\mathrm{Sec}(f_1,f_2)=\lambda_3\mu_3-\mu_1\mu_2=0-\tfrac12=-\tfrac12$.
$\mathrm{Sec}(f_2,f_3)=\lambda_1\mu_1-\mu_2\mu_3=\tfrac1{\sqrt2}\cdot\tfrac1{\sqrt2}-0=+\tfrac12$.
$\mathrm{Sec}(f_3,f_1)=\lambda_2\mu_2-\mu_3\mu_1=+\tfrac12$.
The $(f_1,f_2)$ plane — the two equal, smaller inertias — is negative. $J_3=2=J_1+J_2$, so the body is physical (a uniform disc about its symmetry axis). Note it is axially symmetric yet still not bi-invariant: only $\mathbb J=j\,\mathrm{id}$ is.

**3.** If $\mathfrak g$ is abelian then $[X,Y]=0$ so $R(X,Y)Z=-\tfrac14[[X,Y],Z]=0$. Conversely if $R\equiv0$ then for orthonormal $X,Y$, $0=\langle R(X,Y)Y,X\rangle=\tfrac14\|[X,Y]\|^2$, so $[X,Y]=0$; bilinearity extends this to all pairs, so $\mathfrak g$ is abelian. For a single plane, $\mathrm{Sec}(X,Y)=\tfrac14\|[X,Y]\|^2=0\iff[X,Y]=0$, which for a $2$-plane is exactly the statement that it is closed under the bracket with trivial bracket, i.e. an abelian subalgebra. In $\mathfrak{so}(3)$, $[\hat a,\hat b]=\widehat{a\times b}=0$ forces $a\parallel b$, so no two independent elements commute: every abelian subalgebra is at most $1$-dimensional and no flat $2$-plane exists. Hence $\mathrm{Sec}>0$ strictly.

**4.** With $J_1=J_2=1$, $J_3=J$ the closed form gives
$$\mathrm{Sec}(f_1,f_2)=\frac{2J(1+1)-3J^2+0}{4J}=\frac{4J-3J^2}{4J}=1-\tfrac34 J .$$
This is negative iff $J>4/3$. The physical ceiling is $J\le J_1+J_2=2$. So the negatively curved band is $J\in(4/3,\,2]$ — and since the admissible range is $J\in(0,2]$, a third of it is negatively curved, with the worst value $\mathrm{Sec}=-\tfrac12$ attained at the lamina $J=2$. The triangle inequality does **not** rule out negative curvature.

Cost: the tidal term $\mathrm{Jac}_v(u)=R(u,v)v$ then contributes $\mathrm{Sec}\cdot\|v\|^2\le-\tfrac12\|v\|^2$ on that plane, an anti-restoring term growing quadratically in body angular velocity, so any curvature-corrected stiffness $\mathcal S=\mathrm{Hess}^\sharp V+\mathrm{Jac}_v$ loses positive-definiteness above a finite speed — the contraction region is bounded **in velocity** no matter how much damping is added.
