import streamlit as st
import pandas as pd


def resumen_ejecutivo(seccion, predicciones, comparacion, col_pred, col_f1, col_modelo,
                      cpu_media, memoria_media, temperatura_media, latencia_media):
    if seccion != "Resumen Ejecutivo":
        return

    st.header("📊 Resumen Ejecutivo del Sistema")
    st.markdown("""
        <style>
        [data-testid="metric-container"] > div > div {
            font-size: 1.1rem !important;
        }
        </style>
    """, unsafe_allow_html=True)
    total_registros = len(predicciones)

    if col_pred:
        incidentes = int((predicciones[col_pred] == 1).sum())
        normales = int((predicciones[col_pred] == 0).sum())
        porcentaje_incidentes = round((incidentes / total_registros) * 100, 2)
        incidentes_df = predicciones[predicciones[col_pred] == 1]
    else:
        incidentes = normales = porcentaje_incidentes = "N/D"
        incidentes_df = pd.DataFrame()

    if col_f1:
        mejor_modelo = comparacion.loc[comparacion[col_f1].idxmax()]
        nombre_modelo = mejor_modelo[col_modelo]
        f1_score = round(mejor_modelo[col_f1], 3)
    else:
        nombre_modelo = f1_score = "N/D"

    st.markdown("### 🔑 KPIs principales")
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("🖥️ Registros Analizados", total_registros)
    col2.metric("✅ Registros Normales", normales)
    col3.metric("🚨 Incidentes Detectados", incidentes)
    col4.metric("📉 % de Incidentes", f"{porcentaje_incidentes}%")

    col5, col6, col7, col8 = st.columns(4)
    col5.metric("🤖 Mejor Modelo", nombre_modelo)
    col6.metric("📈 F1-Score", f1_score)
    col7.metric("⚙️ CPU Media", cpu_media)
    col8.metric("💾 Memoria Media", memoria_media)

    col9, col10 = st.columns(2)
    col9.metric("🔥 Temperatura Media", temperatura_media)
    col10.metric("🌐 Latencia Media", latencia_media)

    st.markdown("""
    <style>
    .kpi-legend {
        background:#1e293b; padding:10px 15px; border-radius:8px; margin:10px 0; font-size:12px;
        display:grid; grid-template-columns:1fr 1fr 1fr; gap:4px 15px;
    }
    </style>
    <div class="kpi-legend">
    <div><b>🖥️ Registros Analizados</b> → Total procesado</div>
    <div><b>✅ Registros Normales</b> → Operación normal</div>
    <div><b>🚨 Incidentes Detectados</b> → Posible incidente</div>
    <div><b>📉 % de Incidentes</b> → % sobre el total</div>
    <div><b>🤖 Mejor Modelo</b> → Mayor F1-Score</div>
    <div><b>📈 F1-Score</b> → Precisión + Recall</div>
    <div><b>⚙️ CPU Media</b> → Promedio de CPU</div>
    <div><b>💾 Memoria Media</b> → Promedio de memoria</div>
    <div><b>🔥 Temperatura Media</b> → Promedio de temperatura</div>
    <div><b>🌐 Latencia Media</b> → Promedio de latencia</div>
    </div>
    """, unsafe_allow_html=True)

    if col_pred and incidentes != "N/D":
        st.markdown(f"""
        <div class="alert-card">
        El sistema analizó <b>{total_registros}</b> registros de infraestructura IT.
        El modelo identificó <b>{incidentes}</b> posibles incidencias frente a
        <b>{normales}</b> registros normales, lo que representa un
        <b>{porcentaje_incidentes}%</b> del total.
        </div>
        """, unsafe_allow_html=True)

    if col_pred:
        st.markdown(f"""
        <div class="alert-card">
        <h3>🚨 Incidencias detectadas: {len(incidentes_df)}</h3>
        <p>Registros clasificados por el modelo como posibles incidentes.</p>
        </div>
        """, unsafe_allow_html=True)

    col_a, col_b = st.columns(2)
    with col_a:
        st.subheader("🤖 Comparación de modelos")
        st.dataframe(comparacion, use_container_width=True)
    with col_b:
        st.subheader("🚨 Incidentes detectados por el modelo")
        if len(incidentes_df) > 0:
            st.dataframe(incidentes_df.head(10), use_container_width=True)
        else:
            st.success("No se detectaron incidencias.")
