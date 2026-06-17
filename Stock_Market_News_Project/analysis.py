import pandas as pd
import matplotlib.pyplot as plt
import os
from collections import Counter

def analyze_data():
    os.makedirs("Analysis", exist_ok=True)

    if not os.path.exists("DATA/news.csv"):
        print("Error: news.csv not found!")
        print("Run scraper.py first.")
        return

    try:
        df = pd.read_csv("DATA/news.csv")

    except Exception as e:
        print(f"Error reading CSV: {e}")
        return

    print("\nDATA PREVIEW")
    print(df.head())

    print("\nDATA INFO")
    print(df.info())

    print("\nMISSING VALUES")
    print(df.isnull().sum())

    df = df.dropna(subset=["Headline"])
    before = len(df)
    df = df.drop_duplicates(subset=["Headline"])
    after = len(df)
    print(f"\nDuplicates Removed: {before - after}")
    cleaned_file = "Analysis/cleaned_news.csv"
    df.to_csv(cleaned_file, index=False)
    print(f"\nCleaned data saved: {cleaned_file}")
    print("\nSENTIMENT COUNTS")
    sentiment_counts = df["Sentiment"].value_counts()
    print(sentiment_counts)

    plt.figure(figsize=(8, 5))
    sentiment_counts.plot(kind="bar")
    plt.title("News Sentiment Distribution")
    plt.xlabel("Sentiment")
    plt.ylabel("Number of News")
    plt.tight_layout()
    plt.savefig("Analysis/sentiment_distribution.png", dpi=300)
    plt.show()

    print("Sentiment chart saved.")
    print("\nSECTOR COUNTS")
    sector_counts = df["sector"].value_counts()
    print(sector_counts)

    plt.figure(figsize=(10, 5))
    sector_counts.plot(kind="bar")
    plt.title("News By Sector")
    plt.xlabel("Sector")
    plt.ylabel("Count")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig("Analysis/sector_distribution.png", dpi=300)
    plt.show()

    print("Sector chart saved.")
    avg_score = df["Score"].mean()
    print("\nAVERAGE SENTIMENT SCORE")
    print(round(avg_score, 3))
    positive_news = df.sort_values(by="Score", ascending=False).head(10)
    print("\nTOP 10 POSITIVE NEWS")
    print(positive_news[["Headline", "Score", "Sentiment"]])
    negative_news = df.sort_values(by="Score", ascending=True).head(10)
    print("\nTOP 10 NEGATIVE NEWS")
    print(negative_news[["Headline", "Score", "Sentiment"]])
    positive_news.to_csv("Analysis/top_positive_news.csv", index=False)
    negative_news.to_csv("Analysis/top_negative_news.csv", index=False)
    print("\nTOP 20 KEYWORDS")

    all_text = " ".join(df["Headline"].astype(str)).lower()
    words = all_text.split()
    stop_words = {"the", "a", "an", "and", "or", "of","to", "in", "on", "for", "with", "at", "by", "is", "are", "was", "were", "be", "as", "from", "that", "this", "it"}
    filtered_words = [word.strip(".,!?()[]{}:;\"'") for word in words if word not in stop_words]
    keyword_counts = Counter(filtered_words)
    top_keywords = keyword_counts.most_common(20)
    keyword_df = pd.DataFrame(top_keywords, columns=["Keyword", "Frequency"])
    print(keyword_df)
    keyword_df.to_csv("Analysis/top_keywords.csv", index=False)

    plt.figure(figsize=(10, 5))
    plt.bar(keyword_df["Keyword"], keyword_df["Frequency"])
    plt.title("Top 20 Keywords")
    plt.xlabel("Keyword")
    plt.ylabel("Frequency")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig("Analysis/top_keywords.png", dpi=300)
    plt.show()
    print("Keyword chart saved.")

    with open("Analysis/summary_report.txt", "w", encoding="utf-8") as f:
        f.write("STOCK MARKET SENTIMENT ANALYSIS REPORT\n")
        f.write("=" * 60 + "\n\n")
        f.write(f"Total News: {len(df)}\n")
        f.write(f"Average Score: {round(avg_score,3)}\n\n")
        f.write("Sentiment Counts:\n")
        f.write(sentiment_counts.to_string())
        f.write("\n\n")
        f.write("Sector Counts:\n")
        f.write(sector_counts.to_string())

    print("\nSummary report saved.")
    print("\nANALYSIS COMPLETED SUCCESSFULLY")

if __name__ == "__main__":
    analyze_data()