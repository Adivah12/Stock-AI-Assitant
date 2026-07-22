from app.stocks.fetcher import fetch_stock_data
from app.stocks.indicators import calculate_indicators, get_trend


# Ambil data saham
ticker = "BBCA.JK"

df = fetch_stock_data(
    ticker=ticker,
    period="6mo"
)

# Pastikan data berhasil diambil
if df is None or df.empty:
    print("Data saham tidak ditemukan.")
else:

    # Hitung indikator
    df = calculate_indicators(df)

    # Ambil trend
    trend = get_trend(df)

    print("\n=== HASIL TEST INDIKATOR ===")
    print(f"Ticker : {ticker}")
    print(f"Trend  : {trend}")

    print("\n=== KOLOM DATA ===")
    print(df.columns.tolist())

    print("\n=== 10 DATA TERAKHIR ===")
    print(
        df[
            [
                "Date",
                "Close",
                "MA_20",
                "Daily_Return",
                "RSI_14",
                "BB_Upper",
                "BB_Middle",
                "BB_Lower"
            ]
        ].tail(10)
    )