# 📈 Stock AI Assistant

AI-powered stock analysis dashboard for Indonesian stocks built with **Streamlit**, **Yahoo Finance**, and **OpenAI**.

---

## Overview

Stock AI Assistant is a web-based dashboard that helps users analyze Indonesian stock market data interactively.

Users can:

* Search stock data by ticker symbol
* View historical stock prices
* Analyze moving averages
* Get AI-generated stock insights
* Explore stock performance visually

---

## Features

### Phase 1 (Completed)

*✅ Search Indonesian stocks by ticker symbol
*✅ Fetch stock data from Yahoo Finance API
*✅ Interactive stock chart using Plotly
*✅ Moving Average 20 (MA20) indicator
*✅ AI-generated stock summary analysis
*✅ Historical stock data table

---

## Tech Stack

* **Python**
* **Streamlit**
* **Plotly**
* **yfinance**
* **OpenAI API**
* **Pandas**

---

## Project Structure

```bash
app/
├── ai/
│   └── agent.py
│
├── pipeline/
│   ├── Preprocess.py
│   └── storage.py
│
├── stocks/
│   ├── fetcher.py
│   └── indicators.py
│
├── utils/
│
main.py
requirements.txt
```

---

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

## Roadmap — Phase 2

Planned next features:

* RSI Indicator
* Candlestick Chart
* Bollinger Bands
* Buy / Hold / Sell recommendation
* Multi-stock comparison
* News sentiment analysis
* Portfolio watchlist

---

## Author

**Aditya Vahreza**

Machine Learning & Data Science Enthusiast

```
```
