"""
Streamlit Web Application for UMKM Donat Kentang Syifa (DKS) Decision Support System (DSS).
Provides Fuzzy Inference System (FIS) Mamdani production planning, dynamic MAPE analytics, 
and database management.
"""

import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from datetime import date

from config import DOMAIN_PERMINTAAN, DOMAIN_PERSEDIAAN, DOMAIN_PRODUKSI
from fuzzy_logic import FIS_Mamdani_DKS
from database import (
    init_db,
    save_production_record,
    get_all_production_records,
    get_mape_analytics,
    authenticate_user,
    DB_BACKEND
)

# Set Streamlit Page Configuration
st.set_page_config(
    page_title="DKS - Donat Kentang Syifa",
    page_icon="🍩",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS Styling khusus Light Mode (Bersih, Kontras Tinggi & Profesional)
st.markdown("""
    <style>

    
    .block-container,
    [data-testid="stMainBlockContainer"] {
        padding-top: 1.5rem !important;
        padding-bottom: 3rem !important;
    }
    
    /* Custom Card Containers */
    .css-card {
        background: var(--background-color, #FFFFFF);
        border-radius: 12px;
        padding: 20px;
        border: 1px solid var(--secondary-background-color, #E2E8F0);
        margin-bottom: 20px;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.05);
    }
    
    /* Result Header Glow */
    .result-box {
        background: var(--secondary-background-color, #ECFDF5);
        border: 2px solid var(--primary-color, #059669);
        border-radius: 16px;
        padding: 25px;
        text-align: center;
        box-shadow: 0 4px 12px 0 rgba(0, 0, 0, 0.15);
    }
    .result-number {
        font-size: 52px;
        font-weight: 800;
        color: var(--primary-color, #047857);
        margin: 10px 0;
    }
    .result-subtitle {
        color: var(--text-color, #374151);
        font-size: 16px;
    }

    /* Database Status Badge */
    .db-badge-pg {
        background-color: #10B981;
        color: #FFFFFF;
        padding: 4px 10px;
        border-radius: 12px;
        font-size: 12px;
        font-weight: bold;
    }
    .db-badge-sqlite {
        background-color: #F59E0B;
        color: #FFFFFF;
        padding: 4px 10px;
        border-radius: 12px;
        font-size: 12px;
        font-weight: bold;
    }

    /* Animated Gradient Background for Login */
    @keyframes gradientShift {
        0% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
        100% { background-position: 0% 50%; }
    }
    @keyframes floatOrb1 {
        0%, 100% { transform: translate(0, 0) rotate(0deg) scale(1); }
        50% { transform: translate(45px, -55px) rotate(180deg) scale(1.15); }
    }
    @keyframes floatOrb2 {
        0%, 100% { transform: translate(0, 0) rotate(0deg) scale(1); }
        50% { transform: translate(-55px, 45px) rotate(-180deg) scale(1.2); }
    }

    .login-bg-container {
        position: fixed;
        top: 0;
        left: 0;
        width: 100vw;
        height: 100vh;
        z-index: 0;
        pointer-events: none;
        background: linear-gradient(-45deg, #FFFBEB, #FEF3C7, #FDE68A, #F3F4F6);
        background-size: 400% 400%;
        animation: gradientShift 15s ease infinite;
        overflow: hidden;
    }
    .orb-amber-1 {
        position: absolute;
        top: 10%;
        left: 10%;
        width: 420px;
        height: 420px;
        background: radial-gradient(circle, rgba(245, 158, 11, 0.22) 0%, rgba(251, 191, 36, 0) 70%);
        border-radius: 50%;
        animation: floatOrb1 14s ease-in-out infinite;
    }
    .orb-amber-2 {
        position: absolute;
        bottom: 10%;
        right: 10%;
        width: 480px;
        height: 480px;
        background: radial-gradient(circle, rgba(217, 119, 6, 0.18) 0%, rgba(245, 158, 11, 0) 70%);
        border-radius: 50%;
        animation: floatOrb2 18s ease-in-out infinite;
    }

    /* Unified Form Card Styling with Glassmorphism */
    div[data-testid="stForm"] {
        position: relative !important;
        z-index: 10 !important;
        max-width: 480px !important;
        margin: 0 auto !important;
        border-radius: 24px !important;
        border: 1px solid rgba(252, 211, 77, 0.6) !important;
        padding: 34px 30px !important;
        background: var(--background-color) !important;
        backdrop-filter: blur(16px) !important;
        box-shadow: 0 20px 45px -10px rgba(217, 119, 6, 0.15), 0 10px 15px -3px rgba(0, 0, 0, 0.03) !important;
    }

    /* Login Form Text & Button Sizing - Balanced Proportions */
    .stTextInput label {
        font-size: 16px !important;
        font-weight: 700 !important;
        color: var(--text-color) !important;
        margin-bottom: 5px !important;
    }
    .stTextInput input {
        font-size: 15px !important;
        padding: 10px 14px !important;
        border-radius: 11px !important;
    }
    div[data-testid="stFormSubmitButton"] button,
    div[data-testid="stFormSubmitButton"] button p,
    div[data-testid="stFormSubmitButton"] button span {
        font-weight: 400 !important;
        letter-spacing: 0.3px !important;
    }
    div[data-testid="stFormSubmitButton"] button[kind="secondaryFormSubmit"] {
        border-radius: 12px !important;
        background: linear-gradient(135deg, #FCD34D 0%, #F59E0B 100%) !important; /* Lighter Amber */
        color: #451A03 !important; /* Dark brown for high contrast */
        border: none !important;
        box-shadow: 0 4px 14px rgba(245, 158, 11, 0.3) !important;
        transition: all 0.3s ease !important;
    }
    div[data-testid="stFormSubmitButton"] button[kind="secondaryFormSubmit"]:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 16px rgba(245, 158, 11, 0.4) !important;
        background: linear-gradient(135deg, #FDE68A 0%, #FBBF24 100%) !important;
    }
    div[data-testid="stFormSubmitButton"] button[kind="primaryFormSubmit"] p {
        font-size: 18px !important;
        font-weight: 600 !important;
    }
    
    div[data-testid="stFormSubmitButton"] button[kind="primaryFormSubmit"] {
        border-radius: 12px !important;
        background: rgb(180, 83, 9) !important; /* Portal Admin Color */
        color: #FFFFFF !important; 
        border: none !important;
        box-shadow: 0 4px 14px rgba(180, 83, 9, 0.3) !important;
        transition: all 0.3s ease !important;
    }
    div[data-testid="stFormSubmitButton"] button[kind="primaryFormSubmit"]:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 16px rgba(180, 83, 9, 0.4) !important;
        background: rgb(146, 64, 14) !important; /* Slightly darker on hover */
    }

    /* Sidebar Logout Button (Red Theme) */
    [data-testid="stSidebar"] div.stButton > button {
        background: linear-gradient(135deg, #EF4444 0%, #B91C1C 100%) !important;
        color: white !important;
        border: none !important;
        border-radius: 10px !important;
        font-weight: 700 !important;
        box-shadow: 0 4px 12px rgba(220, 38, 38, 0.3) !important;
        transition: all 0.3s ease !important;
    }
    [data-testid="stSidebar"] div.stButton > button:hover {
        background: linear-gradient(135deg, #F87171 0%, #DC2626 100%) !important;
        transform: translateY(-2px);
    }

    /* Save Data Button (Emerald Green Theme for Primary Buttons) */
    div.stButton > button[kind="primary"] {
        background: linear-gradient(135deg, #10B981 0%, #059669 100%) !important;
        color: white !important;
        border: none !important;
        border-radius: 12px !important;
        font-weight: 700 !important;
        padding: 10px 20px !important;
        box-shadow: 0 4px 12px rgba(16, 185, 129, 0.3) !important;
        transition: all 0.3s ease !important;
    }
    div.stButton > button[kind="primary"]:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 16px rgba(16, 185, 129, 0.4) !important;
    }



    
    /* Margin Bottom Navbar / Padding Top Global Content */
    .block-container, [data-testid="stMainBlockContainer"] {
        padding-top: 3.5rem !important;
    }
    
    /* Styling Global Tombol Home di Navbar */
    .custom-home-btn {
        position: absolute;
        top: 50%;
        left: 50%;
        transform: translate(-50%, -50%);
        z-index: 999999;
        background-color: #F59E0B;
        color: white !important;
        padding: 6px 20px;
        border-radius: 20px;
        font-weight: 600;
        text-decoration: none !important;
        font-size: 15px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        transition: background-color 0.2s ease;
        font-family: 'Inter', sans-serif;
    }
    .custom-home-btn:hover, .custom-home-btn:active {
        background-color: #D97706;
        transform: translate(-50%, -50%); /* Pertahankan posisi tanpa efek scale */
    }
    
    /* Styling khusus Tombol Hitung Rekomendasi (Amber) */
    div[data-testid="stMainBlockContainer"] div.stButton > button[kind="secondary"] {
        border-radius: 12px !important;
        background: linear-gradient(135deg, #FCD34D 0%, #F59E0B 100%) !important;
        color: #451A03 !important;
        border: none !important;
        box-shadow: 0 4px 14px rgba(245, 158, 11, 0.3) !important;
        transition: all 0.3s ease !important;
    }
    div[data-testid="stMainBlockContainer"] div.stButton > button[kind="secondary"]:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 16px rgba(245, 158, 11, 0.4) !important;
        background: linear-gradient(135deg, #FDE68A 0%, #FBBF24 100%) !important;
    }
    </style>
""", unsafe_allow_html=True)


@st.cache_resource
def initialize_system():
    """Initializes DB schema and loads FIS Engine."""
    # Force cache invalidation to load 10x scaled BACK domains
    import importlib
    import config, fuzzy_logic
    importlib.reload(config)
    importlib.reload(fuzzy_logic)
    
    init_db()
    return fuzzy_logic.FIS_Mamdani_DKS()

fis = initialize_system()

import time

# -------------------------------------------------------------
# Authentication Guard & Session Management (Native Cookies)
# -------------------------------------------------------------
import json
import base64

def set_native_cookie(key, value, expires_days=1):
    import streamlit.components.v1 as components
    # Create an expiration date in UTC
    js_code = f"""
        <script>
            var d = new Date();
            d.setTime(d.getTime() + ({expires_days}*24*60*60*1000));
            var expires = "expires="+ d.toUTCString();
            document.cookie = "{key}=" + encodeURIComponent("{value}") + ";" + expires + ";path=/";
        </script>
    """
    components.html(js_code, height=0)

# Process pending auth actions before rendering anything
if st.session_state.get("do_logout"):
    keys_to_clear = ["authenticated", "username", "fullname", "role", "do_logout"]
    for k in keys_to_clear:
        if k in st.session_state:
            del st.session_state[k]
            
    import streamlit.components.v1 as components
    components.html("""
        <script>
            // Manually obliterate cookies to guarantee logout immediately
            document.cookie = "dks_auth=; expires=Thu, 01 Jan 1970 00:00:00 UTC; path=/;";
            
            // For good measure, wipe all cookies
            document.cookie.split(";").forEach(function(c) { 
                document.cookie = c.replace(/^ +/, "").replace(/=.*/, "=;expires=" + new Date().toUTCString() + ";path=/"); 
            });
            
            setTimeout(function() {
                window.parent.location.reload();
            }, 100);
        </script>
    """, height=0)
    st.stop()

if st.session_state.get("do_login"):
    user_data = st.session_state["do_login"]
    
    # Create a simple token containing user data
    token_data = {
        "user": user_data["username"],
        "fullname": user_data.get("fullname") or user_data["username"],
        "role": user_data["role"],
        "last_active": time.time()
    }
    # Encode token as base64 JSON
    token_str = base64.b64encode(json.dumps(token_data).encode()).decode()
    
    # Save to browser cookie
    set_native_cookie("dks_auth", token_str, expires_days=1)
    
    st.session_state["authenticated"] = True
    st.session_state["username"] = token_data["user"]
    st.session_state["fullname"] = token_data["fullname"]
    st.session_state["role"] = token_data["role"]
    del st.session_state["do_login"]
    
    # Force a reload so the browser sends the cookie on the next request
    import streamlit.components.v1 as components
    components.html("""
        <script>
            setTimeout(function() {
                window.parent.location.reload();
            }, 100);
        </script>
    """, height=0)
    st.stop()

current_time = time.time()
TIMEOUT_SECONDS = 2 * 3600  # 2 hours

# Read auth state natively from browser cookies
raw_cookie = st.context.cookies.get("dks_auth")

q_auth = False
q_user = None
q_fullname = None
q_role = "admin"
q_last = 0.0

if raw_cookie:
    try:
        import urllib.parse
        decoded_cookie = urllib.parse.unquote(raw_cookie)
        token_data = json.loads(base64.b64decode(decoded_cookie).decode())
        q_user = token_data.get("user")
        q_fullname = token_data.get("fullname")
        q_role = token_data.get("role", "admin")
        q_last = float(token_data.get("last_active", 0.0))
        q_auth = True
    except Exception as e:
        pass

# Initialize session_state based on cookies
if "authenticated" not in st.session_state:
    st.session_state["authenticated"] = q_auth
    st.session_state["username"] = q_user
    st.session_state["fullname"] = q_fullname
    st.session_state["role"] = q_role

# Handle Timeout logic
if st.session_state.get("authenticated"):
    if current_time - q_last > TIMEOUT_SECONDS and q_last > 0:
        st.session_state["do_logout"] = True
        st.rerun()
    else:
        # Update last active time to keep session alive
        if raw_cookie:
            try:
                token_data["last_active"] = current_time
                new_token_str = base64.b64encode(json.dumps(token_data).encode()).decode()
                set_native_cookie("dks_auth", new_token_str, expires_days=1)
            except:
                pass


def login_page():
    st.markdown("""
        <style>
            [data-testid="collapsedControl"] { display: none !important; }
            [data-testid="stSidebar"] { display: none !important; }
            [data-testid="stHeader"] { display: none !important; }
            .block-container, [data-testid="stMainBlockContainer"] {
                padding-top: 1rem !important;
            }
            
            /* Kunci halaman login ke Light Mode dengan menimpa CSS Variables bawaan Streamlit */
            .stApp, .block-container, div[data-testid="stForm"], .stTextInput {
                --text-color: #0F172A !important;
                --background-color: #FFFFFF !important;
                --secondary-background-color: #F8FAFC !important;
            }
            
            .stApp {
                background-color: #F8FAFC !important;
                background-image: none !important;
                color: #0F172A !important;
            }
            
            /* Kembalikan warna form login ke putih glassmorphism */
            div[data-testid="stForm"] {
                background: rgba(255, 255, 255, 0.94) !important;
            }
            
            /* Paksa Light Mode pada komponen stTextInput secara struktural dan radikal */
            div[data-testid="stTextInput"] > div:nth-of-type(1) {
                background-color: #FFFFFF !important;
                border: 1px solid #CBD5E1 !important;
                border-radius: 8px !important;
                overflow: hidden !important;
            }
            
            /* Hancurkan semua background dan border bawaan Dark Mode di dalam kotak input, 
               serta paksa SEMUA elemen di dalamnya (termasuk ikon font/SVG) menjadi abu-abu gelap */
            div[data-testid="stTextInput"] > div:nth-of-type(1) * {
                background-color: transparent !important;
                border: none !important;
                box-shadow: none !important;
                color: #64748B !important;
            }
            
            /* Warna kursor dan teks ketikan (harus lebih gelap dari ikon) */
            div[data-testid="stTextInput"] input {
                color: #0F172A !important;
                -webkit-text-fill-color: #0F172A !important;
            }
            
            /* Placeholder (teks bayangan) */
            div[data-testid="stTextInput"] input::placeholder {
                color: #94A3B8 !important;
                -webkit-text-fill-color: #94A3B8 !important;
            }
            
            /* Pastikan khusus elemen SVG (jika icon menggunakan SVG) tetap mewarisi warna yang benar tanpa merusak bentuknya */
            div[data-testid="stTextInput"] svg {
                fill: currentColor !important;
            }
        </style>
        <div class="login-bg-container">
            <div class="orb-amber-1"></div>
            <div class="orb-amber-2"></div>
            <div style="position: absolute; top: 10%; left: 15%; font-size: 80px; opacity: 0.15; transform: rotate(-15deg); animation: floatOrb1 15s ease-in-out infinite;">🍩</div>
            <div style="position: absolute; bottom: 20%; right: 10%; font-size: 120px; opacity: 0.1; transform: rotate(25deg); animation: floatOrb2 20s ease-in-out infinite;">🍩</div>
            <div style="position: absolute; top: 70%; left: 5%; font-size: 60px; opacity: 0.15; transform: rotate(10deg); animation: floatOrb1 12s ease-in-out infinite;">🍩</div>
            <div style="position: absolute; top: 30%; right: 20%; font-size: 50px; opacity: 0.12; transform: rotate(-25deg); animation: floatOrb2 16s ease-in-out infinite;">🍩</div>
        </div>
    """, unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns([1, 2.2, 1])
    with col2:
        with st.form("login_form", clear_on_submit=False):
            st.markdown("""
                <div style="text-align: center; margin-bottom: 18px;">
                    <h3 style="color: #D97706; font-size: 24px; font-weight: 800; margin: 0 0 12px 0; line-height: 1.3; text-align: center;">
                        Portal Admin <br>
                        <span style="display: block; text-align: center; margin-top: 2px; font-size: 15px; font-weight: 600; color: #B45309; letter-spacing: 0.2px;">Daily Production Decision Support System</span>
                    </h3>
                    <div style="
                        width: 70px;
                        height: 70px;
                        background: linear-gradient(135deg, #D97706 0%, #B45309 100%);
                        border-radius: 20px;
                        display: inline-flex;
                        align-items: center;
                        justify-content: center;
                        font-size: 38px;
                        box-shadow: 0 6px 14px rgba(217, 119, 6, 0.25);
                        margin-bottom: 10px;
                    ">🍩</div>
                    <h2 style="color: #0F172A; font-size: 20px; font-weight: 700; margin: 0 0 14px 0;">
                        Donat Kentang Syifa (DKS)
                    </h2>
                    <div style="border-top: 1px solid #F1F5F9; margin-bottom: 22px;"></div>
                </div>
            """, unsafe_allow_html=True)
            
            username_input = st.text_input("Username", placeholder="👤 Masukkan username").strip()
            password_input = st.text_input("Password", type="password", placeholder="🔒 Masukkan password").strip()
            
            st.markdown("<div style='margin-top: 15px;'></div>", unsafe_allow_html=True)
            submitted = st.form_submit_button("Masuk ➔", type="primary", use_container_width=True)
            st.markdown("""
                <a href="/" target="_self" style="
                    display: block;
                    width: 100%;
                    padding: 8px 12px;
                    background-color: transparent;
                    color: #0F172A;
                    border: 1px solid #CBD5E1;
                    border-radius: 8px;
                    text-align: center;
                    text-decoration: none;
                    font-size: 15px;
                    font-weight: 500;
                    font-family: inherit;
                    transition: all 0.2s ease;
                " onmouseover="this.style.borderColor='#94A3B8'; this.style.backgroundColor='#F8FAFC';" onmouseout="this.style.borderColor='#CBD5E1'; this.style.backgroundColor='transparent';">
                    Kembali ke Halaman Utama
                </a>
            """, unsafe_allow_html=True)
            if submitted:
                if not username_input or not password_input:
                    st.warning("⚠️ Mohon isi username dan password Anda.")
                else:
                    user_data = authenticate_user(username_input, password_input)
                    if user_data:
                        # Queue login for the next cycle to safely save cookies
                        st.session_state["do_login"] = user_data
                        st.rerun()
                    else:
                        st.error("❌ Username atau password salah. Silakan coba lagi.")



def render_sidebar(pages):
    # Pindahkan tombol Home secara dinamis ke dalam stHeader dan sinkronkan warna background
    st.components.v1.html("""
        <script>
            const header = window.parent.document.querySelector('[data-testid="stHeader"]');
            const sidebar = window.parent.document.querySelector('[data-testid="stSidebar"]');
            
            if (header) {
                // Sinkronisasi background color navbar dengan sidebar secara real-time
                if (sidebar) {
                    const syncColor = () => {
                        const bgColor = window.getComputedStyle(sidebar).backgroundColor;
                        header.style.backgroundColor = bgColor;
                        header.style.background = bgColor;
                    };
                    syncColor();
                    setInterval(syncColor, 50);
                }
                
                // Pindahkan tombol Home
                if (!header.querySelector('.custom-home-btn')) {
                    const btn = window.parent.document.createElement('a');
                    btn.href = '/';
                    btn.target = '_self';
                    btn.className = 'custom-home-btn';
                    btn.innerText = '🏠 Home';
                    
                    header.appendChild(btn);
                }
            }
        </script>
    """, height=0, width=0)
    
    st.sidebar.image("https://img.icons8.com/emoji/96/doughnut-emoji.png", width=70)
    st.sidebar.title("DKS - Donat Kentang Syifa")
    st.sidebar.caption("Daily Production Decision Support System")
    
    st.sidebar.markdown("---")
    st.sidebar.markdown("**Menu Navigasi**")
    for p in pages:
        st.sidebar.page_link(p)
        
    st.sidebar.markdown("---")
    
    display_name = st.session_state.get('fullname') or st.session_state.get('username', 'Admin')
    st.sidebar.markdown(f"👤 Pengguna: **{display_name}**")
    if st.sidebar.button("Logout", width="stretch"):
        st.session_state["do_logout"] = True
        st.rerun()
    if DB_BACKEND == "PostgreSQL":
        st.sidebar.markdown('Database Status: <span class="db-badge-pg">PostgreSQL Active</span>', unsafe_allow_html=True)
    else:
        st.sidebar.markdown('Database Status: <span class="db-badge-sqlite">SQLite Local</span>', unsafe_allow_html=True)
    st.sidebar.markdown("---")

# ==========================================
# PAGE 1: MAIN DASHBOARD (INPUT & PREDIKSI)
# ==========================================
def dashboard_page():
    st.markdown("<h2>🍩 Daily Donut Production Calculator</h2>", unsafe_allow_html=True)
    st.markdown("Determinasi Jumlah Produksi Harian Optimal menggunakan **Fuzzy Inference System Mamdani**.")

    col_input, col_result = st.columns([1, 1], gap="large")

    with col_input:
        st.subheader("📋 Input Operasional Harian")
        
        # Inisialisasi state persisten (permanen)
        if "saved_tgl" not in st.session_state: st.session_state.saved_tgl = date.today()
        if "saved_perm" not in st.session_state: st.session_state.saved_perm = 7500
        if "saved_pers" not in st.session_state: st.session_state.saved_pers = 150
        if "saved_akt" not in st.session_state: st.session_state.saved_akt = 0
            
        # Inisialisasi widget key (temporer) agar sesuai dengan state persisten saat kembali ke halaman
        if "_tgl" not in st.session_state: st.session_state._tgl = st.session_state.saved_tgl
        if "_perm" not in st.session_state: st.session_state._perm = st.session_state.saved_perm
        if "_pers" not in st.session_state: st.session_state._pers = st.session_state.saved_pers
        if "_akt" not in st.session_state: st.session_state._akt = st.session_state.saved_akt
        
        def sync_inputs():
            st.session_state.saved_tgl = st.session_state._tgl
            st.session_state.saved_perm = st.session_state._perm
            st.session_state.saved_pers = st.session_state._pers
            st.session_state.saved_akt = st.session_state._akt

        tgl_input = st.date_input("Tanggal Produksi", key="_tgl", on_change=sync_inputs)
        
        permintaan_input = st.number_input(
            "Jumlah Permintaan Donat (Pcs)",
            min_value=0, max_value=DOMAIN_PERMINTAAN[1], step=10,
            help="Total unit permintaan donat dari konsumen/reseller.",
            key="_perm", on_change=sync_inputs
        )
        
        persediaan_input = st.number_input(
            "Sisa Persediaan / Stok (Pcs)",
            min_value=0, max_value=DOMAIN_PERSEDIAAN[1], step=10,
            help="Sisa stok donat dari hari sebelumnya.",
            key="_pers", on_change=sync_inputs
        )
        
        produksi_aktual_input = st.number_input(
            "Produksi Aktual Harian (Opsional - Pcs)",
            min_value=0, max_value=20000, step=10,
            help="Isi jika sudah ada data realisasi produksi aktual untuk evaluasi MAPE.",
            key="_akt", on_change=sync_inputs
        )
        
        st.markdown("<div class='hitung-btn-marker' style='display:none'></div>", unsafe_allow_html=True)
        submit_calc = st.button("Hitung Rekomendasi Produksi FIS", use_container_width=True)
            
    # Compute FIS result
    if 'current_result' not in st.session_state or submit_calc:
        st.session_state['current_result'] = fis.compute(st.session_state.saved_perm, st.session_state.saved_pers)
        st.session_state['current_date'] = st.session_state.saved_tgl
        st.session_state['current_aktual'] = st.session_state.saved_akt if st.session_state.saved_akt > 0 else None

    result = st.session_state['current_result']

    with col_result:
        st.subheader("🎯 Hasil Rekomendasi Produksi")
        st.markdown(f"""
            <div class="result-box">
                <div class="result-subtitle">Rekomendasi Produksi Donat (Prediksi FIS)</div>
                <div class="result-number">{result['produksi_prediksi']} <span style="font-size: 24px;">Pcs</span></div>
                <div class="result-subtitle">Nilai Centroid Presisi: <b>{result['produksi_float']}</b> unit</div>
            </div>
        """, unsafe_allow_html=True)
        
        st.markdown("<br>", unsafe_allow_html=True)
        btn_save = st.button("💾 Simpan Data Produksi ke Database", width="stretch", type="primary")
        if btn_save:
            try:
                save_production_record(
                    tanggal=st.session_state['current_date'],
                    permintaan=result['permintaan'],
                    persediaan=result['persediaan'],
                    prediksi_fis=result['produksi_prediksi'],
                    produksi_aktual=st.session_state['current_aktual']
                )
                st.success(f"Data tanggal {st.session_state['current_date']} berhasil disimpan ke database!")
            except Exception as e:
                st.error(f"Gagal menyimpan data: {e}")

    st.markdown("---")
    st.subheader("🔍 Visualisasi Detail Fuzzifikasi & Defuzzifikasi")

    tab_mf, tab_defuzz, tab_rules = st.tabs(["📉 Fungsi Keanggotaan (MF)", "📊 Agregasi & Centroid", "📜 Rule Evaluation Detail"])

    with tab_mf:
        c1, c2 = st.columns(2)
        with c1:
            fig_p = fis.plot_membership_functions("permintaan", current_val=result['permintaan'])
            fig_p.update_layout(template="plotly_white")
            st.plotly_chart(fig_p, width="stretch")
            
            # Show fuzzification degree breakdown
            st.write("**Derajat Keanggotaan μ(Permintaan):**")
            cols_p = st.columns(3)
            for i, (k, v) in enumerate(result['mu_permintaan'].items()):
                cols_p[i].metric(label=k, value=f"{v:.3f}")

        with c2:
            fig_s = fis.plot_membership_functions("persediaan", current_val=result['persediaan'])
            fig_s.update_layout(template="plotly_white")
            st.plotly_chart(fig_s, width="stretch")
            
            # Show fuzzification degree breakdown
            st.write("**Derajat Keanggotaan μ(Persediaan):**")
            cols_s = st.columns(3)
            for i, (k, v) in enumerate(result['mu_persediaan'].items()):
                cols_s[i].metric(label=k, value=f"{v:.3f}")

    with tab_defuzz:
        fig_out = fis.plot_aggregated_output(result)
        fig_out.update_layout(template="plotly_white")
        st.plotly_chart(fig_out, width="stretch")
        st.info("Centroid dihitung dengan melakukan integrasi numerik pada daerah kurva fuzzy yang teragregasi.")

    with tab_rules:
        st.markdown("**Evaluasi 9 Aturan Fuzzy Mamdani:**")
        df_rules = pd.DataFrame(result['rule_results'])
        df_rules.columns = ["No", "Aturan FIS (Rule)", "Firing Strength (α-predikat)", "Himpunan Output"]
        st.dataframe(
            df_rules.style.highlight_max(subset=["Firing Strength (α-predikat)"], color="#A7F3D0"),
            width="stretch",
            hide_index=True
        )


# ==========================================
# PAGE 2: HISTORY & ANALYTICS (MAPE)
# ==========================================
def history_page():
    st.markdown("<h2>📈 History & Analytics</h2>", unsafe_allow_html=True)
    st.markdown("Evaluasi Akurasi Prediksi FIS Mamdani dibandingkan dengan **Realisasi Produksi Aktual**.")

    # Analytics Metrics Card
    analytics = get_mape_analytics()

    col_m1, col_m2, col_m3, col_m4 = st.columns(4)
    col_m1.metric("Evaluasi Records", f"{analytics['total_records']} Hari")
    
    # MAPE color coding
    mape_val = analytics['mape']
    
    col_m2.metric(
        "MAPE Current FIS", 
        f"{mape_val}%"
    )
    col_m3.metric("MAE (Mean Abs Error)", f"{analytics['mae']} Pcs")
    col_m4.metric("Rentang APE", f"{analytics['min_ape']}% - {analytics['max_ape']}%")

    st.markdown("---")

    # Load all records
    df_history = get_all_production_records()
    if not df_history.empty:
        import pandas as pd
        df_history['tanggal'] = pd.to_datetime(df_history['tanggal'])
        
        st.subheader("🔍 Filter Data Riwayat")
        col_f1, col_f2 = st.columns(2)
        
        import datetime
        now = datetime.datetime.now()
        
        # Inisialisasi state jika belum ada
        if "history_year" not in st.session_state:
            st.session_state.history_year = now.year
            
        years = sorted(df_history['tanggal'].dt.year.unique().tolist(), reverse=True)
        year_options = ["Semua Tahun"] + years
        
        # Gunakan state untuk menentukan pilihan bawaan (default)
        target_year = st.session_state.history_year
        default_year_idx = year_options.index(target_year) if target_year in year_options else 0
        
        with col_f1:
            selected_year = st.selectbox("Pilih Tahun", year_options, index=default_year_idx)
            # Simpan kembali ke state
            st.session_state.history_year = selected_year
            
        months = [{"id": 1, "name": "Januari"}, {"id": 2, "name": "Februari"}, {"id": 3, "name": "Maret"}, 
                  {"id": 4, "name": "April"}, {"id": 5, "name": "Mei"}, {"id": 6, "name": "Juni"},
                  {"id": 7, "name": "Juli"}, {"id": 8, "name": "Agustus"}, {"id": 9, "name": "September"},
                  {"id": 10, "name": "Oktober"}, {"id": 11, "name": "November"}, {"id": 12, "name": "Desember"}]
        
        if "history_month" not in st.session_state:
            st.session_state.history_month = next((m["name"] for m in months if m["id"] == now.month), "Juli")
            
        month_options = ["Semua Bulan"] + [m["name"] for m in months]
        
        target_month = st.session_state.history_month
        default_month_idx = month_options.index(target_month) if target_month in month_options else 0
        
        with col_f2:
            selected_month_name = st.selectbox("Pilih Bulan", month_options, index=default_month_idx)
            st.session_state.history_month = selected_month_name
            
        if selected_year != "Semua Tahun":
            df_history = df_history[df_history['tanggal'].dt.year == selected_year]
            
        if selected_month_name != "Semua Bulan":
            selected_month_id = next(m["id"] for m in months if m["name"] == selected_month_name)
            df_history = df_history[df_history['tanggal'].dt.month == selected_month_id]
            
        # Revert date to string/date for proper display without time
        df_history['tanggal'] = df_history['tanggal'].dt.date

    if not df_history.empty:
        st.subheader("📊 Chart Perbandingan Produksi Aktual vs Prediksi FIS")
        
        # Filter records with actual production for comparison chart
        df_chart = df_history.dropna(subset=['produksi_aktual']).sort_values(by='tanggal')

        if not df_chart.empty:
            fig_line = go.Figure()

            fig_line.add_trace(go.Scatter(
                x=df_chart['tanggal'],
                y=df_chart['produksi_aktual'],
                mode='lines+markers',
                name='Produksi Aktual (Real)',
                line=dict(color='#2563EB', width=3),
                marker=dict(size=8)
            ))

            fig_line.add_trace(go.Scatter(
                x=df_chart['tanggal'],
                y=df_chart['prediksi_fis'],
                mode='lines+markers',
                name='Prediksi FIS Mamdani',
                line=dict(color='#059669', width=3, dash='dash'),
                marker=dict(size=8)
            ))

            fig_line.update_layout(
                title="Tren Harian Produksi Aktual vs Rekomendasi FIS",
                xaxis_title="Tanggal",
                yaxis_title="Jumlah Produksi (Pcs)",
                template="plotly_white",
                hovermode="x unified",
                legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1)
            )

            st.plotly_chart(fig_line, width="stretch")
        else:
            st.warning("Belum ada data dengan Produksi Aktual terisi untuk menampilkan chart perbandingan.")

        # Data Table with CSV Export
        st.markdown("---")
        st.subheader("📋 Riwayat Data Produksi dalam Database")

        csv_data = df_history.to_csv(index=False).encode('utf-8')
        st.download_button(
            label="📥 Download Data History (CSV)",
            data=csv_data,
            file_name="dks_history_produksi.csv",
            mime="text/csv",
        )

        st.dataframe(
            df_history,
            width="stretch",
            hide_index=True
        )
    else:
        st.info("Database masih kosong. Gunakan Main Dashboard untuk menambah data produksi.")


# ==========================================
# PAGE 3: CONFIGURATION & FUZZY RULES
# ==========================================
def config_page():
    st.markdown("<h2>⚙️ Konfigurasi Himpunan Fuzzy</h2>", unsafe_allow_html=True)
    st.markdown("Spesifikasi variabel, himpunan fuzzy, dan matriks aturan keputusan UMKM Donat Kentang Syifa.")

    st.subheader("📐 Domain & Boundary Variabel")
    c1, c2, c3 = st.columns(3)
    c1.info(f"**Permintaan (Input 1):**\n- Domain: {DOMAIN_PERMINTAAN[0]} - {DOMAIN_PERMINTAAN[1]} unit\n- Sets: Rendah, Sedang, Tinggi")
    c2.info(f"**Persediaan (Input 2):**\n- Domain: {DOMAIN_PERSEDIAAN[0]} - {DOMAIN_PERSEDIAAN[1]} unit\n- Sets: Sedikit, Sedang, Banyak")
    c3.info(f"**Produksi (Output):**\n- Domain: {DOMAIN_PRODUKSI[0]} - {DOMAIN_PRODUKSI[1]} unit\n- Sets: Berkurang, Tetap, Bertambah")

    st.markdown("---")
    st.subheader("📉 Preview Fungsi Keanggotaan All Variables")

    tab_v1, tab_v2, tab_v3 = st.tabs(["Permintaan", "Persediaan", "Produksi"])
    with tab_v1:
        fig1 = fis.plot_membership_functions("permintaan")
        fig1.update_layout(template="plotly_white")
        st.plotly_chart(fig1, width="stretch")
    with tab_v2:
        fig2 = fis.plot_membership_functions("persediaan")
        fig2.update_layout(template="plotly_white")
        st.plotly_chart(fig2, width="stretch")
    with tab_v3:
        fig3 = fis.plot_membership_functions("produksi")
        fig3.update_layout(template="plotly_white")
        st.plotly_chart(fig3, width="stretch")

    st.markdown("---")
    st.subheader("📜 Matriks Rule Base Mamdani (9 Rules)")
    st.table(pd.DataFrame(fis.rules))

# -------------------------------------------------------------
# APP ROUTING (Native Streamlit Navigation)
# -------------------------------------------------------------

page_dashboard = st.Page(dashboard_page, title="Main Dashboard", icon="📊")
page_history = st.Page(history_page, title="History & Analytics", icon="📈")
page_config = st.Page(config_page, title="Fuzzy Configuration", icon="⚙️")
app_pages = [page_dashboard, page_history, page_config]

if not st.session_state.get("authenticated"):
    # If not logged in, force navigation to Login
    pg = st.navigation([st.Page(login_page, title="Login", icon="🔒")], position="hidden")
else:
    # Render custom sidebar
    render_sidebar(app_pages)
    # Hide the default floating navbar to rely on our custom sidebar placement
    pg = st.navigation(app_pages, position="hidden")


pg.run()