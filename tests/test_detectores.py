import pandas as pd
from src.core.detectores import detectar_columna_prediccion, detectar_columna_modelo, detectar_columna_f1


def test_detectar_columna_prediccion_prediccion():
    df = pd.DataFrame({"prediccion": [0, 1]})
    assert detectar_columna_prediccion(df) == "prediccion"


def test_detectar_columna_prediccion_prediction():
    df = pd.DataFrame({"prediction": [0, 1]})
    assert detectar_columna_prediccion(df) == "prediction"


def test_detectar_columna_prediccion_y_pred():
    df = pd.DataFrame({"y_pred": [0, 1]})
    assert detectar_columna_prediccion(df) == "y_pred"


def test_detectar_columna_prediccion_predicted_status():
    df = pd.DataFrame({"predicted_status": [0, 1]})
    assert detectar_columna_prediccion(df) == "predicted_status"


def test_detectar_columna_prediccion_status_predicho():
    df = pd.DataFrame({"status_predicho": [0, 1]})
    assert detectar_columna_prediccion(df) == "status_predicho"


def test_detectar_columna_prediccion_Prediccion():
    df = pd.DataFrame({"Prediccion": [0, 1]})
    assert detectar_columna_prediccion(df) == "Prediccion"


def test_detectar_columna_prediccion_sin_coincidencia():
    df = pd.DataFrame({"otra_columna": [0, 1]})
    assert detectar_columna_prediccion(df) is None


def test_detectar_columna_prediccion_vacia():
    df = pd.DataFrame()
    assert detectar_columna_prediccion(df) is None


def test_detectar_columna_modelo_Modelo():
    df = pd.DataFrame({"Modelo": ["A", "B"]})
    assert detectar_columna_modelo(df) == "Modelo"


def test_detectar_columna_modelo_model():
    df = pd.DataFrame({"model": ["A", "B"]})
    assert detectar_columna_modelo(df) == "model"


def test_detectar_columna_modelo_modelo():
    df = pd.DataFrame({"modelo": ["A", "B"]})
    assert detectar_columna_modelo(df) == "modelo"


def test_detectar_columna_modelo_Model():
    df = pd.DataFrame({"Model": ["A", "B"]})
    assert detectar_columna_modelo(df) == "Model"


def test_detectar_columna_modelo_sin_coincidencia():
    df = pd.DataFrame({"algo": [1, 2]})
    assert detectar_columna_modelo(df) == "algo"


def test_detectar_columna_f1_F1_Score():
    df = pd.DataFrame({"F1-Score": [0.5, 0.9]})
    assert detectar_columna_f1(df) == "F1-Score"


def test_detectar_columna_f1_F1_Score_espacio():
    df = pd.DataFrame({"F1 Score": [0.5, 0.9]})
    assert detectar_columna_f1(df) == "F1 Score"


def test_detectar_columna_f1_F1_Score_guion_bajo():
    df = pd.DataFrame({"F1_Score": [0.5, 0.9]})
    assert detectar_columna_f1(df) == "F1_Score"


def test_detectar_columna_f1_f1_score():
    df = pd.DataFrame({"f1_score": [0.5, 0.9]})
    assert detectar_columna_f1(df) == "f1_score"


def test_detectar_columna_f1_f1_score_guion():
    df = pd.DataFrame({"f1-score": [0.5, 0.9]})
    assert detectar_columna_f1(df) == "f1-score"


def test_detectar_columna_f1_sin_coincidencia():
    df = pd.DataFrame({"accuracy": [0.9]})
    assert detectar_columna_f1(df) is None


def test_detectar_columna_f1_vacia():
    df = pd.DataFrame()
    assert detectar_columna_f1(df) is None
