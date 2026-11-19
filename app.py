
# ==========================================
# PANGAN ALERT AI
# FLASK BACKEND - USER FRIENDLY VERSION
# ==========================================

from flask import Flask, render_template, request
from pathlib import Path

import pandas as pd
import joblib


# 1. KONFIGURASI

app = Flask(
    __name__,
    static_folder="public",
    static_url_path=""
)

BASE_DIR = Path(__file__).resolve().parent

DATA_FILE = BASE_DIR / "data" / "indikator_anomali_pangan_2026.csv"
MODEL_FILE = BASE_DIR / "models" / "pangan_alert_model.joblib"

FEATURES = ["QIPA", "AIPA", "IFPA"]

MONTH_ORDER = {
    "Januari": 1,
    "Februari": 2,
    "Maret": 3,
    "April": 4,
    "Mei": 5,
    "Juni": 6,
    "Juli": 7,
    "Agustus": 8,
    "September": 9,
    "Oktober": 10,
    "November": 11,
    "Desember": 12
}


# 2. MEMERIKSA FILE

if not DATA_FILE.exists():
    raise FileNotFoundError("Dataset tidak ditemukan!")

if not MODEL_FILE.exists():
    raise FileNotFoundError("Model ML tidak ditemukan!")


# 3. MEMBACA DATASET

df = pd.read_csv(DATA_FILE)

required_columns = [
    "Tahun",
    "Bulan",
    "Komoditas",
    "QIPA",
    "AIPA",
    "IFPA",
    "Status"
]

missing_columns = [
    column for column in required_columns
    if column not in df.columns
]

if missing_columns:
    raise ValueError(
        f"Kolom dataset tidak lengkap: {missing_columns}"
    )

df["Tahun"] = pd.to_numeric(
    df["Tahun"], errors="raise"
).astype(int)

df[FEATURES] = df[FEATURES].apply(
    pd.to_numeric, errors="raise"
)

if df[FEATURES].isnull().any().any():
    raise ValueError("Terdapat nilai indeks kosong!")


# 4. MEMUAT MODEL MACHINE LEARNING

bundle = joblib.load(MODEL_FILE)

model = bundle["model"]
scaler = bundle["scaler"]

features = bundle["features"]

cluster_names = {
    int(key): value
    for key, value in bundle["cluster_names"].items()
}

centers_original = scaler.inverse_transform(
    model.cluster_centers_
)


# 5. MENJALANKAN CLUSTERING DATA DASHBOARD

X_scaled = scaler.transform(df[FEATURES])

df["Cluster_ID"] = model.predict(X_scaled)

df["Pola_Cluster"] = df["Cluster_ID"].map(
    cluster_names
)


# 6. MENYIAPKAN DAFTAR KOMODITAS

commodities = df["Komoditas"].drop_duplicates().tolist()


# 7. MENYIAPKAN PILIHAN PERIODE

period_df = df[["Tahun", "Bulan"]].drop_duplicates().copy()

period_df["_urutan_bulan"] = (
    period_df["Bulan"].map(MONTH_ORDER)
)

period_df = period_df.sort_values(
    ["Tahun", "_urutan_bulan"]
)

period_options = []

for row in period_df.itertuples(index=False):

    period_options.append({
        "value": f"{int(row.Tahun)}|{row.Bulan}",
        "label": f"{row.Bulan} {int(row.Tahun)}"
    })

latest_period_value = period_options[-1]["value"]
latest_period = period_options[-1]["label"]


# 8. PENJELASAN STATUS RESMI BAPANAS

status_explanations = {

    "Normal":
        "Dataset Bapanas mencatat status Normal untuk pengamatan ini.",

    "Warning (Low Price)":
        "Dataset Bapanas mencatat label peringatan pada kategori harga rendah.",

    "Alert (Low Price)":
        "Dataset Bapanas mencatat label Alert pada kategori harga rendah.",

    "Warning (High Price)":
        "Dataset Bapanas mencatat label peringatan pada kategori harga tinggi.",

    "Alert (High Price)":
        "Dataset Bapanas mencatat label Alert pada kategori harga tinggi."

}


# 9. GRAFIK BULANAN

monthly = df.groupby(
    ["Tahun", "Bulan"],
    as_index=False
)[FEATURES].mean()

monthly["_urutan_bulan"] = monthly["Bulan"].map(
    MONTH_ORDER
)

monthly = monthly.sort_values(
    ["Tahun", "_urutan_bulan"]
)

monthly_labels = [
    f"{row.Bulan[:3]} {int(row.Tahun)}"
    for row in monthly.itertuples()
]


# 10. DISTRIBUSI STATUS

status_counts = df["Status"].value_counts()

status_labels = status_counts.index.astype(str).tolist()

status_values = [
    int(value) for value in status_counts.values
]


# 11. PROFIL CLUSTER

cluster_summary = []

