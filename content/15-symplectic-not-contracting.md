---
tags: [contraction, symplectic, mechanics, obstruction, control]
---
# Symplectic $\Rightarrow$ Never Contracting

**Prereq:** [[09-hamiltonian-on-cotangent]] ($\mathcal L_{X_H}\omega_0=0$, Liouville volume $\Lambda$, $\mathrm{div}_\Lambda X_H=0$), [[14-contraction-on-manifolds]] (the definition of a contracting system); notation fixed in [[notation]].
**Goal:** prove that a symplectic vector field admits **no** contraction certificate — in any metric, with any rate, on any region with compact closure — and read off the design moral: breaking $\omega_0$ is mandatory, not incidental.

Recall from [[14-contraction-on-manifolds]] the condition being used, in the two equivalent forms of [[@simpson-porcoContractionTheoryRiemannian2014]] Def. 2.1: $(\mathcal U,X,G,\lambda)$ is **contracting** iff for all $x\in\mathcal U$, $v\in T_xM$,

$$\big\langle\overset{G}{\nabla}_{v}X,\,v\big\rangle_{G}\le-\lambda\|v\|^2_{G}
\qquad\Longleftrightarrow\qquad
\mathcal L_XG\preceq-2\lambda G ,$$

the equivalence being the identity $(\mathcal L_XG)(v,v)=2\,G(\overset{G}{\nabla}_vX,v)$. Nothing else from that lesson is needed.

## The divergence bound

:::tip[Lemma — divergence bound]
If $(\mathcal U,X,G,\lambda)$ is contracting on a manifold $M$ with $\dim M=N$, then
$$\mathrm{div}_GX\le-N\lambda\qquad\text{on }\mathcal U,$$
where $\mathrm{div}_G$ is the divergence with respect to the Riemannian volume $\mu_G$.
:::

*Proof.* Let $L:=\overset{G}{\nabla}X$ be the $(1,1)$-tensor $v\mapsto\overset{G}{\nabla}_vX$ and $S:=\mathrm{sym}(L)=\tfrac12(L+L^{*_G})$ its $G$-symmetric part. Since $\langle Lv,v\rangle_G=\langle Sv,v\rangle_G$, the contraction condition says exactly $S\preceq-\lambda\,\mathrm{id}$. Trace in a $G$-orthonormal frame: $\mathrm{tr}(S)\le-N\lambda$. Finally $\mathrm{tr}(L^{*_G})=\mathrm{tr}(L)$, so $\mathrm{tr}(S)=\mathrm{tr}(L)=\mathrm{div}_GX$. $\square$

Read it as a **rate ceiling**, not only as an obstruction: no system can contract faster than its volume shrinks, per dimension. That is already the whole content of the next result.

## The obstruction

:::tip[Proposition — no symplectic vector field is contracting]
Let $(M,\omega)$ be symplectic, $\dim M=N=2n\ge2$, and let $X$ be **symplectic**: $\mathcal L_X\omega=0$. Then there is no Riemannian metric $G$, no $\lambda>0$ and no non-empty $\mathcal U\subseteq M$ with $\overline{\mathcal U}$ compact, $\mathcal U$ forward $X$-invariant and $X$ forward complete on $\mathcal U$, such that $(\mathcal U,X,G,\lambda)$ is contracting.
:::

