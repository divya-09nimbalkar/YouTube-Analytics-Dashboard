import pandas as pd
import os
from src.train import train_model

def test_train_model(tmp_path):
    test_file = tmp_path / "youtube_data.csv"
    df = pd.DataFrame({
        "statistics.viewCount": [100, 200],
        "statistics.likeCount": [10, 20],
        "statistics.commentCount": [5, 7]
    })
    df.to_csv(test_file, index=False)
    model_file = tmp_path / "youtube_model.pkl"
    train_model(data_path=test_file, model_path=model_file)
    assert os.path.exists(model_file)
