import numpy as np

def normalize(data):
    """Returns: np.ndarray of shape (m, n), z-score normalized per column"""
    arr = np.array(data, dtype=np.float64)
    arr_min = arr.mean(axis=0)
    arr_std = arr.std(axis=0)
    std = (arr-arr_min)/arr_std
    return std