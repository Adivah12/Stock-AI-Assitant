# 📈 Stock AI Assistant

Stock AI Assistant is a simple AI-powered stock analysis dashboard built with Python and Streamlit.

The project is designed to provide basic stock analysis for Indonesian stocks using historical market data, technical indicators, interactive charts, and AI-generated summaries.

---

## 🚀 Features

### Phase 1 — AI Stock Assistant Sederhana

- ✅ Search Indonesian stocks by ticker symbol
- ✅ Fetch stock data using Yahoo Finance (`yfinance`)
- ✅ Select analysis period
- ✅ AI-generated stock summary analysis
- ✅ Historical stock data table
- ✅ Interactive stock price chart using Plotly
- ✅ Moving Average 20 (MA20) indicator

### Phase 2 — Technical Analysis Enhancement

- ✅ Candlestick chart
- ✅ Moving Average 20 (MA20)
- ✅ RSI 14 (Relative Strength Index)
- ✅ RSI overbought and oversold status
- ✅ Bollinger Bands
- ✅ Volume trading analysis
- ✅ 20-day average volume comparison
- ✅ Current trend analysis

---

## 🛠️ Tech Stack

- Python
- Streamlit
- Plotly
- yfinance
- pandas
- ta
- OpenAI API

---

## 📂 Project Structure

```text
Stock-AI-Assistant/
│
├── app/
│   ├── ai/
│   │   └── agent.py
│   │
│   └── stocks/
│       ├── fetcher.py
│       └── indicators.py
│
├── tests/
│   └── test_indicators.py
│
├── main.py
├── requirements.txt
├── README.md
└── .gitignore

