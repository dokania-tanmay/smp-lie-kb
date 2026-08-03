---
tags: [riemannian, curvature, geodesics, foundations]
---
# Jacobi Equation, Geodesic Deviation, and the Tidal Operator

**Prereq:** [[riemannian-geometry]] (parallel transport, normal coordinates, Gauss lemma), [[notation]] (curvature sign convention), [[05-riemann-tensor]] (symmetries S1–S4, sectional curvature), [[03-levi-civita-left-invariant]] ($\nabla_\xi\eta=\tfrac12[\xi,\eta]$ in the bi-invariant case), lesson 06 ($\mathrm{Sec}(X,Y)=\tfrac14\|[X,Y]\|^2$)
**Goal:** derive the Jacobi equation from a geodesic variation, know the tidal operator $\mathrm{Jac}_v$ and its three defining properties, and solve it in constant curvature so that "positive curvature focuses, negative curvature spreads" is a computation and not a slogan.

## Setup: a family of geodesics

:::info[Definition]
A **geodesic variation** is a smooth map $\gamma:(-\varepsilon,\varepsilon)\times[0,T]\to M$, $(s,t)\mapsto\gamma(s,t)$, such that $t\mapsto\gamma(s,t)$ is a geodesic of $\nabla$ for every fixed $s$. Write
$$v = \partial_t\gamma \quad(\text{the geodesic velocity}),\qquad u = \partial_s\gamma \quad(\text{the \textbf{variation field}}).$$
$u$ is a vector field along $\gamma$; restricted to $s=0$ it is a field along the single geodesic $\gamma_0=\gamma(0,\cdot)$, and it measures the infinitesimal displacement to the neighbouring geodesic.
:::

Two facts about covariant differentiation along a two-parameter map are all we need. $\tfrac{D}{dt}$ and $\tfrac{D}{ds}$ denote covariant derivatives of fields along $\gamma$ in the $t$- and $s$-directions.

:::tip[Lemma]
**Symmetry (torsion-freeness).** $\ \dfrac{D}{ds}\partial_t\gamma = \dfrac{D}{dt}\partial_s\gamma$, i.e. $\tfrac{D}{ds}v = \tfrac{D}{dt}u$.

**Commutator (curvature).** For any field $W$ along $\gamma$,
$$\Big(\frac{D}{ds}\frac{D}{dt}-\frac{D}{dt}\frac{D}{ds}\Big)W \;=\; R(u,v)\,W .$$
:::

The first is torsion-freeness of the Levi-Civita connection applied to the coordinate fields $\partial_s,\partial_t$, whose bracket vanishes: $\nabla_{\partial_s}\partial_t-\nabla_{\partial_t}\partial_s=[\partial_s,\partial_t]=0$. The second is the definition $R(X,Y)Z=\nabla_X\nabla_YZ-\nabla_Y\nabla_XZ-\nabla_{[X,Y]}Z$ of [[notation]] with $X=u$, $Y=v$ and the bracket term absent, again because $[\partial_s,\partial_t]=0$. **The sign of the Jacobi equation is inherited entirely from these two lines** — change the curvature convention and the equation flips.

## The derivation

Each $t$-curve is a geodesic, so $\tfrac{D}{dt}v=0$ for every $s$. Now differentiate $u$ twice in $t$ and swap derivatives at each step:

$$\frac{D^2u}{dt^2} \;=\; \frac{D}{dt}\Big(\frac{D}{dt}u\Big)
\;\overset{\text{(sym)}}{=}\; \frac{D}{dt}\Big(\frac{D}{ds}v\Big)
\;\overset{\text{(comm)}}{=}\; \frac{D}{ds}\Big(\frac{D}{dt}v\Big) - R(u,v)v
\;=\; \frac{D}{ds}(0) - R(u,v)v .$$

:::tip[Theorem]
**Jacobi equation.** The variation field of a geodesic variation satisfies
$$\boxed{\ \frac{D^2u}{dt^2} + R(u,v)v \;=\; 0\ },\qquad v=\dot\gamma .$$
A field $u$ along a geodesic $\gamma$ solving this is a **Jacobi field**. It is a linear second-order ODE along $\gamma$, so a Jacobi field is determined by $u(0)\in T_{\gamma(0)}M$ and $\tfrac{Du}{dt}(0)\in T_{\gamma(0)}M$, and the space of Jacobi fields along $\gamma$ has dimension $2n$.
:::

