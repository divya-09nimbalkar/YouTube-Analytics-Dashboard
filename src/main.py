from src.extract import fetch_youtube_data
from src.transform import clean_data
from src.load import save_to_csv
from src.train import train_model

def run_pipeline(api_key, channel_id):
    df_raw = fetch_youtube_data(api_key, channel_id)
    df_clean = clean_data(df_raw)
    save_to_csv(df_clean)
    train_model()

if __name__ == "__main__":
    # Replace with your API key and channel ID
    API_KEY = "YOUR_YOUTUBE_API_KEY"
    CHANNEL_ID = "YOUR_CHANNEL_ID"
    run_pipeline(API_KEY, CHANNEL_ID)
