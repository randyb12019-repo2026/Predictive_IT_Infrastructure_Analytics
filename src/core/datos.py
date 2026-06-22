import streamlit as st
import pandas as pd
from pathlib import Path


def carga_datos():
    PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent
    FINAL_DIR = PROJECT_ROOT / "data" / "final"
    PROCESSED_DIR = PROJECT_ROOT / "data" / "processed"

    def cargar_csv(ruta):
        if ruta.exists():
            return pd.read_csv(ruta)
        return None

    comparacion = cargar_csv(FINAL_DIR / "comparacion_modelos.csv")
    predicciones = cargar_csv(FINAL_DIR / "predicciones_random_forest.csv")
    datos_infra = cargar_csv(PROCESSED_DIR / "Big_data_dataset_transformado.csv")

    return comparacion, predicciones, datos_infra


def validar_datos(comparacion, predicciones, datos_infra):
    if comparacion is None or predicciones is None or datos_infra is None:
        st.error("No se encontraron los archivos necesarios.")
        st.markdown("""
        Archivos esperados:
        - `data/final/comparacion_modelos.csv`
        - `data/final/predicciones_random_forest.csv`
        - `data/processed/Big_data_dataset_transformado.csv`
        """)
        st.stop()
