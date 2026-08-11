---
tags: [contraction, under-actuation, interconnection, small-gain, se3, quadrotor]
---
# Hierarchical Contraction: Under-actuation, Virtual Systems, Interconnection

**Prereq:** [[14-contraction-on-manifolds]], [[16-cross-term-metrics]], [[17-curvature-corrected-stiffness]], [[10-euler-poincare]]
**Goal:** certify a mechanical system that no single feedback law can shape — split it into blocks, contract each, and close the loop with a small-gain condition rather than pretending the coupling is one-way.

## The under-actuation obstruction

[[17-curvature-corrected-stiffness]] builds a certificate by choosing a *desired* force — shaping potential $\varphi$ plus damping $d$ — and asking the actuator to deliver it. That step is silent about whether the actuator can.

:::info[Definition — full actuation, recalled from [[17-curvature-corrected-stiffness]]]
A simple mechanical control system on $Q$ with input covector fields $F^1,\dots,F^m\in T^*Q$ has **input distribution** $\mathcal F_q=\mathrm{span}_{\mathbb R}\{F^a(q)\}\subseteq T_q^*Q$. It is **fully actuated** if $\mathcal F_q=T^*_qQ$ for all $q$ in the region of interest.
:::

Full actuation is used *essentially* in [[17-curvature-corrected-stiffness]]: it is exactly what makes "apply $-\mathrm{d}\varphi-d\,\mathbb G^\flat\xi$" a realisable law rather than a wish. The certificate is a statement about the closed-loop field, and if the field cannot be produced, there is nothing to certify.

:::tip[Proposition — the obstruction on $SE(3)$]
For a quadrotor, $Q=SE(3)$, $\dim\mathfrak{se}(3)^*=6$, and the body wrench realisable by four rotors is $F=(f e_3,\,M)$ with $f\in\mathbb R$, $M\in\mathbb R^3$. Hence
$$\mathcal F_q=\{(ce_3,M):c\in\mathbb R,\ M\in\mathbb R^3\},\qquad \dim\mathcal F_q=4<6.$$
The two missing directions are the body $e_1,e_2$ translations. No choice of $(f,M)$ realises an arbitrary shaping-plus-damping law, so lesson 17's theorem simply does not apply.
:::

This is not repairable by a change of metric. [[15-symplectic-not-contracting]] says contraction requires *breaking* the symplectic structure by feedback; $\mathcal F_q$ says which directions the breaking is allowed to act in, and here it is a codimension-2 subspace. A direct certificate for the un-decomposed system on $T^*SE(3)$ would need kinematic reduction / decoupling vector fields, which is a different theory.

## Partial contraction: certify a subsystem, or a virtual one

:::info[Definition — virtual (auxiliary) system]
Let $\dot x=f(x,t)$ on $M$. A **virtual system** is $\dot y=g(y,x,t)$ on $M$, depending on the true trajectory $x(\cdot)$ as an exogenous signal, such that
$$g(x,x,t)=f(x,t).$$
Then $y=x(t)$ is a *particular solution*. Any other known particular solution — e.g. a reference $y=x_d(t)$, if $g(x_d,x,t)=\dot x_d$ — is a second one.
:::

:::tip[Theorem — partial contraction]
If the virtual system $y\mapsto g(y,x(\cdot),t)$ is contracting in $y$ on a forward-invariant $K$-reachable region, uniformly in the driving signal, then **all** of its solutions converge to each other exponentially in $d_G$. In particular any two particular solutions do; so if both $x(t)$ and $x_d(t)$ solve it, $d_G(x(t),x_d(t))\to0$ at the contraction rate.
:::

The proof is nothing but [[14-contraction-on-manifolds]] applied to $y$ with $x(\cdot)$ frozen as a parameter — no new machinery. What is bought is scope: contraction of the virtual system is a *weaker* claim than contraction of the real one, and correspondingly cheaper. On $SO(3)$, a virtual system in the velocity fibre alone certifies $\Omega\to\Omega_r$ with rate $\lambda_{\min}(\mathrm{sym}_{\mathbb G}K)$, needing **no Hessian and no curvature** — because it suppresses precisely the horizontal channel where $\mathrm{Hess}^\sharp\varphi$ and $\mathrm{Jac}_v$ live. It also does not give $R\to R_d$. Weaker claim, weaker hypotheses; say which you are making.

## Decomposition by a virtual input

The recipe for an under-actuated system:

1. Split the state into an under-actuated block and an actuated block. On $SE(3)$: translation $(x,\dot x)$ and attitude $(R,\Omega)$.
2. Invent a **virtual input** $\upsilon$ for the under-actuated block that would make it fully actuated, and design a law for $\upsilon$ ignoring realisability.
3. Compute the *commanded* configuration of the actuated block that would realise $\upsilon$, and ask the actuated block to track it.
4. Certify each block separately, then handle the mismatch.

Step 4 is where the lesson is.

## This is a feedback interconnection, not a cascade

In a **cascade**, block 1 evolves autonomously and drives block 2; the coupling is triangular, and block-wise contraction plus compactness suffices ([[@simpson-porcoContractionTheoryRiemannian2014]] Lem. 3.1). No gain condition is needed — see Problem 3.

In the quadrotor there are *two* couplings:

- **attitude $\to$ translation**: the delivered thrust is $f b_3$ with $b_3=Re_3$, so attitude error rotates the force away from what was commanded;
- **translation $\to$ attitude**: the commanded attitude $R_c$ is built from the desired force, which depends on the translational error.

Because of the second, the composite is genuinely two-way. A naive cascade argument — "the attitude loop is fast, so treat $b_3=b_{3c}$" — is not a proof; it is a singular-perturbation intuition with no certificate attached. What is needed instead is a **coupling term in the combined metric** and a small-gain condition.

## The interconnection theorem

:::tip[Theorem — feedback small gain]
Let $(\mathcal U_i,X_i,G_i,\lambda_i)$, $i=1,2$, be contracting **with inputs** — contracting uniformly over the input value — on compact $K$-reachable regions, with output maps $h_1:M_1\to\mathbb R^{k_2}$, $h_2:M_2\to\mathbb R^{k_1}$ feeding each other's inputs. Let the induced gains be
$$\gamma_{12}=\sup\frac{\|\partial_{u_1}X_1\circ(Th_2)w\|_{G_1}}{\|w\|_{G_2}},\qquad
\gamma_{21}=\sup\frac{\|\partial_{u_2}X_2\circ(Th_1)v\|_{G_2}}{\|v\|_{G_1}}.$$
If
$$\lambda_1\lambda_2>\gamma_{12}\gamma_{21},$$
then the weighted metric $G=\alpha_1G_1\oplus\alpha_2G_2$ with $\alpha_1/\alpha_2=\gamma_{21}/\gamma_{12}$ makes the interconnection contracting on $\mathcal U_1\times\mathcal U_2$. ([[@simpson-porcoContractionTheoryRiemannian2014]] Lem. 3.2, eqs. (11)–(13).)
:::

The mechanism, in one line: on the product, $\tfrac12\tfrac{d}{dt}\|w\|_G^2\le-\alpha_1\lambda_1\|v\|^2_{G_1}-\alpha_2\lambda_2\|w_2\|^2_{G_2}+(\alpha_1\gamma_{12}+\alpha_2\gamma_{21})\|v\|_{G_1}\|w_2\|_{G_2}$, negative definite iff a $2\times2$ matrix is positive definite; minimising over $z=\alpha_1/\alpha_2$ gives $z^*=\gamma_{21}/\gamma_{12}$ and reduces the condition to the displayed one (Problem 2 is this computation).

**The weights are the coupling term in the metric.** This is the same phenomenon as [[16-cross-term-metrics]], one level up. There, a *single* mechanical system forced a position–velocity cross term $2b\langle u,\xi\rangle$ because the block-diagonal energy metric gives $\lambda=0$. Here, two already-certified blocks force a relative weighting $\alpha_1:\alpha_2$ because the equally-weighted sum does not absorb the cross terms. Both are the project's listed "coupling term in the metric" target; the intra-block one is a genuine off-diagonal, the inter-block one is (in this theorem) only a scaling.

:::warning[Open question — is a block-diagonal product metric enough?]
The theorem produces $G=\alpha_1G_1\oplus\alpha_2G_2$: block-diagonal *between* subsystems. But [[16-cross-term-metrics]] is exactly the observation that a block-diagonal metric can be too weak to certify a system that is in fact contracting. So $\lambda_1\lambda_2>\gamma_{12}\gamma_{21}$ is presumably sufficient but not necessary — an honest off-diagonal block $G_{12}$ ought to relax it. Nobody in the sources constructs one. Note also that [[@simpson-porcoContractionTheoryRiemannian2014]] §6 lists "succinct conditions for a dissipative mechanical system to contract" as *open* even in the fully actuated case; the under-actuated case is strictly harder and is not addressed there at all.
:::