*Proof.* $\Lambda:=\omega^{\wedge n}/n!$ is a volume form, so $M$ is orientable; orient it by $\Lambda$ and write the Riemannian volume as
$$\mu_G=f\,\Lambda,\qquad f\in C^\infty(M),\ f>0 .$$
Because $\mathcal L_X$ is a derivation over $\wedge$, $\mathcal L_X\omega=0$ gives $\mathcal L_X\Lambda=0$. Hence
$$(\mathrm{div}_GX)\,f\Lambda=\mathcal L_X(f\Lambda)=(Xf)\,\Lambda+f\,\mathcal L_X\Lambda=(Xf)\,\Lambda
\quad\Longrightarrow\quad
\mathrm{div}_GX=\frac{Xf}{f}=X(\ln f).$$
Pick $x\in\mathcal U$. Forward invariance and forward completeness keep $\Phi_t(x)\in\mathcal U$ for all $t\ge0$, so by the Lemma (with $N=2n$)
$$\frac{d}{dt}\ln f(\Phi_t(x))=\big(X\ln f\big)(\Phi_t(x))=\mathrm{div}_GX(\Phi_t(x))\le-2n\lambda,$$
whence $\ln f(\Phi_t(x))\le\ln f(x)-2n\lambda t\to-\infty$. But $f$ is continuous and positive on the compact set $\overline{\mathcal U}$, so $f\ge f_{\min}>0$ there and $\ln f$ is bounded below on $\mathcal U$. Contradiction. $\square$

Two remarks on the mechanics of the proof. First, $f$ is the *only* place $G$ enters: the argument never touches $\overset{G}{\nabla}$ after the Lemma, and in particular never a Christoffel symbol. Second, this is exactly the device that settles the open question left at the end of [[09-hamiltonian-on-cotangent]] — $\mathrm{div}_\Lambda$ and $\mathrm{div}_G$ *are* different functionals, and their difference is precisely $X(\ln f)$; the obstruction survives because that difference is a total derivative along the flow and therefore cannot be negative on average forever on a compact closure.

## The spectral form — the version to remember

:::tip[Corollary — Hamiltonian spectra are symmetric about $0$]
Let $X$ be symplectic with a fixed point $\bar x\in\mathcal U$ and put $A:=DX(\bar x)$, $P:=G(\bar x)\succ0$. If $(\mathcal U,X,G,\lambda)$ is contracting then $A^\top P+PA\preceq-2\lambda P$, hence $A$ is Hurwitz. But $\mathrm{spec}(A)$ is invariant under $z\mapsto-z$ (and, $A$ being real, under $z\mapsto\bar z$). For $N\ge2$ the two are incompatible.
:::

*Proof.* At a zero of $X$ the linearisation is connection-independent — two connections differ by a tensor applied to $X(\bar x)=0$ — so $\overset{G}{\nabla}_vX=Av$ at $\bar x$. The contraction condition reads $v^\top PAv\le-\lambda v^\top Pv$; symmetrising gives $\tfrac12v^\top(A^\top P+PA)v\le-\lambda v^\top Pv$, i.e. $A^\top P+PA\preceq-2\lambda P\prec0$, which is the Lyapunov equation certifying $A$ Hurwitz.

For the symmetry, work on the vector space $T_{\bar x}M$ with the constant non-degenerate skew form $J:=\omega(\bar x)$. Since $\bar x$ is fixed, $D\Phi_t(\bar x)=e^{At}$ maps $T_{\bar x}M$ to itself, and $\Phi_t^*\omega=\omega$ makes it symplectic: $(e^{At})^\top Je^{At}=J$ for all $t$. Differentiate at $t=0$: $A^\top J+JA=0$, i.e. $A$ is a **Hamiltonian matrix**. Then $A^\top=-JAJ^{-1}$, so $A^\top$ is similar to $-A$, and $\mathrm{spec}(A)=\mathrm{spec}(A^\top)=\mathrm{spec}(-A)=-\mathrm{spec}(A)$. Any eigenvalue with $\mathrm{Re}\,z<0$ therefore comes with $-z$ in the right half-plane. $\square$

This is the checkable-by-inspection version: **if the linearisation's spectrum is symmetric about the imaginary axis' reflection through the origin, stop — no metric will help.** It also localises the failure, which the volume argument does not: contraction fails already at the linear level at a single point.

## Worked example: the undamped oscillator on $T^*\mathbb R$

$H(q,p)=\tfrac{1}{2m}p^2+\tfrac12kq^2$, so by [[09-hamiltonian-on-cotangent]] $\dot q=p/m$, $\dot p=-kq$, and

