import numpy as np

def winsorize(data, lo_q, hi_q):
    """Returns: np.ndarray of shape (3, m, n), stacked clipped values, lo_mask, hi_mask"""
    arr = np.array(data, dtype=np.float64)
    lo = np.percentile(arr, lo_q, axis=0)
    hi = np.percentile(arr, hi_q, axis=0)
    lo_mask = arr<lo
    hi_mask = arr>hi
    return np.stack((np.clip(arr, lo, hi), lo_mask, hi_mask), axis=0)