Every Jacobi field arises from an actual geodesic variation, so nothing is lost by working with the ODE instead of the family.

## The tidal operator

:::info[Definition]
For $v\in T_pM$ the **tidal** (or **Jacobi**) **operator** is the linear map
$$\mathrm{Jac}_v : T_pM\to T_pM,\qquad \mathrm{Jac}_v(u) = R(u,v)v .$$
The Jacobi equation is then $\ \tfrac{D^2u}{dt^2}+\mathrm{Jac}_v(u)=0$: a linear oscillator whose stiffness is the curvature.
:::

:::tip[Proposition]
1. $\mathrm{Jac}_v$ is **$\mathbb G$-symmetric**: $\langle\mathrm{Jac}_v u,\,w\rangle = \langle u,\,\mathrm{Jac}_v w\rangle$.
2. $\mathrm{Jac}_v(v)=0$, so $v$ is always in the kernel and $\mathrm{Jac}_v$ acts nontrivially only on $v^\perp$.
3. $\displaystyle \langle\mathrm{Jac}_v u,\,u\rangle \;=\; \mathrm{Sec}(u,v)\,\big(\|u\|^2\|v\|^2-\langle u,v\rangle^2\big).$
:::

*Proof.* (1) In the $(0,4)$ notation $\mathrm{Rm}(X,Y,Z,W)=\langle R(X,Y)Z,W\rangle$ of [[05-riemann-tensor]], pair symmetry (S4) and the two antisymmetries (S1), (S2) give
$\langle\mathrm{Jac}_vu,w\rangle = \mathrm{Rm}(u,v,v,w) \overset{\text{(S4)}}{=} \mathrm{Rm}(v,w,u,v) \overset{\text{(S1),(S2)}}{=} \mathrm{Rm}(w,v,v,u) = \langle\mathrm{Jac}_vw,u\rangle$,
the third equality being two sign flips (one in each pair). (2) $R(v,v)v=0$ by (S1), antisymmetry in the first two slots. (3) Is the definition $\mathrm{Sec}(u,v)=\langle R(u,v)v,u\rangle/(\|u\|^2\|v\|^2-\langle u,v\rangle^2)$ of [[notation]] read backwards. $\square$

Property (1) says $\mathrm{Jac}_v$ is diagonalizable with real eigenvalues in an orthonormal basis of $v^\perp$; those eigenvalues are $\|v\|^2$ times sectional curvatures of planes containing $v$. Property (3) says: **the sign of the curvature is the sign of the stiffness.**

## Constant curvature: the three pictures

Take $\gamma$ unit speed ($\|v\|=1$) and $u\perp v$ with $u(0)=0$, $\|\tfrac{Du}{dt}(0)\|=1$. If every sectional curvature equals $\kappa$, then $\mathrm{Jac}_v(u)=\kappa u$ on $v^\perp$, and writing $u=f(t)E(t)$ with $E$ a **parallel** unit normal field (so $\tfrac{D}{dt}E=0$, using parallel transport from [[riemannian-geometry]]) reduces the Jacobi equation to the scalar

$$\ddot f + \kappa f = 0,\qquad f(0)=0,\ \dot f(0)=1
\quad\Longrightarrow\quad
\|u(t)\| = f(t) = \begin{cases}
\dfrac{\sin(\sqrt\kappa\,t)}{\sqrt\kappa}, & \kappa>0 \quad\text{(focusing)}\\[4pt]
t, & \kappa=0 \quad\text{(Euclidean)}\\[4pt]
\dfrac{\sinh(\sqrt{|\kappa|}\,t)}{\sqrt{|\kappa|}}, & \kappa<0 \quad\text{(spreading).}
\end{cases}$$

Positive curvature is a restoring force and pulls neighbouring geodesics back together, vanishing again at $t=\pi/\sqrt\kappa$. Negative curvature is a negative stiffness and separates them exponentially. Flat is the linear reference. Everything downstream in this project — comparison theorems, the Hessian of the distance function, the curvature term in the generator — is a quantitative version of this trichotomy.

:::info[Definition]
$q=\gamma(t_1)$ is **conjugate** to $p=\gamma(0)$ along $\gamma$ if a Jacobi field exists with $u(0)=0$, $u\not\equiv0$, $u(t_1)=0$.
:::

## Worked example: the round $S^2$ of radius $r$

