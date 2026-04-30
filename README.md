# Raw ideas and remarks

- [Bridge between group and MLC](./bridge_between_group_and_mlc.md)
- [Bridge between Schur multiplier and Mandelbrot](./bridge_between_schur_multiplier_and_mandelbrot.md)
- [Notebook: Golden-scale self-similarity functional](./notebooks/golden_scale_self_similarity.ipynb)
- [Rendered notebook (HTML)](./notebooks/golden_scale_self_similarity.html)

## Experimental golden-scale search

The notebook `notebooks/golden_scale_self_similarity.ipynb` implements a discrete version of the golden-scale self-similarity functional for the Mandelbrot set. Experimentally, it:

1. samples a binary image of the Mandelbrot set on a finite grid;
2. builds the associated signed distance field;
3. evaluates the golden-scale score on a search window near the main cardioid;
4. lists all sampled local minima of the score on that finite grid.

In the current run, the best sampled candidate is near

$$
c = -0.8,
$$

with score approximately

$$
S_{N,m} \approx 0.037588.
$$

On the chosen finite grid, the detected candidate set is finite; in the grid-based formulation over all finite sampling grids, the union of such candidate sets is at most countable.

### Search window, sampled local minima, and score field

![Golden-scale search window and score field](./notebooks/images/golden_scale_self_similarity_1.png)

The left panel shows the search window together with all sampled local minima and the best candidate. The right panel shows the corresponding score field $S_{N,m}$ on the search grid.

### Normalized patches across golden scales

![Golden-scale normalized patches](./notebooks/images/golden_scale_self_similarity_2.png)

These patches are the normalized fields $f_{N,x,n}$ at scales

$$
r_n = r_0 \lambda^{-2n},
\qquad
n = 0,1,2,3.
$$

Their visual similarity is the experimental signal that the functional is designed to detect.
