---
tags: [mechanics, lie-groups, variational, reduction]
---
# Euler–Poincaré Reduction

**Prereq:** [[01-adjoint-and-coadjoint]] ($\mathrm{ad}^*$, the pairing, $\dot\pi=0\iff\dot\mu=\mathrm{ad}^*_\xi\mu$), [[02-trivialization-of-tg]] (body/spatial split, $T G\cong G\times\mathfrak g$), [[mechanical-systems-on-lie-groups]]; notation fixed in [[notation]].
**Goal:** derive $\dot\mu=\mathrm{ad}^*_\xi\mu+f$ from Hamilton's principle, and know exactly which step fails if you forget that variations of $\xi$ are constrained.

Lessons 01 and 02 both stopped at the same place: they identified $\mathrm{ad}^*_\xi\mu$ as the operator that must appear and deferred the derivation here. This lesson delivers it. The whole content is one identity — $\delta\xi=\dot\eta+\mathrm{ad}_\xi\eta$ — and everything else is integration by parts.

## The reduced Lagrangian

For a mechanical system on $G$ with body-fixed inertia, the Lagrangian $L:TG\to\mathbb R$ is left-invariant: $L(hg,h\dot g)=L(g,\dot g)$. Setting $h=g^{-1}$ collapses it onto the fibre.

:::info[Definition]
The **reduced Lagrangian** is $\ell:\mathfrak g\to\mathbb R$, $\ell(\xi)=L(e,\xi)$, so that $L(g,\dot g)=\ell(g^{-1}\dot g)=\ell(\xi)$. For a kinetic-energy Lagrangian,
$$\ell(\xi)=\tfrac12\langle\mathbb I\xi,\xi\rangle=\tfrac12\|\xi\|^2_{\mathbb I}.$$
Its fibre derivative is the **body momentum**
$$\mu=\frac{\delta\ell}{\delta\xi}\in\mathfrak g^*,\qquad \Big\langle\frac{\delta\ell}{\delta\xi},\zeta\Big\rangle=\left.\frac{d}{d\epsilon}\right|_{0}\ell(\xi+\epsilon\zeta)\quad\forall\zeta\in\mathfrak g,$$
which for the quadratic $\ell$ is $\mu=\mathbb I\xi$.
:::

$\ell$ has lost the $g$-dependence entirely — that is what "reduction" means. But $\xi$ is not a free curve in $\mathfrak g$: it is $g^{-1}\dot g$ for an actual curve in $G$, and that constraint survives reduction in exactly one place, the admissible variations.

## The constrained-variation identity

Take a smooth two-parameter family $g(t,\epsilon)\in G$ with $g(t,0)=g(t)$, and define the two left-trivialized derivatives
$$\xi(t,\epsilon)=g^{-1}\partial_tg,\qquad \eta(t,\epsilon)=g^{-1}\partial_\epsilon g,$$
both valued in $\mathfrak g$. Write $\delta=\partial_\epsilon|_{\epsilon=0}$ and $\dot{\ }=\partial_t$.

:::tip[Lemma — constrained variations]
$$\delta\xi=\dot\eta+\mathrm{ad}_\xi\eta=\dot\eta+[\xi,\eta].$$
:::

*Proof.* Both quantities are $g^{-1}(\text{second derivative})$ plus a first-order correction from differentiating $g^{-1}$, using $\partial_\epsilon(g^{-1})=-g^{-1}(\partial_\epsilon g)g^{-1}$ and likewise in $t$:
$$\partial_\epsilon\xi=\partial_\epsilon\big(g^{-1}\partial_tg\big)=-g^{-1}(\partial_\epsilon g)\,g^{-1}\partial_tg+g^{-1}\partial_\epsilon\partial_tg=-\eta\,\xi+g^{-1}\partial_\epsilon\partial_tg,$$
$$\partial_t\eta=\partial_t\big(g^{-1}\partial_\epsilon g\big)=-g^{-1}(\partial_tg)\,g^{-1}\partial_\epsilon g+g^{-1}\partial_t\partial_\epsilon g=-\xi\,\eta+g^{-1}\partial_t\partial_\epsilon g.$$
The second-order terms are equal — $g$ is smooth, so mixed partials commute — and cancel on subtraction:
$$\partial_\epsilon\xi-\partial_t\eta=\xi\eta-\eta\xi=[\xi,\eta].$$
Evaluate at $\epsilon=0$. $\square$

