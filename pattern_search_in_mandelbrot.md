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

## Experimental golden-scale search

The notebook [./notebooks/golden_scale_self_similarity.ipynb](./notebooks/golden_scale_self_similarity.ipynb) implements a discrete version of the golden-scale self-similarity functional. In the current experiment it:

1. samples a binary image of the Mandelbrot set on a finite grid;
2. constructs the associated signed distance field;
3. evaluates the score $S_{N,m}$ on a search window near the main cardioid;
4. lists all sampled local minima of the score on that finite grid.

In the current run, the best sampled candidate is near

$$
c = -0.8,
$$

with score approximately

$$
S_{N,m} \approx 0.037588.
$$

On the chosen finite grid, the detected candidate set is finite. In the grid-based formulation over the countable family of finite sampling grids $(\Gamma_N)_{N \geq 1}$, the union of all sampled candidate sets is therefore at most countable.

At present, this experiment is only qualitatively consistent with the Dudko-style theory: it does find low-score multiscale candidates near the main cardioid, so the functional is detecting the intended kind of self-similarity. However, it does not yet isolate the specific \((\)anti-\()\)golden mean point, nor does it verify the scaling law

$$
r_n \asymp \lambda^{-2n}
$$

in any rigorous or high-precision sense. It should therefore be interpreted as a proof of concept for the detection functional, not as a confirmation of the full theory.

### Search window, sampled local minima, and score field

![Golden-scale search window and score field](./notebooks/images/golden_scale_self_similarity_1.png)

The left panel shows the search window together with all sampled local minima and the best candidate. The right panel shows the corresponding score field $S_{N,m}$ on the search grid. The presence of several low-score points is qualitatively compatible with the expectation that self-similar loci occur near the main cardioid, but this picture alone does not identify the Dudko point or establish the predicted asymptotic scaling.

### Normalized patches across golden scales

![Golden-scale normalized patches](./notebooks/images/golden_scale_self_similarity_2.png)

These patches are the normalized fields $f_{N,x,n}$ at scales

$$
r_n = r_0 \lambda^{-2n},
\qquad
n = 0,1,2,3.
$$

Their visual similarity is the experimental signal that the functional is designed to detect. In the current notebook this is only a finite-resolution visual and numerical proxy for the theoretical pattern.

## Next step: search for other scaling ratios

A natural next step is to replace the golden scaling law by a more general one

$$
r_n = r_0 \alpha^{-2n},
\qquad \alpha > 1,
$$

and define the corresponding family of functionals

$$
S_{N,m}^{(\alpha)}(x).
$$

One may then search either over a finite set of prescribed values of $\alpha$ or over a discretized interval of possible ratios. The most natural first candidates are:

- the silver ratio
  $$
  1+\sqrt{2};
  $$
- more generally the metallic means
  $$
  \sigma_k = \frac{k+\sqrt{k^2+4}}{2},
  \qquad k \geq 1;
  $$
- quadratic irrationals coming from periodic continued fractions;
- ratios derived from denominators of convergents of bounded-type rotation numbers;
- Feigenbaum-type scaling constants in other renormalization regimes.

Thus the present golden-scale notebook can be regarded as the first member of a broader experimental program of searching for self-similar loci by minimizing $S_{N,m}^{(\alpha)}(x)$ over both $x$ and $\alpha$.
