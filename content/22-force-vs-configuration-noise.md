---
tags: [stochastics, lie-groups, mechanics, noise-models, curvature]
---
# Force Noise vs Configuration Noise

**Prereq:** [[10-euler-poincare]] (the split $\dot g=g\xi$, $\dot\mu=\mathrm{ad}^*_\xi\mu+f$), [[19-ito-vs-stratonovich]] (the non-tensorial $\tfrac12\partial^2\phi\,(\sigma\sigma^\top)$ term, quadratic variation), [[20-generator-on-manifolds]], [[21-brownian-motion-lie-groups]]; [[04-unimodularity]] for $\sum_i\widetilde{\mathrm{ad}}_{e_i}e_i=0$; notation fixed in [[notation]].
**Goal:** decide, for a given noise model, whether the geometry of $G$ produces an extra drift — and know that the answer depends on exactly one thing, *which factor of $G\times\mathfrak g^*$ carries the quadratic variation*.

## The two models

Take a mechanical system on $G$ in body coordinates, state $(g,\mu)\in G\times\mathfrak g^*$, deterministic dynamics from [[10-euler-poincare]]:
$$\dot g=g\xi,\qquad \xi=\mathbb I^{-1}\mu,\qquad \dot\mu=\mathrm{ad}^*_\xi\mu+f .$$
There are two structurally different places to put noise, and they are **not** small perturbations of each other.

:::info[Definition — the two noise models]
**Case A (force noise).** Randomness enters only the dynamic equation, modelling a noisy actuator:
$$dg=g\xi\,dt,\qquad d\mu=\big(\mathrm{ad}^*_\xi\mu+f(g,\mu)\big)dt+\Sigma(g,\mu)\,dW,$$
with $W$ an $m$-dimensional Wiener process, $\Sigma:G\times\mathfrak g^*\to(\mathfrak g^*)^m$. This is the Langevin / stochastic-Hamiltonian form.

**Case B (configuration noise).** Randomness enters the reconstruction equation, so the configuration itself diffuses. In the kinematic (overdamped) limit the fibre is dropped and this is [[21-brownian-motion-lie-groups]]'s Brownian motion,
$$g^{-1}dg=\sum_{i=1}^n e_i\circ dW_i\quad\text{(unimodular }G\text{)},$$
$\{e_i\}$ an $\mathbb I$-orthonormal basis of $\mathfrak g$.
:::

## Case A: the noise never sees the geometry

:::tip[Proposition — structure of the drift under force noise]
For Case A:

1. $g$ has **zero quadratic variation**, $[g,g]_t\equiv0$; the reconstruction equation is *identical* in the Itô and Stratonovich senses.
2. The Itô–Stratonovich discrepancy is confined to the $\mu$-fibre and equals $\tfrac12(\partial_\mu\Sigma)\Sigma:=\tfrac12\sum_{a=1}^m(\partial_\mu\Sigma_a)\Sigma_a$. It is computed with the **flat** connection $\mathfrak g^*$ carries as a vector space in body coordinates, so **no curvature of $G$ enters**. If $\Sigma$ does not depend on $\mu$ (additive noise) it vanishes and the two conventions agree everywhere.
3. Under a configuration reparametrisation $g\mapsto\psi(g)$ lifted to the bundle, the reconstruction drift $g\xi$ transforms as a genuine vector field, with no extra term. No curvature-induced or "pinning" drift is generated.
:::

*Proof.* (1) $dg=g\xi\,dt$ contains no $dW$, so $t\mapsto g_t$ has bounded variation, $[g,g]_t\equiv0$, and the $\tfrac12\,d\sigma\,dW$ bridge term of [[19-ito-vs-stratonovich]] vanishes for the $g$-equation.

(2) Only $\mu$ carries $dW$, so the sole non-zero block of $\sigma\sigma^\top$ on $G\times\mathfrak g^*$ sits in the $\mu\mu$ indices. The conversion is then the Euclidean one on the vector space $\mathfrak g^*$: no Christoffel symbol of $G$ can be contracted against a $\mu\mu$ block.

(3) The correction of [[19-ito-vs-stratonovich]] is $\tfrac12\partial^2\phi\,(\sigma\sigma^\top)$, and the only non-zero block of $\sigma\sigma^\top$ is $\mu\mu$; so all that is needed is $\partial^2_{\mu\mu}\phi=0$ — **$\phi$ affine in the fibre coordinate**. That holds for the full lift, not just for maps fixing $\mu$: a configuration change $q\mapsto\bar q(q)$ lifts to $T^*Q$ as $\bar\mu_a=(\partial q^k/\partial\bar q^a)\mu_k$, which is *linear in $\mu$* however nonlinear it is in $q$. So $\partial^2_{\mu\mu}\phi=0$ identically, the correction vanishes in both the base and fibre components, and $g\xi$ transforms tensorially. $\square$

