import streamlit as st
import pandas as pd
import plotly.express as px


def resumen_ejecutivo(seccion, predicciones, comparacion, col_pred, col_f1, col_modelo,
                      cpu_media, memoria_media, temperatura_media, latencia_media,
                      cpu_nivel=None, memoria_nivel=None, temperatura_nivel=None,
                      latencia_nivel=None):
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

    niveles_emoji = {
        "Low": "🟢 Bajo", "Medium": "🟡 Medio", "High": "🟠 Alto",
        "Warning": "⚠️ Advertencia", "Critical": "🔴 Crítico",
        "Normal": "✅ Normal", "Incident": "🚨 Incidente",
    }

    col5, col6, col7, col8 = st.columns(4)
    col5.metric("🤖 Mejor Modelo", nombre_modelo)
    col6.metric("📈 F1-Score", f1_score)
    col7.metric("⚙️ CPU Media", cpu_media)
    col8.metric("💾 Memoria Media", memoria_media)

    col9, col10 = st.columns(2)
    col9.metric("🔥 Temperatura Media", temperatura_media)
    col10.metric("🌐 Latencia Media", latencia_media)

    niveles_orden = {"Low": 0, "Medium": 1, "High": 2, "Warning": 2, "Critical": 3, "Normal": 0, "Incident": 3}
    niveles_etiqueta = {"Low": "🟢 Bajo", "Medium": "🟡 Medio", "High": "🟠 Alto",
                        "Warning": "⚠️ Advertencia", "Critical": "🔴 Crítico",
                        "Normal": "✅ Normal", "Incident": "🚨 Incidente"}
    niveles_por_kpi = [
        ("CPU", cpu_nivel),
        ("Memoria", memoria_nivel),
        ("Temperatura", temperatura_nivel),
        ("Latencia", latencia_nivel),
    ]
    niveles_por_kpi.sort(key=lambda x: niveles_orden.get(x[1], -1) if x[1] else -1, reverse=True)
    cols_n = st.columns(4)
    for i, (nombre, nivel) in enumerate(niveles_por_kpi):
        if nivel:
            cols_n[i].markdown(f"**{nombre}**: {niveles_etiqueta.get(nivel, nivel)}")

    df_barras = pd.DataFrame([
        {"Métrica": "CPU", "Valor": cpu_media, "Nivel": cpu_nivel},
        {"Métrica": "Memoria", "Valor": memoria_media, "Nivel": memoria_nivel},
        {"Métrica": "Temperatura", "Valor": temperatura_media, "Nivel": temperatura_nivel},
        {"Métrica": "Latencia", "Valor": latencia_media, "Nivel": latencia_nivel},
    ])
    color_map = {"Low": "#22c55e", "Medium": "#eab308", "High": "#f97316",
                 "Warning": "#f97316", "Critical": "#ef4444",
                 "Normal": "#22c55e", "Incident": "#ef4444"}
    df_barras["Color"] = df_barras["Nivel"].map(color_map)
    fig = px.bar(df_barras, x="Métrica", y="Valor", color="Nivel",
                 color_discrete_map=color_map, text_auto=".1f",
                 title="📊 Métricas del sistema por nivel de alerta")
    fig.update_layout(template="plotly_dark", paper_bgcolor="#111827", plot_bgcolor="#111827",
                      showlegend=True, xaxis_title="", yaxis_title="Valor promedio")
    fig.update_traces(textposition="outside", marker_line_width=0)
    st.plotly_chart(fig, width='stretch')

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

    st.subheader("🤖 Comparación de modelos")
    st.dataframe(comparacion, width='stretch')
    st.markdown("""
    <style>
    .info-box {
        background:#0f172a; padding:10px 15px; border-radius:8px; font-size:13px;
        border-left:3px solid #2E86C1; margin:8px 0;
    }
    </style>
    <div class="info-box">
    <b>📖 Significado de las métricas</b><br>
    • <b>Accuracy</b> — Porcentaje total de aciertos del modelo.<br>
    • <b>Precision</b> — De lo que predijo como incidente, cuántos realmente lo eran.<br>
    • <b>Recall</b> — De los incidentes reales, cuántos logró detectar el modelo.<br>
    • <b>F1-Score</b> — Media armónica entre Precision y Recall. Es la métrica principal
    porque equilibra ambas. Un F1 cercano a <b>1.0</b> indica detección precisa sin falsas alarmas.
    </div>
    """, unsafe_allow_html=True)

    st.subheader("🚨 Incidentes detectados por el modelo")
    if len(incidentes_df) > 0:
        cols_mostrar = ["cpu_utilization", "memory_usage", "temperature", "network_latency"]
        cols_reales = ["Valor_Real", "valor_real", "Real", "real", "y_test", "y_real"]
        col_real = next((c for c in predicciones.columns if c in cols_reales), None)
        if col_real and col_pred:
            cols_mostrar = cols_mostrar + [col_real, col_pred]
            cols_mostrar = [c for c in cols_mostrar if c in incidentes_df.columns]
            if cols_mostrar:
                df_vista = incidentes_df[cols_mostrar].head(10).copy()
                df_vista.columns = ["CPU (%)", "Memoria (%)", "Temperatura (°C)", "Latencia (ms)",
                                    "Estado Real", "Predicción"]
                df_vista["Estado Real"] = df_vista["Estado Real"].replace({0: "✅ Normal", 1: "🚨 Incidente"})
                df_vista["Predicción"] = df_vista["Predicción"].replace({0: "✅ Normal", 1: "🚨 Incidente"})
                st.dataframe(df_vista, width='stretch')
                st.markdown("""
                <div class="info-box">
                <b>🔍 Cómo leer esta tabla</b><br>
                • <b>CPU / Memoria / Temperatura / Latencia</b> — Valores del sistema en el instante evaluado.<br>
                • <b>Estado Real</b> — Lo que realmente ocurrió (etiqueta real del dataset).<br>
                • <b>Predicción</b> — Lo que el modelo pronosticó.<br><br>
                Presta atención cuando <b>Estado Real</b> y <b>Predicción</b> no coinciden:
                ahí hay falsos positivos (alarma sin incidente real) o falsos negativos
                (incidente no detectado).
                </div>
                """, unsafe_allow_html=True)
        else:
            st.dataframe(incidentes_df.head(10), width='stretch')
    else:
        st.success("No se detectaron incidencias.")
