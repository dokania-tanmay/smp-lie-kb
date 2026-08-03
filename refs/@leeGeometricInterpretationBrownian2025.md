---
tags: [reference, brownian-motion, lie-groups, riemannian-geometry, stochastic-differential-equations, generator]
---
# Geometric Interpretation of Brownian Motion on Riemannian Manifolds (Taeyoung Lee, Gregory S. Chirikjian, arXiv:2510.19991v1 [math.PR], 22 Oct 2025)

Constructs Brownian motion on manifolds from one axiom — *the process whose generator is $\tfrac12\Delta$* — by injecting noise along each axis of an orthonormal frame and then solving for the drift that makes the generator come out right. Three settings are covered uniformly: intrinsic Riemannian manifolds (Thm 4), embedded submanifolds of $\mathbb R^{\bar n}$ (Thm 7), and Lie groups with a left-invariant metric (Thms 5, 8). Both Itô and Stratonovich forms are given in every case, and the Itô–Stratonovich gap is identified with a geometric object each time: $\nabla_{E_i}E_i$ intrinsically, the mean curvature vector $H$ extrinsically, and the adjoint-trace $\sum_i\mathrm{ad}^*_{e_i}e_i$ on a Lie group (zero for unimodular groups).

**Why it matters here.** Theorems 1–3 are the exact tooling the project needs to push a diffusion's generator through a distance function coordinate-free: Theorem 2 gives $\mathcal A f=\tilde X[f]+\tfrac12\sum_i\mathrm{Hess}_f(\sigma_i,\sigma_i)$ — an Itô drift paired with an *intrinsic Hessian*, which is precisely where Hessian comparison (hence curvature, not $\sup|\partial^2 g_{ij}|$) enters. Theorem 5 supplies the Lie-group noise model. Nothing in the paper is about tubes or contraction; it is the geometry layer beneath them.

## Conventions

- **Left invariance throughout.** The metric on $G$ is built by left-translating an inner product $\langle\cdot,\cdot\rangle_{\mathfrak g}$ on $\mathfrak g$: $g(v,w)=\langle g^{-1}v,\,g^{-1}w\rangle_{\mathfrak g}$ (eq. 43). The global frame is $E_i=(L_g)_*e^{\mathfrak g}_i=g e^{\mathfrak g}_i$ (eq. 44). Right-invariant constructions are never used. Remark 4 states explicitly that Thm 5 / Cor 1 are tied to this choice; another metric or frame sends you back to Thm 4.
- **$\mathfrak g^*$ is identified with $\mathfrak g$** via $\langle\cdot,\cdot\rangle_{\mathfrak g}$ (stated in the hypotheses of Thms 5 and 8). So $\mathrm{ad}^*_\xi$ is treated as a map $\mathfrak g\to\mathfrak g$.
- **$\mathrm{ad}^*$ is the plain dual, no sign flip:** $\langle\mathrm{ad}^*_\xi\alpha,\eta\rangle=\langle\alpha,\mathrm{ad}_\xi\eta\rangle$. And $\mathrm{ad}_\xi\eta=[\xi,\eta]$; on a matrix group $[\eta,\xi]=\eta\xi-\xi\eta$. (Many authors put a minus in $\mathrm{ad}^*$; Lee–Chirikjian do not. Downstream signs depend on this.)
- **Hessian sign:** $\mathrm{Hess}_f(X,Y)=g(\nabla_X\mathrm{grad}f,Y)=X[Y[f]]-(\nabla_XY)[f]$ (eq. 12). **Divergence:** $\mathrm{div}X=\mathrm{tr}(Y\mapsto\nabla_YX)$. **Laplacian:** $\Delta f=\mathrm{div}(\mathrm{grad}f)$ — the *analyst's negative-spectrum* sign, so $\Delta$ on $\mathbb R^n$ is $\sum\partial^2_i$.
- **Second fundamental form sign:** Gauss formula $\bar\nabla_{\bar X}\bar Y=\nabla_XY+\mathrm{II}(X,Y)$ (Thm 6, eq. 57), i.e. $\mathrm{II}=$ ambient $-$ intrinsic, normal-valued.
- **Mean curvature vector is the untraced sum**, $H=\sum_{i=1}^n\mathrm{II}(E_i,E_i)$ (eq. 58) — footnote 4 flags that do Carmo's definition carries an extra $\tfrac1n$. Do not import a $\tfrac1n$.
- **$\mathfrak{so}(3)$ hat map:** $\hat x y=x\times y$; vee $\vee$ is its inverse. **Inner product on $\mathfrak{so}(3)$:** $\langle\eta,\xi\rangle_{\mathfrak g}=\tfrac12\mathrm{tr}[\eta^T\xi]=(\eta^\vee)^T(\xi^\vee)$ (eq. 100) — the paper says the factor $\tfrac12$ is chosen to make $\{\hat e_1,\hat e_2,\hat e_3\}$ orthonormal. The induced metric on $T_RSO(3)$ is then $g(V,W)=\tfrac12\mathrm{tr}[V^TW]$, i.e. **the Frobenius metric scaled by $\tfrac12$**.
- Einstein summation is in force; $g$ denotes both the metric and a group element (footnote 1). Stratonovich integrals are defined by the trapezoidal rule (footnote 2).

