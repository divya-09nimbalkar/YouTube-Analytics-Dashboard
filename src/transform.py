import pandas as pd

def clean_data(df: pd.DataFrame):
    df = df.dropna()
    df["publishedAt"] = pd.to_datetime(df["snippet.publishedAt"])
    return df
