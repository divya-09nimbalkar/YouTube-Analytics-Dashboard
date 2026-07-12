import pandas as pd
import joblib

def predict(df: pd.DataFrame, model_path="models/youtube_model.pkl"):
    model = joblib.load(model_path)
    X = df[["statistics.viewCount", "statistics.likeCount", "statistics.commentCount"]].astype(int)
    preds = model.predict(X)
    return preds
