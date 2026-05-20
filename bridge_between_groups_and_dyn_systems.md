# Bridge Between Dynamical Systems and Groups

## Definition 1: Discrete dynamical system

Let $X$ be a phase space. A discrete-time dynamical system on $X$ is a map

$$
f \colon X \to X
$$

together with the iteration rule

$$
x_{n+1}=f(x_n).
$$

## Definition 2: Symmetry group of a dynamical system

Let $\mathrm{Aut}(X)$ be a chosen group of admissible transformations of $X$, for example homeomorphisms, diffeomorphisms, linear automorphisms, or isometries.

The symmetry group of $f$ relative to $\mathrm{Aut}(X)$ is

$$
G(f)=\lbrace g \in \mathrm{Aut}(X) : g \circ f = f \circ g \rbrace.
$$

This is the commutant of $f$ inside $\mathrm{Aut}(X)$. If $f \in \mathrm{Aut}(X)$, then $G(f)$ is the usual centralizer of $f$ in $\mathrm{Aut}(X)$.

## Definition 3: Orbit and stabilizer of a point

For $z \in X$, define the $G(f)$-orbit of $z$ by

$$
\mathcal{O}_{G(f)}(z)=\lbrace g(z) : g \in G(f) \rbrace
$$

and define the stabilizer subgroup of $z$ by

$$
G(f)_z=\lbrace g \in G(f) : g(z)=z \rbrace.
$$

## Problem 1: Symmetry type of a point

Given $z \in X$, determine the data in $G(f)$ that describe the properties of $z$ preserved by the dynamics.

The natural group-theoretic answer is the pair

$$
\bigl(\mathcal{O}_{G(f)}(z),G(f)_z\bigr).
$$

Two points $z,w \in X$ have the same symmetry type with respect to $f$ if and only if

$$
w \in \mathcal{O}_{G(f)}(z).
$$

The stabilizer $G(f)_z$ records the symmetries of the dynamical system that fix $z$.

