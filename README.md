# 🍩 Decision Support System (DSS) Donat Kentang Syifa (DKS)

Production-ready Web Application Decision Support System (DSS) using **Streamlit**, **Fuzzy Inference System (FIS) Mamdani**, **PostgreSQL**, **Docker**, and **Vue 3** for **UMKM Donat Kentang Syifa (DKS)** to determine daily optimal donut production volumes.

---

## 📌 Project Overview
- **Goal:** A highly interactive, real-time web application for daily operational use to optimize donut production using AI-based fuzzy logic.
- **Core Algorithm:** Fuzzy Inference System (FIS) Mamdani.
- **Input Variables:** 
  1. `Permintaan` (Demand - units of donuts)
  2. `Persediaan` (Stock/Supply - units of donuts)
- **Output Variable:** 
  1. `Produksi` (Recommended production volume - units of donuts)
- **Defuzzification:** Centroid Method (Center of Gravity).

---

## ✨ Key Features & UI Enhancements
The Streamlit dashboard has been heavily customized to provide a premium, modern user experience:
- **Glassmorphism Login Page:** A custom login interface featuring glassmorphism effects, floating donut animations, and an aesthetic amber color palette.
- **Theme-Locked Login Security:** The login page is strictly locked to **Light Mode** using advanced structural CSS injections, ensuring inputs and SVG icons (like the password toggle) render flawlessly regardless of the dashboard's active theme.
- **Dynamic Cross-Theme Sync:** Uses intelligent JavaScript polling to continuously sync the background color of the top Navigation Header (`stHeader`) with the Sidebar (`stSidebar`), maintaining visual consistency across Light and Dark Mode toggles.
- **State Persistence Memory:** The application intelligently remembers your Daily Operational Inputs and History Dashboard filters (Year/Month) across page navigations without requiring form submissions, providing a seamless multi-page experience.
- **Smooth Random Walk Data Generation:** Integrated a realistic data simulator that uses a bounded Random Walk algorithm to generate smooth historical production data (daily fluctuations < 1000 units), perfect for trend analysis.
- **Targeted CSS Injection:** Employs advanced modern CSS (such as `:has()` and adjacent sibling selectors) to style specific Streamlit widgets (like the Amber *Hitung* button) without bleeding styles to other components.

---

## 📁 Directory Structure
```
fuzzy-decision-maker/
├── .gitignore               # Git ignore rules for virtualenv, node_modules, cache & db
├── docker-compose.yml       # Multi-container orchestration (Vue 3, Streamlit, PostgreSQL, Nginx)
├── README.md                # Complete documentation
├── frontend/                # Vue 3 Landing Page service
│   ├── Dockerfile
│   ├── index.html
│   ├── package.json
│   └── src/
├── infra/                  # Infrastructure configurations
│   └── nginx.conf           # Nginx reverse proxy configuration
├── services/               # Backend application services
│   └── streamlit/           # Streamlit DSS Application
│       ├── app.py           # Main Streamlit web app UI & Dashboard
│       ├── config.py        # Configs, env variables & Mamdani rules
│       ├── database.py      # PostgreSQL / SQLite database access layer
│       ├── Dockerfile       # Container definition for Streamlit
│       ├── fuzzy_logic.py   # FIS Mamdani engine & Plotly visualizations
│       └── requirements.txt # Python package dependencies
└── shared/                 # Shared database schemas & assets
    └── sql/
        └── init.sql         # SQL schema initialization, indexes & seed data
```

---

## ⚙️ Logic & Fuzzy Rules
- **Membership Sets:**
  - **Permintaan:** Rendah, Sedang, Tinggi
  - **Persediaan:** Sedikit, Sedang, Banyak
  - **Produksi:** Berkurang, Tetap, Bertambah
- **Rule Base (9 Mamdani Rules):**
  1. IF Permintaan Rendah AND Persediaan Sedikit THEN Produksi Berkurang
  2. IF Permintaan Rendah AND Persediaan Sedang THEN Produksi Berkurang
  3. IF Permintaan Rendah AND Persediaan Banyak THEN Produksi Berkurang
  4. IF Permintaan Sedang AND Persediaan Sedikit THEN Produksi Tetap
  5. IF Permintaan Sedang AND Persediaan Sedang THEN Produksi Tetap
  6. IF Permintaan Sedang AND Persediaan Banyak THEN Produksi Berkurang
  7. IF Permintaan Tinggi AND Persediaan Sedikit THEN Produksi Bertambah
  8. IF Permintaan Tinggi AND Persediaan Sedang THEN Produksi Bertambah
  9. IF Permintaan Tinggi AND Persediaan Banyak THEN Produksi Tetap

---

## 🚀 Running Locally (Development Mode)

### Prerequisites:
- Python 3.10+
- Node.js 18+ & npm

### Steps:

1. **Run Streamlit DSS Application:**
   ```bash
   cd services/streamlit
   pip install -r requirements.txt
   streamlit run app.py
   ```
   *(Note: If PostgreSQL is not active locally, the application automatically uses an embedded SQLite database `dks_fuzzy_local.db` for seamless local testing!)*

2. **Run Vue 3 Frontend:**
   ```bash
   cd frontend
   npm install
   npm run dev
   ```

3. **Access Web App:**
   Open browser at `http://localhost:8501`

---

## 🐳 Containerized Deployment (Docker)

### Prerequisites:
- Docker & Docker Compose installed on your system.

### Deploy Steps:
1. **Build and Start Containers:**
   ```bash
   docker compose up -d --build
   ```
2. **Check Container Status:**
   ```bash
   docker compose ps
   ```
3. **Stop Containers:**
   ```bash
   docker compose down -v
   ```

---

## 📊 Database CTE MAPE Query Example
The application computes MAPE dynamically using the following PostgreSQL Common Table Expression (CTE):

```sql
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
FROM ape_calc;
```

---

## 📄 License & Credits
Developed as a production-grade Decision Support System for **UMKM Donat Kentang Syifa (DKS)** thesis project.
