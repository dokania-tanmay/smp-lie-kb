---
tags: [martingale, supermartingale, affine-martingale, doob, gronwall, probabilistic-tube, amgf]
---
# The Martingale Toolkit — Two Ways Out of a Generator Inequality

**Prereq:** [[20-generator-on-manifolds]] (the generator $\mathcal A$, and that it — not the drift — is the invariant), [[probability-on-manifolds]] (backward Kolmogorov equation), [[notation]]
**Goal:** given a pointwise inequality on $\mathcal A V$, know the two mechanisms that turn it into a probabilistic statement, know exactly which statement each one produces, and be able to say why neither replaces the other.

This is the shared root of both tracks in [[00-study-plan]] Phase 5. Track A (mean-squared, [[@daniObserverDesignStochastic2015]]) leaves by Route A below; track B (sup-over-time tube, [[@liuSafetyVerificationNonlinear2025]]) leaves by Route B. Everything downstream is a fight about the *constants*; this lesson is about the *statements*, and the two are easy to conflate.

Throughout $\{v_t\}$ is a diffusion on a state space with generator $\mathcal A$, and $M(v,t)\ge0$ is a function of state and time. Nothing below uses $\mathbb R^n$.

## Part 1 — the martingale hierarchy

:::info[Definition — martingale, supermartingale]
$\{M_t\}$ adapted and integrable is a **martingale** if $\mathbb E[M_{t+s}\mid\mathcal F_t]=M_t$, a **supermartingale** if $\mathbb E[M_{t+s}\mid\mathcal F_t]\le M_t$ ($s\ge0$). "Super" means it goes *down*.
:::

:::tip[Generator criterion]
If $(\partial_t+\mathcal A)M\le0$ pointwise, then $M(v_t,t)$ is a supermartingale. Dynkin: $\mathbb E M(v_t,t)-M(v_0,0)=\mathbb E\int_0^t(\partial_\tau+\mathcal A)M\,d\tau\le0$, and the same applied from $\mathcal F_t$ gives the conditional version.
:::

This is the *only* input the rest of the lesson takes from the geometry. Whatever [[20-generator-on-manifolds]] says $\mathcal A$ is on a manifold, the machinery below is unchanged.

:::info[Definition — $c$-martingale]
$\dfrac{\mathbb E[M_{t+dt}\mid\mathcal F_t]-M_t}{dt}\le b_t$: a supermartingale up to an additive drift budget $b_t$. Then $M_t-\int_0^tb_\tau d\tau$ is an honest supermartingale.
:::

:::info[Definition IV.1 — affine martingale (AM)]
$M(v,t)\ge0$ is an **affine martingale** of $\{v_t\}$ on $[0,T]$ if there exist $a_t,b_t\in\mathbb R$ with
$$\frac{\mathbb E\big(M(v_{t+dt},t+dt)\mid v_t\big)-M(v_t,t)}{dt}\;\le\;a_tM(v_t,t)+b_t\qquad\text{for all }t.$$
Equivalently $(\partial_t+\mathcal A)M\le a_tM+b_t$. Degenerations: $a_t\equiv0$ is the $c$-martingale; $a_t,b_t\equiv0$ is the supermartingale. [[@liuSafetyVerificationNonlinear2025]] Def. IV.1.
:::

The point of allowing $a_t\ne0$ is that $\mathcal AM\le0$ is often false and $\mathcal AM\le a_tM$ is often true — a *multiplicative* slack is what an exponential test function naturally produces, because $\mathcal A e^{\lambda\cdot}$ regenerates $e^{\lambda\cdot}$.

:::warning[Trap — the discrete-time version degenerates at $a_t\equiv1$, not $0$]
The discrete-time AM ([[@liuSafetyVerificationNonlinear2025]] Def. VI.1) is $\mathbb E(M(v_{t+1},t+1)\mid v_t)\le a_tM(v_t,t)+b_t$ — a bound on the **next value**, not on the increment. So the supermartingale case is $a_t\equiv1,b_t\equiv0$, and the DT $c$-martingale is $a_t\equiv1$. Reading "$a_t=0$" across from CT to DT collapses $M$ to zero. The two $a$'s differ by exactly the $1$ that continuous time hides in $M_{t+dt}-M_t$.
:::

