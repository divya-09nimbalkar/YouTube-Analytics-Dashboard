import pandas as pd

def fetch_youtube_data(api_key=None, channel_id=None):
    data = {
        "videoId": [f"vid{i:03}" for i in range(1, 21)],
        "title": [f"Video {i}" for i in range(1, 21)],
        "statistics.viewCount": [1000 + i*200 for i in range(1, 21)],
        "statistics.likeCount": [50 + i*15 for i in range(1, 21)],
        "statistics.commentCount": [10 + i*5 for i in range(1, 21)],
    }
    return pd.DataFrame(data)