The content is that **force noise does not substantially change the drift field.** The reconstruction drift is untouched; the dynamic drift changes at most by a flat, chart-independent term that is absent for additive noise.

## Case B: the noise sees everything

:::tip[Proposition — structure of the drift under configuration noise]
For Case B:

1. $g$ has **non-zero quadratic variation**: in the left-invariant frame, $[\,g^{-1}dg,\,g^{-1}dg\,]_t=n\,I\,dt$.
2. The **intrinsic** Stratonovich drift is $\tfrac12\sum_i\widetilde{\mathrm{ad}}_{e_i}e_i$, which vanishes iff $G$ is unimodular ([[04-unimodularity]]); the intrinsic Itô drift in the body frame is then zero as well ([[21-brownian-motion-lie-groups]], from [[@leeGeometricInterpretationBrownian2025]] Thm 5 / Cor 1).
3. Written in an ambient embedding $\iota:G\hookrightarrow\mathbb R^{\bar n}$, the Itô drift acquires the **mean-curvature term** $\tfrac12H$ ([[@leeGeometricInterpretationBrownian2025]] Thm 7, eq. (65); Thm 8, eq. (71)). It is generated purely by the non-tensorial correction of [[19-ito-vs-stratonovich]], now non-zero because $\sigma\sigma^\top\neq0$ in the configuration directions.
:::

So in Case B "does noise change the drift?" is *representation-dependent but genuinely yes*: intrinsically the drift is unchanged (zero for unimodular $G$), while ambiently a drift $\tfrac12H$ appears. Be precise about what is chart-dependent: $H$ is a property of the *embedding*, a real geometric object; what is representational is its **presence in the SDE**. It is normal to $G$ and invisible to intrinsic functions ([[@leeGeometricInterpretationBrownian2025]] Remark 5) — it is the normal acceleration that keeps the sample path on the manifold.

## The mechanism, in one sentence

:::tip[The dichotomy]
The extra drift produced by a change of representation is $\tfrac12\partial^2\phi\,(\sigma\sigma^\top)$ — the second derivative of the map contracted against **the quadratic variation of the noise in the transformed directions**. Force noise puts that variation in the *flat* momentum fibre; configuration noise puts it in the *curved* base. That is the whole dichotomy.
:::

| | **Case A — force noise** | **Case B — configuration noise** |
|---|---|---|
| QV of configuration $g$ | $0$ | $\neq0$ |
| Itô $=$ Stratonovich for $g$? | yes | no |
| Curvature / pinning drift? | none, in *any* representation | $\tfrac12H$ in the ambient Itô form |
| Intrinsic Stratonovich drift | mechanical drift only | $+\tfrac12\sum_i\widetilde{\mathrm{ad}}_{e_i}e_i$ ($=0$ if unimodular) |
| Effect of a configuration diffeo | drift is tensorial — no extra term | Itô drift shifts by $\tfrac12\partial^2\iota\,(\sigma\sigma^\top)$ |

## Worked example: the rigid body on $SO(3)$, both ways

Conventions from [[notation]]: $\hat\Omega=R^\top\dot R$, $\langle\eta,\zeta\rangle_{\mathfrak{so}(3)}=\tfrac12\mathrm{tr}(\eta^\top\zeta)$, orthonormal basis $\hat e_1,\hat e_2,\hat e_3$, and the identity $\sum_{i=1}^3\hat e_i^{\,2}=-2I$.

**Case A — random torque.** $\tau\,dt\to\tau\,dt+\Sigma\,dW$ with $W$ three-dimensional:
$$dR=R\hat\Omega\,dt,\qquad d\Omega=\mathbb J^{-1}\big(\mathbb J\Omega\times\Omega+\tau\big)dt+\mathbb J^{-1}\Sigma\,dW .$$
The orthogonality constraint is preserved **with no correction at all**, because $dR$ carries no $dW$:
$$d(R^\top R)=(dR)^\top R+R^\top(dR)+\underbrace{(dR)^\top(dR)}_{=0}=\big(\hat\Omega^\top+\hat\Omega\big)R^\top R\,dt=0,$$
using $\hat\Omega^\top=-\hat\Omega$. The ambient matrix form of the $R$-equation has drift $R\hat\Omega$ and **no** mean-curvature term. The only Itô–Stratonovich gap is the flat fibre term $\tfrac12\sum_a(\partial_\Omega\sigma_a)\sigma_a$ with $\sigma=\mathbb J^{-1}\Sigma$; for constant $\Sigma$ the equation is simultaneously Itô and Stratonovich.

