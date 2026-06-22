import streamlit as st
import pandas as pd
import plotly.express as px


def estado_infraestructura(seccion, datos_infra, metricas_disponibles):
    if seccion != "Estado de Infraestructura":
        return

    st.header("🖥️ Estado de Infraestructura IT")
    if not metricas_disponibles:
        st.warning("No se encontraron columnas numéricas en el dataset transformado.")
        return

    metricas_analisis = [c for c in metricas_disponibles
                         if not c.endswith("_norm") and not c.endswith("_level")]
    if not metricas_analisis:
        metricas_analisis = metricas_disponibles

    st.markdown("### 📌 Indicadores operativos")
    cols = st.columns(min(len(metricas_analisis), 4))
    for i, metrica in enumerate(metricas_analisis[:4]):
        cols[i].metric(metrica.replace("_", " ").title(), round(datos_infra[metrica].mean(), 2))

    st.markdown("""
    <style>
    .kpi-legend { display:grid; grid-template-columns:1fr 1fr; gap:2px 20px;
        background:#1e293b; padding:8px 15px; border-radius:8px; margin:5px 0 15px 0; font-size:12px; }
    </style>
    <div class="kpi-legend">
    <div><b>⚙️ CPU Utilization</b> → Porcentaje de uso del procesador</div>
    <div><b>💾 Memory Usage</b> → Porcentaje de memoria RAM en uso</div>
    <div><b>🌡️ Temperature</b> → Temperatura del sistema en °C</div>
    <div><b>🌐 Network Latency</b> → Tiempo de respuesta de red en ms</div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("### 📈 Distribución de métricas")
    metrica_sel = st.selectbox("Selecciona una métrica para analizar:", metricas_analisis)

    fig = px.histogram(
        datos_infra, x=metrica_sel, nbins=40,
        title=f"Distribución de {metrica_sel.replace('_', ' ').title()}"
    )
    fig.update_traces(texttemplate="%{y}", textposition="outside")
    fig.update_layout(template="plotly_dark", paper_bgcolor="#111827", plot_bgcolor="#111827")
    st.plotly_chart(fig, width='stretch')

    st.markdown("### 📊 Estadísticas descriptivas")
    st.dataframe(datos_infra[metricas_analisis].describe().T, width='stretch')

    st.markdown("### 📖 Significado de las estadísticas")
    st.markdown("""
    <style>
    .stats-legend { display:grid; grid-template-columns:1fr; gap:4px;
        background:#1e293b; padding:12px 18px; border-radius:8px; margin:10px 0; font-size:13px; }
    </style>
    <div class="stats-legend">
    <div><b>count</b> → Recuento: cantidad total de mediciones registradas. A más datos, más representativa es la muestra.</div>
    <div><b>mean</b> → Media: promedio aritmético de todos los valores. Indica el comportamiento típico del sistema.</div>
    <div><b>std</b> → Desviación estándar: mide cuánto se dispersan los datos respecto al promedio. Bajo = valores estables y predecibles. Alto = valores muy variables e irregulares. No es lo mismo que la varianza, pero sí es su raíz cuadrada.</div>
    <div><b>min</b> → Mínimo: el valor más pequeño registrado. Representa el momento de menor carga o mejor rendimiento.</div>
    <div><b>25%</b> → Primer cuartil (Q1): el 25% de las mediciones están por debajo de este valor. El 75% restante está por encima.</div>
    <div><b>50%</b> → Mediana: valor que divide los datos en dos mitades iguales. El 50% está por debajo y el 50% por encima. A diferencia de la media, no se ve afectada por valores extremos.</div>
    <div><b>75%</b> → Tercer cuartil (Q3): el 75% de las mediciones están por debajo de este valor. El 25% restante lo supera.</div>
    <div><b>max</b> → Máximo: el valor más grande registrado. Representa el pico máximo de carga o el peor escenario.</div>
    </div>
    <div style="background:#0f172a; padding:10px 15px; border-radius:8px; margin:10px 0; font-size:13px; border-left:3px solid #2E86C1;">
    <b>🧑‍💼 Ejemplo para un gerente:</b><br>
    <b>mean=52%</b> → el servidor usa 52% de CPU en promedio. <br>
    <b>max=99%</b> → pero hubo un pico al 99% (riesgo de saturación). <br>
    <b>std=25</b> → los valores varían mucho, el rendimiento es impredecible. <br>
    <b>75%=74%</b> → el 25% del tiempo la CPU supera el 74%. Es decir, 1 de cada 4 mediciones está cerca del límite.
    </div>
    """, unsafe_allow_html=True)

    st.markdown("### 📖 Significado de las variables")
    leyenda = {
        "cpu_utilization": "Uso de CPU (%)",
        "memory_usage": "Uso de memoria (%)",
        "temperature": "Temperatura del sistema (°C)",
        "network_latency": "Latencia de red (ms)",
        "disk_io": "Operaciones de disco (IOPS)",
        "power_consumption": "Consumo energético (W)",
        "context_switches": "Cambios de contexto por segundo",
        "uptime": "Tiempo de actividad del sistema",
        "system_pressure_score": "Indicador compuesto de presión del sistema",
        "cpu_level": "Nivel de CPU (Low/Medium/High)",
        "memory_level": "Nivel de memoria (Low/Medium/High)",
        "temperature_level": "Nivel de temperatura (Normal/Warning/Critical)",
        "latency_level": "Nivel de latencia (Low/Medium/High)",
        "pressure_level": "Nivel de presión (Low/Medium/High)",
    }
    items_visibles = [(col, desc) for col, desc in leyenda.items() if col in metricas_disponibles]
    if items_visibles:
        cols_var = st.columns(3)
        for i, (col, desc) in enumerate(items_visibles):
            cols_var[i % 3].markdown(f"**{col}**: {desc}")

    st.markdown("### 🚦 Umbrales de alerta por nivel")
    umbrales_map = {
        "cpu_utilization": "cpu_level",
        "memory_usage": "memory_level",
        "temperature": "temperature_level",
        "network_latency": "latency_level",
        "system_pressure_score": "pressure_level",
    }
    filas_umbrales = []
    for metrica, nivel_col in umbrales_map.items():
        if metrica in datos_infra.columns and nivel_col in datos_infra.columns:
            grupos = datos_infra.groupby(nivel_col)[metrica].agg(["min", "max", "mean", "count"])
            for nivel, row in grupos.iterrows():
                filas_umbrales.append({
                    "Métrica": metrica.replace("_", " ").title(),
                    "Nivel": str(nivel),
                    "Rango": f"{row['min']:.1f} - {row['max']:.1f}",
                    "Promedio": f"{row['mean']:.1f}",
                    "Registros": int(row["count"]),
                })
    if filas_umbrales:
        orden_nivel = {"Critical": 0, "High": 1, "Warning": 2, "Medium": 3, "Low": 4, "Normal": 5, "Incident": 0}
        nombres_nivel = {"Low": "🟢 Bajo", "Medium": "🟡 Medio", "High": "🟠 Alto",
                         "Warning": "⚠️ Advertencia", "Critical": "🔴 Crítico",
                         "Normal": "✅ Normal", "Incident": "🚨 Incidente"}
        df_umbrales = pd.DataFrame(filas_umbrales)
        df_umbrales["Orden"] = df_umbrales["Nivel"].map(orden_nivel)
        df_umbrales = df_umbrales.sort_values(["Métrica", "Orden"])
        metricas_unicas = df_umbrales["Métrica"].unique()
        cols = st.columns(len(metricas_unicas))
        for i, metrica in enumerate(metricas_unicas):
            with cols[i]:
                st.markdown(f"**{metrica}**")
                sub = df_umbrales[df_umbrales["Métrica"] == metrica]
                for _, row in sub.iterrows():
                    st.markdown(f"{nombres_nivel.get(row['Nivel'], row['Nivel'])}: {row['Rango']}")

    st.markdown("### 🔗 Matriz de correlaciones")
    corr_cols = [c for c in metricas_disponibles
                 if not c.endswith("_level") and not c.endswith("_norm")
                 and c != "status" and c != "status_label"]
    if len(corr_cols) > 1:
        corr_matrix = datos_infra[corr_cols].corr()
        fig_corr = px.imshow(
            corr_matrix, text_auto=".2f", color_continuous_scale="RdBu_r",
            title="Correlación entre variables del sistema",
            aspect="auto", width=700, height=600,
        )
        fig_corr.update_layout(
            template="plotly_dark", paper_bgcolor="#111827", plot_bgcolor="#111827",
        )
        st.plotly_chart(fig_corr, width='stretch')
        st.markdown("""
        <div style="background:#0f172a; padding:10px 15px; border-radius:8px; font-size:13px; border-left:3px solid #2E86C1;">
        <b>🔍 Cómo leerlo:</b> Cada celda muestra la correlación entre dos variables.
        <b>1.0</b> = correlación perfecta (suben juntas).
        <b>-1.0</b> = correlación inversa (una sube, otra baja).
        <b>0.0</b> = sin relación. Colores <span style="color:#d73027;">rojos</span> = correlación positiva,
        <span style="color:#4575b4;">azules</span> = correlación negativa.
        </div>
        """, unsafe_allow_html=True)
