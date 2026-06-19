def obtener_media(df, posibles_columnas):
    for col in posibles_columnas:
        if col in df.columns:
            return round(df[col].mean(), 2), col
    return "N/D", None


def obtener_metricas(datos_infra, metricas_preferidas):
    metricas_disponibles = [col for col in metricas_preferidas if col in datos_infra.columns]
    if not metricas_disponibles:
        metricas_disponibles = datos_infra.select_dtypes(include="number").columns.tolist()
    return metricas_disponibles
