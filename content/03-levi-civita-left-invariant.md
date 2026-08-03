---
tags: [lie-groups, riemannian, connections, so3, se3]
---
# Levi-Civita Connection of a Left-Invariant Metric

**Prereq:** [[01-adjoint-and-coadjoint]], [[riemannian-geometry]], [[notation]]
**Goal:** compute $\nabla$ for a left-invariant metric using only the bracket and $\mathbb I$, and read off exactly when the Lie exponential and the Riemannian exponential agree.

## Setup and definitions

$G$ is a matrix Lie group, $\mathbb I:\mathfrak g\to\mathfrak g^*$ symmetric positive-definite, $\langle\xi,\eta\rangle_{\mathbb I}=\langle\mathbb I\xi,\eta\rangle$, and $\mathbb G$ the left-invariant metric it generates. Write $\nabla_\xi\eta$ for the algebra element with $\nabla_{X_\xi}X_\eta=X_{\nabla_\xi\eta}$ — legitimate because the answer will turn out to be left-invariant.

:::info[Definition]
The **metric adjoint** is $\widetilde{\mathrm{ad}}_\xi=\mathbb I^{-1}\mathrm{ad}^*_\xi\mathbb I:\mathfrak g\to\mathfrak g$. Unwinding the plain-dual definition of $\mathrm{ad}^*$ from [[01-adjoint-and-coadjoint]],

$$\langle\widetilde{\mathrm{ad}}_\xi\eta,\zeta\rangle_{\mathbb I}=\langle\mathrm{ad}^*_\xi\mathbb I\eta,\zeta\rangle=\langle\mathbb I\eta,\mathrm{ad}_\xi\zeta\rangle=\langle\eta,[\xi,\zeta]\rangle_{\mathbb I}.$$

So $\widetilde{\mathrm{ad}}_\xi$ is precisely **the adjoint of $\mathrm{ad}_\xi$ with respect to $\langle\cdot,\cdot\rangle_{\mathbb I}$**. Unlike $\mathrm{ad}^*$, it needs the metric; unlike $\mathrm{ad}$, it is not a bracket.
:::

## The computation

:::tip[Theorem]
For $\xi,\eta\in\mathfrak g$ and the left-invariant metric $\mathbb G$,

$$\nabla_\xi\eta=\tfrac12\big([\xi,\eta]-\widetilde{\mathrm{ad}}_\xi\eta-\widetilde{\mathrm{ad}}_\eta\xi\big),
\qquad\text{hence}\qquad
\nabla_\xi\xi=-\widetilde{\mathrm{ad}}_\xi\xi .$$
:::

*Proof.* Koszul, valid for any Levi-Civita connection:

$$2\langle\nabla_XY,Z\rangle=X\langle Y,Z\rangle+Y\langle Z,X\rangle-Z\langle X,Y\rangle+\langle[X,Y],Z\rangle-\langle[X,Z],Y\rangle-\langle[Y,Z],X\rangle.$$

Take $X=X_\xi$, $Y=X_\eta$, $Z=X_\zeta$ left-invariant. The function $g\mapsto\mathbb G(X_\eta,X_\zeta)|_g=\langle g^{-1}g\eta,g^{-1}g\zeta\rangle_{\mathbb I}=\langle\eta,\zeta\rangle_{\mathbb I}$ is **constant on $G$** — that is what left-invariance buys — and likewise for the other two pairings. So all three derivative terms are derivatives of constants and vanish. What is left is bracket terms only, and $[X_\xi,X_\eta]=X_{[\xi,\eta]}$:

$$2\langle\nabla_\xi\eta,\zeta\rangle_{\mathbb I}=\langle[\xi,\eta],\zeta\rangle_{\mathbb I}-\langle[\xi,\zeta],\eta\rangle_{\mathbb I}-\langle[\eta,\zeta],\xi\rangle_{\mathbb I}.$$

By the definition above, $\langle[\xi,\zeta],\eta\rangle_{\mathbb I}=\langle\eta,[\xi,\zeta]\rangle_{\mathbb I}=\langle\widetilde{\mathrm{ad}}_\xi\eta,\zeta\rangle_{\mathbb I}$ and $\langle[\eta,\zeta],\xi\rangle_{\mathbb I}=\langle\widetilde{\mathrm{ad}}_\eta\xi,\zeta\rangle_{\mathbb I}$. Since $\zeta$ is arbitrary and $\langle\cdot,\cdot\rangle_{\mathbb I}$ is non-degenerate, the claim follows; $\eta=\xi$ kills the bracket and doubles the rest. $\square$

