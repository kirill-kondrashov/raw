# Bridge between Pacman Renormalization and Noncommutative Motives

This note compares three frameworks:

- Pacman renormalization of holomorphic maps;
- stable categories and universal algebraic K-theory;
- rigid localizing motives.

The dynamical statements below come from the Pacman paper. The categorical
statements come from Blumberg-Gepner-Tabuada and Efimov. A category of Pacmen
and a functor induced by Pacman renormalization require additional
construction. Proposed categorical constructions are marked accordingly.

## References

- [Dudko-Lyubich-Selinger, *Pacmen*](./refs/pacman%20renormalization%201703.01206v3.pdf)
- [Blumberg-Gepner-Tabuada, *A universal characterization of higher algebraic K-theory*](./refs/blumberg-gepner-tabuada-universal-characterization-higher-algebraic-k-theory-1001.2282.pdf)
- [Efimov, *Rigidity of the category of localizing motives*](./refs/efimov-rigidity-category-localizing-motives-2510.17010v1.pdf)

The TeX sources are:
[BGT TeX](./refs/blumberg-gepner-tabuada-universal-characterization-higher-algebraic-k-theory-1001.2282.tex)
and
[Efimov TeX](./refs/efimov-rigidity-category-localizing-motives-2510.17010v1.tex).

## I. Objects in Pacman renormalization

**Definition 1 (Quadratic polynomial).** For $\theta\in\mathbb R/\mathbb Z$, the
quadratic polynomial with multiplier $e^{2\pi i\theta}$ at the origin is
$p_\theta(z)=e^{2\pi i\theta}z+z^2$.

**Definition 2 (Rotation number).** Let $f$ be holomorphic near a fixed point
$\alpha$. Its rotation number is $\theta\in\mathbb R/\mathbb Z$ when
$f'(\alpha)=e^{2\pi i\theta}$.

**Definition 3 (Siegel disk).** Let $f$ be holomorphic near a fixed point
$\alpha$ with irrational rotation number $\theta$. A Siegel disk of $f$ is a
maximal connected domain $Z_f$ containing $\alpha$ for which there is a
biholomorphism $\varphi:Z_f\to\mathbb D$ with $\varphi(\alpha)=0$ and
$\varphi\circ f\circ\varphi^{-1}(z)=e^{2\pi i\theta}z$.

**Definition 4 (Siegel map).** A holomorphic map $f:U\to\mathbb C$ is a
Siegel map when it has a fixed point $\alpha$, a Siegel quasidisk $Z_f$
compactly contained in $U$, and a unique critical point in $U$ on
$\partial Z_f$.

**Definition 5 ($f$-lift).** Let $f:U\to\mathbb C$ be continuous and let
$S\subset\mathbb C$ be connected. An $f$-lift of $S$ is a connected component
of $f^{-1}(S)$.

**Definition 6 (Pullback along an orbit).** Let $f:U\to\mathbb C$ be
continuous, let $S\subset\mathbb C$ be connected, and let

$$
x_0,x_1,\ldots,x_n,
\qquad x_{i+1}=f(x_i),
\qquad x_n\in S,
$$

be an orbit segment with $x_i\in U$ for $0\leq i<n$. The pullback of $S$
along this orbit is the component of $f^{-n}(S)$ containing $x_0$.

**Definition 7 (Full Pacman).** Let $V$ be a closed topological disk, let
$\alpha\in\operatorname{int}(V)$, and let $\gamma_1$ be a simple arc from
$\partial V$ to $\alpha$. A full Pacman is a map $f:U\longrightarrow V$ with
the following properties:

- $U$ is a closed topological disk contained in $V$ and $f(\alpha)=\alpha$.
- $f$ is analytic, and the critical arc $\gamma_1$ has exactly three lifts
  $\gamma_0\subset U$ and $\gamma_-,\gamma_+\subset\partial U$.
  The arc $\gamma_0$ starts at $\alpha$, while $\gamma_-$ and $\gamma_+$
  start at the pre-fixed point $\alpha_0$.
- The critical arc and its three lifts are disjoint away from their prescribed
  endpoints.
- The restriction $f:U\setminus\gamma_0\longrightarrow V\setminus\gamma_1$
  is a two-to-one branched covering.
- The map extends locally conformally through $\partial U\setminus\{\alpha_0\}$.

**Definition 8 (Truncated Pacman).** Let $f:U\to V$ be a full Pacman. Let
$O\subset\operatorname{int}(V)$ be a closed disk with
$\alpha\in\operatorname{int}(O)$, excluding the critical value, and meeting
$\gamma_1$ once. Let $O_0$ and
$O_{\alpha_0}$ be the components of $f^{-1}(O)$ containing $\alpha$ and
$\alpha_0$, respectively. The associated truncated Pacman is
$f:(U\setminus O_{\alpha_0},O_0)\longrightarrow (V,O)$.

Points in $V\setminus O$ have two preimages, and points in $O$ have one
preimage.

**Definition 9 (Non-escaping set).** For a Pacman $f:U\to V$, its non-escaping
set is $K_f=\bigcap_{n\geq 0}f^{-n}(U)$.

**Definition 10 (Escaping set).** For a Pacman $f:U\to V$, its escaping set is
$E_f=V\setminus K_f$.

**Definition 11 (External boundary).** For a Pacman $f:U\to V$, its external
boundary is $\partial_{\mathrm{ext}}U=f^{-1}(\partial V)$.

**Definition 12 (Forbidden boundary).** For a Pacman $f:U\to V$, its forbidden
boundary is $\partial_{\mathrm{frb}}U=\partial U\setminus\partial_{\mathrm{ext}}U$.

**Definition 13 (External-ray lamination).** Let $R\subset V\setminus U$ be a
closed rectangle with bottom side
$B=\partial_{\mathrm{ext}}U$ and top side $T\subset\partial V$. The images of
the vertical segments of $R$ form a lamination, and the external-ray
lamination of $f$ is the lamination obtained by pulling it back through all
iterated preimages $f^{-n}(R)$.

**Definition 14 (External ray).** An external ray of $f$ is an infinite leaf
of the external-ray lamination that starts on $\partial V$. A finite leaf is
an external-ray segment.

**Definition 15 (External-ray angle).** In the notation of Definition 13, let
$B=\partial_{\mathrm{ext}}U$ and let $T\subset\partial V$ be the opposite
side of $R$. Let $\pi:B\to T$ be the identification along the vertical
leaves. The partial map $\phi=\pi^{-1}\circ f:B\dashrightarrow B$ is defined
on $f^{-1}(T)$. Let $A\subset B$ be the set of points with
well-defined forward $\phi$-orbits. The angle map is the unique
orientation-preserving map $\vartheta:A\to S^1$ satisfying
$\vartheta\circ\phi=d_2\circ\vartheta$ with $d_2(z)=z^2$.

