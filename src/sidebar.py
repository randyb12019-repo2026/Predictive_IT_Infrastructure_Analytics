import streamlit as st


def sidebar(datos_infra=None):
    st.sidebar.title("⚙️ Centro de Control")
    st.sidebar.markdown("Dashboard de infraestructura, incidencias y modelo predictivo.")

    seccion = st.sidebar.radio(
        "Navegación",
        ["Resumen Ejecutivo", "Estado de Infraestructura", "Comparación de Modelos",
         "Predicciones", "Conclusiones"]
    )

    st.sidebar.divider()
    st.sidebar.markdown("### 📁 Archivos cargados")
    st.sidebar.success("comparacion_modelos.csv")
    st.sidebar.success("predicciones_random_forest.csv")
    st.sidebar.success("Big_data_dataset_transformado.csv")

    filtro_col = None
    filtro_val = None
    if datos_infra is not None:
        st.sidebar.divider()
        st.sidebar.markdown("### 🎯 Segmentar datos")
        segment_cols = ["status_label", "cpu_level", "memory_level",
                        "latency_level", "temperature_level", "pressure_level"]
        segment_cols = [c for c in segment_cols if c in datos_infra.columns]
        if segment_cols:
            filtro_col = st.sidebar.selectbox(
                "Columna", ["(Todos)"] + segment_cols, key="segment_col"
            )
            if filtro_col and filtro_col != "(Todos)":
                valores = sorted(datos_infra[filtro_col].dropna().unique().tolist())
                filtro_val = st.sidebar.selectbox("Valor", valores, key="segment_val")

    return seccion, filtro_col, filtro_val
