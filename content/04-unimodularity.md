---
tags: [lie-groups, haar-measure, unimodularity, stochastics]
---
# Unimodularity

**Prereq:** [[01-adjoint-and-coadjoint]], [[probability-on-manifolds]] (§ Haar measure — left/right Haar, and *unimodular = the two coincide*, are assumed known)
**Goal:** turn "left Haar $=$ right Haar" into the algebraic test $\mathrm{tr}\,\mathrm{ad}_\eta=0$, and from there into the identity $\sum_i\mathrm{ad}^*_{e_i}e_i=0$ that deletes the drift from Brownian motion on $G$.

## Definitions

:::info[Definition]
Fix a left Haar measure $\mu$ on $G$ ($\mu(hA)=\mu(A)$, the $dg$ of [[probability-on-manifolds]]). For fixed $h$, set $\mu_h(A):=\mu(Ah)$. Left and right translations commute, $g(Ah)=(gA)h$, so $\mu_h(gA)=\mu((gA)h)=\mu(g(Ah))=\mu(Ah)=\mu_h(A)$: $\mu_h$ is again a (nonzero, Radon) left Haar measure. Uniqueness of left Haar up to scale then gives a single $\Delta(h)>0$ with $\mu_h=\Delta(h)\mu$ *as measures* —

$$\mu(Ah)=\Delta(h)\,\mu(A)\qquad\text{for all measurable }A .$$

$\Delta:G\to(\mathbb R_{>0},\times)$ is the **modular function**. It is a continuous homomorphism: $\mu(Ah_1h_2)=\Delta(h_2)\Delta(h_1)\mu(A)$. It does not depend on which left Haar measure was chosen, since rescaling $\mu$ cancels.

*Convention.* Some texts define $\Delta$ as the reciprocal of this. The only statement used downstream is $\Delta\equiv1$, which is convention-free — but the formula $\Delta=|\det\mathrm{Ad}|^{-1}$ below is not, so do not mix sources.
:::

:::info[Definition]
$G$ is **unimodular** if $\Delta\equiv1$, equivalently if some (hence every) left Haar measure is also right-invariant.
:::

*Where the load is carried.* The only non-formal input above is **uniqueness of left Haar up to scale** — without it, $\mu(Ah)/\mu(A)$ could a priori depend on $A$ and $\Delta$ would not be a function of $h$ at all. It is assumed here (see [[probability-on-manifolds]]); for a Lie group it is not needed as a black box, since the volume-form construction below produces $\Delta$ directly — see the *Aside* after the proof of (2) $\Leftrightarrow$ (3).

## The equivalences

:::tip[Theorem]
For a connected matrix Lie group $G$ with Lie algebra $\mathfrak g$, the following are equivalent.

1. Left Haar measure is right-invariant.
2. $\Delta(h)=1$ for all $h\in G$.
3. $|\det\mathrm{Ad}_h|=1$ for all $h\in G$.
4. $\mathrm{tr}\,\mathrm{ad}_\eta=0$ for all $\eta\in\mathfrak g$.
:::

### Reading the statement: $\det$ and $\mathrm{tr}$ of an *operator*

Conditions (3) and (4) apply $\det$ and $\mathrm{tr}$ to $\mathrm{Ad}_h:\mathfrak g\to\mathfrak g$ and $\mathrm{ad}_\eta:\mathfrak g\to\mathfrak g$ — linear maps of an abstract vector space, with no matrix in sight (and $\mathfrak g$ has no preferred basis). Two ways to make sense of that. They agree, and the first is enough to read the Theorem.

**Route 1 — pick a basis, then check the answer doesn't depend on it.** Fix a basis $\{b_1,\dots,b_n\}$ of $\mathfrak g$. Any linear $A:\mathfrak g\to\mathfrak g$ acquires a matrix $[A]$ by expanding the images of the basis vectors, $Ab_j=\sum_i[A]_{ij}b_i$ (*columns are images* — this is the convention used in the worked examples below). A second basis, related by an invertible $P$, gives

$$[A]'=P^{-1}[A]P,$$

and both $\det$ and $\mathrm{tr}$ are blind to that conjugation:

$$\det(P^{-1}[A]P)=(\det P)^{-1}\det[A]\det P=\det[A],\qquad
\mathrm{tr}(P^{-1}[A]P)=\mathrm{tr}([A]PP^{-1})=\mathrm{tr}[A]$$

(the second by cyclicity, $\mathrm{tr}(XY)=\mathrm{tr}(YX)$). So the two *numbers* belong to $A$ itself, not to the basis, and one defines $\det A:=\det[A]$, $\mathrm{tr}\,A:=\mathrm{tr}[A]$ computed in any basis whatsoever.

Note what this needs: $A$ must map $\mathfrak g$ to **itself**. A linear map between two different spaces has no determinant and no trace — there is no conjugation for it to be invariant under. That is exactly why $\det\mathrm{Ad}_h$ and $\mathrm{tr}\,\mathrm{ad}_\eta$ are legal ($\mathrm{Ad}_h,\mathrm{ad}_\eta:\mathfrak g\to\mathfrak g$) while, say, $\det\mathbb I$ for $\mathbb I:\mathfrak g\to\mathfrak g^*$ is **not** — the "determinant of the inertia tensor" is a basis-dependent quantity, and this is one concrete instance of the conservatism the project is chasing.

