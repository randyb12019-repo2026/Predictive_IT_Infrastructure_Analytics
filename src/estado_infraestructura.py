import streamlit as st
import plotly.express as px


def estado_infraestructura(seccion, datos_infra, metricas_disponibles):
    if seccion != "Estado de Infraestructura":
        return

    st.header("🖥️ Estado de Infraestructura IT")
    if not metricas_disponibles:
        st.warning("No se encontraron columnas numéricas en el dataset transformado.")
        return

    st.markdown("### 📌 Indicadores operativos")
    cols = st.columns(min(len(metricas_disponibles), 4))
    for i, metrica in enumerate(metricas_disponibles[:4]):
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
    metrica_sel = st.selectbox("Selecciona una métrica para analizar:", metricas_disponibles)

    fig = px.histogram(
        datos_infra, x=metrica_sel, nbins=40,
        title=f"Distribución de {metrica_sel.replace('_', ' ').title()}"
    )
    fig.update_traces(texttemplate="%{y}", textposition="outside")
    fig.update_layout(template="plotly_dark", paper_bgcolor="#111827", plot_bgcolor="#111827")
    st.plotly_chart(fig, use_container_width=True)

    st.markdown("### 📊 Estadísticas descriptivas")
    st.dataframe(datos_infra[metricas_disponibles].describe().T, use_container_width=True)

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
    Si CPU tiene <b>mean=52%</b> y <b>max=99%</b>, en promedio el servidor opera al 52%,
    pero en algún momento llegó al 99% (riesgo de saturación). Si el <b>std</b> es alto (ej. 25),
    el rendimiento es <b>impredecible</b> — hay que revisar. Si el <b>75%</b> está en 74%,
    1 de cada 4 mediciones supera el 74% de CPU, lo cual indica que el servidor está
    cerca de sus límites con frecuencia.
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
    for col, desc in leyenda.items():
        if col in metricas_disponibles:
            st.markdown(f"- **{col}**: {desc}")
