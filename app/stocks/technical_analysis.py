def build_technical_context(df, ticker):

    latest = df.iloc[-1]

    close = latest["Close"]
    ma20 = latest["MA_20"]
    rsi = latest["RSI_14"]
    bb_upper = latest["BB_Upper"]
    bb_lower = latest["BB_Lower"]
    volume = latest["Volume"]
    volume_ma20 = latest["Volume_MA_20"]


    if close > ma20:
        trend = "Harga berada di atas MA20"
    elif close < ma20:
        trend = "Harga berada di bawah MA20"
    else:
        trend = "Harga berada di sekitar MA20"


    if rsi > 70:
        momentum = "RSI menunjukkan kondisi overbought"
    elif rsi < 30:
        momentum = "RSI menunjukkan kondisi oversold"
    else:
        momentum = "RSI berada dalam zona netral"


    if close >= bb_upper:
        bb_position = "Harga berada di sekitar atau di atas upper band"

    elif close <= bb_lower:
        bb_position = "Harga berada di sekitar atau di bawah lower band"

    else:
        bb_position = "Harga berada di dalam Bollinger Bands"


    if volume > volume_ma20:
        volume_status = "Volume berada di atas rata-rata 20 hari"

    else:
        volume_status = "Volume berada di bawah rata-rata 20 hari"


    context = f"""
    Ticker: {ticker}

    Harga terakhir: {close:.2f}
    MA20: {ma20:.2f}
    RSI14: {rsi:.2f}

    Bollinger Upper: {bb_upper:.2f}
    Bollinger Lower: {bb_lower:.2f}

    Volume: {volume:,.0f}
    Volume MA20: {volume_ma20:,.0f}

    Technical Interpretation:

    Trend:
    {trend}

    Momentum:
    {momentum}

    Bollinger Bands:
    {bb_position}

    Volume:
    {volume_status}
    """

    return context