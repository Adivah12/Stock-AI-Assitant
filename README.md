# 📈 Stock AI Assistant

AI-powered stock analysis dashboard for Indonesian stocks built with **Python**, **Streamlit**, **Yahoo Finance**, **Plotly**, and **Google Gemini**.

---

## 📌 Overview

**Stock AI Assistant** is a web-based dashboard designed to help users analyze Indonesian stock market data through interactive technical analysis and AI-generated insights.

The application combines traditional technical indicators with Generative AI to provide a more understandable interpretation of stock market conditions.

Users can:

* 🔎 Search Indonesian stocks by ticker symbol
* 📊 View historical stock price data
* 📈 Analyze Moving Average 20 (MA20)
* 📉 Analyze RSI (Relative Strength Index)
* 📊 Analyze Bollinger Bands
* 🕯️ View Candlestick charts
* 📦 Compare trading volume with Volume MA20
* 🤖 Generate AI-powered technical analysis
* 📋 Explore historical stock data

> ⚠️ **Disclaimer:** This application is intended for educational and informational purposes only. The analysis provided by the application is not financial advice or a guarantee of investment returns.

---

# 🚀 Features

## Phase 1 — Basic Stock Analysis ✅

* ✅ Search Indonesian stocks by ticker symbol
* ✅ Fetch stock data from Yahoo Finance using `yfinance`
* ✅ Interactive stock price chart using Plotly
* ✅ Moving Average 20 (MA20)
* ✅ AI-generated stock summary
* ✅ Historical stock data table

---

## Phase 2 — Technical Analysis ✅

The application was extended with several technical indicators and visualization features.

* ✅ RSI (Relative Strength Index) 14
* ✅ RSI overbought and oversold detection
* ✅ Bollinger Bands
* ✅ Candlestick chart
* ✅ Volume Moving Average 20 (Volume MA20)
* ✅ Technical trend detection based on MA20
* ✅ Technical indicator visualization using Plotly

### Technical Indicators

| Indicator       | Purpose                                             |
| --------------- | --------------------------------------------------- |
| MA20            | Identify short-term price trend                     |
| RSI14           | Analyze momentum and overbought/oversold conditions |
| Bollinger Bands | Analyze price position and volatility               |
| Volume MA20     | Compare current trading volume with average volume  |

---

## Phase 3 — AI Technical Analysis ✅

The application now uses **Google Gemini** to interpret technical indicators and generate structured AI-powered insights.

The analysis pipeline works as follows:

```text
Stock Data
    ↓
Technical Indicators
    ↓
Technical Analysis Context
    ↓
Google Gemini
    ↓
AI Technical Insight
```

The AI analysis includes:

* 📈 **Trend Analysis**
* 💪 **Momentum Analysis**
* 📊 **Bollinger Bands Analysis**
* 📦 **Volume Analysis**
* 🔎 **Overall Technical Analysis**
* ⚠️ **Technical Risk Note**

The AI considers multiple technical indicators together instead of analyzing each indicator independently.

For example:

```text
MA20
→ Price above MA20
→ Bullish signal

RSI14
→ Neutral momentum

Bollinger Bands
→ Price in middle area

Volume
→ Below average

Overall
→ Potential consolidation / weak bullish condition
```

This approach allows the AI to identify potential conflicts between technical indicators and provide a more comprehensive explanation.

---

# 🛠️ Tech Stack

* **Python**
* **Streamlit**
* **Pandas**
* **Plotly**
* **yfinance**
* **TA**
* **Google Gemini API**
* **python-dotenv**

---

# 📂 Project Structure

```text
Stock-AI-Assistant/
│
├── app/
│   │
│   ├── ai/
│   │   └── agent.py
│   │
│   ├── pipeline/
│   │   ├── Preprocess.py
│   │   └── storage.py
│   │
│   ├── stocks/
│   │   ├── fetcher.py
│   │   ├── indicators.py
│   │   └── technical_analysis.py
│   │
│   └── utils/
│
├── tests/
│
├── data/
│
├── notebooks/
│
├── main.py
├── requirements.txt
├── .gitignore
└── README.md
```

