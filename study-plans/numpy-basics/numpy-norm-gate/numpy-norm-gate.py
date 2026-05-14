import numpy as np

def norm_gate(X, W, threshold):
    """Returns: np.ndarray of shape (n, k), gated projection where rows below threshold are zeroed"""
    X = np.array(X)
    W = np.array(W)
    
    product = X@W
    norm = np.linalg.norm(product, axis=1)
    gate = (norm >= threshold).astype(np.float64)
    return product*gate[:,np.newaxis]
    
    