import numpy as np

def row_summary(data, threshold):
    """Returns: np.ndarray of shape (3, m, n), stacked element mask, any-filtered, all-filtered"""
    arr = np.array(data)
    elem_level = (arr>threshold).astype(int)
    any = np.any(arr > threshold, axis=1, keepdims=True)
    all = np.all(arr>threshold, axis=1, keepdims=True)
    return [elem_level, arr*any, arr*all]