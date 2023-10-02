import numpy as np
from fractal_noise import get_fractal_noise


def test_fractal_noise():
    # TEST CASE: a small 5x5 array
    width, height, scale, octaves = 5, 5, 1, [0, 1]
    noise = get_fractal_noise(width, height, scale, octaves)
    assert noise.shape == (width, height)
    assert np.all(np.abs(noise) <= 1.0 + 1e-6)

    # TEST CASE: a larger 20x20 array
    width, height, scale, octaves = 20, 20, 1, [0, 1, 2]
    noise = get_fractal_noise(width, height, scale, octaves)
    assert noise.shape == (width, height)
    assert np.all(np.abs(noise) <= 1.0 + 1e-6)

    # TEST CASE: a non-square 5x10 array
    width, height, scale, octaves = 5, 10, 1, [0, 1, 2, 3]
    noise = get_fractal_noise(width, height, scale, octaves)
    assert noise.shape == (width, height)
    assert np.all(noise >= -1.0) and np.all(noise <= 1.0)
