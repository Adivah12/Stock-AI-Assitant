import pandas as pd

def preprocess_data(file_path: str) -> pd.DataFrame:
    try:
        df= pd.read_csv(file_path)
        df["Date"]= pd.to_datetime(df["Date"])
        df.set_index("Date", inplace=True)
        df.sort_index(inplace=True)
        df.dropna(inplace=True)
        print("Preprocessing data berhasil dilakukan.")
        print(df.head())
        return df

    except Exception as e:
        print(f"Terjadi kesalahan saat preprocessing data: {e}")
        return pd.DataFrame()  # Return empty DataFrame on error
    