## Worked example — quadrotor on $SE(3)$

Dynamics (left-trivialised, [[notation]] conventions; $\xi=(V,\Omega)$, $b_3=Re_3$, $\mathbb I=\mathrm{diag}(mI_3,\mathbb J)$):
$$m\ddot x=f\,b_3-mg\,e_3,\qquad \mathbb J\dot\Omega+\Omega\times\mathbb J\Omega=M.$$

**Virtual input.** Set $\upsilon:=f b_3\in\mathbb R^3$. If $\upsilon$ were free, $m\ddot x=\upsilon-mge_3$ on $\mathbb R^3$ is fully actuated. It is not free: $\upsilon$ is constrained to the ray through $b_3$. With $e_x=x-x_d$, $e_v=\dot x-\dot x_d$, gains $k_x,k_v>0$,
$$F_{\mathrm{des}}:=-k_xe_x-k_ve_v+mge_3+m\ddot x_d,\qquad f:=F_{\mathrm{des}}\cdot b_3,\qquad b_{3c}:=F_{\mathrm{des}}/\|F_{\mathrm{des}}\|,$$
and $R_c$ is the attitude with third column $b_{3c}$ (heading fixed by a desired $b_{1d}\not\parallel b_{3c}$).

**Translational block.** Substituting,
$$m\ddot e_x+k_ve_v+k_xe_x=\Delta,\qquad \Delta:=-(I-b_3b_3^\top)F_{\mathrm{des}},\qquad \|\Delta\|=\|F_{\mathrm{des}}\|\sin\theta,$$
$\theta=\angle(b_3,b_{3c})$. So $\Delta$ is exactly the part of the desired force the current attitude cannot deliver — it *is* the interconnection signal, and it vanishes iff $b_3=\pm b_{3c}$.

With $\Delta\equiv0$ this is lesson 17's setup on the flat $Q_{\mathrm{tr}}=\mathbb R^3$, metric $\mathbb G_{\mathrm{tr}}=m\,I$, shaping $\varphi_{\mathrm{tr}}=\tfrac{k_x}2\|e_x\|^2$, damping $\mathcal D=\tfrac{k_v}m\mathrm{id}$: flatness gives $\mathrm{Jac}_v\equiv0$, so $\mathcal S_\alpha=\mathrm{Hess}^\sharp\varphi_{\mathrm{tr}}=(k_x/m)\,\mathrm{id}$ and $\mu=\sigma=k_x/m$. Lesson 17's condition $d>(\sigma-\mu)/(2\sqrt\mu)$ reads $k_v/m>0$: **every positive damping gain works** — this is exactly its isotropic consistency check. The certificate still needs the [[16-cross-term-metrics]] cross term,
$$G_{\mathrm{tr}}(w,w)=m\big(a_{\mathrm{tr}}\|u\|^2+2b_{\mathrm{tr}}\,u\cdot\xi+\|\xi\|^2\big),\quad b_{\mathrm{tr}}=\tfrac{k_v}{2m},\ a_{\mathrm{tr}}=\tfrac{k_v^2}{2m^2}+\tfrac{k_x}{m}.$$
Because $\Delta$ enters *additively*, the Jacobian is independent of it: the block is contracting with inputs, uniformly, for free.

**Attitude block.** Lesson 17 verbatim with $R_d$ replaced by $R_c(t)$ and $\tau$ by $M$, giving $(\mathcal W_{\mathrm{att}},G_{\mathrm{att}},\lambda_{\mathrm{att}})$.

**The loop.** $h_2(R,\Omega)=b_3$ determines $\Delta$; $h_1(e_x,e_v)=F_{\mathrm{des}}$ determines $R_c$. Two-way, hence the theorem above with $\gamma_{\mathrm{tr}}\gamma_{\mathrm{att}}<\lambda_{\mathrm{tr}}\lambda_{\mathrm{att}}$. Order of magnitude: $\partial\Delta/\partial b_3=-(b_3F_{\mathrm{des}}^\top+(F_{\mathrm{des}}\cdot b_3)I)$ gives $\gamma_{\mathrm{tr}}=O(\sup\|F_{\mathrm{des}}\|)$, and $\partial b_{3c}/\partial F_{\mathrm{des}}=(I-b_{3c}b_{3c}^\top)/\|F_{\mathrm{des}}\|$ gives $\gamma_{\mathrm{att}}=O(\max(k_x,k_v)/F_{\min})$. Since $\lambda_{\mathrm{att}}$ grows with the attitude gains and $\gamma_{\mathrm{att}}$ does not, the condition is achievable by making the attitude loop fast — timescale separation, but now with a certificate instead of an appeal.

