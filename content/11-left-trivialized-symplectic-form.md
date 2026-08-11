---
tags: [mechanics, symplectic, lie-groups, connections]
---
# The Left-Trivialized Canonical Symplectic Form

**Prereq:** [[mechanical-systems-on-lie-groups]] (tautological one-form, $\iota_{X_H}\omega=dH$), [[09-hamiltonian-on-cotangent]] ($\omega_0=-d\theta_0$, natural coordinates), [[10-euler-poincare]], [[02-trivialization-of-tg]], [[01-adjoint-and-coadjoint]], [[notation]].
**Goal:** write $\omega_0$ in the coordinates $(g,\mu)$ on $T^*G\cong G\times\mathfrak g^*$, know why a bracket term appears, and know why that does **not** contradict the correction-free formula obtained from the Levi-Civita splitting.

This lesson answers the open question in [[mechanical-systems-on-lie-groups]] § Symplectic form — *"does the canonical $\omega$ stay canonical in left-trivialized coordinates, or pick up structure constants?"* The answer is: **it picks up structure constants.** And the reason is not an accident of bookkeeping; it is the torsion of the connection hidden inside the word "trivialized".

## Coordinates

:::info[Definition]
Left-trivialize $T^*G\cong G\times\mathfrak g^*$ by $\alpha_g\mapsto(g,\mu)$, $\mu=T^*_eL_g\alpha_g$ (this is $\lambda^*$ of [[02-trivialization-of-tg]]). A tangent vector to $T^*G$ at $(g,\mu)$ is represented by a pair
$$(\eta,\nu)\in\mathfrak g\times\mathfrak g^*, \qquad \eta = g^{-1}\dot g,\quad \nu=\dot\mu,$$
computed along any curve $s\mapsto(g(s),\mu(s))$ through the point. Both components are honest: $\mathfrak g^*$ is a fixed vector space, so $\dot\mu$ needs no identification.
:::

Throughout, $\pi:T^*G\to G$ is the **bundle projection**, per the overloading warning in [[notation]]; spatial momentum does not appear in this lesson. The tautological one-form $\theta_{\alpha_g}(w)=\langle\alpha_g,T\pi(w)\rangle$ trivializes instantly: $T\pi(\eta,\nu)=\dot g=g\eta$, so

$$\theta_{(g,\mu)}(\eta,\nu)=\langle\alpha_g,g\eta\rangle=\langle\mu,\eta\rangle,
\qquad\text{i.e.}\qquad \theta=\langle\mu,\ g^{-1}dg\rangle .$$

$\theta$ *is* canonical-looking in these coordinates — it is $\langle\mu,\cdot\rangle$ against the Maurer–Cartan form. The bracket enters only on differentiating, because $g^{-1}dg$ is not closed.

## The form

:::tip[Theorem — left-trivialized canonical form]
With $\omega_0=-d\theta$,
$$\omega_0\big((\eta_1,\nu_1),(\eta_2,\nu_2)\big)\Big|_{(g,\mu)}
=\langle\nu_2,\eta_1\rangle-\langle\nu_1,\eta_2\rangle+\langle\mu,[\eta_1,\eta_2]\rangle .$$
The third term is base-point dependent (through $\mu$) and vanishes identically iff $\mathfrak g$ is abelian.
:::

*Proof.* Evaluate $d\theta$ with the invariant formula $d\theta(W_1,W_2)=W_1(\theta(W_2))-W_2(\theta(W_1))-\theta([W_1,W_2])$ on the vector fields $W_i=(X_{\eta_i},\nu_i)$ on $G\times\mathfrak g^*$, with $\eta_i\in\mathfrak g$ and $\nu_i\in\mathfrak g^*$ **constant** — i.e. left-invariant in the base, constant in the fibre. These have value $(\eta_i,\nu_i)$ at every point, so they realise the given tangent vectors.

- $\theta(W_2)=\langle\mu,\eta_2\rangle$ is a linear function of the fibre coordinate alone, and $W_1$ has fibre component $\nu_1$, so $W_1(\theta(W_2))=\langle\nu_1,\eta_2\rangle$. Symmetrically $W_2(\theta(W_1))=\langle\nu_2,\eta_1\rangle$.
- The fibre components are constant and the base fields are left-invariant, so $[W_1,W_2]=(X_{[\eta_1,\eta_2]},0)$, using $[X_{\eta_1},X_{\eta_2}]=X_{[\eta_1,\eta_2]}$ (matrix commutator, [[01-adjoint-and-coadjoint]]). Hence $\theta([W_1,W_2])=\langle\mu,[\eta_1,\eta_2]\rangle$.