The right-hand side is built from $[\cdot,\cdot]$ and $\mathbb I$ alone. No Christoffel symbols, no $\partial g_{ij}$: the three terms that would have carried chart-dependent metric derivatives are identically zero, not merely bounded. This is the model case for what the project wants everywhere — an estimate whose constants are algebraic rather than sup-norms of $\partial g$.

Cross-check: [[@leeGeometricInterpretationBrownian2025]] eq. (48) records the same Koszul computation as $\nabla_{E_i}E_i=-g\,\mathrm{ad}^*_{e_i}e_i$. That paper identifies $\mathfrak g^*\cong\mathfrak g$ through the inner product, so its $\mathrm{ad}^*$ **is** our $\widetilde{\mathrm{ad}}$; with an orthonormal $\{e_i\}$ (so $\mathbb I=\mathrm{id}$ in that basis) the two statements are the same equation.

## The payoff: when do the two exponentials agree?

:::tip[Corollary]
If $\langle\cdot,\cdot\rangle_{\mathbb I}$ is $\mathrm{Ad}$-invariant (i.e. $\mathbb G$ is **bi-invariant**), then $\mathrm{ad}_\xi$ is skew-adjoint, so $\widetilde{\mathrm{ad}}_\xi=-\mathrm{ad}_\xi$, hence $\widetilde{\mathrm{ad}}_\xi\eta=-[\xi,\eta]=-\widetilde{\mathrm{ad}}_\eta\xi$ and

$$\nabla_\xi\eta=\tfrac12[\xi,\eta],\qquad \nabla_\xi\xi=0 .$$

So every one-parameter subgroup $t\mapsto\exp_G(t\xi)$ is a geodesic, and $\exp_G=\exp_e$ on $\mathfrak g$: **the Lie exponential and the Riemannian exponential coincide.**
:::

Without bi-invariance $\nabla_\xi\xi=-\widetilde{\mathrm{ad}}_\xi\xi\neq0$ in general, and then $\exp_G(t\xi)$ is *not* a geodesic. Differentiating $\mathbb G$-parallel transport of $\dot g=g\xi(t)$ in the left-invariant frame gives $\tfrac{D\dot g}{dt}=g\,(\dot\xi+\nabla_\xi\xi)$, so the geodesic equation is the **Euler–Arnold equation**

$$\dot\xi=\widetilde{\mathrm{ad}}_\xi\xi ,$$

and $\exp_G(t\xi)=\exp_e(t\xi)$ for all $t$ exactly when $\widetilde{\mathrm{ad}}_\xi\xi=0$.

:::info[Resolution of an open question]
This answers the open question in [[riemannian-geometry]] § *Exp and log: two sources* ("how far apart are the two exponentials, and is the gap controlled by the failure of $\mathrm{Ad}$-invariance?"). The gap is generated by $\widetilde{\mathrm{ad}}_\xi\xi$, which is exactly the symmetric part of $\mathrm{ad}_\xi$ — the infinitesimal failure of $\mathrm{Ad}$-invariance. It is the initial acceleration of $\exp_G(t\xi)$ measured against the geodesic with the same initial velocity: $\|\widetilde{\mathrm{ad}}_\xi\xi\|_{\mathbb I}$ is the leading coefficient of the discrepancy, $d\big(\exp_G(t\xi),\exp_e(t\xi)\big)=\tfrac12t^2\|\widetilde{\mathrm{ad}}_\xi\xi\|_{\mathbb I}+O(t^3)$. A bound uniform in $t$ needs curvature and is not settled here.
:::

## Worked example — $SO(3)$, both cases

Identify $\mathfrak{so}(3)\cong\mathbb R^3$ by $\hat{\cdot}$, so $[\hat a,\hat b]=\widehat{a\times b}$, and let $\langle\hat a,\hat b\rangle_{\mathbb J}=a^\top\mathbb J b$ ($\mathbb J=\mathrm{id}$ recovers $\tfrac12\mathrm{tr}(\eta^\top\zeta)$ from [[notation]]). Then for all $c$,

$$c^\top\mathbb J\,\widetilde{\mathrm{ad}}_ab=\langle\widetilde{\mathrm{ad}}_ab,c\rangle_{\mathbb J}=\langle b,a\times c\rangle_{\mathbb J}=(\mathbb Jb)^\top(a\times c)=c^\top\big((\mathbb Jb)\times a\big),$$

using the triple product $u\cdot(a\times c)=c\cdot(u\times a)$. Hence

$$\boxed{\ \widetilde{\mathrm{ad}}_ab=-\mathbb J^{-1}\big(a\times\mathbb Jb\big),\qquad \nabla_\Omega\Omega=-\widetilde{\mathrm{ad}}_\Omega\Omega=\mathbb J^{-1}\big(\Omega\times\mathbb J\Omega\big).\ }$$

