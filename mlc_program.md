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


The connection to MLC of the given $\mathcal S$ that can be defined in several ways, is that if all classes are locally connected, that means $\mathcal M$ is locally connected.