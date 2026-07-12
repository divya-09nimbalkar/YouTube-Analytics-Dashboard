import pandas as pd
from src.transform import clean_data

def test_clean_data():
    df = pd.DataFrame({"snippet.publishedAt": ["2021-01-01", None]})
    df_clean = clean_data(df)
    assert df_clean["snippet.publishedAt"].dtype == "datetime64[ns]"
