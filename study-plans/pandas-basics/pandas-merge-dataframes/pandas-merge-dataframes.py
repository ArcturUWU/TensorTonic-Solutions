import pandas as pd

def merge_dataframes(left, right, on, how):
    """
    Returns: dict of column to value lists
    """
    left_df = pd.DataFrame(left)
    right_df = pd.DataFrame(right)
    merged = left_df.merge(right_df, on=on, how=how)
    return merged.to_dict(orient='list')