:::warning[Open question — two gaps in this argument]
**(a) $h_1$ is not a function of the translational state.** The attitude block needs $R_c$ *and* the feedforward $\Omega_c,\dot\Omega_c$, i.e. $\dot F_{\mathrm{des}},\ddot F_{\mathrm{des}}$. But $\dot F_{\mathrm{des}}=-k_xe_v-k_v\dot e_v+m\dddot x_d$ and $\dot e_v=(\Delta-k_ve_v-k_xe_x)/m$ contains $\Delta$, hence $b_3$. So the "input" of the attitude block depends on the attitude state — an algebraic loop the theorem's hypothesis $h_1:M_1\to\mathbb R^{k_2}$ forbids. Either $\Omega_c$ must be filtered/estimated, or the state split must be redrawn.

**(b) Autonomy.** [[@simpson-porcoContractionTheoryRiemannian2014]] is stated for time-invariant $X\in\Gamma^\infty(TM)$ throughout, and both blocks here are tracking-error systems around time-varying references. The extension is expected to be routine but is not in the source, so quoting Lem. 3.2 at a time-varying pair is formally out of hypothesis.

A minor bookkeeping point: the $\tfrac12$ printed in the source's gain definition (11) cannot be reconciled with its own condition (13) — the derivation in Problem 2 reproduces (13) exactly with **no** $\tfrac12$. Treat the prefactor as an extraction artifact and re-derive if the constants are ever load-bearing.
:::

## Region conditions

Everything regional from [[17-curvature-corrected-stiffness]] survives, per block, and must additionally be *compatible*:

- **Curvature.** The translational block is flat, so the whole curvature story lives in the attitude block: an inertially asymmetric airframe has negative sectional curvatures ([[06-curvature-left-invariant-metrics]]), so $\mathcal W_{\mathrm{att}}$ is bounded **in velocity** and damping cannot repair it.
- **Topology.** $T^*SE(3)$ retracts onto $SE(3)\simeq \mathbb{RP}^3\times\mathbb R^3$, not contractible; contraction regions are contractible, so no global region exists. The attitude error function keeps its three antipodal critical points.
- **Thrust positivity.** Need $\|F_{\mathrm{des}}\|\ge F_{\min}>0$ and $\theta\le\theta_{\max}<\pi/2$, so $f=\|F_{\mathrm{des}}\|\cos\theta>0$ and $b_{3c}$, $R_c$ are well defined and $C^2$. This is the "do not flip" condition and it bounds the initial attitude error.
- **Saturation.** Contraction is a property of the *unsaturated* field. The product region must be intersected with the unsaturated rotor set, and that intersection shown forward invariant — not done in any source I have.

Under-actuation's real cost: the fully actuated case yields an unconditional theorem, this one yields a theorem conditional on a small-gain hypothesis that must be checked numerically over the region.

## Problems

1. **State.** Define full actuation, and state what partial contraction asserts and what it does *not* assert. Then say in one sentence why lesson 17's certificate fails for the quadrotor.

2. **Compute.** Take $\dot x_1=-\lambda_1x_1+\gamma_{12}x_2$, $\dot x_2=-\lambda_2x_2+\gamma_{21}x_1$ on $\mathbb R^2$ with $\lambda_i,\gamma_{ij}>0$. Using $G=\alpha_1\,dx_1^2+\alpha_2\,dx_2^2$, find the exact condition on $z=\alpha_1/\alpha_2$ for contraction, minimise it, and read off both $z^*$ and the small-gain condition. Then check $(\lambda_1,\lambda_2,\gamma_{12},\gamma_{21})=(2,3,1,4)$.

3. **Prove.** A genuine cascade needs no gain condition: with $\gamma_{12}=0$ and $\gamma_{21}>0$ arbitrary, show a weight $\alpha_1/\alpha_2$ always exists making $G$ a contraction metric, and say which block gets the heavy weight.

4. **Break it.** Exhibit two subsystems, each contracting uniformly over its input, whose *feedback* interconnection has an unstable equilibrium — so no metric whatsoever certifies it. Conclude that block-wise contraction is genuinely insufficient and that the gain condition is sharp in this class.

---

## Solutions

