import pandas as pd

def generate_stock_summary(df, ticker, trend):

    latest = df.iloc[-1]
    close_price = latest["Close"]
    volume = latest["Volume"]
    daily_return = latest["Daily_Return"]

    if pd.isna(daily_return):
        daily_return = 0

    if trend == "bulish":
        trend_text = " menunjukkan tren naik karena harga penutupan berada di atas MA 20 hari."
    elif trend == "downtrend":
        trend_text = " menunjukkan tren turun karena harga penutupan berada di bawah MA 20 hari."
    else:
        trend_text = " menunjukkan tren sideway karena harga penutupan berada di sekitar MA 20 hari."

    summary = f"""
    anaisa saham {ticker}
    harga penutupan terakhir adalah {close_price:.2f}
    perubahan harian adalah {daily_return:.2f}%
    volume perdagangan adalah {volume:,.0f}
    secara teknikal, saham {ticker} {trend_text}
    """
    return summary.strip()