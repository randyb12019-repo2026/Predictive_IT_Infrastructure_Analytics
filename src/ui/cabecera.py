import streamlit as st


def cabecera():
    st.markdown("""
    <div class="info-card">
    Dashboard analítico orientado a monitorización de infraestructura IT, detección de incidencias
    y evaluación de modelos predictivos. El objetivo es transformar métricas técnicas del sistema
    en indicadores útiles para operaciones, soporte, ciberseguridad y toma de decisiones.
    </div>
    """, unsafe_allow_html=True)
