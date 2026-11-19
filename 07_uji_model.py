
# ==========================================
# PANGAN ALERT AI
# TAHAP 7: UJI MODEL TERSIMPAN
# ==========================================

import pandas as pd
import joblib

from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent

MODEL_FILE = (
    BASE_DIR / "models" /
    "pangan_alert_model.joblib"
)

DATA_FILE = (
    BASE_DIR / "data" /
    "indikator_anomali_pangan_2026.csv"
)

# 1. Memuat model
bundle = joblib.load(MODEL_FILE)

model = bundle["model"]
scaler = bundle["scaler"]

features = bundle["features"]
cluster_names = bundle["cluster_names"]

# 2. Membaca satu data contoh dari CSV
df = pd.read_csv(DATA_FILE)

data_contoh = df.loc[0, features]

# 3. Menyiapkan input
input_data = pd.DataFrame(
    [data_contoh],
    columns=features
)

# 4. Standardisasi
input_scaled = scaler.transform(input_data)

# 5. Prediksi cluster
cluster = int(model.predict(input_scaled)[0])

# 6. Menampilkan hasil
nama_cluster = cluster_names[cluster]

print("\n===== HASIL UJI MODEL =====")

print("Input:", data_contoh.to_dict())

print("Cluster ID:", cluster)

print("Karakteristik:", nama_cluster)

print("\nModel berhasil digunakan kembali!")