The angle of an external-ray segment is the value of $\vartheta$ at its
initial point.

**Definition 16 (Julia set of a Siegel Pacman).** For a Siegel Pacman $f$ with
Siegel disk $Z_f$, its Julia set is $J_f=\bigcup_{n\geq 0}f^{-n}(\partial Z_f)$.

**Definition 17 (Bubble).** Let $f$ be a Siegel Pacman. A bubble of $f$ is
$Z_f$, the component $Z_f'=f^{-1}(Z_f)\setminus Z_f$ attached to $Z_f$, or an
iterated $f$-lift of $Z_f'$.

**Definition 18 (Bubble chain).** A bubble chain is a sequence
$(Z_1,Z_2,\ldots)$ of bubbles such that $Z_1$ is attached to $Z_f$ and
$Z_{n+1}$ is attached to $Z_n$ for every $n\geq 1$.

**Definition 19 (Closed sector).** A closed sector is a closed topological disk
$S$ with two distinguished simple boundary arcs $\beta_-$ and $\beta_+$ that
meet at one point $v$, called the vertex, and bound the sector.

**Definition 20 (Gluing map).** Let $S$ be a closed sector with boundary arcs
$\beta_-$ and $\beta_+$. A gluing map onto a closed topological disk $V$ is a
map $\psi:S\longrightarrow V$ that is conformal on $\operatorname{int}(S)$,
satisfies
$\psi(\beta_-)=\psi(\beta_+)$, and extends conformally near every point of
$\beta_-\cup\beta_+$ other than the vertex.

**Definition 21 (Prepacman).** Let $\beta_0$ be an interior arc of a closed
sector $S$ that divides $S$ into two subsectors $T_-$ and $T_+$. A prepacman is
a triple $(S,f_-,f_+)$ consisting of a pair of holomorphic maps
$f_-:U_-\longrightarrow S$ and $f_+:U_+\longrightarrow S$, where
$U_-\subset T_-$ and $U_+\subset T_+$. It is a prepacman when there is
a gluing map $\psi:S\to V$ for which the pair $(f_-,f_+)$ projects to a
Pacman, with $\beta_-$ and $\beta_+$ projecting to its critical arc and
$\beta_0$ projecting to its critical lift. The defining condition implies that
the branches commute in a neighborhood of $\beta_0$.

**Definition 22 (First-return pre-renormalization).** Let $f:U\to V$ be a
Pacman. A first-return pre-renormalization of $f$ is a prepacman
$G=(g_-=f^a:U_-\to S,\;g_+=f^b:U_+\to S)$
whose branches are first-return iterates to $S$. The orbits of $U_-$ and $U_+$
before returning to $S$ cover a neighborhood of $\alpha$ compactly contained
in $U$.

**Definition 23 (Renormalizable Pacman).** A Pacman is renormalizable when it
admits a first-return pre-renormalization.

**Definition 24 (Pacman renormalization).** Let $G$ be a first-return
pre-renormalization of $f$. The Pacman $g:\widehat U\to\widehat V$ obtained by
gluing the boundary rays of $G$ is the renormalization of $f$, denoted by $Rf$.

**Definition 25 (Prime renormalization).** In Definition 22, the integers $a$
and $b$ are the return times. The renormalization is prime when $a+b=3$.

**Definition 26 (Renormalization triangulation).** Let $G$ be as in Definition
22. Its renormalization triangulation is

$$
\Delta_G=
\bigcup_{i=0}^{a-1}f^i(U_-)\ \cup\
\bigcup_{j=0}^{b-1}f^j(U_+).
$$

It is the union of the orbit pieces visited before the first return.

**Definition 27 (Prime rotation-number renormalization).** The map induced by
prime Pacman renormalization on rotation numbers is

$$
R_{\mathrm{prm}}(\theta)=
\begin{cases}
\dfrac{\theta}{1-\theta}, & 0\leq\theta\leq \dfrac12,\\[6pt]
\dfrac{2\theta-1}{\theta}, & \dfrac12\leq\theta\leq 1.
\end{cases}
$$

**Definition 28 (Periodic rotation numbers).** The set of periodic rotation
numbers is

$$
\Theta_{\mathrm{per}}
=\{\theta\in\mathbb R/\mathbb Z:
R_{\mathrm{prm}}^n(\theta)=\theta\text{ for some }n\geq 1\}.
$$

**Definition 29 (Bounded-type rotation numbers).** The set of bounded-type
rotation numbers is

$$
\Theta_{\mathrm{bnd}}
=\{[\theta]\in\mathbb R/\mathbb Z:\theta\in(0,1)\setminus\mathbb Q
\text{ and the continued-fraction coefficients of }\theta\text{ are bounded}\}.
$$

**Definition 30 (Siegel Pacman).** A Pacman is a Siegel Pacman when it is a
Siegel map with Siegel disk $Z_f$ centered at $\alpha$, its critical arc is a
concatenation of an external ray and an internal ray of $Z_f$, the unique
point of this arc on $\partial Z_f$ is not precritical, and its truncation disk
is bounded by an equipotential in $Z_f$.

**Definition 31 (Combinatorial equivalence).** Two Siegel Pacmen are
combinatorially equivalent when they have the same rotation number and their
distinguished external rays have the same angles.

**Definition 32 (Hybrid equivalence).** Two Siegel Pacmen
$f_i:U_i\to V_i$ are hybrid equivalent when there is a quasiconformal
conjugacy $h:U_1\cup V_1\longrightarrow U_2\cup V_2$
that is conformal on the Siegel disks.

**Theorems from the Pacman paper.** For every $\theta\in\Theta_{\mathrm{per}}$, the Pacman renormalization has a
unique periodic point $f_*$ with rotation number $\theta$. The corresponding
operator is hyperbolic at $f_*$. Its unstable manifold is one-dimensional,
and its stable manifold consists of the corresponding Siegel Pacmen. The
analytic operator is compact on a suitable Banach neighborhood.

If $p_n/q_n$ are continued-fraction approximants to $\theta$, the scaling
theorem gives

$$
|c(\theta)-a_{p_n/q_n}|\sim\frac{1}{q_n^2},
$$

where $c(\theta)$ is the point on the main cardioid and $a_{p_n/q_n}$ is the
satellite center. For Fibonacci denominators, the scale is $\lambda^{-2n}$,
where

