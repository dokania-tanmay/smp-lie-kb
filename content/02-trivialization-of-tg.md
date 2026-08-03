---
tags: [lie-groups, mechanics, bundles, foundations]
---
# Trivialization of $TG$ and $T^*G$

**Prereq:** [[riemannian-geometry]] (groups, bundles, sections), [[mechanical-systems-on-lie-groups]], [[01-adjoint-and-coadjoint]]
**Goal:** turn a state $(g,\dot g)\in TG$ into a pair $(g,\xi)\in G\times\mathfrak g$, know that this is a genuine bundle isomorphism, and know why it splits the equations of motion into a reconstruction equation and a dynamic equation.

## The trivialization maps

Throughout, $G$ is a matrix Lie group, so $T_gG$ is a set of matrices and $L_g$, $R_g$ act by matrix multiplication: $T_eL_g\,\eta = g\eta$ and $T_eR_g\,\eta=\eta g$.

:::info[Definition]
The **left trivialization** of $TG$ is
$$\lambda : TG \to G\times\mathfrak g, \qquad \lambda(g,\dot g) = \big(g,\ (T_gL_{g^{-1}})\dot g\big) = (g,\ g^{-1}\dot g).$$
Its second component $\xi = g^{-1}\dot g\in\mathfrak g$ is the **body velocity**. The **right trivialization** is
$$\rho : TG\to G\times\mathfrak g,\qquad \rho(g,\dot g) = \big(g,\ (T_gR_{g^{-1}})\dot g\big) = (g,\ \dot g\,g^{-1}),$$
and $\xi_s = \dot g\,g^{-1}$ is the **spatial velocity**.
:::

Both are defined pointwise on each fibre and both are linear there, with inverses $(g,\xi)\mapsto g\xi$ and $(g,\xi_s)\mapsto\xi_s g$. Neither uses a chart, a metric, or a connection — only the group multiplication. Per the notation contract in [[notation]] the project runs on **left (body) trivialization** unless stated otherwise.

:::tip[Proposition]
$\xi_s = \mathrm{Ad}_g\,\xi$. The same tangent vector has two algebra representatives, and they differ by the adjoint action.
:::

*Proof.* $\xi_s = \dot g g^{-1} = g(g^{-1}\dot g)g^{-1} = g\xi g^{-1} = \mathrm{Ad}_g\xi$. $\square$

So "body" and "spatial" are not two conventions for the same object; they are two sections of the same bundle isomorphism class, and the discrepancy is exactly $\mathrm{Ad}$. They agree for every $g$ and every $\dot g$ iff $\mathrm{Ad}_g=\mathrm{id}$ for all $g$ — for connected $G$, iff $G$ is abelian.

:::tip[Lemma]
Along a curve $g(t)$ with body velocity $\xi=g^{-1}\dot g$, for any fixed $\eta\in\mathfrak g$,
$$\tfrac{d}{dt}\,\mathrm{Ad}_{g(t)}\eta \;=\; \mathrm{Ad}_{g}\,\mathrm{ad}_\xi\,\eta .$$
:::

*Proof.* $\frac{d}{dt}(g\eta g^{-1}) = \dot g\eta g^{-1} - g\eta g^{-1}\dot g g^{-1} = g(\xi\eta-\eta\xi)g^{-1} = \mathrm{Ad}_g[\xi,\eta]$, using $\frac{d}{dt}g^{-1}=-g^{-1}\dot gg^{-1}$. $\square$

## Every Lie group is parallelizable

:::tip[Theorem]
$\lambda$ is a diffeomorphism and a vector-bundle isomorphism over $\mathrm{id}_G$: it is fibrewise linear, smooth with smooth inverse, and commutes with the projections. Hence $TG\cong G\times\mathfrak g$ globally, and **every Lie group is parallelizable**.
:::

Equivalently: pick any basis $\{e_i\}$ of $\mathfrak g$ and the left-invariant fields $E_i(g)=ge_i$ are globally defined, smooth, and a basis of $T_gG$ at every $g$ — a global frame. Compare [[riemannian-geometry]]: a fibre bundle is only *locally* a product, and a global frame is exactly the obstruction that usually fails. On a group it never fails, because left translation moves a basis of $T_eG$ to every other fibre without choices.