:::tip[Lemma IV.1 — AM $\Rightarrow$ sublevel-set probability]
Let $M$ be an AM on $[0,T]$ with coefficients $a_t,b_t$. Put
$$\psi_t=e^{\int_t^Ta_\tau\,d\tau},\qquad \widetilde M(v,t)=M(v,t)\,\psi_t+\int_t^Tb_\tau\psi_\tau\,d\tau.$$
Then for any level $\mathsf M>0$, with $\mathcal V_t=\{v:\widetilde M(v,t)\le \mathsf M\}$,
$$\mathbb P\big(v_t\in\mathcal V_t,\ \forall t\le T\big)\;\ge\;1-\frac{M(v_0,0)\psi_0+\int_0^Tb_\tau\psi_\tau\,d\tau}{\mathsf M}.$$
:::

Read the construction: $\psi_t$ is the **integrating factor** for $\dot y=a_ty+b_t$ run backwards from $T$, and $\widetilde M$ is exactly the transformation that makes $\tfrac{d}{dt}\mathbb E\widetilde M\le0$. Note $\dot\psi_t=-a_t\psi_t$, so $(\partial_t+\mathcal A)\widetilde M=\psi_t\big[(\partial_t+\mathcal A)M-a_tM-b_t\big]\le0$. Once $\widetilde M$ is a nonnegative supermartingale, the conclusion is a single application of the maximal inequality below. **Nothing in Lemma IV.1 uses a chart, an inner product, or $\mathbb R^n$** — it needs only a nonnegative $M$ on the state space and a generator inequality. It ports to a manifold verbatim; all the work of lesson 28 is in producing $M$.

## Part 2 — the two routes, side by side

Suppose the geometry has delivered a pointwise inequality of contraction shape,
$$\mathcal AV\;\le\;-2\gamma V+C,\qquad V\ge0,\ \gamma>0. \tag{$\ast$}$$

### Route A — Grönwall on the moment, then Chebyshev

Dynkin turns ($\ast$) into an ODE inequality for the *scalar* $\mathbb EV$, killing the state dependence:
$$\frac{d}{dt}\mathbb EV(v_t)\le-2\gamma\,\mathbb EV(v_t)+C
\quad\overset{\text{Grönwall}}{\Longrightarrow}\quad
\mathbb EV(v_t)\;\le\;\frac{C}{2\gamma}+\mathbb EV(v_0)\,e^{-2\gamma t}. \tag{A}$$
That is the [[@daniObserverDesignStochastic2015]] Lemma 2 shape. To get a probability, Markov (equivalently Chebyshev when $V=d^2$): $\mathbb P[V(v_t)\ge \rho]\le\mathbb EV(v_t)/\rho$.

**What it gives.** A statement about **one fixed $t$ at a time**. The quantifier $\forall t$ sits outside $\mathbb P$, not inside.
**What it costs.** A first moment and nothing else — no exponential integrability, no free parameter, no optimisation. It is the natural output of a contraction argument ([[14-contraction-on-manifolds]]) with noise added, and it is cheap.

### Route B — affine martingale, then Doob/Ville

