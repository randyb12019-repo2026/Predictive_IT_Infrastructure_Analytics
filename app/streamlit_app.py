import sys
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT_DIR))

import streamlit as st
from dashboard.dashboard import mostrar_dashboard
from src.generar_presentacion import sidebar_presentacion
from src.plantilla import configurar_pagina

configurar_pagina()

with st.sidebar:
    sidebar_presentacion()

mostrar_dashboard()