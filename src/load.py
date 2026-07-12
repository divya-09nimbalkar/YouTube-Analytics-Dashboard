def save_to_csv(df, path="data/processed/youtube_data.csv"):
    df.to_csv(path, index=False)
