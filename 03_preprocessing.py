
# ==========================================
# PANGAN ALERT AI
# TAHAP 3: DATA PREPROCESSING
# ==========================================

import pandas as pd
import numpy as np
import joblib

from pathlib import Path
from sklearn.preprocessing import StandardScaler


# 1. MENENTUKAN LOKASI PROJECT

BASE_DIR = Path(__file__).resolve().parent

DATA_FILE = BASE_DIR / "data" / "indikator_anomali_pangan_2026.csv"

OUTPUT_DIR = BASE_DIR / "outputs"
MODEL_DIR = BASE_DIR / "models"

OUTPUT_DIR.mkdir(exist_ok=True)
MODEL_DIR.mkdir(exist_ok=True)


# 2. MEMBACA DATASET

df = pd.read_csv(DATA_FILE)

print("===== DATASET ASLI =====")
print("Jumlah data:", df.shape)


# 3. MENENTUKAN FITUR ML

fitur = ["QIPA", "AIPA", "IFPA"]

X = df[fitur].copy()

# Pastikan semua fitur bertipe numerik
X = X.apply(pd.to_numeric, errors="coerce")

# Periksa data kosong
if X.isnull().any().any():
    raise ValueError("Terdapat data kosong pada fitur ML!")

print("\n===== FITUR YANG DIGUNAKAN =====")
print(X.head())


# 4. MEMBUAT STANDARD SCALER

scaler = StandardScaler()

X_scaled = scaler.fit_transform(X)


# 5. MENGUBAH HASIL MENJADI DATAFRAME

df_scaled = pd.DataFrame(
    X_scaled,
    columns=[
        "QIPA_scaled",
        "AIPA_scaled",
        "IFPA_scaled"
    ]
)

# Menggabungkan metadata dan hasil scaling
hasil = pd.concat(
    [df.reset_index(drop=True), df_scaled],
    axis=1
)


# 6. MENYIMPAN HASIL PREPROCESSING

hasil.to_csv(
    OUTPUT_DIR / "data_preprocessed.csv",
    index=False
)

# Menyimpan scaler untuk digunakan kembali
joblib.dump(
    scaler,
    MODEL_DIR / "scaler.joblib"
)


# 7. MENAMPILKAN PERBANDINGAN

print("\n===== SEBELUM STANDARDISASI =====")
print(X.describe().round(3))

print("\n===== SESUDAH STANDARDISASI =====")
print(df_scaled.describe().round(3))


# 8. SELESAI

print("\n================================")
print("PREPROCESSING BERHASIL!")
print("Data tersimpan di folder outputs")
print("Scaler tersimpan di folder models")
print("================================")
