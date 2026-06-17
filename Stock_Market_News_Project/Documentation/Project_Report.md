# STOCK MARKET NEWS SCRAPER & SENTIMENT ANALYSIS SYSTEM

## Project Report

### Submitted By

**Manisha Jangir**

### Technology Used

Python, Streamlit, Pandas, BeautifulSoup, Requests, TextBlob

### Academic Year

2024-25

---

# CERTIFICATE

This is to certify that the project titled **"Stock Market News Scraper & Sentiment Analysis System"** has been successfully completed by **Manisha Jangir** as part of academic requirements. The project demonstrates the application of web scraping, natural language processing, sentiment analysis, and data visualization techniques using Python.

---

# ACKNOWLEDGEMENT

I would like to express my sincere gratitude to my teachers, mentors, and everyone who supported me throughout the development of this project. Their guidance and encouragement helped me successfully complete this project.

---

# ABSTRACT

The Stock Market News Scraper & Sentiment Analysis System is a Python-based application developed to collect stock market news from online financial websites and analyze the sentiment of the collected news articles. The system automatically scrapes financial news, processes textual data, classifies sentiments into Positive, Negative, and Neutral categories, and displays the results through an interactive Streamlit dashboard.

The project helps investors and analysts understand market sentiment by analyzing financial news trends. The dashboard provides visual insights through charts and statistics, making decision-making easier.

---

# TABLE OF CONTENTS

1. Introduction
2. Objectives
3. Problem Statement
4. System Requirements
5. Methodology
6. System Architecture
7. Modules Description
8. Technologies Used
9. Database Structure
10. Implementation
11. Results
12. Advantages
13. Limitations
14. Future Scope
15. Conclusion
16. References

---

# 1. INTRODUCTION

Financial markets are heavily influenced by news and public sentiment. Investors frequently analyze market news before making investment decisions. Manually monitoring large amounts of financial news is time-consuming and inefficient.

This project automates the process of collecting stock market news and analyzing sentiment using Natural Language Processing (NLP). The system provides quick insights into market sentiment and presents the information in an easy-to-understand dashboard.

---

# 2. OBJECTIVES

The main objectives of this project are:

* To automate stock market news collection.
* To perform sentiment analysis on financial news.
* To classify news into Positive, Negative, and Neutral sentiments.
* To store processed data efficiently.
* To provide interactive visualizations.
* To assist users in understanding market trends.

---

# 3. PROBLEM STATEMENT

Investors and traders rely heavily on financial news to make decisions. However, manually collecting and analyzing large volumes of news is difficult and time-consuming.

The proposed system addresses this issue by automatically scraping news articles and analyzing sentiment using NLP techniques, providing instant insights into market conditions.

---

# 4. METHODOLOGY

The project follows the following workflow:

1. News Collection
2. Data Cleaning
3. Sentiment Analysis
4. Data Storage
5. Data Visualization

---

# 5. SYSTEM ARCHITECTURE

News Websites
↓
Web Scraper
↓
Raw News Data
↓
Data Cleaning
↓
Sentiment Analysis
↓
CSV Storage
↓
Visualization
↓
Streamlit Dashboard

---

# 6. MODULES DESCRIPTION

## 6.1 News Scraper Module

This module collects stock market news from online financial websites using Requests and BeautifulSoup.

Functions:

* Fetch web pages
* Extract headlines
* Extract article information
* Save data into CSV files

---

## 6.2 Sentiment Analysis Module

This module processes the news text and performs sentiment analysis using TextBlob.

Functions:

* Calculate polarity score
* Determine sentiment category
* Generate analyzed dataset

Sentiment Rules:

Positive → Polarity > 0

Neutral → Polarity = 0

Negative → Polarity < 0

---

## 6.3 Dashboard Module

The dashboard provides interactive visualizations and statistics.

Functions:

* Display latest news
* Sentiment filtering
* Pie charts
* Bar charts
* Sentiment statistics

---

# 7. TECHNOLOGIES USED

## Programming Language

Python

## Libraries

### Requests

Used for downloading webpage content.

### BeautifulSoup

Used for extracting information from HTML pages.

### Pandas

Used for data cleaning and manipulation.

### TextBlob

Used for sentiment analysis.

### Streamlit

Used for dashboard development.

### Matplotlib

Used for chart generation.

---

# 8. DATABASE STRUCTURE

## stock_news.csv

| Field    |
| -------- |
| Date     |
| Source   |
| Headline |
| Link     |

## analyzed_news.csv

| Field     |
| --------- |
| Date      |
| Source    |
| Headline  |
| Polarity  |
| Sentiment |

---

# 9. IMPLEMENTATION

## Step 1

Run News Scraper

python scraper.py

## Step 2

Run Sentiment Analysis

python analysis.py

## Step 3

Launch Dashboard

streamlit run dashboard.py

---

# 10. RESULTS

The system successfully:

* Collected stock market news.
* Processed financial text.
* Classified sentiments.
* Generated sentiment statistics.
* Displayed visual charts.
* Presented information through Streamlit dashboard.

---

# 11. ADVANTAGES

* Automated news collection.
* Fast sentiment analysis.
* Easy-to-use interface.
* Real-time insights.
* Helpful for investors and researchers.
* Lightweight and scalable.

---

# 12. LIMITATIONS

* Depends on website structure.
* Limited sentiment accuracy using TextBlob.
* Does not predict stock prices.
* Requires internet connection.

---

# 13. FUTURE SCOPE

Future enhancements may include:

* Real-time news APIs.
* FinBERT sentiment model.
* Machine learning predictions.
* Stock price integration.
* Email notifications.
* Advanced market trend forecasting.
* Multi-language sentiment analysis.

---

# 14. CONCLUSION

The Stock Market News Scraper & Sentiment Analysis System successfully automates financial news collection and sentiment analysis. The system provides valuable insights into market sentiment and demonstrates the practical application of web scraping, NLP, and data visualization techniques.

The project can be further extended using advanced AI and machine learning models to improve prediction accuracy and provide deeper market intelligence.

---

# 15. REFERENCES

1. Python Official Documentation
2. Pandas Documentation
3. Streamlit Documentation
4. BeautifulSoup Documentation
5. TextBlob Documentation
6. Financial News Websites
7. NLP Research Articles

---

# THANK YOU
