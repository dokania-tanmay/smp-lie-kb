---
tags: [lie-groups, haar-measure, unimodularity, stochastics]
---
# Unimodularity

**Prereq:** [[01-adjoint-and-coadjoint]], [[probability-on-manifolds]] (§ Haar measure — left/right Haar, and *unimodular = the two coincide*, are assumed known)
**Goal:** turn "left Haar $=$ right Haar" into the algebraic test $\mathrm{tr}\,\mathrm{ad}_\eta=0$, and from there into the identity $\sum_i\mathrm{ad}^*_{e_i}e_i=0$ that deletes the drift from Brownian motion on $G$.

## Definitions

:::info[Definition]
Fix a left Haar measure $\mu$ on $G$ ($\mu(hA)=\mu(A)$, the $dg$ of [[probability-on-manifolds]]). For fixed $h$, the measure $A\mapsto\mu(Ah)$ is again left-invariant, so by uniqueness of left Haar up to scale there is a number $\Delta(h)>0$ with

$$\mu(Ah)=\Delta(h)\,\mu(A)\qquad\text{for all measurable }A .$$

$\Delta:G\to(\mathbb R_{>0},\times)$ is the **modular function**. It is a continuous homomorphism: $\mu(Ah_1h_2)=\Delta(h_2)\Delta(h_1)\mu(A)$. It does not depend on which left Haar measure was chosen, since rescaling $\mu$ cancels.

*Convention.* Some texts define $\Delta$ as the reciprocal of this. The only statement used downstream is $\Delta\equiv1$, which is convention-free — but the formula $\Delta=|\det\mathrm{Ad}|^{-1}$ below is not, so do not mix sources.
:::

:::info[Definition]
$G$ is **unimodular** if $\Delta\equiv1$, equivalently if some (hence every) left Haar measure is also right-invariant.
:::

## The equivalences

:::tip[Theorem]
For a connected matrix Lie group $G$ with Lie algebra $\mathfrak g$, the following are equivalent.

1. Left Haar measure is right-invariant.
2. $\Delta(h)=1$ for all $h\in G$.
3. $|\det\mathrm{Ad}_h|=1$ for all $h\in G$.
4. $\mathrm{tr}\,\mathrm{ad}_\eta=0$ for all $\eta\in\mathfrak g$.
:::

**(1) $\Leftrightarrow$ (2)** is the definition: $\mu(Ah)=\mu(A)$ for all $A,h$ says exactly $\Delta\equiv1$.

**(2) $\Leftrightarrow$ (3).** Identify $\mu$ near $e$ with a left-invariant volume form, i.e. with Lebesgue measure on $\mathfrak g$ transported by $\exp_G$ (Lie exponential — see [[notation]]) and then left-translated. Right translation by $h$ read in this trivialization is conjugation, $g\mapsto h^{-1}gh$ followed by a left translation, and conjugation differentiates at $e$ to $\mathrm{Ad}_{h^{-1}}$. A linear map scales Lebesgue measure by $|\det|$, so $\Delta(h)=|\det\mathrm{Ad}_{h^{-1}}|=|\det\mathrm{Ad}_h|^{-1}$.

**(3) $\Leftrightarrow$ (4).** $\mathrm{Ad}_{\exp_G(t\eta)}=e^{t\,\mathrm{ad}_\eta}$, so $\det\mathrm{Ad}_{\exp_G(t\eta)}=e^{t\,\mathrm{tr}\,\mathrm{ad}_\eta}$ and hence

$$\Delta(\exp_G(t\eta))=e^{-t\,\mathrm{tr}\,\mathrm{ad}_\eta}.$$

If $\mathrm{tr}\,\mathrm{ad}_\eta=0$ for every $\eta$ then $\Delta=1$ on the image of $\exp_G$, which generates $G$ when $G$ is connected, and $\Delta$ is a homomorphism, so $\Delta\equiv1$. Conversely $\Delta\equiv1$ forces $\tfrac{d}{dt}\big|_{0}\Delta(\exp_G(t\eta))=-\mathrm{tr}\,\mathrm{ad}_\eta=0$. Connectedness is used only in the "generates $G$" step; for disconnected $G$, (4) controls the identity component only. $\square$

## From $\mathrm{tr}\,\mathrm{ad}=0$ to $\sum_i\mathrm{ad}^*_{e_i}e_i=0$

This is the step that gets used, and the one where the metric enters. Let $\langle\cdot,\cdot\rangle_{\mathbb I}$ be an inner product on $\mathfrak g$ with $\{e_i\}_{i=1}^n$ orthonormal, and $\mathbb I:\mathfrak g\to\mathfrak g^*$ the induced flat map.

Note first that $\mathrm{ad}^*_{e_i}e_i$ is an abuse: $\mathrm{ad}^*_\xi$ eats elements of $\mathfrak g^*$, not $\mathfrak g$. What is meant is $\mathrm{ad}^*_{e_i}(\mathbb I e_i)$, pulled back to $\mathfrak g$ — that is, the metric adjoint $\widetilde{\mathrm{ad}}_\xi=\mathbb I^{-1}\mathrm{ad}^*_\xi\mathbb I$ of [[notation]]. So define

