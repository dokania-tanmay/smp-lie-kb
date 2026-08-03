---
tags: [riemannian, curvature, conventions]
---
# Riemann Curvature Tensor and Sectional Curvature

**Prereq:** [[riemannian-geometry]] (connections, parallel transport, normal coordinates), [[notation]]
**Goal:** state $R$ and $\mathrm{Sec}$ in the project's convention, prove $R$ is a tensor, and know the four symmetries well enough to catch a sign slip downstream.

Bookkeeping lesson. Every curvature formula in Phases 1–5 of [[00-study-plan]] is convention-sensitive, so the sign is fixed here once and never renegotiated. Throughout, $\nabla$ is Levi-Civita for a Riemannian metric $\langle\cdot,\cdot\rangle$ — **torsion-free** and **metric-compatible**. Both hypotheses are used, and each buys exactly one symmetry.

## Definitions

:::info[Definition]
The **Riemann curvature tensor** of $\nabla$ is, for $X,Y,Z\in\mathfrak X(M)$,
$$R(X,Y)Z \;=\; \nabla_X\nabla_Y Z-\nabla_Y\nabla_X Z-\nabla_{[X,Y]}Z .$$
This is the sign convention of [[notation]]. Its $(0,4)$ form is $\mathrm{Rm}(X,Y,Z,W)=\langle R(X,Y)Z,\,W\rangle$.
:::

The first two terms measure the failure of second covariant derivatives to commute. The third subtracts off the failure of the *fields* to commute — without it, the object measures the fields as much as the geometry, which is exactly the "break it" problem below.

:::info[Definition]
For linearly independent $u,v\in T_pM$, the **sectional curvature** is
$$\mathrm{Sec}(u,v) \;=\; \frac{\langle R(u,v)v,\,u\rangle}{\|u\|^2\|v\|^2-\langle u,v\rangle^2}.$$
The denominator is $\|u\wedge v\|^2$, the squared area of the parallelogram they span.
:::

Both are **intrinsic** in the sense of `content/CLAUDE.md`: they are computed from Christoffel symbols in a chart, but their values are chart-independent. That is the whole point — they are the legitimate replacement for $\sup|\partial^2 g_{ij}|$.

## Theorems

:::tip[Proposition — tensoriality]
$R$ is $C^\infty(M)$-linear in all three arguments:
$$R(fX,Y)Z=R(X,fY)Z=R(X,Y)(fZ)=f\,R(X,Y)Z,\qquad f\in C^\infty(M).$$
Hence $R(X,Y)Z|_p$ depends only on $X_p,Y_p,Z_p$, and $R$ is a $(1,3)$-tensor field.
:::

This is the surprise: $R$ is built from three derivative operators, yet is pointwise. Compare $\nabla_XY$, which is $C^\infty$-linear in $X$ only (see [[riemannian-geometry]] § Connections) — it is *not* a tensor in $Y$. Proof of the first identity is the worked example below; the $Z$ slot is done in the same style, and the $Y$ slot follows from the $X$ slot plus antisymmetry (S1).

:::tip[Theorem — the four symmetries]
For the Levi-Civita connection, with $\mathrm{Rm}(X,Y,Z,W)=\langle R(X,Y)Z,W\rangle$:

- **(S1) first-pair antisymmetry** $\ \mathrm{Rm}(X,Y,Z,W)=-\mathrm{Rm}(Y,X,Z,W)$ — immediate from the definition (swapping $X,Y$ negates each of the three terms, using $[Y,X]=-[X,Y]$). Needs neither hypothesis.
- **(S2) last-pair antisymmetry** $\ \mathrm{Rm}(X,Y,Z,W)=-\mathrm{Rm}(X,Y,W,Z)$ — equivalently $\langle R(X,Y)Z,Z\rangle=0$. Needs **metric compatibility**.
- **(S3) first Bianchi identity** $\ R(X,Y)Z+R(Y,Z)X+R(Z,X)Y=0$. Needs **torsion-freeness**.
- **(S4) pair symmetry** $\ \mathrm{Rm}(X,Y,Z,W)=\mathrm{Rm}(Z,W,X,Y)$.

