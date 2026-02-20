import pandas as pd

def clean_data(path):
    df = pd.read_csv(path)
    df.dropna(inplace=True)
    return df
