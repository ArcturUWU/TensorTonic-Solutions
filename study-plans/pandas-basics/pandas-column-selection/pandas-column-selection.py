import pandas as pd

def select_column(data, column):
    """
    Returns: dict with 'values' (list) and 'length' (int)
    """
    col = data[column]
    return {
        "values": col,
        "length": len(col)
    }
    pass