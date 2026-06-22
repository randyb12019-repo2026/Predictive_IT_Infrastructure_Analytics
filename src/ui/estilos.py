import streamlit as st


def estilos():
    st.markdown("""
    <style>
    .stApp {
        background: linear-gradient(135deg, #020617 0%, #0f172a 50%, #111827 100%);
        color: #e5e7eb;
    }
    h1 { color: #38bdf8; font-size: 42px; }
    h2, h3 { color: #7dd3fc; }
    [data-testid="stMetric"] {
        background-color: #111827;
        border: 1px solid #1e293b;
        padding: 18px;
        border-radius: 16px;
        box-shadow: 0px 0px 14px rgba(56, 189, 248, 0.18);
    }
    .block-container { padding-top: 2rem; }
    .info-card {
        background-color: #0f172a;
        border-left: 6px solid #38bdf8;
        padding: 18px;
        border-radius: 12px;
        color: #e5e7eb;
        margin-bottom: 18px;
    }
    .alert-card {
        background-color: #450a0a;
        border-left: 6px solid #ef4444;
        padding: 18px;
        border-radius: 12px;
        color: white;
    }
    .ok-card {
        background-color: #052e16;
        border-left: 6px solid #22c55e;
        padding: 18px;
        border-radius: 12px;
        color: white;
    }
    </style>
    """, unsafe_allow_html=True)