**1.** Full actuation: $\mathcal F_q=\mathrm{span}\{F^a(q)\}=T^*_qQ$ — every covector force is realisable. Partial contraction: if a virtual system $\dot y=g(y,x,t)$ with $g(x,x,t)=f(x,t)$ is contracting in $y$ uniformly in the driving signal, then all its solutions converge to one another; hence any two *particular* solutions do. It asserts convergence of specified signals (e.g. $\Omega\to\Omega_r$); it does **not** assert contraction of the true system, nor convergence in the suppressed channels (e.g. $R\to R_d$). Quadrotor: $\dim\mathcal F_q=4<6$, so the shaping-plus-damping force lesson 17 requires cannot be produced.

**2.** $\tfrac12\tfrac{d}{dt}G=-\alpha_1\lambda_1x_1^2-\alpha_2\lambda_2x_2^2+(\alpha_1\gamma_{12}+\alpha_2\gamma_{21})x_1x_2$. Negative definite iff
$$\alpha_1\alpha_2\lambda_1\lambda_2>\tfrac14(\alpha_1\gamma_{12}+\alpha_2\gamma_{21})^2
\iff \lambda_1\lambda_2>\tfrac14\big(z\gamma_{12}^2+\gamma_{21}^2/z\big)+\tfrac12\gamma_{12}\gamma_{21}.$$
The RHS is convex in $z>0$ with minimum at $z^*=\gamma_{21}/\gamma_{12}$, where $\tfrac14(z^*\gamma_{12}^2+\gamma_{21}^2/z^*)=\tfrac12\gamma_{12}\gamma_{21}$, so the minimised condition is exactly $\lambda_1\lambda_2>\gamma_{12}\gamma_{21}$. (This is the source's eq. (13) with no $\tfrac12$ in the gain definition.)

Numbers: $\gamma_{12}\gamma_{21}=4<6=\lambda_1\lambda_2$ ✓, $z^*=4$, so $\alpha_1=4\alpha_2$; the condition value is $\tfrac14(4\cdot1+16/4)+2=4<6$ ✓. Cross-check: $A=\begin{psmallmatrix}-2&1\\4&-3\end{psmallmatrix}$ has $\mathrm{tr}=-5<0$, $\det=2>0$, Hurwitz.

**3.** With $\gamma_{12}=0$ the condition from Problem 2 becomes $\lambda_1\lambda_2>\gamma_{21}^2/(4z)$, i.e.
$$z=\frac{\alpha_1}{\alpha_2}>\frac{\gamma_{21}^2}{4\lambda_1\lambda_2},$$
which is satisfiable for any finite $\gamma_{21}$ — no condition relating $\lambda_i$ to $\gamma_{21}$ survives. The **driving** block (block 1, the one with no return path) takes the heavy weight: making $\alpha_1$ large means its own decay $-\alpha_1\lambda_1\|v\|^2$ dominates the cross term $\alpha_2\gamma_{21}\|v\|\|w_2\|$, which is only $O(\alpha_2)$. This is why cascades are free and feedback is not.

**4.** Take $\lambda_1=\lambda_2=1$, $\gamma_{12}=\gamma_{21}=2$:
$$\dot x_1=-x_1+2x_2,\qquad \dot x_2=-x_2+2x_1.$$
Each block *is* contracting with inputs: $\dot x_1=-x_1+2u$ has $\partial_{x_1}=-1$ for **every** value of $u$ (the input is additive, so it does not touch the Jacobian), rate $\lambda_1=1$, in the Euclidean metric; likewise block 2. But $A=\begin{psmallmatrix}-1&2\\2&-1\end{psmallmatrix}$ has eigenvalues $1$ and $-3$. The origin is a saddle, so trajectories separate; contraction on any region containing the origin would force all trajectories to converge, so **no** metric $G$ certifies the interconnection.

Here $\gamma_{12}\gamma_{21}=4>1=\lambda_1\lambda_2$, so the small-gain condition fails — and it fails for a reason, not by slack: for this $2\times2$ family $\det A=\lambda_1\lambda_2-\gamma_{12}\gamma_{21}$ and $\mathrm{tr}\,A=-(\lambda_1+\lambda_2)<0$ always, so $A$ is Hurwitz **iff** $\lambda_1\lambda_2>\gamma_{12}\gamma_{21}$. The condition is exactly sharp in this class. Note the contrast with Problem 3: setting $\gamma_{12}=0$ in the same example gives $A=\begin{psmallmatrix}-1&0\\2&-1\end{psmallmatrix}$, eigenvalues $-1,-1$, stable for any $\gamma_{21}$. The *return path* is what breaks it.
