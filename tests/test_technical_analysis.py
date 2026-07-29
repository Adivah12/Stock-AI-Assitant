from app.stocks.fetcher import fetch_stock_data
from app.stocks.indicators import calculate_indicators, get_trend
from app.stocks.technical_analysis import prepare_technical_context


# =========================================
# 1. AMBIL DATA SAHAM
# =========================================

df = fetch_stock_data(
    "BBCA.JK",
    "5y"
)


# =========================================
# 2. CEK DATA
# =========================================

if df is None or df.empty:

    print("❌ Data saham tidak ditemukan.")

else:

    print("✅ Data saham berhasil diambil.")

    # =========================================
    # 3. HITUNG INDIKATOR
    # =========================================

    df = calculate_indicators(df)

    print("✅ Indikator berhasil dihitung.")

    # =========================================
    # 4. HITUNG TREND
    # =========================================

    trend = get_trend(df)

    print(f"✅ Trend: {trend}")

    # =========================================
    # 5. SIAPKAN TECHNICAL CONTEXT
    # =========================================

    technical_context = prepare_technical_context(
        df,
        trend
    )

    # =========================================
    # 6. TAMPILKAN HASIL
    # =========================================

    print("\n" + "=" * 40)
    print("TECHNICAL CONTEXT")
    print("=" * 40)

    for key, value in technical_context.items():

        print(f"{key}: {value}")