Realize $S^2_r\subset\mathbb R^3$ with the induced metric; its geodesics are great circles and its curvature is $\kappa=1/r^2$. Take $p=(0,0,r)$ and the unit tangent directions $e(s)=(\cos s,\sin s,0)\in T_pS^2_r$. The great circle leaving $p$ in direction $e(s)$, at unit speed, is

$$\gamma(s,t) \;=\; \big(r\sin(t/r)\cos s,\ \ r\sin(t/r)\sin s,\ \ r\cos(t/r)\big),$$

which has $\|\gamma\|=r$ for all $(s,t)$, so it does lie on the sphere. Differentiate:

$$v=\partial_t\gamma = \big(\cos(t/r)\cos s,\ \cos(t/r)\sin s,\ -\sin(t/r)\big), \qquad \|v\|=1\ \checkmark$$
$$u=\partial_s\gamma = \big(-r\sin(t/r)\sin s,\ \ r\sin(t/r)\cos s,\ \ 0\big).$$

Then $\langle u,v\rangle = -r\sin\tfrac tr\cos\tfrac tr\cos s\sin s + r\sin\tfrac tr\cos\tfrac tr\sin s\cos s = 0$, so $u\perp v$ throughout, and

$$\|u(t)\| \;=\; r\,\sin(t/r).$$

Check against the ODE: $u = r\sin(t/r)E(t)$ with $E=(-\sin s,\cos s,0)$, which is a constant vector of $\mathbb R^3$ tangent to the sphere along $\gamma$, hence parallel. So $\tfrac{D^2u}{dt^2} = \tfrac{d^2}{dt^2}\big(r\sin(t/r)\big)E = -\tfrac1{r^2}u = -\mathrm{Jac}_v(u)$, exactly the Jacobi equation with $\kappa=1/r^2$, and $\|u\|=r\sin(t/r)=\sin(\sqrt\kappa t)/\sqrt\kappa$ as predicted.

**Focusing, read off.** $\|u\|$ grows from $0$, peaks at $t=\pi r/2$ (the equator, where the great circles are farthest apart) and returns to $0$ at $t=\pi r$ — the antipode. Every geodesic leaving $p$ refocuses there: the antipode is conjugate to $p$ at distance $\pi r$, and $d(\exp_p)_{v}$ is singular on the sphere of radius $\pi r$ in $T_pS^2_r$, which is where normal coordinates die.

Contrast: on hyperbolic space of curvature $-1/\rho^2$ the same computation gives $\|u(t)\|=\rho\sinh(t/\rho)$, which never vanishes for $t>0$, so there are no conjugate points and $\exp_p$ is a diffeomorphism on all of $T_pM$.

## Forward pointer

In the closed-loop contraction analysis (lesson 17) the variational equation of a controlled mechanical system on $G$ is the Jacobi equation with extra terms, and $\mathrm{Jac}_v$ appears inside a **curvature-corrected stiffness** $\mathcal S = \mathrm{Hess}^\sharp(V+\varphi)+\mathrm{Jac}_v$. Positive curvature therefore *adds* stiffness and helps a tracking controller, while negative curvature subtracts a term proportional to $\|v\|^2$ — which is why the contraction region ends up bounded **in velocity** and damping cannot repair it. This lesson supplies only the operator; the estimate is lesson 17's.

**Which of the three kinds is this?** Fully intrinsic. $\mathrm{Jac}_v$ is built from $R$, the Jacobi equation is an identity between covariant derivatives along a curve, and $\mathrm{Sec}$, conjugate distance and injectivity radius are chart-independent numbers. No $\sup|\partial g_{ij}|$ can enter, which is precisely why this is the intended replacement for the chart-dependent constants in [[00-study-plan]] Phase 5.

## Problems

1. **Recall.** From memory: state what a geodesic variation is, define its variation field, write the Jacobi equation with the curvature convention of [[notation]], and define $\mathrm{Jac}_v$. Then state the two identities ($\tfrac{D}{ds}\partial_t\gamma=\tfrac{D}{dt}\partial_s\gamma$ and the commutator) and say which structural property of $\nabla$ each one comes from.

