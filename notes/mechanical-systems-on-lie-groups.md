---
tags: [mechanics, symplectic, control, lie-groups]
---
# Mechanical Systems on Manifolds / Lie Groups

My own notes. Companion files: [[riemannian-geometry]], [[probability-on-manifolds]].

## Geometric control of mechanical systems

- **Hamiltonian systems**: symplectic or Poisson geometry dominates.
- **Lagrangian systems**: less clear on what the correct structure is.

Mechanical systems have a metric that can be used to define an affine connection — the Levi-Civita connection of the kinetic energy metric. Unforced motion is then geodesic motion and control forces appear on the right-hand side.

This is the bridge: the mechanics *supplies* the metric, so it is not an arbitrary choice. On a Lie group the kinetic-energy metric is left-invariant when the inertia is body-fixed.

## Differential forms

A differential form is a special kind of tensor field that has the alternating property and only acts on vectors.

A differential $k$-form is a special kind of $(0,k)$-tensor that is antisymmetric (or alternating) — swap two elements and it changes sign. It also forms a vector space and can be represented in a basis of $(0,k)$-tensors obtained from the basis elements of the vector space.

A $k$-form is evaluated over a $k$-dimensional oriented manifold. One can construct a basis for $k$-forms using the exterior product over basis elements of the vector space $k$ times. *The dimensionality of the spaces increases and decreases with $k$.*

**A metric is not a two-form**, as it is not alternating.

### Wedge / exterior product

$\wedge$: $v_1 \wedge v_2$ denotes the parallelogram area captured by the two vectors. It is a bilinear operator and skew-symmetric. Interestingly enough, the space obtained from exterior products is also a vector space; for $\mathbb R^3$ it can be identified with itself.

### Stokes' theorem

The generalization of the fundamental theorem of calculus. *Total change on the outside is the sum of little changes on the inside.* Integration and derivatives are not opposite operations, but rather the integration set changes: integration of the derivative of a function on a set is the same as integration of the function on the boundary of the set.

## Exterior derivative

Suppose a differential form is defined as $\omega = f dx^{I} \in \Omega^k (M)$, where $f\in C^{\infty} (M) =\Omega^0(M)$ and $dx^I$ denotes an ordered set of indices over which the wedge product is taken. Then

$$
d \omega = \sum_{i=1}^n \frac{\partial f}{\partial x^i} dx^i \wedge dx^I \in \Omega^{k+1}(M)
$$

This can be extended to general $k$-forms using linearity. **This is a coordinate-dependent definition, but the object obtained is not.**

A smooth function is a $0$-form that is evaluated on a point. The differential of a function is a $1$-form that is evaluated on a line.

$d^2 = 0$, and $d$ needs no metric and no connection — so the closedness condition $d\omega = 0$ below is a purely smooth-structure condition.

## Symplectic form

A symplectic 2-form on a manifold is defined as $\omega = \omega_{ij}dx^i \wedge dx^j$. This is a representation in a local chart. For every pair of covectors there is an entry, so effectively it is a skew-symmetric matrix.

A skew-symmetric matrix can be full rank in even-dimensional spaces. The even-dimensional space that we consider is the **cotangent bundle**.

Non-degeneracy is what turns $dH$ into a vector field: $\iota_{X_H}\omega = dH$. That is Hamilton's equations, coordinate-free.

:::warning[Open question]
Where do the Lie group and the symplectic structure interact? $T^*G \cong G\times\mathfrak g^*$ by left trivialization — does the canonical $\omega$ stay canonical in those coordinates, or pick up structure constants?
:::

## Tautological one-form

A 1-form on $M$ is a mapping $M \to T^*M$ (a covector field).

Given a map $\phi : M \to N$, then

- $d\phi : TM \to TN$
- $d\phi^* : T^*N \to T^*M$, defined as $d\phi^*(n^*)(\cdot) = n^* \cdot d\phi(\cdot)$

Now consider $\pi : T^*Q \to Q$; then $d\pi^* : T^*Q \to T^*(T^*Q)$. This defines a one-form on $T^*Q$ and hence is the tautological one-form.

A one-form acts on vectors and gives a real number. So for an element of $T_{(q,p)}(T^*_qQ)$ which is $((q,p),(v,\hat p))$, it gives $\langle p, v\rangle$.

It is the only canonical 1-form on a cotangent bundle — no choices made — and $\omega = -d\theta$ gives the canonical symplectic form.

## Double tangent bundle

:::warning[Open question]
How do vector fields on $TG$ translate to a second-order ODE on $TTG$?
:::

:::warning[Open question]
How does the curvature of $TG$ in the Sasaki metric look?
:::