So $d\theta(W_1,W_2)=\langle\nu_1,\eta_2\rangle-\langle\nu_2,\eta_1\rangle-\langle\mu,[\eta_1,\eta_2]\rangle$, and $\omega_0=-d\theta$ gives the claim. $\square$

The bracket term comes from exactly one place: **the trivializing frame does not commute.** In a canonical chart $(q^i,p_i)$ the coordinate fields commute and $\theta([W_1,W_2])=0$; the left-invariant frame $E_i(g)=ge_i$ closes on itself with structure constants instead, and $\theta$ eats them.

## The two splittings — this is the point

A second-order or Hamiltonian formula on $T^*G$ never sees $\omega_0$ alone; it sees $\omega_0$ *written against a splitting* $T(T^*G)=H\oplus V$. The vertical part $V=\ker T\pi$ is canonical. **A horizontal complement is a choice, and the choice is a connection.** Different connections give different component pairs for the same tangent vector, hence different-looking formulas for the same $\omega_0$.

:::tip[Proposition — the correction is the torsion]
Let $\nabla$ be any affine connection on $Q$, with torsion $T$. Split a tangent vector to $T^*Q$ at $\alpha$ along a curve as $w=(u,\beta)=\big(\dot q,\ \tfrac{D^\nabla\alpha}{dt}\big)\in T_qQ\times T^*_qQ$. Then
$$\omega_0(w_1,w_2)=\langle\beta_2,u_1\rangle-\langle\beta_1,u_2\rangle-\langle\alpha,\ T(u_1,u_2)\rangle .$$
:::

*Proof.* For the Levi-Civita connection the formula holds with no third term: in normal coordinates at $q$ the $\nabla^{\mathrm{LC}}$-splitting is the natural-chart splitting, where [[09-hamiltonian-on-cotangent]] gives $\omega_0=dq^i\wedge dp_i$, i.e. exactly $\langle\beta_2,u_1\rangle-\langle\beta_1,u_2\rangle$. (Torsion-freeness is what makes the two splittings agree there — the same property that carries the contraction computation, [[@simpson-porcoContractionTheoryRiemannian2014]] eq. (8).) Any other connection is $\nabla'=\nabla^{\mathrm{LC}}+A$ for a $(1,2)$-tensor $A$, and on covectors $\langle\beta'_i,v\rangle=\langle\beta_i,v\rangle-\langle\alpha,A(u_i,v)\rangle$. Substituting,
$$\omega_0=\langle\beta'_2,u_1\rangle-\langle\beta'_1,u_2\rangle+\langle\alpha,\ A(u_2,u_1)-A(u_1,u_2)\rangle,$$
and $T'(u_1,u_2)=A(u_1,u_2)-A(u_2,u_1)$ because $\nabla^{\mathrm{LC}}$ is torsion-free. $\square$

Now specialize. The left trivialization keeps $\mu=T^*_eL_g\alpha$ and differentiates it — so its "parallel" covector fields are the **left-invariant** ones. That is the splitting of the flat left-invariant connection $\nabla^-$ ($\nabla^-_XY=0$ on left-invariant $Y$), whose torsion is, per [[notation]],
$$T^-(\eta_1,\eta_2)=-[\eta_1,\eta_2].$$
Feeding this into the Proposition gives $-\langle\mu,-[\eta_1,\eta_2]\rangle=+\langle\mu,[\eta_1,\eta_2]\rangle$ — the Theorem, rederived independently of the $d\theta$ computation. Two routes, same sign.

:::warning[The trap]
"$\omega_0(w_1,w_2)=\langle\beta_2,u_1\rangle-\langle\beta_1,u_2\rangle$, no correction" and "$\omega_0=\langle\nu_2,\eta_1\rangle-\langle\nu_1,\eta_2\rangle+\langle\mu,[\eta_1,\eta_2]\rangle$" are **both true and not in conflict**. They are the same 2-form resolved against two different connections. The pair $(u,\beta)$ and the pair $(\eta,\nu)$ are *not* the same data left-translated — the horizontal parts agree ($u=g\eta$) but the vertical parts differ by $\Gamma(\xi,\cdot)$.

