"""
Configuration module for UMKM Donat Kentang Syifa (DKS) DSS Application.
Contains database settings, default fuzzy logic domains, membership function parameters,
and Mamdani rule definitions.
"""

import os
from pathlib import Path
from dotenv import load_dotenv

# Load environment variables if .env exists
load_dotenv()

# Database Configuration
DB_HOST = os.getenv("POSTGRES_HOST", "localhost")
DB_PORT = os.getenv("POSTGRES_PORT", "5432")
DB_NAME = os.getenv("POSTGRES_DB", "dks_fuzzy_db")
DB_USER = os.getenv("POSTGRES_USER", "dks_user")
DB_PASSWORD = os.getenv("POSTGRES_PASSWORD", "dks_password_2026")

DATABASE_URL = os.getenv(
    "DATABASE_URL",
    f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
)

# SQLite fallback URL for local testing without PostgreSQL container
BASE_DIR = Path(__file__).resolve().parent
SQLITE_FALLBACK_URL = f"sqlite:///{BASE_DIR / 'dks_fuzzy_local.db'}"

# Fuzzy Variable Domains (Min, Max) in donut units
DOMAIN_PERMINTAAN = (6270, 10220)
DOMAIN_PERSEDIAAN = (10, 450)
DOMAIN_PRODUKSI = (6270, 10390)

# Default Membership Function Parameters
# Trapezoidal: [a, b, c, d], Triangular: [a, b, c]
FUZZY_PARAMS = {
    "permintaan": {
        "Rendah": {"type": "tri", "params": [6270, 6270, 7400]},
        "Sedang": {"type": "tri", "params": [7000, 8100, 9200]},
        "Tinggi": {"type": "tri", "params": [8700, 10220, 10220]},
    },
    "persediaan": {
        "Rendah": {"type": "tri", "params": [10, 10, 150]},
        "Sedang": {"type": "tri", "params": [100, 220, 350]},
        "Tinggi": {"type": "tri", "params": [300, 450, 450]},
    },
    "produksi": {
        "Sedikit": {"type": "tri", "params": [6270, 6270, 7400]},
        "Sedang": {"type": "tri", "params": [7000, 8200, 9400]},
        "Banyak": {"type": "tri", "params": [8800, 10390, 10390]},
    }
}

# Fuzzy Mamdani Rules (9 combinations for 3x3 input sets)
# Rule structure: (Permintaan, Persediaan) -> Produksi
MAMDANI_RULES = [
    # IF Permintaan Rendah
    {"permintaan": "Rendah", "persediaan": "Rendah", "produksi": "Sedang"},
    {"permintaan": "Rendah", "persediaan": "Sedang", "produksi": "Sedikit"},
    {"permintaan": "Rendah", "persediaan": "Tinggi", "produksi": "Sedikit"},
    
    # IF Permintaan Sedang
    {"permintaan": "Sedang", "persediaan": "Rendah", "produksi": "Sedang"},
    {"permintaan": "Sedang", "persediaan": "Sedang", "produksi": "Sedang"},
    {"permintaan": "Sedang", "persediaan": "Tinggi", "produksi": "Sedikit"},
    
    # IF Permintaan Tinggi
    {"permintaan": "Tinggi", "persediaan": "Rendah", "produksi": "Banyak"},
    {"permintaan": "Tinggi", "persediaan": "Sedang", "produksi": "Banyak"},
    {"permintaan": "Tinggi", "persediaan": "Tinggi", "produksi": "Sedang"},
]