$$
\lambda=\frac{1+\sqrt 5}{2}.
$$

The theorem concerns satellite centers. Scaling for entire satellite limbs is
an open problem.

## II. Stable categories and universal invariants

**Definition 33 (Stable infinity-category).** A stable infinity-category is an
infinity-category $\mathcal A$ with a zero object and finite limits and
colimits such that every pushout square is a pullback square.

**Definition 34 (Exact functor).** A functor between stable infinity-categories
is exact when it preserves finite limits and finite colimits.

**Definition 35 (Category of small stable categories).** The category
$\operatorname{Cat}^{\mathrm{ex}}_\infty$ is the category whose objects are
small stable infinity-categories and whose morphisms are exact functors.

**Definition 36 (Perfect stable categories).** The category
$\operatorname{Cat}^{\mathrm{perf}}_\infty$ is the full subcategory of
$\operatorname{Cat}^{\mathrm{ex}}_\infty$ consisting of idempotent-complete
stable infinity-categories, where every idempotent splits.

**Definition 37 (Morita equivalence).** An exact functor
$F:\mathcal A\longrightarrow\mathcal B$ is a Morita equivalence when its
idempotent completion
$\operatorname{Idem}(F)$ is an equivalence:

$$
\operatorname{Idem}(F):
\operatorname{Idem}(\mathcal A)\xrightarrow{\ \simeq\ }
\operatorname{Idem}(\mathcal B).
$$

Equivalently, $F$ induces an equivalence on the corresponding categories of
module objects.

**Definition 38 (Exact sequence).** A sequence
$\mathcal A\longrightarrow\mathcal B\longrightarrow\mathcal C$ in
$\operatorname{Cat}^{\mathrm{perf}}_\infty$ is exact when the composite is
zero, the first functor is fully faithful, and the quotient map identifies the
target with $\mathcal B/\mathcal A\simeq\mathcal C$,
with idempotent completion inserted when required.

**Definition 39 (Split-exact sequence).** An exact sequence
$\mathcal A\to\mathcal B\to\mathcal C$ is split-exact when it admits
compatible adjoint splittings; equivalently, it is equivalent to the sequence
$\mathcal A\longrightarrow\mathcal A\oplus\mathcal C\longrightarrow\mathcal C$
given by inclusion and projection.

**Definition 40 (Additive invariant).** Let $\mathcal D$ be a stable
presentable infinity-category. An additive invariant is a functor
$E:\operatorname{Cat}^{\mathrm{ex}}_\infty\longrightarrow\mathcal D$
satisfying the following conditions:

- $E$ inverts Morita equivalences;
- $E$ preserves filtered colimits;
- $E$ sends split-exact sequences to split cofiber sequences.

**Definition 41 (Localizing invariant).** A localizing invariant is an
additive invariant that sends every exact sequence to a cofiber sequence.

**Definition 42 (Universal additive motive).** The additive motive category
$\operatorname{Mot}_{\mathrm{add}}$ is the stable presentable category
equipped with the universal additive invariant
$\mathcal U_{\mathrm{add}}:\operatorname{Cat}^{\mathrm{ex}}_\infty\longrightarrow\operatorname{Mot}_{\mathrm{add}}$.

Precomposition with $\mathcal U_{\mathrm{add}}$ induces, for every stable
presentable $\mathcal D$, the equivalence

$$
\operatorname{Fun}^{L}(\operatorname{Mot}_{\mathrm{add}},\mathcal D)
\simeq
\operatorname{Fun}_{\mathrm{add}}
(\operatorname{Cat}^{\mathrm{ex}}_\infty,\mathcal D).
$$

**Definition 43 (Universal localizing motive).** The localizing motive
category $\operatorname{Mot}_{\mathrm{loc}}$ is the stable presentable
category equipped with the universal localizing invariant
$\mathcal U_{\mathrm{loc}}:\operatorname{Cat}^{\mathrm{ex}}_\infty\longrightarrow\operatorname{Mot}_{\mathrm{loc}}$.

Precomposition with $\mathcal U_{\mathrm{loc}}$ induces, for every stable
presentable $\mathcal D$, the equivalence

$$
\operatorname{Fun}^{L}(\operatorname{Mot}_{\mathrm{loc}},\mathcal D)
\simeq
\operatorname{Fun}_{\mathrm{loc}}
(\operatorname{Cat}^{\mathrm{ex}}_\infty,\mathcal D).
$$

**Definition 44 (Tensor product).** For
$\mathcal A,\mathcal B\in\operatorname{Cat}^{\mathrm{perf}}_\infty$, their
tensor product is

$$
\mathcal A\widehat\otimes\mathcal B
=
\bigl(\operatorname{Ind}(\mathcal A)\otimes
\operatorname{Ind}(\mathcal B)\bigr)^\omega,
$$

where $\operatorname{Ind}(-)$ is ind-completion and the superscript $\omega$
denotes compact objects.

**Definition 45 (Tensor unit).** The tensor unit is
$\mathbb S^\omega$, the category of compact spectra.

**Definition 46 (Proper stable category).** A small stable category
$\mathcal A$ is proper when $\operatorname{Map}_{\mathcal A}(x,y)$ is a
compact spectrum for every $x,y\in\mathcal A$.

**Definition 47 (Smooth stable category).** A small stable category
$\mathcal A$ is smooth when it is a perfect module over
$\mathcal A^{\mathrm{op}}\widehat\otimes\mathcal A$.

Here $\mathcal A$ is regarded as the bimodule given by its mapping spectra,
and perfect means belonging to the smallest subcategory of modules containing
the representable modules and closed under finite colimits and retracts.

**Definition 48 (Dualizable object).** Let $\mathcal C^\otimes$ be a symmetric
monoidal infinity-category. An object $\mathcal A\in\mathcal C$ is
dualizable when there are an object $\mathcal A^\vee$, an evaluation map
$\mathcal A\otimes\mathcal A^\vee\to\mathbb 1$, and a coevaluation map
$\mathbb 1\to\mathcal A^\vee\otimes\mathcal A$ such that

$$
\mathcal A\simeq\mathcal A\otimes\mathbb 1
\longrightarrow\mathcal A\otimes\mathcal A^\vee\otimes\mathcal A
\longrightarrow\mathbb 1\otimes\mathcal A\simeq\mathcal A
$$

and

$$
\mathcal A^\vee\simeq\mathbb 1\otimes\mathcal A^\vee
\longrightarrow\mathcal A^\vee\otimes\mathcal A\otimes\mathcal A^\vee
\longrightarrow\mathcal A^\vee\otimes\mathbb 1\simeq\mathcal A^\vee
$$