**Route 2 — no basis at all.** Both numbers are the scalar by which $A$ acts on a one-dimensional space.

*Determinant.* $\Lambda^n\mathfrak g^*$, the alternating $n$-forms on the $n$-dimensional $\mathfrak g$, is one-dimensional: an alternating $n$-form is determined by its single value $\omega(b_1,\dots,b_n)$, because expanding any other $n$-tuple multilinearly kills every term with a repeated basis vector. Now $A$ acts on this space by pullback, $\omega\mapsto\omega(A\,\cdot,\dots,A\,\cdot)$, and a linear map of a one-dimensional space *is* a number. That number is $\det A$. (This is T1 below.)

*Trace.* The same statement one degree down. The map

$$v_1\wedge\dots\wedge v_n\;\longmapsto\;\sum_{i=1}^n v_1\wedge\dots\wedge Av_i\wedge\dots\wedge v_n$$

is again a linear map of the one-dimensional $\Lambda^n\mathfrak g$, hence a number, and that number is $\mathrm{tr}\,A$. The memorable form of the same fact is the Leibniz rule for $\det$:

$$\mathrm{tr}\,A=\left.\frac{d}{dt}\right|_{t=0}\det(\mathrm{id}+tA),\qquad\text{equivalently}\qquad \left.\frac{d}{dt}\right|_{t=0}\det e^{tA}=\mathrm{tr}\,A .$$

**Trace is the infinitesimal determinant** — which is precisely why the Theorem's (3) and (4) are the same condition, one at group level and one at algebra level, and why the proof of (3) $\Leftrightarrow$ (4) below is just a differentiation at $t=0$.

:::warning[Two different traces live on a matrix Lie algebra — do not conflate them]
For a matrix group the elements of $\mathfrak g$ are themselves matrices, so "trace" is ambiguous:

- $\mathrm{tr}(\eta)$ — the trace of $\eta$ as an $n\times n$ matrix;
- $\mathrm{tr}(\mathrm{ad}_\eta)$ — the trace of the operator $\mathrm{ad}_\eta=[\eta,\cdot\,]$ on the $\dim\mathfrak g$-dimensional space $\mathfrak g$.

Different sizes, different numbers, and **only the second one appears in the Theorem**. Sharpest example: $\mathfrak{gl}(n,\mathbb R)$ has $\dim=n^2$, and $\mathrm{ad}_\eta=L_\eta-R_\eta$ where $L_\eta X=\eta X$, $R_\eta X=X\eta$. In the basis $\{E_{ij}\}$ one finds $\mathrm{tr}\,L_\eta=\mathrm{tr}\,R_\eta=n\,\mathrm{tr}\,\eta$, so

$$\mathrm{tr}\,\mathrm{ad}_\eta=n\,\mathrm{tr}\,\eta-n\,\mathrm{tr}\,\eta=0\quad\text{for every }\eta,$$

and $GL(n,\mathbb R)$ is unimodular — even though $\mathrm{tr}\,\eta\neq0$ for most $\eta$. Where the two agree in the worked examples below ($\mathfrak{so}(3)$, $\mathfrak{aff}(\mathbb R)$) it is a coincidence of small dimension, not a rule.
:::

**(1) $\Leftrightarrow$ (2)** is the definition: $\mu(Ah)=\mu(A)$ for all $A,h$ says exactly $\Delta\equiv1$.

The other two implications need a way to *compute* $\mu$. The next subsection builds it; the proofs follow.

### Toolkit: Haar measure as a left-invariant volume form

On a matrix Lie group, write $(dL_g)_x u=gu$ and $(dR_h)_x u=uh$ — for matrix groups the differentials of translation are literally matrix multiplication, so $g^{-1}u\in\mathfrak g$ means the matrix product. Three facts:

:::info[T1 — determinant, basis-free]
$\Lambda^n\mathfrak g^*$ (alternating $n$-forms on the $n$-dimensional $\mathfrak g$) is **one-dimensional**. Consequently, for any linear $F:\mathfrak g\to\mathfrak g$ and any $\omega_e\in\Lambda^n\mathfrak g^*$,

$$\omega_e(Fv_1,\dots,Fv_n)=\det(F)\,\omega_e(v_1,\dots,v_n).$$

This is Route 2 above, restated for use: $(v_1,\dots,v_n)\mapsto\omega_e(Fv_1,\dots,Fv_n)$ is alternating and $n$-linear, hence a multiple of $\omega_e$ by one-dimensionality, and the multiple is by definition $\det F$ — no basis, no matrix.

The proof below needs the basis-free version specifically. Route 1 would force a choice of basis of $\mathfrak g$ at every $h$, and then an argument that the choices are compatible; Route 2 skips that entirely, because the one-dimensionality of $\Lambda^n\mathfrak g^*$ is doing the work a basis would otherwise do.
:::

