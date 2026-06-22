"""
Configuracion y plantilla principal de la pagina.
"""
import streamlit as st


def configurar_pagina():
    st.set_page_config(
        page_title="IT Infrastructure Analytics",
        page_icon="📊",
        layout="wide"
    )
    st.title("🛡️ Predictive IT Infrastructure Analytics")