for cluster_id in sorted(cluster_names):

    center = centers_original[cluster_id]

    jumlah = int(
        (df["Cluster_ID"] == cluster_id).sum()
    )

    cluster_summary.append({

        "id": cluster_id,

        "name": cluster_names[cluster_id],

        "count": jumlah,

        "qipa": float(center[0]),

        "aipa": float(center[1]),

        "ifpa": float(center[2])

    })


# 12. DATA DASHBOARD UNTUK CHART.JS

dashboard_data = {

    "monthly_labels": monthly_labels,

    "monthly_values": {
        feature: monthly[feature].astype(float).tolist()
        for feature in FEATURES
    },

    "status_labels": status_labels,

    "status_values": status_values

}


# 13. HALAMAN UTAMA

@app.route("/", methods=["GET", "POST"])
def index():

    result = None
    error = None

    default_commodity = (
        "Beras Premium"
        if "Beras Premium" in commodities
        else commodities[0]
    )

    selected_commodity = request.form.get(
        "commodity",
        default_commodity
    )

    selected_period = request.form.get(
        "period",
        latest_period_value
    )

    # ======================================
    # ANALISIS KETIKA TOMBOL DITEKAN
    # ======================================

    if request.method == "POST":

        try:

            # Periksa komoditas
            if selected_commodity not in commodities:

                raise ValueError(
                    "Komoditas yang dipilih tidak tersedia."
                )


            # Periksa periode
            valid_periods = {
                item["value"] for item in period_options
            }

            if selected_period not in valid_periods:

                raise ValueError(
                    "Periode yang dipilih tidak tersedia."
                )


            # Memisahkan tahun dan bulan
            year_text, selected_month = selected_period.split("|", 1)

            selected_year = int(year_text)


            # Mengambil data asli dari CSV
            selected_data = df[
                (df["Komoditas"] == selected_commodity)
                &
                (df["Tahun"] == selected_year)
                &
                (df["Bulan"] == selected_month)
            ]


            if selected_data.empty:

                raise ValueError(
                    "Data komoditas untuk periode tersebut tidak ditemukan."
                )


            # Mengambil satu baris data
            row = selected_data.iloc[0]


            # Menyiapkan fitur untuk ML
            input_data = pd.DataFrame(
                [[float(row[feature]) for feature in FEATURES]],
                columns=FEATURES
            )


            # Standardisasi
            input_scaled = scaler.transform(input_data)


            # Prediksi cluster
            cluster_id = int(
                model.predict(input_scaled)[0]
            )


            # Nama kelompok
            cluster_name = cluster_names[cluster_id]


            # Status resmi
            official_status = str(row["Status"])

            status_note = status_explanations.get(
                official_status,
                "Status mengikuti informasi yang tercantum dalam dataset."
            )


            # Hasil analisis
            result = {

                "commodity": selected_commodity,

                "period": f"{selected_month} {selected_year}",

                "cluster_id": cluster_id,

                "cluster_name": cluster_name,

                "status": official_status,

                "status_note": status_note,

                "qipa": float(row["QIPA"]),

                "aipa": float(row["AIPA"]),

                "ifpa": float(row["IFPA"]),

                "explanation": (
                    "Berdasarkan nilai indeks yang tersedia, "
                    "model menemukan bahwa data ini paling mirip "
                    "dengan kelompok tersebut dibandingkan "
                    "kelompok lainnya dalam data pelatihan."
                )

            }


        except ValueError as e:

            error = str(e)

        except Exception as e:

            print("ERROR ANALISIS:", e)

            error = (
                "Analisis belum berhasil. "
                "Silakan periksa kembali data dan model."
            )


    # 14. MENGURUTKAN DATA TABEL

    display_df = df.copy()

    display_df["_urutan_bulan"] = (
        display_df["Bulan"].map(MONTH_ORDER)
    )

    display_df = display_df.sort_values(
        ["Tahun", "_urutan_bulan"]
    )

    table_data = display_df.to_dict(
        orient="records"
    )


    # 15. MENGIRIM DATA KE HTML

    return render_template(

        "index.html",

        total_data=len(df),

        total_komoditas=df["Komoditas"].nunique(),

        total_cluster=len(cluster_names),

        latest_period=latest_period,

        commodities=commodities,

        period_options=period_options,

        selected_commodity=selected_commodity,

        selected_period=selected_period,

        cluster_summary=cluster_summary,

        dashboard_data=dashboard_data,

        table_data=table_data,

        result=result,

        error=error

    )


# 16. MENJALANKAN SERVER

if __name__ == "__main__":

    print("====================================")

    print("PANGAN ALERT AI")

    print("====================================")

    print("Total data:", len(df))

    print("Total komoditas:", len(commodities))

    print("Total cluster:", len(cluster_names))

    print("Website: http://127.0.0.1:5000")

    print("====================================")

    app.run(
        host="127.0.0.1",
        port=5000,
        debug=True
    )
