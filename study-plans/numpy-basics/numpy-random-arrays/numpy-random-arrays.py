import numpy as np

def generate_random_array(shape, kind, seed):
    rng = np.random.RandomState(seed)

    if kind == 'uniform':
        return rng.rand(*shape)
    elif kind == 'normal':
        return rng.randn(*shape)