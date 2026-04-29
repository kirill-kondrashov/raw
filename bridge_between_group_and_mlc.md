# Bridge Between a Special Group G and MLC

## Definitions related to the quotient space $\mathcal{S}$

Let $\mathcal{M} \subset \mathbb{C}$ be the Mandelbrot set. Let $\mathcal{K}(\mathcal{M})$ denote the collection of nonempty compact subsets of $\mathcal{M}$. Let
$$
\mathcal{A} = \{K \subset \mathbb{C} : K \text{ is compact and } K \cong D^2\},
$$
where $D^2$ is the closed unit disk and $\cong$ denotes homeomorphism.

For $m \in \mathcal{K}(\mathcal{M})$ and $\varepsilon > 0$, define
$$
\mathcal{A}_\varepsilon(m) = \{K \in \mathcal{A} : m \subset K \text{ and } d_H(K,m) < \varepsilon\},
$$
where $d_H$ denotes the Hausdorff distance on nonempty compact subsets of $\mathbb{C}$.

Define a relation $\sim_{\mathrm{comp}}$ on $\mathcal{K}(\mathcal{M})$ by
$$
m_1 \sim_{\mathrm{comp}} m_2
\quad\Longleftrightarrow\quad
\mathcal{A}_\varepsilon(m_1) = \mathcal{A}_\varepsilon(m_2)
\text{ for every } \varepsilon > 0.
$$

Define
$$
\mathcal{S} = \mathcal{K}(\mathcal{M})/\sim_{\mathrm{comp}}
$$
and let
$$
q \colon \mathcal{K}(\mathcal{M}) \to \mathcal{S}
$$
denote the quotient map.

Define
$$
\iota \colon \mathcal{M} \to \mathcal{K}(\mathcal{M}),
\qquad
\iota(c) = \{c\},
$$
and
$$
\pi = q \circ \iota \colon \mathcal{M} \to \mathcal{S}.
$$
Thus
$$
\pi = q \circ \iota .
$$

Let $X_{\mathcal{S}}$ be a simplicial complex and let
$$
\rho \colon \pi(\mathcal{M}) \to |X_{\mathcal{S}}|
$$
be a continuous map, where $|X_{\mathcal{S}}|$ denotes the geometric realization of $X_{\mathcal{S}}$. Then
$$
\rho \circ \pi \colon \mathcal{M} \to |X_{\mathcal{S}}|
$$
is a continuous map.

Let
$$
C_\bullet(X_{\mathcal{S}};\mathbb{Z}) \colon \cdots \to C_2(X_{\mathcal{S}};\mathbb{Z}) \xrightarrow{\partial_2} C_1(X_{\mathcal{S}};\mathbb{Z}) \xrightarrow{\partial_1} C_0(X_{\mathcal{S}};\mathbb{Z}) \to 0
$$
denote the simplicial chain complex of $X_{\mathcal{S}}$ with integer coefficients.

For an abelian group $A$, define
$$
C_\bullet(X_{\mathcal{S}};A) = C_\bullet(X_{\mathcal{S}};\mathbb{Z}) \otimes_{\mathbb{Z}} A
$$
and
$$
H_n(X_{\mathcal{S}};A) = H_n\bigl(C_\bullet(X_{\mathcal{S}};A)\bigr), \qquad n \ge 0.
$$

Let $H_n(\mathcal{M};A)$ denote the singular homology of $\mathcal{M}$ with coefficients in $A$. The continuous map $\rho \circ \pi \colon \mathcal{M} \to |X_{\mathcal{S}}|$ induces a homomorphism
$$
(\rho \circ \pi)_* \colon H_n(\mathcal{M};A) \to H_n(X_{\mathcal{S}};A).
$$

If $G$ is a group and $n \ge 0$, any homomorphism
$$
\Phi_n \colon H_n(X_{\mathcal{S}};A) \to G
$$
determines a composite homomorphism
$$
H_n(\mathcal{M};A)
\xrightarrow{(\rho \circ \pi)_*}
H_n(X_{\mathcal{S}};A)
\xrightarrow{\Phi_n}
G.
$$

For fixed $n$, $A$, $G$, $\rho$, and $\Phi_n$, define the obstruction homomorphism
$$
\operatorname{ob}_n = \Phi_n \circ (\rho \circ \pi)_*
\colon H_n(\mathcal{M};A) \to G.
$$
For $\xi \in H_n(\mathcal{M};A)$, define the obstruction class of $\xi$ to be
$$
\operatorname{ob}_n(\xi) \in G.
$$
If a distinguished class $\xi \in H_n(\mathcal{M};A)$ has been specified, then $\operatorname{ob}_n(\xi)$ is called the distinguished obstruction class associated with the chosen data.

## Remarks, motivation, and heuristic claims

The relation $\sim_{\mathrm{comp}}$ is not intended to be canonical. It is a candidate formalization of the heuristic idea that two compact subsets of $\mathcal{M}$ should be regarded as equivalent when they admit the same disk-like outer approximants at every scale.

The motivation for introducing the quotient space $\mathcal{S}$ is that the map
$$
\pi \colon \mathcal{M} \to \mathcal{S}
$$
packages points of $\mathcal{M}$ into equivalence classes determined by the chosen approximation theory. One may then ask whether geometric or topological properties of $\pi(\mathcal{M}) \subseteq \mathcal{S}$ and of the fibers $\pi^{-1}(s)$ influence corresponding properties of $\mathcal{M}$.

Heuristically, one possible MLC-oriented program is to choose the relation $\sim_{\mathrm{comp}}$ so that local connectivity of the quotient object $\pi(\mathcal{M})$, together with suitable regularity of the fibers of $\pi$, constrains or reflects local connectivity of $\mathcal{M}$.

Likewise, the simplicial complex $X_{\mathcal{S}}$ and the map
$$
\rho \colon \pi(\mathcal{M}) \to |X_{\mathcal{S}}|
$$
are auxiliary choices rather than canonical constructions. Their purpose is to replace the quotient geometry by combinatorial models whose homology groups may be easier to analyze.

The final passage from homology groups to a group $G$ through a homomorphism
$$
\Phi_n \colon H_n(X_{\mathcal{S}};A) \to G
$$
should therefore be understood as extra structure imposed for a specific application, rather than data determined uniquely by $\mathcal{M}$.

If one constructs the group $G$, then a possible relation to MLC would be to interpret algebraic properties of $G$ as invariants of the quotient model that either detect obstructions to local connectivity of $\mathcal{M}$ or furnish criteria implying local connectivity under additional hypotheses.

## Problem: formulation of MLC in terms of $G$

A possible formulation is the following. An MLC-related statement involving $G$ can only be formulated after specifying a construction in which $G$ measures obstructions to local connectivity. In that case, the relevant sentence would have the form: if the obstruction classes $\operatorname{ob}_n(\xi)$ vanish for all $\xi$ in a specified family of homology classes, or equivalently if the canonical map
$$
\Phi_n \circ (\rho \circ \pi)_* \colon H_n(\mathcal{M};A) \to G
$$
is trivial for the chosen degree $n$, then $\mathcal{M}$ is locally connected. Conversely, if $\mathcal{M}$ is not locally connected, one would expect this construction to produce a nonzero obstruction class $\operatorname{ob}_n(\xi)$ for some $\xi \in H_n(\mathcal{M};A)$. Thus $G$ would have to be defined so that vanishing of the relevant obstruction classes is equivalent, or at least closely related, to MLC.