**Bi-invariant case, $\mathbb J=j\,\mathrm{id}$.** Then $\widetilde{\mathrm{ad}}_ab=-\tfrac1j(a\times jb)=-a\times b=-[a,b]$: skew, as the corollary demands. So $\widetilde{\mathrm{ad}}_\Omega\Omega=-\Omega\times\Omega=0$ and $\nabla_\Omega\Omega=0$ for every $\Omega$. Every rotation about a fixed axis at constant rate is a geodesic; $\exp_G=\exp_e$.

**Asymmetric case, $\mathbb J=\mathrm{diag}(J_1,J_2,J_3)$ distinct.** Take $\Omega=(1,1,0)^\top$. Then $\mathbb J\Omega=(J_1,J_2,0)^\top$ and

$$\Omega\times\mathbb J\Omega=\begin{pmatrix}1\\1\\0\end{pmatrix}\times\begin{pmatrix}J_1\\J_2\\0\end{pmatrix}=\begin{pmatrix}0\\0\\J_2-J_1\end{pmatrix},
\qquad \nabla_\Omega\Omega=\begin{pmatrix}0\\0\\(J_2-J_1)/J_3\end{pmatrix}\neq0$$

whenever $J_1\neq J_2$. So $t\mapsto\exp_G(t\hat\Omega)$ is not a geodesic and the two exponentials genuinely differ. In general $\nabla_\Omega\Omega=0$ iff $\Omega\times\mathbb J\Omega=0$, i.e. iff $\Omega$ lies along a **principal axis** — three geodesic directions instead of all of them.

Sanity check on every sign at once: the geodesic equation $\dot\Omega=\widetilde{\mathrm{ad}}_\Omega\Omega=\mathbb J^{-1}(\mathbb J\Omega\times\Omega)$ is $\mathbb J\dot\Omega=\mathbb J\Omega\times\Omega$ — Euler's equation with $\tau=0$, exactly as in [[notation]]. Geodesics of the left-invariant metric *are* free rigid-body motions.

## Problems

1. **Recall.** State the Koszul formula and the defining identity of $\widetilde{\mathrm{ad}}$ from memory, then prove $\widetilde{\mathrm{ad}}_\xi=(\mathrm{ad}_\xi)^\dagger$ where $\dagger$ is the adjoint in $\langle\cdot,\cdot\rangle_{\mathbb I}$. Which of $\mathrm{ad},\mathrm{ad}^*,\widetilde{\mathrm{ad}}$ need a metric?

2. **Compute.** On $SO(3)$ with $\mathbb J=\mathrm{diag}(1,2,3)$: find $\nabla_\Omega\Omega$ for $\Omega=(1,1,0)^\top$ and for $\Omega=(0,1,0)^\top$, and compute $\nabla_{e_1}e_2$ and $\nabla_{e_2}e_1$ in full. Verify $\nabla_{e_1}e_2-\nabla_{e_2}e_1=[e_1,e_2]$ (torsion-free).

3. **Prove.** For connected $G$, show $\nabla_\xi\xi=0$ for all $\xi\in\mathfrak g$ $\iff$ $\widetilde{\mathrm{ad}}_\xi$ is skew-adjoint for all $\xi$ $\iff$ $\langle\cdot,\cdot\rangle_{\mathbb I}$ is $\mathrm{Ad}$-invariant. (Polarize.) Conclude that $\exp_G=\exp_e$ iff the metric is bi-invariant.

4. **Break it.** $SE(3)$ carries no bi-invariant metric. Equip $\mathfrak{se}(3)$ with $\langle(\omega,v),(\rho,u)\rangle_{\mathbb I}=\omega^\top\rho+v^\top u$ (left-invariant, by transport). Using $[(\omega_1,v_1),(\omega_2,v_2)]=(\omega_1\times\omega_2,\ \omega_1\times v_2-\omega_2\times v_1)$, compute $\widetilde{\mathrm{ad}}_\xi\xi$ for $\xi=(\omega,v)$, exhibit a $\xi$ with $\nabla_\xi\xi\neq0$ — a one-parameter subgroup that is not a geodesic — and characterise all $\xi$ for which it *is* one.

---

## Solutions

**1.** $\widetilde{\mathrm{ad}}_\xi=\mathbb I^{-1}\mathrm{ad}^*_\xi\mathbb I$ and $\langle\widetilde{\mathrm{ad}}_\xi\eta,\zeta\rangle_{\mathbb I}=\langle\mathbb I\eta,\mathrm{ad}_\xi\zeta\rangle=\langle\eta,\mathrm{ad}_\xi\zeta\rangle_{\mathbb I}$, which is the definition of the adjoint operator. $\mathrm{ad}$ is metric-free (bracket only); $\mathrm{ad}^*$ is metric-free (plain dual, pairing $\mathfrak g^*\times\mathfrak g$); only $\widetilde{\mathrm{ad}}$ needs $\mathbb I$, since it must return to $\mathfrak g$.