:::info[T2 — change of variables]
For a diffeomorphism $\varphi:M\to M$ and a top form $\omega$, $\displaystyle\int_{\varphi(A)}|\omega|=\int_A|\varphi^*\omega|$, where $(\varphi^*\omega)_x(v_1,\dots,v_n)=\omega_{\varphi(x)}(d\varphi\,v_1,\dots,d\varphi\,v_n)$. The absolute value is what turns a form (orientation-sensitive) into a measure (not).
:::

**Construction of $\mu$.** Pick any nonzero $\omega_e\in\Lambda^n\mathfrak g^*$ — a choice of "unit volume" on $\mathfrak g$, unique up to scale by T1. Push it around by left translation:

$$\omega_g(u_1,\dots,u_n):=\omega_e\big(g^{-1}u_1,\dots,g^{-1}u_n\big),\qquad u_i\in T_gG .$$

This is a nowhere-vanishing smooth $n$-form with $L_h^*\omega=\omega$ (immediate: $(L_h^*\omega)_g(u_i)=\omega_{hg}(hu_i)=\omega_e((hg)^{-1}hu_i)=\omega_e(g^{-1}u_i)$). Then $\mu(A):=\int_A|\omega|$ is left-invariant by T2, and it is the left Haar measure.

### Proof of (2) $\Leftrightarrow$ (3)

Compute $R_h^*\omega$, the pullback of $\omega$ by right translation $R_h(g)=gh$.

**Step 1 — $R_h^*\omega$ is still left-invariant.** Because left and right translation commute ($L_g\circ R_h=R_h\circ L_g$, i.e. $g(xh)=(gx)h$, associativity again):

$$L_g^*(R_h^*\omega)=(R_h\circ L_g)^*\omega=(L_g\circ R_h)^*\omega=R_h^*(L_g^*\omega)=R_h^*\omega .$$

**Step 2 — so it is a constant multiple of $\omega$.** A left-invariant top form is determined by its value at $e$ (left-translate it everywhere else), and $\Lambda^n\mathfrak g^*$ is one-dimensional by T1. Hence $R_h^*\omega=c(h)\,\omega$ for a single number $c(h)$, and $c(h)$ is read off at $e$.

**Step 3 — evaluate at $e$.** Note $R_h(e)=h$, so for $v_1,\dots,v_n\in\mathfrak g=T_eG$,

$$(R_h^*\omega)_e(v_1,\dots,v_n)=\omega_h\big(v_1h,\dots,v_nh\big)=\omega_e\big(h^{-1}v_1h,\dots,h^{-1}v_nh\big)=\omega_e\big(\mathrm{Ad}_{h^{-1}}v_1,\dots\big),$$

using the definition of $\omega_h$ in the middle step. Abstractly the same line is $(dL_{h^{-1}})_h\circ(dR_h)_e=d(L_{h^{-1}}\circ R_h)_e=d\big(g\mapsto h^{-1}gh\big)_e=\mathrm{Ad}_{h^{-1}}$: *conjugation is the composite of a right and a left translation*, and that is the entire content of the proof. Now T1 gives

$$R_h^*\omega=\det(\mathrm{Ad}_{h^{-1}})\,\omega .$$

**Step 4 — back to measures.** By T2, $\mu(Ah)=\int_{R_h(A)}|\omega|=\int_A|R_h^*\omega|=|\det\mathrm{Ad}_{h^{-1}}|\,\mu(A)$. Since $\mathrm{Ad}$ is a homomorphism, $\mathrm{Ad}_{h^{-1}}=(\mathrm{Ad}_h)^{-1}$, so

$$\Delta(h)=|\det\mathrm{Ad}_{h^{-1}}|=|\det\mathrm{Ad}_h|^{-1},$$

and $\Delta\equiv1\iff|\det\mathrm{Ad}_h|=1$ for all $h$. $\square$

*Aside.* This also re-proves that $\Delta$ exists, for Lie groups, without invoking Haar uniqueness: Step 2's one-dimensionality does the job that uniqueness did in the Definition.

### Proof of (3) $\Leftrightarrow$ (4)

Three ingredients.

**(a) $\mathrm{Ad}_{\exp_G(t\eta)}=e^{t\,\mathrm{ad}_\eta}$ as operators on $\mathfrak g$.** Set $F(t)=\mathrm{Ad}_{\exp_G(t\eta)}$. Since $\mathrm{Ad}$ is a homomorphism and $\exp_G((s+t)\eta)=\exp_G(s\eta)\exp_G(t\eta)$, we get $F(s+t)=F(s)F(t)$. Differentiate in $s$ at $s=0$: $F'(t)=F'(0)F(t)=\mathrm{ad}_\eta F(t)$, where $F'(0)=\mathrm{ad}_\eta$ is exactly [[01-adjoint-and-coadjoint]]'s $\tfrac{d}{dt}\big|_0\mathrm{Ad}_{\exp_G(t\eta)}=\mathrm{ad}_\eta$. A linear ODE with $F(0)=\mathrm{id}$ has the unique solution $F(t)=e^{t\,\mathrm{ad}_\eta}$.

**(b) $\det e^A=e^{\mathrm{tr}A}$.** Triangularize $A$ over $\mathbb C$ with eigenvalues $\lambda_i$; then $e^A$ is triangular with diagonal $e^{\lambda_i}$, so $\det e^A=\prod_ie^{\lambda_i}=e^{\sum_i\lambda_i}=e^{\mathrm{tr}A}$.

