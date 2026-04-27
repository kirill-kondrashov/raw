## WIP

The 5-term exact sequence in group homology provides the formal bridge between the Schur multiplier $M(G)$, the lower central series, and the simplicial lamination of the Mandelbrot set.

Given a group $G$ with a free presentation $1 \to R \to F \to G \to 1$, where $F$ is a free group and $R$ is the group of relations (the "pinches" in lamination $K$), the 5-term exact sequence is:

$$
H_2(F, \mathbb{Z}) \to H_2(G, \mathbb{Z}) \to \frac{R}{[F, R]} \to H_1(F, \mathbb{Z}) \to H_1(G, \mathbb{Z}) \to 0
$$ 

* $H_2(F, \mathbb{Z})$: The second homology of a free group, which is always $0$.
* $H_2(G, \mathbb{Z})$: The Schur multiplier $M(G)$.
* $R / [F, R]$: The abelianized relations. This is isomorphic to the cycle group $Z_1(K)$ in the sequence $S$.
* $H_1(F, \mathbb{Z})$: The abelianization $F/[F,F]$. This represents the free group of rays $C_1(K)$.
* $H_1(G, \mathbb{Z})$: The abelianization $G/[G,G]$. This is the algebraic equivalent of the reduced 0-chains $\tilde{C}_0(K)$.
* $S$ is the augmented simplicial chain complex of the lamination $\mathcal{L}$ of the Mandelbrot set $M$, formalized as a split short exact sequence:

$$
0 \to Z_1(K) \xrightarrow{\iota} C_1(K) \xrightarrow{\partial_1} \tilde{C}_0(K) \to 0
$$ 

Because $H_2(F) = 0$, the sequence simplifies to:

$$
0 \to M(G) \to Z_1(K) \xrightarrow{\iota_*} C_1(K) \to \tilde{C}_0(K) \to 0
$$ 
