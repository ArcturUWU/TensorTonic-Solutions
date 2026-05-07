import numpy as np

def sort_with_indices(data, axis):
    """Returns: np.ndarray of shape (2, m, n), stacked sorted values and sort indices"""
    arr = np.array(data, dtype=np.float64)
    s_arr = np.sort(arr, axis)
    pos_arr = np.argsort(arr, axis)
    return np.array([s_arr, pos_arr])