$$J \;:=\; \sum_{i=1}^n \widetilde{\mathrm{ad}}_{e_i}e_i \;=\; \mathbb I^{-1}\sum_{i=1}^n\mathrm{ad}^*_{e_i}(\mathbb I e_i) \;\in\;\mathfrak g .$$

:::tip[Proposition]
$\langle J,\eta\rangle_{\mathbb I}=-\mathrm{tr}\,\mathrm{ad}_\eta$ for every $\eta\in\mathfrak g$. Hence $G$ unimodular $\iff J=0$, and $J$ is independent of which orthonormal basis is used.
:::

*Proof.* Unfolding the pairing (plain dual, no sign flip — [[notation]]) and then antisymmetry of the bracket,

$$\langle J,\eta\rangle_{\mathbb I}=\sum_i\langle\mathrm{ad}^*_{e_i}(\mathbb I e_i),\eta\rangle=\sum_i\langle\mathbb I e_i,[e_i,\eta]\rangle=\sum_i\langle e_i,[e_i,\eta]\rangle_{\mathbb I}=-\sum_i\langle e_i,\mathrm{ad}_\eta e_i\rangle_{\mathbb I}=-\mathrm{tr}\,\mathrm{ad}_\eta .$$

The last equality is where orthonormality is used: $\sum_i\langle e_i,Ae_i\rangle_{\mathbb I}=\mathrm{tr}\,A$ holds for an orthonormal basis and not otherwise. $\square$

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

Cross-check against Haar directly, in coordinates $g=(a,b)$ with $(a_1,b_1)(a_2,b_2)=(a_1a_2,\,a_1b_2+b_1)$: left translation has Jacobian $h_a^2$ and right translation Jacobian $h_a$, so $d\mu_L=\dfrac{da\,db}{a^2}$ but $d\mu_R=\dfrac{da\,db}{a}$. They differ; $\Delta(h)=1/h_a$, and indeed $\mathrm{Ad}_{(a,b)}=\begin{pmatrix}1&0\\-b&a\end{pmatrix}$ has $\det=a$, matching $\Delta=|\det\mathrm{Ad}|^{-1}$.

*Convention note.* [[@leeGeometricInterpretationBrownian2025]] §V-G reports $J=-\sqrt2\,e_1$. That is the same computation with $\langle\eta,\zeta\rangle=\tfrac12\mathrm{tr}(\eta^\top\zeta)$, whose orthonormal basis is $e_i=\sqrt2E_i$; then $[e_1,e_2]=\sqrt2 e_2$ and $\mathrm{tr}\,\mathrm{ad}_{e_1}=\sqrt2$. Exactly the metric-dependence flagged above.

## Why it matters

:::tip[Corollary]
[[@leeGeometricInterpretationBrownian2025]] Theorem 5 (eq. 45) gives Brownian motion on $G$ with a left-invariant metric, in Stratonovich form,

$$g^{-1}dg=\tfrac12\sum_i\mathrm{ad}^*_{e_i}e_i\,dt+\sum_i e_i\circ dW_i=\tfrac12 J\,dt+\sum_i e_i\circ dW_i .$$

If $G$ is unimodular then $J=0$ and this collapses to the drift-free $g^{-1}dg=\sum_i e_i\circ dW_i$ ([[@leeGeometricInterpretationBrownian2025]] Corollary 1, eq. 49). $\square$
:::

$J$ is not an artifact of the stochastic calculus: by the Koszul formula for a left-invariant metric (lesson 03), $\nabla_{E_i}E_i=-g\,\widetilde{\mathrm{ad}}_{e_i}e_i$, so $J$ is precisely $-\sum_i\nabla_{E_i}E_i$ — the failure of the left-translated orthonormal frame to be geodesic. Lesson 21 does the stochastics; this lesson supplies the algebraic hypothesis that makes it vanish, and it holds for $SO(3)$ and $SE(3)$, which is why those two are easy.

:::warning[Open question]
$\mathrm{tr}\,\mathrm{ad}=0$ is metric-free, but the *bound* it feeds is not: for non-unimodular $G$ the drift $\tfrac12\mathbb I^{-1}\chi$ inherits $\mathbb I$, and its size is exactly the sort of metric-dependent constant the thesis wants out of tube estimates. What is the intrinsic statement — is $\|\chi\|$ measured in $\mathbb I^{-1}$ the honest constant, or does it recombine with curvature?
:::

## Problems