are identity maps.

**Theorem 1 (BGT dualizability criterion).** An object
$\mathcal A\in\operatorname{Cat}^{\mathrm{perf}}_\infty$ is dualizable if and
only if it is smooth and proper. Its dual is
$\mathcal A^{\mathrm{op}}$.

**Theorem 2 (BGT corepresentability of connective K-theory).** For
$\mathcal A\in\operatorname{Cat}^{\mathrm{perf}}_\infty$, connective
K-theory is corepresented by the additive motive:

$$
\operatorname{Map}\bigl(
\mathcal U_{\mathrm{add}}(\mathbb S^\omega),
\mathcal U_{\mathrm{add}}(\mathcal A)
\bigr)
\simeq K(\mathcal A).
$$

**Theorem 3 (BGT corepresentability of non-connective K-theory).** For
$\mathcal A\in\operatorname{Cat}^{\mathrm{perf}}_\infty$, non-connective
K-theory is corepresented by the localizing motive:

$$
\operatorname{Map}\bigl(
\mathcal U_{\mathrm{loc}}(\mathbb S^\omega),
\mathcal U_{\mathrm{loc}}(\mathcal A)
\bigr)
\simeq \mathbb K(\mathcal A).
$$

The non-connective theory is obtained from cone and suspension constructions,
schematically

$$
\mathbb K(\mathcal A)
=
\operatorname*{colim}_{n}
\Omega^n K\bigl(\Sigma_\kappa^{(n)}\mathcal A\bigr).
$$

**Definition 49 (Topological Hochschild homology).**
$\operatorname{THH}$ is the localizing invariant given by topological
Hochschild homology of a spectral-category model of $\mathcal A$.

**Definition 50 (Topological cyclic homology).**
$\operatorname{TC}$ is the cyclotomic fixed-point construction applied to
$\operatorname{THH}$.

**Definition 51 (Topological Dennis trace).** The topological Dennis trace is
the natural transformation
$\operatorname{tr}_{\mathrm{D}}:K\longrightarrow\operatorname{THH}$.

**Definition 52 (Cyclotomic trace).** The cyclotomic trace is the natural
transformation $\operatorname{tr}_{\mathrm{cyc}}:K\longrightarrow\operatorname{TC}$.

In BGT, $\operatorname{TC}$ need not preserve filtered colimits.

## III. Efimov's rigid localizing motives

**Definition 53 (Dualizable $\mathcal E$-module).** Let $\mathcal E$ be a
rigid $E_1$-monoidal presentable stable category. A dualizable
$\mathcal E$-module is a presentable stable left $\mathcal E$-module that is
dualizable as an object of the monoidal category of $\mathcal E$-modules.

**Definition 54 (Strongly continuous functor).** Let $\mathcal C$ and
$\mathcal D$ be presentable stable categories. A colimit-preserving functor
$F:\mathcal C\to\mathcal D$ is strongly continuous when it has a right adjoint
$F^R$ that preserves colimits.

**Definition 55 (Category of dualizable $\mathcal E$-modules).** The category
$\operatorname{Cat}^{\mathrm{dual}}_{\mathcal E}$ is the category whose
objects are dualizable $\mathcal E$-modules and whose
morphisms are strongly continuous $\mathcal E$-linear functors.

**Definition 56 (Relatively compactly generated module).** An
$\mathcal E$-module is relatively compactly generated when it is generated
under colimits by a small subcategory of compact $\mathcal E$-module
objects. The category of such modules is denoted
$\operatorname{Cat}^{\mathrm{cg}}_{\mathcal E}$.

**Definition 57 (Relative localizing motive).** Let $\mathcal E$ be a rigid
$E_1$-monoidal category and let $\kappa$ be a regular cardinal. The relative
localizing motive category
$\operatorname{Mot}^{\mathrm{loc}}_{\mathcal E,\kappa}$ is the accessible
stable category with $\kappa$-filtered colimits equipped with the universal
$\kappa$-finitary localizing invariant

$$
\mathcal U_{\mathrm{loc},\kappa}:
\operatorname{Cat}^{\mathrm{dual}}_{\mathcal E}
\longrightarrow
\operatorname{Mot}^{\mathrm{loc}}_{\mathcal E,\kappa}.
$$

Precomposition with $\mathcal U_{\mathrm{loc},\kappa}$ induces the equivalence

$$
\operatorname{Fun}_{\mathrm{loc},\kappa}
(\operatorname{Cat}^{\mathrm{dual}}_{\mathcal E},\mathcal T)
\simeq
\operatorname{Fun}^{\kappa\text{-cont}}
(\operatorname{Mot}^{\mathrm{loc}}_{\mathcal E,\kappa},\mathcal T)
$$

for every accessible stable category $\mathcal T$ with $\kappa$-filtered
colimits. Write
$\operatorname{Mot}^{\mathrm{loc}}_{\mathcal E}$ for
$\operatorname{Mot}^{\mathrm{loc}}_{\mathcal E,\omega}$.

**Definition 58 (Relative tensor product).** For a dualizable left
$\mathcal E$-module $\mathcal C$ and a dualizable left
$\mathcal E^{\mathrm{mop}}$-module $\mathcal D$, their relative tensor product
$\mathcal D\otimes_{\mathcal E}\mathcal C$ is characterized by the universal
property of balanced $\mathcal E$-bilinear colimit-preserving functors.

The universal invariant carries this relative tensor product to the tensor
product of motives:

$$
\mathcal U_{\mathrm{loc}}(\mathcal C)\otimes
\mathcal U_{\mathrm{loc}}(\mathcal D)
\simeq
\mathcal U_{\mathrm{loc}}(\mathcal D\otimes_{\mathcal E}\mathcal C).
$$

**Definition 59 (Rigid $E_1$-monoidal category).** A presentable stable
$E_1$-monoidal category $\mathcal E$ is rigid when its unit
$\mathbb 1_{\mathcal E}$ is compact and its multiplication functor
$\mu:\mathcal E\otimes\mathcal E\longrightarrow\mathcal E$
has a colimit-preserving right adjoint that is
$\mathcal E$-$\mathcal E$-linear.

**Definition 60 (Multiplicative opposite).** For an $E_1$-monoidal category
$\mathcal E$, the multiplicative opposite $\mathcal E^{\mathrm{mop}}$ is the
$E_1$-monoidal category with the same underlying category as $\mathcal E$ and
with the order of the tensor product reversed.

