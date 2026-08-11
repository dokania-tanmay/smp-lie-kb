---
tags: [trajectory-optimization, set-erosion, probabilistic-tube, planning, so3]
---
# Deterministic Surrogate of a Stochastic Trajectory-Optimization Problem

**Prereq:** [[27-set-erosion-tubes]] (the erosion theorem), [[28-intrinsic-amgf]] (where $r_{\delta,t}$ comes from), [[17-curvature-corrected-stiffness]] (the tracking controller and its region), [[10-euler-poincare]] (the nominal dynamics), [[notation]]
**Goal:** replace a chance-constrained optimal-control problem on $G$ by a deterministic program over nominal curves with **geodesically eroded** constraints, and know precisely where the replacement is conservative and where it stops being valid at all.

This is pathway step 6. The whole lesson rests on one observation from [[27-set-erosion-tubes]]: the set-erosion theorem of [[@liuSafetyVerificationStochastic2024a]] Thm 1 assumes **nothing** about the drift or the diffusion. It is set algebra plus the sup-over-time tube hypothesis. So once [[28-intrinsic-amgf]] delivers a radius, erosion is free — and free of coordinates.

## The two problems

Throughout: $G$ a matrix Lie group, state $\alpha_t\in T^*G$ over $g_t$, $\mathcal C\subseteq G$ a closed safe set in **configuration**, $T$ a horizon, $\delta\in(0,1)$. Distance $d_{\mathbb G}$ on $G$ is that of the left-invariant metric; $d_{G_\alpha}$ on $T^*G$ is that of the cross-term contraction metric of [[17-curvature-corrected-stiffness]].

:::info[Definition — the stochastic problem $\mathrm P_{\text{stoch}}$]
Minimize $J$ over **feedback policies** $u:\,T^*G\times[0,T]\to\mathfrak g^*$ driving the noisy forced Euler–Poincaré system of [[10-euler-poincare]]/[[22-force-vs-configuration-noise]],
$$dg_t=g_t\xi_t\,dt,\qquad d\mu_t=\big(\mathrm{ad}^*_{\xi_t}\mu_t+f(g_t)+u_t\big)dt+\Sigma\,dW_t,\qquad \xi_t=\mathbb I^{-1}\mu_t,$$
subject to the boundary conditions $g_0=g_{\mathrm i}$, $g_T=g_{\mathrm f}$ and the **chance constraint**
$$\mathbb P\big[\,g_t\in\mathcal C\ \ \forall t\le T\,\big]\ \ge\ 1-\delta .$$
:::

:::info[Definition — geodesic erosion]
For $\mathcal C\subseteq M$ and $r\ge0$, the **erosion** of $\mathcal C$ by the geodesic ball is
$$\mathcal C\ominus B(r)\;:=\;\{x\in M:\ \bar B(x,r)\subseteq\mathcal C\},\qquad \bar B(x,r)=\{y: d(x,y)\le r\}.$$
This is the intrinsic replacement for the Minkowski difference, written $\mathcal C\ominus_{\mathbb G}r$ in [[28-intrinsic-amgf]] — same object. Note it needs **no vector-space structure**: the Euclidean $\mathcal C\ominus B^N(r,0)$ is defined through $\oplus$, but the equivalent characterisation "every point within $r$ is still safe" uses only the metric, and that is the one that lifts.

*Dimension symbol.* Following [[27-set-erosion-tubes]] and [[28-intrinsic-amgf]], $N$ is the **state** dimension the sphere average runs over — $N=2\dim G$ on $T^*G$, so $N=6$ for the rigid body — while $n=\dim G$ stays as in [[notation]].
:::

:::info[Definition — the deterministic surrogate $\mathrm P_{\det}$]
Minimize $J$ over **deterministic curves** $(\bar g_t,\bar\mu_t)$ on $T^*G$ obeying the noiseless forced Euler–Poincaré equations with an open-loop $\bar u_t$, same boundary conditions, subject to the pointwise-in-time deterministic constraint
$$\bar g_t\ \in\ \mathcal C\ominus B\big(c_\pi\, r_{\delta,t}\big)\qquad\forall t\in[0,T].$$
No probability appears. $r_{\delta,t}$ is the tube radius from [[28-intrinsic-amgf]] for the closed loop of [[17-curvature-corrected-stiffness]] tracking $\bar g_t$, and $c_\pi$ is the Lipschitz constant of $\pi:T^*G\to G$ in the pair $(d_{G_\alpha},d_{\mathbb G})$ — see the remark below.
:::