Both appear in this project: the trivialized form drives the reduction, the Levi-Civita one drives the contraction metric. Mixing components from one with the formula from the other produces a wrong sign or a missing $\mathrm{ad}^*$ term, and problem 4 exhibits it.
:::

## Hamilton's equations in these coordinates

Write $X_H=(\eta_H,\nu_H)$, and split $dH$ as $dH(\eta,\nu)=\langle\mathbf d_gH,\eta\rangle+\langle\nu,\partial H/\partial\mu\rangle$, where $\mathbf d_gH\in\mathfrak g^*$ is the **left-trivialized derivative in $g$**, $\langle\mathbf d_gH,\eta\rangle=\frac{d}{ds}\big|_{0}H(g\exp_G(s\eta),\mu)$, and $\partial H/\partial\mu\in\mathfrak g$.

Then $\omega_0(X_H,(\eta,\nu))=\langle\nu,\eta_H\rangle+\langle\mathrm{ad}^*_{\eta_H}\mu-\nu_H,\ \eta\rangle$, using $\langle\mu,[\eta_H,\eta]\rangle=\langle\mathrm{ad}^*_{\eta_H}\mu,\eta\rangle$. Matching components in $\iota_{X_H}\omega_0=dH$, and adding a body force $F\in\mathfrak g^*$:

$$\boxed{\ \dot g=g\,\frac{\partial H}{\partial\mu},\qquad
\dot\mu=\mathrm{ad}^*_{\partial H/\partial\mu}\mu-\mathbf d_gH+F\ }$$

**The $\mathrm{ad}^*$ term is the bracket term.** It exists in the equations of motion for exactly the reason the bracket exists in $\omega_0$. If $H$ is left-invariant then $\mathbf d_gH=0$ and, with $\partial H/\partial\mu=\xi$, this is the forced Euler–Poincaré / Lie–Poisson equation $\dot\mu=\mathrm{ad}^*_\xi\mu+f$ of [[10-euler-poincare]] and [[notation]].

## Worked example: $SO(3)$

$\mathfrak{so}(3)\cong\mathbb R^3$ by the hat map, $[\hat\Omega_1,\hat\Omega_2]=\widehat{\Omega_1\times\Omega_2}$, and $\mu\leftrightarrow\Pi\in\mathbb R^3$ with $\langle\mu,\hat\Omega\rangle=\Pi\cdot\Omega$. The form reads
$$\omega_0\big((\hat\Omega_1,\Pi'_1),(\hat\Omega_2,\Pi'_2)\big)\Big|_{(R,\Pi)}
=\Pi'_2\cdot\Omega_1-\Pi'_1\cdot\Omega_2+\Pi\cdot(\Omega_1\times\Omega_2).$$

**It is genuinely not the naive form.** Take the point $(R,\Pi)$ with $\Pi=(0,0,1)$ and the two purely horizontal vectors $w_1=(\hat e_1,0)$, $w_2=(\hat e_2,0)$. The naive expression gives $0-0=0$. The truth is
$$\omega_0(w_1,w_2)=\Pi\cdot(e_1\times e_2)=\Pi\cdot e_3=1\neq0 .$$
Two vectors that the naive formula calls $\omega_0$-orthogonal are not. No choice of $R$ rescues this; the discrepancy depends only on $\Pi$.

**Reduction to Euler.** Take $H(R,\Pi)=\tfrac12\Pi\cdot\mathbb J^{-1}\Pi$, left-invariant, so $\mathbf d_RH=0$ and $\partial H/\partial\Pi=\mathbb J^{-1}\Pi=\Omega$. For $\mathfrak{so}(3)$,
$$\langle\mathrm{ad}^*_{\hat\Omega}\Pi,\hat\zeta\rangle=\Pi\cdot(\Omega\times\zeta)=(\Pi\times\Omega)\cdot\zeta
\quad\Longrightarrow\quad \mathrm{ad}^*_{\hat\Omega}\Pi=\Pi\times\Omega .$$
So $\dot R=R\hat\Omega$ and $\dot\Pi=\Pi\times\Omega+\tau$, i.e. $\mathbb J\dot\Omega=\mathbb J\Omega\times\Omega+\tau$ — Euler's equations as fixed in [[notation]]. Delete the bracket term from $\omega_0$ and you delete the entire free rigid-body dynamics.