$$A=\begin{pmatrix}0&1/m\\-k&0\end{pmatrix},\qquad \chi_A(z)=z^2+\tfrac km,\qquad \mathrm{spec}(A)=\{\pm i\omega\},\ \ \omega=\sqrt{k/m}.$$

Symmetric under $z\mapsto-z$, as the Corollary demands; $\mathrm{tr}\,A=0$, so $\mathrm{div}=0$, as the Lemma demands. Not Hurwitz, therefore **not contracting in any Riemannian metric $G$ whatsoever**, on any neighbourhood of the origin. No amount of metric design — cross terms, conformal factors, $g$-natural lifts — changes a spectrum.

Now add viscous damping, the force $\beta=-d\,\dot q$ of [[09-hamiltonian-on-cotangent]] problem 4:

$$A_d=\begin{pmatrix}0&1/m\\-k&-d/m\end{pmatrix},\qquad \chi_{A_d}(z)=z^2+\tfrac dm z+\tfrac km,\qquad z_\pm=\frac{-d/m\pm\sqrt{(d/m)^2-4k/m}}{2}.$$

For $d>0$ both roots have $\mathrm{Re}<0$: Hurwitz, and the $z\mapsto-z$ symmetry is gone. In the *same stroke*, $\mathcal L_{\mathrm{ver}(\beta)}\omega_0=-(d/m)\,\omega_0\ne0$ ([[09-hamiltonian-on-cotangent]] problem 4(b)) and $\mathrm{div}_\Lambda(X_H+\mathrm{ver}(\beta))=-d/m<0$. The spectral shift and the destruction of $\omega_0$ are not two facts, they are one fact seen twice. And the Lemma prices it: $\mathrm{div}_G$ at the fixed point is $\mathrm{tr}\,A_d=-d/m$, so **any** certificate must have $\lambda\le d/(2m)$.

## The moral

:::info[Design consequence]
Contraction is **not** a structure-preserving property. Certifying it forces $\mathcal L_{X_{\mathrm{cl}}}\omega_0\ne0$ for the closed-loop field, and strict volume dissipation at rate at least $N\lambda$. So the design question is never *whether* to break the symplectic structure but **how** — and, equally, **which metric $G$** can certify what is left.
:::

[[09-hamiltonian-on-cotangent]] showed that any dissipative or velocity-dependent feedback breaks $\omega_0$; that could have been read as a defect of clumsy design. This lesson closes the loop: it is compulsory. The remaining freedom is entirely in the *how*, and lesson 16 shows the obvious choices of $G$ still fail.

One alternative, stated and not developed: if preserving $\omega_0$ genuinely matters — variational integrators, energy methods, long-horizon structure-preserving simulation — then contraction is simply the wrong target, and one should use energy–momentum (Lyapunov/Casimir) methods, or ask for contraction on a reduced or quotient space where the conserved quantities have been divided out.

:::warning[Open question]
$T^*Q$ is **never** compact: the fibres are vector spaces. So "$\overline{\mathcal U}$ compact" is not a hypothesis one gets for free here — it is a standing restriction to bounded-momentum regions, and problem 4 shows it is doing real work rather than being a technical convenience. What is not clear is the sharp replacement. Boundedness of $f$ below by a positive constant on $\mathcal U$ suffices and is strictly weaker, but it is a statement about $G$ relative to $\Lambda$, not about the system; whether it can be phrased as a completeness or curvature condition on $(M,G)$ is open here.
:::

## Problems

1. **Recall.** State the divergence bound and the proposition. Then say precisely which step of the proof consumes compactness of $\overline{\mathcal U}$, and which consumes forward invariance of $\mathcal U$ — they are different steps.