## The reduction

:::tip[Proposition — sound surrogate]
Suppose the tracking controller of [[17-curvature-corrected-stiffness]] achieves the intrinsic tube of [[28-intrinsic-amgf]] around $\bar\alpha_t$,
$$\mathbb P\big[\,d_{\mathbb G}(g_t,\bar g_t)\le c_\pi r_{\delta,t}\ \ \forall t\le T\,\big]\ \ge\ 1-\delta, \tag{$\ast$}$$
and that $\bar g_t\in\mathcal C\ominus B(c_\pi r_{\delta,t})$ for all $t\le T$. Then $\mathbb P[g_t\in\mathcal C\ \forall t\le T]\ge1-\delta$.

Hence: **feasible for $\mathrm P_{\det}$ $\Rightarrow$ feasible for $\mathrm P_{\mathrm{stoch}}$**, and $J(\mathrm P_{\det}^\star)\ge J(\mathrm P_{\mathrm{stoch}}^\star)$. Proof: problem 3.
:::

The converse fails, and that is the whole cost of the method. $\mathrm P_{\det}$ infeasible does **not** mean $\mathrm P_{\text{stoch}}$ is: erosion demands that *every* point of the ball be safe, which is a worst-case over directions, while a violation needs the realised deviation to point at the constraint. Problem 4 makes this quantitative.

**Why it survives the move to a manifold.** The Euclidean proof ([[@liuSafetyVerificationStochastic2024a]] Thm 1) writes $X_t\in\{x_t\}\oplus B^n(r,0)$ and puts the sum inside $\mathcal C$. The intrinsic version never forms a sum: ($\ast$) says $g_t\in\bar B(\bar g_t,r)$ directly, and the erosion hypothesis says $\bar B(\bar g_t,r)\subseteq\mathcal C$. Transitivity of $\subseteq$ closes it. Nothing chart-dependent, no curvature, no injectivity radius — the geometry is entirely inside $r_{\delta,t}$. This is the one step of the whole programme that is **free**.

:::warning[Remark — the tube lives on $T^*G$, the constraint on $G$]
[[17-curvature-corrected-stiffness]] certifies contraction in $G_\alpha(w,w)=a\|u\|^2+2b\langle u,\xi\rangle+c\|\xi\|^2$ on the $2n$-manifold, so the tube radius is a $T^*G$-distance. Projecting: $G_\alpha(w,w)=z^\top\mathcal Pz\ge\lambda_{\min}(\mathcal P)\|u\|^2$ with $z=(\|u\|,\|\xi\|)$, so $\pi$ is Lipschitz with
$$c_\pi=\lambda_{\min}(\mathcal P)^{-1/2}.$$
For the worked example of [[17-curvature-corrected-stiffness]] ($d=2.5$, $\mathcal P$ with entries $a=8.125$, $b=1.25$, $c=1$), $\mathrm{spec}(\mathcal P)=\{8.338,\ 0.787\}$, so $c_\pi\approx1.13$ — a 13% inflation of the erosion depth, paid purely for the cross term $b$ that made the certificate work at all. Direct erosion of a *state* constraint in $T^*G$ would avoid it.
:::

## What the nominal must satisfy — and the planner/controller coupling

$\bar g_t$ is not a free curve. It must (i) solve the deterministic forced Euler–Poincaré equations of [[10-euler-poincare]] with an admissible $\bar u$, and (ii) stay inside the **contraction region** $\mathcal W\subseteq T^*G$ of [[17-curvature-corrected-stiffness]] together with a neighbourhood of radius $r_{\delta,t}$ — because outside $\mathcal W$ the rate $\lambda$ does not exist and $r_{\delta,t}$ is not a valid radius.

So $\mathrm P_{\det}$ silently inherits every regional limitation of Phase 3:

- **A velocity cap.** Negative $\mathrm{Sec}$ forces $\sup_{\mathcal W}\|v\|^2<\lambda_{\min}(\mathrm{Hess}^\sharp(V+\varphi))/|\mathrm{Sec}_-|$. For the rigid body with $\mathbb J=\mathrm{diag}(1,2,3)$ and $\mathrm{spec}(\mathrm{Hess}^\sharp\varphi)\subset[4,6]$ this was $|\Omega|<2\ \mathrm{rad/s}$. That is a **hard state constraint the planner must also carry**, and it comes from curvature, not from actuator limits.
- **A topological obstruction.** Contraction regions are contractible, so $\mathcal W$ is never all of $T^*SO(3)$. A nominal path that wraps the group can leave $\mathcal W$ even at low speed.