**Theorem 4 (Efimov's rigidity theorem).** Let $\mathcal E$ be a rigid
$E_1$-monoidal category. Then $\operatorname{Mot}^{\mathrm{loc}}_{\mathcal E}$
is dualizable and

$$
\bigl(\operatorname{Mot}^{\mathrm{loc}}_{\mathcal E}\bigr)^\vee
\simeq
\operatorname{Mot}^{\mathrm{loc}}_{\mathcal E^{\mathrm{mop}}}.
$$

For $E_2$-monoidal $\mathcal E$, the category
$\operatorname{Mot}^{\mathrm{loc}}_{\mathcal E}$ is rigid. Its evaluation is
given on generators by continuous K-theory of relative tensor products:

$$
\operatorname{ev}\bigl(
\mathcal U_{\mathrm{loc}}(\mathcal C)\otimes
\mathcal U_{\mathrm{loc}}(\mathcal D)\bigr)
\simeq
K^{\mathrm{cont}}(\mathcal D\otimes_{\mathcal E}\mathcal C).
$$

**Definition 61 (Relative internal Hom).** For dualizable $\mathcal E$-modules
$\mathcal C$ and $\mathcal D$, the relative internal Hom
$\operatorname{Hom}^{\mathrm{dual}}_{\mathcal E}(\mathcal C,\mathcal D)$ is
characterized by

$$
\operatorname{Map}_{\operatorname{Cat}^{\mathrm{dual}}_{\mathcal E}}\bigl(
\mathcal B,\operatorname{Hom}^{\mathrm{dual}}_{\mathcal E}(\mathcal C,\mathcal D)
\bigr)
\simeq
\operatorname{Map}_{\operatorname{Cat}^{\mathrm{dual}}_{\mathcal E}}\bigl(
\mathcal B\otimes_{\mathcal E}\mathcal C,\mathcal D
\bigr)
$$

for dualizable $\mathcal E$-modules $\mathcal B$.

**Definition 62 (Trace-class morphism).** Let $\mathcal V$ be a symmetric
monoidal category with internal Homs. A morphism $u:X\to Y$ is trace-class
when the adjunct $\mathbb 1\longrightarrow\operatorname{Hom}_{\mathcal V}(X,Y)$
factors through

$$
\operatorname{Hom}_{\mathcal V}(X,\mathbb 1)\otimes Y
\longrightarrow
\operatorname{Hom}_{\mathcal V}(X,Y).
$$

**Definition 63 (Right trace-class functor).** Let $\mathcal C$ and
$\mathcal D$ be dualizable $\mathcal E$-modules. A strongly continuous
$\mathcal E$-linear functor $F:\mathcal C\to\mathcal D$ is right trace-class
over $\mathcal E$ when it lies in the essential image of

$$
\bigl(
\operatorname{Hom}^{\mathrm{dual}}_{\mathcal E}(\mathcal C,\mathcal E)
\otimes_{\mathcal E}\mathcal D
\bigr)^\omega
\longrightarrow
\bigl(
\operatorname{Hom}^{\mathrm{dual}}_{\mathcal E}(\mathcal C,\mathcal D)
\bigr)^\omega
\simeq
\operatorname{Fun}^{LL}_{\mathcal E}(\mathcal C,\mathcal D).
$$

**Definition 64 (Nuclear module).** A relatively compactly generated
$\mathcal E$-module $\mathcal C$ is nuclear over $\mathcal E$ when, for every
$\omega_1$-compact $\mathcal D\in
(\operatorname{Cat}^{\mathrm{cg}}_{\mathcal E})_{\omega_1}$ and every strongly
continuous $\mathcal E$-linear functor $F:\mathcal D\to\mathcal C$, compactness
of $F$ as a morphism in $\operatorname{Cat}^{\mathrm{cg}}_{\mathcal E}$
implies that $F$ is right trace-class over $\mathcal E$.

**Definition 65 (Basic nuclear module).** A relatively compactly generated
$\mathcal E$-module $\mathcal C$ is basic nuclear when there is a sequential
diagram $\mathcal C_0\longrightarrow\mathcal C_1\longrightarrow\cdots$
with right trace-class transition functors and
$\mathcal C\simeq\operatorname*{colim}_{n}\mathcal C_n$.

Efimov also studies Calkin categories and corepresentability for topological
restriction and cyclic homology.

## IV. Proposed correspondences

The status column records the level of construction required for each
correspondence.

| Pacman datum | Candidate categorical datum | Status |
| --- | --- | --- |
| A Pacman $f:U\to V$ | An object of a category of finite or analytic dynamical models | Requires a category |
| A conformal or hybrid conjugacy | A morphism or equivalence of models | Choice of morphisms |
| A prepacman $(f_-,f_+)$ | A two-branch diagram or correspondence | Candidate encoding |
| The gluing map $\psi$ | A quotient, cofiber, or localization functor | Requires a stable model |
| First-return data $(a,b)$ | A filtered diagram or exact endofunctor | Requires a construction |
| Renormalization triangulation $\Delta_G$ | A filtration by sectors, rays, and return pieces | Candidate filtration |
| A renormalization $Rf$ | An exact endofunctor $R_*:\mathcal A\to\mathcal A$ | Requires a construction |
| Hybrid equivalence classes | Equivalence classes before Morita localization | Choice of morphisms |
| A periodic Pacman $f_*$ | A periodic object or motive under $R_*$ | Requires $R_*$ |
| Bubble chains and external rays | Generators or incidence objects in a spectral category | Model-dependent |
| The stable/unstable decomposition at $f_*$ | A filtration or decomposition in a realization | Requires a realization |
| The scale $\lambda^{-2}$ | An eigenvalue of a realized endomorphism | Requires a comparison |
| A finite marked model $P$ | A compact connected parameter set $Q_n(P)\subset\mathcal M$ | Definition 73 |
| MLC for $\mathcal M$ | The connected-neighborhood condition in Definition 74 | Requires a parameter realization |

The analytic operator $R$ acts on a Banach neighborhood of maps. BGT and
Efimov use stable categories and exact functors. A boundary gluing becomes a
categorical cofiber only after a categorical quotient has been specified.

## V. Candidate categorical construction

**Definition 66 (Finite marked Pacman model).** Fix $n\geq 0$ and a finite
marking $\mathfrak m_n=(E_n,B_n,I_n)$, where $E_n$ is a finite set of
external-ray segments, $B_n$ is a finite set of bubbles, and $I_n$ is their
incidence relation $I_n\subseteq(E_n\cup B_n)^2$ as in Definitions 13 and 17.
A finite marked Pacman model
of depth $n$ is a tuple $P=(f,S,G,\psi,\mathfrak m_n)$, where $f$ is a Siegel
Pacman with the truncated data of Definition 8, $S$ is a closed sector
(Definition 19), $G=(g_-:U_-\to S,g_+:U_+\to S)$ is a chosen first-return
pre-renormalization (Definition 22), and $\psi:S\to\widehat V$ is its gluing
map (Definition 20), with $Rf:\widehat U\to\widehat V$ as in Definition 24.

**Definition 67 (Marked morphism).** For finite marked Pacman models
$P=(f,S,G,\psi,\mathfrak m_n)$ and
$P'=(f',S',G',\psi',\mathfrak m'_n)$, a marked morphism
$P\to P'$ is a tuple $(h,\widetilde h,\widehat h)$ in which $h$ and
$\widehat h$ are hybrid conjugacies (Definition 32) for $f$ and $Rf$,
respectively, $\widetilde h:S\to S'$ is a homeomorphism preserving the
distinguished boundary arcs, and
$h(U_\pm)=U'_\pm$, $\widetilde h\circ g_\pm=g'_\pm\circ h|_{U_\pm}$,
$\widehat h\circ\psi=\psi'\circ\widetilde h$,
$\widehat h\circ Rf=Rf'\circ\widehat h$, and
$h(\mathfrak m_n)=\mathfrak m'_n$.