**(c) For connected $G$, $\exp_G(\mathfrak g)$ generates $G$.** $d(\exp_G)_0=\mathrm{id}$, so $\exp_G$ is a diffeomorphism from a neighbourhood of $0$ onto a neighbourhood $U\ni e$. The subgroup $H$ generated by $U$ is open (it contains $hU$ for every $h\in H$), hence closed (its complement is a union of cosets $gH$, each open), hence $H=G$ by connectedness. So every $h\in G$ is a *finite product* $\exp_G(\eta_1)\cdots\exp_G(\eta_k)$.

Combining (a) and (b) with the formula just proved,

$$\Delta(\exp_G(t\eta))=\big|\det e^{t\,\mathrm{ad}_\eta}\big|^{-1}=e^{-t\,\mathrm{tr}\,\mathrm{ad}_\eta}$$

($\mathrm{tr}\,\mathrm{ad}_\eta$ is real, so the absolute value is vacuous).

**(4) $\Rightarrow$ (3).** If $\mathrm{tr}\,\mathrm{ad}_\eta=0$ for every $\eta$ then $\Delta=1$ on $\exp_G(\mathfrak g)$. By (c) any $h$ is a finite product of exponentials, and $\Delta$ is a homomorphism, so $\Delta(h)$ is the corresponding product of $1$s.

**(3) $\Rightarrow$ (4).** Fix $\eta$ and differentiate the constant function $t\mapsto\Delta(\exp_G(t\eta))=1$ at $t=0$: $-\mathrm{tr}\,\mathrm{ad}_\eta=0$. $\square$

Connectedness is used **only** in (c). For disconnected $G$, (4) still controls the identity component, and $\Delta$ can be nontrivial on the other components.

## From $\mathrm{tr}\,\mathrm{ad}=0$ to $\sum_i\mathrm{ad}^*_{e_i}e_i=0$

This is the step that gets used, and the one where the metric enters. Let $\langle\cdot,\cdot\rangle_{\mathbb I}$ be an inner product on $\mathfrak g$ with $\{e_i\}_{i=1}^n$ orthonormal, and $\mathbb I:\mathfrak g\to\mathfrak g^*$ the induced flat map.

Note first that $\mathrm{ad}^*_{e_i}e_i$ is an abuse: $\mathrm{ad}^*_\xi$ eats elements of $\mathfrak g^*$, not $\mathfrak g$. What is meant is $\mathrm{ad}^*_{e_i}(\mathbb I e_i)$, pulled back to $\mathfrak g$ — that is, the metric adjoint $\widetilde{\mathrm{ad}}_\xi=\mathbb I^{-1}\mathrm{ad}^*_\xi\mathbb I$ of [[notation]]. So define

$$J \;:=\; \sum_{i=1}^n \widetilde{\mathrm{ad}}_{e_i}e_i \;=\; \mathbb I^{-1}\sum_{i=1}^n\mathrm{ad}^*_{e_i}(\mathbb I e_i) \;\in\;\mathfrak g .$$

:::tip[Proposition]
$\langle J,\eta\rangle_{\mathbb I}=-\mathrm{tr}\,\mathrm{ad}_\eta$ for every $\eta\in\mathfrak g$. Hence $G$ unimodular $\iff J=0$, and $J$ is independent of which orthonormal basis is used.
:::

*Proof.* One equality per line. Throughout, $\langle\cdot,\cdot\rangle$ with no subscript is the **dual pairing** $\mathfrak g^*\times\mathfrak g\to\mathbb R$ and $\langle\cdot,\cdot\rangle_{\mathbb I}$ is the **inner product** on $\mathfrak g$; they are linked by $\langle\xi,\eta\rangle_{\mathbb I}=\langle\mathbb I\xi,\eta\rangle$ ([[notation]]). Keeping them apart is the whole difficulty of this computation.

$$\langle J,\eta\rangle_{\mathbb I}
\;\overset{(1)}{=}\;\langle\mathbb IJ,\eta\rangle
\;\overset{(2)}{=}\;\sum_i\langle\mathrm{ad}^*_{e_i}(\mathbb I e_i),\eta\rangle
\;\overset{(3)}{=}\;\sum_i\langle\mathbb I e_i,\mathrm{ad}_{e_i}\eta\rangle
\;\overset{(4)}{=}\;\sum_i\langle e_i,[e_i,\eta]\rangle_{\mathbb I}
\;\overset{(5)}{=}\;-\sum_i\langle e_i,\mathrm{ad}_\eta e_i\rangle_{\mathbb I}
\;\overset{(6)}{=}\;-\mathrm{tr}\,\mathrm{ad}_\eta .$$

