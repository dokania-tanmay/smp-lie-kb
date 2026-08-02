---
tags: [probability, stochastics, lie-groups]
---
# Probability Theory on Manifolds

My own notes. Companion files: [[riemannian-geometry]], [[mechanical-systems-on-lie-groups]].

## Haar measure

```ad-def
**Left Haar Measure**: If $S\subset G$ and $h S := \{hg|g\in S\}$, then
$$
\int_S dg = \int_{hS} dg \ \forall h \in G,
$$
where $dg$ denotes integration w.r.t. the (left) Haar measure. If $G$ is compact, then the integral is finite and there exists a unique normalized Haar measure for which the integral $\int_G dg$ is equal to 1.
```

Similarly, one can define a right-invariant Haar measure. When the measures coincide, the group is called **unimodular**.

This is the measure-theoretic sibling of the left-invariant metric in [[riemannian-geometry]] — same invariance idea, different structure. Needed to write down a pdf on $G$ at all.

## Means of random variables in Lie groups

[[@khanMeansRandomVariables2025]]

There are multiple notions of means, which are **not the same**. One needs to make an informed choice for things to make sense. A discrete set of samples is used to define means in practice.

*Deep learning tools can be used to represent fairly complicated pdfs on Lie groups (normalizing flows, Moser flows and diffusion models).*

### Extrinsic Euclidean mean

Consider a matrix Lie group $G$ and a probability density function $f$ of the random variable $\tilde g$ on $G$.

$$\mu_E(\tilde g) = \int_G g f(g) dg$$

This definition commutes with the product with a fixed deterministic variable.

*This mean need not lie on the group and is a limitation. One can use projection to bring it back. But such definitions are still extrinsic.*

### Fréchet mean

Define a distance function $\mathcal D : G \times G \to \mathbb R_{\ge 0}$. Consider the minimizer of

$$\min_{h\in G} \left(\int_G \mathcal D(g,h)^2 f(g) dg \right)$$

A Riemannian metric $\mathcal R$ can be used to define distance between two points; this is denoted $\mu_F(\tilde g; \mathcal R)$.

*Karcher mean* refers to a point $\mu \in G$ that minimizes the distance. A first-order necessary condition for local minimization is

$$\int_{G'} \log_{\mu} (g) f(g) dg = 0_m$$

with $G' \subseteq G$ a neighbourhood of $\mu$ such that

- $\int_{G'} f(g) dg = 1$ → the support of $f$ is contained in $G'$;
- $\log_\mu g$ is well-defined for all $g \in G'$ (normal neighbourhood).

($G$ might not be connected. $\log_\mu$ is the Riemannian log map at $\mu$.)

```ad-question
Karcher means is a superset of Frechet mean? How are they related?
```
Working answer to check against the paper: Fréchet = global minimizer, Karcher = stationary point / local minimizer, so every Fréchet mean is a Karcher mean but not conversely.

### Group-theoretic means

In general, Lie exponential and log maps don't agree with Riemannian notions (see [[riemannian-geometry]]). Hence Lie notions are different. The group-theoretic mean $\mu$ solves

$$\int_{G'} \log (\mu ^{-1} g)f(g) dg = 0_m$$

with $G'$ such that $\int_{G'} f(g) dg = 1$ and $\log(\mu^{-1}g)$ is defined for $g \in G'$. These conditions are easy to satisfy for groups like $SE(3)$, as all but a measure-zero subset can be traversed to.

For $\mathbb R^n$, if we consider $\log(y^{-1}x) = x-y$, we get the Euclidean mean.

### Parametric means

Suppose we have a diffeomorphism $\phi : S_{\mathbb R^n} \to S_G$ — a local parametrization. The parametric mean of $\tilde g$ with parameterization $\phi$ is the Euclidean mean of the transformed variable pushed forward:

$$\phi (\mu_E (\phi^{-1} (\tilde g)))$$

## Background on stochastic processes

Kolmogorov extended the discrete Markov process theory to continuous time, where two processes were defined:

- **Jump process** — a small chance of large/discontinuous change;
- **Diffusion process** — a small change is likely.

To describe each there are PDEs, known as the forward and backward Kolmogorov equations. For a diffusion process, the forward Kolmogorov equation is the same as the Fokker–Planck equation.

The backward equation is the one built from the **generator**. That is the object the pathway needs: apply it to a distance function and show the result is a (super)martingale, then convert to a tube bound by a maximal inequality.

```ad-question
Not yet worked through: Itô vs Stratonovich on a manifold, the generator as a second-order operator, and where the curvature terms enter. See the study plan in `content/`.
```