**Definition 68 (Finite marked-model category).** The category
$\mathscr P_n$ is the topological category whose objects are the finite
marked Pacman models of Definition 66 and whose morphism spaces are the
marked morphisms of Definition 67 with the compact-open topology. Composition
is componentwise.

**Definition 69 (Spectral enhancement).** After choosing a small skeleton of
$\mathscr P_n$, its spectral enhancement $\mathcal S_n$ is the spectral
category with the same objects and mapping spectra
$\mathcal S_n(P,Q)=\Sigma^\infty_+\operatorname{Map}_{\mathscr P_n}(P,Q)$.

**Definition 70 (Perfect categorical model).** The perfect categorical model
associated to $\mathcal S_n$ is
$\mathcal A_n=\operatorname{Perf}(\mathcal S_n)$, where
$\operatorname{Perf}(\mathcal S_n)$ is the idempotent-complete stable
subcategory of $\operatorname{Mod}_{\mathcal S_n}$ generated by the
representable modules. Thus $\mathcal A_n$ is an object of
$\operatorname{Cat}^{\mathrm{perf}}_\infty$ (Definition 36).

**Definition 71 (Refinement system).** A refinement system is a sequence of
marking-preserving functors
$\rho_n:\mathscr P_n\to\mathscr P_{n+1}$ whose induced spectral functors
$r_n:\mathcal S_n\to\mathcal S_{n+1}$ preserve perfect modules under
extension of scalars. The resulting exact functors are
$\rho_{n,!}(M)=M\otimes_{\mathcal S_n}\mathcal S_{n+1}$, and the associated
stable category is $\mathcal A=\operatorname*{colim}_n\mathcal A_n$ in
$\operatorname{Cat}^{\mathrm{perf}}_\infty$, where
$\mathcal S_{n+1}$ is regarded as an
$\mathcal S_n$-$\mathcal S_{n+1}$-bimodule via $r_n$. Morita compatibility is
required.

**Definition 72 (Categorical renormalization).** A categorical
renormalization is a compatible family of marking-preserving functors
$\mathfrak R_n:\mathscr P_n\to\mathscr P_n$ whose object component sends a
model with underlying Pacman $f$ to a model with underlying Pacman $Rf$ from
Definition 24, and whose morphism component has Pacman component
$\widehat h$. Compatibility means
$\mathfrak R_{n+1}\circ\rho_n\simeq\rho_n\circ\mathfrak R_n$. If the induced
spectral functors preserve perfect modules, they define an exact endofunctor
$R_*:\mathcal A\to\mathcal A$.

**Definition 73 (Parameter realization).** Let $\mathcal M$ be the Mandelbrot
set for the quadratic family $z^2+c$, and let $\mathcal K(\mathcal M)$ denote
its nonempty compact subsets. A parameter realization of a refinement system
is a family of maps
$Q_n:\operatorname{Ob}(\mathscr P_n)\to\mathcal K(\mathcal M)$ such that
each $Q_n(P)$ is connected, $Q_n$ is invariant under isomorphisms in
$\mathscr P_n$,
$Q_{n+1}(\rho_nP)\subseteq Q_n(P)$, and the intersection of the sets along
every compatible chain $\rho_n(P_n)=P_{n+1}$ satisfies
$\bigcap_{n\geq 0}Q_n(P_n)\neq\varnothing$.

**Definition 74 (MLC-compatible parameter realization).** A parameter
realization is MLC-compatible when, for every $c\in\mathcal M$ and every
relative neighborhood $O$ of $c$ in $\mathcal M$, there are $n$ and
$P\in\operatorname{Ob}(\mathscr P_n)$ such that
$c\in\operatorname{int}_{\mathcal M}Q_n(P)\subseteq Q_n(P)\subseteq O$.
Equivalently, the realized sets form a basis of connected neighborhoods in
$\mathcal M$. Here MLC means local connectivity of the Mandelbrot set
$\mathcal M$.

Definitions 66-74 are additional structures. They are not supplied by the
three source frameworks.

## VI. Consequences of Definitions 66-74

**First-return localization.** If the gluing map $\psi$ in Definition 66 is
represented by an exact sequence in
$\operatorname{Cat}^{\mathrm{perf}}_\infty$ (Definition 38)

$$
\mathcal A_{\mathrm{discarded}}
\longrightarrow
\mathcal A_{\mathrm{return}}
\longrightarrow
\mathcal A_{\mathrm{renormalized}},
$$

then every localizing invariant $E$ (Definition 41) gives a cofiber sequence

$$
E(\mathcal A_{\mathrm{discarded}})
\longrightarrow
E(\mathcal A_{\mathrm{return}})
\longrightarrow
E(\mathcal A_{\mathrm{renormalized}}).
$$

Taking $E=\mathbb K$ uses Theorem 3. The quotient functor must identify
boundary gluing with this cofiber.

**Renormalization dynamics.** Definition 72 gives an exact endofunctor
$R_*:\mathcal A\to\mathcal A$ and hence the motive endomorphism
$\mathcal U_{\mathrm{loc}}(R_*)$ by Definition 43. If a periodic Pacman
$f_*$ is represented by $\mathcal A_*$ and the encoding intertwines the two
actions, then $R^p f_*=f_*$ implies
$R_*^p\mathcal A_*\simeq\mathcal A_*$.

