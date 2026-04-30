# Search for a pattern experimentally?

Following Dudko, Lyubich, and Selinger, *Pacman renormalization and self-similarity of the Mandelbrot set near Siegel parameters* ([arXiv:1703.01206](https://arxiv.org/abs/1703.01206)), it might be interesting to use image processing techniques to automatically locate interesting patterns. In Section 1.1 they describe self-similarity features of the Mandelbrot set near its main cardioid; more precisely, near the (anti-)golden mean point, the $(p_n/p_{n+2})$-limbs of $M$ scale down at rate

$$
\lambda^{-2n},
$$

where

$$
\lambda = \frac{1+\sqrt{5}}{2},
$$

and $p_n$ are the Fibonacci numbers. The stated goal there is to develop a renormalization theory responsible for this phenomenon.

Fix a bounded rectangle $B \subset \mathbb{C}$ containing $\mathcal{M}$. For each integer $N \geq 1$, let $I_N$ be the binary image obtained by sampling membership in $\mathcal{M}$ at the centers of an $N \times N$ square grid in $B$. A related problem is to determine whether prescribed geometric or combinatorial patterns in $\mathcal{M}$ can be detected algorithmically from the family of finite-resolution approximations $(I_N)_{N \geq 1}$.

## Known related works

- Dudko, Lyubich, and Selinger, *Pacman renormalization and self-similarity of the Mandelbrot set near Siegel parameters* ([arXiv](https://arxiv.org/abs/1703.01206), [local PDF](./refs/pacman%20renormalization%201703.01206v3.pdf)).
- Dudko and Lyubich, *Local connectivity of the Mandelbrot set at some satellite parameters of bounded type* ([arXiv](https://arxiv.org/abs/1808.10425), [local PDF](./refs/dudko-lyubich-local-connectivity-1808.10425.pdf)).
- McMullen, *Self-similarity of Siegel disks and Hausdorff dimension of Julia sets* ([arXiv](https://arxiv.org/abs/math/9805097), [local PDF](./refs/mcmullen-self-similarity-siegel-disks-math9805097.pdf)).
- Chéritat, *Near parabolic renormalization for unicritical holomorphic maps* ([arXiv](https://arxiv.org/abs/1404.4735), [local PDF](./refs/cheritat-near-parabolic-renormalization-1404.4735.pdf)).
- Gaidashev and Yampolsky, *Renormalization of almost commuting pairs* ([arXiv](https://arxiv.org/abs/1604.00719), [local PDF](./refs/gaidashev-yampolsky-almost-commuting-pairs-1604.00719.pdf)).
- Lyubich, *Conformal Geometry and Dynamics of Quadratic Polynomials* ([author PDF](https://www.math.stonybrook.edu/~mlyubich/book.pdf), [local PDF](./refs/lyubich-conformal-geometry-dynamics-quadratic-polynomials.pdf)).

## Existing attempts to search for patterns

Existing attempts appear to fall into three classes.

First, the main rigorous literature studies recurrent structure in $\mathcal{M}$ by dynamical and renormalization methods rather than by direct image analysis. The works of McMullen, Dudko--Lyubich--Selinger, Dudko--Lyubich, Ch\'eritat, Gaidashev--Yampolsky, and Lyubich belong to this class. They locate and explain self-similar features, scaling laws, and renormalization patterns by analytic and combinatorial arguments, not by template matching on finite rasterizations.

Second, there are computer-assisted search procedures implemented in fractal-exploration software. These methods are designed to locate minibrots, nuclei, or related distinguished parameters by using the dynamics of the defining iteration, for example Newton-type refinement or other parameter-space search heuristics. Such procedures constitute genuine algorithmic pattern search, but they are not generic computer-vision methods applied to the sampled images $(I_N)_{N \geq 1}$.

Third, one finds experimental and machine-learning work on fractal images more generally, including clustering, classification, and synthetic-dataset constructions. However, a systematic literature devoted specifically to detecting mathematically meaningful Mandelbrot patterns from finite-resolution images by image-processing methods appears to be sparse.

Accordingly, the problem formulated above seems to remain largely open in its purely image-based form: the closest existing work is either rigorous renormalization theory or software-assisted dynamical search, rather than a developed theory of pattern detection from the pixel approximations $(I_N)_{N \geq 1}$ alone.

## The golden-scale self-similarity functional

Fix a compact set $U \subset B$, an integer $m \geq 1$, and a number $r_0 > 0$ such that

$$
U + r_0 \overline{\mathbb{D}} \subset B,
$$

where $\mathbb{D} = \{z \in \mathbb{C} : |z| < 1\}$. Let

$$
\lambda = \frac{1+\sqrt{5}}{2},
\qquad
r_n = r_0 \lambda^{-2n},
\qquad 0 \leq n \leq m.
$$

Let $\widehat{I}_N \colon B \to \{0,1\}$ be the piecewise-constant extension of $I_N$, and define

$$
\delta_N(z)
=
\operatorname{dist}\bigl(z,\widehat{I}_N^{-1}(0)\bigr)
-
\operatorname{dist}\bigl(z,\widehat{I}_N^{-1}(1)\bigr),
\qquad z \in B.
$$

For $x \in U$ and $0 \leq n \leq m$, define

$$
f_{N,x,n}(u)
=
r_n^{-1}\delta_N(x+r_n u),
\qquad
u \in \overline{\mathbb{D}}.
$$

For $1 \leq n \leq m$, define

$$
E_{N,n}(x)
=
\inf_{\theta \in [0,2\pi)}
\left\|
f_{N,x,n}
-
f_{N,x,0}(e^{i\theta}\,\cdot)
\right\|_{L^2(\overline{\mathbb{D}})}.
$$

Define the golden-scale self-similarity functional

$$
S_{N,m}(x)
=
\sum_{n=1}^m 2^{-n} E_{N,n}(x),
\qquad x \in U.
$$

Define the candidate set

$$
\mathcal{C}_{N,m,\tau}
=
\{x \in U : S_{N,m}(x) \leq \tau\},
\qquad \tau > 0,
$$

and define

$$
x_{N,m} \in \operatorname*{argmin}_{x \in U \cap \Gamma_N} S_{N,m}(x),
$$

where $\Gamma_N$ is the sampling grid of $I_N$. The points of $\mathcal{C}_{N,m,\tau}$, or equivalently the minimizers of $S_{N,m}$ on $U \cap \Gamma_N$, are the outputs of the search procedure.
