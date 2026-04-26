import pandas as pd

def iloc_selection(data, row, col):
    """
    Returns: list [element, row_values, col_values]
    """
    df = pd.DataFrame(data)
    elem = df.iloc[row, col]
    r_v = df.iloc[row]
    c_v = df.iloc[:, col]
    return [elem, r_v, c_v]