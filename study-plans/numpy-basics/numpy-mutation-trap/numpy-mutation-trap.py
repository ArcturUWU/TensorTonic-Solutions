import numpy as np

def original_and_clipped(data, row_idx, lo, hi):
    """
    Returns: 2D ndarray of float64 with shape (2, ncols)
    """
    arr = np.array(data, dtype=np.float64)
    clipped = np.clip(arr[row_idx], lo, hi)
    return [arr[row_idx], clipped]