**Literature.** This is the standard orbit-stabilizer viewpoint for group actions; see Lyons, [Group Actions](./refs/lyons-group-actions-libretexts.pdf), especially the definitions of orbit and stabilizer and the orbit-stabilizer theorem. In equivariant dynamics, the same language appears as orbit and isotropy data for solutions and states; see [Equivariant dynamical systems](https://www.scholarpedia.org/article/Equivariant_dynamical_systems) in Scholarpedia.

## Lemma 1: Rotational symmetry in the complex plane

Let $X=\mathbb{C}\cong \mathbb{R}^2$, and let

$$
SO(2)=\lbrace R_\theta : \mathbb{C} \to \mathbb{C},\ R_\theta(z)=e^{i\theta}z,\ \theta \in \mathbb{R}/2\pi\mathbb{Z} \rbrace.
$$

Then

$$
SO(2) \leq G(f)
$$

if and only if

$$
f(e^{i\theta}z)=e^{i\theta}f(z)
\qquad
\text{for all } \theta \in \mathbb{R}/2\pi\mathbb{Z}\text{ and all }z \in \mathbb{C}.
$$

Thus $SO(2)$ is a symmetry group of $f$ precisely when $f$ is rotationally equivariant.

**Literature.** This is the usual definition of equivariance specialized to the rotation action of $SO(2)$. Standard references are Golubitsky, Stewart, and Schaeffer, [Singularities and Groups in Bifurcation Theory, Volume II](./refs/golubitsky-stewart-schaeffer-singularities-groups-bifurcation-vol2.pdf), especially the chapters on group-theoretic preliminaries and Hopf bifurcation with $O(2)$ symmetry, and Golubitsky and Stewart, [The Symmetry Perspective](https://link.springer.com/book/10.1007/978-3-0348-8167-8), which develops symmetry methods for equilibria, periodic states, and chaos.

## Problem 2: When can the symmetry group be $SO(2)$?

Determine whether the symmetry group of $f$ is exactly $SO(2)$.

This requires the stronger condition

$$
G(f)=SO(2),
$$

not merely

$$
SO(2)\leq G(f).
$$

Therefore, the answer depends on both $f$ and the chosen ambient transformation group $\mathrm{Aut}(X)$. It is not determined by the point $z \in \mathbb{C}$ alone.

**Literature.** The problem of finding the full symmetry group of a dynamical system is usually phrased as a centralizer problem. Baake's overview [A brief guide to reversing and extended symmetries of dynamical systems](./refs/baake-brief-guide-reversing-extended-symmetries-1803.06263.pdf) reviews this viewpoint and the related extension from centralizers to normalizers. For concrete computations of exact symmetry groups in dynamical systems, see also Baake and Roberts on [symmetries and reversing symmetries of toral automorphisms](./refs/baake-roberts-symmetries-reversing-symmetries-toral-automorphisms-math0006092.pdf).

## Lemma 2: Higher-dimensional equivariance

Let $X=\mathbb{R}^n$, and let

$$
H \leq GL(n,\mathbb{R}).
$$

Then

$$
H \leq G(f)
$$

if and only if

$$
f(hx)=h f(x)
\qquad
\text{for all } h \in H\text{ and all }x \in \mathbb{R}^n.
$$

Full rotational symmetry in dimension $n$ corresponds to the choice

$$
H=SO(n).
$$

**Literature.** This is the basic equivariance condition for a linear group action on $\mathbb{R}^n$. The general theory is treated in Golubitsky, Stewart, and Schaeffer, [Singularities and Groups in Bifurcation Theory, Volume II](./refs/golubitsky-stewart-schaeffer-singularities-groups-bifurcation-vol2.pdf), and in Chossat and Lauterbach's book [Methods in Equivariant Bifurcations and Dynamical Systems](https://archive-dsweb.siam.org/The-Magazine/All-Issues/methods-in-equivariant-bifurcations-and-dynamical-systems.html), reviewed by DSWeb as a systematic account of equivariant bifurcation theory.

## Definition 4: Continuous-time dynamical system

Let

$$
\Phi \colon \mathbb{R} \times X \to X
$$

be a flow. Its symmetry group is

$$
G(\Phi)=\lbrace g \in \mathrm{Aut}(X) : g \circ \Phi_t = \Phi_t \circ g\text{ for all }t \in \mathbb{R} \rbrace.
$$

If $\Phi$ is generated by a vector field

$$
\dot{x}=F(x),
$$

then a subgroup $H \leq GL(n,\mathbb{R})$ acts by symmetries if and only if

$$
F(hx)=hF(x)
\qquad
\text{for all } h \in H\text{ and all }x \in \mathbb{R}^n.
$$

## Definition 5: Stationary points

A stationary point of the discrete system $f \colon X \to X$ is a point $p \in X$ such that

$$
f(p)=p.
$$

A stationary point of a flow $\Phi$ is a point $p \in X$ such that

$$
\Phi_t(p)=p
\qquad
\text{for all }t \in \mathbb{R}.
$$

For a vector field $\dot{x}=F(x)$, this is equivalent to

$$
F(p)=0.
$$

## Definition 6: Fixed-point set of a group action

For a group action $H \curvearrowright X$, define

$$
X^H=\lbrace x \in X : hx=x\text{ for all }h \in H \rbrace.
$$

For a single transformation $R \in \mathrm{Aut}(X)$, define

$$
\mathrm{Fix}(R)=\lbrace x \in X : R(x)=x \rbrace.
$$

## Lemma 3: Symmetry fixed-point sets are dynamically invariant

If

$$
H \leq G(f),
$$

then

$$
f(X^H)\subseteq X^H.
$$

Proof. Let $x \in X^H$ and let $h \in H$. Since $h \in G(f)$,

$$
hf(x)=f(hx).
$$

Since $x \in X^H$, one has $hx=x$. Hence

$$
hf(x)=f(x).
$$

Therefore $f(x)\in X^H$.

**Literature.** Fixed-point subspaces are fundamental invariant subspaces in equivariant dynamics. Golubitsky and Stewart state this viewpoint explicitly in [Dynamics and Bifurcation in Networks, Chapter 13](https://epubs.siam.org/doi/10.1137/1.9781611977332.ch13): fixed-point subspaces of isotropy subgroups are flow-invariant for arbitrary equivariant ODEs. The same principle is part of the standard setup in equivariant bifurcation theory; see Chossat and Lauterbach, [Methods in Equivariant Bifurcations and Dynamical Systems](https://archive-dsweb.siam.org/The-Magazine/All-Issues/methods-in-equivariant-bifurcations-and-dynamical-systems.html).

## Corollary 1: Singleton fixed-point sets give stationary points

If

$$
H \leq G(f)
$$

and

$$
X^H=\lbrace p \rbrace,
$$

then

$$
f(p)=p.
$$

Thus a singleton fixed-point set of a symmetry group is forced to be a stationary point of every dynamical system commuting with that group action.

## Lemma 4: The origin is fixed by full rotational symmetry

For the standard action of $SO(n)$ on $\mathbb{R}^n$ with $n \geq 2$,

$$
(\mathbb{R}^n)^{SO(n)}=\lbrace 0 \rbrace.
$$

Consequently, if

$$
SO(n)\leq G(f),
$$

then

$$
f(0)=0.
$$

Similarly, if $F \colon \mathbb{R}^n \to \mathbb{R}^n$ is $SO(n)$-equivariant, meaning

$$
F(hx)=hF(x)
\qquad
\text{for all }h \in SO(n)\text{ and all }x \in \mathbb{R}^n,
$$

then

$$
F(0)=0.
$$

**Literature.** The statement is an instance of fixed-point subspace invariance for the standard representation of $SO(n)$. For the role of fixed-point subspaces in equivariant dynamics, see Golubitsky and Stewart, [Dynamics and Bifurcation in Networks, Chapter 13](https://epubs.siam.org/doi/10.1137/1.9781611977332.ch13). For rotational actions and spherical symmetry in dynamical systems, see Golubitsky and Stewart, [The Symmetry Perspective](https://link.springer.com/book/10.1007/978-3-0348-8167-8), and Golubitsky, Stewart, and Schaeffer, [Singularities and Groups in Bifurcation Theory, Volume II](./refs/golubitsky-stewart-schaeffer-singularities-groups-bifurcation-vol2.pdf).

## Lemma 5: Fixed points of a single commuting rotation are invariant

Let $R \in \mathrm{Aut}(X)$. If

$$
R \in G(f),
$$

then

$$
f(\mathrm{Fix}(R))\subseteq \mathrm{Fix}(R).
$$

Proof. If $x \in \mathrm{Fix}(R)$, then $R(x)=x$. Since $R \in G(f)$,

$$
R(f(x))=f(R(x))=f(x).
$$

Hence $f(x)\in \mathrm{Fix}(R)$.

**Literature.** For a single commuting transformation, this is the same centralizer idea used in the literature on symmetries and reversing symmetries of maps. Baake, [A brief guide to reversing and extended symmetries of dynamical systems](./refs/baake-brief-guide-reversing-extended-symmetries-1803.06263.pdf), reviews symmetries of a homeomorphism through its centralizer. The invariant fixed-set conclusion is the one-generator version of fixed-point subspace invariance in equivariant dynamics; compare Golubitsky and Stewart, [Dynamics and Bifurcation in Networks, Chapter 13](https://epubs.siam.org/doi/10.1137/1.9781611977332.ch13).

## Corollary 2: A singleton rotation fixed point is stationary

If

$$
R \in G(f)
$$

and

$$
\mathrm{Fix}(R)=\lbrace p \rbrace,
$$

then

$$
f(p)=p.
$$

## Problem 3: Relation between stationary points and rotation fixed points

Determine when a fixed point of a rotation is also a stationary point of the dynamical system.

The sufficient condition is the commutation relation

$$
R \circ f=f \circ R.
$$

Under this condition,

$$
f(\mathrm{Fix}(R))\subseteq \mathrm{Fix}(R).
$$

If additionally

$$
\mathrm{Fix}(R)=\lbrace p \rbrace,
$$

then

$$
f(p)=p.
$$

Without the commutation relation

$$
R \circ f=f \circ R,
$$

the existence of a fixed point of $R$ and the existence of a stationary point of $f$ are independent conditions.

**Literature.** The connection between equilibria, isotropy, and fixed-point subspaces is one of the organizing principles of equivariant bifurcation theory. See Golubitsky, Stewart, and Schaeffer, [Singularities and Groups in Bifurcation Theory, Volume II](./refs/golubitsky-stewart-schaeffer-singularities-groups-bifurcation-vol2.pdf), Chossat and Lauterbach, [Methods in Equivariant Bifurcations and Dynamical Systems](https://archive-dsweb.siam.org/The-Magazine/All-Issues/methods-in-equivariant-bifurcations-and-dynamical-systems.html), and Golubitsky and Stewart, [Dynamics and Bifurcation in Networks, Chapter 13](https://epubs.siam.org/doi/10.1137/1.9781611977332.ch13). These references treat fixed-point subspaces as invariant subspaces and use them to organize equilibria and bifurcating solution branches.

## Open problems related to the problem sections

### Open Problem 1.1: Orbit-type stratification of a dynamical system

Let $f \colon X \to X$ be a dynamical system and let $G(f)$ be its symmetry group. For each subgroup $K \leq G(f)$, define

$$
X_K=\lbrace x \in X : G(f)_x=K \rbrace
$$

and, for each conjugacy class $(K)$ of subgroups of $G(f)$, define the orbit-type stratum

$$
X_{(K)}=\lbrace x \in X : G(f)_x \text{ is conjugate to }K \rbrace.
$$

Determine conditions on $X$, $\mathrm{Aut}(X)$, and $f$ under which the decomposition

$$
X=\bigcup_{(K)}X_{(K)}
$$

has useful geometric structure, such as a stratification by manifolds, semialgebraic sets, or analytic sets.

### Open Problem 1.2: Dynamical meaning of stabilizers

Given $z \in X$, determine which dynamical properties of the orbit

$$
\lbrace f^n(z):n\geq 0\rbrace
$$

are determined by the pair

$$
\bigl(\mathcal{O}_{G(f)}(z),G(f)_z\bigr).
$$

In particular, decide when equality of symmetry type implies equality of qualitative dynamical type, such as periodicity, recurrence, stability, or membership in the same invariant set.

### Open Problem 1.3: Realizability of stabilizer subgroups

Given a subgroup $K \leq G(f)$, determine whether there exists a point $z \in X$ such that

$$
G(f)_z=K.
$$

Equivalently, classify the subgroups of $G(f)$ that occur as point stabilizers for the action

$$
G(f)\curvearrowright X.
$$

### Open Problem 2.1: Exact symmetry group problem

For a prescribed group $H \leq \mathrm{Aut}(X)$, characterize the maps

$$
f \colon X \to X
$$

such that

$$
G(f)=H.
$$

In particular, for $X=\mathbb{C}$, characterize the maps satisfying

$$
G(f)=SO(2).
$$

### Open Problem 2.2: Symmetry rigidity

Determine classes of maps $f \colon X \to X$ for which the inclusion

$$
H \leq G(f)
$$

forces a larger symmetry group

$$
H \lt G(f).
$$

For example, determine when rotational equivariance

$$
SO(2)\leq G(f)
$$

implies additional symmetries, such as reflection symmetry, scaling symmetry, or full orthogonal symmetry.

### Open Problem 2.3: Computation of symmetry groups

For a specified class of maps, such as polynomial maps, rational maps, smooth vector fields, or analytic vector fields, develop effective criteria to compute

$$
G(f)=\lbrace g \in \mathrm{Aut}(X):g\circ f=f\circ g\rbrace.
$$

The corresponding decision problem is to determine whether a given subgroup

$$
H\leq \mathrm{Aut}(X)
$$

satisfies

$$
G(f)=H.
$$

### Open Problem 3.1: Converse fixed-point problem

Let $p \in X$ be a stationary point of $f$:

$$
f(p)=p.
$$

Determine whether there exists a nontrivial subgroup

$$
H\leq G(f)
$$

such that

$$
X^H=\lbrace p \rbrace.
$$

Equivalently, decide which stationary points arise as singleton fixed-point sets of symmetry subgroups.

### Open Problem 3.2: Equilibria forced by symmetry

Given a group action $H\curvearrowright X$, classify all dynamical systems $f \colon X \to X$ satisfying

$$
H\leq G(f)
$$

for which every point in $X^H$ is stationary:

$$
f(x)=x
\qquad
\text{for all }x\in X^H.
$$

More generally, determine when the restriction

$$
f|_{X^H}\colon X^H\to X^H
$$

has prescribed dynamics.

### Open Problem 3.3: Stability of symmetry-forced stationary points

Suppose

$$
H\leq G(f)
$$

and

$$
X^H=\lbrace p \rbrace.
$$

Determine how the representation of $H$ on the tangent space

$$
T_pX
$$

constrains the local stability, bifurcations, and normal forms of the stationary point $p$.

For a vector field

$$
\dot{x}=F(x),
$$

this asks how the equivariance condition

$$
F(hx)=hF(x)
$$

restricts the linearization

$$
DF(p).
$$

## Summary

The bridge between groups and dynamical systems is the commutation relation

$$
g\circ f=f\circ g.
$$

A group satisfying this relation acts by symmetries of the dynamical system. Its orbits and stabilizers describe symmetry types of points, and its fixed-point sets are invariant under the dynamics. When such a fixed-point set is a singleton, that point is forced to be stationary.
