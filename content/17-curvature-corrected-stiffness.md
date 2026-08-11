---
tags: [contraction, curvature, mechanics, control, so3]
---
# Curvature-Corrected Stiffness and the Contraction Certificate

**Prereq:** [[07-jacobi-equation]] ($\mathrm{Jac}_v(u)=R(u,v)v$ and its forced Jacobi equation, problem 4(a)), [[08-hessian-comparison]] ($\mathrm{Hess}^\sharp$), [[06-curvature-left-invariant-metrics]] (negative $\mathrm{Sec}$ on $SO(3)$), [[09-hamiltonian-on-cotangent]], [[14-contraction-on-manifolds]], [[16-cross-term-metrics]], [[notation]]
**Goal:** state and prove the contraction certificate for a fully actuated simple mechanical system, and read off what curvature does to it — positive curvature helps, negative curvature caps the region **in velocity**, and no amount of damping repairs that.

Throughout: $\Sigma=(Q,\mathbb G,V,\mathcal F)$ a simple mechanical system, state $\alpha\in T^*Q$ over $q$, velocity $v=\mathbb G^\sharp\alpha$, and $\nabla$ the Levi-Civita connection of $\mathbb G$. The unforced dynamics are the geodesic spray plus $-\mathrm{grad}\,V$.

## The feedback

:::info[Assumptions]
**Full actuation.** $\mathrm{span}_{\mathbb R}\{F^1(q),\dots,F^m(q)\}=T^*_qQ$ for every $q$ in the region of interest, so any covector force is realisable.

**Parallel damping.** $\mathcal D\in\Gamma(T^1_1Q)$ is $\mathbb G$-symmetric positive-definite with $\nabla\mathcal D=0$ — in particular $\mathcal D=d\,\mathrm{id}$, $d>0$.
:::

Potential shaping plus damping:

$$F_{\mathrm{ctrl}}(\alpha)\;=\;-\,d\varphi(q)\;-\;\mathbb G^\flat\big(\mathcal D(q)\,\mathbb G^\sharp\alpha\big),\qquad \varphi\in C^\infty(Q)\ \text{the shaping potential},$$

giving the closed loop

$$\dot q=v=\mathbb G^\sharp\alpha,\qquad \tfrac{D}{dt}\alpha=-d(V+\varphi)(q)-\mathbb G^\flat(\mathcal Dv),
\qquad\text{i.e.}\qquad \nabla_vv=-\mathrm{grad}(V+\varphi)-\mathcal Dv .$$

The damping term is dissipative, so the closed-loop flow is **not** symplectic. That is mandatory, not incidental: [[15-symplectic-not-contracting]] shows a symplectic flow can never be contracting (its Lyapunov spectrum is symmetric about $0$). The shaping term $-d\varphi$ alone would leave the flow Hamiltonian and hence useless here.

## The closed-loop variational system

Take a family $\alpha(s,t)$ of closed-loop trajectories, base curves $q(s,t)$, and set $u=\partial_sq$, $\xi=\mathbb G^\sharp\tfrac{D}{ds}\alpha$. Problem 4(a) of [[07-jacobi-equation]] already gives the forced Jacobi equation $\tfrac{D^2u}{dt^2}+\mathrm{Jac}_v(u)=\tfrac{D}{ds}A$; here $A=-\mathrm{grad}(V+\varphi)-\mathcal Dv$, and $\tfrac{D}{ds}A=-\mathrm{Hess}^\sharp(V+\varphi)(u)-\mathcal D\xi$ using $\nabla\mathcal D=0$ and $\tfrac{D}{ds}v=\tfrac{D}{dt}u=\xi$. Written as a first-order system:

:::tip[Proposition — closed-loop variational equations]
$$\frac{D}{dt}u=\xi,\qquad \frac{D}{dt}\xi=-\,\mathcal S_\alpha(u)-\mathcal D\,\xi,
\qquad \boxed{\ \mathcal S_\alpha\;:=\;\mathrm{Hess}^\sharp(V+\varphi)(q)\;+\;\mathrm{Jac}_v\ }$$
$\mathcal S_\alpha$ is the **curvature-corrected shaped stiffness**. It is $\mathbb G$-symmetric (both summands are), and it depends on the **full state $\alpha$**, not just on $q$ — because $\mathrm{Jac}_v$ carries $v=\mathbb G^\sharp\alpha$ quadratically.
:::

*Consistency check 1.* Put $V+\varphi\equiv0$ and $\mathcal D=0$: the system collapses to $\tfrac{D^2u}{dt^2}+R(u,v)v=0$, the Jacobi equation of [[07-jacobi-equation]] — as it must, since the unforced dynamics are the geodesic spray of $\mathbb G$. ✓

## The certificate

Use the cross-term metric of [[16-cross-term-metrics]] on $T^*Q$: for $a,c>0$, $ac>b^2$,

$$G_\alpha(w,w)\;=\;a\|u\|^2+2b\langle u,\xi\rangle+c\|\xi\|^2,\qquad w\leftrightarrow(u,\xi).$$

:::tip[Theorem — contraction certificate]
Let $\mathcal D=d\,\mathrm{id}$ and let $\mathcal W\subseteq T^*Q$ be open, forward invariant and $K$-reachable, with the closed-loop field forward complete on it. Suppose $0<\mu\le\sigma$ satisfy, uniformly on $\mathcal W$,
$$\mu\|u\|^2\le\langle\mathcal S_\alpha u,u\rangle,\qquad \|\mathcal S_\alpha u\|\le\sigma\|u\|
\qquad\text{i.e.}\qquad \mathrm{spec}(\mathcal S_\alpha)\subset[\mu,\sigma].$$
If
$$\boxed{\ d\;>\;\frac{\sigma-\mu}{2\sqrt\mu}\ }$$
then $G$ with $c=1$, $b=d/2$, $a=\tfrac{d^2}2+\tfrac{\mu+\sigma}2$ certifies contraction on $\mathcal W$ at rate
$$\lambda=\frac{\lambda_{\min}(\mathcal Q)}{\lambda_{\max}(\mathcal P)},\qquad
\mathcal Q=\begin{bmatrix}\tfrac{\mu d}2&-\tfrac\kappa2\\[2pt]-\tfrac\kappa2&\tfrac d2\end{bmatrix},\quad
\mathcal P=\begin{bmatrix}a&b\\b&c\end{bmatrix},\quad \kappa\le\tfrac{\sigma-\mu}2,$$
and hence $d_G(\Phi_t\alpha_0,\Phi_t\alpha_1)\le Ke^{-\lambda t}d_G(\alpha_0,\alpha_1)$ by [[@simpson-porcoContractionTheoryRiemannian2014]] Thm. 2.3.
:::

*Proof.* By [[14-contraction-on-manifolds]] it suffices to bound $\tfrac{d}{dt}G(w,w)$ along the variational system — no Levi-Civita connection of $G$ on the $2n$-manifold is needed. Since $a,b,c$ are constants and $\mathbb G$ is $\nabla$-parallel,

$$\tfrac12\tfrac{d}{dt}G(w,w)=a\langle\xi,u\rangle+b\|\xi\|^2+b\langle u,-\mathcal Su-d\xi\rangle+c\langle-\mathcal Su-d\xi,\xi\rangle .$$

Collecting with $\mathbb G$-symmetry of $\mathcal S$ (this is where symmetry is used — it lets $-c\langle\mathcal Su,\xi\rangle$ join $a\langle u,\xi\rangle-bd\langle u,\xi\rangle$ in one bilinear term):

$$\tfrac12\tfrac{d}{dt}G(w,w)=-b\langle\mathcal Su,u\rangle-(cd-b)\|\xi\|^2+\big\langle\big(a\,\mathrm{id}-bd\,\mathrm{id}-c\,\mathcal S_\alpha\big)u,\ \xi\big\rangle .$$