2. **Compute — $SO(3)$, bi-invariant metric.** With $\nabla_\xi\eta=\tfrac12[\xi,\eta]$ for left-invariant fields, verify $R(X,Y)Z=-\tfrac14[[X,Y],Z]$ using the Jacobi identity, and confirm it reproduces $\mathrm{Sec}(X,Y)=\tfrac14\|[X,Y]\|^2$ for orthonormal $X,Y$. Then with $u=\hat a$, $v=\hat b$ show
$$\mathrm{Jac}_{\hat b}(\hat a) \;=\; \tfrac14\big(\|b\|^2a - (a\cdot b)\,b\big)^{\wedge}.$$
Deduce that $SO(3)$ with this metric has constant curvature $\kappa=\tfrac14$, and find the distance to the first conjugate point along a geodesic $\exp_G(t\hat b)$, $\|b\|=1$.

3. **Prove.** (a) Show $\mathrm{Jac}_v(v)=0$ directly from the antisymmetry of $R$, and deduce that $u(t)=(\alpha+\beta t)v(t)$ solves the Jacobi equation for any constants $\alpha,\beta$. Identify the geodesic variation that produces it. (b) Show $\mathbb G$-symmetry of $\mathrm{Jac}_v$ from pair symmetry (S4) of [[05-riemann-tensor]]. (c) Conclude that if $u$ is a Jacobi field with $u(0)\perp v$ and $\tfrac{Du}{dt}(0)\perp v$, then $u(t)\perp v(t)$ for all $t$.

4. **Break it.** Two failures of hypothesis.
   (a) *Not geodesics.* Let $\gamma(s,t)$ be a smooth family of curves that are **not** geodesics, with acceleration $A(s,t)=\tfrac{D}{dt}\partial_t\gamma \ne 0$. Redo the derivation and show
   $$\frac{D^2u}{dt^2} + \mathrm{Jac}_v(u) \;=\; \frac{D}{ds}A .$$
   This forced Jacobi equation is the variational equation the mechanics lessons actually need. Say what $\tfrac{D}{ds}A$ is when $A$ comes from a control law $A=F(\gamma,v)$.
   (b) *Past a conjugate point.* On $S^2_r$, exhibit a nonzero Jacobi field along a great circle vanishing at both $t=0$ and $t=\pi r$, and conclude that $d(\exp_p)_w$ is singular for $\|w\|=\pi r$. Hence $\exp_p$ is not a diffeomorphism on any ball of radius $>\pi r$ and normal coordinates centred at $p$ cannot cover the antipode.

---

## Solutions

**1.** Definitions as stated above. Symmetry $\tfrac{D}{ds}\partial_t\gamma=\tfrac{D}{dt}\partial_s\gamma$ is **torsion-freeness** ($\nabla_XY-\nabla_YX=[X,Y]$ applied to $\partial_s,\partial_t$, whose bracket is zero). The commutator identity is the **definition of $R$**, with the $\nabla_{[X,Y]}$ term absent for the same reason. Metric-compatibility is not used in the derivation at all — it is used only when one starts taking inner products, as in Proposition (3).

**2.** $R(X,Y)Z=\tfrac14[X,[Y,Z]]-\tfrac14[Y,[X,Z]]-\tfrac12[[X,Y],Z]$; Jacobi gives $[X,[Y,Z]]-[Y,[X,Z]]=[[X,Y],Z]$, so $R(X,Y)Z=(\tfrac14-\tfrac12)[[X,Y],Z]=-\tfrac14[[X,Y],Z]$. Then with $\mathrm{Ad}$-invariance $\langle[A,B],C\rangle=-\langle B,[A,C]\rangle$:
$\langle R(X,Y)Y,X\rangle=-\tfrac14\langle[[X,Y],Y],X\rangle=\tfrac14\langle Y,[X,[X,Y]]\rangle\cdot(-1)\cdot(-1)=\tfrac14\|[X,Y]\|^2$ for orthonormal $X,Y$ — matching [[notation]]. For $SO(3)$, $[\hat a,\hat b]=\widehat{a\times b}$, so
$\mathrm{Jac}_{\hat b}(\hat a)=-\tfrac14[[\hat a,\hat b],\hat b]=-\tfrac14\widehat{(a\times b)\times b}=\tfrac14\widehat{b\times(a\times b)}=\tfrac14\big(\|b\|^2a-(a\cdot b)b\big)^{\wedge}$,
using $b\times(a\times b)=a\|b\|^2-b(a\cdot b)$. For $\|b\|=1$ and $a\perp b$ this is $\tfrac14\hat a$, i.e. $\mathrm{Jac}_v=\tfrac14\mathrm{id}$ on $v^\perp$: constant curvature $\kappa=\tfrac14$ (indeed $SO(3)$ with this metric is a round $S^3$ of radius $2$, quotiented by $\pm$). First conjugate point at $t=\pi/\sqrt\kappa=2\pi$ — the geodesic $\exp_G(t\hat b)$ has returned to the identity. Note the cut locus comes earlier, at $t=\pi$, because $SO(3)\cong\mathbb{RP}^3$; conjugate distance and injectivity radius are not the same number.

