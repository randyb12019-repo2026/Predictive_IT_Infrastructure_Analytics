from src.core.conclusiones import TEXTOS_CONCLUSIONES


def test_textos_conclusiones_no_vacio():
    assert len(TEXTOS_CONCLUSIONES) > 0


def test_textos_conclusiones_estructura():
    for titulo, cuerpo in TEXTOS_CONCLUSIONES:
        assert isinstance(titulo, str)
        assert isinstance(cuerpo, str)
        assert len(titulo) > 0
        assert len(cuerpo) > 0


def test_textos_conclusiones_cantidad():
    assert len(TEXTOS_CONCLUSIONES) == 6


def test_textos_conclusiones_titulos_esperados():
    titulos = [t for t, _ in TEXTOS_CONCLUSIONES]
    assert "1. Preparación y Transformación de los Datos" in titulos
    assert "2. Análisis Exploratorio de Datos" in titulos
    assert "3. Modelo Predictivo" in titulos
    assert "4. Resultados Obtenidos" in titulos
    assert "5. Aplicación Práctica" in titulos
    assert "6. Trabajo Futuro" in titulos
