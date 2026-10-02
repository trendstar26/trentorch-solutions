import numpy as np


def make_zero_grid(rows: int, cols: int) -> np.ndarray:
    return np.zeros((rows,cols))
    """
    Return a 2D array with `rows` rows and `cols` columns,
    every element equal to 0, using np.zeros.
    """
    pass


def make_filled_grid(rows: int, cols: int, fill_value) -> np.ndarray:
    return np.full((rows,cols),fill_value)
    """
    Return a 2D array with `rows` rows and `cols` columns,
    every element equal to `fill_value`, using np.full.
    """
    pass


def make_ones_vector(length: int) -> np.ndarray:
    return np.ones(length)
    """
    Return a 1D array of the given `length`, every element
    equal to 1, using np.ones.
    """
    pass