1. **Recall.** Without looking: define the modular function $\Delta$, state the four equivalent conditions of the Theorem, and write $J$ in terms of $\mathrm{ad}^*$ and of $\widetilde{\mathrm{ad}}$. Say precisely where an inner product is needed and where it is not.
2. **Compute.** On $\mathfrak{se}(3)$, with $\eta=(\omega,v)$ and $[(\omega,v),(\omega',v')]=(\omega\times\omega',\ \omega\times v'-\omega'\times v)$, write the $6\times6$ matrix of $\mathrm{ad}_{(\omega,v)}$ in $\{(\omega',v')\}$ coordinates and compute its trace. Conclude $J=0$ for **every** left-invariant metric on $SE(3)$ — including the ones that are not bi-invariant.
3. **Prove.** (a) Show $\mathrm{tr}\,\mathrm{ad}_{[\xi,\eta]}=0$ for all $\xi,\eta$, and deduce that $[\mathfrak g,\mathfrak g]=\mathfrak g$ implies unimodular. (b) Show that a compact $G$ is unimodular, using only that $\Delta:G\to(\mathbb R_{>0},\times)$ is a continuous homomorphism.
4. **Break it.** On $\mathrm{Aff}(\mathbb R)$ with $\{E_1,E_2\}$ orthonormal as above, $J=-E_1$. (a) Write the Stratonovich SDE for Brownian motion and identify the surviving drift. (b) Integrate the drift alone: solve $\dot g=g\cdot(\tfrac12 J)$ in coordinates $(a,b)$. (c) Say what this means dynamically for a "driftless, isotropic" noise model on a non-unimodular group, and what it does to a tube drawn around a nominal trajectory.

---

## Solutions

**1.** $\mu(Ah)=\Delta(h)\mu(A)$ for a left Haar $\mu$; conditions (1)–(4) of the Theorem. $J=\sum_i\widetilde{\mathrm{ad}}_{e_i}e_i=\mathbb I^{-1}\sum_i\mathrm{ad}^*_{e_i}(\mathbb I e_i)$. Metric-free: $\Delta$, $\det\mathrm{Ad}$, $\mathrm{tr}\,\mathrm{ad}$, the functional $\chi=-\mathrm{tr}\,\mathrm{ad}\in\mathfrak g^*$, and the statement $\chi=0$. Metric-dependent: the orthonormal basis $\{e_i\}$, the identification $\mathfrak g^*\cong\mathfrak g$, and the vector $J=\mathbb I^{-1}\chi$ itself.

**2.** The first component of the bracket is $\hat\omega\omega'$; the second is $\omega\times v'-\omega'\times v=\hat\omega v'+\hat v\omega'$. Hence

$$\mathrm{ad}_{(\omega,v)}=\begin{pmatrix}\hat\omega&0\\ \hat v&\hat\omega\end{pmatrix},\qquad \mathrm{tr}=2\,\mathrm{tr}\,\hat\omega=0 .$$

So $\chi=0$, and since $J=\mathbb I^{-1}\chi$ this gives $J=0$ for *any* $\mathbb I$ — the conclusion is independent of the metric even though $J$'s definition is not. $SE(3)$ therefore has drift-free Brownian motion despite admitting no bi-invariant metric.

**3.** (a) $\mathrm{ad}$ is a Lie algebra homomorphism (Jacobi identity), so $\mathrm{ad}_{[\xi,\eta]}=\mathrm{ad}_\xi\mathrm{ad}_\eta-\mathrm{ad}_\eta\mathrm{ad}_\xi$, whose trace is $0$ by $\mathrm{tr}(AB)=\mathrm{tr}(BA)$. So the functional $\chi$ annihilates $[\mathfrak g,\mathfrak g]$; if that equals $\mathfrak g$ then $\chi=0$.
(b) $\Delta(G)$ is the continuous image of a compact set, hence a compact subgroup of $(\mathbb R_{>0},\times)$. If it contained some $c\neq1$ it would contain $\{c^k:k\in\mathbb Z\}$, which is unbounded (or accumulates at $0$), contradicting compactness. So $\Delta(G)=\{1\}$. Equivalently: $\det\mathrm{Ad}$ is a bounded multiplicative character on a compact group, so $\equiv1$.

**4.** (a) $g^{-1}dg=\tfrac12 J\,dt+\sum_i E_i\circ dW_i=-\tfrac12E_1\,dt+E_1\circ dW_1+E_2\circ dW_2$. The drift $-\tfrac12E_1$ survives.
(b) $\dot g=g\xi$ with $\xi=-\tfrac12E_1$ gives $\begin{pmatrix}a&b\\0&1\end{pmatrix}\begin{pmatrix}-\tfrac12&0\\0&0\end{pmatrix}=\begin{pmatrix}-a/2&0\\0&0\end{pmatrix}$, i.e. $\dot a=-a/2$, $\dot b=0$. So $a_t=a_0e^{-t/2}$: the scale coordinate decays deterministically, $\mathbb E[\log a_t]$ drifting linearly at rate $-\tfrac12$.
(c) A noise model built to be isotropic in the left-invariant frame — the same construction that on $SO(3)$ or $SE(3)$ is genuinely driftless — is *not* symmetric here. Left Haar is not right Haar, so "uniform" spreading in the left-invariant sense transports mass systematically toward $a\to0$. For a tube: the centre of the distribution separates from the nominal trajectory at a rate linear in $t$, on top of the $\sqrt t$ spread, so any bound that assumed the process was centred on the nominal flow is wrong at first order, not merely loose. Concretely, the drift term must be carried through the generator inequality; dropping it because "Brownian motion has no drift" is the error unimodularity is there to license.
