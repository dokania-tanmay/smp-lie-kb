---
tags: [lie-groups, algebra, mechanics, foundations]
---
# Adjoint and Coadjoint

**Prereq:** [[riemannian-geometry]] (groups, Lie bracket, left-invariant metrics), [[mechanical-systems-on-lie-groups]]; notation fixed in [[notation]].
**Goal:** know why momenta are elements of $\mathfrak g^*$ rather than $\mathfrak g$, and why $\mathrm{ad}^*_\xi$ — not $\mathrm{ad}_\xi$ — is the operator that shows up in the equations of motion.

## Why the dual space at all

A velocity is $\dot g\in T_gG$; left-trivialized, $\xi = g^{-1}\dot g\in\mathfrak g$. A momentum is *not* another velocity. It is whatever eats a velocity and returns power: $\partial L/\partial\xi$ is by construction a **linear functional on $\mathfrak g$**, i.e. an element of $\mathfrak g^*$. Kinetic energy is $\tfrac12\langle\mu,\xi\rangle$ and the pairing is the only operation used.

That pairing $\langle\cdot,\cdot\rangle:\mathfrak g^*\times\mathfrak g\to\mathbb R$, $\langle\mu,\xi\rangle=\mu(\xi)$, needs **no inner product, no metric, no chart**. It exists on the bare vector space $\mathfrak g$. Everything in this lesson is built from it alone, so everything here is intrinsic in the strong sense — not "chart-dependent but provably invariant", but never chart-dependent to begin with.

The inertia operator $\mathbb I:\mathfrak g\to\mathfrak g^*$ with $\mu=\mathbb I\xi$ is an *extra choice* that identifies the two spaces. Keeping $\mathfrak g$ and $\mathfrak g^*$ apart until $\mathbb I$ is invoked is what stops us from writing down statements that are silently true only when $\mathbb I$ happens to be $\mathrm{Ad}$-invariant. Problem 4 is exactly that failure.

## Definitions

:::info[Definition]
For $g\in G$, the **adjoint action of the group** is conjugation on the algebra,
$$\mathrm{Ad}_g:\mathfrak g\to\mathfrak g,\qquad \mathrm{Ad}_g\eta = g\eta g^{-1},$$
the differential at $e$ of the inner automorphism $h\mapsto ghg^{-1}$. It is a group action: $\mathrm{Ad}_{gh}=\mathrm{Ad}_g\mathrm{Ad}_h$, $\mathrm{Ad}_e=\mathrm{id}$.
:::

:::info[Definition]
The **adjoint action of the algebra** is $\mathrm{ad}_\xi\eta=[\xi,\eta]=\xi\eta-\eta\xi$ (matrix commutator).
:::

:::tip[Lemma]
$\mathrm{ad}$ is the derivative of $\mathrm{Ad}$ at the identity:
$$\left.\frac{d}{dt}\right|_{t=0}\mathrm{Ad}_{\exp_G(t\xi)}\eta = \mathrm{ad}_\xi\eta.$$
*Proof.* With $g(t)=\exp_G(t\xi)$ (Lie exponential — the matrix exponential here), $\mathrm{Ad}_{g(t)}\eta = e^{t\xi}\eta e^{-t\xi}$. Differentiate the product at $t=0$: $\xi\eta+\eta(-\xi)=[\xi,\eta]$. $\square$
:::

:::info[Definition]
The **coadjoint operators** are the plain linear duals — no sign flip, no metric:
$$\langle\mathrm{Ad}^*_g\alpha,\eta\rangle=\langle\alpha,\mathrm{Ad}_g\eta\rangle,\qquad
\langle\mathrm{ad}^*_\xi\mu,\eta\rangle=\langle\mu,\mathrm{ad}_\xi\eta\rangle\quad\forall\eta\in\mathfrak g.$$
Since $\eta$ ranges over all of $\mathfrak g$ and the pairing is non-degenerate, these define $\mathrm{Ad}^*_g\alpha$ and $\mathrm{ad}^*_\xi\mu$ uniquely. Note $\mathrm{Ad}^*$ is an *anti*-action: $\mathrm{Ad}^*_{gh}=\mathrm{Ad}^*_h\mathrm{Ad}^*_g$.
:::

This is the convention of [[@leeGeometricInterpretationBrownian2025]]. Many mechanics texts define $\mathrm{ad}^*$ with a minus sign; if a source does, convert at the point of use and say so.

## Why $\mathrm{ad}^*$ is what appears in the dynamics

