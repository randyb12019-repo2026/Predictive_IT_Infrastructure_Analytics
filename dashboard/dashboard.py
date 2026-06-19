"""Módulo que importa todas las funciones desde src/ para mantener
la interfaz pública en dashboard.dashboard."""
from src.estilos import estilos
from src.datos import carga_datos, validar_datos
from src.detectores import detectar_columna_prediccion, detectar_columna_modelo, detectar_columna_f1
from src.metricas import obtener_media, obtener_metricas
from src.sidebar import sidebar
from src.cabecera import cabecera
from src.resumen_ejecutivo import resumen_ejecutivo
from src.estado_infraestructura import estado_infraestructura
from src.comparacion_modelos import comparacion_modelos
from src.predicciones import predicciones as mostrar_predicciones
from src.conclusiones import conclusiones

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

    metricas_preferidas = [
        "cpu_utilization", "memory_usage", "temperature", "network_latency",
        "disk_io", "power_consumption", "cpu_utilization_norm", "memory_usage_norm",
        "temperature_norm", "network_latency_norm", "disk_io_norm",
        "power_consumption_norm", "system_pressure_score"
    ]
    metricas_disponibles = obtener_metricas(datos_infra_filt, metricas_preferidas)
    cabecera()

    resumen_ejecutivo(seccion, predicciones, comparacion, col_pred, col_f1, col_modelo,
                      cpu_media, memoria_media, temperatura_media, latencia_media)
    estado_infraestructura(seccion, datos_infra_filt, metricas_disponibles)
    comparacion_modelos(seccion, comparacion, col_modelo, col_f1)
    mostrar_predicciones(seccion, predicciones, col_pred)
    conclusiones(seccion)


__all__ = ["mostrar_dashboard"]