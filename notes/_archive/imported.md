Structure hierarchy

```ad-def
Group is a set $G$ with an operation $(\cdot)$ that satisfies:
1. Associativity: $(a\cdot b) \cdot c = a \cdot ( b \cdot c) \ \forall a,b,c \in G$
2. Identity: $\exists e \in G : a \cdot e = e \cdot a = a \ \forall a \in G$
3. Inverse: $\forall a \in G: \exists b \in G : b \cdot a = a \cdot b = e$
4. Closure: $a\cdot b \in G \ \forall a,b \in G$
   
Uniqueness of inverse and identity follows from the axioms.
```

A manifold is second countable Hausdorff space that is locally homeomorphic to a Euclidean space.
*A manifold need not have a constant dimension. If the charts are diffeomorphic, we get additional structure, which is often our interest.*

From the definition of a smooth **manifold**, certain structures are defined:
- Tangent vectors - *Equivalence class of curves which map to same derivative under charts.*
- Vector fields - *Maps a function to a function as dirc*
- Differential forms
- Lie brackets of vector fields
- Tensors
- Directional derivatives of functions



Additional structure can stem from:
- Lie groups
- Connection
- Riemannian metric
- Homogeneous manifolds

Exponential or Log map stems from two sources:
1. Lie Exponential: *When working with Lie groups, we can define left-invariant vector fields. Flow along this vector field can also be defined, which leads to a map from tangent space to the manifold.*
2. Connection: *One can define the covariant derivative, which can be used to define geodesics.*
As a Riemannian metric induces a connection, one can define Riemannian exponential.
They need not agree in general. When there's no bi-invariant metric, the matrix exponential differs from Riemannian exponential of any left-invariant metric.

```ad-def
A Riemannanian metric $\braket{}$ on a Lie Group $G$ is called **left-invariant** if
$$
\braket{u,v}_p = \braket{(dL_h)_p u, (dL_h)_p v},
$$
here, $(dL_h)_g : T_g G \to T_{hg}G$ is a linear isomorphism. In pullback notation, written as: $L_h^* \braket{} = \braket{}, \forall h \in G.$ The diffeomorphism $L_h$ is an isometry of $(G, \braket{})$ for every $h.$
```

A connection has more degrees of freedom, even making it torsion-free does not guarantee that it is the Levi-Civita connection of any metric.

```ad-def
A **connection** (affine/linear on $TM$) is an $\mathbb R$-bilinear map $\nabla: \mathfrak X (M) \times \mathfrak X (M) \to \mathfrak X(M)$, $(X,Y)\to \nabla_X Y$. It satisfies:
- $C^{\infty}(M)$-linear in $X$ : $$\nabla_{fX} Y = f \nabla_X Y$$
- Leibniz in $Y$ :$$\nabla_X (fY) = X(f) Y + f \nabla_X Y$$
```

```ad-def
A **Lie Bracket** is defined for a smooth manifold:
$$
[X, Y] f = X(Y f) - Y (X f),\quad \forall\ f \in C^{\infty}(M)
$$
This requires seeing vector fields as derivation of functions.
Additionally, this definition only requires the smoothness of the vector fields. 
```

#### Homogeneous manifold *can* have different connections
A homogeneous manifold is a manifold with a transitive group action and therefore, one can define a tangent map from any element to any other element. However, this map is not unique. 
Connection fundamentally is an infinitesimal structure that is path dependent. However, as this defines a normal coordinate chart, one can define connection such that the normal vectors are orthogonal. This is mentioned in Remark 6.1 of [[@goorEquivariantFilterEqF2023]]
This also talks about different works that account for curvature correction.

# Means of Random Variables in Lie Groups
[[@khanMeansRandomVariables2025]]
There are multiple notions of means, which are not the same. One needs to make an informed choice for things to make sense.
Discrete set of samples are used to define means.
**Deep learning tools can be used to represent fairly complicate pdfs on Lie Groups (normalizing flows, Moser flows and diffusion models)**