This is why $TG$ is trivial even for topologically interesting $G$: $SO(3)\cong\mathbb{RP}^3$ is not simply connected, yet $T(SO(3))\cong SO(3)\times\mathbb R^3$. The nontrivial topology sits entirely in the base.

The converse fails hard, and that is problem 4: a manifold with no global frame — $S^2$ — admits no Lie group structure at all.

## The dual statement

:::info[Definition]
The **left trivialization of $T^*G$** is $\lambda^* : T^*G\to G\times\mathfrak g^*$, $\alpha_g\mapsto(g,\mu)$ with the **body momentum**
$$\mu = (T_e L_g)^*\alpha_g \in\mathfrak g^*, \qquad \langle\mu,\eta\rangle = \langle\alpha_g,\ g\eta\rangle\ \ \forall\eta\in\mathfrak g,$$
where $\langle\cdot,\cdot\rangle$ is the metric-free pairing. The right version gives the **spatial momentum** $\pi=(T_eR_g)^*\alpha_g$, $\langle\pi,\eta\rangle=\langle\alpha_g,\eta g\rangle$.
:::

Note the direction: $T^*_eL_g$ pulls back covectors from $T^*_gG$ to $\mathfrak g^*$, so no inverse appears. Setting $\eta g = g\zeta$, i.e. $\zeta=\mathrm{Ad}_{g^{-1}}\eta$, gives
$$\langle\pi,\eta\rangle = \langle\mu,\mathrm{Ad}_{g^{-1}}\eta\rangle \quad\Longrightarrow\quad \pi = \mathrm{Ad}^*_{g^{-1}}\mu,$$
matching [[notation]]. Momenta transform by the *coadjoint* action, velocities by the adjoint — which is the whole reason [[01-adjoint-and-coadjoint]] insisted on keeping $\mathfrak g$ and $\mathfrak g^*$ apart.

Consequence: $T^*G\cong G\times\mathfrak g^*$, so Hamiltonian mechanics on a group takes place on $G\times\mathfrak g^*$ with state $(g,\mu)$ rather than on an abstract $2n$-manifold. What the canonical symplectic form looks like in these coordinates is the open question in [[mechanical-systems-on-lie-groups]] and is answered in lesson 11 — it is *not* canonical there; it acquires a $\langle\mu,[\eta_1,\eta_2]\rangle$ term.

## Worked example: $SO(3)$

Let $R(t)\in SO(3)$. Differentiating $R^\top R = I$ gives $\dot R^\top R + R^\top\dot R=0$, so $R^\top\dot R$ is skew — it lies in $\mathfrak{so}(3)$, as the trivialization promises. Write both representatives with the hat map of [[notation]]:
$$\hat\Omega = R^\top\dot R \quad(\text{body}), \qquad \hat\omega = \dot R R^\top\quad(\text{spatial}).$$
$\Omega$ is the angular velocity an onboard gyroscope reads; $\omega$ is what a fixed observer measures. By the proposition, $\hat\omega = \mathrm{Ad}_R\hat\Omega = R\hat\Omega R^\top$. Now push it through the hat map. For $R\in SO(3)$, $a,b\in\mathbb R^3$:
$$R\hat a R^\top b = R\big(a\times R^\top b\big) = (Ra)\times(RR^\top b) = (Ra)\times b = \widehat{(Ra)}\,b,$$
where the middle step is $R(u\times v)=(Ru)\times(Rv)$, valid because $\det R=+1$. Since $b$ was arbitrary, $R\hat aR^\top = \widehat{Ra}$. Applying this with $a=\Omega$:
$$\hat\omega = R\hat\Omega R^\top = \widehat{R\Omega} \quad\Longrightarrow\quad \boxed{\ \omega = R\,\Omega\ }$$
Direct check without $\mathrm{Ad}$: $\hat\omega = \dot RR^\top = R(R^\top\dot R)R^\top = R\hat\Omega R^\top$. Same thing.

**Read what this says.** One physical motion of one rigid body; two vectors $\Omega\ne\omega$ in the same $\mathbb R^3$. They are not two coordinate expressions of one vector in two charts — no chart was used. They are the images of one element of $T_RSO(3)$ under two different bundle isomorphisms, and $\mathrm{Ad}_R$ is the map between them. Euler's equations $\mathbb J\dot\Omega=\mathbb J\Omega\times\Omega+\tau$ are stated in the body representative; in the spatial one they look different.

## The split