2. **Compute.** On $T^*\mathbb R^2$ with $J=\begin{pmatrix}0&I_2\\-I_2&0\end{pmatrix}$, take $H=\tfrac12|p|^2+\tfrac12q^\top Kq$ with $K=\mathrm{diag}(1,-4)$, giving $A=\begin{pmatrix}0&I_2\\-K&0\end{pmatrix}$. (a) Verify $A^\top J+JA=0$. (b) Compute $\mathrm{spec}(A)$ and check both symmetries. (c) Verify $\mathrm{tr}\,A=0$. (d) Now damp: replace the $(2,2)$ block by $-\tfrac dm I_2$ with $m=1$ and compute $\mathrm{div}$ of the new field; what upper bound on $\lambda$ does the Lemma impose?

3. **Prove.** (a) Show directly from $A^\top J+JA=0$ that $\mathrm{tr}\,A=0$, without computing the spectrum. (b) Deduce that a symplectic field with a fixed point $\bar x$ is not contracting on any $\mathcal U\ni\bar x$, in any metric — using only the Lemma, not the Hurwitz argument. (c) More generally, show that for *any* $X$ with a fixed point $\bar x\in\mathcal U$, a contraction certificate forces $\lambda\le-\tfrac1N\mathrm{tr}\,DX(\bar x)$.

4. **Break it.** Take $M=T^*\mathbb R=\mathbb R^2$, $\omega_0=dq\wedge dp$, and $X=\partial_q$. (a) Show $X$ is Hamiltonian (find $H$), hence symplectic. (b) Find an explicit Riemannian metric $G$ and a $\lambda>0$ for which $(\mathbb R^2,X,G,\lambda)$ satisfies the pointwise contraction inequality. *Hint: use the $\mathcal L_XG\preceq-2\lambda G$ form and try $G=e^{2\varphi(q)}(dq^{\otimes2}+dp^{\otimes2})$.* (c) Identify exactly which hypothesis of the proposition fails, by computing $f$ and its infimum. (d) Why does the spectral corollary also fail to apply?

---

## Solutions

**1.** Statements as above. **Forward invariance (plus forward completeness)** is used to guarantee $\Phi_t(x)\in\mathcal U$ for all $t\ge0$, which is what licenses applying the Lemma's pointwise bound along the whole trajectory and integrating to $\ln f(\Phi_t x)\le\ln f(x)-2n\lambda t$. **Compactness of $\overline{\mathcal U}$** is used only at the very last step, to conclude $\inf_{\mathcal U}f>0$, hence $\ln f$ bounded below. Non-emptiness is used to pick $x$ at all.

**2(a).** $JA=\begin{pmatrix}0&I\\-I&0\end{pmatrix}\begin{pmatrix}0&I\\-K&0\end{pmatrix}=\begin{pmatrix}-K&0\\0&-I\end{pmatrix}$, which is **symmetric** because $K=K^\top$. Now $A^\top J=-A^\top J^\top=-(JA)^\top=-JA$, the first equality by $J^\top=-J$ and the last by the symmetry just checked. Hence $A^\top J+JA=0$. (In general: $A$ is Hamiltonian $\iff$ $JA$ is symmetric — the two statements are the same equation rearranged.)

**2(b).** $\det(A-zI)$ decouples into the two scalar blocks: $z^2+K_{ii}=0$. So $z^2=-1$ and $z^2=4$, giving $\mathrm{spec}(A)=\{+i,-i,+2,-2\}$. Closed under $z\mapsto-z$ and under conjugation — the full quadruple $\{z,-z,\bar z,-\bar z\}$. Two eigenvalues sit strictly in the right half-plane, so $A$ is not Hurwitz; the negative eigenvalue $-2$ is *not* evidence of contraction, it is the mandatory partner of $+2$.

**2(c).** $\mathrm{tr}\,A=\mathrm{tr}(0)+\mathrm{tr}(0)=0$; the diagonal blocks of $A$ are zero.

**2(d).** $A_d=\begin{pmatrix}0&I\\-K&-dI\end{pmatrix}$, so $\mathrm{tr}\,A_d=-2d$. At the fixed point the origin, $\mathrm{div}_GX=\mathrm{tr}\,A_d=-2d$ for every $G$ (solution 3(c)). With $N=4$, the Lemma gives $-2d\le-4\lambda$, i.e. $\lambda\le d/2$. Note this is only necessary: $K$ indefinite means the damped system is still not contracting near the origin, since $K_{22}=-4$ leaves an unstable root.