(S4) is a purely algebraic consequence of (S1)–(S3): it holds for any $4$-linear form satisfying them, so it carries no independent geometric content and is not proved here.
:::

Proof of (S2), the one worth doing. Metric compatibility gives $X\langle Z,Z\rangle=2\langle\nabla_XZ,Z\rangle$. Then
$$\langle\nabla_X\nabla_YZ,Z\rangle=X\langle\nabla_YZ,Z\rangle-\langle\nabla_YZ,\nabla_XZ\rangle=\tfrac12XY\langle Z,Z\rangle-\langle\nabla_YZ,\nabla_XZ\rangle .$$
Subtracting the $X\leftrightarrow Y$ version kills the symmetric middle term and leaves $\tfrac12(XY-YX)\langle Z,Z\rangle=\tfrac12[X,Y]\langle Z,Z\rangle$, which is exactly $\langle\nabla_{[X,Y]}Z,Z\rangle$. So $\langle R(X,Y)Z,Z\rangle=0$; polarizing in $Z$ gives (S2). $\square$

:::tip[Proposition — $\mathrm{Sec}$ determines $R$]
$\mathrm{Sec}(u,v)$ depends only on the $2$-plane $\sigma=\mathrm{span}(u,v)$, not the basis; write $\mathrm{Sec}(\sigma)$. Conversely, if two $4$-linear forms satisfy (S1)–(S4) and give the same $\mathrm{Sec}(\sigma)$ for every plane $\sigma\subset T_pM$, they are equal. So the sectional curvatures carry all of $R$.
:::

Counting confirms it: (S1)–(S4) cut the $n^4$ components of $\mathrm{Rm}$ down to $n^2(n^2-1)/12$ independent ones. For $n=1$ that is $0$ (curves are flat), $n=2$ gives $1$ (one number, the Gauss curvature), $n=3$ gives $6$, and $n=6$ — the dimension of $SE(3)$ — gives $105$.

:::tip[Proposition — curvature is infinitesimal holonomy]
For a smooth two-parameter map $\Gamma(s,t)$ and a vector field $V$ along it,
$$\tfrac{D}{\partial s}\tfrac{D}{\partial t}V-\tfrac{D}{\partial t}\tfrac{D}{\partial s}V \;=\; R(\partial_s\Gamma,\partial_t\Gamma)V .$$
Consequently, parallel transport around the coordinate parallelogram with sides $sX,tY$ acts on $T_pM$ as $\mathrm{id}-st\,R(X,Y)+O((s+t)^3)$.
:::

This is the formal version of the remark in [[riemannian-geometry]] § Parallel transport: *transporting an orthonormal frame around a closed loop returns a rotated frame.* By (S2) the operator $R(X,Y):T_pM\to T_pM$ is skew-symmetric, hence lies in $\mathfrak{so}(n)$, hence $\mathrm{id}-st\,R(X,Y)$ is a rotation to first order. Curvature *is* the generator of that rotation, per unit area of loop. Zero curvature on an open set $\iff$ the holonomy is trivial there $\iff$ a parallel frame exists — the third bullet of that same section.

**Sanity anchors** under this convention: $\mathbb R^n$ flat, $\mathrm{Sec}\equiv0$; the round sphere $S^n_r$ has $\mathrm{Sec}\equiv 1/r^2>0$; hyperbolic space $\mathbb H^n_r$ has $\mathrm{Sec}\equiv-1/r^2<0$. If a computation ever hands back a negative curvature for a sphere, the sign convention was dropped somewhere — not the algebra.

## Worked example

**(a) Tensoriality in the first slot.** Check $R(fX,Y)Z=fR(X,Y)Z$ term by term. Three inputs: $\nabla$ is $C^\infty$-linear in its subscript, Leibniz in its argument, and $[fX,Y]=f[X,Y]-Y(f)X$.

$$\nabla_{fX}\nabla_YZ = f\,\nabla_X\nabla_YZ \qquad\text{(no extra term: subscript slot)}$$
$$\nabla_Y\nabla_{fX}Z = \nabla_Y\big(f\nabla_XZ\big) = \underline{Y(f)\,\nabla_XZ} + f\,\nabla_Y\nabla_XZ$$
$$\nabla_{[fX,Y]}Z = f\,\nabla_{[X,Y]}Z - \underline{Y(f)\,\nabla_XZ}$$