1. Definition of the induced inner product, read right-to-left.
2. $\mathbb IJ=\mathbb I\,\mathbb I^{-1}\sum_i\mathrm{ad}^*_{e_i}(\mathbb Ie_i)=\sum_i\mathrm{ad}^*_{e_i}(\mathbb Ie_i)$ — the $\mathbb I$ cancels the $\mathbb I^{-1}$ in the definition of $J$. Everything so far lives in $\mathfrak g^*$.
3. Definition of the coadjoint, $\langle\mathrm{ad}^*_\xi\mu,\eta\rangle=\langle\mu,\mathrm{ad}_\xi\eta\rangle$, applied with $\xi=\mu^\sharp=e_i$. This is the plain dual with **no sign flip** — see [[notation]]; a source that defines $\mathrm{ad}^*$ with a minus sign flips the sign of $J$ here.
4. $\mathrm{ad}_{e_i}\eta=[e_i,\eta]$ by definition, and $\langle\mathbb Ie_i,\cdot\rangle=\langle e_i,\cdot\rangle_{\mathbb I}$ by step 1 again — we are back in $\mathfrak g$ with an inner product.
5. Antisymmetry of the bracket: $[e_i,\eta]=-[\eta,e_i]=-\mathrm{ad}_\eta e_i$. **This is the swap that matters** — before it, $\eta$ sits in the second slot of the bracket and the sum is not a trace of anything; after it, the operator being summed against is $\mathrm{ad}_\eta$, one fixed operator, with the summation index only in the basis vectors.
6. The trace formula $\sum_i\langle e_i,Ae_i\rangle_{\mathbb I}=\mathrm{tr}\,A$. Writing $Ae_i=\sum_jA_{ji}e_j$, orthonormality gives $\langle e_i,Ae_i\rangle_{\mathbb I}=A_{ii}$, and summing gives the trace. **Orthonormality is used only here**, and the formula is false for a general basis (there one needs the dual basis, $\mathrm{tr}A=\sum_i\langle e^i,Ae_i\rangle$).

For the two consequences: $\mathrm{tr}\,\mathrm{ad}_\eta$ is the trace of a linear operator, so basis-independent, and $\eta\mapsto\mathrm{ad}_\eta$ is linear — hence $\chi:=-\mathrm{tr}\,\mathrm{ad}\in\mathfrak g^*$ is a well-defined linear functional built with no metric and no basis. The identity just proved says $\langle\mathbb IJ,\eta\rangle=\chi(\eta)$ for **all** $\eta$, and a functional is determined by its values, so $\mathbb IJ=\chi$, i.e. $J=\mathbb I^{-1}\chi$. Since $\mathbb I$ is invertible, $J=0\iff\chi=0\iff\mathrm{tr}\,\mathrm{ad}_\eta=0$ for all $\eta$, which is condition (4) of the Theorem. And $J=\mathbb I^{-1}\chi$ makes no reference to $\{e_i\}$, so any other orthonormal basis produces the same $J$ — even though the *defining sum* $\sum_i\widetilde{\mathrm{ad}}_{e_i}e_i$ visibly mentions one. $\square$

:::info[Read this carefully]
$\eta\mapsto-\mathrm{tr}\,\mathrm{ad}_\eta$ is a linear functional on $\mathfrak g$: a genuine element $\chi\in\mathfrak g^*$, defined with no metric at all. The Proposition says $J=\mathbb I^{-1}\chi$. So:

- **Vanishing is metric-free.** $\mathbb I$ is invertible, so $J=0\iff\chi=0$, whatever inner product was chosen.
- **The vector $J$ is not.** Rescale $\langle\cdot,\cdot\rangle_{\mathbb I}\mapsto c\langle\cdot,\cdot\rangle_{\mathbb I}$ and $J\mapsto c^{-1}J$. A non-unimodular group has a drift whose *size* is a metric choice; only its being nonzero is intrinsic.

This is why $\mathrm{tr}\,\mathrm{ad}=0$ is the right hypothesis to state, and $J=0$ the right consequence to use.
:::

## Who is unimodular

| Class | Reason |
|---|---|
| abelian | $\mathrm{ad}\equiv0$ |
| compact ($SO(3)$, $SU(n)$, $O(n)$) | $\Delta(G)$ is a compact subgroup of $\mathbb R_{>0}$, hence $\{1\}$ — Problem 3b |
| nilpotent (Heisenberg) | every $\mathrm{ad}_\eta$ is nilpotent, so $\mathrm{tr}\,\mathrm{ad}_\eta=0$ |
| perfect, $[\mathfrak g,\mathfrak g]=\mathfrak g$ (semisimple, $SL(n,\mathbb R)$) | Problem 3a |
| $SE(3)$, $SE(n)$ | Problem 2 — and note $SE(3)$ carries **no** bi-invariant metric, so unimodular is strictly weaker |
| $\mathrm{Aff}(\mathbb R)$ | **not** — worked example (b) |

The list follows [[@leeGeometricInterpretationBrownian2025]] Remark 3.

## Worked example

**(a) $\mathfrak{so}(3)$.** Basis $\hat e_1,\hat e_2,\hat e_3$, orthonormal for $\langle\eta,\zeta\rangle=\tfrac12\mathrm{tr}(\eta^\top\zeta)=(\eta^\vee)^\top\zeta^\vee$. Since $[\hat a,\hat b]=\widehat{a\times b}$, the matrix of $\mathrm{ad}_{\hat a}$ in the basis $\{\hat e_i\}$ is the matrix of $b\mapsto a\times b$, namely $\hat a$ itself:

$$\mathrm{ad}_{\hat a}\;\cong\;\hat a=\begin{pmatrix}0&-a_3&a_2\\a_3&0&-a_1\\-a_2&a_1&0\end{pmatrix},\qquad \mathrm{tr}\,\mathrm{ad}_{\hat a}=0 .$$

Skew matrices have zero diagonal, so this is immediate for every $a$. Directly, term by term,

$$\langle J,\hat\eta\rangle=\sum_{i=1}^3\langle \hat e_i,[\hat e_i,\hat\eta]\rangle=\sum_{i=1}^3 e_i^\top(e_i\times\eta)=0,$$

each summand vanishing on its own because $e_i\perp(e_i\times\eta)$. So $J=0$: $SO(3)$ is unimodular.

**(b) $\mathrm{Aff}(\mathbb R)$**, the $ax+b$ group $\Big\{\begin{pmatrix}a&b\\0&1\end{pmatrix}:a>0\Big\}$. Take $E_1=\begin{pmatrix}1&0\\0&0\end{pmatrix}$, $E_2=\begin{pmatrix}0&1\\0&0\end{pmatrix}$, so $[E_1,E_2]=E_1E_2-E_2E_1=E_2$, and **declare $\{E_1,E_2\}$ orthonormal** (this fixes $\mathbb I$; a different scaling changes $J$'s length, not its vanishing).

$$\mathrm{ad}_{E_1}:\;E_1\mapsto0,\;E_2\mapsto E_2 \;\Rightarrow\; \begin{pmatrix}0&0\\0&1\end{pmatrix},\quad \mathrm{tr}\,\mathrm{ad}_{E_1}=1\neq0 .$$

$$\mathrm{ad}_{E_2}:\;E_1\mapsto[E_2,E_1]=-E_2,\;E_2\mapsto0 \;\Rightarrow\; \begin{pmatrix}0&0\\-1&0\end{pmatrix},\quad \mathrm{tr}\,\mathrm{ad}_{E_2}=0 .$$

By the Proposition, $\langle J,E_1\rangle=-1$ and $\langle J,E_2\rangle=0$, so

$$\boxed{\;J=\sum_i\widetilde{\mathrm{ad}}_{E_i}E_i=-E_1\neq0\;}$$

**Cross-check against Haar directly.** Coordinates $g=(a,b)$, product $(a_1,b_1)(a_2,b_2)=(a_1a_2,\,a_1b_2+b_1)$ (read off from $\left(\begin{smallmatrix}a_1&b_1\\0&1\end{smallmatrix}\right)\left(\begin{smallmatrix}a_2&b_2\\0&1\end{smallmatrix}\right)$).

*Left translation* by $h=(h_a,h_b)$ is $(a,b)\mapsto(h_aa,\ h_ab+h_b)$, so its Jacobian matrix is $\left(\begin{smallmatrix}h_a&0\\0&h_a\end{smallmatrix}\right)$, determinant $h_a^2$ — a constant in $(a,b)$. To make a measure $\rho(a,b)\,da\,db$ left-invariant we need $\rho$ to undo that factor: $\rho(h_aa,h_ab+h_b)\cdot h_a^2=\rho(a,b)$, and $\rho=1/a^2$ works ($\tfrac{1}{h_a^2a^2}\cdot h_a^2=\tfrac1{a^2}$). So $d\mu_L=\dfrac{da\,db}{a^2}$.

*Right translation* by $h$ is $(a,b)\mapsto(ah_a,\ ah_b+b)$, Jacobian $\left(\begin{smallmatrix}h_a&0\\h_b&1\end{smallmatrix}\right)$, determinant $h_a$. The same argument with $\rho=1/a$ gives $d\mu_R=\dfrac{da\,db}{a}$.

They are genuinely different measures, so $\mathrm{Aff}(\mathbb R)$ is not unimodular. For $\Delta$ itself, change variables in the defining integral: substituting $(a,b)=R_h(a',b')=(a'h_a,\ a'h_b+b')$, with Jacobian $h_a$,

$$\mu_L(Ah)=\int_{Ah}\frac{da\,db}{a^2}=\int_A\frac{h_a\,da'\,db'}{(a'h_a)^2}=\frac{1}{h_a}\int_A\frac{da'\,db'}{a'^2}=\frac{1}{h_a}\,\mu_L(A),$$

so $\Delta(h)=1/h_a$ — and note the factor came out *constant*, independent of $A$, which is the $A$-independence of the Definition made visible in coordinates.

Confirm against $\Delta=|\det\mathrm{Ad}|^{-1}$. With $g=\left(\begin{smallmatrix}a&b\\0&1\end{smallmatrix}\right)$ and $g^{-1}=\left(\begin{smallmatrix}1/a&-b/a\\0&1\end{smallmatrix}\right)$, the conjugations $\mathrm{Ad}_g\eta=g\eta g^{-1}$ are

$$gE_1g^{-1}=\left(\begin{smallmatrix}1&-b\\0&0\end{smallmatrix}\right)=E_1-bE_2,\qquad gE_2g^{-1}=\left(\begin{smallmatrix}0&a\\0&0\end{smallmatrix}\right)=aE_2 .$$

Columns are images, so in the basis $\{E_1,E_2\}$,

$$\mathrm{Ad}_{(a,b)}=\begin{pmatrix}1&0\\-b&a\end{pmatrix},\qquad\det=a,$$

so $|\det\mathrm{Ad}_h|^{-1}=1/h_a=\Delta(h)$. ✓ And the infinitesimal version: $\mathrm{tr}\,\mathrm{ad}_{E_1}=1$ is the derivative of $a\mapsto\det\mathrm{Ad}$ along $\exp(tE_1)=(e^t,0)$, namely $\tfrac{d}{dt}e^t\big|_0=1$. ✓

*Convention note.* [[@leeGeometricInterpretationBrownian2025]] §V-G reports $J=-\sqrt2\,e_1$. That is the same computation with $\langle\eta,\zeta\rangle=\tfrac12\mathrm{tr}(\eta^\top\zeta)$, whose orthonormal basis is $e_i=\sqrt2E_i$; then $[e_1,e_2]=\sqrt2 e_2$ and $\mathrm{tr}\,\mathrm{ad}_{e_1}=\sqrt2$. Exactly the metric-dependence flagged above.

## Why it matters

:::tip[Corollary]
[[@leeGeometricInterpretationBrownian2025]] Theorem 5 (eq. 45) gives Brownian motion on $G$ with a left-invariant metric, in Stratonovich form,

$$g^{-1}dg=\tfrac12\sum_i\mathrm{ad}^*_{e_i}e_i\,dt+\sum_i e_i\circ dW_i=\tfrac12 J\,dt+\sum_i e_i\circ dW_i .$$

If $G$ is unimodular then $J=0$ and this collapses to the drift-free $g^{-1}dg=\sum_i e_i\circ dW_i$ ([[@leeGeometricInterpretationBrownian2025]] Corollary 1, eq. 49). $\square$
:::

$J$ is not an artifact of the stochastic calculus. [[03-levi-civita-left-invariant]] computes, from Koszul, that for a left-invariant metric

$$\nabla_\xi\eta=\tfrac12\big([\xi,\eta]-\widetilde{\mathrm{ad}}_\xi\eta-\widetilde{\mathrm{ad}}_\eta\xi\big)
\quad\Longrightarrow\quad
\nabla_{e_i}e_i=\tfrac12\big(0-2\widetilde{\mathrm{ad}}_{e_i}e_i\big)=-\widetilde{\mathrm{ad}}_{e_i}e_i$$

(the bracket $[e_i,e_i]$ vanishes and the two adjoint terms coincide). Summing over the frame,

$$\sum_i\nabla_{E_i}E_i=-\sum_i\widetilde{\mathrm{ad}}_{e_i}e_i=-J .$$

So $J$ is exactly the failure of the left-translated orthonormal frame to be geodesic — it is a Riemannian object that happens to be computable algebraically, which is why the same quantity shows up whether one arrives via Haar measure, via the connection, or via Itô's formula. Lesson 21 does the stochastics; this lesson supplies the algebraic hypothesis that makes it vanish, and it holds for $SO(3)$ and $SE(3)$, which is why those two are easy.

:::warning[Open question]
$\mathrm{tr}\,\mathrm{ad}=0$ is metric-free, but the *bound* it feeds is not: for non-unimodular $G$ the drift $\tfrac12\mathbb I^{-1}\chi$ inherits $\mathbb I$, and its size is exactly the sort of metric-dependent constant the thesis wants out of tube estimates. What is the intrinsic statement — is $\|\chi\|$ measured in $\mathbb I^{-1}$ the honest constant, or does it recombine with curvature?
:::

## Problems

1. **Recall.** Without looking: define the modular function $\Delta$, state the four equivalent conditions of the Theorem, and write $J$ in terms of $\mathrm{ad}^*$ and of $\widetilde{\mathrm{ad}}$. Say precisely where an inner product is needed and where it is not. Then: why is $\det\mathrm{Ad}_h$ a well-defined number, while $\det\mathbb I$ for $\mathbb I:\mathfrak g\to\mathfrak g^*$ is not?
2. **Compute.** On $\mathfrak{se}(3)$, with $\eta=(\omega,v)$ and $[(\omega,v),(\omega',v')]=(\omega\times\omega',\ \omega\times v'-\omega'\times v)$, write the $6\times6$ matrix of $\mathrm{ad}_{(\omega,v)}$ in $\{(\omega',v')\}$ coordinates and compute its trace. Conclude $J=0$ for **every** left-invariant metric on $SE(3)$ — including the ones that are not bi-invariant.
3. **Prove.** (a) Show $\mathrm{tr}\,\mathrm{ad}_{[\xi,\eta]}=0$ for all $\xi,\eta$, and deduce that $[\mathfrak g,\mathfrak g]=\mathfrak g$ implies unimodular. (b) Show that a compact $G$ is unimodular, using only that $\Delta:G\to(\mathbb R_{>0},\times)$ is a continuous homomorphism.
4. **Break it.** On $\mathrm{Aff}(\mathbb R)$ with $\{E_1,E_2\}$ orthonormal as above, $J=-E_1$. (a) Write the Stratonovich SDE for Brownian motion and identify the surviving drift. (b) Integrate the drift alone: solve $\dot g=g\cdot(\tfrac12 J)$ in coordinates $(a,b)$. (c) Say what this means dynamically for a "driftless, isotropic" noise model on a non-unimodular group, and what it does to a tube drawn around a nominal trajectory.

---

## Solutions

**1.** $\mu(Ah)=\Delta(h)\mu(A)$ for a left Haar $\mu$; conditions (1)–(4) of the Theorem. $J=\sum_i\widetilde{\mathrm{ad}}_{e_i}e_i=\mathbb I^{-1}\sum_i\mathrm{ad}^*_{e_i}(\mathbb I e_i)$. Metric-free: $\Delta$, $\det\mathrm{Ad}$, $\mathrm{tr}\,\mathrm{ad}$, the functional $\chi=-\mathrm{tr}\,\mathrm{ad}\in\mathfrak g^*$, and the statement $\chi=0$. Metric-dependent: the orthonormal basis $\{e_i\}$, the identification $\mathfrak g^*\cong\mathfrak g$, and the vector $J=\mathbb I^{-1}\chi$ itself.

$\mathrm{Ad}_h$ maps $\mathfrak g$ to itself, so a change of basis acts on its matrix by conjugation, $[\mathrm{Ad}_h]\mapsto P^{-1}[\mathrm{Ad}_h]P$, and $\det$ is conjugation-invariant. $\mathbb I$ maps $\mathfrak g$ to the *different* space $\mathfrak g^*$; changing the basis of $\mathfrak g$ changes the dual basis of $\mathfrak g^*$ too, so its matrix transforms as $[\mathbb I]\mapsto P^\top[\mathbb I]P$ and $\det[\mathbb I]\mapsto(\det P)^2\det[\mathbb I]$ — not a number attached to $\mathbb I$. (What *is* well defined is the sign of $\det[\mathbb I]$, and ratios like $\det\mathbb I_1/\det\mathbb I_2$ for two inner products.)

**2.** The first component of the bracket is $\hat\omega\omega'$; the second is $\omega\times v'-\omega'\times v=\hat\omega v'+\hat v\omega'$. Hence

$$\mathrm{ad}_{(\omega,v)}=\begin{pmatrix}\hat\omega&0\\ \hat v&\hat\omega\end{pmatrix},\qquad \mathrm{tr}=2\,\mathrm{tr}\,\hat\omega=0 .$$

So $\chi=0$, and since $J=\mathbb I^{-1}\chi$ this gives $J=0$ for *any* $\mathbb I$ — the conclusion is independent of the metric even though $J$'s definition is not. $SE(3)$ therefore has drift-free Brownian motion despite admitting no bi-invariant metric.

**3.** (a) $\mathrm{ad}$ is a Lie algebra homomorphism (Jacobi identity), so $\mathrm{ad}_{[\xi,\eta]}=\mathrm{ad}_\xi\mathrm{ad}_\eta-\mathrm{ad}_\eta\mathrm{ad}_\xi$, whose trace is $0$ by $\mathrm{tr}(AB)=\mathrm{tr}(BA)$. So the functional $\chi$ annihilates $[\mathfrak g,\mathfrak g]$; if that equals $\mathfrak g$ then $\chi=0$.
(b) $\Delta(G)$ is the continuous image of a compact set, hence a compact subgroup of $(\mathbb R_{>0},\times)$. If it contained some $c\neq1$ it would contain $\{c^k:k\in\mathbb Z\}$, which is unbounded (or accumulates at $0$), contradicting compactness. So $\Delta(G)=\{1\}$. Equivalently: $\det\mathrm{Ad}$ is a bounded multiplicative character on a compact group, so $\equiv1$.

**4.** (a) $g^{-1}dg=\tfrac12 J\,dt+\sum_i E_i\circ dW_i=-\tfrac12E_1\,dt+E_1\circ dW_1+E_2\circ dW_2$. The drift $-\tfrac12E_1$ survives.
(b) $\dot g=g\xi$ with $\xi=-\tfrac12E_1$ gives $\begin{pmatrix}a&b\\0&1\end{pmatrix}\begin{pmatrix}-\tfrac12&0\\0&0\end{pmatrix}=\begin{pmatrix}-a/2&0\\0&0\end{pmatrix}$, i.e. $\dot a=-a/2$, $\dot b=0$. So $a_t=a_0e^{-t/2}$: the scale coordinate decays deterministically, $\mathbb E[\log a_t]$ drifting linearly at rate $-\tfrac12$.
(c) A noise model built to be isotropic in the left-invariant frame — the same construction that on $SO(3)$ or $SE(3)$ is genuinely driftless — is *not* symmetric here. Left Haar is not right Haar, so "uniform" spreading in the left-invariant sense transports mass systematically toward $a\to0$. For a tube: the centre of the distribution separates from the nominal trajectory at a rate linear in $t$, on top of the $\sqrt t$ spread, so any bound that assumed the process was centred on the nominal flow is wrong at first order, not merely loose. Concretely, the drift term must be carried through the generator inequality; dropping it because "Brownian motion has no drift" is the error unimodularity is there to license.
