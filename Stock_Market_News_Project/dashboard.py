import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import os

st.set_page_config(page_title="Stock Market Sentiment Dashboard", layout="wide")
st.title("Stock Market News Sentiment Dashboard")

if not os.path.exists("DATA/news.csv"):
    st.error("news.csv not found. Run scraper.py first.")
    st.stop()

try:
    df = pd.read_csv("DATA/news.csv")
except Exception as e:
    st.error(f"Error loading CSV: {e}")
    st.stop()

st.subheader("Quick Statistics")
col1, col2, col3, col4 = st.columns(4)
col1.metric("Total News", len(df))
col2.metric("Average Score", round(df["Score"].mean(), 3))
col3.metric("Unique Sectors", df["sector"].nunique())
col4.metric("Companies", df["Company"].nunique())
st.subheader("Filters")
search_text = st.text_input("Search Headline")
sector_options = ["All"] + sorted(df["sector"].dropna().unique())
selected_sector = st.selectbox("Select Sector", sector_options)
sentiment_options = ["All", "Positive","Negative", "Neutral"]
selected_sentiment = st.selectbox("Select Sentiment", sentiment_options)
filtered_df = df.copy()

if search_text:
    filtered_df = filtered_df[filtered_df["Headline"].str.contains(search_text, case=False, na=False)]

if selected_sector != "All":
    filtered_df = filtered_df[filtered_df["sector"] == selected_sector]

if selected_sentiment != "All":
    filtered_df = filtered_df[filtered_df["Sentiment"] == selected_sentiment]

st.subheader("News Dataset")
st.dataframe(filtered_df, use_container_width=True)
col_left, col_right = st.columns(2)

with col_left:
    st.subheader("Sentiment Distribution")
    sentiment_counts = df["Sentiment"].value_counts()
    fig1, ax1 = plt.subplots(figsize=(6, 4))
    ax1.bar(sentiment_counts.index, sentiment_counts.values)
    ax1.set_title("Sentiment Distribution")
    ax1.set_xlabel("Sentiment")
    ax1.set_ylabel("Count")
    st.pyplot(fig1)

with col_right:
    st.subheader("Sentiment Pie Chart")
    sentiment_counts = df["Sentiment"].value_counts()
    fig2, ax2 = plt.subplots(figsize=(6, 4))
    ax2.pie(sentiment_counts.values, labels=sentiment_counts.index, autopct="%1.1f%%")
    ax2.set_title("Sentiment Share")
    st.pyplot(fig2)

st.subheader("Sector Distribution")
sector_counts = df["sector"].value_counts()
fig3, ax3 = plt.subplots(figsize=(10, 5))
ax3.bar(sector_counts.index,sector_counts.values)
ax3.set_title("News By Sector")
ax3.set_xlabel("Sector")
ax3.set_ylabel("Count")
plt.xticks(rotation=45)
st.pyplot(fig3)
st.subheader("Top 10 Positive News")
top_positive = (df.sort_values(by="Score", ascending=False).head(10))
st.dataframe(top_positive[["Headline", "Company", "Score", "Sentiment"]], use_container_width=True)
st.subheader("Top 10 Negative News")
top_negative = (df.sort_values(by="Score", ascending=True).head(10))
st.dataframe(top_negative[["Headline", "Company", "Score", "Sentiment"]], use_container_width=True)
st.subheader("Company Wise News Count")
company_counts = (df["Company"].value_counts().head(10))
fig4, ax4 = plt.subplots(figsize=(10, 5))
ax4.bar(company_counts.index, company_counts.values)
ax4.set_title("Top Companies Mentioned")
ax4.set_xlabel("Company")
ax4.set_ylabel("News Count")
plt.xticks(rotation=45)
st.pyplot(fig4)
st.download_button(label="Download CSV", data=df.to_csv(index=False), file_name="news.csv", mime="text/csv")
st.success("Dashboard Loaded Successfully")