Read what this says. In a vector space one has $\delta\dot q=\frac{d}{dt}\delta q$ and nothing else: velocity variations are the time-derivatives of position variations, full stop. On a group, $\xi$ is a velocity *measured in a moving frame*, and varying the curve also varies the frame. The extra $[\xi,\eta]$ is precisely that second effect, and it is exactly the non-commutativity of $G$: if $G$ is abelian then $\mathrm{ad}\equiv0$ and the classical rule is recovered.

**So $\delta\xi$ is not arbitrary.** Given the curve $\xi$, the admissible $\delta\xi$ form the image of the linear map $\eta\mapsto\dot\eta+\mathrm{ad}_\xi\eta$ acting on curves $\eta$ with $\eta(t_0)=\eta(t_1)=0$ — a proper subset of all curves in $\mathfrak g$. This is the single point where Euler–Poincaré differs from writing Euler–Lagrange on the vector space $\mathfrak g$, and Problem 4 shows it changes the answer.

## The reduced equations

:::tip[Theorem — Euler–Poincaré]
Let $\ell:\mathfrak g\to\mathbb R$ and let $g(t)$ be a curve in $G$ with $\xi=g^{-1}\dot g$. Then $g$ is a stationary point of $\int_{t_0}^{t_1}L(g,\dot g)\,dt$ over variations with fixed endpoints if and only if
$$\frac{d}{dt}\frac{\delta\ell}{\delta\xi}=\mathrm{ad}^*_\xi\frac{\delta\ell}{\delta\xi},\qquad\text{i.e.}\qquad \dot\mu=\mathrm{ad}^*_\xi\mu .$$
:::

*Proof.* Fixed endpoints $g(t_0,\epsilon)=g(t_0)$, $g(t_1,\epsilon)=g(t_1)$ mean $\partial_\epsilon g$ vanishes there, hence $\eta(t_0)=\eta(t_1)=0$. By left-invariance $\int L(g,\dot g)\,dt=\int\ell(\xi)\,dt$, so
$$\delta\!\int_{t_0}^{t_1}\!\ell(\xi)\,dt=\int_{t_0}^{t_1}\!\Big\langle\frac{\delta\ell}{\delta\xi},\delta\xi\Big\rangle dt
=\int_{t_0}^{t_1}\!\big\langle\mu,\dot\eta\big\rangle+\big\langle\mu,\mathrm{ad}_\xi\eta\big\rangle\,dt,$$
the second equality being the Lemma. The first term integrates by parts, the second is the definition of $\mathrm{ad}^*$ from [[01-adjoint-and-coadjoint]]:
$$=\Big[\langle\mu,\eta\rangle\Big]_{t_0}^{t_1}+\int_{t_0}^{t_1}\big\langle-\dot\mu+\mathrm{ad}^*_\xi\mu,\ \eta\big\rangle\,dt .$$
The boundary term dies because $\eta(t_0)=\eta(t_1)=0$. Now $\eta$ *is* free — any curve in $\mathfrak g$ vanishing at the endpoints is realizable, by solving $\partial_\epsilon g=g\eta$ — so by the fundamental lemma of the calculus of variations and non-degeneracy of the pairing, $\dot\mu=\mathrm{ad}^*_\xi\mu$. $\square$

The constraint moved: $\delta\xi$ was not free, $\eta$ is. That trade is the whole trick.

