---
tags: [mechanics, symplectic, cotangent-bundle, control]
---
# The Hamiltonian Side on $T^*Q$

**Prereq:** [[mechanical-systems-on-lie-groups]] (forms, exterior derivative, symplectic form, tautological one-form), [[riemannian-geometry]] (musical isomorphisms), [[02-trivialization-of-tg]]; notation fixed in [[notation]].
**Goal:** move a simple mechanical system from $TQ$ to $T^*Q$, prove $\mathcal L_{X_H}\omega_0=0$ and $\mathrm{div}_\Lambda X_H=0$ in two lines each, and locate exactly which forces preserve that structure — because every useful feedback will have to destroy it.

Throughout $Q$ is the configuration manifold, $\dim Q=n$, with a Riemannian metric $\mathbb G$ supplied by the kinetic energy. On a Lie group $Q=G$ and $\mathbb G$ is the left-invariant metric of [[notation]]. Nothing below needs $Q$ to be a group; the group structure re-enters in lesson 11.

## From $TQ$ to $T^*Q$

:::info[Definition]
A **simple mechanical system** is $(Q,\mathbb G,V)$ with Lagrangian $L(v_q)=\tfrac12\mathbb G(v_q,v_q)-V(q)$. Its **Legendre transform** is the fibre derivative
$$\mathbb F L=\mathbb G^\flat : TQ\to T^*Q,\qquad v_q\mapsto \mathbb G(v_q,\cdot).$$
:::

:::tip[Proposition — hyperregularity]
$\mathbb G\succ0$ makes $\mathbb G^\flat$ a fibrewise linear isomorphism at every $q$, hence a diffeomorphism $TQ\to T^*Q$ over $\mathrm{id}_Q$, with inverse $\mathbb G^\sharp$. The system is **hyperregular**: Lagrangian and Hamiltonian descriptions carry the same information.
:::

*Proof.* Positive-definiteness is exactly injectivity of $\mathbb G^\flat_q$ on each fibre; equal finite dimensions give surjectivity. Smoothness of $\mathbb G$ and of matrix inversion give smoothness both ways. $\square$

The point of *hyper*regularity is that $\mathbb F L$ is a global diffeomorphism, not merely a local one — so there is one $H$ on all of $T^*Q$, no branch choices. This is where $\mathbb G\succ0$ is spent, and it is the only place it is needed in this lesson. Note the type discipline of [[01-adjoint-and-coadjoint]] surviving intact: velocities live in $TQ$, momenta in $T^*Q$, and $\mathbb G^\flat$ is the *extra input* that relates them.

:::info[Definition]
The **Hamiltonian** of a simple mechanical system is
$$H:T^*Q\to\mathbb R,\qquad H(\alpha_q)=\tfrac12\big\langle\alpha_q,\mathbb G^\sharp\alpha_q\big\rangle+V(q)=\tfrac12\|\alpha_q\|^2_{\mathbb G^{-1}}+V(q),$$
with $\langle\cdot,\cdot\rangle$ the metric-free pairing. It is $H=\langle\alpha_q,v_q\rangle-L(v_q)$ evaluated at $v_q=\mathbb G^\sharp\alpha_q$.
:::

## Canonical structures

$\theta_0\in\Omega^1(T^*Q)$ is the tautological one-form of [[mechanical-systems-on-lie-groups]]: with $\pi:T^*Q\to Q$ the bundle projection (in this lesson only — [[notation]] reserves $\pi$ for spatial momentum, which does not appear here),
$$\big\langle\theta_0(\alpha_q),\,w\big\rangle=\big\langle\alpha_q,\,T_{\alpha_q}\pi(w)\big\rangle,\qquad w\in T_{\alpha_q}(T^*Q),$$
and $\omega_0:=-d\theta_0$. In **natural coordinates** $(q^i,p_i)$ — a chart $q$ on $Q$ together with the induced fibre coordinates $\alpha=p_i\,dq^i$ —
$$\theta_0=p_i\,dq^i,\qquad \omega_0=-dp_i\wedge dq^i=dq^i\wedge dp_i.$$

:::info[Definition]
The **Hamiltonian vector field** $X_H\in\Gamma(T(T^*Q))$ is the unique solution of $\iota_{X_H}\omega_0=dH$.
:::

