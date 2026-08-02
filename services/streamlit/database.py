"""
Database Access Layer for UMKM Donat Kentang Syifa (DKS) DSS Application.
Supports PostgreSQL (with fallback to SQLite for local development).
Implements SQLAlchemy engine management, record insertion, dynamic CTE analytics, and sample data seeding.
"""

import logging
import hashlib
import pandas as pd
import numpy as np
from datetime import date, timedelta
from sqlalchemy import create_engine, text, Table, Column, Integer, String, Date, DateTime, func, MetaData
from sqlalchemy.exc import OperationalError
from config import DATABASE_URL, SQLITE_FALLBACK_URL

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def get_db_engine():
    """
    Creates and tests connection to PostgreSQL database.
    Falls back gracefully to SQLite if PostgreSQL connection fails.
    """
    try:
        engine = create_engine(DATABASE_URL, pool_pre_ping=True, connect_args={"connect_timeout": 3})
        # Test connection
        with engine.connect() as conn:
            conn.execute(text("SELECT 1"))
        logger.info("Successfully connected to PostgreSQL database.")
        return engine, "PostgreSQL"
    except Exception as e:
        logger.warning(f"PostgreSQL connection failed: {e}. Falling back to SQLite database.")
        fallback_engine = create_engine(SQLITE_FALLBACK_URL, pool_pre_ping=True)
        return fallback_engine, "SQLite (Fallback)"


# Initialize engine instance and store active database backend type
engine, DB_BACKEND = get_db_engine()
metadata = MetaData()

# Table Definitions
production_table = Table(
    'production_data', metadata,
    Column('id', Integer, primary_key=True, autoincrement=True),
    Column('tanggal', Date, nullable=False, unique=True),
    Column('permintaan', Integer, nullable=False),
    Column('persediaan', Integer, nullable=False),
    Column('produksi_aktual', Integer, nullable=True),
    Column('prediksi_fis', Integer, nullable=False),
    Column('created_at', DateTime, server_default=func.now())
)

users_table = Table(
    'users', metadata,
    Column('id', Integer, primary_key=True, autoincrement=True),
    Column('username', String(50), nullable=False, unique=True),
    Column('password_hash', String(255), nullable=False),
    Column('fullname', String(100), nullable=True),
    Column('role', String(20), server_default='admin'),
    Column('created_at', DateTime, server_default=func.now())
)


def hash_password(password: str) -> str:
    """
    Hashes a plain password using PBKDF2-HMAC-SHA256 with a static salt.
    """
    return hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), b'dks_salt_2026', 100000).hex()


def authenticate_user(username: str, password: str):
    """
    Validates username and password against users table.
    Returns user record dict if valid, None if invalid.
    """
    pwd_hash = hash_password(password)
    try:
        with engine.connect() as conn:
            query = text("SELECT id, username, role, fullname FROM users WHERE username = :u AND password_hash = :p")
            result = conn.execute(query, {"u": username.strip(), "p": pwd_hash}).fetchone()
            if result:
                return {"id": result[0], "username": result[1], "role": result[2], "fullname": result[3] if len(result) > 3 else result[1]}
    except Exception as e:
        logger.error(f"Authentication error: {e}")
    return None


def seed_default_user():
    """
    Seeds default admin user (username: admin, password: dks2026) if users table is empty.
    """
    try:
        with engine.connect() as conn:
            result = conn.execute(text("SELECT COUNT(*) FROM users")).scalar()
            if result == 0:
                admin_hash = hash_password("dks2026")
                conn.execute(
                    text("INSERT INTO users (username, password_hash, role, fullname) VALUES (:u, :p, :r, :f)"),
                    {"u": "admin", "p": admin_hash, "r": "admin", "f": "Administrator"}
                )
                conn.commit()
                logger.info("Default admin user created (admin / dks2026).")
    except Exception as e:
        logger.error(f"Error seeding default user: {e}")


def init_db():
    """
    Creates tables and seeds initial historical data if table is empty.
    """
    try:
        metadata.create_all(engine)
        logger.info("Database tables initialized successfully.")
        
        # Seed default admin user
        seed_default_user()

        # Check if table has records, seed if empty
        with engine.connect() as conn:
            result = conn.execute(text("SELECT COUNT(*) FROM production_data"))
            count = result.scalar()
            if count == 0:
                logger.info("No records found in database. Seeding initial historical data...")
                seed_sample_data()
    except Exception as e:
        logger.error(f"Error initializing database: {e}")
        raise e


