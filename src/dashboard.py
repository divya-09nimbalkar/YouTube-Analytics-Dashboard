import streamlit as st
import pandas as pd

def run_dashboard():
    st.title("YouTube Analytics Dashboard")
    df = pd.read_csv("data/processed/youtube_data.csv")

    st.subheader("Raw Data Preview")
    st.write(df.head())

    if "snippet.publishedAt" in df.columns:
        st.subheader("Views Over Time")
        st.line_chart(df.set_index("snippet.publishedAt")["statistics.viewCount"])
    else:
        st.warning("No publish date column found. Showing views only.")
        st.line_chart(df["statistics.viewCount"])

    st.subheader("Likes vs Comments")
    st.scatter_chart(df[["statistics.likeCount", "statistics.commentCount"]])

if __name__ == "__main__":
    run_dashboard()