**Case B — configuration Brownian motion.** From [[21-brownian-motion-lie-groups]], $SO(3)$ unimodular gives the drift-free Stratonovich form $dR=\sum_iR\hat e_i\circ dW_i$, whose ambient Itô form ([[@leeGeometricInterpretationBrownian2025]] §V-F, eqs. (104)–(105)) is
$$dR=-R\,dt+\sum_{i=1}^3R\hat e_i\,dW_i,\qquad \tfrac12H=-R,\quad H=-2R .$$
Now the constraint **needs** that drift. Itô:
$$d(R^\top R)=\underbrace{(-R^\top R-R^\top R)}_{\text{drift}}dt+\underbrace{\textstyle\sum_i\hat e_i^\top R^\top R\hat e_i}_{(dR)^\top(dR)}dt=\big(-2I-\textstyle\sum_i\hat e_i^{\,2}\big)dt=(-2I+2I)dt=0,$$
the martingale part cancelling by $\hat e_i^\top+\hat e_i=0$. **The side-by-side is the deliverable:** in Case A the two positive terms are each zero; in Case B they are $\mp2I$ and cancel only because the curvature drift is present.

## Which one the project should target

:::info[Standing question — answered for the tube results]
The tube bounds of Phase 5 should target **Case A**. A noisy actuator or torque model is force noise: the physical randomness is in the applied wrench, not in the configuration, which continues to obey the deterministic kinematic identity $\dot g=g\xi$. By the Case A proposition the noise itself then contributes **no curvature correction** — this is the potential result "coordinate invariance as noise enters on the flat subsystem".

Curvature does not disappear from the problem; it is relocated. It enters only later and only through the **distance function**, when $\mathcal L$ is applied to $\Phi_\lambda(d(X_t,\bar x_t))$ and $\mathrm{Hess}\,d$ must be bounded ([[08-hessian-comparison]], [[20-generator-on-manifolds]]). Separating the two entry points is exactly what makes the intrinsic bound cleaner than [[@daniObserverDesignStochastic2015]]'s, which mixes them.
:::

:::warning[Open question — the price of Case A is degeneracy]
With pure force noise the diffusion on $G\times\mathfrak g^*$ is **degenerate**: $\sigma\sigma^\top$ has rank $\le m$ in the fibre and rank $0$ on the base. So in $\mathcal Af=\tilde X[f]+\tfrac12\sum_i\mathrm{Hess}_f(\sigma_i,\sigma_i)$ the second-order term sees a configuration-distance $f$ only through the drift, via the coupling $\dot g=g\xi$ — a hypoelliptic problem. Whether the AMGF argument survives that, and at what cost in the constant, is not settled by anything in `refs/`.

Separately, the Case A proposition assumes the fibre is carried with the **flat** connection $\mathfrak g^*$ has as a vector space. Multiplicative noise entering through a non-flat fibre metric would need the vertical connection made explicit; no source covers it (Problem 4b).
:::

## Problems

1. **Recall.** State the two noise models and the one-sentence mechanism that separates them. Then answer without computing: for Case A, is the Itô form of the $g$-equation different from the Stratonovich form, and why?

2. **Compute.** On $SO(3)$ in Case A, take the body torque noise $\Sigma(\Pi)\,dW=\varepsilon\,\Pi\times dW$ (so $\sigma_a(\Pi)=\varepsilon\,\Pi\times e_a$), working in body momentum $\Pi=\mathbb J\Omega$. Compute the Itô–Stratonovich fibre correction $\tfrac12\sum_a(\partial_\Pi\sigma_a)\sigma_a$. Then say why the $-2$ you will meet is *not* the same $-2$ as in $H=-2R$.

3. **Prove.** Show that if $\Sigma$ is independent of $\mu$, then in Case A the Itô and Stratonovich SDEs coincide on the *whole* state space $G\times\mathfrak g^*$ — not just in the fibre — even when $\Sigma$ depends on $g$.

4. **Break it.** A hybrid: keep the Euler–Poincaré equation but add configuration noise, $g^{-1}dg=\xi\,dt+\varepsilon\sum_ie_i\circ dW_i'$ with $W'$ independent of $W$.
   (a) Which of the three Case A conclusions survive, and which fail? Give the ambient Itô drift of the $g$-equation.
   (b) Now let $\Sigma=\Sigma(g)$ and drive *both* equations with the **same** Wiener process. Show a new correction term appears that Case A did not have, and identify which directions its quadratic variation lives in.

---

## Solutions

