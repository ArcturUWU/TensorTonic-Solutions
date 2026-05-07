import numpy as np

def summarize(data, axis):
    """Returns: np.ndarray of shape (4, k), rows are mean, std, min, max"""    
    data = np.array(data, dtype=np.float64)
    features = np.array([data.mean(axis), data.std(axis), data.min(axis), data.max(axis)])
    return features