import pandas as pd

def set_index_column(data, index_col):
    """
    Returns: dict with 'index_values', 'columns', 'data'
    """
    df = pd.DataFrame(data)
    df = df.set_index(index_col)
    index_values = df.index
    columns = df.columns
    data = df.to_dict(orient='list')
    return {
        'index_values': index_values,
        'columns': columns,
        'data': data,
    }