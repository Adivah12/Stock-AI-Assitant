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
'''

⚙️ Installation

Clone this repository:

git clone https://github.com/Adivah12/Stock-AI-Assitant.git

Move into the project directory:

cd Stock-AI-Assitant

Create a virtual environment:

python -m venv venv

Activate the virtual environment on Windows:

venv\Scripts\activate

Install dependencies:

pip install -r requirements.txt
▶️ Run the Application

Run the Streamlit application:

streamlit run main.py

Or:

python -m streamlit run main.py

The application will open in your browser.

📊 Analysis Features
Candlestick Chart

Displays:

Open price
High price
Low price
Close price

The chart also includes:

MA20
Bollinger Upper Band
Bollinger Lower Band
RSI 14

The application calculates RSI using a 14-day period.

The RSI analysis uses:

RSI > 70 → Overbought
RSI < 30 → Oversold
RSI 30–70 → Neutral
Volume Analysis

The application displays:

Latest trading volume
20-day average volume
Historical trading volume chart

The latest volume is compared with the 20-day average to provide a basic volume insight.

🤖 AI Stock Summary

The AI assistant generates a basic stock analysis based on:

Stock price data
Current trend
Technical indicators

Example:

BBCA.JK shows a bullish short-term trend with price moving above MA20.
Recent trading activity remains stable based on the available market data.

Note: AI-generated analysis is for educational and informational purposes only and should not be considered financial advice.

📸 Application Preview
Stock Analysis Dashboard

Add your application screenshot here:

![Stock AI Assistant Dashboard](docs/images/dashboard.png)
🗺️ Project Roadmap
Phase 1 — AI Stock Assistant Sederhana
 Stock data fetching
 MA20 indicator
 AI-generated stock summary
 Interactive stock chart
 Historical stock data
Phase 2 — Technical Analysis Enhancement
 Candlestick chart
 RSI 14
 Bollinger Bands
 Volume analysis
 20-day average volume
 Basic trend analysis
Phase 3 — AI Technical Intelligence

Planned improvements:

 AI technical insight
 AI analysis using multiple indicators
 Technical signal generation
 Buy / Hold / Sell analysis
 Explainable AI analysis
 News sentiment analysis
Phase 4 — Advanced Stock Assistant

Planned improvements:

 Multi-stock comparison
 Portfolio monitoring
 Watchlist
 News aggregation
 Advanced sentiment analysis
 Conversational stock assistant
 Agentic AI workflow
⚠️ Disclaimer

This project is developed for educational and experimental purposes.

The information and AI-generated analysis provided by this application should not be considered financial advice or a recommendation to buy or sell any financial instrument.

Always conduct your own research and consult a qualified financial professional before making investment decisions.

📌 Project Status

Current Version: Phase 2

Status: Technical Analysis Enhancement Completed

Next Goal: AI Technical Intelligence

👨‍💻 Author

Aditya Vahreza
