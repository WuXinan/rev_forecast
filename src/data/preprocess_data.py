def preprocess_data(data):
    # Fill missing values, create new features, etc.
    data.fillna(method='ffill', inplace=True)
    data['Month'] = data.index.month
    data['Quarter'] = data.index.quarter
    return data
