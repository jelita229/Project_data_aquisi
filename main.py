
import pandas as pd
from pathlib import Path

lifecycle = pd.DataFrame({
    "Tahap": [
        "Acquisition", "Storage", "Cleaning",
        "Transformation", "Analysis", "Delivery"
    ],
    "Aktivitas Utama": [
        "Mengumpulkan data dari berbagai sumber",
        "Menyimpan dan mengelola data",
        "Membersihkan data kosong dan duplikat",
        "Mengubah format dan struktur data",
        "Menganalisis pola dan informasi dari data",
        "Menyajikan hasil analisis"
    ],
    "Contoh Tools": [
        "Python Requests, BeautifulSoup",
        "MySQL, PostgreSQL",
        "Pandas, OpenRefine",
        "Pandas, Apache Spark",
        "NumPy, Scikit-learn",
        "Matplotlib, Power BI"
    ],
    "Risiko Jika Diabaikan": [
        "Data tidak lengkap atau tidak akurat",
        "Data hilang atau diakses tanpa izin",
        "Hasil analisis tidak akurat",
        "Struktur data salah atau tidak konsisten",
        "Kesimpulan salah atau bias",
        "Informasi sulit dipahami atau menyesatkan"
    ]
})

print(lifecycle.to_string(index=False))

output = Path("docs/lifecycle.csv")
output.parent.mkdir(parents=True, exist_ok=True)
lifecycle.to_csv(output, index=False)

print("File CSV berhasil disimpan:", output)
