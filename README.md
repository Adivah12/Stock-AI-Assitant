# 📈 Stock AI Assistant

An AI-powered stock analysis dashboard designed to analyze Indonesian stock market trends using historical data, technical indicators, interactive charts, and AI-generated insights.

---

## 🌟 Overview

**Stock AI Assistant** simplifies technical analysis for the Indonesian stock market (`.JK` tickers). Built with Python and Streamlit, it fetches live and historical market data, calculates key technical indicators, and leverages OpenAI to generate easy-to-understand stock summaries.

---

## 🚀 Key Features

### 🔹 Phase 1 — Core Functionality
* 🔍 **Ticker Search:** Search Indonesian stocks by ticker symbol (e.g., `BBCA.JK`, `TLKM.JK`).
* 📊 **Market Data:** Fetch historical stock data via Yahoo Finance (`yfinance`).
* 🗓️ **Custom Range:** Flexible selection for analysis periods.
* 📈 **Interactive Charts:** Price visualization powered by Plotly.
* 🤖 **AI Summaries:** Automated stock analysis powered by OpenAI API.
* 📋 **Data Tables:** View raw historical price and volume data.

### 🔹 Phase 2 — Technical Analysis
* 🕯️ **Candlestick Charts:** High-detail price movement visualization.
* 📉 **Moving Averages:** 20-day Moving Average (MA20) trend line.
* 🎯 **RSI (14):** Relative Strength Index with Overbought/Oversold detection.
* 📊 **Bollinger Bands:** Volatility bands for overextended market moves.
* 🔊 **Volume Analysis:** Trading volume tracking against 20-day average volume.
* ⚡ **Trend Detection:** Instant identification of short-term price trends.

---

## 🛠️ Tech Stack

| Domain | Technology / Library |
| :--- | :--- |
| **Language** | Python |
| **UI Framework** | Streamlit |
| **Visualization** | Plotly |
| **Data & Finance** | `yfinance`, `pandas`, `ta` (Technical Analysis) |
| **AI Engine** | OpenAI API |

---

## 📂 Project Structure

```text
Stock-AI-Assistant/
├── app/
│   ├── ai/
│   │   └── agent.py         # AI prompt logic & OpenAI connection
│   └── stocks/
│       ├── fetcher.py       # Data fetching from yfinance
│       └── indicators.py    # RSI, MA20, Bollinger Bands calculation
├── tests/
│   └── test_indicators.py   # Unit tests for technical indicators
├── main.py                  # Streamlit application entry point
├── requirements.txt         # Project dependencies
├── README.md                # Project documentation
└── .gitignore               # Git ignore rules