## Notation

| Symbol | Meaning |
|---|---|
| $X[f]=\mathcal L_Xf=df(X)$ | Lie derivative / directional derivative, eq. (1) |
| $\nabla$ | Levi-Civita connection; $\bar\nabla$ = ambient Euclidean one |
| $\sigma_i$ | diffusion vector fields; $W_i$ independent scalar Wiener processes |
| $X$ vs $\tilde X$ | Stratonovich drift vs Itô drift |
| $\{E_i\}_{i=1}^n$ | orthonormal frame, $g(E_i,E_j)=\delta_{ij}$ |
| $\{e^{\mathfrak g}_i\}_{i=1}^n$ | orthonormal basis of $\mathfrak g$, eq. (42) |
| $P(x):\mathbb R^{\bar n}\to T_xM$ | orthogonal projection, eq. (52); idempotent and symmetric |
| $\{P(x)e_i\}_{i=1}^{\bar n}$ | **pseudo-frame** (Def. 1) — spans $T_xM$ but is neither independent nor orthonormal |
| $\mathrm{II}$, $H$ | second fundamental form, mean curvature vector |
| $J=\sum_i\mathrm{ad}^*_{e^{\mathfrak g}_i}e^{\mathfrak g}_i$ | adjoint-trace vector, eq. (50); Stratonovich Lie-group drift is $\tfrac12J$ |
| $\bar f,\bar X$ | extensions of $f\in C^\infty(M)$, $X\in\mathfrak X(M)$ to $\mathbb R^{\bar n}$ |

## Key definitions

:::info[Definition — Brownian motion]
Brownian motion on $(M,g)$ is the stochastic process whose infinitesimal generator is $\tfrac12\Delta$, $\Delta$ the Laplace–Beltrami operator. Section III-B. This is the *only* axiom; every SDE in the paper is reverse-engineered from it.
:::

:::info[Definition 1 — Pseudo-frame]
For $M^n\subset\mathbb R^{\bar n}$ and $\{e_1,\dots,e_{\bar n}\}$ the standard basis of $\mathbb R^{\bar n}$, the pseudo-frame at $x$ is $\{P(x)e_1,\dots,P(x)e_{\bar n}\}\subset T_xM$ (eq. 62). Redundant ($\bar n>n$) and non-orthonormal, but **globally defined** — that is the point. Proposition 3 shows it still computes traces correctly: $\sum_{i=1}^n\langle E_i,AE_i\rangle=\sum_{i=1}^{\bar n}\langle Pe_i,\bar APe_i\rangle$ (eq. 63).
:::

:::info[Generator is the invariant]
Section II-C: "While a single stochastic process can be described by multiple SDEs, depending on the choice of coordinates or the Itô versus Stratonovich convention, it has a unique generator." Remark 1 makes the operational version: two Itô SDEs built from *different* orthonormal frames differ pathwise but share generator $\tfrac12\Delta$, hence define the same diffusion **in law**. This is prose + a remark, not a numbered theorem.
:::

## Main results