## Which of the three kinds?

Intrinsic, and *harmless*. Nothing here is a chart estimate: $\omega_0$, $\theta$, the trivialization and the torsion of $\nabla^-$ are all defined without coordinates, and the bracket term is a tensor, not a coordinate artifact. It carries no $\sup|\partial g_{ij}|$-type constant — indeed no metric appears anywhere in this lesson, which is why the pairing $\langle\cdot,\cdot\rangle$ stays metric-free throughout. The metric only enters when $H$ is built from $\mathbb I$.

The load-bearing thing this lesson supplies to later bounds is negative: it fixes *which* splitting a formula is stated against, so that a contraction estimate written in the Levi-Civita splitting is never fed components from the trivialized one.

## Problems

1. **Recall.** State $\theta$ and $\omega_0$ in left-trivialized coordinates without looking. Then say, in one sentence each: which step of the $d\theta$ computation produces the bracket term, and which connection's splitting the pair $(\eta,\nu)$ belongs to.

2. **Compute.** On $SE(3)$ write $\eta=(\hat\Omega,v)$ and $\mu=(\Pi,P)$ with $\langle\mu,\eta\rangle=\Pi\cdot\Omega+P\cdot v$. Using $[\eta_1,\eta_2]=\big(\widehat{\Omega_1\times\Omega_2},\ \Omega_1\times v_2-\Omega_2\times v_1\big)$, write the bracket term of $\omega_0$ explicitly. Then evaluate it at $\mu=(0,e_3)$ on $\eta_1=(\hat e_1,0)$ (pure rotation) and $\eta_2=(0,e_2)$ (pure translation). Finally: show the term vanishes whenever both $\eta_i$ are pure translations, and say why that is expected.

3. **Prove.** Show the bracket term vanishes for all $\mu\in\mathfrak g^*$ and all $\eta_1,\eta_2\in\mathfrak g$ iff $\mathfrak g$ is abelian. Deduce that the naive form $\langle\nu_2,\eta_1\rangle-\langle\nu_1,\eta_2\rangle$ is correct in left-trivialized coordinates exactly on connected abelian groups — $\mathbb R^k\times\mathbb T^m$ — and that on those groups $\nabla^-$ is torsion-free, consistently with the Proposition.

4. **Break it.** Conflate the two splittings deliberately, on the free rigid body ($G=SO(3)$, $H=\tfrac12\Pi\cdot\mathbb J^{-1}\Pi$, $\tau=0$, $\mathbb J=\mathrm{diag}(1,2,3)$).
   (a) Take the trivialized components $(\eta,\nu)$ but insert them into the correction-free Levi-Civita formula. Redo the matching in $\iota_{X_H}\omega_0=dH$ and write down the resulting $\dot\Pi$. What does it predict for a free asymmetric body released with $\Omega(0)=(1,1,1)$, and why is that observably false?
   (b) Now keep the bracket term but flip its sign (as you would by taking $T^-=+[\cdot,\cdot]$). Show that the resulting $\dot\Pi=\Omega\times\Pi$ still conserves **both** $H$ and $\|\Pi\|$. What does this say about using conservation laws to check the sign?

---

## Solutions

**1.** $\theta=\langle\mu,g^{-1}dg\rangle$, i.e. $\theta(\eta,\nu)=\langle\mu,\eta\rangle$; and $\omega_0((\eta_1,\nu_1),(\eta_2,\nu_2))=\langle\nu_2,\eta_1\rangle-\langle\nu_1,\eta_2\rangle+\langle\mu,[\eta_1,\eta_2]\rangle$. The bracket term is the $-\theta([W_1,W_2])$ term of the invariant formula for $d\theta$: the left-invariant frame does not commute, so $[W_1,W_2]=(X_{[\eta_1,\eta_2]},0)$ is nonzero and $\theta$ evaluates it to $\langle\mu,[\eta_1,\eta_2]\rangle$. The pair $(\eta,\nu)$ is the splitting of the flat left-invariant connection $\nabla^-$, whose parallel covector fields are the left-invariant ones, so that $\nu=\dot\mu$ is the $\nabla^-$-covariant derivative of $\alpha$.

