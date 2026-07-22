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

## Installation

Clone repository:

```bash
git clone https://github.com/your-username/stock-ai-assistant.git
cd stock-ai-assistant
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Run the App

Start Streamlit locally:

```bash
streamlit run main.py
```

Then open:

```bash
http://localhost:8501
```

---

## Example Output
<img width="1800" height="904" alt="image" src="https://github.com/user-attachments/assets/17c82d92-7fe9-43ae-aa38-d8eb97050d38" />
<img width="1861" height="568" alt="image" src="https://github.com/user-attachments/assets/eda85f5b-c29f-4fe9-b00c-110e297bfdc3" />



### Stock Price Chart

* Closing Price
* MA20 Trend Line

### AI Summary Example

```text
BBCA.JK shows a bullish short-term trend with price moving above MA20.
Momentum remains positive with stable recent trading activity.
```

---

## Data Source

Stock market data is retrieved from:

* Yahoo Finance (`yfinance`)

---

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

---

## Author

**Aditya Vahreza**

Machine Learning & Data Science Enthusiast

```
```