Left trivialization turns a second-order system on $G$ into a first-order system on $G\times\mathfrak g$, and the two components decouple in structure:
$$\underbrace{\dot g = g\,\xi}_{\text{reconstruction (kinematic)}}, \qquad \underbrace{\dot\mu = \mathrm{ad}^*_\xi\mu + f}_{\text{dynamic}},\qquad \mu=\mathbb I\xi .$$
The reconstruction equation is nothing but the definition of $\xi$ read backwards — it is free, and it is where all of the group's topology lives. The dynamic equation is a flow on the **fixed vector space** $\mathfrak g^*$, of dimension $n$ rather than $2n$, and for left-invariant Lagrangians it does not depend on $g$ at all. That reduction is the payoff and is the whole reason to trivialize.

Deriving the dynamic equation is lesson 10 (Euler–Poincaré, via constrained variations $\delta\xi=\dot\eta+\mathrm{ad}_\xi\eta$); it is stated here only to show what the split is for. The $\mathrm{ad}^*_\xi\mu$ term is the price of working in the moving body frame — it is exactly the derivative-of-$\mathrm{Ad}$ lemma above, showing up in the dual.

**Which of the three kinds is this?** Intrinsic, but *not canonical*: no chart, no metric and no connection enters $\lambda$ or $\lambda^*$, so nothing here can contribute a $\sup|\partial g_{ij}|$-type constant. What it does carry is a **choice** — left or right — and the two are related by $\mathrm{Ad}_g$, which on a non-compact group like $SE(3)$ is unbounded. So any estimate that mixes body and spatial quantities will pay $\|\mathrm{Ad}_g\|$. That constant is intrinsic (it is a property of $G$, not of a chart), but it is not harmless: flag it wherever it appears.

## Problems

1. **Recall.** Without looking: write $\lambda:TG\to G\times\mathfrak g$ and its inverse; write the definition of body momentum $\mu$ as a pairing. Then say why $\mu$ lands in $\mathfrak g^*$ and not $\mathfrak g$, given that no metric has been chosen.

2. **Compute.** For $SE(3)$ in homogeneous coordinates, $g=\begin{pmatrix}R&p\\0&1\end{pmatrix}$ with $R\in SO(3)$, $p\in\mathbb R^3$, compute the body velocity $\xi=g^{-1}\dot g$ and the spatial velocity $\xi_s=\dot g g^{-1}$ as $4\times4$ matrices. Identify the translational part of each and say in words what it measures.

3. **Prove.** Let $g(t)$ have body velocity $\xi(t)$ and spatial velocity $\xi_s(t)=\mathrm{Ad}_{g}\xi$. Show $\dot\xi_s = \mathrm{Ad}_g\dot\xi$ — the accelerations are related by the *same* $\mathrm{Ad}$, with no extra term. Deduce that constant body velocity implies constant spatial velocity, and give the curve.

4. **Break it.** Two failures.
   (a) Show that $\lambda=\rho$ (left and right trivialization agree on all of $TG$) iff $\mathrm{Ad}_g=\mathrm{id}$ for every $g$, and exhibit an explicit $R\in SO(3)$ and $\hat\Omega\in\mathfrak{so}(3)$ with $\mathrm{Ad}_R\hat\Omega\ne\hat\Omega$. So the choice of trivialization is real, not bookkeeping.
   (b) The theorem above is a statement about groups, not manifolds. Using the hairy-ball theorem (every continuous vector field on $S^2$ vanishes somewhere), show $TS^2\not\cong S^2\times\mathbb R^2$, and conclude that $S^2$ admits no Lie group structure. Which step of the parallelizability argument is unavailable on $S^2$?

---

## Solutions

**1.** $\lambda(g,\dot g)=(g,g^{-1}\dot g)$, inverse $(g,\xi)\mapsto(g,g\xi)$. Body momentum: $\mu=(T_eL_g)^*\alpha_g$, i.e. $\langle\mu,\eta\rangle=\langle\alpha_g,g\eta\rangle$ for all $\eta\in\mathfrak g$. $\lambda^*$ is built from the *pullback* of $T_eL_g$, and a pullback maps covectors to covectors: $\alpha_g\in T^*_gG$ so $\mu\in\mathfrak g^*$. Identifying $\mathfrak g^*$ with $\mathfrak g$ would require an inner product on $\mathfrak g$; the trivialization uses none, and in mechanics that identification is $\mathbb I$, which is a physical input (inertia), not a canonical one.

