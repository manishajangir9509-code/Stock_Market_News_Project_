import requests
import csv
from bs4 import BeautifulSoup
from textblob import TextBlob
from datetime import datetime
import os

def stock_market_data():
    os.makedirs("DATA", exist_ok=True)
    os.makedirs("Reports", exist_ok=True)

    url = "https://finance.yahoo.com/news/"
    headers = {"User-Agent": "Mozilla/5.0"}

    try:
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status(

            
        )

    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
        return

    soup = BeautifulSoup(response.text, "html.parser")
    articles = soup.find_all("h3")

    if not articles:
        print("No news articles found!")
        return

    sector_map = {
        "Tesla": "Technology / EV",
        "Elon Musk": "Technology / EV",
        "Apple": "Technology",
        "Microsoft": "Technology",
        "Amazon": "E-commerce",
        "Google": "Technology",
        "Alphabet": "Technology",
        "Meta": "Technology",
        "Nvidia": "Technology / AI",
        "Bank": "Banking",
        "Gold": "Commodities",
        "Oil": "Energy",
        "Power": "Energy",
        "Plug Power": "Energy / Hydrogen",
        "Dividend": "Investment / Finance",
        "Markets": "Finance",
        "Stocks": "Finance",
        "Income": "Finance",
        "Costco": "Retail"
        }

    stock_data = []
    seen_headlines = set()
    date = datetime.now().strftime("%Y-%m-%d")

    for article in articles:
        headline = article.get_text(strip=True)

        if len(headline) < 10:
            continue

        if headline in seen_headlines:
            continue

        seen_headlines.add(headline)
        source = "Yahoo Finance"
        score = TextBlob(headline).sentiment.polarity

        if score > 0:
            sentiment = "Positive"
        elif score < 0:
            sentiment = "Negative"
        else:
            sentiment = "Neutral"

        sector = "General Finance"
        company = "Unknown"

        for key, value in sector_map.items():
            if key.lower() in headline.lower():
                company = key
                sector = value
                break
        stock_data.append([headline, date, source, company, round(score, 3), sector, sentiment])

    if not stock_data:
        print("No valid news collected!")
        return
    csv_file = "DATA/news.csv"

    with open(csv_file, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["Headline", "Date", "Source", "Company", "Score", "sector", "Sentiment"])
        writer.writerows(stock_data)

    print(f"CSV saved successfully: {csv_file}")
    report_file = "Reports/report.txt"

    with open(report_file, "w", encoding="utf-8") as f:
        f.write("STOCK MARKET SENTIMENT REPORT\n")
        f.write("=" * 80 + "\n\n")
        for news in stock_data:
            f.write(f"Headline  : {news[0]}\n")
            f.write(f"Date      : {news[1]}\n")
            f.write(f"Source    : {news[2]}\n")
            f.write(f"Company   : {news[3]}\n")
            f.write(f"Score     : {news[4]}\n")
            f.write(f"Sector    : {news[5]}\n")
            f.write(f"Sentiment : {news[6]}\n")
            f.write("-" * 80 + "\n")

    print(f"Report saved successfully: {report_file}")
    print(f"\nTotal News Collected: {len(stock_data)}")

if __name__ == "__main__":
    stock_market_data()