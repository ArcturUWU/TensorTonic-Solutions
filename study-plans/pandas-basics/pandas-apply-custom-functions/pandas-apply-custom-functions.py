import pandas as pd

def apply_transform(data, column, operation):
    """
    Returns: dict with original columns plus column_transformed
    """
    df = pd.DataFrame(data)
    if operation == 'normalize':
        df[column + '_transformed'] = ((df[column] - df[column].min()) / (df[column].max()-df[column].min())).round(4)
    elif operation == 'rank':
        df[column + '_transformed'] = df[column].rank().astype(int)
    elif operation == 'cumsum':
        df[column + '_transformed'] = df[column].cumsum()
    else:
        df[column + '_transformed'] = df[column]*2

    return df.to_dict(orient='list')