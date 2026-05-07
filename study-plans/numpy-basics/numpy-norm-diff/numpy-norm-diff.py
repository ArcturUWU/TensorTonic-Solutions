import numpy as np

def norm_diff(a, b, lo, hi):
    """Returns: np.ndarray of absolute differences after clipping and rescaling to [0, 1]"""
    a = np.array(a, dtype=np.float64)
    b = np.array(b, dtype=np.float64)
    a_c = np.clip(a, lo, hi)
    b_c = np.clip(b, lo, hi)
    a_c_s = (a_c-lo)/(hi-lo)
    b_c_s = (b_c-lo)/(hi-lo)
    return np.abs(a_c_s-b_c_s)