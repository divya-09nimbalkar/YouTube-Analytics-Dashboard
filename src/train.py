import pandas as pd
from sklearn.linear_model import LinearRegression
import joblib

def train_model(data_path="data/processed/youtube_data.csv", model_path="models/youtube_model.pkl"):
    df = pd.read_csv(data_path)
    # Example: use views, likes, comments to predict engagement
    X = df[["statistics.viewCount", "statistics.likeCount", "statistics.commentCount"]].astype(int)
    y = df["statistics.viewCount"].astype(int)  # dummy target, replace with engagement metric
    model = LinearRegression()
    model.fit(X, y)
    joblib.dump(model, model_path)
    print(f"Model saved to {model_path}")

if __name__ == "__main__":
    train_model()
