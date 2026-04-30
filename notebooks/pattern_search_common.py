import math

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Rectangle
from scipy.ndimage import distance_transform_edt, map_coordinates

PHI = (1.0 + math.sqrt(5.0)) / 2.0


def metallic_mean(k):
    return (k + math.sqrt(k * k + 4.0)) / 2.0


def mandelbrot_indicator(bounds, n, max_iter=200):
    xmin, xmax, ymin, ymax = bounds
    dx = (xmax - xmin) / n
    dy = (ymax - ymin) / n
    xs = xmin + (np.arange(n) + 0.5) * dx
    ys = ymin + (np.arange(n) + 0.5) * dy
    c = xs[None, :] + 1j * ys[:, None]
    z = np.zeros_like(c)
    inside = np.ones(c.shape, dtype=bool)
    for _ in range(max_iter):
        z[inside] = z[inside] * z[inside] + c[inside]
        inside[inside] = np.abs(z[inside]) <= 2.0
    return inside.astype(np.uint8)


def signed_distance(indicator, spacing):
    inside = indicator.astype(bool)
    return distance_transform_edt(inside, sampling=spacing) - distance_transform_edt(~inside, sampling=spacing)


def build_mandelbrot_field(bounds, n, max_iter=200):
    indicator = mandelbrot_indicator(bounds, n, max_iter=max_iter)
    dx = (bounds[1] - bounds[0]) / n
    dy = (bounds[3] - bounds[2]) / n
    field = signed_distance(indicator, spacing=(dy, dx))
    return indicator, field


def unit_disk_grid(patch_size):
    grid = np.linspace(-1.0, 1.0, patch_size)
    u, v = np.meshgrid(grid, grid, indexing="xy")
    mask = u * u + v * v <= 1.0
    return u, v, mask


def sample_field(field, bounds, x_coords, y_coords):
    xmin, xmax, ymin, ymax = bounds
    ny, nx = field.shape
    col = (x_coords - xmin) / (xmax - xmin) * nx - 0.5
    row = (y_coords - ymin) / (ymax - ymin) * ny - 0.5
    return map_coordinates(field, [row, col], order=1, mode="nearest")


def normalized_patch(field, bounds, center, radius, patch_size):
    x0, y0 = center
    u, v, mask = unit_disk_grid(patch_size)
    x = x0 + radius * u
    y = y0 + radius * v
    patch = sample_field(field, bounds, x, y)
    patch[~mask] = 0.0
    return patch, mask


def rotate_patch(patch, angle, mask):
    patch_size = patch.shape[0]
    u, v, _ = unit_disk_grid(patch_size)
    c = math.cos(angle)
    s = math.sin(angle)
    x = c * u - s * v
    y = s * u + c * v
    rotated = sample_field(patch, (-1.0, 1.0, -1.0, 1.0), x, y)
    rotated[~mask] = 0.0
    return rotated


def patch_l2_error(patch_a, patch_b, mask):
    diff = patch_a - patch_b
    return math.sqrt(np.mean(np.square(diff[mask])))


def scale_self_similarity(field, bounds, center, r0, ratio, m=3, patch_size=40, angle_samples=16, exponent=2.0):
    base_patch, mask = normalized_patch(field, bounds, center, r0, patch_size)
    angles = np.linspace(0.0, 2.0 * math.pi, angle_samples, endpoint=False)
    rotated_base = [(angle, rotate_patch(base_patch, angle, mask)) for angle in angles]
    errors = []
    patches = {0: base_patch}
    matches = {}
    for n in range(1, m + 1):
        radius = r0 * ratio ** (-exponent * n)
        patch, _ = normalized_patch(field, bounds, center, radius, patch_size)
        patches[n] = patch
        best_value = math.inf
        best_angle = 0.0
        best_match = None
        for angle, rotated in rotated_base:
            value = patch_l2_error(patch, rotated, mask)
            if value < best_value:
                best_value = value
                best_angle = angle
                best_match = rotated
        errors.append({"n": n, "radius": radius, "angle": best_angle, "value": best_value})
        matches[n] = best_match
    score = sum((2.0 ** (-item["n"])) * item["value"] for item in errors)
    return {
        "center": center,
        "score": score,
        "errors": errors,
        "patches": patches,
        "matches": matches,
        "mask": mask,
        "ratio": ratio,
    }


def search_grid(field, bounds, search_bounds, r0, ratio, m=3, patch_size=40, angle_samples=16, grid_shape=(17, 17), exponent=2.0):
    xmin, xmax, ymin, ymax = search_bounds
    xs = np.linspace(xmin, xmax, grid_shape[0])
    ys = np.linspace(ymin, ymax, grid_shape[1])
    scores = np.empty((len(ys), len(xs)))
    best = None
    for j, y in enumerate(ys):
        for i, x in enumerate(xs):
            result = scale_self_similarity(
                field,
                bounds,
                (x, y),
                r0,
                ratio,
                m=m,
                patch_size=patch_size,
                angle_samples=angle_samples,
                exponent=exponent,
            )
            scores[j, i] = result["score"]
            if best is None or result["score"] < best["score"]:
                best = result
    return xs, ys, scores, best


def sampled_local_minima(xs, ys, scores):
    minima = []
    ny, nx = scores.shape
    for j in range(ny):
        for i in range(nx):
            j0 = max(0, j - 1)
            j1 = min(ny, j + 2)
            i0 = max(0, i - 1)
            i1 = min(nx, i + 2)
            neighborhood = scores[j0:j1, i0:i1]
            value = scores[j, i]
            if value == np.min(neighborhood):
                minima.append({"center": (xs[i], ys[j]), "score": value})
    minima.sort(key=lambda item: item["score"])
    return minima