Uniqueness *and* existence are exactly non-degeneracy of $\omega_0$: the map $X\mapsto\iota_X\omega_0$ from $T_\alpha(T^*Q)$ to $T^*_\alpha(T^*Q)$ is a linear map between spaces of equal dimension, injective iff $\omega_0$ is non-degenerate, hence then bijective. Without non-degeneracy $dH$ need not be in the image and the equation has no solution — this is the sense in which "$\omega_0$ turns $dH$ into a vector field", and it is why the cotangent bundle, being even-dimensional with a canonical non-degenerate form, is the arena.

## Worked example: a particle on $\mathbb R^n$

Take $Q=\mathbb R^n$ with constant mass matrix $M=M^\top\succ0$, so $\mathbb G(u,v)=u^\top Mv$, and potential $V$. Then $\mathbb G^\flat v=Mv$, hyperregular because $M$ is invertible, and
$$H(q,p)=\tfrac12 p^\top M^{-1}p+V(q).$$
Write $X_H=\dot q^i\,\partial/\partial q^i+\dot p_i\,\partial/\partial p_i$ and contract. Since $\iota_X(\eta\wedge\zeta)=(\iota_X\eta)\zeta-(\iota_X\zeta)\eta$ for one-forms,
$$\iota_{X_H}\omega_0=\iota_{X_H}(dq^i\wedge dp_i)=\dot q^i\,dp_i-\dot p_i\,dq^i,\qquad
dH=\frac{\partial H}{\partial q^i}dq^i+\frac{\partial H}{\partial p_i}dp_i.$$
Matching the coefficients of the basis one-forms $dq^i$ and $dp_i$ separately gives **Hamilton's equations**
$$\dot q^i=\frac{\partial H}{\partial p_i},\qquad \dot p_i=-\frac{\partial H}{\partial q^i},$$
here $\dot q=M^{-1}p$ and $\dot p=-\nabla V(q)$ — i.e. $M\ddot q=-\nabla V$, Newton. The sign asymmetry is not a convention artifact; it is the skewness of $\omega_0$, and it is the whole reason the flow preserves volume.

For the free rigid body the same $H$ reads, in the left-trivialized coordinates $(R,\Pi)\in SO(3)\times\mathbb R^3$ of [[02-trivialization-of-tg]], $H(R,\Pi)=\tfrac12\Pi^\top\mathbb J^{-1}\Pi$ with $\Pi=\mathbb J\Omega$ — hyperregular because $\mathbb J\succ0$. But $\omega_0$ is *not* $dq^i\wedge dp_i$ in those coordinates: it picks up a $\langle\mu,[\eta_1,\eta_2]\rangle$ term, which is lesson 11.

## The flow preserves everything canonical

:::tip[Proposition — symplecticity of the drift]
$\mathcal L_{X_H}\omega_0=0$. Hence the flow $\Phi^{X_H}_t$ satisfies $(\Phi^{X_H}_t)^*\omega_0=\omega_0$, and the **Liouville volume** $\Lambda:=\tfrac{1}{n!}\omega_0^{\wedge n}$ is preserved: $\mathcal L_{X_H}\Lambda=0$, i.e. $\mathrm{div}_\Lambda X_H=0$.
:::

*Proof.* Cartan's magic formula $\mathcal L_X=d\,\iota_X+\iota_X\,d$ (valid on any form, any manifold; no metric, no connection) gives
$$\mathcal L_{X_H}\omega_0=d\,\iota_{X_H}\omega_0+\iota_{X_H}\,d\omega_0.$$
The second term dies because $\omega_0=-d\theta_0$ is exact, hence closed: $d\omega_0=-d^2\theta_0=0$. The first dies because $\iota_{X_H}\omega_0=dH$ is exact: $d(dH)=0$. Both terms are killed by $d^2=0$, applied once to $\theta_0$ and once to $H$. For the volume, $\mathcal L_X$ is a derivation over $\wedge$, so $\mathcal L_{X_H}\Lambda=\tfrac{1}{(n-1)!}(\mathcal L_{X_H}\omega_0)\wedge\omega_0^{\wedge(n-1)}=0$. $\square$