**Traces.** If $\mathcal A$ is dualizable (Definition 48 and Theorem 1), the
endomorphism $R_*$ has a trace
$\operatorname{Tr}(R_*)\in
\operatorname{Map}_{\operatorname{Mot}_{\mathrm{loc}}}(\mathbb 1,\mathbb 1)$
in the tensor unit. Definitions 53-63 and Theorem 4 give the relative
version. A
comparison with rays or bubbles requires an incidence functor $\Phi$ and an
orbit endomorphism $\mathfrak r$ with
$\Phi\circ\mathfrak r\simeq R_*\circ\Phi$.

**Parameter neighborhoods.** A parameter realization (Definition 73) gives
nested connected compact subsets of the Mandelbrot set. An
MLC-compatible realization (Definition 74) gives a basis of connected
neighborhoods; this condition implies local connectivity of $\mathcal M$.
The categorical construction therefore contributes to MLC only after such a
realization has been constructed.

**Scaling.** Let $D R_{f_*}$ be the derivative of analytic renormalization at
a periodic point. If a realization
$\mathcal L:\operatorname{Mot}_{\mathrm{loc}}\to\mathcal V$ has a
finite-dimensional invariant subquotient $W$ on which
$\mathcal L(\mathcal U_{\mathrm{loc}}(R_*))$ is conjugate to $D R_{f_*}$,
its spectral data can be compared with the parameter sets of Definition 73.
Recovering the golden-mean factor $\lambda^{-2}$, where
$\lambda=(1+\sqrt 5)/2$, additionally requires diameter estimates for those
sets.

## VII. Requirements for a categorical theorem

A categorical theorem must construct Definitions 66-74 and prove that the
refinement, renormalization, gluing, and parameter-realization maps are
compatible. It must establish exactness and Morita invariance in
$\operatorname{Cat}^{\mathrm{perf}}_\infty$, the dualizability or nuclearity
conditions needed for Definitions 53-65 and Theorem 4, and the parameter
nesting and neighborhood condition in Definition 74.

## Open problems

