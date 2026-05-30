Stock AI Assistant

A simple AI-powered stock analysis dashboard built with Streamlit.

Features
Phase 1
Search Indonesian stocks by ticker symbol
Fetch stock price data using Yahoo Finance API
Interactive stock price chart using Plotly
Moving Average 20 (MA20) indicator
AI-generated stock summary analysis
Historical stock data table
Tech Stack
Python
Streamlit
Plotly
yfinance
OpenAI API
Project Structure
app/
├── ai/
│   └── agent.py
│
├── stocks/
│   ├── fetcher.py
│   └── indicators.py
│
└── main.py
How to Run

Install dependencies:

pip install -r requirements.txt

Run Streamlit:

streamlit run app.py
Example Features
Stock Price Chart
Closing Price
Moving Average 20
AI Summary

Example:

BBCA.JK shows a bullish short-term trend with price moving above MA20.
Momentum remains positive with stable recent trading activity.
Future Roadmap (Phase 2)

Planned improvements:

RSI indicator
Candlestick chart
Bollinger Bands
Buy / Hold / Sell AI recommendation
Multi-stock comparison
News sentiment analysis