Cross-check in natural coordinates, where $\Lambda=dq^1\wedge dp_1\wedge\cdots\wedge dq^n\wedge dp_n$ is the coordinate volume, so $\mathrm{div}_\Lambda X=\partial a^i/\partial q^i+\partial b_i/\partial p_i$ for $X=a^i\partial_{q^i}+b_i\partial_{p_i}$. For $X_H$ this is $\partial^2H/\partial q^i\partial p_i-\partial^2H/\partial p_i\partial q^i=0$ by equality of mixed partials.

**Which of the three kinds?** $\theta_0$, $\omega_0$, $\Lambda$ and $X_H$ are **intrinsic**, and in the strong sense of [[01-adjoint-and-coadjoint]]: no chart, no metric, no connection enters their definitions, so they cannot contribute a $\sup|\partial g_{ij}|$-type constant to any bound. The natural coordinates $(q^i,p_i)$ are chart-dependent but harmless — the expression $\omega_0=dq^i\wedge dp_i$ holds in *every* natural chart simultaneously. Only $H$ needs $\mathbb G$, and that is a physical input, not a coordinate choice.

## Where the controls enter

:::info[Definition]
For $\beta\in T^*_qQ$ and $\alpha\in T^*_qQ$, the **vertical lift** is the fibre derivative
$$\mathrm{ver}_\alpha(\beta)=\left.\frac{d}{d\varepsilon}\right|_{\varepsilon=0}(\alpha+\varepsilon\beta)\in T_\alpha(T^*Q);$$
in natural coordinates $\mathrm{ver}(\beta)=\beta_i\,\partial/\partial p_i$. It is well defined because a fibre of $T^*Q$ is a vector space and is canonically its own tangent space.
:::

:::tip[Lemma]
For a one-form $\beta\in\Omega^1(Q)$, $\ \iota_{\mathrm{ver}(\beta)}\omega_0=-\pi^*\beta$.
:::

*Proof.* In natural coordinates $\iota_{\beta_i\partial_{p_i}}(dq^j\wedge dp_j)=-\beta_i\,dq^i=-\pi^*\beta$, since $\partial_{p_i}$ annihilates every $dq^j$ and $\pi^*(dq^i)=dq^i$. $\square$

A force $\beta$ enters the dynamics as $X=X_H+\mathrm{ver}(\beta)$; an actuated system with inputs is $X_\Sigma=X_H+\sum_a u^a\,\mathrm{ver}(F^a)$.

:::tip[Corollary — which forces are symplectic]
$\mathrm{ver}(\beta)$ preserves $\omega_0$ iff $\pi^*\beta$ is closed, i.e. iff $\beta$ is **locally a potential force** $\beta=-dV_c$. Every dissipative or velocity-dependent feedback therefore breaks $\omega_0$.
:::

*Proof.* $\mathcal L_{\mathrm{ver}(\beta)}\omega_0=d\,\iota_{\mathrm{ver}(\beta)}\omega_0=-d\pi^*\beta=-\pi^*d\beta$, using Cartan, $d\omega_0=0$ and $d\pi^*=\pi^*d$. This vanishes iff $d\beta=0$ ($\pi$ is a submersion, so $\pi^*$ is injective on forms), which by the Poincaré lemma is local exactness. $\square$

Read the corollary the right way round. A potential force is not really a new force at all — problem 3 shows it is absorbed into $H$. So *nothing* outside the original Hamiltonian family preserves $\omega_0$. Damping, velocity feedback, an observer innovation term: all of them are non-closed, all of them break $\omega_0$, and problem 4 computes by how much.

That is not a defect of clumsy design. Lesson 15 shows the converse direction — a symplectic flow can never be contracting, because $\mathrm{div}_\Lambda X=0$ forbids the volume decay that contraction forces (cf. [[@simpson-porcoContractionTheoryRiemannian2014]] Prop. 2.5(iv), where contraction gives $\mathrm{div}\,X\le-n\lambda$). Breaking $\omega_0$ is a *requirement* on the feedback, not a side effect.