**Open Problem 1 (Finite marked-model categories).** For each $n\geq 0$,
define $\operatorname{Map}_{\mathscr P_n}(P,P')$ as the subspace of the
product of mapping spaces consisting of tuples
$(h,\widetilde h,\widehat h)$ satisfying all equations in Definition 67,
with the product compact-open topology. Prove that these spaces have
continuous identities and componentwise composition, that $\mathscr P_n$
admits a small skeleton, and that
$\mathcal S_n(P,Q)=\Sigma^\infty_+
\operatorname{Map}_{\mathscr P_n}(P,Q)$ is independent up to Morita
equivalence of the admissible truncation, marking, and representative choices.

**Missing from Sections V and VI.** Section V specifies the tuples and
equations but does not prove closure under composition, smallness, or
independence of choices. Section VI assumes that $\mathscr P_n$ and
$\mathcal A_n=\operatorname{Perf}(\mathcal S_n)$ already exist.

**Open Problem 2 (Refinement system).** Given the categories $\mathscr P_n$,
define $\rho_n$ on objects and morphisms so that the marking at depth $n+1$
restricts to the marking at depth $n$. Prove that $\rho_n$ is continuous,
that it induces a spectral functor
$r_n:\mathcal S_n\to\mathcal S_{n+1}$, and that
$F_n(M)=M\otimes_{\mathcal S_n}\mathcal S_{n+1}$, with its
$r_n$-induced bimodule structure, maps perfect modules to perfect modules.
Prove that each $F_n$ is exact, that
$\mathcal A=\operatorname*{colim}_n\mathcal A_n$ is an object of
$\operatorname{Cat}^{\mathrm{perf}}_\infty$, and that Morita-equivalent
refinement systems have equivalent colimits.

**Missing from Sections V and VI.** Definitions 69-71 give the mapping-spectrum
and extension-of-scalars formulas but no refinement maps or compactness proof.
Section VI assumes the colimit and its transition functors without proving
their existence, exactness, or Morita invariance.

**Open Problem 3 (Exact gluing sequence).** For each marked model, define
stable idempotent-complete categories
$\mathcal A_{\mathrm{discarded}}$ and $\mathcal A_{\mathrm{return}}$ and an
exact functor
$i:\mathcal A_{\mathrm{discarded}}\to\mathcal A_{\mathrm{return}}$ whose
image is the discarded boundary sector. Define the quotient functor
$q:\mathcal A_{\mathrm{return}}\to\mathcal A_{\mathrm{renormalized}}$ from
the gluing map $\psi$ and prove that $i$ is fully faithful and that
$\operatorname{Idem}(\mathcal A_{\mathrm{return}}/\operatorname{im}(i))
\simeq\mathcal A_{\mathrm{renormalized}}$. Then prove, for every localizing
invariant $E$, the induced sequence is a cofiber sequence, including
$E=\mathbb K$.

**Missing from Sections V and VI.** Definition 66 supplies the point-set map
$\psi$ but no stable categories, quotient, or exact functors. Section VI
assumes both the exact sequence and its identification with the renormalized
model.

**Open Problem 4 (Categorical renormalization).** For every $n$, define a
continuous endofunctor $\mathfrak R_n:\mathscr P_n\to\mathscr P_n$ on the
full model and morphism data, with underlying Pacman $f$ sent to $Rf$ and a
morphism component whose renormalized conjugacy is $\widehat h$. Prove the
coherent natural equivalences
$\mathfrak R_{n+1}\rho_n\simeq\rho_n\mathfrak R_n$ and prove that the
induced endofunctor $R_*:\mathcal A\to\mathcal A$ is exact. For an analytic
period-$p$ Pacman $f_*$, define a corresponding $\mathcal A_*$ and prove an
equivalence $\eta:R_*^p\mathcal A_*\simeq\mathcal A_*$ satisfying
$\eta\circ R_*^p(\alpha_*)\simeq\alpha_*\circ\eta$ for the rotation
automorphism $\alpha_*$, with this action identified with
$R_{\mathrm{prm}}^p$.

**Missing from Sections V and VI.** Definition 72 prescribes the desired
object and morphism behavior only conditionally on perfectness and
compatibility. Section VI assumes the functors, the exact colimit endomorphism,
and the periodic encoding.

**Open Problem 5 (Parameter loci).** For every $c\in\mathcal M$ and $n\geq 0$,
define the set $\mathscr D_n(c)$ of depth-$n$ marked Pacman data extracted
from $p_c(z)=z^2+c$, including its domains, first-return maps, gluing map,
and external-ray and bubble marking. Define
$\operatorname{Real}_n(P,c)$ to mean that some element of $\mathscr D_n(c)$
is marked-hybrid-equivalent to $P$, and set
$Q_n(P)=\{c\in\mathcal M:\operatorname{Real}_n(P,c)\}$. Prove that every
$Q_n(P)$ is nonempty, compact, and connected, that marked-isomorphic models
have equal loci, that
$Q_{n+1}(\rho_nP)\subseteq Q_n(P)$, and that every chain
$\rho_n(P_n)=P_{n+1}$ has nonempty intersection of its loci.

**Missing from Sections V and VI.** Definition 73 imposes the required
properties of $Q_n(P)$ but does not define the extraction $\mathscr D_n(c)$
or the predicate $\operatorname{Real}_n$. Section VI assumes that these
parameter loci already exist and therefore proves none of their geometric
properties.

**Open Problem 6 (MLC neighborhood basis).** For the loci from Open Problem 5,
prove the quantified statement
for every $c\in\mathcal M$ and every relative open set
$O\subseteq\mathcal M$ with $c\in O$, there exist $n\geq 0$ and
$P\in\operatorname{Ob}(\mathscr P_n)$ such that
$c\in\operatorname{int}_{\mathcal M}Q_n(P)\subseteq Q_n(P)\subseteq O$.
Together with connectedness of the $Q_n(P)$, prove that these sets form a
basis of connected neighborhoods and hence that $\mathcal M$ is locally
connected.

**Missing from Sections V and VI.** Definition 74 states this neighborhood
basis as a target and supplies no construction of $n$ or $P$ for a given
$(c,O)$. Section VI establishes only the implication from the target condition
to MLC.

**Open Problem 7 (Categorical traces).** Prove that $\mathcal A$ is smooth and
proper by proving compactness of all mapping spectra and perfectness of the
diagonal bimodule; equivalently, provide the duality data in
$\operatorname{Cat}^{\mathrm{perf}}_\infty$. For each coefficient category
$\mathcal E_\theta$ used in the construction, prove that the corresponding
Ind-completed modules are dualizable and that the Ind-extended refinement and
renormalization functors satisfy the right trace-class or nuclearity
conditions in Definitions 53-65. Define a category $\mathcal R$ of ray-bubble
data, an incidence functor $\Phi:\mathcal R\to\mathcal A$, and an orbit
endomorphism $\mathfrak r:\mathcal R\to\mathcal R$ with
$\Phi\circ\mathfrak r\simeq R_*\circ\Phi$. Show that the induced trace classes
in $K$, $\operatorname{THH}$, and $\operatorname{TC}$ are well-defined and
prove their
compatibility with the corresponding periodic ray and bubble-chain
invariants.

**Missing from Sections V and VI.** Definitions 48 and 53-65 give criteria
for duality and trace-class behavior but do not verify them for this system.
Section VI assumes dualizability and the incidence comparison before invoking
traces.

**Open Problem 8 (Scaling comparison).** Choose a linear symmetric monoidal
category $\mathcal V$ with finite-dimensional invariant subquotients and
eigenvalues, and define an exact symmetric monoidal functor
$\mathcal L:\operatorname{Mot}_{\mathrm{loc}}\to\mathcal V$. Define invariant
finite-dimensional subquotients $W$ of
$\mathcal L(\mathcal U_{\mathrm{loc}}(\mathcal A))$ and $W_{f_*}$ of the
tangent representation at $f_*$, together with an isomorphism
$\gamma:W\to W_{f_*}$ satisfying
$\gamma\circ\mathcal L(\mathcal U_{\mathrm{loc}}(R_*))|_W
=D R_{f_*}|_{W_{f_*}}\circ\gamma$. For every compatible chain
$\rho_n(P_n)=P_{n+1}$ represented by $f_*$, prove uniform constants
$C>0$ and $0<\alpha<1$ with
$\operatorname{diam}Q_n(P_n)\leq C\alpha^n$. In the golden-mean case, prove
an explicit comparison theorem between the center estimate
$|c(\theta)-a_{p_n/q_n}|\asymp\lambda^{-2n}$ and the loci $Q_n(P_n)$:
under stated hypotheses, either derive
$\operatorname{diam}Q_n(P_n)=O(\lambda^{-2n})$ or identify the additional
geometric estimate required for that conclusion. Finally, identify the stable
and unstable subspaces of $D R_{f_*}$ and prove inequalities transferring
their contraction and expansion estimates to the parameter-diameter bound.

**Missing from Sections V and VI.** Section V defines neither the realization
$\mathcal L$ nor the comparison with the analytic tangent representation.
Section VI assumes both and consequently supplies no parameter-diameter
estimate; the satellite-center scaling theorem does not by itself control
diameters of entire parameter loci.

**Contribution to MLC.** Open Problems 1-4 provide the finite categorical
objects, exact refinement, gluing localization, and renormalization dynamics.
Open Problems 5-6 provide the parameter realization and the connected-
neighborhood basis required for MLC. Open Problems 7-8 supply trace and
scaling data that may control periodic and non-shrinking renormalization
pieces. The MLC implication is obtained by proving Definition 74 for the
parameter sets constructed in Open Problem 5.

**Role of K-theory and Efimov's framework.** BGT's localizing invariants send
the exact sequence in Open Problem 3 to a cofiber sequence, and Theorem 3
identifies non-connective K-theory as corepresented by the localizing motive.
THH and the trace maps of Definitions 49-52 provide further functorial data
for $R_*$. Efimov's relative motives place rotation data in a coefficient
category $\mathcal E_\theta$ and provide duality, trace-class, and nuclearity
tools for the infinite system in Open Problems 2 and 4. An MLC application
requires a proved comparison from these invariants to the parameter sets
$Q_n(P)$, including connectedness and diameter control.

## Summary

Definitions 66-72 associate finite marked Pacman models with a perfect stable
category $\mathcal A$ and an exact renormalization endomorphism $R_*$.
Definitions 73-74 assign nested connected compact parameter sets
$Q_n(P)\subset\mathcal M$ and formulate the connected-neighborhood criterion
for MLC.

**MLC connection program.** Define $Q_n(P)$ from the parameter loci realizing
the first $n$ marked renormalization data. Prove nonemptiness, connectedness,
refinement nesting, compatible-chain intersections, and the neighborhood
condition in Definition 74; prove diameter estimates such as the
golden-mean scale $\lambda^{-2}$ when scaling is included. BGT localizing
invariants turn categorical gluing into cofiber sequences, while Efimov's
relative motives provide duality and trace-class or nuclearity tools for
infinite refinement systems. An MLC theorem requires a comparison showing that
these categorical invariants imply the connected-neighborhood and diameter
properties of the sets $Q_n(P)$.
