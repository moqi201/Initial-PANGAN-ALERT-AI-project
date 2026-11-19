
# ==========================================
# PROJECT PANGAN ALERT AI
# TAHAP 2: EXPLORATORY DATA ANALYSIS (EDA)
# ==========================================

import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

# 1. Menentukan lokasi project
BASE_DIR = Path(__file__).resolve().parent

DATA_FILE = BASE_DIR / "data" / "indikator_anomali_pangan_2026.csv"

OUTPUT_DIR = BASE_DIR / "outputs"
OUTPUT_DIR.mkdir(exist_ok=True)

# 2. Membaca dataset
df = pd.read_csv(DATA_FILE)

# 3. Urutan bulan
urutan_bulan = [
    "Januari", "Februari", "Maret",
    "April", "Mei", "Juni",
    "Juli", "Agustus", "September",
    "Oktober", "November", "Desember"
]

df["Bulan"] = pd.Categorical(
    df["Bulan"],
    categories=urutan_bulan,
    ordered=True
)

# ==========================================
# ANALISIS 1: DISTRIBUSI STATUS
# ==========================================

print("\n===== DISTRIBUSI STATUS =====")

status_count = df["Status"].value_counts()

print(status_count)

plt.figure(figsize=(10, 6))

status_count.sort_values().plot(
    kind="barh"
)

plt.title("Distribusi Status Anomali Harga Pangan")
plt.xlabel("Jumlah Data")
plt.ylabel("Status")
plt.tight_layout()

plt.savefig(
    OUTPUT_DIR / "01_distribusi_status.png",
    dpi=150
)

plt.show()


# ==========================================
# ANALISIS 2: RATA-RATA INDEKS BULANAN
# ==========================================

print("\n===== RATA-RATA INDEKS BULANAN =====")

rata_bulanan = df.groupby(
    "Bulan",
    observed=False
)[["QIPA", "AIPA", "IFPA"]].mean()

print(rata_bulanan.round(3))

rata_bulanan.plot(
    figsize=(12, 6),
    marker="o"
)

plt.title("Rata-rata Indeks Anomali per Bulan")
plt.xlabel("Bulan")
plt.ylabel("Nilai Indeks")
plt.xticks(rotation=45)

plt.axhline(
    y=0,
    linestyle="--",
    alpha=0.7
)

plt.tight_layout()

plt.savefig(
    OUTPUT_DIR / "02_rata_rata_indeks.png",
    dpi=150
)

plt.show()


# ==========================================
# ANALISIS 3: POLA KOMODITAS
# ==========================================

print("\n===== ANALISIS POLA KOMODITAS =====")

komoditas_pilihan = [
    "Beras Premium",
    "Cabai Rawit Merah",
    "Gula Pasir Lokal/Curah"
]

data_pilihan = df[
    df["Komoditas"].isin(komoditas_pilihan)
]

pivot_ifpa = data_pilihan.pivot(
    index="Bulan",
    columns="Komoditas",
    values="IFPA"
)

print(pivot_ifpa.round(3))

pivot_ifpa.plot(
    figsize=(12, 6),
    marker="o"
)

plt.title("Perbandingan Pola IFPA Beberapa Komoditas")
plt.xlabel("Bulan")
plt.ylabel("Nilai IFPA")
plt.xticks(rotation=45)

plt.axhline(
    y=0,
    linestyle="--",
    alpha=0.7
)

plt.tight_layout()

plt.savefig(
    OUTPUT_DIR / "03_pola_komoditas.png",
    dpi=150
)

plt.show()


# ==========================================
# SELESAI
# ==========================================

print("\n================================")
print("ANALISIS EDA SELESAI!")
print("Grafik tersimpan di folder outputs")
print("================================")