def run_single_ratio_search(bounds, search_bounds, n, max_iter, r0, ratio, m=3, patch_size=40, angle_samples=16, grid_shape=(17, 17), exponent=2.0):
    indicator, field = build_mandelbrot_field(bounds, n, max_iter=max_iter)
    grid_xs, grid_ys, score_grid, best = search_grid(
        field,
        bounds,
        search_bounds,
        r0,
        ratio,
        m=m,
        patch_size=patch_size,
        angle_samples=angle_samples,
        grid_shape=grid_shape,
        exponent=exponent,
    )
    local_minima = sampled_local_minima(grid_xs, grid_ys, score_grid)
    return {
        "indicator": indicator,
        "field": field,
        "grid_xs": grid_xs,
        "grid_ys": grid_ys,
        "score_grid": score_grid,
        "best": best,
        "local_minima": local_minima,
        "params": {
            "bounds": bounds,
            "search_bounds": search_bounds,
            "n": n,
            "max_iter": max_iter,
            "r0": r0,
            "ratio": ratio,
            "m": m,
            "patch_size": patch_size,
            "angle_samples": angle_samples,
            "grid_shape": grid_shape,
            "exponent": exponent,
        },
    }


def search_over_ratios(bounds, search_bounds, n, max_iter, r0, ratios, m=3, patch_size=40, angle_samples=16, grid_shape=(17, 17), exponent=2.0):
    indicator, field = build_mandelbrot_field(bounds, n, max_iter=max_iter)
    results = []
    for name, ratio in ratios:
        grid_xs, grid_ys, score_grid, best = search_grid(
            field,
            bounds,
            search_bounds,
            r0,
            ratio,
            m=m,
            patch_size=patch_size,
            angle_samples=angle_samples,
            grid_shape=grid_shape,
            exponent=exponent,
        )
        local_minima = sampled_local_minima(grid_xs, grid_ys, score_grid)
        results.append(
            {
                "name": name,
                "ratio": ratio,
                "grid_xs": grid_xs,
                "grid_ys": grid_ys,
                "score_grid": score_grid,
                "best": best,
                "local_minima": local_minima,
            }
        )
    results.sort(key=lambda item: item["best"]["score"])
    return {
        "indicator": indicator,
        "field": field,
        "results": results,
        "params": {
            "bounds": bounds,
            "search_bounds": search_bounds,
            "n": n,
            "max_iter": max_iter,
            "r0": r0,
            "m": m,
            "patch_size": patch_size,
            "angle_samples": angle_samples,
            "grid_shape": grid_shape,
            "exponent": exponent,
        },
    }


def candidate_array(local_minima):
    if not local_minima:
        return np.empty((0, 2)), np.empty((0,))
    centers = np.array([item["center"] for item in local_minima], dtype=float)
    scores = np.array([item["score"] for item in local_minima], dtype=float)
    return centers, scores


def plot_search_result(indicator, bounds, search_bounds, grid_xs, grid_ys, score_grid, best, local_minima):
    fig, axes = plt.subplots(1, 2, figsize=(12, 5), constrained_layout=True)
    centers, _ = candidate_array(local_minima)
    extent = (bounds[0], bounds[1], bounds[2], bounds[3])
    axes[0].imshow(indicator, extent=extent, origin="lower", cmap="binary")
    axes[0].add_patch(
        Rectangle(
            (search_bounds[0], search_bounds[2]),
            search_bounds[1] - search_bounds[0],
            search_bounds[3] - search_bounds[2],
            fill=False,
            edgecolor="tab:red",
            linewidth=2,
        )
    )
    if len(centers) > 0:
        axes[0].scatter(centers[:, 0], centers[:, 1], color="tab:cyan", s=20, label="sampled local minima")
    axes[0].scatter([best["center"][0]], [best["center"][1]], color="tab:orange", s=35, label="best candidate")
    axes[0].set_title("Search window and best candidate")
    axes[0].set_xlabel(r"$\mathrm{Re}(c)$")
    axes[0].set_ylabel(r"$\mathrm{Im}(c)$")
    axes[0].legend(loc="lower left")

    score_extent = (grid_xs[0], grid_xs[-1], grid_ys[0], grid_ys[-1])
    im = axes[1].imshow(score_grid, extent=score_extent, origin="lower", cmap="viridis")
    if len(centers) > 0:
        axes[1].scatter(centers[:, 0], centers[:, 1], color="tab:red", s=18)
    axes[1].scatter([best["center"][0]], [best["center"][1]], color="white", s=24)
    axes[1].set_title("Self-similarity score on the search grid")
    axes[1].set_xlabel(r"$\mathrm{Re}(c)$")
    axes[1].set_ylabel(r"$\mathrm{Im}(c)$")
    fig.colorbar(im, ax=axes[1], label=r"$S_{N,m}$")
    return fig, axes


def plot_patches(best, m):
    fig, axes = plt.subplots(1, m + 1, figsize=(3 * (m + 1), 3), constrained_layout=True)
    for n in range(m + 1):
        axes[n].imshow(best["patches"][n], cmap="coolwarm", origin="lower")
        axes[n].set_title(r"$n = " + str(n) + r"$")
        axes[n].set_xticks([])
        axes[n].set_yticks([])
    return fig, axes


def plot_ratio_comparison(results):
    names = [item["name"] for item in results]
    scores = [item["best"]["score"] for item in results]
    fig, ax = plt.subplots(figsize=(8, 4), constrained_layout=True)
    ax.bar(names, scores, color="tab:purple")
    ax.set_ylabel(r"best value of $S_{N,m}^{(\alpha)}$")
    ax.set_title("Best score by scaling ratio")
    ax.grid(axis="y", alpha=0.3)
    return fig, ax
