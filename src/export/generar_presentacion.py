"""
Sidebar para exportar presentacion PDF desde Streamlit.
"""
import streamlit as st
from src.export.presentacion import generar_presentacion as generar_pdf


def sidebar_presentacion():
    st.header("📥 Exportar presentación")
    if st.button("🚀 Generar PDF"):
        with st.spinner("Generando presentación…"):
            try:
                ruta = generar_pdf()
                with open(ruta, "rb") as f:
                    st.download_button(
                        label="📥 Descargar presentación",
                        data=f,
                        file_name="Presentacion_Predictive_IT_Analytics.pdf",
                        mime="application/pdf"
                    )
                st.success("✅ Presentación lista para descargar")
            except Exception as e:
                st.error(f"Error: {e}")

