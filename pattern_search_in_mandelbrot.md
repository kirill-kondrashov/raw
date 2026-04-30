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
