import streamlit as st
import plotly.graph_objects as go

from app.stocks.fetcher import fetch_stock_data
from app.stocks.indicators import calculate_indicators, get_trend
from app.ai.agent import generate_stock_summary


# konfigurasi halaman
st.set_page_config(
    page_title="Stock AI Assistant",
    page_icon="📈",
    layout="wide"
)


# judul
st.title("📈 Stock AI Assistant")
st.write("Tanyakan analisa saham Indonesia sederhana.")


# input user
ticker = st.text_input(
    "Masukkan kode saham",
    value="BBCA.JK"
)


period = st.selectbox(
    "Pilih periode",
    ["1mo", "3mo", "6mo", "1y"],
    index=0
)


# tombol analisa
if st.button("Analisa"):

    with st.spinner("Mengambil data saham..."):

        raw_df = fetch_stock_data(ticker, "6mo")

        if raw_df is None or raw_df.empty:
            st.error("Data saham tidak ditemukan.")
        else:
            raw_df = calculate_indicators(raw_df)

            if period == "1mo":
                df = raw_df.tail(22)
            elif period == "3mo":
                df = raw_df.tail(66)
            elif period == "6mo":
                df = raw_df.tail(132)
            else:
                df = raw_df

            trend = get_trend(df)

            summary = generate_stock_summary(
                df=df,
                ticker=ticker,
                trend=trend
            )

            st.success("Analisa selesai")

            st.subheader("📌 Ringkasan AI")
            st.write(summary)

            st.subheader("📈 Grafik Harga Saham")
            fig = go.Figure()
            fig.add_trace(
                go.Scatter(
                    x=df["Date"],
                    y=df["Close"],
                    mode="lines",
                    name="Harga Penutupan"
                    )
                )
            fig.add_trace(
                go.Scatter(
                    x=df["Date"],
                    y=df["MA_20"],
                    mode="lines",
                    name="MA 20 Hari"
                    )
                )
            fig.update_layout(
                xaxis_title="Tanggal",
                yaxis_title="Harga (IDR)",
                hovermode="x unified",
                template="plotly_dark"
            )
            st.plotly_chart(fig, use_container_width=True)

            st.subheader("📊 Data Saham")
            st.dataframe(df.tail())

            with st.expander("Lihat semua data"):
                st.dataframe(df)