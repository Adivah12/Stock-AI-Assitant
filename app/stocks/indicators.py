import pandas as pd 
import ta

def calculate_indicators(df):
    df = df.copy()
    # Tambahkan indikator teknikaL

    # Moving Average 20 hari
    df["MA_20"] = ta.trend.SMAIndicator(
        close=df["Close"],
        window=20
        ).sma_indicator()

    # Volume Moving Average 20 hari
    df["Volume_MA_20"] = ta.trend.SMAIndicator(
        close=df["Volume"],
        window=20
        ).sma_indicator()

    # daily return
    df["Daily_Return"] = df["Close"].pct_change()*100

    # RSI 14 hari
    df["RSI_14"] = ta.momentum.RSIIndicator(
        close=df["Close"],
        window=14
        ).rsi()

    # Bollinger bands
    bollinger = ta.volatility.BollingerBands(   
        close=df["Close"],
        window=20,
        window_dev=2
    )

    df["BB_Upper"] = bollinger.bollinger_hband()
    df["BB_Middle"] = bollinger.bollinger_mavg()
    df["BB_Lower"] = bollinger.bollinger_lband()
    
    return df

def get_trend(df):
    latest_close = df["Close"].iloc[-1]
    ma_20 = df["MA_20"].iloc[-1]

    if pd.isna(ma_20):
        return "neutral"
    if latest_close > ma_20:
        return "uptrend"
    elif latest_close < ma_20:
        return "downtrend"
    else:
        return "sideways"
    