This is a genuine two-way coupling: the planner may not use the whole configuration space, and the controller's gains set the radius the planner must erode by.

## Worked example — attitude planning on $SO(3)$ with a keep-out cone

Steer a rigid body from $R_{\mathrm i}$ to $R_{\mathrm f}$ while keeping a body-fixed boresight $b\in S^2$ (a star tracker) at least $\theta_0$ away from an inertial bright direction $s\in S^2$ (the Sun):
$$\mathcal C=\{R\in SO(3):\ \angle(Rb,s)\ \ge\ \theta_0\}\ =\ \{R:\ s^\top Rb\le\cos\theta_0\}.$$

Take $\mathbb J=j\,\mathrm{id}$, so the metric is bi-invariant and $d_{\mathbb G}(R_1,R_2)=\sqrt j\,\phi(R_1^\top R_2)$ with $\phi=\|\log_G(\cdot)^\vee\|$ the relative rotation angle (the $\sqrt j$ is the notation contract's $\langle\eta,\zeta\rangle=\tfrac12\mathrm{tr}(\eta^\top\zeta)$ scaled by $\mathbb I$).

**The erosion, computed.** Write $R'=R\exp_G(\hat w)$. Then $R'b=R\exp_G(\hat w)b$, and Rodrigues gives $\angle(b,\exp_G(\hat w)b)\le|w|$, with equality iff $w\perp b$. So a geodesic ball of radius $\rho$ *in angle* moves the boresight by at most $\rho$, and that bound is attained. Therefore
$$\bar B(R,\sqrt j\rho)\subseteq\mathcal C\iff \angle(Rb,s)\ \ge\ \theta_0+\rho
\qquad\Longrightarrow\qquad
\boxed{\ \mathcal C\ominus B(r)=\{R:\ \angle(Rb,s)\ge\theta_0+\tfrac{r}{\sqrt j}\}\ }$$
The keep-out cone **grows** by the erosion depth $\rho_t=c_\pi r_{\delta,t}/\sqrt j$ radians; equivalently the admissible pointing region on $S^2$ shrinks by that geodesic amount. This is exactly what "erode a set on a curved space" means, and note that no chart was used to say it.

**Numbers.** $j=1$, $\theta_0=30^\circ$, $c_\pi=1.13$ from the remark above, and an illustrative radius $r_{\delta,t}=0.10$ in $d_{G_\alpha}$-units from [[28-intrinsic-amgf]] (which supplies the shape but no $SO(3)$ number; [[27-set-erosion-tubes]]'s worked example lands at $r_{\delta,T}=0.356$, so this is the right order): $\rho=0.113$ rad $=6.5^\circ$, so the planner must respect a $36.5^\circ$ cone. Two further facts, both intrinsic and both absent in $\mathbb R^n$: $\mathrm{diam}(SO(3))=\pi\sqrt j$, so erosion is **globally destructive** — $\rho\ge\pi-\theta_0=150^\circ$ empties $\mathcal C\ominus B(r)$ outright; and the free region on $S^2$ is a spherical cap of area $2\pi(1+\cos(\theta_0+\rho))$, which shrinks *faster than linearly* in $\rho$ near $\theta_0+\rho=\pi/2$.

## Discretisation

The surrogate constraint is indexed by $t\in[0,T]$, a continuum. In practice one imposes it on a grid $0=t_0<\dots<t_N=T$ and gets nothing between nodes. Two honest repairs:

1. **Inflate.** If $\bar g$ has speed $\le v_{\max}$ and $r_{\delta,t}$ is $\ell_r$-Lipschitz in $t$, then enforcing $\bar g_{t_k}\in\mathcal C\ominus B\big(c_\pi r_{\delta,t_k}+(v_{\max}+\ell_r)h/2\big)$ at the nodes, $h=\max_k(t_{k+1}-t_k)$, implies the continuous constraint — because $d_{\mathbb G}(\bar g_t,\bar g_{t_k})\le v_{\max}h/2$ and erosion is monotone in $r$.
2. **Certify.** Use a parametrisation whose collision function is checkable in closed form on each segment; this is what the safe-corridor construction of [[@wattersonTrajectoryOptimizationManifolds2020]] buys on manifolds.

Repair 1 is the one that composes with everything above and costs an $O(h)$ addition to the erosion depth. It should not be skipped: a grid-only surrogate is **not** sound, and the Proposition does not cover it.

:::warning[Open question]
1. **The radius depends on the gains.** $r_{\delta,t}$ is built from $\lambda$ and $\lambda_{\max}(\mathcal P)$, which depend on $d$ and on the shaping potential $\varphi$ — so $\mathcal C\ominus B(c_\pi r_{\delta,t})$ moves when the controller is retuned. Stiffer shaping enlarges $\mathcal W$ *and* shrinks the tube, but raises the torque the nominal must be able to spare for tracking. Jointly optimizing $(\bar g,\varphi,d)$ is a coupled design problem no source here solves; [[@maFeedbackMotionPlanning2026]] is the closest — predicate erosion plus contraction-based tracker synthesis — but is Euclidean and treats the controller family as fixed.
2. **Optimizing over curves on $G$.** $\mathrm P_{\det}$ is still an optimization over a non-Euclidean feasible set. The available machinery — embedded SCP [[@bonalliTrajectoryOptimizationManifolds2019]], safe corridors [[@wattersonTrajectoryOptimizationManifolds2020]], error-state convex MPC on Lie groups [[@jangConvexGeometricTrajectory2023]], constraint manifolds with corners [[@zhangCMCOptConstraintManifold2026]] — is *not* neutral: embedding-based methods reintroduce ambient coordinates, which is precisely the chart-dependence the thesis removes upstream. Whether an eroded constraint expressed intrinsically stays intrinsic through the solver is unresolved.
3. **Anisotropy.** The tube of [[@liuConcentrationStochasticSystem2026]] is an ellipsoid $\|X_t-x_t\|_{M_t}\le r$; erosion by a *round* geodesic ball throws that away. On a manifold there is no clean analogue of "erode by an ellipsoid" — the anisotropy would have to be carried as a field of shapes over $\bar g_t$.
:::

## Problems

1. **Recall/state.** Write down $\mathrm P_{\mathrm{stoch}}$ and $\mathrm P_{\det}$ side by side. State which implication between "feasible for $\mathrm P_{\det}$" and "feasible for $\mathrm P_{\mathrm{stoch}}$" holds, and give the one-sentence reason the other fails.
2. **Compute.** Rigid body with $\mathbb J=4\,\mathrm{id}$, keep-out half-angle $\theta_0=30^\circ$, $c_\pi=1.13$, $r_{\delta,t}=0.20$. (a) Give the eroded constraint explicitly. (b) Find the largest $r_{\delta,t}$ for which the eroded set is nonempty.
3. **Prove.** Prove the Proposition. Then prove the two facts the discretisation repair needs: $r\mapsto\mathcal C\ominus B(r)$ is nonincreasing, and $\bar B(y,\varepsilon)\subseteq\bar B(x,r+\varepsilon)$ whenever $d(x,y)\le r$.
4. **Break it.** State dimension $N=6$ ($T^*SO(3)$), radius of the shape $r_{\delta,t}=\vartheta\sqrt{\varepsilon_1N+\varepsilon_2\log(1/\delta)}$ with $\varepsilon_1=\varepsilon^{-2}\log\frac1{1-\varepsilon^2}$, $\varepsilon_2=2/\varepsilon^2$ ([[27-set-erosion-tubes]]). Take $\varepsilon=0.9$, $\delta=10^{-3}$. A straight corridor has half-width $w$ (in $d_{\mathbb G}$) about the nominal, and the *only* constraint is not to cross either wall. Find the range of $w$ for which $\mathrm P_{\det}$ is infeasible for **every** nominal while the chance constraint is still met by the centred nominal. Name the two distinct sources of the gap.

---

## Solutions

**1.** $\mathrm P_{\mathrm{stoch}}$: minimize over feedback policies subject to $\mathbb P[\forall t\le T:g_t\in\mathcal C]\ge1-\delta$. $\mathrm P_{\det}$: minimize over deterministic Euler–Poincaré curves subject to $\bar g_t\in\mathcal C\ominus B(c_\pi r_{\delta,t})$ for all $t$, no probability. **Feasible for $\mathrm P_{\det}\Rightarrow$ feasible for $\mathrm P_{\mathrm{stoch}}$** — a sufficient condition. The converse fails because erosion requires *every* point of $\bar B(\bar g_t,r)$ to be safe, a worst case over all directions and all $t$ simultaneously, whereas a violation requires the realised deviation to point at the constraint.

**2.** (a) $\sqrt j=2$, depth $\rho=c_\pi r/\sqrt j=1.13\cdot0.20/2=0.113$ rad $=6.47^\circ$. Eroded set $\{R:\angle(Rb,s)\ge36.47^\circ\}$. (b) Nonempty iff $\theta_0+\rho<\pi$, i.e. $\rho<150^\circ=2.618$ rad, i.e. $r<\sqrt j\rho/c_\pi=2\cdot2.618/1.13\approx4.63$. (Compare $\mathrm{diam}=\pi\sqrt j=6.28$: erosion kills the set well before the radius reaches the diameter.)

**3.** *Proposition.* Let $E$ be the event in ($\ast$); $\mathbb P(E)\ge1-\delta$. On $E$, for each $t\le T$: $d_{\mathbb G}(g_t,\bar g_t)\le c_\pi r_{\delta,t}$, so $g_t\in\bar B(\bar g_t,c_\pi r_{\delta,t})$. The erosion hypothesis says $\bar B(\bar g_t,c_\pi r_{\delta,t})\subseteq\mathcal C$. Hence $g_t\in\mathcal C$ for all $t\le T$ on $E$, so $\mathbb P[\forall t\le T:g_t\in\mathcal C]\ge\mathbb P(E)\ge1-\delta$. $\square$ Only transitivity of $\subseteq$ was used — no Minkowski sum, no vector-space structure, no assumption on drift or diffusion.
*Monotonicity.* If $r\le r'$ then $\bar B(x,r)\subseteq\bar B(x,r')$, so $\bar B(x,r')\subseteq\mathcal C$ implies $\bar B(x,r)\subseteq\mathcal C$: $\mathcal C\ominus B(r')\subseteq\mathcal C\ominus B(r)$.
*Ball inclusion.* If $d(x,y)\le r$ and $d(y,z)\le\varepsilon$ then $d(x,z)\le r+\varepsilon$ by the triangle inequality. Combining the two gives the repair: $\bar g_{t_k}\in\mathcal C\ominus B(c_\pi r_{\delta,t_k}+\eta)$ with $\eta\ge\sup_{|t-t_k|\le h/2}\big(d_{\mathbb G}(\bar g_t,\bar g_{t_k})+c_\pi|r_{\delta,t}-r_{\delta,t_k}|\big)$ forces $\bar g_t\in\mathcal C\ominus B(c_\pi r_{\delta,t})$ on the whole interval.

**4.** $\varepsilon=0.9$: $\varepsilon_1=\log(1/0.19)/0.81=1.6607/0.81=2.050$, $\varepsilon_2=2/0.81=2.469$; $\log(1/\delta)=6.908$. Full dimension $N=6$: $r_{\delta,t}=\vartheta\sqrt{6(2.050)+2.469(6.908)}=\vartheta\sqrt{12.30+17.05}=5.42\,\vartheta$ — the same $5.418$ computed in [[27-set-erosion-tubes]]. The eroded corridor is $\{|y|\le w-5.42\vartheta\}$, **empty for every nominal** when $w<5.42\vartheta$. But crossing a wall is a *scalar* event: apply the same bound to the single wall-normal component, $N=1$, giving $r^{(1)}=\vartheta\sqrt{2.050+17.05}=4.37\,\vartheta$, so the centred nominal already satisfies $\mathbb P[\sup_{t\le T}|y_t|\le4.37\vartheta]\ge1-\delta$. Hence for
$$4.37\,\vartheta\ <\ w\ <\ 5.42\,\vartheta$$
the surrogate is infeasible while $\mathrm P_{\mathrm{stoch}}$ is feasible with the trivial straight-down-the-middle nominal. Two sources: (i) **dimension** — erosion charges $\varepsilon_1N$ for all $6$ state directions when the constraint sees $1$; (ii) **isotropy** — the round ball must clear the wall in every direction, including the $5$ that cannot violate it. Both are artifacts of eroding by a ball, not of the tube being loose; note neither is chart-dependence, so a fully intrinsic $r_{\delta,t}$ does not remove them.