**3.** (a) $\mathrm{Jac}_v(v)=R(v,v)v=0$ since $R$ is antisymmetric in its first two arguments. For $u=(\alpha+\beta t)v$: $\tfrac{Du}{dt}=\beta v$ (as $\tfrac{Dv}{dt}=0$), so $\tfrac{D^2u}{dt^2}=0$, and $\mathrm{Jac}_v(u)=(\alpha+\beta t)\mathrm{Jac}_v(v)=0$. The variation is reparametrization/translation along the *same* geodesic: $\gamma(s,t)=\gamma_0\big(t+s(\alpha+\beta t)\big)$ to first order in $s$. These are the trivial Jacobi fields and carry no curvature information — which is why one always restricts to $u\perp v$.
(b) $\langle\mathrm{Jac}_vu,w\rangle=\mathrm{Rm}(u,v,v,w)\overset{\text{(S4)}}{=}\mathrm{Rm}(v,w,u,v)$; flipping the first pair and the last pair gives two minus signs, so $=\mathrm{Rm}(w,v,v,u)=\langle\mathrm{Jac}_vw,u\rangle$.
(c) Let $\phi(t)=\langle u(t),v(t)\rangle$. Metric compatibility and $\tfrac{Dv}{dt}=0$ give $\ddot\phi=\langle\tfrac{D^2u}{dt^2},v\rangle=-\langle\mathrm{Jac}_vu,v\rangle=-\langle u,\mathrm{Jac}_vv\rangle=0$ by (b) and (a). So $\phi$ is affine in $t$; $\phi(0)=0$ and $\dot\phi(0)=\langle\tfrac{Du}{dt}(0),v\rangle=0$ force $\phi\equiv0$.

**4(a).** Only the last step of the derivation changes. Still $\tfrac{D}{dt}u=\tfrac{D}{ds}v$ by torsion-freeness, so
$$\frac{D^2u}{dt^2}=\frac{D}{dt}\frac{D}{ds}v=\frac{D}{ds}\frac{D}{dt}v-R(u,v)v=\frac{D}{ds}A-\mathrm{Jac}_v(u).$$
If $A=F(\gamma,v)$ then by the chain rule $\tfrac{D}{ds}A=(\nabla_uF)(\gamma,v)+ (\partial_vF)\big(\tfrac{D}{ds}v\big)=\nabla_uF + (\partial_vF)\tfrac{Du}{dt}$: a stiffness term and a damping term acting on the variation field. That is exactly the structure lesson 17 combines with $\mathrm{Jac}_v$ — the closed-loop stiffness is $\mathrm{Jac}_v-\nabla F$, and curvature enters on equal footing with the control gains.

**4(b).** Take $\gamma$ the great circle from $p=(0,0,r)$ in direction $(1,0,0)$ and $u(t)=r\sin(t/r)E(t)$ with $E=(0,1,0)$ parallel along $\gamma$ — this is the $s$-derivative computed in the worked example, evaluated at $s=0$. It is a Jacobi field, it is not identically zero, and it vanishes at $t=0$ and $t=\pi r$. Now let $w=\pi r\,\dot\gamma(0)\in T_pS^2_r$ and $\tilde w=\pi r\,E(0)$. The standard identification $u(t)=d(\exp_p)_{t\dot\gamma(0)}\big(t\,\tfrac{Du}{dt}(0)\big)$ for Jacobi fields with $u(0)=0$ gives $d(\exp_p)_{w}(\pi r\,E(0))=u(\pi r)=0$ with $\pi rE(0)\ne0$, so $d(\exp_p)_w$ has nontrivial kernel. Hence $\exp_p$ is not an immersion at $w$, not a diffeomorphism on any ball of radius $>\pi r$, and normal coordinates around $p$ break down exactly at the antipode: the whole sphere $\|w\|=\pi r$ in $T_pS^2_r$ collapses to a single point.
