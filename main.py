import streamlit as st
import plotly.graph_objects as go

from app.stocks.fetcher import fetch_stock_data
from app.stocks.indicators import calculate_indicators, get_trend
from app.ai.agent import generate_stock_summary
from app.stocks.technical_analysis import build_technical_context


# =========================================================
# KONFIGURASI HALAMAN
# =========================================================

st.set_page_config(
    page_title="Stock AI Assistant",
    page_icon="📈",
    layout="wide"
)


# =========================================================
# FUNGSI FILTER PERIODE
# =========================================================

def filter_period(df, period):
    """
    Memfilter data berdasarkan periode yang dipilih user.

    Data indikator tetap dihitung menggunakan data 5 tahun,
    kemudian hasilnya difilter untuk kebutuhan tampilan.
    """

    if period == "1mo":
        return df.tail(22)

    elif period == "3mo":
        return df.tail(66)

    elif period == "6mo":
        return df.tail(132)

    elif period == "1y":
        return df.tail(252)

    return df


# =========================================================
# FUNGSI CHART HARGA
# =========================================================

def render_price_chart(df):
    """
    Menampilkan Candlestick Chart,
    MA20, dan Bollinger Bands.
    """

    st.subheader("📈 Grafik Harga Saham")

    fig = go.Figure()

    # Candlestick
    fig.add_trace(
        go.Candlestick(
            x=df["Date"],
            open=df["Open"],
            high=df["High"],
            low=df["Low"],
            close=df["Close"],
            name="Candlestick"
        )
    )

    # MA20
    fig.add_trace(
        go.Scatter(
            x=df["Date"],
            y=df["MA_20"],
            mode="lines",
            name="MA 20 Hari"
        )
    )

    # Bollinger Upper
    fig.add_trace(
        go.Scatter(
            x=df["Date"],
            y=df["BB_Upper"],
            mode="lines",
            name="BB Upper"
        )
    )

    # Bollinger Lower
    fig.add_trace(
        go.Scatter(
            x=df["Date"],
            y=df["BB_Lower"],
            mode="lines",
            name="BB Lower"
        )
    )

    fig.update_layout(
        xaxis_title="Tanggal",
        yaxis_title="Harga (IDR)",
        hovermode="x unified",
        template="plotly_dark",
        xaxis_rangeslider_visible=False
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )


# =========================================================
# FUNGSI RSI CHART
# =========================================================

def render_rsi_chart(df):
    """
    Menampilkan grafik RSI 14 hari
    dengan level Overbought dan Oversold.
    """

    st.subheader("📊 RSI (Relative Strength Index)")

    fig_rsi = go.Figure()

    # RSI
    fig_rsi.add_trace(
        go.Scatter(
            x=df["Date"],
            y=df["RSI_14"],
            mode="lines",
            name="RSI 14 Hari"
        )
    )

    # Level Overbought
    fig_rsi.add_hline(
        y=70,
        line_dash="dash",
        annotation_text="Overbought"
    )

    # Level Oversold
    fig_rsi.add_hline(
        y=30,
        line_dash="dash",
        annotation_text="Oversold"
    )

    fig_rsi.update_layout(
        xaxis_title="Tanggal",
        yaxis_title="RSI",
        yaxis_range=[0, 100],
        hovermode="x unified",
        template="plotly_dark"
    )

    st.plotly_chart(
        fig_rsi,
        use_container_width=True
    )


# =========================================================
# FUNGSI STATUS RSI
# =========================================================

def render_rsi_status(df):
    """
    Menampilkan kondisi RSI terbaru.
    """

    latest_rsi = df["RSI_14"].iloc[-1]

    if latest_rsi > 70:

        st.warning(
            f"RSI saat ini adalah {latest_rsi:.2f}, "
            "menunjukkan kondisi overbought."
        )

    elif latest_rsi < 30:

        st.warning(
            f"RSI saat ini adalah {latest_rsi:.2f}, "
            "menunjukkan kondisi oversold."
        )

    else:

        st.info(
            f"RSI saat ini adalah {latest_rsi:.2f}, "
            "menunjukkan kondisi netral."
        )


# =========================================================
# FUNGSI VOLUME ANALYSIS
# =========================================================