Spatial momentum is $\pi=\mathrm{Ad}^*_{g^{-1}}\mu$ — the body momentum $\mu$ pushed into the frame at the identity, i.e. the inertially-fixed one. The next proposition is the entire reason the coadjoint operator is in Euler–Poincaré.

:::tip[Proposition]
Along any curve $g(t)$ with $\xi=g^{-1}\dot g$, and $\pi=\mathrm{Ad}^*_{g^{-1}}\mu$,
$$\dot\pi = 0 \quad\Longleftrightarrow\quad \dot\mu = \mathrm{ad}^*_\xi\mu .$$
*Proof.* Fix $\eta\in\mathfrak g$ constant. Then $\langle\pi,\eta\rangle=\langle\mu,\mathrm{Ad}_{g^{-1}}\eta\rangle$, and
$$\frac{d}{dt}\big(g^{-1}\eta g\big)=-g^{-1}\dot g\,g^{-1}\eta g+g^{-1}\eta\,\dot g=-\big[\xi,\;\mathrm{Ad}_{g^{-1}}\eta\big],$$
using $\dot g = g\xi$. Hence
$$\frac{d}{dt}\langle\pi,\eta\rangle=\langle\dot\mu,\mathrm{Ad}_{g^{-1}}\eta\rangle-\langle\mu,\mathrm{ad}_\xi\mathrm{Ad}_{g^{-1}}\eta\rangle=\big\langle\dot\mu-\mathrm{ad}^*_\xi\mu,\;\mathrm{Ad}_{g^{-1}}\eta\big\rangle.$$
$\mathrm{Ad}_{g^{-1}}$ is invertible, so this vanishes for all $\eta$ iff $\dot\mu=\mathrm{ad}^*_\xi\mu$. $\square$
:::

So $\mathrm{ad}^*_\xi\mu$ is not a force. It is the bookkeeping cost of writing a conservation law ($\dot\pi=0$) in the body frame: the frame rotates, and $\mathrm{ad}^*_\xi\mu$ is exactly the rate at which it does. Adding a genuine force $f\in\mathfrak g^*$ gives $\dot\mu=\mathrm{ad}^*_\xi\mu+f$.

## Worked example: $\mathfrak{so}(3)$

The hat map $\hat{\cdot}:\mathbb R^3\to\mathfrak{so}(3)$ is defined by $\hat a\,b=a\times b$, with inverse $(\cdot)^\vee$; explicitly $\hat a=\begin{psmallmatrix}0&-a_3&a_2\\a_3&0&-a_1\\-a_2&a_1&0\end{psmallmatrix}$.

**Step 1 — hat intertwines commutator and cross product.** For any $c\in\mathbb R^3$,
$$[\hat a,\hat b]\,c=a\times(b\times c)-b\times(a\times c)=(a\times b)\times c=\widehat{a\times b}\,c,$$
the middle equality being the Jacobi identity for $\times$. So $\mathrm{ad}_{\hat a}\hat b=\widehat{a\times b}$: under $\vee$, $\mathrm{ad}$ *is* the cross product.

**Step 2 — identify $\mathfrak g^*$ with $\mathbb R^3$.** The notation contract fixes $\langle\eta,\zeta\rangle_{\mathfrak{so}(3)}=\tfrac12\mathrm{tr}(\eta^\top\zeta)=(\eta^\vee)^\top\zeta^\vee$. Represent $\mu\in\mathfrak{so}(3)^*$ by $\Pi\in\mathbb R^3$ through $\langle\mu,\eta\rangle=\Pi^\top\eta^\vee$, and write $\Omega=\xi^\vee$. This is a choice; it is the standard one, and $SO(3)$ is the case where it is harmless (Problem 4).

**Step 3 — compute.** For arbitrary $\eta=\hat b$,
$$\langle\mathrm{ad}^*_{\hat\Omega}\mu,\hat b\rangle=\langle\mu,[\hat\Omega,\hat b]\rangle=\langle\mu,\widehat{\Omega\times b}\rangle=\Pi^\top(\Omega\times b)=(\Pi\times\Omega)^\top b,$$
the last step being the cyclic identity $\Pi\cdot(\Omega\times b)=b\cdot(\Pi\times\Omega)$. Since $b$ was arbitrary:
$$\boxed{\;\mathrm{ad}^*_\Omega\Pi=\Pi\times\Omega\;}$$

That is precisely the gyroscopic term in Euler's equation $\dot\Pi=\Pi\times\Omega+\tau$, i.e. $\mathbb J\dot\Omega=\mathbb J\Omega\times\Omega+\tau$. **This lesson only identifies the operator** — that the rigid body actually obeys that equation is derived in lesson 10 from constrained variations.