:::tip[Ville's maximal inequality]
$\{M_t\}_{t\le T}$ a nonnegative supermartingale, $c>0$. Then $\mathbb P\big[\sup_{t\le T}M_t\ge c\big]\le\mathbb E M_0/c$.
:::

**What it gives.** The **whole trajectory at once**: $\sup_{t\le T}$ lives *inside* $\mathbb P$. Fed through Lemma IV.1 with $M=$ an exponential-type function of the deviation, the sublevel sets $\mathcal V_t$ are exactly a tube.
**What it costs.** You must construct a martingale-like $M$ — a strictly stronger demand than a moment bound, since it must survive conditioning at every $t$ — and typically carry a free $\lambda$ (the exponential rate) that has to be optimised at the end.

:::info[Definition III.1 — probabilistic tube]
For horizon $[0,T]$, level $\delta$, and a radius curve $r_{\delta,t}$, the set $\mathcal T=\{(t,y):t\le T,\ \|y\|\le r_{\delta,t}\}$ is a **probabilistic tube** if $\mathbb P\big(\|X_t-x_t\|\le r_{\delta,t}\ \ \forall t\le T\big)\ge1-\delta$. Trajectory-level, one $\delta$ budget spent over the whole horizon. [[@liuSafetyVerificationNonlinear2025]] Def. III.1. On a manifold $\|X_t-x_t\|$ becomes $d(X_t,\bar x_t)$; this is the target object of Route B.
:::

### The lossy step, explicitly

Can Route A be upgraded? Pick a grid $0=t_0<\cdots<t_N=T$, spend $\delta/N$ at each node, and union-bound. With $B=\sup_t\mathbb EV(v_t)$ from (A) and $V=d^2$,
$$\mathbb P\Big[\max_{k\le N}d(v_{t_k})\ge r\Big]\;\le\;\sum_{k}\frac{B}{r^2}\;=\;\frac{NB}{r^2}
\qquad\Longrightarrow\qquad r=\sqrt{\frac{NB}{\delta}}\;\propto\;\sqrt N .$$
Three separate losses, and they are worth separating:

1. **The $\sqrt N$.** Chebyshev's tail is polynomial, so paying $\delta/N$ per node costs a factor $\sqrt N$. If the *same* system also admits an exponential moment bound $\mathbb P[d(v_{t_k})\ge r]\le 2e^{-r^2/2\nu}$, the union bound instead gives $r=\sqrt{2\nu\log(2N/\delta)}$ — cost only $\sqrt{\log N}$, and after optimising $N$ against a continuity estimate, $O(\sqrt{\log T})$. So the catastrophic version of the loss is Chebyshev's fault; the irreducible version is $\sqrt{\log}$.
2. **The gap between nodes.** The union bound controls $\max_k$, never $\sup_{t\le T}$. Closing it needs a modulus-of-continuity estimate that Route A does not supply, and refining the grid re-triggers loss 1.
3. **It is the wrong object.** Route B's Lemma IV.1 pays *none* of this: $\sup_t$ is inside $\mathbb P$ from the first line, because a supermartingale controls its own running maximum.

:::tip[The statement to hold onto]
**Neither route subsumes the other.** A mean-squared bound plus Markov is genuinely weaker than a tube, not a different presentation of one: it yields $\forall t\,\mathbb P[\cdot]\ge1-\delta$, and $\forall t\,\mathbb P\ne\mathbb P\,\forall t$. Problem 4 exhibits a process where the first holds at every $t$ and the second fails at probability $1$. Conversely Route A is cheaper, needs no $\lambda$, and is the right sanity check on B's constants — which is why lesson 29 wants both.
:::

## Worked example — scalar Ornstein–Uhlenbeck, both routes

$dX_t=-\gamma X_t\,dt+\sigma\,dW_t$, $X_0=0$, generator $\mathcal Af=-\gamma x f'+\tfrac12\sigma^2f''$. Fix $\gamma=\sigma=1$, $T=10$, $\delta=0.05$.

**Route A.** $V=x^2$: $\mathcal AV=-2\gamma x^2+\sigma^2=-2\gamma V+\sigma^2$, i.e. ($\ast$) with $C=\sigma^2$. Then (A) gives $\mathbb EX_t^2\le\sigma^2/(2\gamma)=0.5$, and Chebyshev at level $\delta$ gives
$$r_A=\sigma/\sqrt{2\gamma\delta}=\sqrt{10}\approx 3.16,\qquad\text{for each fixed }t.$$

**Route B.** Take $M(x)=\cosh(\lambda x)$ — the $n=1$ AMGF energy function, chosen because it is even and exponential. Then
$$\mathcal AM=\underbrace{-\gamma\lambda x\sinh(\lambda x)}_{\le\,0\ \text{since }x\sinh(\lambda x)\ge0}+\tfrac12\sigma^2\lambda^2\cosh(\lambda x)\;\le\;\tfrac{\lambda^2\sigma^2}{2}M .$$
So $M$ is an AM with $a_t\equiv\lambda^2\sigma^2/2$, $b_t\equiv0$ — the contraction is *discarded* at the marked step. Lemma IV.1: $\psi_t=e^{a(T-t)}\ge1$, $M(x_0,0)=1$, so $\mathbb P[\sup_{t\le T}\cosh(\lambda X_t)\ge u]\le e^{aT}/u$. With $\cosh(\lambda r)\ge\tfrac12e^{\lambda r}$,
$$\mathbb P\big[\sup_{t\le T}|X_t|\ge r\big]\le 2\exp\!\big(\tfrac{\lambda^2\sigma^2T}{2}-\lambda r\big)
\ \overset{\lambda^*=r/(\sigma^2T)}{=}\ 2e^{-r^2/(2\sigma^2T)}
\ \Rightarrow\ r_B=\sigma\sqrt{2T\log(2/\delta)}\approx 8.59 .$$

**The comparison.** $4\times10^4$ exact-transition sample paths give the true 95th percentile of $\sup_{t\le10}|X_t|$ as $\mathbf{2.44}$.

| | radius | statement proved | ratio to truth |
|---|---|---|---|
| Route A, Chebyshev | $3.16$ | $\mathbb P[|X_t|\le r]\ge0.95$ **at each fixed $t$** | — (wrong statement) |
| Route A + union, $N=100$ | $31.6$ | $\max_{k\le100}$ only | $13\times$ |
| Route A + union, $N=1000$ | $100.0$ | $\max_{k\le1000}$ only | $41\times$ |
| **Route B, Doob** | $\mathbf{8.59}$ | $\mathbb P[\sup_{t\le10}|X_t|\le r]\ge0.95$ | $3.5\times$ |

Route A's $3.16$ empirically does cover the sup (simulated $\mathbb P=0.9988$) — but that is a fact about this system, **not something Route A proves**, and the honest upgrade of A costs $4\times$ more than B at $N=100$ and diverges as $N\to\infty$, while never reaching $\sup_t$.

:::warning[Open question — B is loose here for a known reason]
$r_B\propto\sqrt T$, but the truth for a contractive OU grows like $\sqrt{\log T}$: discarding the drift term made $a_t$ blind to $\gamma$. This is exactly the "conservative for $c<0$" caveat after [[@liuSafetyVerificationNonlinear2025]] Thm. 2, patched there by Thm. 3's window-splitting (which reintroduces a union bound over $T/\Delta t$ windows — loss 1 above, at the $\sqrt{\log}$ rate, deliberately). Keeping $\gamma$ inside the AM needs a time-varying $\lambda_t=\lambda_0e^{\gamma t}$, which cancels the $x\sinh$ term exactly and reproduces Thm. 2's $e^{ct}\sqrt{(1-e^{-2cT})/2c}$ prefactor. Whether an exit-time argument ([[@phamTightEstimatesExit2019]], unread) beats both is open.
:::

## Where this sits in the standing question

Both routes are **kind 1 — intrinsic — at this level of abstraction**: Grönwall, Dynkin, Ville and Lemma IV.1 are statements about $\mathcal A$ and a nonnegative function, and none of them mentions a chart. The chart-dependence the thesis attacks enters *upstream*, when ($\ast$) or the AM inequality is produced by differentiating a distance-like $V$ twice — that is where $\sup|\partial^2g_{ij}|$ appears in [[@daniObserverDesignStochastic2015]] and where curvature must replace it. **The critique applies identically to both tracks**, and this lesson is where they still agree.

## Problems

1. **Recall.** State from memory: supermartingale, $c$-martingale, affine martingale (continuous time), and both maximal/moment inequalities. Then (a) give the two parameter choices that degenerate the CT affine martingale, (b) give the corresponding choices in discrete time and explain in one sentence why they differ, (c) say which of the two routes puts $\sup_t$ inside $\mathbb P$ and why the other cannot.

2. **Compute.** For $dX_t=-X_t\,dt+\sqrt2\,dW_t$ with $X_0=0$, $T=4$, $\delta=0.1$: (a) run Route A — find $C$, the Grönwall bound on $\mathbb EX_t^2$, and the Chebyshev radius; (b) run Route B with $M=\cosh(\lambda x)$ — identify $a_t,b_t$, write $\psi_t$, and optimise $\lambda$; (c) state precisely what each radius means, in one sentence each, with the quantifiers in the right order.

3. **Prove.** Let $\{M_t\}_{t\le T}$ be a nonnegative càdlàg supermartingale. Using optional stopping at $\tau=\inf\{t:M_t\ge c\}$, prove $\mathbb P[\sup_{t\le T}M_t\ge c]\le\mathbb EM_0/c$. Then deduce Lemma IV.1 from it: verify $\widetilde M$ is a nonnegative supermartingale and identify $\mathbb E\widetilde M_0$.

4. **Break it.** Fix $T=1$ and $\delta\in(0,1)$. Let $U\sim\mathrm{Unif}[0,1]$ and define the (non-Markov, but adapted to $\sigma(U)$) process
$$Y_t=\mathbf 1\{|t-U|\le\delta/2\},\qquad t\in[0,1].$$
(a) Compute $\mathbb EY_t^2$ for $t\in[\delta/2,1-\delta/2]$ and show the fixed-$t$ Markov bound $\mathbb P[Y_t\ge1]\le\delta$ holds at every such $t$. (b) Compute $\mathbb P[\sup_{t\le1}Y_t\ge1]$. (c) Conclude that no bound on $\sup_t\mathbb EY_t^2$ alone can produce a probabilistic tube of radius $<1$, at any $\delta$. (d) Where does Route B refuse to apply to this process — i.e. which hypothesis of Lemma IV.1 fails? (e) One sentence: what does this say about lesson 29's plan to compare track A and track B on the same system?

---

## Solutions

**1.** (a) CT: $a_t\equiv0$ gives the $c$-martingale, $a_t\equiv b_t\equiv0$ the supermartingale. (b) DT: $a_t\equiv1$ gives the $c$-martingale, $a_t\equiv1,b_t\equiv0$ the supermartingale. The CT definition bounds the *increment* divided by $dt$, the DT definition bounds the *next value*; the identity term $M_t$ that CT subtracts off is the missing $1$. Setting $a_t=0$ in DT forces $\mathbb E M_{t+1}\le b_t$, which is a boundedness statement, not a martingale one. (c) Route B, because a nonnegative supermartingale controls its own running maximum through optional stopping; Route A produces only $\mathbb EV(v_t)$ for each $t$ separately, a family of one-time-marginal statements from which no joint statement about the path follows (Problem 4).

**2.** (a) $\mathcal Ax^2=-2x^2+2$, so $\gamma=1$, $C=\sigma^2=2$; $\mathbb EX_t^2\le\frac{C}{2\gamma}(1-e^{-2t})\le1$; Chebyshev $\mathbb P[|X_t|\ge r]\le1/r^2=0.1$ gives $r_A=\sqrt{10}\approx3.16$. (b) $\mathcal A\cosh(\lambda x)=-\lambda x\sinh(\lambda x)+\lambda^2\cosh(\lambda x)\le\lambda^2\cosh(\lambda x)$, so $a_t\equiv\lambda^2\sigma^2/2=\lambda^2$, $b_t\equiv0$, $\psi_t=e^{\lambda^2(4-t)}$. The bound is $2e^{\lambda^2\sigma^2T/2-\lambda r}=2e^{4\lambda^2-\lambda r}$, optimal at $\lambda^*=r/8$, value $2e^{-r^2/16}$; setting it to $0.1$ gives $r_B=\sqrt{2\sigma^2T\log(2/\delta)}=\sqrt{16\log20}\approx6.92$. (c) A: "for each fixed $t\le4$, $\mathbb P[|X_t|\le3.16]\ge0.9$" — different events for different $t$, no joint claim. B: "$\mathbb P[|X_t|\le6.92$ for all $t\le4]\ge0.9$" — one event, one budget.

**3.** $\tau$ is a stopping time; $M_{t\wedge\tau}$ is a nonnegative supermartingale, so $\mathbb EM_0\ge\mathbb EM_{T\wedge\tau}$. Split on $\{\tau\le T\}$: $\mathbb EM_{T\wedge\tau}\ge\mathbb E[M_\tau\mathbf1_{\tau\le T}]\ge c\,\mathbb P[\tau\le T]$, using $M\ge0$ on the complement and $M_\tau\ge c$ on $\{\tau\le T\}$ (càdlàg gives $M_\tau\ge c$ at the hitting time). Since $\{\sup_{t\le T}M_t\ge c\}\subseteq\{\tau\le T\}$ up to a null set, $\mathbb P[\sup_{t\le T}M_t\ge c]\le\mathbb EM_0/c$. For Lemma IV.1: $\widetilde M=M\psi_t+\int_t^Tb_\tau\psi_\tau d\tau\ge0$, and since $\dot\psi_t=-a_t\psi_t$ and $\tfrac{d}{dt}\int_t^Tb_\tau\psi_\tau d\tau=-b_t\psi_t$,
$$(\partial_t+\mathcal A)\widetilde M=\psi_t\big[(\partial_t+\mathcal A)M-a_tM-b_t\big]\le0$$
by the AM inequality and $\psi_t>0$. So $\widetilde M(v_t,t)$ is a nonnegative supermartingale with $\mathbb E\widetilde M_0=M(v_0,0)\psi_0+\int_0^Tb_\tau\psi_\tau d\tau$ (deterministic $v_0$), and Ville at $c=\mathsf M$ gives the complement of the stated bound. Note the last step is the *only* probabilistic ingredient — the rest is an integrating factor.

**4.** (a) $Y_t\in\{0,1\}$, so $\mathbb EY_t^2=\mathbb EY_t=\mathbb P[|t-U|\le\delta/2]=\delta$ for $t$ in the interior. Markov: $\mathbb P[Y_t\ge1]\le\mathbb EY_t^2/1=\delta$. This holds at **every** such $t$, so the fixed-$t$ guarantee "radius $1$ at level $1-\delta$" is satisfied uniformly in $t$. (b) The spike is always somewhere in $[0,1]$, so $\sup_{t\le1}Y_t=1$ almost surely: $\mathbb P[\sup_tY_t\ge1]=1$, not $\le\delta$. Taking $\delta\to0$ makes the fixed-$t$ bound arbitrarily strong while the sup statement stays at probability $1$ — the loss is unbounded, not a constant factor. (c) Any tube of radius $r<1$ is violated with probability $1$, while $\sup_t\mathbb EY_t^2=\delta$ is as small as you like; so the map (moment bound) $\mapsto$ (tube) does not exist. Route A's output is a family of marginals, and the joint law is not determined by its marginals — that is the whole content. (d) Lemma IV.1 needs a *generator* inequality, i.e. an inequality on the conditional increment given $\mathcal F_t$. Here, conditionally on the past, $Y$ is not a diffusion and there is no $M\ge0$ with $\mathbb E[M(Y_{t+dt})\mid\mathcal F_t]-M(Y_t)\le a_tM+b_t$ that is nontrivial before the spike: knowing $Y_s=0$ for $s\le t$ says $U>t$, and the conditional probability of jumping in $[t,t+dt]$ stays bounded away from $0$, so no finite $a_t,b_t$ with $M(0)$ small can absorb it. The failure is real and not an artefact — Route B is *stronger*, and this process is outside its hypotheses, as it must be. (e) Lesson 29 must compare A and B on a system where **both** apply, and must report the two statements separately rather than a single ratio of radii: any "A vs B" number is a comparison of costs conditional on B being available at all.
