# ==================================
# PROJECT PANGAN ALERT AI
# TAHAP 1: MENGENAL DATASET
# ==================================

# 1. Import library
import pandas as pd
from pathlib import Path

# 2. Menentukan lokasi dataset
BASE_DIR = Path(__file__).resolve().parent

file_dataset = (
    BASE_DIR / "data" / "indikator_anomali_pangan_2026.csv"
)

# 3. Membaca dataset
df = pd.read_csv(file_dataset)

# 4. Menampilkan lima data pertama
print("\n===== 5 DATA PERTAMA =====")
print(df.head())

# 5. Melihat ukuran dataset
print("\n===== UKURAN DATASET =====")
print("Baris dan Kolom:", df.shape)

# 6. Melihat informasi dataset
print("\n===== INFORMASI DATASET =====")
df.info()

# 7. Mengecek data kosong
print("\n===== DATA KOSONG =====")
print(df.isnull().sum())

# 8. Mengecek duplikat
print("\n===== DATA DUPLIKAT =====")
print(df.duplicated().sum())

# 9. Melihat komoditas
print("\n===== DAFTAR KOMODITAS =====")
print(df["Komoditas"].unique())

# 10. Melihat distribusi status
print("\n===== DISTRIBUSI STATUS =====")
print(df["Status"].value_counts())