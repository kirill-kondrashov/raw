# Draft: MLC research program

## Overall idea

Let

- $\mathcal{M} \subset \mathbb{C}$ denote the Mandelbrot set;
- $\mathcal{K}(\mathcal{M})$ denote the collection of nonempty compact subsets of $\mathcal{M}$;
- $\mathcal{A}$ denote the collection of compact sets $K \subset \mathbb{C}$ such that $K$ is homeomorphic to the closed disk $D^2$.

For $m \in \mathcal{K}(\mathcal{M})$ and $\varepsilon > 0$, define the set of $\varepsilon$-admissible outer approximants of $m$ by

$$
\mathcal{A}_\varepsilon(m) = \{K \in \mathcal{A} : m \subset K \text{ and } d_H(K,m) < \varepsilon\},
$$

where $d_H$ is the Hausdorff distance on nonempty compact subsets of $\mathbb{C}$.

This leads to one possible equivalence relation on $\mathcal{K}(\mathcal{M})$:

$$
m_1 \sim_{\mathrm{comp}} m_2
\quad\Longleftrightarrow\quad
\mathcal{A}_\varepsilon(m_1) = \mathcal{A}_\varepsilon(m_2)
\text{ for every } \varepsilon > 0.
$$

Since equality of the families $\mathcal{A}_\varepsilon(m)$ is reflexive, symmetric, and transitive, the relation $\sim_{\mathrm{comp}}$ is an equivalence relation. We may therefore define

$$
\mathcal{S} = \mathcal{K}(\mathcal{M}) / \sim_{\mathrm{comp}},
$$

__Remark__: the choice of $\sim_{\mathrm{comp}}$ is not canonical; it is only one topological/geometric formalization of the informal idea of "having the same disk-like outer approximants";

The intended connection with MLC should be formulated through the quotient map
$$
q \colon \mathcal{K}(\mathcal{M}) \to \mathcal{S}
= \mathcal{K}(\mathcal{M}) / \sim_{\mathrm{comp}}.
$$
If $\iota \colon \mathcal{M} \to \mathcal{K}(\mathcal{M})$ is the map $\iota(c) = \{c\}$, then $\pi = q \circ \iota$ fits into the diagram
$$
\begin{array}{ccc}
\mathcal{M} & \xrightarrow{\iota} & \mathcal{K}(\mathcal{M}) \\
{\scriptstyle \pi}\downarrow && \downarrow{\scriptstyle q} \\
\pi(\mathcal{M}) & \hookrightarrow & \mathcal{S}.
\end{array}
$$
A possible route toward MLC is then to choose the relation $\sim_{\mathrm{comp}}$ so that one can prove a theorem of the following form: if the quotient space $\pi(\mathcal{M})$ and the fibers $\pi^{-1}(s)$, $s \in \pi(\mathcal{M})$, are locally connected, then $\mathcal{M}$ is locally connected. In this sense, the role of $\mathcal{S}$ is to encode a decomposition of $\mathcal{M}$ whose quotient geometry may control local connectivity of $\mathcal{M}$ itself.

The given $\mathcal S$ can be associated with a simplicial complexes chain.