**2.** $g^{-1}=\begin{pmatrix}R^\top&-R^\top p\\0&1\end{pmatrix}$, $\dot g=\begin{pmatrix}\dot R&\dot p\\0&0\end{pmatrix}$. Then
$$\xi = g^{-1}\dot g = \begin{pmatrix}R^\top\dot R & R^\top\dot p\\0&0\end{pmatrix} = \begin{pmatrix}\hat\Omega & R^\top\dot p\\0&0\end{pmatrix},\qquad
\xi_s = \dot g g^{-1} = \begin{pmatrix}\dot RR^\top & \dot p-\dot RR^\top p\\0&0\end{pmatrix}=\begin{pmatrix}\hat\omega & \dot p-\omega\times p\\0&0\end{pmatrix}.$$
Body translational part $v=R^\top\dot p$: the velocity of the origin resolved in the body frame — what a strapdown accelerometer integrates. Spatial part $\dot p-\omega\times p$: the velocity, in the fixed frame, of the body point currently at the spatial origin. It is *not* $\dot p$, which is why "spatial velocity" is a screw and not just $\dot p$.

**3.** Differentiate $\xi_s=\mathrm{Ad}_{g}\xi$ with the product rule, using the lemma for the first factor:
$$\dot\xi_s = \mathrm{Ad}_g\,\mathrm{ad}_\xi\xi + \mathrm{Ad}_g\dot\xi = \mathrm{Ad}_g[\xi,\xi] + \mathrm{Ad}_g\dot\xi = \mathrm{Ad}_g\dot\xi,$$
since $[\xi,\xi]=0$. If $\xi\equiv\xi_0$ is constant then $\dot\xi_s=0$, so $\xi_s$ is constant too. The curve is $g(t)=g_0\exp_G(t\xi_0)$ (Lie exponential — matrix exponential here), and indeed $\xi_s=\dot gg^{-1}=g_0\xi_0g_0^{-1}=\mathrm{Ad}_{g_0}\xi_0$, independent of $t$.

**4(a).** $\lambda=\rho$ means $g^{-1}\dot g=\dot gg^{-1}$ for all $(g,\dot g)$. Fibrewise, every $\dot g\in T_gG$ is $g\xi$ for some $\xi\in\mathfrak g$, so the condition reads $\xi=\mathrm{Ad}_g\xi$ for all $\xi\in\mathfrak g$ and all $g$, i.e. $\mathrm{Ad}_g=\mathrm{id}$. For connected $G$ this forces $\mathrm{ad}_\eta=0$, i.e. $[\cdot,\cdot]\equiv0$, i.e. $G$ abelian. Counterexample: take $R=\mathrm{diag}(1,-1,-1)$ (rotation by $\pi$ about $e_1$) and $\Omega=e_2$. Then $\mathrm{Ad}_R\hat\Omega=\widehat{R\Omega}=\widehat{-e_2}=-\hat\Omega\ne\hat\Omega$. A gyro reading $+1$ rad/s about body-$y$ corresponds to $-1$ rad/s about spatial-$y$.

**4(b).** If $TS^2\cong S^2\times\mathbb R^2$ as a vector bundle, then the constant section $x\mapsto(x,(1,0))$ pulls back to a smooth vector field on $S^2$ that is nowhere zero (the isomorphism is a linear isomorphism on each fibre, so it does not kill a nonzero vector). The hairy-ball theorem forbids this, so $TS^2$ is nontrivial. If $S^2$ carried a Lie group structure, the theorem would give $TS^2\cong S^2\times\mathfrak g$ with $\dim\mathfrak g=2$ — contradiction. Hence no Lie group structure exists on $S^2$.
The unavailable step is the frame construction $E_i(g)=ge_i$: it needs a globally defined, smooth, fibrewise-invertible way to move one basis of one tangent space to every other tangent space. Left translation supplies exactly that, and it exists only because the group multiplication is defined everywhere and $L_g$ is a diffeomorphism for every $g$. On $S^2$ there is no such family of maps — its symmetry group $SO(3)$ acts transitively but not freely (a stabilizer $SO(2)$ fixes each point), so $S^2$ is a homogeneous space and not a torsor, and the identification of tangent spaces is only defined up to that $SO(2)$.