**3(a).** From $A^\top J+JA=0$: $A^\top=-JAJ^{-1}$. Trace is similarity-invariant and $\mathrm{tr}\,A^\top=\mathrm{tr}\,A$, so $\mathrm{tr}\,A=-\mathrm{tr}(JAJ^{-1})=-\mathrm{tr}\,A$, hence $2\,\mathrm{tr}\,A=0$.

**3(b).** At $\bar x$, $\mathrm{div}_GX(\bar x)=\mathrm{tr}(\overset{G}{\nabla}X)(\bar x)=\mathrm{tr}\,DX(\bar x)=\mathrm{tr}\,A=0$ by (a), the middle equality because $\overset{G}{\nabla}_vX=DX(\bar x)v$ at a zero of $X$. The Lemma demands $\mathrm{div}_GX(\bar x)\le-N\lambda<0$. Contradiction, at a single point. This version needs neither compactness nor forward invariance — it is a purely pointwise obstruction, available whenever a fixed point exists.

**3(c).** Same identity: at a fixed point $\mathrm{div}_GX(\bar x)=\mathrm{tr}\,DX(\bar x)$ independently of $G$ (the metric-dependent correction is $X(\ln f)$, which vanishes where $X=0$). The Lemma then reads $\mathrm{tr}\,DX(\bar x)\le-N\lambda$. So the achievable contraction rate is capped by the *average* linear decay rate, and no clever metric can beat it — a metric can redistribute decay between directions but not create any.

**4(a).** $\iota_X\omega_0=\iota_{\partial_q}(dq\wedge dp)=dp$, so $X=X_H$ with $H(q,p)=p$. Hamiltonian $\Rightarrow$ symplectic, by [[09-hamiltonian-on-cotangent]].

**4(b).** With $G=e^{2\varphi(q)}\delta$ and $X=\partial_q$, the Lie derivative acts on the coefficient only: $\mathcal L_XG=\partial_q\!\big(e^{2\varphi}\big)\,\delta=2\varphi'(q)\,G$. Choosing $\varphi(q)=-\lambda q$ gives $\mathcal L_XG=-2\lambda G$ — the contraction condition, with **equality**, on all of $\mathbb R^2$, for any $\lambda>0$. So
$$G=e^{-2\lambda q}\big(dq\otimes dq+dp\otimes dp\big)$$
is a genuine contraction metric for a genuinely symplectic field. The two trajectories through $(q_0,p_0)$ and $(q_0,p_1)$ stay a coordinate distance $|p_1-p_0|$ apart forever, but their $G$-distance $e^{-\lambda q}|p_1-p_0|$ decays at rate exactly $\lambda$.

**4(c).** $\mu_G=\sqrt{\det G}\,dq\wedge dp=e^{-2\lambda q}\Lambda$, so $f=e^{-2\lambda q}$ and $\mathrm{div}_GX=X(\ln f)=\partial_q(-2\lambda q)=-2\lambda=-N\lambda$: the Lemma is satisfied, with equality. Nothing pointwise is violated. What fails is $\inf_{\mathcal U}f>0$: here $\inf f=0$, because $\mathcal U=\mathbb R^2$ has non-compact closure in the $q$ direction. **The obstruction is global, not pointwise** — the proposition is a statement that a positive function cannot decrease at a uniform rate forever on a set where it is bounded below, and nothing more.

**4(d).** $X=\partial_q$ has no zeros, so there is no $\bar x$ at which to linearise. Both routes to the obstruction need a hypothesis this example denies: a fixed point (spectral) or compact closure (volume). On $T^*Q$ a bounded-momentum region supplies the second and an equilibrium of the closed loop supplies the first, which is why the proposition bites there and not here.
