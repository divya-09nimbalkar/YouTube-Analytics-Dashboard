import pandas as pd

def fetch_youtube_data():
    data = {
        "videoId": [f"vid{i:03}" for i in range(1, 21)],
        "title": [f"Video {i}" for i in range(1, 21)],
        "snippet.publishedAt": pd.date_range("2024-01-01", periods=20, freq="7D"),
        "statistics.viewCount": [1000 + i*200 for i in range(1, 21)],
        "statistics.likeCount": [50 + i*15 for i in range(1, 21)],
        "statistics.commentCount": [10 + i*5 for i in range(1, 21)],
    }
    return pd.DataFrame(data)

if __name__ == "__main__":
    df = fetch_youtube_data()
    df.to_csv("data/raw/youtube_sample.csv", index=False)
    print("Dummy raw data saved to data/raw/youtube_sample.csv")
