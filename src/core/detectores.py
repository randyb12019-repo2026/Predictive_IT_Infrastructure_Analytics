def detectar_columna_prediccion(df):
    posibles = ["prediccion", "prediction", "y_pred", "predicted_status", "status_predicho", "Prediccion"]
    for col in df.columns:
        if col.lower() in [p.lower() for p in posibles]:
            return col
    return None


def detectar_columna_modelo(df):
    posibles = ["Modelo", "model", "modelo", "Model"]
    for col in df.columns:
        if col in posibles:
            return col
    return df.columns[0]


def detectar_columna_f1(df):
    posibles = ["F1-Score", "F1 Score", "F1_Score", "f1_score", "f1-score"]
    for col in df.columns:
        if col in posibles:
            return col
    return None