Set $\kappa:=\sup_{\mathcal W}\|a\,\mathrm{id}-bd\,\mathrm{id}-c\,\mathcal S_\alpha\|$. Then with $z=(\|u\|,\|\xi\|)^\top$,

$$\tfrac12\tfrac{d}{dt}G(w,w)\le-b\mu\|u\|^2-(cd-b)\|\xi\|^2+\kappa\|u\|\|\xi\|=-z^\top\mathcal Qz,
\qquad \mathcal Q=\begin{bmatrix}b\mu&-\kappa/2\\-\kappa/2&cd-b\end{bmatrix}.$$

Choosing $c=1$ and $a=bd+\tfrac{\mu+\sigma}2$ **centres** the residual operator: $a\,\mathrm{id}-bd\,\mathrm{id}-\mathcal S=\tfrac{\mu+\sigma}2\mathrm{id}-\mathcal S$, whose spectrum lies in $[-\tfrac{\sigma-\mu}2,\tfrac{\sigma-\mu}2]$, so $\kappa\le\tfrac{\sigma-\mu}2$. Now $\mathcal Q\succ0$ iff $b>0$, $b<d$ and $b\mu(d-b)>\kappa^2/4$. The left side is maximised at $b=d/2$, giving $\mu d^2/4>\kappa^2/4$, i.e. $d>\kappa/\sqrt\mu$, and the worst case $\kappa=\tfrac{\sigma-\mu}2$ is exactly the boxed condition. With $b=d/2$, $a=\tfrac{d^2}2+\tfrac{\mu+\sigma}2>\tfrac{d^2}4=b^2=b^2/c$, so $G$ is positive-definite. Finally $G(w,w)=z^\top\mathcal Pz\le\lambda_{\max}(\mathcal P)\|z\|^2$ and $z^\top\mathcal Qz\ge\lambda_{\min}(\mathcal Q)\|z\|^2$, so $\tfrac{d}{dt}G\le-2\lambda G$. $\square$

*Consistency check 2 (isotropic sanity check).* If $\mathcal S_\alpha=\mu\,\mathrm{id}$ then $\sigma=\mu$, $\kappa=0$, and the condition reads $d>0$: **any** damping works, provided the metric carries the cross term $b=d/2$. (With $\kappa=0$, $\mathcal Q=\mathrm{diag}(\mu d/2,\,d/2)\succ0$ for every $d>0$.) That is the intrinsic version of the damped oscillator of [[16-cross-term-metrics]], and it is the consistency check on the constant: the constant must vanish when the stiffness is isotropic, and $(\sigma-\mu)/(2\sqrt\mu)$ does. ✓

**Both checks reproduce, and the constant $(\sigma-\mu)/(2\sqrt\mu)$ is confirmed by independent rederivation** — the draft's algebra is correct as printed.

## Reading the condition

By the Proposition and [[07-jacobi-equation]] property (3),

$$\langle\mathcal S_\alpha u,u\rangle=\mathrm{Hess}(V+\varphi)(u,u)+\mathrm{Sec}(u,v)\big(\|u\|^2\|v\|^2-\langle u,v\rangle^2\big).$$

**1. Positive curvature helps.** Where $\mathrm{Sec}\ge0$ the curvature term *adds* to the effective stiffness. This is geodesic deviation read as control: neighbouring geodesics focus, and the focusing does part of the controller's work. On a bi-invariant metric $\mathrm{Sec}(X,Y)=\tfrac14\|[X,Y]\|^2\ge0$ ([[06-curvature-left-invariant-metrics]]), e.g. $SO(3)$ with $\mathbb J=j\,\mathrm{id}$: there $\mathrm{Jac}_v=\tfrac{\|v\|^2}{4j}\cdot\mathrm{id}$ on $v^\perp$ is a free stiffness bonus growing with speed.