**1.** Case A: $dg=g\xi\,dt$, $d\mu=(\mathrm{ad}^*_\xi\mu+f)dt+\Sigma\,dW$. Case B: noise in $g^{-1}dg$, e.g. $\sum_ie_i\circ dW_i$. Mechanism: a change of representation adds $\tfrac12\partial^2\phi\,(\sigma\sigma^\top)$, so the extra drift is the second derivative of the map contracted against the quadratic variation *in the directions being transformed*; A puts that variation in the flat fibre, B in the curved base. For Case A the two forms of the $g$-equation are identical: the conversion term is $\tfrac12 d\sigma\,dW$ and the $g$-equation has $\sigma\equiv0$, so $[g,g]_t=0$ and there is nothing to correct.

**2.** Write $\sigma_a(\Pi)=\varepsilon\,\Pi\times e_a=-\varepsilon\,e_a\times\Pi=-\varepsilon\hat e_a\Pi$, which is **linear** in $\Pi$, so $\partial_\Pi\sigma_a=-\varepsilon\hat e_a$. Hence
$$\tfrac12\sum_{a=1}^3(\partial_\Pi\sigma_a)\sigma_a=\tfrac12\sum_a(-\varepsilon\hat e_a)(-\varepsilon\hat e_a\Pi)=\tfrac{\varepsilon^2}{2}\Big(\sum_a\hat e_a^{\,2}\Big)\Pi=\tfrac{\varepsilon^2}{2}(-2I)\Pi=-\varepsilon^2\Pi .$$
So the Stratonovich equation with this $\Sigma$ equals the Itô equation with an extra linear damping $-\varepsilon^2\Pi$ of the body momentum. The two $-2$'s look alike and are not the same object: here $\sum_a\hat e_a^2=-2I$ arises because *we chose* a noise shape built from the cross product, so its $\Pi$-derivative is $\hat e_a$; the entire computation happens inside the vector space $\mathfrak g^*\cong\mathbb R^3$ with the flat connection, and no metric on $SO(3)$, no $\nabla$, and no curvature is used. In $H=-2R$ the same structure constants appear as the trace of the second fundamental form of the *embedding*. A different multiplicative $\Sigma$ gives a different fibre correction; $H$ does not change.

**3.** If $\Sigma=\Sigma(g)$ only, the conversion term for the $\mu$-equation is $\tfrac12\sum_a d\Sigma_a\,dW_a$ with $d\Sigma_a=(\partial_g\Sigma_a)\,dg$. But $dg=g\xi\,dt$ has no martingale part, so $d\Sigma_a\,dW_a=(\partial_g\Sigma_a)(g\xi)\,dt\,dW_a=0$ (a $dt\,dW$ product). The $g$-equation needs no correction by conclusion (1). Both components are correction-free, so the two SDEs coincide as written. The point: additivity *in the fibre variable* is what matters, not constancy — $g$-dependence is free because $g$ is of bounded variation.

**4(a).** Conclusion (1) fails at once: $[g,g]_t\neq0$, with $\varepsilon^2n\,dt$ in the frame, so Itô $\neq$ Stratonovich for the $g$-equation. Conclusion (3) fails with it: in the ambient embedding the Itô $g$-drift becomes $g\xi+\tfrac{\varepsilon^2}{2}H$ (plus $\tfrac{\varepsilon^2}{2}\sum_i\widetilde{\mathrm{ad}}_{e_i}e_i$ intrinsically, which is $0$ on unimodular $G$) — for $SO(3)$, $dR=(R\hat\Omega-\varepsilon^2R)dt+\varepsilon\sum_iR\hat e_i\,dW_i$. Conclusion (2) survives verbatim, since $W$ and $W'$ are independent: the $\mu\mu$ block of $\sigma\sigma^\top$ is unchanged and the $g\mu$ blocks are zero. Note the failure is $O(\varepsilon^2)$ — Case A is the $\varepsilon\to0$ limit, and the curvature drift degrades gracefully rather than switching on discontinuously.

**(b)** With one shared $W$ and $\Sigma=\Sigma(g)$, the $g\mu$ cross-block of $\sigma\sigma^\top$ is no longer zero, so the Itô–Stratonovich conversion for the $\mu$-equation acquires $\tfrac12\sum_a(\partial_g\Sigma_a)\big[\varepsilon\,g e_a\big]$ — a derivative of the noise coefficient along a **configuration** direction, contracted against configuration quadratic variation. This term is a genuine counterexample to the flat-fibre claim: it is a derivative in a curved direction, so writing it invariantly requires a connection on the bundle $G\times\mathfrak g^*\to G$, not just the flat structure of $\mathfrak g^*$. It is exactly the case the sources do not cover, and it is why the Case A proposition is stated for independent (or fibre-only) noise. Solution 3 is the reason it was invisible before: there the $dt\,dW$ product killed it; here $dg$ has a martingale part and it does not.
