import pandas as pd

def concat_dataframes(dfs):
    """
    Returns: list [shape, data] where shape is [rows, cols]
    """
    final_df = pd.DataFrame()
    pandas_dfs = [pd.DataFrame(one) for one in dfs]
    final_df = pd.concat(pandas_dfs, ignore_index=True)
    return [final_df.shape, final_df.to_dict(orient='list')]