Sanity check against the Proposition: $\langle\mathrm{Ad}^*_R\mu,\hat b\rangle=\langle\mu,R\hat bR^\top\rangle=\Pi^\top(Rb)$, so $\mathrm{Ad}^*_R\Pi=R^\top\Pi$ and the spatial momentum is $\pi=\mathrm{Ad}^*_{R^{-1}}\Pi=R\Pi$ — the body angular momentum rotated into the inertial frame, conserved when $\tau=0$.

## Problems

1. **Recall.** Without looking above: state the defining identities for $\mathrm{ad}^*_\xi$ and $\mathrm{Ad}^*_g$, and say in one sentence which structures on $\mathfrak g$ each definition uses. Then say what changes if the source you are reading defines $\mathrm{ad}^*$ with a minus sign.

2. **Compute.** On $SE(3)$, write $\xi=(\omega,v)$ for $\begin{psmallmatrix}\hat\omega&v\\0&0\end{psmallmatrix}\in\mathfrak{se}(3)$. Compute $\mathrm{ad}_{(\omega_1,v_1)}(\omega_2,v_2)$ from the matrix commutator, then compute $\mathrm{ad}^*_{(\omega,v)}(\Pi,P)$ using the pairing $\langle(\Pi,P),(\alpha,u)\rangle=\Pi^\top\alpha+P^\top u$.

3. **Prove.** Show $\langle\mathrm{ad}^*_\xi\mu,\xi\rangle=0$ for every $\xi\in\mathfrak g$, $\mu\in\mathfrak g^*$. Deduce that the unforced Euler–Poincaré flow $\dot\mu=\mathrm{ad}^*_\xi\mu$ with $\xi=\mathbb I^{-1}\mu$ conserves the energy $E=\tfrac12\langle\mu,\mathbb I^{-1}\mu\rangle$.

4. **Break it.** On $SO(3)$ the computation above gives $\mathrm{ad}^*_\Omega\Pi=\Pi\times\Omega=-\,\mathrm{ad}_\Omega\Pi$: under the identification $\mathfrak g^*\cong\mathfrak g$, $\mathrm{ad}^*_\xi=-\mathrm{ad}_\xi$. Show that the hypothesis making this work is $\mathrm{Ad}$-invariance of the inner product, and that it fails on $SE(3)$: using your answer to Problem 2 and the naive inner product $\langle(\omega_1,v_1),(\omega_2,v_2)\rangle=\omega_1^\top\omega_2+v_1^\top v_2$, exhibit $\xi,\eta$ with $\mathrm{ad}^*_\xi\eta\neq-\mathrm{ad}_\xi\eta$.

---

## Solutions

**1.** $\langle\mathrm{ad}^*_\xi\mu,\eta\rangle=\langle\mu,\mathrm{ad}_\xi\eta\rangle$ and $\langle\mathrm{Ad}^*_g\alpha,\eta\rangle=\langle\alpha,\mathrm{Ad}_g\eta\rangle$, for all $\eta\in\mathfrak g$. Both use only the vector-space structure of $\mathfrak g$, the bracket (resp. the group multiplication), and the canonical pairing — no inner product, no chart. A minus-sign convention replaces $\mathrm{ad}^*_\xi$ by $-\mathrm{ad}^*_\xi$, which flips the sign of the gyroscopic term: that source's Euler–Poincaré equation reads $\dot\mu=-\mathrm{ad}^*_\xi\mu+f$ and its $SO(3)$ specialization is $\mathrm{ad}^*_\Omega\Pi=\Omega\times\Pi$. Convert, do not adopt.