**2. Negative curvature bounds $\mathcal W$ in velocity.** If $\mathrm{Sec}\ge\mathrm{Sec}_-$ with $\mathrm{Sec}_-<0$,

$$\mu\;\ge\;\lambda_{\min}\big(\mathrm{Hess}^\sharp(V+\varphi)\big)-|\mathrm{Sec}_-|\,\sup_{\mathcal W}\|v\|^2
\qquad\Longrightarrow\qquad
\sup_{\mathcal W}\|v\|^2<\frac{\lambda_{\min}\big(\mathrm{Hess}^\sharp(V+\varphi)\big)}{|\mathrm{Sec}_-|},$$

since the theorem requires $\mu>0$. **Damping cannot repair this.** $\mathcal D$ enters only the $\xi$-block of the variational system, whereas $\mu$ lives in the $u$-block; raising $d$ changes the $\mathcal Q$-entries but cannot make $\mu$ positive. Enlarging the region needs **stiffer shaping**, not more damping. And [[06-curvature-left-invariant-metrics]] showed this case is live: $SO(3)$ with $\mathbb J=\mathrm{diag}(1,2,3)$ — a physical flat lamina — has principal curvatures $(-\tfrac13,+\tfrac13,+\tfrac13)$.

**3. Topology bounds $\mathcal W$ too.** Contraction regions are contractible ([[14-contraction-on-manifolds]], after Bhat–Bernstein), and $T^*Q$ deformation-retracts onto $Q$. So $\mathcal W$ can never be all of $T^*Q$ when $Q$ is not contractible — $SO(3)$, $S^2$, $\mathbb T^n$. Contraction designs on such $Q$ are unavoidably local, for the same reason smooth global stabilisation is impossible.

## Worked example — $SO(3)$ attitude tracking

Rigid body, $\mathbb J=\mathrm{diag}(1,2,3)$, so $\mathrm{Sec}_-=-\tfrac13$ on the $(f_1,f_2)$ plane and $+\tfrac13$ on the other two. Take $V\equiv0$ (torque-free) and a shaping potential with $\mathrm{spec}\big(\mathrm{Hess}^\sharp\varphi\big)\subset[4,6]\ \mathrm{s}^{-2}$ on the region. Recall $\|v\|^2_{\mathbb G}=\Omega^\top\mathbb J\Omega$, *not* $|\Omega|^2$.

**Velocity cap (consequence 2).**

$$\sup_{\mathcal W}\|v\|^2\;<\;\frac{4}{1/3}\;=\;12\ \mathrm{rad^2/s^2},
\qquad\text{i.e.}\qquad \Omega^\top\mathbb J\Omega<12 .$$

Since $|\Omega|^2\le\Omega^\top\mathbb J\Omega\le3|\Omega|^2$, the **guaranteed-safe ball is $|\Omega|<2\ \mathrm{rad/s}$**, and even along the softest axis no contraction region can reach $|\Omega|=\sqrt{12}\approx3.46\ \mathrm{rad/s}$.

**A certificate inside it.** Design for $\sup_{\mathcal W}\|v\|^2=6$ (half the cap). Then

$$\mu\ge4-\tfrac13(6)=2,\qquad \sigma\le6+\tfrac13(6)=8,\qquad
d>\frac{8-2}{2\sqrt2}=\frac{3}{\sqrt2}\approx2.121 .$$

Take $d=2.5$. Then $\kappa\le3$, $b=1.25$, $c=1$, $a=\tfrac{6.25}2+5=8.125$, and

$$\mathcal Q=\begin{bmatrix}2.5&-1.5\\-1.5&1.25\end{bmatrix}\ \Rightarrow\ \mathrm{spec}=\{3.5,\ 0.25\},
\qquad
\mathcal P=\begin{bmatrix}8.125&1.25\\1.25&1\end{bmatrix}\ \Rightarrow\ \lambda_{\max}\approx8.338,$$

so $\lambda\approx0.25/8.338\approx0.030\ \mathrm{s^{-1}}$ — a contraction time constant of about $33$ s.

