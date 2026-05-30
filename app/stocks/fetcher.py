import yfinance as yf


def fetch_stock_data(ticker, period="6mo"):
    try:
        stock = yf.Ticker(ticker)

        df = stock.history(
            period=period,
            interval="1d"
        )

        if df.empty:
            return None

        # Hapus hari tanpa transaksi
        df = df[df["Volume"] > 0]
        df.reset_index(inplace=True)

        return df

    except Exception as e:
        print(f"Error fetching data for {ticker}: {e}")
        return None