def seed_sample_data():
    """
    Seeds 30 days of realistic historical donut production data for DKS.
    Includes Permintaan, Persediaan, Produksi Aktual, and Prediksi FIS.
    """
    from fuzzy_logic import FIS_Mamdani_DKS
    fis = FIS_Mamdani_DKS()
    
    start_date = date.today() - timedelta(days=30)
    np.random.seed(42)  # Deterministic seed for reproducible evaluation

    records = []
    
    # Nilai awal seed
    curr_permintaan = 8000
    curr_persediaan = 150
    
    for i in range(30):
        current_date = start_date + timedelta(days=i)
        
        # Random Walk halus (< 1000 per hari)
        curr_permintaan += int(np.random.uniform(-800, 800))
        permintaan = max(6273, min(10224, curr_permintaan))
        curr_permintaan = permintaan # Update state
        
        curr_persediaan += int(np.random.uniform(-50, 50))
        persediaan = max(9, min(450, curr_persediaan))
        curr_persediaan = persediaan # Update state
        
        # Calculate FIS prediction
        fis_res = fis.compute(permintaan, persediaan)
        prediksi_fis = fis_res["produksi_prediksi"]
        
        # Add realistic actual production (with slight historical variance)
        actual_variance = int(np.random.normal(loc=0, scale=45))
        produksi_aktual = max(100, prediksi_fis + actual_variance)

        records.append({
            "tanggal": current_date,
            "permintaan": permintaan,
            "persediaan": persediaan,
            "produksi_aktual": produksi_aktual,
            "prediksi_fis": prediksi_fis
        })

    with engine.connect() as conn:
        for r in records:
            stmt = text("""
                INSERT INTO production_data (tanggal, permintaan, persediaan, produksi_aktual, prediksi_fis)
                VALUES (:tanggal, :permintaan, :persediaan, :produksi_aktual, :prediksi_fis)
                ON CONFLICT (tanggal) DO UPDATE SET
                    permintaan = EXCLUDED.permintaan,
                    persediaan = EXCLUDED.persediaan,
                    produksi_aktual = EXCLUDED.produksi_aktual,
                    prediksi_fis = EXCLUDED.prediksi_fis
            """)
            conn.execute(stmt, r)
        conn.commit()
    logger.info("Successfully seeded 30 sample production records.")


def save_production_record(tanggal, permintaan, persediaan, prediksi_fis, produksi_aktual=None):
    """
    Inserts or updates a daily production entry.
    """
    with engine.connect() as conn:
        if DB_BACKEND == "PostgreSQL":
            stmt = text("""
                INSERT INTO production_data (tanggal, permintaan, persediaan, prediksi_fis, produksi_aktual)
                VALUES (:tanggal, :permintaan, :persediaan, :prediksi_fis, :produksi_aktual)
                ON CONFLICT (tanggal) DO UPDATE SET
                    permintaan = EXCLUDED.permintaan,
                    persediaan = EXCLUDED.persediaan,
                    prediksi_fis = EXCLUDED.prediksi_fis,
                    produksi_aktual = COALESCE(EXCLUDED.produksi_aktual, production_data.produksi_aktual)
            """)
        else:
            # SQLite fallback syntax
            stmt = text("""
                INSERT INTO production_data (tanggal, permintaan, persediaan, prediksi_fis, produksi_aktual)
                VALUES (:tanggal, :permintaan, :persediaan, :prediksi_fis, :produksi_aktual)
                ON CONFLICT(tanggal) DO UPDATE SET
                    permintaan = excluded.permintaan,
                    persediaan = excluded.persediaan,
                    prediksi_fis = excluded.prediksi_fis,
                    produksi_aktual = COALESCE(excluded.produksi_aktual, production_data.produksi_aktual)
            """)
        
        conn.execute(stmt, {
            "tanggal": tanggal,
            "permintaan": int(permintaan),
            "persediaan": int(persediaan),
            "prediksi_fis": int(prediksi_fis),
            "produksi_aktual": int(produksi_aktual) if produksi_aktual is not None else None
        })
        conn.commit()


def get_all_production_records():
    """
    Retrieves all production records sorted by date descending.
    Returns pandas DataFrame.
    """
    query = "SELECT id, tanggal, permintaan, persediaan, produksi_aktual, prediksi_fis, created_at FROM production_data ORDER BY tanggal DESC"
    try:
        df = pd.read_sql_query(query, engine)
        if not df.empty and 'tanggal' in df.columns:
            df['tanggal'] = pd.to_datetime(df['tanggal']).dt.date
        return df
    except Exception as e:
        logger.error(f"Error querying production records: {e}")
        return pd.DataFrame()


def get_mape_analytics():
    """
    Computes MAPE (Mean Absolute Percentage Error) and MAE using SQL CTE (Common Table Expression).
    """
    cte_query = text("""
        WITH ape_calc AS (
            SELECT 
                tanggal,
                produksi_aktual,
                prediksi_fis,
                ABS(produksi_aktual - prediksi_fis) AS abs_error,
                (ABS(produksi_aktual - prediksi_fis) * 100.0 / NULLIF(produksi_aktual, 0)) AS ape
            FROM production_data
            WHERE produksi_aktual IS NOT NULL AND produksi_aktual > 0
        )
        SELECT 
            COUNT(*) AS total_eval_records,
            AVG(ape) AS mape,
            AVG(abs_error) AS mae,
            MIN(ape) AS min_ape,
            MAX(ape) AS max_ape
        FROM ape_calc
    """)

    try:
        with engine.connect() as conn:
            result = conn.execute(cte_query).fetchone()
            if result and result[0] > 0:
                return {
                    "total_records": result[0],
                    "mape": round(float(result[1]), 2) if result[1] is not None else 0.0,
                    "mae": round(float(result[2]), 2) if result[2] is not None else 0.0,
                    "min_ape": round(float(result[3]), 2) if result[3] is not None else 0.0,
                    "max_ape": round(float(result[4]), 2) if result[4] is not None else 0.0
                }
    except Exception as e:
        logger.error(f"Error calculating MAPE analytics CTE: {e}")

    return {
        "total_records": 0,
        "mape": 0.0,
        "mae": 0.0,
        "min_ape": 0.0,
        "max_ape": 0.0
    }