:::warning[Open question]
That rate is *very* conservative relative to $d=2.5$: the bottleneck is $\kappa\le(\sigma-\mu)/2$, a worst-case operator norm taken uniformly over $\mathcal W$, whereas $\mathcal S_\alpha$ is anisotropic in a *known* way ($\mathrm{Jac}_v$ annihilates $v$ and is largest on $v^\perp$). Constant $a,b,c$ cannot exploit that. Whether state-dependent coefficients $A,B,C$ on $Q$ recover a rate comparable to $d$ — at the cost of a PDE-like condition on them — is open, and is the same conservatism-vs-tightness question the thesis asks of the tube bounds.

Second: $\sigma$ also grows like $|\mathrm{Sec}|\sup\|v\|^2$, so the required damping $d>(\sigma-\mu)/(2\sqrt\mu)$ blows up as the region approaches the velocity cap from **both** ends — $\sigma\uparrow$ and $\mu\downarrow0$.
:::

**Which kind is this?** Entirely intrinsic. Every constant in the theorem is $\mathrm{spec}(\mathcal S_\alpha)$, and $\mathcal S_\alpha=\mathrm{Hess}^\sharp(V+\varphi)+\mathrm{Jac}_v$ is built from the Hessian and the curvature tensor. No $\sup|\partial g_{ij}|$ appears anywhere — the chart-dependent route to the same statement would write the variational equation in coordinates and pick up Christoffel derivative bounds in place of $\mathrm{Jac}_v$.

## Problems

1. **Recall.** State the closed-loop variational system and define $\mathcal S_\alpha$. Say precisely which hypothesis kills each of: the $\tfrac{D}{ds}\mathcal D$ term; the non-symmetric part of the stiffness; the obstruction of [[15-symplectic-not-contracting]]. Then state the contraction condition and say why it is *not* enough to make $\mathcal D$ large.

2. **Compute.** $SO(3)$ with $\mathbb J=\mathrm{diag}(1,1,2)$ (principal curvatures $-\tfrac12,+\tfrac12,+\tfrac12$ from [[06-curvature-left-invariant-metrics]] problem 2). With $V\equiv0$ and $\mathrm{spec}(\mathrm{Hess}^\sharp\varphi)\subset[3,5]$, find the cap on $\sup_{\mathcal W}\|v\|^2$, the corresponding bound on $|\Omega|$ that is guaranteed safe, and — designing at $\sup\|v\|^2=3$ — the minimum admissible $d$.

3. **Prove.** (a) Show $\mathcal S_\alpha$ is $\mathbb G$-symmetric, citing the source of symmetry of each summand. (b) Show that if $\mathcal S_\alpha=\mu\,\mathrm{id}$ then every $d>0$ certifies contraction, and compute the resulting $\lambda$ in closed form as a function of $\mu$ and $d$.

4. **Break it.** Same body as the worked example, but isotropic shaping $\mathrm{Hess}^\sharp\varphi=4\,\mathrm{id}$. Exhibit an explicit $v$ (give $\Omega$ in rad/s and the axis) and a $u$ for which $\langle\mathcal S_\alpha u,u\rangle\le0$. Conclude that no $d>0$ whatsoever certifies contraction on a region containing that state, and say in one sentence which hypothesis of the theorem fails.

---

## Solutions

**1.** System: $\tfrac{D}{dt}u=\xi$, $\tfrac{D}{dt}\xi=-\mathcal S_\alpha(u)-\mathcal D\xi$ with $\mathcal S_\alpha=\mathrm{Hess}^\sharp(V+\varphi)+\mathrm{Jac}_v$. *Parallel damping* $\nabla\mathcal D=0$ kills $(\nabla_u\mathcal D)v$. *$\mathbb G$-symmetry* of $\mathrm{Hess}^\sharp$ and of $\mathrm{Jac}_v$ makes $\mathcal S_\alpha$ symmetric, which is what lets the cross terms collect in the proof; a skew part would only inflate $\kappa$. *The damping term itself* breaks the symplectic structure, without which [[15-symplectic-not-contracting]] forbids contraction outright. Condition: $d>(\sigma-\mu)/(2\sqrt\mu)$, and it is not enough to raise $d$ because the condition presupposes $\mu>0$ — an $u$-block property that $\mathcal D$ never touches.

