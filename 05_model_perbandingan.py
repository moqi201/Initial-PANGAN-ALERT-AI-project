
# ==========================================
# PANGAN ALERT AI
# TAHAP 5: PEMBANDINGAN MODEL K-MEANS
# ==========================================

import pandas as pd
import joblib

from pathlib import Path
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score


# 1. MENENTUKAN LOKASI PROJECT

BASE_DIR = Path(__file__).resolve().parent

DATA_FILE = BASE_DIR / "data" / "indikator_anomali_pangan_2026.csv"

PREPROCESS_FILE = BASE_DIR / "outputs" / "data_preprocessed.csv"

MODEL_DIR = BASE_DIR / "models"
OUTPUT_DIR = BASE_DIR / "outputs"

MODEL_DIR.mkdir(exist_ok=True)
OUTPUT_DIR.mkdir(exist_ok=True)


# 2. MEMBACA DATA

df = pd.read_csv(DATA_FILE)
df_scaled = pd.read_csv(PREPROCESS_FILE)

# Fitur asli
features = ["QIPA", "AIPA", "IFPA"]

# Fitur hasil standardisasi
scaled_features = [
    "QIPA_scaled",
    "AIPA_scaled",
    "IFPA_scaled"
]

# Mengambil data untuk ML
X = df_scaled[scaled_features]

# Memuat scaler sebelumnya
scaler = joblib.load(
    MODEL_DIR / "scaler.joblib"
)


# 3. MEMBANDINGKAN K=2 DAN K=3

for k in [2, 3]:

    print("\n" + "=" * 40)
    print(f"PEMBUATAN MODEL K-MEANS K={k}")
    print("=" * 40)

    # Membuat model
    model = KMeans(
        n_clusters=k,
        random_state=42,
        n_init=20
    )

    # Training dan clustering
    labels = model.fit_predict(X)

    # Menghitung Silhouette Score
    score = silhouette_score(X, labels)

    print("Jumlah Cluster:", k)
    print("Silhouette Score:", round(score, 4))


    # 4. MENAMBAHKAN HASIL CLUSTER

    hasil = df.copy()

    hasil["Cluster"] = labels

    # Simpan hasil clustering
    hasil.to_csv(
        OUTPUT_DIR / f"hasil_cluster_k{k}.csv",
        index=False
    )


    # 5. MELIHAT JUMLAH DATA PER CLUSTER

    print("\nDistribusi Cluster:")

    print(
        hasil["Cluster"].value_counts().sort_index()
    )


    # 6. MEMBANDINGKAN DENGAN STATUS RESMI

    print("\nPerbandingan dengan Status Bapanas:")

    perbandingan = pd.crosstab(
        hasil["Cluster"],
        hasil["Status"]
    )

    print(perbandingan)

    perbandingan.to_csv(
        OUTPUT_DIR / f"perbandingan_status_k{k}.csv"
    )


    # 7. MELIHAT TITIK PUSAT CLUSTER

    centroid_asli = scaler.inverse_transform(
        model.cluster_centers_
    )

    centroid_df = pd.DataFrame(
        centroid_asli,
        columns=features
    )

    centroid_df.index.name = "Cluster"

    print("\nRata-rata Indeks Pusat Cluster:")

    print(centroid_df.round(3))

    centroid_df.to_csv(
        OUTPUT_DIR / f"centroid_k{k}.csv"
    )


    # 8. MENYIMPAN MODEL

    model_bundle = {
        "model": model,
        "scaler": scaler,
        "features": features,
        "n_clusters": k
    }

    joblib.dump(
        model_bundle,
        MODEL_DIR / f"kmeans_k{k}.joblib"
    )

    print(f"\nModel K={k} berhasil disimpan!")


print("\n====================================")
print("PERBANDINGAN MODEL SELESAI!")
print("Periksa folder models dan outputs.")
print("====================================")

