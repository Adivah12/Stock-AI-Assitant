import pandas as pd
import os

def save_to_csv(data: pd.DataFrame, ticker: str):
    # Tujuan Folder
    folder_path = os.path.join("data", "raw")

    os.makedirs(folder_path, exist_ok=True)

    name_file = f"{ticker}.csv"

    path_file = os.path.join(folder_path, name_file)

    try:
        data.to_csv(path_file, index=True)
        print(f"Data berhasil disimpan di {path_file}")

    except Exception as e:
        print(f"Terjadi kesalahan saat menyimpan data: {e}")

    return path_file

def save_proceseed_data(data: pd.DataFrame, ticker: str):
    # Tujuan Folder
    folder_path = os.path.join("data", "processed")

    os.makedirs(folder_path, exist_ok=True)

    name_file = f"{ticker}_processed.csv"

    path_file = os.path.join(folder_path, name_file)

    try:
        data.to_csv(path_file, index=True)
        print(f"Data berhasil disimpan di {path_file}")

    except Exception as e:
        print(f"Terjadi kesalahan saat menyimpan data: {e}")

    return path_file