def render_volume_analysis(df):
    """
    Menampilkan grafik volume perdagangan
    dan perbandingan dengan rata-rata volume 20 hari.
    """

    st.subheader("📊 Volume Perdagangan")

    # Grafik volume
    fig_volume = go.Figure()

    fig_volume.add_trace(
        go.Bar(
            x=df["Date"],
            y=df["Volume"],
            name="Volume"
        )
    )

    fig_volume.update_layout(
        xaxis_title="Tanggal",
        yaxis_title="Volume",
        hovermode="x unified",
        template="plotly_dark"
    )

    st.plotly_chart(
        fig_volume,
        use_container_width=True
    )

    # Volume terbaru
    latest_volume = df["Volume"].iloc[-1]

    # Rata-rata volume 20 hari
    avg_volume = (
        df["Volume"]
        .rolling(window=20)
        .mean()
        .iloc[-1]
    )

    # Tampilkan metric
    col1, col2 = st.columns(2)

    with col1:
        st.metric(
            label="Volume Perdagangan Terakhir",
            value=f"{latest_volume:,.0f}"
        )

    with col2:
        st.metric(
            label="Rata-rata Volume 20 Hari",
            value=f"{avg_volume:,.0f}"
        )

    # Volume insight
    if latest_volume > avg_volume:

        st.success(
            "Volume perdagangan saat ini berada di atas "
            "rata-rata 20 hari."
        )

    elif latest_volume < avg_volume:

        st.info(
            "Volume perdagangan saat ini berada di bawah "
            "rata-rata 20 hari."
        )

    else:

        st.info(
            "Volume perdagangan saat ini berada di sekitar "
            "rata-rata 20 hari."
        )


# =========================================================
# FUNGSI DATA SAHAM
# =========================================================

def render_stock_data(df):
    """
    Menampilkan data saham terbaru
    dan seluruh data historis.
    """

    st.subheader("📊 Data Saham")

    # Tampilkan 5 data terbaru
    st.dataframe(
        df.tail()
    )

    # Tampilkan semua data
    with st.expander("Lihat semua data"):

        st.dataframe(
            df
        )


# =========================================================
# MAIN APPLICATION
# =========================================================

def main():

    # Judul aplikasi
    st.title("📈 Stock AI Assistant")

    st.write(
        "Tanyakan analisa saham Indonesia sederhana."
    )

    # Input ticker
    ticker = st.text_input(
        "Masukkan kode saham",
        value="BBCA.JK"
    )

    # Pilihan periode
    period = st.selectbox(
        "Pilih periode",
        ["1mo", "3mo", "6mo", "1y"],
        index=0
    )

    # Tombol analisa
    if st.button("Analisa"):

        with st.spinner(
            "Mengambil data saham..."
        ):

            # Ambil data 5 tahun
            # Digunakan untuk perhitungan indikator
            raw_df = fetch_stock_data(
                ticker,
                "5y"
            )

            # Validasi data
            if raw_df is None or raw_df.empty:

                st.error(
                    "Data saham tidak ditemukan."
                )

                return

            # Hitung semua indikator
            raw_df = calculate_indicators(
                raw_df
            )

            # Filter data berdasarkan periode
            df = filter_period(
                raw_df,
                period
            )

            # Hitung trend
            trend = get_trend(
                df
            )

            technical_context = build_technical_context(
                df,
                ticker
            )

            # Generate AI Summary
            summary = generate_stock_summary(
                ticker=ticker,
                technical_context=technical_context
            )

            st.success(
                "Analisa selesai"
            )

            # =================================================
            # AI SUMMARY
            # =================================================

            st.subheader(
                "📌 Ringkasan AI"
            )

            st.write(
                summary
            )

            # =================================================
            # PRICE CHART
            # =================================================

            render_price_chart(
                df
            )

            # =================================================
            # RSI
            # =================================================

            render_rsi_chart(
                df
            )

            render_rsi_status(
                df
            )

            # =================================================
            # TREND
            # =================================================

            st.metric(
                label="Trend Saat Ini",
                value=trend.capitalize()
            )

            # =================================================
            # VOLUME
            # =================================================

            render_volume_analysis(
                df
            )

            # =================================================
            # STOCK DATA
            # =================================================

            render_stock_data(
                df
            )


# =========================================================
# RUN APPLICATION
# =========================================================

if __name__ == "__main__":
    main()