**2.** $\langle\mu,[\eta_1,\eta_2]\rangle=\Pi\cdot(\Omega_1\times\Omega_2)+P\cdot(\Omega_1\times v_2-\Omega_2\times v_1)$. At $\mu=(0,e_3)$, $\eta_1=(\hat e_1,0)$, $\eta_2=(0,e_2)$: the first term dies ($\Pi=0$), and the second is $e_3\cdot(e_1\times e_2-0)=e_3\cdot e_3=1\neq0$. Note the *linear* momentum, not the angular one, is what makes it nonzero — the coupling is rotation-against-translation. If both $\eta_i$ are pure translations then $\Omega_1=\Omega_2=0$ and every term vanishes: the translation subgroup $\mathbb R^3\subset SE(3)$ is abelian, so its structure constants are zero and the correction has nothing to see. Restricted to that subgroup the naive form is right, which is problem 3 in miniature.

**3.** ($\Leftarrow$) If $[\eta_1,\eta_2]=0$ always, the term is $\langle\mu,0\rangle=0$. ($\Rightarrow$) Fix $\eta_1,\eta_2$. If $\langle\mu,[\eta_1,\eta_2]\rangle=0$ for **every** $\mu\in\mathfrak g^*$, then $[\eta_1,\eta_2]=0$, since the dual pairing separates points of $\mathfrak g$ (no metric needed: pick any basis and its dual). So $\mathfrak g$ is abelian. For connected $G$, abelian $\mathfrak g$ ⟺ abelian $G$, and connected abelian Lie groups are exactly $\mathbb R^k\times\mathbb T^m$. Consistency: $T^-(\eta_1,\eta_2)=-[\eta_1,\eta_2]=0$, so $\nabla^-$ is torsion-free there and the Proposition predicts no correction — and indeed $\nabla^-$ then coincides with the Levi-Civita connection of any left-invariant metric, both being flat.

**4(a).** Matching $\langle\nu,\eta_H\rangle-\langle\nu_H,\eta\rangle=\langle\mathbf d_gH,\eta\rangle+\langle\nu,\partial H/\partial\mu\rangle$ gives $\eta_H=\partial H/\partial\mu$ as before but $\nu_H=-\mathbf d_gH$, with no $\mathrm{ad}^*$ term. For the free rigid body $\mathbf d_RH=0$, so $\dot\Pi=0$: angular momentum *and* angular velocity constant, since $\Omega=\mathbb J^{-1}\Pi$. With $\Omega(0)=(1,1,1)$ this predicts a body spinning forever about a fixed body axis. False: for $\mathbb J=\mathrm{diag}(1,2,3)$ the true Euler equations give $\dot\Pi=\Pi\times\mathbb J^{-1}\Pi\neq0$ at that state (e.g. $\Pi=(1,2,3)$, $\Omega=(1,1,1)$, $\Pi\times\Omega=(2\cdot1-3\cdot1,\ 3\cdot1-1\cdot1,\ 1\cdot1-2\cdot1)=(-1,2,-1)$), which is the observed precession of a tumbling asymmetric body. The error is exactly one term, and it is the one the conflation deletes.

**4(b).** With the sign flipped, $\dot\Pi=\mathrm{ad}^{*}$-term reversed $=\Omega\times\Pi$. Then $\frac{d}{dt}\|\Pi\|^2=2\Pi\cdot(\Omega\times\Pi)=0$ and $\dot H=\Omega\cdot\dot\Pi=\Omega\cdot(\Omega\times\Pi)=0$. Both invariants survive, because both are quadratic and the flipped term is still a cross product with $\Pi$ and $\Omega$ — the motion still runs on the intersection of the momentum sphere and the energy ellipsoid, just **traversed in the opposite direction**. So the two standard sanity checks are blind to this sign error; only the *direction* of precession, or a direct check against the derivation of $\omega_0$, catches it. That is why [[notation]] fixes the sign of $\mathrm{ad}^*$ once and demands sources be converted at the point of use rather than trusted.