**2.** $\begin{psmallmatrix}\hat\omega_1&v_1\\0&0\end{psmallmatrix}\begin{psmallmatrix}\hat\omega_2&v_2\\0&0\end{psmallmatrix}=\begin{psmallmatrix}\hat\omega_1\hat\omega_2&\hat\omega_1v_2\\0&0\end{psmallmatrix}$, so the commutator has blocks $[\hat\omega_1,\hat\omega_2]=\widehat{\omega_1\times\omega_2}$ and $\hat\omega_1v_2-\hat\omega_2v_1$:
$$\mathrm{ad}_{(\omega_1,v_1)}(\omega_2,v_2)=(\omega_1\times\omega_2,\;\omega_1\times v_2-\omega_2\times v_1).$$
Then, with $\eta=(\alpha,u)$,
$$\langle\mu,\mathrm{ad}_{(\omega,v)}\eta\rangle=\Pi\cdot(\omega\times\alpha)+P\cdot(\omega\times u)-P\cdot(\alpha\times v)
=\alpha\cdot(\Pi\times\omega+P\times v)+u\cdot(P\times\omega),$$
using $\Pi\cdot(\omega\times\alpha)=\alpha\cdot(\Pi\times\omega)$ and $-P\cdot(\alpha\times v)=-\alpha\cdot(v\times P)=\alpha\cdot(P\times v)$. Hence
$$\mathrm{ad}^*_{(\omega,v)}(\Pi,P)=(\Pi\times\omega+P\times v,\;P\times\omega).$$
The linear-momentum cross-term $P\times v$ is the part with no $SO(3)$ analogue.

**3.** $\langle\mathrm{ad}^*_\xi\mu,\xi\rangle=\langle\mu,\mathrm{ad}_\xi\xi\rangle=\langle\mu,[\xi,\xi]\rangle=0$. For the energy, $\mathbb I^{-1}$ is symmetric (as $\mathbb I$ is), so $\dot E=\langle\dot\mu,\mathbb I^{-1}\mu\rangle=\langle\mathrm{ad}^*_\xi\mu,\xi\rangle=0$. Note this used nothing about $G$ — the gyroscopic term is always workless, on any Lie group and for any $\mathbb I$.

**4.** An inner product $\langle\cdot,\cdot\rangle_{\mathbb I}$ is $\mathrm{Ad}$-invariant iff $\langle\mathrm{Ad}_g\eta,\mathrm{Ad}_g\zeta\rangle_{\mathbb I}=\langle\eta,\zeta\rangle_{\mathbb I}$; differentiating at $g=e$ along $\exp_G(t\xi)$ gives $\langle\mathrm{ad}_\xi\eta,\zeta\rangle_{\mathbb I}+\langle\eta,\mathrm{ad}_\xi\zeta\rangle_{\mathbb I}=0$, i.e. every $\mathrm{ad}_\xi$ is **skew**. That is exactly the statement that the induced $\mathfrak g^*\cong\mathfrak g$ turns $\mathrm{ad}^*_\xi$ into $-\mathrm{ad}_\xi$ — so the identification is the hypothesis, not a free lunch.

$SE(3)$ is not compact and carries no $\mathrm{Ad}$-invariant inner product ([[riemannian-geometry]], left-invariant metrics), so the naive $\langle\cdot,\cdot\rangle$ above cannot be one. Take $\xi=(0,e_1)$ and $\eta=(0,e_2)$. From Problem 2,
$$\mathrm{ad}_{(0,e_1)}(0,e_2)=(0\times0,\;0\times e_2-0\times e_1)=(0,0),$$
$$\mathrm{ad}^*_{(0,e_1)}(0,e_2)=(0\times 0+e_2\times e_1,\;e_2\times 0)=(-e_3,\,0)\neq(0,0).$$
So $\mathrm{ad}^*_\xi\eta\neq-\mathrm{ad}_\xi\eta$; worse, $\eta$ lies in $\ker\mathrm{ad}_\xi$ but not in $\ker\mathrm{ad}^*_\xi$, so the two operators do not even share a kernel and no rescaling of the inner product can repair it. Practical consequence: on $SE(3)$ any formula written with "$-\mathrm{ad}$" in place of "$\mathrm{ad}^*$" is wrong, and the metric adjoint $\widetilde{\mathrm{ad}}_\xi=\mathbb I^{-1}\mathrm{ad}^*_\xi\mathbb I$ of [[notation]] is a genuinely third operator. Lesson 03 shows that its non-vanishing, $\nabla_\xi\xi=-\widetilde{\mathrm{ad}}_\xi\xi$, is precisely the gap between the Lie and Riemannian exponentials.

:::warning[Open question]
$\mathrm{ad}^*$, $\mathrm{Ad}^*$ and the pairing are metric-free, hence intrinsic outright. But every *bound* eventually needs a norm on $\mathfrak g^*$, and that norm comes from $\mathbb I$. On $SE(3)$ the choice is not canonical, so any constant of the form $\sup\|\mathrm{ad}^*_\xi\|$ is $\mathbb I$-dependent — a softer cousin of the chart-dependence this project is removing. Whether the downstream tube constants can be stated in terms of $\mathrm{Ad}$-invariance defect alone, rather than a chosen $\mathbb I$, is open.
:::
