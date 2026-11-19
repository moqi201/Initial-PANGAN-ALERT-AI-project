
# ==========================================
# PANGAN ALERT AI
# TAHAP 6: MODEL K-MEANS FINAL
# ==========================================

import pandas as pd
import joblib

from pathlib import Path
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans


# 1. MENENTUKAN LOKASI PROJECT

BASE_DIR = Path(__file__).resolve().parent

DATA_FILE = (
    BASE_DIR / "data" /
    "indikator_anomali_pangan_2026.csv"
)

MODEL_DIR = BASE_DIR / "models"
OUTPUT_DIR = BASE_DIR / "outputs"

MODEL_DIR.mkdir(exist_ok=True)
OUTPUT_DIR.mkdir(exist_ok=True)


# 2. MEMBACA DATASET

df = pd.read_csv(DATA_FILE)

features = ["QIPA", "AIPA", "IFPA"]

X = df[features].copy()

print("Jumlah data:", len(df))


# 3. STANDARDISASI DATA

scaler = StandardScaler()

X_scaled = scaler.fit_transform(X)


# 4. TRAINING K-MEANS

K = 3

model = KMeans(
    n_clusters=K,
    random_state=42,
    n_init=20
)

labels = model.fit_predict(X_scaled)


# 5. MENENTUKAN KARAKTERISTIK CLUSTER

# Rata-rata centroid dalam skala standardisasi
center_scores = model.cluster_centers_.mean(axis=1)

# Urutkan centroid dari nilai terendah ke tertinggi
ordered_clusters = center_scores.argsort()

cluster_names = {
    ordered_clusters[0]: "Pola Indeks Relatif Rendah",
    ordered_clusters[1]: "Pola Indeks Menengah",
    ordered_clusters[2]: "Pola Indeks Relatif Tinggi"
}


# 6. MENAMBAHKAN HASIL CLUSTER

hasil = df.copy()

hasil["Cluster_ID"] = labels

hasil["Pola_Cluster"] = [
    cluster_names[label] for label in labels
]


# 7. MEMBUAT PROFIL CLUSTER

profil = hasil.groupby(
    ["Cluster_ID", "Pola_Cluster"]
).agg(
    jumlah_data=("Komoditas", "count"),
    rata_QIPA=("QIPA", "mean"),
    rata_AIPA=("AIPA", "mean"),
    rata_IFPA=("IFPA", "mean")
).reset_index()

print("\n===== PROFIL CLUSTER =====")

print(profil.round(3).to_string(index=False))


# 8. MEMBANDINGKAN STATUS RESMI

print("\n===== PERBANDINGAN STATUS BAPANAS =====")

perbandingan = pd.crosstab(
    hasil["Pola_Cluster"],
    hasil["Status"]
)

print(perbandingan)


# 9. MENYIMPAN HASIL CSV

hasil.to_csv(
    OUTPUT_DIR / "hasil_cluster_final.csv",
    index=False
)

profil.to_csv(
    OUTPUT_DIR / "profil_cluster.csv",
    index=False
)

perbandingan.to_csv(
    OUTPUT_DIR / "perbandingan_status_final.csv"
)


# 10. MENYIMPAN MODEL DAN SCALER

model_bundle = {
    "model": model,
    "scaler": scaler,
    "features": features,
    "n_clusters": K,
    "cluster_names": cluster_names
}

joblib.dump(
    model_bundle,
    MODEL_DIR / "pangan_alert_model.joblib"
)


# 11. SELESAI

print("\n===================================")
print("MODEL PANGAN ALERT AI BERHASIL!")
print("Jumlah Cluster:", K)
print("Model tersimpan di:", MODEL_DIR)
print("===================================")
