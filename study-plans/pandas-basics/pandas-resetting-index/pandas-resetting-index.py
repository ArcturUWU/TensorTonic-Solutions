import pandas as pd

def reset_index_demo(data, index_col):
    """
    Returns: list [columns_before_reset, columns_after_reset]
    """

    df = pd.DataFrame(data)
    df = df.set_index(index_col)
    before = df.columns
    after = df.reset_index().columns
    return [before, after]