:::tip[Theorem 1 — Itô–Stratonovich conversion on a manifold]
Let $X,\sigma_1,\dots,\sigma_m\in\mathfrak X(M)$ be smooth vector fields, $W_i$ independent scalar Wiener processes. The Stratonovich SDE $dx=X(x)dt+\sum_{i=1}^m\sigma_i(x)\circ dW_i$ (eq. 20) is equivalent to the Itô SDE $dx=\tilde X(x)dt+\sum_i\sigma_i(x)dW_i$ (eq. 21) with
$$\tilde X(x)=X(x)+\frac12\sum_{i=1}^m\nabla_{\sigma_i(x)}\sigma_i(x).\qquad(22)$$
$\nabla$ is Levi-Civita. Proof: $\sigma_i\circ dW_i=\sigma_i dW_i+\tfrac12 d\sigma_i\,dW_i$ with $d\sigma_i=\nabla_{dx}\sigma_i$ and $dW_idW_j=\delta_{ij}dt$. On $M=\mathbb R^1$ the Christoffel symbols vanish and this recovers $\tfrac12\sigma\sigma'$.
:::

:::tip[Theorem 2 — Generator of an SDE on a manifold]
For the Stratonovich SDE (20), the generator $\mathcal A:C^\infty(M)\to C^\infty(M)$ is
$$\mathcal Af=X[f]+\frac12\sum_{i=1}^m\sigma_i[\sigma_i[f]]\qquad(26)$$
and equivalently, in terms of the Itô drift (21)–(22),
$$\mathcal Af=\tilde X[f]+\frac12\sum_{i=1}^m\big\{\sigma_i[\sigma_i[f]]-(\nabla_{\sigma_i}\sigma_i)[f]\big\}=\tilde X[f]+\frac12\sum_{i=1}^m\mathrm{Hess}_f(\sigma_i,\sigma_i).\qquad(27),(28)$$
Proof: Stratonovich chain rule on $df$, convert to Itô, use Cartan's magic formula to get $d(\sigma_i[f])=\sigma_i[df]$, then $\mathbb E[dW]=0$.
:::

