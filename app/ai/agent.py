import os

from dotenv import load_dotenv
from google import genai
from google.genai import errors


load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

client = genai.Client(
    api_key=api_key
)


def generate_stock_summary(
    ticker,
    technical_context
):
    """"
    Menghasilkan analisis teknikal saham menggunakan Gemini AI.

    parameters
    ----------
    ticker : str
        Ticker saham yang dianalisis.

    technical_context : str
        Konteks teknikal yang sudah disiapkan oleh technical_analysis.py.

    Returns
    -------
    str
        Hasil analisis teknikal dari Gemini
    """

    prompt = f"""
Anda adalah AI Technical Analyst yang membantu menjelaskan
kondisi teknikal saham berdasarkan data indikator yang diberikan.

Analisis saham:
{ticker}

Gunakan HANYA data teknikal yang tersedia di bawah ini.

==============================
TECHNICAL CONTEXT
==============================

{technical_context}

==============================
INSTRUKSI ANALISIS
==============================

Buat analisis teknikal yang ringkas, jelas, dan mudah dipahami
oleh investor pemula.

Gunakan struktur berikut:

📈 Trend
Jelaskan kondisi trend berdasarkan posisi harga terhadap MA20.

💪 Momentum
Jelaskan kondisi momentum berdasarkan RSI14.
Sebutkan apakah kondisi:
- Overbought
- Oversold
- Neutral

📊 Bollinger Bands
Jelaskan posisi harga terhadap Bollinger Bands.
Jelaskan apakah harga:
- Mendekati upper band
- Mendekati lower band
- Berada di area tengah
- Berada di luar band

📦 Volume
Bandingkan volume saat ini dengan Volume MA20.
Jelaskan apakah volume:
- Mendukung pergerakan harga
- Lemah
- Berada di atas rata-rata
- Berada di bawah rata-rata

🔎 Overall Analysis
Gabungkan seluruh indikator menjadi satu kesimpulan teknikal.
Jelaskan apakah kondisi secara keseluruhan cenderung:
- Bullish
- Bearish
- Netral
- Konsolidasi

Jelaskan juga jika terdapat konflik antar indikator.

⚠️ Risk Note
Sebutkan risiko teknikal yang perlu diperhatikan berdasarkan
indikator yang tersedia.

ATURAN PENTING:

1. Jangan mengarang data atau angka.
2. Jangan menggunakan data yang tidak tersedia dalam context.
3. Jangan memberikan target harga jika tidak tersedia.
4. Jangan menjamin harga akan naik atau turun.
5. Jangan memberikan rekomendasi investasi absolut.
6. Gunakan bahasa Indonesia.
7. Analisis harus berdasarkan data teknikal yang diberikan.
8. Gunakan paragraf singkat agar mudah dibaca.
9. Jangan mengulang angka yang sama terlalu banyak.
10. Fokus pada interpretasi teknikal, bukan berita atau fundamental.

Berikan hasil analisis langsung tanpa menjelaskan proses berpikir Anda.
"""
    
    try:

        response = client.models.generate_content(
            model="gemini-3.5-flash",
            contents=prompt
        )

        return response.text


    except errors.ServerError as e:

        return (
            "⚠️ Gemini AI sedang mengalami gangguan "
            "atau kapasitas server sedang penuh. "
            "Silakan coba lagi beberapa saat kemudian."
        )


    except Exception as e:

        return (
            f"⚠️ Terjadi kesalahan saat menghubungi "
            f"Gemini API: {str(e)}"
        )