### Module Description

| Module                  | Description                                                        |
| ----------------------- | ------------------------------------------------------------------ |
| `fetcher.py`            | Fetches stock market data from Yahoo Finance                       |
| `indicators.py`         | Calculates technical indicators                                    |
| `technical_analysis.py` | Builds technical context for AI analysis                           |
| `agent.py`              | Sends technical context to Google Gemini and generates AI insights |
| `main.py`               | Streamlit application and user interface                           |
| `tests/`                | Testing modules for application components                         |

---

# ⚙️ Installation

## 1. Clone Repository

```bash
git clone https://github.com/Adivah12/Stock-AI-Assitant.git
cd Stock-AI-Assitant
```

---

## 2. Create Virtual Environment

```bash
python -m venv venv
```

Activate the virtual environment.

### Windows

```bash
venv\Scripts\activate
```

### Linux / macOS

```bash
source venv/bin/activate
```

---

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

# 🔑 Environment Variables

The application uses the **Google Gemini API** to generate AI-powered technical analysis.

Create a `.env` file in the root project directory:

```text
GEMINI_API_KEY=your_gemini_api_key
```

Make sure `.env` is included in `.gitignore`:

```text
.env
```

> ⚠️ Never upload your API key or `.env` file to GitHub.

---

# ▶️ Run the Application

Start the Streamlit application:

```bash
streamlit run main.py
```

Then open the application in your browser:

```text
http://localhost:8501
```

---

# 📊 Example Output

The application provides an interactive technical analysis dashboard containing:

### 📈 Stock Price Chart

* Candlestick chart
* MA20
* Bollinger Upper Band
* Bollinger Lower Band

### 📊 RSI Chart

* RSI14
* Overbought level (70)
* Oversold level (30)

### 📦 Volume Analysis

* Current trading volume
* Volume MA20
* Comparison between current volume and average volume

### 🤖 AI Technical Insight

The AI generates a structured analysis containing:

```text
📈 Trend

💪 Momentum

📊 Bollinger Bands

📦 Volume

🔎 Overall Analysis

⚠️ Risk Note
```

The AI analysis is generated based on the technical context calculated by the application.

---

# 📡 Data Source

Stock market data is retrieved from:

* **Yahoo Finance**
* Python library: `yfinance`

Technical indicators are calculated using:

* Python library: `ta`

AI-generated analysis is powered by:

* **Google Gemini API**

---

# 🗺️ Roadmap

## Phase 4 — Technical Signal Engine 🚧

Planned improvements:

* ⬜ Rule-based technical signal engine
* ⬜ Bullish / Bearish / Neutral classification
* ⬜ Signal strength scoring
* ⬜ Multi-indicator signal combination
* ⬜ Support and resistance detection
* ⬜ Technical risk level
* ⬜ AI explanation of technical signals

Planned architecture:

```text
Technical Indicators
        ↓
Signal Engine
        ↓
Technical Signal
        ↓
Google Gemini
        ↓
AI Explanation
```

---

## Phase 5 — Advanced Analysis 🔮

Future improvements:

* ⬜ Buy / Hold / Sell decision support
* ⬜ Multi-stock comparison
* ⬜ News sentiment analysis
* ⬜ Fundamental analysis
* ⬜ Portfolio watchlist
* ⬜ Stock screening
* ⬜ Historical signal backtesting
* ⬜ Performance evaluation of technical signals

---

# ⚠️ Disclaimer

Stock AI Assistant is an educational and informational project.

The technical analysis and AI-generated insights provided by this application are based on available market data and technical indicators. They should not be considered financial advice, investment recommendations, or a guarantee of future performance.

Users should conduct their own research and consider consulting a qualified financial professional before making investment decisions.

---

# 👨‍💻 Author

**Aditya Vahreza**

Machine Learning & Data Science Enthusiast
