"""Módulo que importa todas las funciones desde src/ para mantener
la interfaz pública en dashboard.dashboard."""
import streamlit as st
from src.ui.estilos import estilos
from src.core.datos import carga_datos, validar_datos
from src.core.detectores import detectar_columna_prediccion, detectar_columna_modelo, detectar_columna_f1
from src.core.metricas import obtener_media, obtener_metricas
from src.ui.sidebar import sidebar
from src.ui.cabecera import cabecera
from src.pages.resumen_ejecutivo import resumen_ejecutivo
from src.pages.estado_infraestructura import estado_infraestructura
from src.pages.comparacion_modelos import comparacion_modelos
from src.pages.predicciones import predicciones as mostrar_predicciones
from src.core.conclusiones import conclusiones

def mostrar_dashboard():
    estilos()
    comparacion, predicciones, datos_infra = carga_datos()
    validar_datos(comparacion, predicciones, datos_infra)

    col_pred = detectar_columna_prediccion(predicciones)
    col_modelo = detectar_columna_modelo(comparacion)
    col_f1 = detectar_columna_f1(comparacion)

    seccion, filtro_col, filtro_val = sidebar(datos_infra)

    if filtro_col and filtro_val:
        datos_infra_filt = datos_infra[datos_infra[filtro_col] == filtro_val].copy()
    else:
        datos_infra_filt = datos_infra

    cpu_media, _ = obtener_media(datos_infra_filt, ["cpu_utilization", "cpu_utilization_norm", "cpu_level"])
    memoria_media, _ = obtener_media(datos_infra_filt, ["memory_usage", "memory_usage_norm", "memory_level"])
    temperatura_media, _ = obtener_media(datos_infra_filt, ["temperature", "temperature_norm", "temperature_level"])
    latencia_media, _ = obtener_media(datos_infra_filt, ["network_latency", "network_latency_norm"])

    def _nivel_por_valor(metrica_col, nivel_col, valor):
        if valor == "N/D" or nivel_col not in datos_infra_filt.columns:
            return None
        grupos = datos_infra_filt.groupby(nivel_col)[metrica_col].agg(["min", "max"])
        for nivel, row in grupos.iterrows():
            if row["min"] <= valor <= row["max"]:
                return str(nivel)
        return None

    cpu_nivel = _nivel_por_valor("cpu_utilization", "cpu_level", cpu_media)
    memoria_nivel = _nivel_por_valor("memory_usage", "memory_level", memoria_media)
    temperatura_nivel = _nivel_por_valor("temperature", "temperature_level", temperatura_media)
    latencia_nivel = _nivel_por_valor("network_latency", "latency_level", latencia_media)

    metricas_preferidas = [
        "cpu_utilization", "memory_usage", "temperature", "network_latency",
        "disk_io", "power_consumption", "cpu_utilization_norm", "memory_usage_norm",
        "temperature_norm", "network_latency_norm", "disk_io_norm",
        "power_consumption_norm", "system_pressure_score", "status"
    ]
    metricas_disponibles = obtener_metricas(datos_infra_filt, metricas_preferidas)
    cabecera()

    total_datos = len(datos_infra) if datos_infra is not None else None
    total_incidentes_reales = int((datos_infra["status"] == 1).sum()) if datos_infra is not None and "status" in datos_infra.columns else None
    resumen_ejecutivo(seccion, predicciones, comparacion, col_pred, col_f1, col_modelo,
                      cpu_media, memoria_media, temperatura_media, latencia_media,
                      cpu_nivel, memoria_nivel, temperatura_nivel, latencia_nivel,
                      total_datos=total_datos, total_incidentes_reales=total_incidentes_reales)
    estado_infraestructura(seccion, datos_infra_filt, metricas_disponibles)
    comparacion_modelos(seccion, comparacion, col_modelo, col_f1)
    mostrar_predicciones(seccion, predicciones, col_pred)
    conclusiones(seccion)

    st.markdown("---")
    st.markdown(
        "<div style='text-align:center; font-size:13px; color:#6b7280;' "
        "title='Este proyecto se distribuye bajo licencia MIT. Consulte el archivo LICENCE.md para más detalles.'>"
        "<b>Predictive IT Infrastructure Analytics</b> | "
        "Licencia MIT ⓘ | Desarrollado por Ing. Randy Bonucci Martin"
        "</div>",
        unsafe_allow_html=True,
    )


__all__ = ["mostrar_dashboard"]