:::warning[Open question]
$\mathrm{div}_\Lambda$ and the divergence with respect to a Riemannian volume on $T^*Q$ are different functionals in general, and lesson 15's contraction condition is stated with the latter. For the Sasaki metric (lesson 13) the two volumes should coincide — horizontal and vertical blocks contribute $\det\mathbb G$ and $\det\mathbb G^{-1}$ — but for the cross-term $g$-natural metrics that lesson 16 says are the only ones that can certify, they need not. Until that is checked, do not transport "$\mathrm{div}_\Lambda X_H=0$" into a contraction estimate as if the volumes were the same.
:::

## Problems

1. **Recall.** State hyperregularity and say precisely where $\mathbb G\succ0$ is used. Write $H$ for a simple mechanical system in both the pairing form and the $\|\cdot\|_{\mathbb G^{-1}}$ form. Then state the defining equation for $X_H$ and explain, in one sentence, what goes wrong if $\omega_0$ is degenerate.

2. **Compute.** Free rigid body on $SO(3)$: with $\hat\Omega=R^\top\dot R$ and $L=\tfrac12\Omega^\top\mathbb J\Omega$, $\mathbb J\succ0$, compute $\mathbb F L$ in the left-trivialized coordinates of [[02-trivialization-of-tg]], identify the momentum it produces, verify hyperregularity, and write $H$. Then say why the Legendre transform is insensitive to which trivialization you use, while the resulting *expression* for $H$ is not.

