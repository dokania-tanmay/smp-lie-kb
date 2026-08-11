---
tags: [contraction, mechanics, cotangent-bundle, metrics, g-natural]
---
# Cross-term metrics: why block-diagonal lifts cannot certify contraction

**Prereq:** [[12-double-tangent-bundle]], [[13-sasaki-metric]], [[14-contraction-on-manifolds]], [[07-jacobi-equation]], [[09-hamiltonian-on-cotangent]], [[notation]]
**Goal:** prove that no fibre-independent block-diagonal metric on $T^*Q$ can certify contraction of a mechanical system — for *any* feedback — and write down the base–fibre cross term that repairs it.

## The splitting, and the one variational equation the argument needs

:::info[Definition — the $(u,\xi)$ coordinates on $T_\alpha(T^*Q)$]
Let $K_\alpha:T_\alpha(T^*Q)\to T^*_qQ$ be the connection map of the Levi-Civita $\nabla$ of the kinetic-energy metric $\mathbb G$ — the cotangent counterpart of the connector $K:TTM\to TM$ of [[12-double-tangent-bundle]], defined the same way ($K(\alpha'(0))=\tfrac{D}{ds}\alpha|_0$ for a curve of covectors). A tangent vector $w\in T_\alpha(T^*Q)$ over $q=\pi(\alpha)$ splits as
$$w \;\longleftrightarrow\; (u,\beta) \;=\; \big(T\pi(w),\,K_\alpha(w)\big)\in T_qQ\times T^*_qQ,\qquad \xi\;:=\;\mathbb G^\sharp\beta\in T_qQ .$$
Writing $\xi$ instead of $\beta$ puts **both slots in $T_qQ$**, so a metric on $T^*Q$ becomes a pair of $(1,1)$-tensors plus a coupling. Note $\langle\beta,u\rangle=\langle\xi,u\rangle_{\mathbb G}$, and that $(u,\xi)$ ranges over *all* of $T_qQ\times T_qQ$ as $w$ ranges over $T_\alpha(T^*Q)$.
:::

For a family of closed-loop trajectories $\alpha(s,t)$ with $v=\mathbb G^\sharp\alpha$ the base velocity, $u=\partial_sq$ and $\beta=\tfrac{D}{ds}\alpha$, the variation field obeys

$$\boxed{\ \tfrac{D}{dt}u \;=\; \xi\ }\qquad\text{and}\qquad \tfrac{D}{dt}\xi \;=\; -\mathrm{Hess}^\sharp V(u)\;-\;\mathrm{Jac}_v(u)\;+\;\delta_u .$$

The first is exact and is the whole hinge of what follows: it holds because $\nabla$ is torsion-free ($\tfrac{D}{ds}\partial_tq=\tfrac{D}{dt}\partial_sq$) and $\mathbb G^\sharp$ is $\nabla$-parallel ($\tfrac{D}{ds}\mathbb G^\sharp\alpha=\mathbb G^\sharp\beta$). The second collects the potential Hessian, the tidal operator $\mathrm{Jac}_v(u)=R(u,v)v$ of [[07-jacobi-equation]], and $\delta_u$, the variation of the control force. **The feedback appears only in the second equation.** Remember that.

By [[@simpson-porcoContractionTheoryRiemannian2014]] eq. (8), contraction of $(\mathcal W,X,G,\lambda)$ is equivalent to $\tfrac{d}{dt}G(w,w)\le-2\lambda\,G(w,w)$ along every variation field — no Levi-Civita connection of $G$ on the $2n$-manifold is ever computed ([[14-contraction-on-manifolds]]).

## The obstruction

:::tip[Proposition — no block-diagonal certificate]
Let $A,C$ be $\mathbb G$-symmetric positive-definite $(1,1)$-tensor fields **on $Q$** (i.e. fibre-independent), and put
$$G_\alpha(w,w)\;=\;\langle A(q)u,u\rangle_{\mathbb G}+\langle C(q)\xi,\xi\rangle_{\mathbb G},\qquad w\leftrightarrow(u,\xi).$$
If $\mathcal W\subseteq T^*Q$ contains a pair $\pm\alpha_q$ with $\alpha_q\ne0$, then $G$ satisfies the contraction inequality on $\mathcal W$ **for no feedback whatsoever**.
:::

*Proof.* Differentiate along a closed-loop trajectory with base velocity $v$, using $\nabla\mathbb G=0$ and $\tfrac{D}{dt}u=\xi$:

$$\tfrac12\tfrac{d}{dt}G(w,w)\;=\;\tfrac12\langle(\nabla_vA)u,u\rangle+\langle A\xi,u\rangle+\tfrac12\langle(\nabla_vC)\xi,\xi\rangle+\langle C\,\tfrac{D}{dt}\xi,\xi\rangle .$$

Now evaluate at a variation with $\xi=0$, $u\ne0$ — legitimate, since $(u,\xi)$ is unconstrained at a point. Every term containing $\xi$ drops, **including the entire dependence on $\tfrac{D}{dt}\xi$ and hence on the feedback**, leaving

$$\tfrac12\tfrac{d}{dt}G(w,w)\Big|_{\xi=0}=\tfrac12\langle(\nabla_vA)u,u\rangle,\qquad G(w,w)\big|_{\xi=0}=\langle Au,u\rangle .$$

Contraction would require $\langle(\nabla_vA)u,u\rangle\le-2\lambda\langle Au,u\rangle$. Apply this at $\alpha_q$ and at $-\alpha_q$: same $q$, same $A(q)$ and $\nabla A(q)$, same admissible $u$, but base velocity $-v$. Since $\nabla_vA$ is tensorial (hence linear) in $v$, $\nabla_{-v}A=-\nabla_vA$, so the two instances read
$$\langle(\nabla_vA)u,u\rangle\le-2\lambda\langle Au,u\rangle\quad\text{and}\quad\langle(\nabla_vA)u,u\rangle\ge 2\lambda\langle Au,u\rangle .$$
Together $\langle Au,u\rangle\le0$, contradicting $A\succ0$, $u\ne0$, $\lambda>0$. $\square$

**The moral, plainly.** The feedback enters only the fibre slot, through $\tfrac{D}{dt}\xi$. A metric with no base–fibre coupling multiplies $\tfrac{D}{dt}\xi$ by $\xi$, so in the purely horizontal direction $\xi=0$ the certificate is **blind to the feedback**. All that is left is the drift of $A$ along the flow, and that drift is odd in $v$ — so it cannot be negative in both time-reversed copies of the same configuration.

:::tip[Corollary — the obvious lifts all fail]
$A=C=\mathrm{id}$ (the **Sasaki metric** of [[13-sasaki-metric]]) is $\nabla$-parallel, so $\nabla_vA=0$ and $\tfrac{d}{dt}G|_{\xi=0}=0$ exactly: no $\pm\alpha_q$ hypothesis is needed and the failure is on *any* nonempty region. The **total-energy metric** $A=\mathrm{Hess}^\sharp V$, $C=\mathrm{id}$ has $\nabla A\ne0$ in general and falls to the $\pm v$ argument.
:::

So the block-diagonal lift fails for a *second, independent* reason beyond the curvature distortion catalogued in [[13-sasaki-metric]]: even where its curvature is benign, it is structurally incapable of seeing the control.

:::tip[Remark — on the zero section the hypothesis is free]
If $\mathcal W$ contains a closed-loop equilibrium, that equilibrium is a zero covector $\alpha_q=0$ (a fixed point needs $\mathbb G^\sharp\alpha=0$), so $v=0$ and $\nabla_vA=0$; the $\xi=0$ evaluation gives $0\le-2\lambda\langle Au,u\rangle<0$ in one line. Any region large enough to contain the point one is trying to converge to is already dead.
:::

## The linear shadow

No geometry required. For $M\ddot q+D\dot q+Kq=0$ in Hamiltonian variables $p=M\dot q$, i.e. $\dot q=M^{-1}p$, $\dot p=-Kq-DM^{-1}p$ with system matrix $\mathcal A=\begin{psmallmatrix}0&M^{-1}\\-K&-DM^{-1}\end{psmallmatrix}$, the energy metric $P=\mathrm{diag}(K,M^{-1})$ gives

$$\mathcal A^\top P+P\mathcal A=\begin{pmatrix}0&KM^{-1}-KM^{-1}\\ M^{-1}K-M^{-1}K&-2M^{-1}DM^{-1}\end{pmatrix}=\mathrm{diag}\big(0,\,-2M^{-1}DM^{-1}\big),$$

negative **semi**definite only: the stiffness and inertia terms cancel identically and the $(1,1)$ block is exactly zero. The zero block sits in the $q$ directions — the linear image of "$\xi=0$, $u\ne0$". Damping can never fix it, because damping only ever enters the $(2,2)$ block.

## Worked example — damped oscillator ([[@simpson-porcoContractionTheoryRiemannian2014]] Example 1)

[[14-contraction-on-manifolds]] already ran this system to get the admissible range $\varepsilon\in(0,1/(1+\zeta^2))$. Here the point is different: read the failure as the proposition's $\xi=0$ evaluation, and get the actual rate.

$Q=\mathbb R$, $m=k=b=1$: $\dot x=y$, $\dot y=-x-y$. The variation obeys the same linear equations, $\dot u=\xi$, $\dot\xi=-u-\xi$.

**Block-diagonal energy metric** $G_0(w,w)=\tfrac12u^2+\tfrac12\xi^2$:
$$\tfrac{d}{dt}G_0=u\xi+\xi(-u-\xi)=-\xi^2\;\le\;0 .$$
Decaying, but at $\xi=0,\ u\ne0$ the derivative is $0$ while $G_0=\tfrac12u^2>0$, so no $\lambda>0$ can satisfy $\tfrac{d}{dt}G_0\le-2\lambda G_0$. This *is* the proposition's $\xi=0$ evaluation, in the flat case where $\nabla A=0$.

**Add a cross term** $\varepsilon b\,dx\otimes dy$ with $\varepsilon=\tfrac12$ — the metric $G(w,w)=\tfrac12u^2+\tfrac12u\xi+\tfrac12\xi^2=\tfrac12(u^2+u\xi+\xi^2)$:
$$\tfrac{d}{dt}G=u\xi+\xi(-u-\xi)+\tfrac12\big(\xi^2+u(-u-\xi)\big)=-\tfrac12\big(u^2+u\xi+\xi^2\big)=-G .$$
Strict decay with $\lambda=\tfrac12$, on all of $\mathbb R^2$ — and $\tfrac12$ is exactly the spectral abscissa of $s^2+s+1$, so this metric is not merely adequate but tight. Positive definiteness holds since $\det\begin{psmallmatrix}1/2&1/4\\1/4&1/2\end{psmallmatrix}=\tfrac3{16}>0$. At $\xi=0$ the surviving term is $\tfrac12u\,\dot\xi=-\tfrac12u^2$: the cross term is the channel through which $\dot\xi$ — the feedback — reaches the $u$ direction.

## The fix

:::info[Definition — the canonical symmetric pairing and the skewed lift]
$$\Pi(w_1,w_2)\;:=\;\langle\beta_2,u_1\rangle+\langle\beta_1,u_2\rangle$$
is the **symmetrization** of the canonical form $\omega_0(w_1,w_2)=\langle\beta_2,u_1\rangle-\langle\beta_1,u_2\rangle$: metric-independent, symmetric, of signature $(n,n)$ (in $(u,\xi)$ coordinates its matrix is $\begin{psmallmatrix}0&I\\I&0\end{psmallmatrix}$). The **skewed lift** is
$$G_\alpha(w,w)\;=\;a\|u\|^2_{\mathbb G}+2b\langle u,\xi\rangle_{\mathbb G}+c\|\xi\|^2_{\mathbb G},\qquad a,c>0,\ ac>b^2,$$
i.e. horizontal block $a\,\pi^*\mathbb G$, vertical block $c\,\mathbb G^{-1}$, cross term $b\,\Pi$. These are $g$-natural metrics with constant, fibre-independent coefficients.
:::

The obstruction proof is precisely the statement that $b\ne0$ is **indispensable**, not a convenience: $b\,\Pi$ is the only term whose derivative at $\xi=0$ contains $\tfrac{D}{dt}\xi$. The contraction condition on $(a,b,c)$ — where curvature and the potential Hessian finally enter — is lesson 17; do not guess it from the example.

**The structural point.** $\omega_0$ antisymmetrized is the symplectic form that contraction must *break* ([[15-symplectic-not-contracting]]: a symplectic flow is never contracting). $\Pi$, its symmetrization, is what a certifying metric must *contain*. One underlying pairing $\langle\beta,u\rangle$, two roles — one obstruction, one remedy.

:::warning[Open question]
The proposition rules out $b=0$ with $A,C$ fibre-independent. It says nothing about (i) fibre-dependent blocks $A(q,\alpha)$, where $\tfrac{d}{dt}A$ picks up $\tfrac{D}{dt}\alpha$ and the feedback re-enters the horizontal slot (Problem 4), or (ii) whether constant $(a,b,c)$ suffice on a curved $Q$ — on $SO(3)$ with asymmetric inertia the required $b$ plausibly has to vary with $q$ and $\|v\|$. Both are untested here.
:::

## Problems

1. State the splitting $w\leftrightarrow(u,\xi)$ and both covariant variational equations, and say in one sentence which of the two contains the feedback and why that is what dooms block-diagonal metrics.
2. Show that $G(w,w)=a\|u\|^2+2b\langle u,\xi\rangle+c\|\xi\|^2$ is positive definite on $T_qQ\times T_qQ$ iff $\begin{psmallmatrix}a&b\\b&c\end{psmallmatrix}\succ0$, i.e. iff $a>0$ and $ac>b^2$ — including why $\dim Q=n$ adds nothing to the $n=1$ case. Then redo the worked example with general $\varepsilon\in(0,1)$ at $m=k=b=1$ and find the $\varepsilon$ maximizing the certified rate.
3. Prove the Sasaki corollary directly: with $A=C=\mathrm{id}$, show $\tfrac{d}{dt}G(w,w)|_{\xi=0}=0$ and conclude without invoking $\pm\alpha_q$. Which hypothesis of the proposition did you not need?
4. **Break it.** The proposition needs *both* $\pm\alpha_q\in\mathcal W$ *and* fibre-independence of $A$. (a) Where exactly does the proof fail if $A=A(q,\alpha)$? Exhibit the extra term and show it carries the feedback. (b) Where does it fail if $\mathcal W$ contains $\alpha_q$ but not $-\alpha_q$? For each, say whether it is a real escape or a technicality.

---

## Solutions

**1.** $w\mapsto(u,\beta)=(T\pi(w),K_\alpha(w))$, $\xi=\mathbb G^\sharp\beta$; then $\tfrac{D}{dt}u=\xi$ and $\tfrac{D}{dt}\xi=-\mathrm{Hess}^\sharp V(u)-\mathrm{Jac}_v(u)+\delta_u$. Only the second carries $\delta_u$, the variation of the control force. In a block-diagonal metric $\tfrac{D}{dt}\xi$ appears solely in the term $\langle C\tfrac{D}{dt}\xi,\xi\rangle$, which vanishes at $\xi=0$; the certificate therefore cannot be influenced by any choice of feedback in the horizontal directions.

**2.** Fix $\rho_1=\|u\|,\rho_2=\|\xi\|$. Cauchy–Schwarz gives $\langle u,\xi\rangle\in[-\rho_1\rho_2,\rho_1\rho_2]$, and both endpoints are attained ($\xi=\pm\rho_2u/\rho_1$). So $\min G$ over that pair of radii is $a\rho_1^2-2|b|\rho_1\rho_2+c\rho_2^2$, the $n=1$ form with $b$ replaced by $-|b|$; $G\succ0$ iff this is positive for all $(\rho_1,\rho_2)\ne0$ with $\rho_i\ge0$, i.e. iff $a>0$ and $ac-b^2>0$ (Sylvester). Dimension is irrelevant because only the 2-plane $\mathrm{span}\{u,\xi\}$ ever matters.
With $G=\tfrac12u^2+\varepsilon u\xi+\tfrac12\xi^2$ and $\dot u=\xi,\ \dot\xi=-u-\xi$: $\tfrac{d}{dt}G=u\xi+\xi(-u-\xi)+\varepsilon(\xi^2+u(-u-\xi))=-\varepsilon u^2-\varepsilon u\xi-(1-\varepsilon)\xi^2$. The certified rate is the largest $\lambda$ with $\tfrac{d}{dt}G\le-2\lambda G$. At $\varepsilon=\tfrac12$ the two forms are proportional, $\tfrac{d}{dt}G=-G$, giving $\lambda=\tfrac12$; since $\tfrac12$ is the spectral abscissa no $\varepsilon$ can do better, so $\varepsilon=\tfrac12$ is optimal. (Positive definiteness needs $\varepsilon<1$; $\varepsilon\to0$ recovers $\lambda\to0$.)

**3.** $\nabla\,\mathrm{id}=0$, so $\nabla_v A=\nabla_vC=0$ and $\tfrac12\tfrac{d}{dt}G=\langle\xi,u\rangle+\langle\tfrac{D}{dt}\xi,\xi\rangle$, which is $0$ at $\xi=0$. But contraction demands $\tfrac{d}{dt}G\le-2\lambda\|u\|^2<0$ for $u\ne0$. Contradiction. Not needed: the pair $\pm\alpha_q$, hence also $\alpha_q\ne0$ — any nonempty region kills the Sasaki metric, including regions inside a single velocity half-space.

**4.** (a) With $A=A(q,\alpha)$ the chain rule along the trajectory adds $\langle(\partial_\alpha A\cdot\tfrac{D}{dt}\alpha)u,u\rangle$, and $\tfrac{D}{dt}\alpha=-dV+\sum_au^aF^a$ contains the control. This term survives at $\xi=0$, so the feedback is no longer invisible; moreover $A(q,-\alpha)\ne A(q,\alpha)$ in general, so the $\pm$ pairing has nothing to pair. This is a **real escape** — the class of metrics is genuinely larger — but an expensive one: it buys back the feedback through a term quadratic in the state's own momentum, whereas $b\,\Pi$ does it with one constant. (b) Restricting to a region with $\alpha_q$ of one sign leaves the $\xi=0$ identity $\tfrac12\tfrac{d}{dt}G=\tfrac12\langle(\nabla_vA)u,u\rangle$ intact but blocks the contradiction; one would need $\langle(\nabla_vA)u,u\rangle\le-2\lambda\langle Au,u\rangle$ to hold with a *definite* sign of $v$, which is not absurd. It is nonetheless a **technicality**: by the remark above, any region containing the closed-loop equilibrium contains a zero covector, where $v=0$ makes $\nabla_vA=0$ and the contradiction returns with no $\pm$ argument at all. A one-signed region can only certify contraction *away from* the point it converges to, which is not a useful certificate.