**2.** $|\mathrm{Sec}_-|=\tfrac12$, $\lambda_{\min}(\mathrm{Hess}^\sharp\varphi)=3$, so $\sup\|v\|^2<3/(1/2)=6$. Here $\|v\|^2=\Omega^\top\mathrm{diag}(1,1,2)\Omega\le2|\Omega|^2$, so $|\Omega|<\sqrt3\approx1.73\ \mathrm{rad/s}$ is guaranteed. At $\sup\|v\|^2=3$: $\mu\ge3-\tfrac32=\tfrac32$, $\sigma\le5+\tfrac32=\tfrac{13}2$, so $d>(6.5-1.5)/(2\sqrt{1.5})=5/2.449\approx2.04$.

**3.** (a) $\mathrm{Hess}^\sharp\psi=\nabla\,\mathrm{grad}\,\psi$ is self-adjoint because $\mathrm{Hess}\,\psi$ is a symmetric $(0,2)$-tensor ([[08-hessian-comparison]]); $\mathrm{Jac}_v$ is self-adjoint by pair symmetry (S4) of $R$ ([[07-jacobi-equation]] Prop. 1). A sum of self-adjoint endomorphisms is self-adjoint.
(b) $\sigma=\mu$ makes the centred residual $a\,\mathrm{id}-bd\,\mathrm{id}-\mathcal S=\mu\,\mathrm{id}-\mu\,\mathrm{id}=0$, so $\kappa=0$ and $\mathcal Q=\mathrm{diag}(\mu d/2,\ d/2)$, positive-definite for every $d>0$; the condition $d>0/(2\sqrt\mu)=0$ is vacuous. Then $\lambda_{\min}(\mathcal Q)=\tfrac d2\min(\mu,1)$. With $b=d/2$, $c=1$, $a=\tfrac{d^2}2+\mu$: $\lambda_{\max}(\mathcal P)=\tfrac12\big(a+1+\sqrt{(a-1)^2+d^2}\big)$, so
$$\lambda=\frac{d\,\min(\mu,1)}{a+1+\sqrt{(a-1)^2+d^2}},\qquad a=\tfrac{d^2}2+\mu .$$
For large $d$ this behaves like $d\min(\mu,1)/(d^2/2)\to0$: over-damping *destroys* the certified rate, which is the correct physics.

**4.** Take $u$ and $v$ spanning the negatively curved plane: $v=\sqrt{12}\,f_2$ where $f_2=\hat e_2/\sqrt{J_2}=\hat e_2/\sqrt2$, i.e. $\Omega=\sqrt6\,e_2\approx2.449\ \mathrm{rad/s}$ **about the intermediate axis**, and $u=f_1$ (orthonormal, so the Gram factor $\|u\|^2\|v\|^2-\langle u,v\rangle^2=\|v\|^2=12$). Then
$$\langle\mathcal S_\alpha u,u\rangle=4+\mathrm{Sec}(f_1,f_2)\cdot12=4-\tfrac13\cdot12=0 .$$
Any $\|\Omega\|$ beyond this on that axis makes it strictly negative. The hypothesis that fails is $\mu>0$ — there is no positive $\mu$ with $\mu\|u\|^2\le\langle\mathcal S_\alpha u,u\rangle$ on a region containing this state — and $d>(\sigma-\mu)/(2\sqrt\mu)$ is then unsatisfiable for *every* $d$, since its right-hand side is $+\infty$ as $\mu\downarrow0$. Damping is powerless: the variational system has a genuine negative-stiffness direction, and a negative-stiffness oscillator with any damping still has an unstable eigenvalue.
