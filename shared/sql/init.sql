-- Database Schema for UMKM Donat Kentang Syifa (DKS) FIS DSS
-- Automatically executed on PostgreSQL container startup

CREATE TABLE IF NOT EXISTS production_data (
    id SERIAL PRIMARY KEY,
    tanggal DATE NOT NULL UNIQUE,
    permintaan INTEGER NOT NULL CHECK (permintaan >= 0),
    persediaan INTEGER NOT NULL CHECK (persediaan >= 0),
    produksi_aktual INTEGER CHECK (produksi_aktual >= 0),
    prediksi_fis INTEGER NOT NULL CHECK (prediksi_fis >= 0),
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

CREATE INDEX IF NOT EXISTS idx_production_tanggal ON production_data(tanggal);

-- User Authentication Table
CREATE TABLE IF NOT EXISTS users (
    id SERIAL PRIMARY KEY,
    username VARCHAR(50) NOT NULL UNIQUE,
    password_hash VARCHAR(255) NOT NULL,
    role VARCHAR(20) DEFAULT 'admin',
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- Seed Default Admin User (username: admin, password: dks2026)
INSERT INTO users (username, password_hash, role)
VALUES ('admin', '9c3a3f56cb0a715974a497aa97ae82ab11b99facd16aee6addca402958cc0492', 'admin')
ON CONFLICT (username) DO NOTHING;

-- Sample Data Seeding for Evaluation (30 historical daily records)
INSERT INTO production_data (tanggal, permintaan, persediaan, produksi_aktual, prediksi_fis)
VALUES 
    (CURRENT_DATE - INTERVAL '30 days', 520, 110, 580, 568),
    (CURRENT_DATE - INTERVAL '29 days', 610, 140, 620, 604),
    (CURRENT_DATE - INTERVAL '28 days', 480, 90,  540, 532),
    (CURRENT_DATE - INTERVAL '27 days', 700, 160, 710, 688),
    (CURRENT_DATE - INTERVAL '26 days', 350, 60,  400, 395),
    (CURRENT_DATE - INTERVAL '25 days', 580, 130, 600, 590),
    (CURRENT_DATE - INTERVAL '24 days', 640, 150, 630, 615),
    (CURRENT_DATE - INTERVAL '23 days', 420, 80,  460, 450),
    (CURRENT_DATE - INTERVAL '22 days', 530, 100, 570, 555),
    (CURRENT_DATE - INTERVAL '21 days', 690, 170, 680, 675),
    (CURRENT_DATE - INTERVAL '20 days', 750, 180, 760, 742),
    (CURRENT_DATE - INTERVAL '19 days', 310, 50,  350, 360),
    (CURRENT_DATE - INTERVAL '18 days', 490, 110, 520, 510),
    (CURRENT_DATE - INTERVAL '17 days', 620, 140, 640, 630),
    (CURRENT_DATE - INTERVAL '16 days', 570, 120, 590, 580),
    (CURRENT_DATE - INTERVAL '15 days', 660, 160, 670, 650),
    (CURRENT_DATE - INTERVAL '14 days', 430, 90,  470, 465),
    (CURRENT_DATE - INTERVAL '13 days', 500, 100, 530, 520),
    (CURRENT_DATE - INTERVAL '12 days', 720, 170, 730, 715),
    (CURRENT_DATE - INTERVAL '11 days', 380, 70,  410, 415),
    (CURRENT_DATE - INTERVAL '10 days', 550, 130, 570, 560),
    (CURRENT_DATE - INTERVAL '9 days',  600, 140, 610, 600),
    (CURRENT_DATE - INTERVAL '8 days',  670, 150, 680, 665),
    (CURRENT_DATE - INTERVAL '7 days',  440, 90,  480, 470),
    (CURRENT_DATE - INTERVAL '6 days',  510, 110, 540, 530),
    (CURRENT_DATE - INTERVAL '5 days',  730, 180, 740, 725),
    (CURRENT_DATE - INTERVAL '4 days',  360, 60,  400, 390),
    (CURRENT_DATE - INTERVAL '3 days',  590, 130, 610, 595),
    (CURRENT_DATE - INTERVAL '2 days',  650, 150, 660, 645),
    (CURRENT_DATE - INTERVAL '1 day',   540, 120, 560, 550)
ON CONFLICT (tanggal) DO NOTHING;
