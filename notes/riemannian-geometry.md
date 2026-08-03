---
tags: [riemannian, lie-groups, foundations]
---
# Riemannian Geometry

My own notes on the geometric background. Companion files: [[probability-on-manifolds]], [[mechanical-systems-on-lie-groups]].

## Structure hierarchy

A manifold is a second countable Hausdorff space that is locally homeomorphic to a Euclidean space.

*A manifold need not have a constant dimension. If the charts are diffeomorphic, we get additional structure, which is often our interest.*

From the definition of a smooth **manifold**, certain structures are defined — **no metric and no connection needed**:

- Tangent vectors — *equivalence class of curves which map to the same derivative under charts.*
- Vector fields — *a derivation: maps a function to a function, directionally.*
- Differential forms
- Lie brackets of vector fields
- Tensors
- Directional derivatives of functions

Additional structure can stem from:

- Lie groups
- Connection
- Riemannian metric
- Homogeneous manifolds

Each of these is an extra **choice**. The whole difficulty of this project is that a Lie group admits several at once and **they need not agree** — see [[#Exp and log two sources]].

## Groups

:::info[Definition]
Group is a set $G$ with an operation $(\cdot)$ that satisfies:
1. Associativity: $(a\cdot b) \cdot c = a \cdot ( b \cdot c) \ \forall a,b,c \in G$
2. Identity: $\exists e \in G : a \cdot e = e \cdot a = a \ \forall a \in G$
3. Inverse: $\forall a \in G: \exists b \in G : b \cdot a = a \cdot b = e$
4. Closure: $a\cdot b \in G \ \forall a,b \in G$

Uniqueness of inverse and identity follows from the axioms.
:::

A **Lie group** is a group that is also a smooth manifold, with multiplication and inversion smooth.

Working assumption throughout: **matrix Lie groups first**, then homogeneous manifolds, then general Riemannian manifolds.

## Lie bracket

:::info[Definition]
A **Lie Bracket** is defined for a smooth manifold:
$$
[X, Y] f = X(Y f) - Y (X f),\quad \forall\ f \in C^{\infty}(M)
$$
This requires seeing vector fields as derivations of functions.
Additionally, this definition only requires the smoothness of the vector fields.
:::

Key point: **no connection and no metric are involved.** Contrast with $\nabla_X Y$, which needs a connection choice. The two are linked by torsion, $T(X,Y) = \nabla_X Y - \nabla_Y X - [X,Y]$; torsion-free means $\nabla_X Y - \nabla_Y X = [X,Y]$.

On a Lie group, the bracket of left-invariant vector fields gives the Lie algebra bracket — for matrix groups, the commutator $AB - BA$.

## Connections

:::info[Definition]
A **connection** (affine/linear on $TM$) is an $\mathbb R$-bilinear map $\nabla: \mathfrak X (M) \times \mathfrak X (M) \to \mathfrak X(M)$, $(X,Y)\to \nabla_X Y$. It satisfies:
- $C^{\infty}(M)$-linear in $X$ : $$\nabla_{fX} Y = f \nabla_X Y$$
- Leibniz in $Y$ : $$\nabla_X (fY) = X(f) Y + f \nabla_X Y$$
:::

The asymmetry between the slots is the whole content:

- $C^\infty$-linear in $X$ ⟹ $\nabla_X Y|_p$ depends only on $X_p$, the *value* at the point;
- Leibniz in $Y$ ⟹ it depends on how $Y$ *changes* along $X$.

**A connection has more degrees of freedom than a metric. Even making it torsion-free does not guarantee that it is the Levi-Civita connection of any metric.** The implication runs one way only:

$$\text{metric} \implies \text{connection}, \qquad \text{connection} \not\implies \text{metric}$$

## Left-invariant metrics

:::info[Definition]
A Riemannanian metric $\braket{}$ on a Lie Group $G$ is called **left-invariant** if
$$
\braket{u,v}_p = \braket{(dL_h)_p u, (dL_h)_p v},
$$
here, $(dL_h)_g : T_g G \to T_{hg}G$ is a linear isomorphism. In pullback notation, written as: $L_h^* \braket{} = \braket{}, \forall h \in G.$ The diffeomorphism $L_h$ is an isometry of $(G, \braket{})$ for every $h.$
:::

Consequence: a left-invariant metric is determined entirely by an inner product on $\mathfrak g = T_e G$, transported by $dL_h$. So choosing a metric on $G$ is choosing a positive-definite operator on the Lie algebra.

**Bi-invariant** = invariant under both $L_h$ and $R_h$. Exists iff $\mathfrak g$ carries an $\mathrm{Ad}$-invariant inner product — true for compact groups ($SO(3)$), false for $SE(3)$.

## Exp and log: two sources

Exponential or Log map stems from two sources:

1. **Lie exponential**: *When working with Lie groups, we can define left-invariant vector fields. Flow along this vector field can also be defined, which leads to a map from the tangent space to the manifold.* No metric involved. For matrix groups this is the matrix exponential.
2. **Connection**: *One can define the covariant derivative, which can be used to define geodesics.* As a Riemannian metric induces a connection, one can define the Riemannian exponential.

**They need not agree in general. When there's no bi-invariant metric, the matrix exponential differs from the Riemannian exponential of any left-invariant metric.**

Why this matters here: the group-theoretic mean uses $\log(\mu^{-1}g)$ while the Fréchet/Karcher mean uses $\log_\mu(g)$ (see [[probability-on-manifolds]]); a distance built from one is not the distance built from the other; and any coordinate-invariance claim must say **which** log is meant.

:::warning[Open question]
For $SE(3)$ with a left-invariant metric: how far apart are the two exponentials, quantitatively? Is there a bound in terms of the failure of $\mathrm{Ad}$-invariance?
:::

## Homogeneous manifolds *can* have different connections

A homogeneous manifold is a manifold with a transitive group action and therefore one can define a tangent map from any element to any other element. However, **this map is not unique.**

Connection is fundamentally an infinitesimal structure that is path dependent. However, as this defines a normal coordinate chart, one can define the connection such that the normal vectors are orthogonal. This is mentioned in Remark 6.1 of [[@goorEquivariantFilterEqF2023]], which also discusses different works that account for curvature correction.

## Bundles

Fiber, principal, vector, frame, tangent.

### Fiber bundle

Generalization of the *Cartesian Product*. Locally a product space, globally maybe not. It requires: total space $E$, base space $B$, fiber $F$, and bundle projection $\pi : E \to B$ (continuous, surjective). When $E = B \times F$ it is a **trivial bundle**.

:::info[Definition]
To define a fiber bundle, one needs the total space $E$, base space $B$, fiber $F$ and a bundle projection map: $\pi : E \to B$.
Every $x \in B$, there is an open "trivializing" neighbourhood $U\subset B$, such that there exists a homeomorphism $\phi : \pi^{-1} (U) \to U \times F$, in a way that $\pi$ agrees with the projection onto the first factor.
:::

A **section** is a *smooth inverse of the projection*: $s : B \to E$ with $\pi \circ s = \mathrm{id}$. A vector field is a section of $TM$.

A **vector bundle** is a fiber bundle whose fibers are vector spaces.

### Torsor

(Principal homogeneous space) for a group $G$ is a homogeneous manifold on which the group acts

- **transitively** — there exists an action that can move from anywhere to anywhere (implies group dim $\ge$ manifold dim), and
- **freely** — the only group action leaving a point unchanged is the identity (implies group dim $\le$ manifold dim).

*A torsor is a group that has forgotten its identity element.* One can define right and left torsors.

### Principal bundle $P$

Generalizes the *Cartesian Product* of a group $G$ and a topological space $X$. (A topological space has the notion of closeness defined — popularly using open sets — without requiring a way to measure distances.) Additional property:

1. Fibers are $G$-torsors: the fibers are preserved by the group action, i.e. the group action does not change the base projection.

The two properties in play are *closure* and *homogeneity* of the group action on a fiber.

### Frame bundle

Associated with a vector bundle $E$, denoted $F(E)$. For a point on the base space, one associates a basis of the vector space. This basis can be acted on by $GL(k,\mathbb R)$ — all invertible $k \times k$ matrices — and the fiber is a $GL(k,\mathbb R)$-torsor.

Choosing a metric reduces the structure group to $O(k)$ (orthonormal frames).

## Parallel transport

Move vectors of the manifold along curves such that they remain parallel wrt the connection. Given a curve $\gamma:[0,1]\to M$, transport solves $\nabla_{\dot\gamma}X = 0$.

A vector field $X$ is called *parallel* if for any vector field $Y$, $\nabla_Y X = 0$.

- The covariant derivative only depends on the value of $Y$ at that point, not its derivative, and depends on $X$'s value and how it changes along $Y$.
- Parallel vector fields exist for flat spaces, as it is an over-determined condition for curved spaces.
- Parallel transport around a closed loop of an orthonormal frame returns a rotated orthonormal frame (the connection is compatible with the metric and curvature is non-zero).
- A **parallel frame** is a collection of parallel vector fields $\{E_i\}$ spanning the tangent space. To show it is a parallel frame it suffices to show $\nabla_{E_j}E_i = 0\ \forall i,j$ for a spanning frame, as the connection is linear over $C^\infty(M)$ in the subscript slot.
- Suppose we have an orthonormal frame; if the set where the mutual covariant derivatives vanish is an open set, then the manifold has $0$ curvature there.

## Normal coordinates

The identification of $T_pM$ with $\mathbb R^n$ leads to a definition of coordinates through the Riemannian exponential map. This can be used to define a frame around $p$ at $q = \exp_p v$, using $d\exp_p : T_vT_pM \to T_{\exp_p(v)}M$, i.e. $d\exp_p : T_pM \to T_qM$.

One can also define parallel orthonormal frames this way. **But these frames don't retain the property that the covariant derivative vanishes — this property holds only at the point.** In normal coordinates $\Gamma^k_{ij}(p)=0$ and $\partial_k g_{ij}(p)=0$, but the *second* derivatives of $g$ at $p$ are curvature and cannot be removed.

This is exactly the obstruction that makes curvature-correction terms appear in generator computations on manifolds.

## Isometries

:::info[Definition]
A map between two Riemannian manifolds $f:(M,g)\to (N,h)$ is called an **isometry** if it preserves the metric, i.e., the following holds
$$
     \langle df_p v, df_p w \rangle_{h,{f(p)}} = \langle v, w\rangle_{g , p}
$$
:::

For a Riemannian metric one can define an exponential map that uses geodesics, which are defined using ODEs and covariant derivatives. Isometries map geodesics to geodesics, hence commute with $\exp$: $f(\exp_p v) = \exp_{f(p)} df_p v$. That identity is why left-invariance buys coordinate-invariant statements.

## Gauss lemma

:::tip[Theorem]
**Gauss Lemma**: The exponential map is a radial isometry, i.e.,
$$
\langle d (\exp_p)_v \tilde v, d (\exp_p)_v \tilde w \rangle_{g, \exp_p v} = \langle v, w \rangle_{g, p}
$$
It is important to note that the term $v$ is common. Additionally, $d(\exp_p)_v : T_v T_p M \to T_p M$. To make the distinction clear $\tilde v, \tilde w \in T_v T_p M$.
:::

"Radial" is the whole point: one argument must be the radial direction $v$. $\exp_p$ is **not** an isometry in general — it preserves the radial component and orthogonality to it, and transverse distortion is what Jacobi fields and curvature measure.

Why it is the workhorse: it makes $r(x) = d(p,x)$ satisfy $\|\nabla r\| = 1$, which is what lets a distance function be fed into a generator computation.
