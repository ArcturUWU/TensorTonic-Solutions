import pandas as pd

def boolean_filter(data, column, threshold):
    """
    Returns: dict with 'filtered_data' (dict) and 'count' (int)
    """
    df = pd.DataFrame(data)
    filtered_data = df[df[column] > threshold].to_dict(orient='list')
    count = df[df[column] > threshold].shape[0]
    return {
        'filtered_data': filtered_data,
        'count': count,
    }