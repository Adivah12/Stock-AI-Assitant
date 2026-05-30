import pandas as pd 

def calculate_indicators(df):
    df = df.copy()
    # Tambahkan indikator teknikaL

    # Moving Average 20 hari
    df["MA_20"] = df["Close"].rolling(window=20).mean()

    # daily return
    df["Daily_Return"] = df["Close"].pct_change()*100
    
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
    