**2.** $\nabla_\Omega\Omega=\mathbb J^{-1}(\Omega\times\mathbb J\Omega)$. For $\Omega=(1,1,0)$: $\mathbb J\Omega=(1,2,0)$, cross product $(0,0,1)$, so $\nabla_\Omega\Omega=(0,0,1/3)\neq0$. For $\Omega=(0,1,0)$ (a principal axis): $\mathbb J\Omega=(0,2,0)$, parallel, so $\nabla_\Omega\Omega=0$.
$\widetilde{\mathrm{ad}}_{e_1}e_2=-\mathbb J^{-1}(e_1\times 2e_2)=-2\mathbb J^{-1}e_3=(0,0,-2/3)$ and $\widetilde{\mathrm{ad}}_{e_2}e_1=-\mathbb J^{-1}(e_2\times e_1)=\mathbb J^{-1}e_3=(0,0,1/3)$. With $[e_1,e_2]=e_3$,
$\nabla_{e_1}e_2=\tfrac12(e_3-(0,0,-2/3)-(0,0,1/3))=(0,0,\tfrac12(1+\tfrac13))=(0,0,2/3)$, and
$\nabla_{e_2}e_1=\tfrac12(-e_3-\widetilde{\mathrm{ad}}_{e_2}e_1-\widetilde{\mathrm{ad}}_{e_1}e_2)=(0,0,\tfrac12(-1+\tfrac13))=(0,0,-1/3)$.
Difference $=(0,0,1)=e_3=[e_1,e_2]$. ✓

**3.** $\nabla_\xi\xi=-\widetilde{\mathrm{ad}}_\xi\xi$, so $\nabla_\xi\xi=0$ for all $\xi$ $\iff$ $\langle\xi,[\xi,\zeta]\rangle_{\mathbb I}=0$ for all $\xi,\zeta$. Polarizing $\xi\mapsto\xi+\eta$ gives $\langle\xi,[\eta,\zeta]\rangle_{\mathbb I}+\langle\eta,[\xi,\zeta]\rangle_{\mathbb I}=0$, i.e. $\langle\mathrm{ad}_\zeta\xi,\eta\rangle_{\mathbb I}+\langle\xi,\mathrm{ad}_\zeta\eta\rangle_{\mathbb I}=0$ after using antisymmetry of the bracket: $\mathrm{ad}_\zeta$ is skew, equivalently $\widetilde{\mathrm{ad}}_\zeta=-\mathrm{ad}_\zeta$ is skew. Skewness of every $\mathrm{ad}_\zeta$ is the derivative at $t=0$ of $\mathrm{Ad}$-invariance along $\exp_G(t\zeta)$; for connected $G$ those exponentials generate $G$, so the infinitesimal statement integrates to $\mathrm{Ad}$-invariance, i.e. bi-invariance. Then $\nabla_\xi\xi=0$ says each $\exp_G(t\xi)$ solves the geodesic equation with $\dot\xi=0$, so $\exp_e(t\xi)=\exp_G(t\xi)$; conversely if the exponentials agree for all $\xi$ then every one-parameter subgroup is a geodesic and $\nabla_\xi\xi=0$.

**4.** With $\zeta=(\rho,u)$: $\langle\widetilde{\mathrm{ad}}_\xi\xi,\zeta\rangle_{\mathbb I}=\langle\xi,[\xi,\zeta]\rangle_{\mathbb I}=\omega\cdot(\omega\times\rho)+v\cdot(\omega\times u-\rho\times v)$. The first and last terms vanish, and $v\cdot(\omega\times u)=u\cdot(v\times\omega)$, so
$$\widetilde{\mathrm{ad}}_\xi\xi=(0,\ v\times\omega),\qquad \nabla_\xi\xi=(0,\ \omega\times v).$$
Take $\omega=e_3$, $v=e_1$ — a screw whose translation is perpendicular to the rotation axis. Then $\nabla_\xi\xi=(0,e_2)\neq0$: the one-parameter subgroup $\exp_G(t\xi)$ is not a geodesic of this left-invariant metric, so $\exp_G\neq\exp_e$ on $SE(3)$. It vanishes iff $\omega\times v=0$: pure rotations ($v=0$), pure translations ($\omega=0$), and screws with $v\parallel\omega$. The obstruction is exactly the perpendicular component of $v$, which is the part of the translation that $\mathrm{Ad}$ mixes into rotation — the failure of $\mathrm{Ad}$-invariance made concrete.