```ad-def
**Left Haar Measure**: If $S\subset G$ and $h S := \{hg|g\in S\}$, then
$$
\int_S dg = \int_{hS} dg \ \forall h \in G,
$$
where $dg$ denotes integration w.r.t. the (left) Haar measure. If $G$ is compact, then the integral is finite and there exists a unique normalized Haar measure for which the integral $\int_G dg$ is equal to 1.
```
Similarly, one can define an right-invariant Haar measure. When the measures coincide, the group is called unimodular.
#### Extrinsic Euclidean Mean
Consider a matrix lie group $G$ and a probability density function $f$ of the random variable $\tilde g$ on $G$.
$$
\mu_E(\tilde g) = \int_G g f(g) dg
$$
This definition commutes with the product with a fixed deterministic variable.
*This mean need not lie on the group and is a limitation. One can use projection to bring it back. But such definitions are still extrinsic.*
#### Fréchet Mean
Define a distance function: $\mathcal D : G \times G \to \mathbb R_{\ge 0}$. Consider the minimizer of this:
$$
\min_{h\in G} \left(\int_G \mathcal D(g,h)^2 f(g) dg \right)
$$
A Riemannian metric $\mathcal R$ can be used to define distance between two points, this is denoted by $\mu_F(\tilde g; \mathcal R)$.
*Karcher mean* refers to a point $\mu \in G$ that minimizes the distance. A first-order necessary condition for local minimization is:
$$
\int_{G'} \log_{\mu} (g) f(g) dg = 0_m
$$
$G' \subseteq G$ of $\mu$ that satisfies. ($G$ might not be connected. $\log_\mu$ is the Riemannian log map at $\mu$)
- $\int_{G'} f(g) dg =1$ -> support of $f$ is contained in $G'$
- $\log_{\mu} g$ is well-defined for all $g\in G'$ (normal neighborhood)
```ad-question
Karcher means is a superset of Frechet mean? How are they related?
```
#### Group-Theoretic Means
In general, Lie exponential and log maps don't agree with Riemannian notions.
Hence, Lie notions are different.
Group theoretic mean: $\mu$
$$
\int_{G'} \log (\mu ^{-1} g)f(g) dg = 0_m
$$
Choice of $G'$ is such that:
- $\int_{G'} f(g) dg =1$
- $\log(\mu^{-1} g)$ is defined for $g\in G'$
These conditions are easy to satisfy for groups like $SE(3)$, as all but a measure-zero subset can be traversed to.
For $\mathbb R^n$, if we consider $\log (y^{-1} x) = x-y$, we get the Euclidean mean.
#### Parametric Means
Suppose we have a diffeomorphism $\phi : S_{\mathbb R^n} \to S_G$, this is a local parametrization. The parametric mean of $\tilde g$ with the parameterization $\phi$ is defined as, the Euclidean mean of the transformation to the 
$$
\phi (\mu_E (\phi^{-1} (\tilde g)))
$$


# Bundles

Fiber Bundles
Principal Bundles
Vector Bundles
Frame Bundles
Tangent Bundles

### Fiber Bundle
Generalization of *Cartesian Product*. Locally, it is a product space, but globally might not. It requires the following four items.
- Total space: $E$
- Base space: $B$
- Fiber: $F$
- Bundle Projection Map: $\pi:E \to B$ : A continuous surjective mapping.
When $E  = B\times F$, then it is called a trivial bundle. The notion of "local product structure" is formalized as:
```ad-def
To define a fiber bundle, one needs the total space $E$, base space $B$, fiber $F$ and a bundle projection map: $\pi : E \to B$.
Every $x \in B$, there is an open "trivializing" neighbourhood $U\subset B$, such that there exists a homeomorphism $\phi : \pi^{-1} (U) \to U \times F$, in a way that $\pi$ agrees with thr projection onto the first factor.
```
### Torsor 
(Principal Homogeneous Space) for a group $G$ is a homogeneous manifold on which the group acts transitively (there exists an action that can move from anywhere to anywhere (implies a larger or equal group dim)) and freely (only identity group action is the unchanged action (implies a smaller or equal group dim)). 
*A torsor is a group that has forgotten its identity element.*
One can define right and left torsors.
### Principal Bundle $P$ 
Generalizes the *Cartesian Product* of a group $G$ and a topological space $X$ (A topological space has the notion of closeness defined (popularly using open sets), not requiring a way to measure distances). Additional properties are:
1. Fibers are $G$-torsors : The fibers are preserved by the group action, i.e., group action does not change the base projection.
There are two properties: *closure* and *homogeneous* with group action on a fiber
Vector bundle is a fiber bundle when the fibers are vector spaces.
### Frame Bundles
Associated with a vector bundle $E$, denoted by $F(E)$.
For a point on the base space, one associates a basis of the vector space. This basis can be acted upon by $GL(k,\mathbb R)$ and the fiber is a $GL(k,\mathbb R)$-torsor. This is the set of all invertible matrices of size $k\times k$.

### Parallel transport
Move vectors of manifold along curves such that they remain parallel wrt the connection. Given a curve $\gamma:[0, 1] \to M$

A vector field $X$ is called *parallel* if for any vector field $Y$, $\nabla_Y X =0$.
- The covariant derivative only depends on the value of $Y$ at that point, not the derivative and depends on $X$'s value and how it changes along $Y$
- Parallel vector fields exist for flat spaces as it is over-determined case for curved spaces.
- Parallel transport around a closed loop of an orthonormal frame returns a rotated orthonormal frame. (As the connection is compatible with the metric and curvature is non-zero.)
- A **parallel frame** is a collection of parallel vector fields $\{E_i\}$ such that they span the tangent space. To show that it is a parallel frame, it suffices to show that $\nabla_{E_j} E_i =0\ \forall i,j$ for a spanning frame as the connection is linear over $C^{\infty}(M)$ for the subscript slot.
- Suppose we have an orthonormal frame, then the set where the mutual covariant derivatives is an open set, then the manifold has 0 curvature.

### Normal Coordinates
The identification of $T_p M$ with $\mathbb R^n$ leads to a definition of coordinates through the Riemannian exponential map. This can be used to define a frame around $p$ at $q=\exp_p v$, using the mapping: $d\exp_p : T_vT_p M \to T_{\exp_p (v)} M$, which is $d \exp_p : T_p M \to T_q M$. 


# Background on Stochastic Process
Kolmogorov extended the discrete Markov process theory to continuous time, where two processes were defined: Jump process and Diffusion process. The former is a process where there is a small chance of large/discontinuous change and the other is a process where a small change is likely.
To describe each, there are PDEs, known as forward and backward Kolmogorov equations.
For a diffusion process, the forward Kolmogorov equation is same as the Fokker-Planck equation.


# Riemannian Manifolds
For a Riemannian metric, one can define a exponential map that uses geodesics, which are defined using ODEs and covariant derivatives.
```ad-def
A map between two Riemannian manifolds $f:(M,g)\to (N,h)$ is called an **isometry** if it preserves the metric, i.e., the following holds
$$
     \langle df_p v, df_p w \rangle_{h,{f(p)}} = \langle v, w\rangle_{g , p}
$$
```

One can also define the notion of parallel orthonormal frames. But these frames don't retain the property that the covariant derivative vanishes and this property holds only at point.

```ad-thm
**Gauss Lemma**: The exponential map is a radial isometry, i.e.,
$$
\langle d (\exp_p)_v \tilde v, d (\exp_p)_v \tilde w \rangle_{g, \exp_p v} = \langle v, w \rangle_{g, p}
$$
It is important to note that the term $v$ is common. Additionally, $d(\exp_p)_v : T_v T_p M \to T_p M$. To make the distinction clear $\tilde v, \tilde w \in T_v T_p M$.
```

# Geometric Control of Mechanical Systems
- Hamiltonian Systems: Symplectic or Poisson geometry dominates.
- Lagrangian Systems: Less clear on what the correct structure is.
Mechanical Systems have a metric that can be used to define an affine connection.

# Symplectic Manifolds
Keywords:
- Section: *smooth inverse of projection*
 
Stokes' theorem is the generalization of fundamental theorem of calculus. *Total change on the outside is the sum of little changes on the inside.* Integration and derivatives are not opposite operations, but rather the integration set changes. Integration on derivative of function in set is same as integration on boundary of set of function.

- Wedge/Exterior product: $\wedge$: $v_1 \wedge v_2$ denotes the parallelogram area captured by the two vectors. It is a bilinear operator. It is skew-symmetric.
- Interestingly enough, the space obtained from exterior products is also a vector space. For $\mathbb R^3$, it can be identified with itself.

Now, a symplectic 2-form on a manifold is defined as $\omega=\omega_{ij}dx^i \wedge dx^j$. This is a representation in a local chart. Every pair of covectors(?), there is an entry, so effectively it is a skew symmetric matrix.
A skew symmetric matrix can be full rank in even-dimensional spaces.
The even dimensional space that we consider is the cotangent bundle.
#### What is a differential k-form?
Differential form is a special kind of tensor field, that has alternating property and only acts on vectors.

A $k$-form is evaluated over a $k$-dimensional oriented manifold.
One can construct a basis for $k$-forms using exterior product over basis elements of the vector space $k$ times. *The dimensionality of the spaces increases and decreases with $k$*. 
A differential $k$-form is a special kind of $(0,k)$-tensor that is antisymmetric (or alternating). (swap two elements and it changes sign). It also forms a vector space and can be represented in a basis of $(0,k)$-tensors that are obtained from the basis elements of the vector space.
A metric is a **not** a two-form as it is not alternating. 
#### What is the tautological one-form?
1-form on $M$ is a mapping: $M\to T^* M$ (a covector field)
Given a map $\phi: M\to N$, then
- $d\phi:TM\to TN$
- $d\phi^*:T^*N\to T^*M$, which is defined as $d\phi^* (n^*) (\cdot)= n\cdot d\phi(\cdot)$

Now, consider $\pi:T^*Q \to Q$, then $d\pi^* : T^*Q \to T^*(T^* Q)$. This defines a one form on $T^* Q$ and hence is the tautological one-form.
A one-form acts on vectors and gives a real number. So, for an element of $T_{(q,p)}(T_q^*Q)$ which is $((q,p),(v,\hat p))$, it gives $\langle p, v \rangle$. 
#### Exterior Derivative
Suppose a differential form is defined as $\omega = f dx^{I} \in \Omega^k (M)$, where $f\in C^{\infty} (M) =\Omega^0(M)$ and $dx^I$ denotes an ordered set of indices over which the wedge product is taken. Then,
$$
d \omega = \sum_{i=1}^n \frac{\partial f}{\partial x^i} dx^i \wedge dx^I \in \Omega^{k+1}(M)
$$
This can be extended to general $k$-forms using linearity. This is a coordinate-dependent definition, but the object obtained is not!
A smooth function is a $0$-form that is evaluated on a point. The differential of a function is a $1$-form that is evaluated on line. 
#### Double Tangent Bundle
Q: How do vector fields on $TG$ translate to a second-order ODE on $TTG$?
Q: How does the curvature of $TG$ in Sasaki metric look like?