:::tip[Theorem 3 — Itô's lemma on a manifold]
If $x$ solves the Itô SDE (21) and $f\in C^\infty(M)$, then
$$df(x)=\Big(\tilde X[f]+\frac12\sum_{i=1}^m\mathrm{Hess}_f(\sigma_i,\sigma_i)\Big)dt+\sum_{i=1}^m\sigma_i[f]\,dW_i.\qquad(31)$$
Proof: covariant Taylor expansion $df=\nabla_{dx}f+\tfrac12\mathrm{Hess}_f(dx,dx)$ (coordinate-invariant, credited to Avramidi), then substitute the Itô SDE. Taking the mean recovers Theorem 2.
:::

:::tip[Proposition 1 — Frame formulas]
For an orthonormal frame $\{E_i\}$: $\mathrm{grad}f=\sum_i(E_i[f])E_i$ (33); $\mathrm{div}X=\sum_i g(\nabla_{E_i}X,E_i)$ (34); $\Delta f=\sum_i\big(E_i[E_i[f]]-(\nabla_{E_i}E_i)[f]\big)=\sum_i\mathrm{Hess}_f(E_i,E_i)$ (35),(36). All three are independent of the choice of orthonormal frame (proof: $O(n)$ change of frame, $R^TR=I$).
:::

:::tip[Theorem 4 — Brownian motion on a Riemannian manifold]
Let $\{E_1,\dots,E_n\}$ be an orthonormal frame on $M$. The Stratonovich SDE
$$dx=-\frac12\sum_{i=1}^n\nabla_{E_i}E_i\,dt+\sum_{i=1}^nE_i\circ dW_i\qquad(39)$$
is equivalent to the **drift-free** Itô SDE
$$dx=\sum_{i=1}^nE_i\,dW_i,\qquad(40)$$
and either has generator $\mathcal Af=\tfrac12\Delta f$; the process is Brownian motion on $M$. Proof: the Stratonovich drift is exactly $-\tfrac12\sum\nabla_{\sigma_i}\sigma_i$, cancelling the Theorem 1 correction; then apply (26) and Proposition 1.
:::

:::tip[Theorem 5 — Brownian motion on a Lie group]
Let $G$ carry the **left-invariant** metric (43) built from $\langle\cdot,\cdot\rangle_{\mathfrak g}$, identify $\mathfrak g^*\cong\mathfrak g$ by that inner product, and let $\{e^{\mathfrak g}_1,\dots,e^{\mathfrak g}_n\}$ be an orthonormal basis of $\mathfrak g$. Then
$$g^{-1}dg=\frac12\sum_{i=1}^n\mathrm{ad}^*_{e^{\mathfrak g}_i}e^{\mathfrak g}_i\,dt+\sum_{i=1}^ne^{\mathfrak g}_i\circ dW_i\qquad(45)$$
is equivalent to the drift-free Itô form $g^{-1}dg=\sum_i e^{\mathfrak g}_i\,dW_i$ (46), and both have generator $\tfrac12\Delta$.

Proof: Koszul formula on left-invariant fields kills the three metric-derivative terms and yields
$$(\nabla_XY)(g)=\tfrac12(L_g)_*\big([\eta,\xi]-\mathrm{ad}^*_\eta\xi-\mathrm{ad}^*_\xi\eta\big),\quad\text{hence}\quad \nabla_{E_i}E_i=-(L_g)_*(\mathrm{ad}^*_{e^{\mathfrak g}_i}e^{\mathfrak g}_i)=-g\,\mathrm{ad}^*_{e^{\mathfrak g}_i}e^{\mathfrak g}_i.\qquad(48)$$
Substituting (48) into (39) gives (45).
:::

:::tip[Corollary 1 — Unimodular case]
If $G$ is **unimodular** — Haar measure both left- and right-invariant, equivalently $\mathrm{tr}[\mathrm{ad}_\eta]=0$ for every $\eta\in\mathfrak g$ — then $J=\sum_i\mathrm{ad}^*_{e^{\mathfrak g}_i}e^{\mathfrak g}_i=0$ and the Stratonovich SDE reduces to $g^{-1}dg=\sum_ie^{\mathfrak g}_i\circ dW_i$ (49).
Proof: $\langle J,\eta\rangle_{\mathfrak g}=\sum_i\langle\mathrm{ad}^*_{e_i}e_i,\eta\rangle=-\sum_i\langle e_i,\mathrm{ad}_\eta e_i\rangle=-\mathrm{tr}[\mathrm{ad}_\eta]$ (eq. 51).
Remark 3 lists the unimodular classes: abelian ($S^1,\mathbb T^n$), compact ($SO(n),SU(n),Sp(n),O(n)$), semisimple ($SL(n,\mathbb R)$, $n\ge2$), nilpotent (Heisenberg $H_n$), Euclidean ($SE(n),E(n)$), $GL(n,\mathbb R)$ — **and any group admitting a bi-invariant metric**. $\mathrm{Aff}(\mathbb R)$ is the running non-unimodular counterexample (§V-G): there $J=-\sqrt2\,e^{\mathfrak g}_1$ and the Stratonovich drift is $-\tfrac{\sqrt2}{2}e^{\mathfrak g}_1$ (eq. 110).
:::

:::tip[Theorem 6 — Gauss formula (quoted, from J.M. Lee)]
For $X,Y\in\mathfrak X(M)$ with extensions $\bar X,\bar Y$: $\bar\nabla_{\bar X}\bar Y=\nabla_XY+\mathrm{II}(X,Y)$, with $\mathrm{II}$ symmetric, bilinear, normal-valued (eq. 57). Proposition 2 adds $X[f]=\bar X[\bar f]$, $\nabla_XY=P(x)(\bar\nabla_{\bar X}\bar Y)$, and $\mathrm{Hess}_f(X,Y)=\mathrm{Hess}_{\bar f}(\bar X,\bar Y)+(\mathrm{II}(X,Y))[f]$ (59)–(61).
:::

:::tip[Theorem 7 — Brownian motion on an embedded manifold]
Let $M^n\subset\mathbb R^{\bar n}$, $\bar n>n$, $\{e_i\}$ the standard basis of $\mathbb R^{\bar n}$, $P(x)$ the orthogonal projection (52). Then
$$dx=-\frac12\sum_{i=1}^{\bar n}\nabla_{P(x)e_i}P(x)e_i\,dt+\sum_{i=1}^{\bar n}P(x)e_i\circ dW_i\qquad(64)$$
is equivalent to the Itô form
$$dx=\frac12H\,dt+\sum_{i=1}^{\bar n}P(x)e_i\,dW_i,\qquad(65)$$
and both have generator $\tfrac12\Delta$. Note the covariant derivative in (64) is the **intrinsic** $\nabla$ on $M$, and the sums run to $\bar n$, so $\bar n$ Wiener processes are needed. Proof: Proposition 3's pseudo-frame trace identity plus the Hessian relation (61); the $\mathrm{II}$-terms cancel $\tfrac12H$ exactly.

Remark 5: the Itô drift $\tfrac12H$ is purely normal, so it does not affect the generator on intrinsic functions — it is exactly the "normal acceleration" that keeps the sample path on $M$.
:::

:::tip[Theorem 8 — Brownian motion on an embedded Lie group]
Additional hypothesis (69): the induced ambient metric is left-invariant, $\langle(L_g)_*\eta,(L_g)_*\zeta\rangle_{\mathbb R^{\bar n}}=\langle\eta,\zeta\rangle_{\mathbb R^{\bar n}}$ for all $\eta,\zeta\in\mathfrak g$ — i.e. left translation acts as a Euclidean isometry. Then
$$g^{-1}dg=\frac12\sum_{i=1}^n\mathrm{ad}^*_{e^{\mathfrak g}_i}e^{\mathfrak g}_i\,dt+\sum_{i=1}^ne^{\mathfrak g}_i\circ dW_i\quad(70)\qquad\Longleftrightarrow\qquad dg=\frac12H\,dt+\sum_{i=1}^n g\,e^{\mathfrak g}_i\,dW_i.\quad(71)$$
Both have generator $\tfrac12\Delta$. The Stratonovich form (70) is *identical* to (45); only the Itô form gains the $\tfrac12H$ drift, because it is written in the ambient space. Remark 6: (69) holds for $O(n),U(n),SO(n),SU(n)$ (and $Sp(n)$ with a symplectically weighted metric), but not in general.
:::

:::tip[Corollary 2 — Embedded unimodular group]
If the embedded $G$ satisfying (69) is also unimodular, then (70)–(71) reduce to
$$g^{-1}dg=\sum_{i=1}^ne^{\mathfrak g}_i\circ dW_i\quad(73),\qquad dg=\frac12H\,dt+\sum_{i=1}^n g\,e^{\mathfrak g}_i\,dW_i\quad(74),$$
with the mean curvature vector computable purely from the **ambient** derivative:
$$H=\sum_{i=1}^n\bar\nabla_{\bar E_i}\bar E_i,\qquad \bar E_i \text{ the extension of } E_i=ge^{\mathfrak g}_i.\qquad(75)$$
Proof: $H=\sum_i(\bar\nabla_{\bar E_i}\bar E_i-\nabla_{E_i}E_i)=\sum_i\bar\nabla_{\bar E_i}\bar E_i+gJ$ by (48), and $J=0$ by unimodularity.
:::

:::warning[Open question — numbering check against the secondary source]
Verified against the PDF: Theorem 1 (Itô–Stratonovich, eq. 22), Theorem 2 (generator, eqs. 26–28), Theorem 4 (Brownian motion on a manifold, eqs. 39–40), Theorem 5 (Lie group, eq. 45 with the identity eq. 48), Corollary 1 (unimodular, eq. 49), Theorem 7 (embedded manifold, mean-curvature Itô drift $\tfrac12H$, eqs. 64–65) — **all six match** the attributions carried by `refs/claude-gen-import/stoch-contraction-RG.tex`.

**One mismatch.** Corollary 2 is *not* "$H=-2R$ on $SO(3)$." Corollary 2 is the general **embedded unimodular group** statement (eqs. 73–75), i.e. $H=\sum_i\bar\nabla_{\bar E_i}\bar E_i$. The result $H=-2R$ is an *example*, §V-F, obtained by applying Corollary 2 to $SO(3)$: with $E_i=R\hat e_i$ and $\bar\nabla_{\bar X}\bar Y=R\eta_x\eta_y$ for left-invariant fields, $H=R\sum_{i=1}^3\hat e_i^2=-2R$ (using $\sum_i\hat e_i^2=-2I_{3\times3}$), giving the Itô SDE $dR=-R\,dt+\sum_iR\hat e_i\,dW_i$ (eq. 105) against the drift-free Stratonovich $dR=\sum_iR\hat e_i\circ dW_i$ (eq. 104). Any citation in the draft of the form "Corollary 2 gives $H=-2R$" should point at **§V-F, eqs. (104)–(105)** instead. Note also that $-2R$ is convention-locked to the $\tfrac12\mathrm{tr}[\eta^T\xi]$ inner product (eq. 100); a different scaling rescales $H$.

Two further attributions worth pinning: the claim that "the generator, not the drift, is the invariant of the diffusion" is **not** part of Theorem 2 — it lives in §II-C prose and Remark 1. And Theorem 6 is the *quoted* Gauss formula, not a contribution.
:::

## What this gives the project

- **Theorem 2 eq. (28) is the entry point for a distance-function argument.** $\mathcal Af=\tilde X[f]+\tfrac12\sum_i\mathrm{Hess}_f(\sigma_i,\sigma_i)$ with $f=\tfrac12 d(\cdot,\bar x)^2$ turns the generator estimate into a Hessian-comparison problem — i.e. a *curvature* bound, exactly the intrinsic replacement for the $\bar m_x,\bar m_{x^2}$ chart constants of [[@daniObserverDesignStochastic2015]]. This is the single most useful result in the paper for the thesis.
- **Theorem 5 fixes the noise model on $G$.** A left-invariant Stratonovich SDE $g^{-1}dg=u\,dt+\sum_ie^{\mathfrak g}_i\circ dW_i$ is Brownian motion *plus* control, with a known drift correction $\tfrac12\sum_i\mathrm{ad}^*_{e_i}e_i$. Both bound types in the thesis need this to say what "isotropic noise" means intrinsically.
- **Corollary 1 is why $SO(3)$ and $SE(3)$ are easy.** Both are unimodular, so the Stratonovich drift vanishes and the noise term is literally $\sum_ie^{\mathfrak g}_i\circ dW_i$. $\mathrm{Aff}(\mathbb R)$ (§V-G) is the counterexample to keep in mind when claiming generality.
- **Theorem 1 is the sign discipline.** Any Itô-form Grönwall argument on $M$ must carry $+\tfrac12\sum\nabla_{\sigma_i}\sigma_i$; getting this wrong flips the curvature-induced drift.
- **Remark 1 / §II-C license frame changes.** Since the generator determines the law, one may pick whatever orthonormal frame makes the distance-function computation cleanest (e.g. a radial frame at $\bar x_t$) without changing the process.
- **Theorem 7 + $\tfrac12H$** is the bridge to ambient-space numerics and to any simulation check of a tube — and it makes explicit that the extra drift is normal, hence invisible to intrinsic functionals like $d(X_t,\bar x_t)$.

## Caveats / limitations

- **Only Brownian motion, only $\tfrac12\Delta$.** The paper constructs the *driftless isotropic* diffusion. General controlled/anisotropic SDEs are covered only by Theorems 1–3; the design results (4,5,7,8) assume noise injected along an orthonormal frame with unit intensity. Rescaling to $\sigma^2\Delta$ or anisotropic diffusion is not carried out.
- **Left-invariance is a standing assumption**, not a derived fact (Remark 4). Nothing here covers right-invariant or non-invariant metrics on $G$, nor bi-invariance failure on $SE(3)$ — which is precisely where the project expects trouble.
- **Theorem 8 needs the extra compatibility (69)**, which fails for $\mathrm{Aff}(\mathbb R)$ and is not automatic for embedded groups.
- **Theorem 4's frame is generally only local.** The paper is candid that a global orthonormal frame need not exist; Theorem 7 (pseudo-frame, $\bar n$ Wiener processes) and Theorem 5 (left-translated basis) are the two escapes.
- **Regularity is left informal.** The Itô calculus rules (18) are described by the authors as "shorthand … understood to hold in a mean-square sense"; no completeness, non-explosion, or $C^2$-of-$d$ hypotheses are stated. For distance functions, cut locus regularity is *not* addressed anywhere — the project has to supply that itself.
- The proofs are self-contained but elementary; for a measure-theoretic treatment the paper defers to [[@hsuStochasticAnalysisManifolds2002]]. The $SO(3)$ "pinning drift" comparison is with [[@piggottGeometricEulerMaruyamaSchemes2016]].
- Extraction note: the LaTeX of eq. (48) and the Koszul expansion came out of `pdftotext` cleanly and were cross-checked for consistency (setting $X=Y$ in (48) reproduces the sign in (45), and (45)+(39) reproduce Corollary 1's $-\mathrm{tr}[\mathrm{ad}_\eta]$). No constant in this file is a guess.
