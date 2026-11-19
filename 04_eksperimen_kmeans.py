
# ==========================================
# PANGAN ALERT AI
# TAHAP 4: EKSPERIMEN K-MEANS
# ==========================================

import pandas as pd
import matplotlib.pyplot as plt

from pathlib import Path
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score


# 1. LOKASI PROJECT

BASE_DIR = Path(__file__).resolve().parent

DATA_FILE = BASE_DIR / "outputs" / "data_preprocessed.csv"

OUTPUT_DIR = BASE_DIR / "outputs"


# 2. MEMBACA DATA PREPROCESSING

df = pd.read_csv(DATA_FILE)

fitur = [
    "QIPA_scaled",
    "AIPA_scaled",
    "IFPA_scaled"
]

X = df[fitur]


# 3. MENCOBA JUMLAH CLUSTER

daftar_k = range(2, 7)

inertia_values = []
silhouette_values = []

print("\n===== HASIL EKSPERIMEN K-MEANS =====")

for k in daftar_k:

    model = KMeans(
        n_clusters=k,
        random_state=42,
        n_init=20
    )

    labels = model.fit_predict(X)

    inertia = model.inertia_

    silhouette = silhouette_score(
        X,
        labels
    )

    inertia_values.append(inertia)
    silhouette_values.append(silhouette)

    print(
        f"K = {k} | "
        f"Inertia = {inertia:.3f} | "
        f"Silhouette = {silhouette:.4f}"
    )


# 4. GRAFIK ELBOW METHOD

plt.figure(figsize=(9, 5))

plt.plot(
    list(daftar_k),
    inertia_values,
    marker="o"
)

plt.title("Elbow Method - PANGAN ALERT AI")
plt.xlabel("Jumlah Cluster (K)")
plt.ylabel("Inertia")

plt.xticks(list(daftar_k))
plt.grid(alpha=0.3)
plt.tight_layout()

plt.savefig(
    OUTPUT_DIR / "04_elbow_method.png",
    dpi=150
)

plt.show()


# 5. GRAFIK SILHOUETTE SCORE

plt.figure(figsize=(9, 5))

plt.plot(
    list(daftar_k),
    silhouette_values,
    marker="o"
)

plt.title("Silhouette Score - PANGAN ALERT AI")
plt.xlabel("Jumlah Cluster (K)")
plt.ylabel("Silhouette Score")

plt.xticks(list(daftar_k))
plt.grid(alpha=0.3)
plt.tight_layout()

plt.savefig(
    OUTPUT_DIR / "05_silhouette_score.png",
    dpi=150
)

plt.show()


print("\nEksperimen selesai!")