3. **Prove.** (a) $H$ is conserved: $X_H[H]=0$. (b) Let $V_c\in C^\infty(Q)$ and $\beta=-dV_c$. Show $X_H+\mathrm{ver}(\beta)=X_{H'}$ with $H'=H+V_c\circ\pi$ — a potential force is a relabelling of $H$, not a new object.

4. **Break it.** Linear damping on $Q=\mathbb R^n$, $\mathbb G=M$ constant. The force is $\beta=-D\,v$ with $D=D^\top\succ0$ and $v=\mathbb G^\sharp\alpha$ the velocity, so in natural coordinates $\beta_i=-(DM^{-1}p)_i$ and $Y:=\mathrm{ver}(\beta)$.
   (a) Show $\beta$ is *not* the pullback of a one-form on $Q$, so the lemma does not apply, and compute $\iota_Y\omega_0$ directly.
   (b) Compute $\mathcal L_Y\omega_0$ and exhibit it as nonzero. For $n=1$, $M=m$, $D=d$, show $\mathcal L_Y\omega_0=-(d/m)\,\omega_0$.
   (c) Compute $\mathrm{div}_\Lambda(X_H+Y)$ and deduce the exponential rate at which the Liouville volume of any region contracts.

---

## Solutions

**1.** Hyperregular: $\mathbb F L=\mathbb G^\flat:TQ\to T^*Q$ is a global diffeomorphism. $\mathbb G\succ0$ is used once, for fibrewise injectivity of $\mathbb G^\flat_q$; equal finite fibre dimensions then give bijectivity, and smoothness of inversion gives the smooth inverse $\mathbb G^\sharp$. $H(\alpha_q)=\tfrac12\langle\alpha_q,\mathbb G^\sharp\alpha_q\rangle+V(q)=\tfrac12\|\alpha_q\|^2_{\mathbb G^{-1}}+V(q)$. $X_H$ solves $\iota_{X_H}\omega_0=dH$. If $\omega_0$ were degenerate, $X\mapsto\iota_X\omega_0$ would have nontrivial kernel, hence non-full image: $X_H$ would be non-unique where it exists and, for a $dH$ outside the image, would not exist at all.

**2.** The fibre derivative is taken along the fibre $T_RSO(3)$; in the coordinates $(R,\Omega)$ the fibre is $\mathbb R^3$ and $\partial L/\partial\Omega=\mathbb J\Omega=\Pi$, the body angular momentum of [[notation]]. So $\mathbb FL(R,\Omega)=(R,\Pi)$, linear on each fibre with matrix $\mathbb J$. Hyperregular because $\mathbb J=\mathbb J^\top\succ0$ is invertible, uniformly in $R$ since it is constant in the body frame. Then $H(R,\Pi)=\langle\Pi,\Omega\rangle-L=\Pi^\top\mathbb J^{-1}\Pi-\tfrac12\Pi^\top\mathbb J^{-1}\Pi=\tfrac12\Pi^\top\mathbb J^{-1}\Pi$. $\mathbb FL=\mathbb G^\flat$ is defined by $\mathbb G$ alone and is a map $TQ\to T^*Q$ — no trivialization appears in its definition. But $\lambda$ and $\lambda^*$ are the two different bundle isomorphisms that turn it into a formula: in the body picture $H=\tfrac12\Pi^\top\mathbb J^{-1}\Pi$ with $\mathbb J$ constant, in the spatial picture the momentum is $\mathrm{Ad}^*_{R^{-1}}\Pi$ and the inertia becomes the $R$-dependent $R\mathbb JR^\top$. Same function, two expressions; the body one is the reason to use left trivialization.

**3(a).** $X_H[H]=dH(X_H)=(\iota_{X_H}\omega_0)(X_H)=\omega_0(X_H,X_H)=0$ by skew-symmetry of $\omega_0$. No coordinates, no metric — energy conservation is a consequence of skewness alone, which is why it survives on any symplectic manifold.

**3(b).** By the lemma, $\iota_{\mathrm{ver}(\beta)}\omega_0=-\pi^*\beta=\pi^*(dV_c)=d(\pi^*V_c)=d(V_c\circ\pi)$. Contraction is linear in the vector field, so
$$\iota_{X_H+\mathrm{ver}(\beta)}\omega_0=dH+d(V_c\circ\pi)=d\big(H+V_c\circ\pi\big),$$
and by uniqueness of the solution of $\iota_X\omega_0=d(\cdot)$ (non-degeneracy again), $X_H+\mathrm{ver}(\beta)=X_{H'}$ with $H'=H+V_c\circ\pi$. Consistent with the definition of $H$: adding $V_c$ to the potential $V$ does exactly this.

**4(a).** $\pi^*$ of a one-form on $Q$ has coefficients depending on $q$ only, whereas $\beta_i=-(DM^{-1}p)_i$ depends on $p$; so $\beta$ is a fibrewise-defined one-form along $\pi$, not a pullback, and the lemma's hypothesis fails. Directly, $Y=-(DM^{-1}p)_i\,\partial/\partial p_i$, and
$$\iota_Y\omega_0=\iota_Y(dq^i\wedge dp_i)=-(-(DM^{-1}p)_i)\,dq^i=(DM^{-1}p)_i\,dq^i.$$

**4(b).** $d\omega_0=0$, so Cartan gives $\mathcal L_Y\omega_0=d\,\iota_Y\omega_0=d\big((DM^{-1}p)_i\,dq^i\big)=(DM^{-1})_i{}^{\,j}\,dp_j\wedge dq^i=-(DM^{-1})_i{}^{\,j}\,dq^i\wedge dp_j\neq0$, since $DM^{-1}$ is invertible so no coefficient matrix vanishes. For $n=1$: $\iota_Y\omega_0=(d/m)p\,dq$, so $\mathcal L_Y\omega_0=(d/m)\,dp\wedge dq=-(d/m)\,dq\wedge dp=-(d/m)\,\omega_0$. The symplectic form is not merely perturbed — it is scaled down exponentially along the flow.

**4(c).** In natural coordinates $\mathrm{div}_\Lambda(X_H+Y)=\mathrm{div}_\Lambda X_H+\partial\beta_i/\partial p_i=0-\mathrm{tr}(DM^{-1})<0$, strictly negative because $D\succ0$ and $M\succ0$ give $\mathrm{tr}(DM^{-1})=\mathrm{tr}(M^{-1/2}DM^{-1/2})>0$. Hence $\mathcal L_{X_H+Y}\Lambda=-\mathrm{tr}(DM^{-1})\Lambda$ and $\frac{d}{dt}\mathrm{Vol}_\Lambda(\Phi_t(A))=-\mathrm{tr}(DM^{-1})\,\mathrm{Vol}_\Lambda(\Phi_t(A))$, so $\mathrm{Vol}_\Lambda(\Phi_t(A))=e^{-\mathrm{tr}(DM^{-1})t}\,\mathrm{Vol}_\Lambda(A)$. The rate is constant and does not depend on $V$ — the potential is $p$-independent and contributes nothing to the divergence. This is the computation Phase 3 rests on: damping buys volume contraction at exactly the price of $\omega_0$.