:::info[Definition — forced Euler–Poincaré, Lagrange–d'Alembert]
For a non-conservative force $f\in\mathfrak g^*$ (body-frame torque/wrench), stationarity is replaced by the Lagrange–d'Alembert principle
$$\delta\!\int_{t_0}^{t_1}\!\ell(\xi)\,dt+\int_{t_0}^{t_1}\!\langle f,\eta\rangle\,dt=0,$$
and the same computation gives $\dot\mu=\mathrm{ad}^*_\xi\mu+f$. Together with the reconstruction equation the full system on $G\times\mathfrak g^*$ is
$$\dot g=g\xi,\qquad \dot\mu=\mathrm{ad}^*_\xi\mu+f,\qquad \xi=\mathbb I^{-1}\mu,$$
matching the split announced in [[02-trivialization-of-tg]].
:::

Note $f$ pairs with $\eta$, not with $\delta\xi$: virtual work is done against the *configuration* variation. That is why no bracket term attaches to $f$.

## Frame transport, Lie–Poisson, and the sign

**$\mathrm{ad}^*_\xi\mu$ is not a force.** [[01-adjoint-and-coadjoint]] proves $\dot\pi=0\iff\dot\mu=\mathrm{ad}^*_\xi\mu$ for the spatial momentum $\pi=\mathrm{Ad}^*_{g^{-1}}\mu$; take it from there rather than reproving. Unforced Euler–Poincaré says *the spatial momentum is constant*, and $\mathrm{ad}^*_\xi\mu$ is the transport cost of saying so in the rotating body frame. Adding $f$ gives $\dot\pi=\mathrm{Ad}^*_{g^{-1}}f$: the spatial momentum changes at exactly the applied force, as it should.

**Lie–Poisson (stated, not developed).** The Legendre-transformed picture lives on $\mathfrak g^*$ with $H(\mu)=\langle\mu,\mathbb I^{-1}\mu\rangle/2$ and the reduced bracket
$$\{F,K\}_-(\mu)=-\Big\langle\mu,\Big[\frac{\delta F}{\delta\mu},\frac{\delta K}{\delta\mu}\Big]\Big\rangle ,$$
for which $\dot F=\{F,H\}_-$ reproduces $\dot\mu=\mathrm{ad}^*_{\delta H/\delta\mu}\mu$. This is a genuine Poisson structure but a *degenerate* one — it is not symplectic; its degeneracy is the Casimirs, and the symplectic leaves are the coadjoint orbits (Problem 3). It is what the canonical $\omega_0$ on $T^*G$ becomes after reduction; lesson 11 does the left-trivialized $\omega_0$ properly.

:::warning[Sign flag — left/body convention]
Everything here is the **left (body)** reduction of [[notation]]. A right-invariant Lagrangian reduced by right translations gives $\delta\xi_s=\dot\eta-\mathrm{ad}_{\xi_s}\eta$ and hence $\dot\mu=-\mathrm{ad}^*_{\xi_s}\mu$. Both the variation identity and the equation flip sign; a source using the right convention, or the minus-sign convention for $\mathrm{ad}^*$ itself, must be converted at the point of use.
:::

**Which of the three kinds is this?** Intrinsic and metric-free down to the last step: the Lemma uses only group multiplication, the Theorem only the canonical pairing. The single metric input is $\mathbb I$, entering when $\mu=\mathbb I\xi$ is inverted to close the system — and $\mathbb I$ is physics (inertia), not a chart. No $\sup|\partial g_{ij}|$-type constant can arise here; the conservatism this project targets enters later, when distances are measured.

## Worked example: $SO(3)$

Take $G=SO(3)$, $\ell(\hat\Omega)=\tfrac12\Omega^\top\mathbb J\Omega$, so $\mu\leftrightarrow\Pi=\mathbb J\Omega$ under the identification of [[01-adjoint-and-coadjoint]] (Step 2). That lesson computed $\mathrm{ad}^*_\Omega\Pi=\Pi\times\Omega$. Substituting into the Theorem:
$$\boxed{\ \dot\Pi=\Pi\times\Omega+\tau\ }\qquad\text{i.e.}\qquad \mathbb J\dot\Omega=\mathbb J\Omega\times\Omega+\tau,$$
Euler's equations, with the reconstruction equation $\dot R=R\hat\Omega$. In components with $\mathbb J=\mathrm{diag}(J_1,J_2,J_3)$ and $\tau=0$: $J_1\dot\Omega_1=(J_2-J_3)\Omega_2\Omega_3$ and cyclic. A symmetric body $J_1=J_2=J_3$ makes the right side vanish and $\Omega$ constant; an asymmetric one does not, and that is entirely the $\mathrm{ad}^*$ term.

**Cross-check against the Riemannian route.** [[03-levi-civita-left-invariant]] derives the geodesic equation of the left-invariant metric $\mathbb G$ as the Euler–Arnold equation $\dot\xi=\widetilde{\mathrm{ad}}_\xi\xi$, and specializes it to $\mathbb J\dot\Omega=\mathbb J\Omega\times\Omega$. Same equation, two independent routes: here from Hamilton's principle with constrained variations, there from $\nabla_{\dot g}\dot g=0$. They agree because $\widetilde{\mathrm{ad}}_\xi=\mathbb I^{-1}\mathrm{ad}^*_\xi\mathbb I$, so $\dot\xi=\widetilde{\mathrm{ad}}_\xi\xi$ is $\mathbb I\dot\xi=\mathrm{ad}^*_\xi\mathbb I\xi$ verbatim. Unforced Euler–Poincaré *is* the geodesic equation of the kinetic-energy metric — which is the statement in [[mechanical-systems-on-lie-groups]] that the mechanics supplies the metric, now proved on a group.

## Problems

1. **Recall.** Without looking: state the constrained-variation identity, say which structure on $G$ each of its two terms comes from, and state unforced Euler–Poincaré. Then say in one sentence where the fixed-endpoint hypothesis is used and where non-degeneracy of the pairing is used.

2. **Compute.** Free rigid body on $SE(3)$: take $\ell(\omega,v)=\tfrac12\omega^\top\mathbb J\omega+\tfrac12m\|v\|^2$, so $\mu=(\Pi,P)=(\mathbb J\omega,mv)$. Using $\mathrm{ad}^*_{(\omega,v)}(\Pi,P)=(\Pi\times\omega+P\times v,\ P\times\omega)$ from [[01-adjoint-and-coadjoint]] Problem 2, write out $\dot\mu=\mathrm{ad}^*_\xi\mu$ in terms of $\omega,v$. Which term drops, and does the rotational equation decouple from the translational one?

3. **Prove.** Show that the unforced flow satisfies $\mu(t)=\mathrm{Ad}^*_{g(t)}\mu(0)$ when $g(0)=e$ — the solution stays on one coadjoint orbit. Deduce that on $SO(3)$ the quantity $\|\Pi\|$ is conserved, and combine with the energy conservation of [[01-adjoint-and-coadjoint]] Problem 3 to describe the free rigid-body trajectories in $\mathbb R^3$.

4. **Break it.** Suppose you forget the Lemma and treat $\xi$ as the velocity of a curve in the vector space $\mathfrak g$, i.e. impose only $\delta\xi=\dot\eta$.
   (a) Redo the variational computation and show you obtain $\dot\mu=0$.
   (b) On $SO(3)$ with $\mathbb J=\mathrm{diag}(1,2,3)$ and $\Omega(0)=(1,1,0)$, show the two predictions disagree immediately by computing $\dot\Omega(0)$ under each.
   (c) Show that on an abelian $G$ the two derivations agree, and say what $\dot\mu=0$ is then.

---

## Solutions

**1.** $\delta\xi=\dot\eta+\mathrm{ad}_\xi\eta$ for $\xi=g^{-1}\partial_tg$, $\eta=g^{-1}\partial_\epsilon g$. The $\dot\eta$ term is the ordinary "vary then differentiate" rule; the $\mathrm{ad}_\xi\eta$ term comes from the group multiplication alone — it is the non-commutativity of $G$, and vanishes iff the bracket does. Unforced: $\frac{d}{dt}\frac{\delta\ell}{\delta\xi}=\mathrm{ad}^*_\xi\frac{\delta\ell}{\delta\xi}$. Fixed endpoints kill the boundary term $[\langle\mu,\eta\rangle]_{t_0}^{t_1}$ after integrating by parts; non-degeneracy converts "$\langle-\dot\mu+\mathrm{ad}^*_\xi\mu,\eta\rangle=0$ for all $\eta$" into the vanishing of the covector itself.

**2.** $\dot\Pi=\Pi\times\omega+P\times v=\mathbb J\omega\times\omega+mv\times v=\mathbb J\omega\times\omega$, since $v\times v=0$; and $\dot P=P\times\omega$, i.e. $m\dot v=mv\times\omega$. So
$$\mathbb J\dot\omega=\mathbb J\omega\times\omega,\qquad \dot v=v\times\omega .$$
The $P\times v$ cross-term — the part of $\mathrm{ad}^*_{\mathfrak{se}(3)}$ with no $SO(3)$ analogue — drops, but only because the inertia operator is block-diagonal with $P\parallel v$. The rotational equation is exactly Euler's and does not see $v$, so it decouples; the translational one does not, and reads "the body-frame velocity of a body moving in a straight line rotates backwards with the body". Note the decoupling is a property of *this* $\mathbb I$: a body with a rotational–translational inertia coupling (offset centre of mass) has $P\not\parallel v$ and the term survives.

**3.** From [[01-adjoint-and-coadjoint]], $\dot\mu=\mathrm{ad}^*_\xi\mu\iff\dot\pi=0$ where $\pi=\mathrm{Ad}^*_{g^{-1}}\mu$. So $\pi(t)=\pi(0)=\mathrm{Ad}^*_e\mu(0)=\mu(0)$. Apply $\mathrm{Ad}^*_{g(t)}$ and use the anti-action law $\mathrm{Ad}^*_h\mathrm{Ad}^*_g=\mathrm{Ad}^*_{gh}$ with $g\to g^{-1}$, $h\to g$: $\mathrm{Ad}^*_g\mathrm{Ad}^*_{g^{-1}}=\mathrm{Ad}^*_{g^{-1}g}=\mathrm{id}$. Hence $\mu(t)=\mathrm{Ad}^*_{g(t)}\mu(0)$, so $\mu(t)$ lies in the coadjoint orbit of $\mu(0)$ for all $t$.

On $SO(3)$, [[01-adjoint-and-coadjoint]] computed $\mathrm{Ad}^*_R\Pi=R^\top\Pi$, and $R^\top$ is orthogonal, so $\|\Pi(t)\|=\|\Pi(0)\|$: the coadjoint orbits are spheres, and $\|\Pi\|^2$ is a Casimir of the Lie–Poisson bracket. (Direct check: $\frac{d}{dt}\|\Pi\|^2=2\Pi\cdot(\Pi\times\Omega)=0$.) Energy $E=\tfrac12\Pi^\top\mathbb J^{-1}\Pi$ is conserved too, and its level sets are ellipsoids. So $\Pi(t)$ traces the intersection of a sphere with an ellipsoid — the polhode. For $J_1<J_2<J_3$ these intersections are closed curves around the $\pm e_1$ and $\pm e_3$ axes (stable) and a figure-eight separatrix through $\pm e_2$ (unstable) — the intermediate-axis instability, visible here as pure geometry with no linearization.

**4(a).** With $\delta\xi=\dot\eta$ only, $\delta\int\ell\,dt=\int\langle\mu,\dot\eta\rangle dt=[\langle\mu,\eta\rangle]_{t_0}^{t_1}-\int\langle\dot\mu,\eta\rangle dt=-\int\langle\dot\mu,\eta\rangle dt$. Arbitrary $\eta$ then forces $\dot\mu=0$. This is just Euler–Lagrange for a Lagrangian on the vector space $\mathfrak g$ with no potential: $\frac{d}{dt}\frac{\partial\ell}{\partial\xi}=\frac{\partial\ell}{\partial q}=0$.

**(b)** Correct: $\mathbb J\dot\Omega=\mathbb J\Omega\times\Omega$. With $\mathbb J\Omega=(1,2,0)$ and $\Omega=(1,1,0)$, $\mathbb J\Omega\times\Omega=(1,2,0)\times(1,1,0)=(0,0,-1)$, so $\dot\Omega(0)=\mathbb J^{-1}(0,0,-1)=(0,0,-\tfrac13)\ne0$. Naive: $\mathbb J\dot\Omega=0$, so $\dot\Omega(0)=0$ and $\Omega$ is constant forever. The naive answer predicts that *every* free rigid body spins about a fixed body axis at constant rate — no precession, no polhode, no intermediate-axis instability. The discarded term $\mathrm{ad}_\xi\eta$ is carrying all of rigid-body dynamics; it is not a correction.

**(c)** If $G$ is abelian then $[\cdot,\cdot]\equiv0$, so $\mathrm{ad}_\xi\eta=0$, the Lemma reduces to $\delta\xi=\dot\eta$, and $\mathrm{ad}^*_\xi\mu=0$ makes Euler–Poincaré read $\dot\mu=0$. The two derivations coincide because there was never a difference. For $G=(\mathbb R^n,+)$ with $\mathbb I$ the mass matrix, $\dot\mu=0$ is conservation of linear momentum, i.e. Newton's first law — and it is the *correct* answer there. So the naive derivation is not wrong in general; it is wrong exactly to the extent that $G$ is non-commutative, which is the content of the identity being dropped.