Assembling $R(fX,Y)Z=\text{(first)}-\text{(second)}-\text{(third)}$, the two underlined terms appear with signs $-Y(f)\nabla_XZ$ and $+Y(f)\nabla_XZ$ and cancel, leaving $f\,R(X,Y)Z$. The bracket term is what does it: the derivative-of-coefficient debris from the second term is produced in exactly matching form by $[fX,Y]$.

The $Z$ slot works the same way. $\nabla_X\nabla_Y(fZ)=\big(XY f\big)Z+ (Yf)\nabla_XZ+(Xf)\nabla_YZ+f\nabla_X\nabla_YZ$; antisymmetrizing in $X,Y$ leaves $\big((XY-YX)f\big)Z=\big([X,Y]f\big)Z$, which is precisely what $\nabla_{[X,Y]}(fZ)$ subtracts.

**(b) Convention check on the round sphere.** A space of constant curvature $\kappa$ has
$$R_\kappa(X,Y)Z=\kappa\big(\langle Y,Z\rangle X-\langle X,Z\rangle Y\big).$$
Feed it to the contract's $\mathrm{Sec}$: $\langle R_\kappa(u,v)v,u\rangle=\kappa\big(\langle v,v\rangle\langle u,u\rangle-\langle u,v\rangle\langle v,u\rangle\big)=\kappa\big(\|u\|^2\|v\|^2-\langle u,v\rangle^2\big)$, so $\mathrm{Sec}(u,v)=\kappa$ with **no sign flip and no factor**. For $S^2_r\subset\mathbb R^3$, Gauss gives $\kappa=1/r^2$, so $\mathrm{Sec}=1/r^2>0$: the convention passes its own anchor. Had the contract used $R'=-R$ with the same $\mathrm{Sec}$ formula, the same sphere would report $-1/r^2$.

## Problems

1. **Recall.** From memory, write $R(X,Y)Z$, the $(0,4)$ form, and $\mathrm{Sec}(u,v)$. State the four symmetries. For each of (S1), (S2), (S3), say which hypothesis on $\nabla$ (torsion-free / metric-compatible / neither) it consumes, and say why (S4) is not on that list.
2. **Compute.** For $R_\kappa(X,Y)Z=\kappa(\langle Y,Z\rangle X-\langle X,Z\rangle Y)$: verify (S1), (S2) and (S3) directly, and evaluate $\mathrm{Sec}$ on an orthonormal pair. Then write the $\mathrm{Sec}$ of $S^3_r$ and of $\mathbb H^3_r$.
3. **Prove.** (a) $\mathrm{Sec}(u,v)$ depends only on $\mathrm{span}(u,v)$: it is unchanged under $u'=au+bv$, $v'=cu+dv$ with $ad-bc\neq0$. (b) Deduce from the symmetries alone that $R\equiv0$ on any $1$-manifold, and that on a $2$-manifold $R$ is determined by the single function $\mathrm{Sec}$.
4. **Break it.** Define the "obvious" curvature $\tilde R(X,Y)Z=\nabla_X\nabla_YZ-\nabla_Y\nabla_XZ$, dropping the bracket term. (a) Show $\tilde R(fX,Y)Z=f\tilde R(X,Y)Z-Y(f)\nabla_XZ$, so $\tilde R$ is not a tensor. (b) On flat $\mathbb R^2$ with $\nabla$ the ordinary derivative, exhibit explicit $f,X,Y,Z$ with $\tilde R(fX,Y)Z\neq f\tilde R(X,Y)Z$ — note that the true $R$ vanishes identically here, so $\tilde R$ is reporting curvature on a flat space. (c) One line: if the project had fixed $R'=-R$ but kept the contract's $\mathrm{Sec}$ formula, what curvature would $S^2_1$ report, and which downstream results would silently invert?

---

## Solutions

