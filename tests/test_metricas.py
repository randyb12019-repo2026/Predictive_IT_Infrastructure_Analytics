import pandas as pd
from src.metricas import obtener_media, obtener_metricas


def test_obtener_media_columna_existente():
    df = pd.DataFrame({"cpu_utilization": [10, 20, 30]})
    resultado, col = obtener_media(df, ["cpu_utilization"])
    assert resultado == 20.0
    assert col == "cpu_utilization"


def test_obtener_media_primera_columna_valida():
    df = pd.DataFrame({"a": [1.0, 2.0], "b": [3.0, 4.0]})
    resultado, col = obtener_media(df, ["a", "b"])
    assert resultado == 1.5
    assert col == "a"


def test_obtener_media_saltar_columna_inexistente():
    df = pd.DataFrame({"b": [2.0, 4.0]})
    resultado, col = obtener_media(df, ["a", "b"])
    assert resultado == 3.0
    assert col == "b"


def test_obtener_media_sin_columnas():
    df = pd.DataFrame({"a": [1, 2]})
    resultado, col = obtener_media(df, ["z", "y"])
    assert resultado == "N/D"
    assert col is None


def test_obtener_media_df_vacio():
    df = pd.DataFrame()
    resultado, col = obtener_media(df, ["a"])
    assert resultado == "N/D"
    assert col is None


def test_obtener_media_con_norm():
    df = pd.DataFrame({"cpu_utilization_norm": [0.1, 0.2, 0.3]})
    resultado, col = obtener_media(df, ["cpu_utilization", "cpu_utilization_norm", "cpu_level"])
    assert resultado == 0.2
    assert col == "cpu_utilization_norm"


def test_obtener_metricas_todas_disponibles():
    df = pd.DataFrame({"a": [1], "b": [2], "c": [3]})
    preferidas = ["a", "b", "c"]
    resultado = obtener_metricas(df, preferidas)
    assert resultado == ["a", "b", "c"]


def test_obtener_metricas_algunas_disponibles():
    df = pd.DataFrame({"a": [1], "c": [3]})
    preferidas = ["a", "b", "c"]
    resultado = obtener_metricas(df, preferidas)
    assert resultado == ["a", "c"]


def test_obtener_metricas_ninguna_disponible():
    df = pd.DataFrame({"x": [1], "y": [2]})
    preferidas = ["a", "b"]
    resultado = obtener_metricas(df, preferidas)
    assert resultado == ["x", "y"]


def test_obtener_metricas_df_vacio():
    df = pd.DataFrame()
    resultado = obtener_metricas(df, ["a"])
    assert resultado == []


def test_obtener_metricas_con_columnas_no_numericas_en_preferidas():
    df = pd.DataFrame({"a": [1], "b": ["texto"], "c": [3.0]})
    preferidas = ["a", "b", "c"]
    resultado = obtener_metricas(df, preferidas)
    assert resultado == ["a", "b", "c"]