**1.** Definitions as above. (S1) needs neither hypothesis — it is visible in the definition. (S2) needs metric compatibility (the proof runs through $X\langle Z,Z\rangle=2\langle\nabla_XZ,Z\rangle$). (S3) needs torsion-freeness ($\nabla_XY-\nabla_YX=[X,Y]$, applied inside the Jacobi identity for $[\cdot,\cdot]$). (S4) is not a geometric hypothesis at all: it is implied algebraically by (S1)–(S3).

**2.** (S1): swapping $X,Y$ sends $\kappa(\langle Y,Z\rangle X-\langle X,Z\rangle Y)\mapsto\kappa(\langle X,Z\rangle Y-\langle Y,Z\rangle X)$, the negative. (S2): $\langle R_\kappa(X,Y)Z,W\rangle=\kappa(\langle Y,Z\rangle\langle X,W\rangle-\langle X,Z\rangle\langle Y,W\rangle)$, which is manifestly antisymmetric under $Z\leftrightarrow W$. (S3): summing the three cyclic terms, $\kappa[(\langle Y,Z\rangle X-\langle X,Z\rangle Y)+(\langle Z,X\rangle Y-\langle Y,X\rangle Z)+(\langle X,Y\rangle Z-\langle Z,Y\rangle X)]=0$; each coefficient cancels against its partner. For orthonormal $u,v$ the denominator is $1$ and $\mathrm{Sec}=\kappa$. $S^3_r$: $+1/r^2$. $\mathbb H^3_r$: $-1/r^2$.

**3.** (a) $R$ is $4$-linear, so expanding $\langle R(u',v')v',u'\rangle$ and using (S1)+(S2) (every term with a repeated argument in either antisymmetric pair dies) leaves $(ad-bc)^2\langle R(u,v)v,u\rangle$. The denominator is $\|u'\wedge v'\|^2=(ad-bc)^2\|u\wedge v\|^2$ — the Gram determinant scales by $\det{}^2$ of the change of basis. The factors cancel. (b) $n=1$: every component has two indices in an antisymmetric pair drawn from a $1$-dimensional space, so $\mathrm{Rm}=0$; equivalently the count $n^2(n^2-1)/12=0$. $n=2$: the count gives $1$, and $R_{1212}=\mathrm{Sec}\cdot(\|e_1\|^2\|e_2\|^2-\langle e_1,e_2\rangle^2)$ fixes it; all other components follow from (S1),(S2),(S4).

**4.** (a) $\nabla_{fX}\nabla_YZ=f\nabla_X\nabla_YZ$ while $\nabla_Y\nabla_{fX}Z=Y(f)\nabla_XZ+f\nabla_Y\nabla_XZ$; subtracting gives the stated result. The leftover $-Y(f)\nabla_XZ$ is precisely the piece the true definition cancels with $\nabla_{[fX,Y]}Z$. (b) On $\mathbb R^2$ take $f=x^2$, $X=\partial_1$, $Y=\partial_2$, $Z=x^1\partial_1$. Since $X,Y$ commute and the space is flat, $\tilde R(X,Y)Z=0$, so $f\tilde R(X,Y)Z=0$. But $fX=x^2\partial_1$, and $\nabla_{\partial_2}(x^1\partial_1)=0$ kills the first term, while $\nabla_{x^2\partial_1}(x^1\partial_1)=x^2\partial_1$ and $\nabla_{\partial_2}(x^2\partial_1)=\partial_1$ give the second, so $\tilde R(fX,Y)Z=-\partial_1\neq0$. Matches $-Y(f)\nabla_XZ=-\partial_1$. A non-tensorial object returning a nonzero value on flat $\mathbb R^2$ is not measuring geometry — it is measuring the coefficient functions of the frame, i.e. a chart artifact of exactly the kind the project is trying to keep out of its constants. (c) $S^2_1$ would report $\mathrm{Sec}=-1$. Everything whose sign is read off curvature would invert: the bi-invariant formula $\mathrm{Sec}=\tfrac14\|[X,Y]\|^2\ge0$, the direction of the Jacobi/tidal term $R(u,v)v$ in the variational equation, and every Hessian comparison bound on $d(\cdot,\cdot)$ — i.e. the sign of the curvature correction in the eventual tube.
