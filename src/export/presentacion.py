"""
Generación de PDF del proyecto Predictive IT Infrastructure Analytics.
"""
import os
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent.parent))
import pandas as pd
from src.core.conclusiones import TEXTOS_CONCLUSIONES

PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent
from reportlab.lib.pagesizes import landscape, letter
from reportlab.lib.units import inch
from reportlab.lib.colors import HexColor
from reportlab.pdfgen import canvas
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import Paragraph, Table, TableStyle
from reportlab.lib.enums import TA_CENTER, TA_LEFT
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

# Colores corporativos
AZUL_OSCURO  = HexColor("#1B3A5C")
AZUL_CLARO   = HexColor("#2E86C1")
BLANCO       = HexColor("#FFFFFF")
GRIS         = HexColor("#D0D0D0")
VERDE        = HexColor("#27AE60")
ROJO         = HexColor("#E74C3C")
NARANJA      = HexColor("#F39C12")
FONDO_CLARO  = HexColor("#F0F4F8")

PAGE_W, PAGE_H = landscape(letter)  # 11 x 8.5 in
MARGIN = 0.8 * inch
CONTENT_W = PAGE_W - 2 * MARGIN


def _draw_bg(c, color=AZUL_OSCURO):
    c.setFillColor(color)
    c.rect(0, 0, PAGE_W, PAGE_H, fill=1, stroke=0)


def _draw_accent_bar(c, y, color=AZUL_CLARO):
    c.setFillColor(color)
    c.rect(MARGIN, y, CONTENT_W, 4, fill=1, stroke=0)


def _draw_title(c, text, y, size=28, color=BLANCO):
    c.setFillColor(color)
    c.setFont("Helvetica-Bold", size)
    c.drawString(MARGIN, y, text)
    _draw_accent_bar(c, y - 12)


def _draw_text(c, text, x, y, size=16, color=BLANCO, bold=False, max_width=None, leading=None):
    c.setFillColor(color)
    c.setFont("Helvetica-Bold" if bold else "Helvetica", size)
    lh = leading or (size * 1.4)
    cy = y
    for paragraph in text.split("\n"):
        if max_width:
            words = paragraph.split(" ")
            line = ""
            for w in words:
                test = f"{line} {w}".strip()
                if c.stringWidth(test, "Helvetica-Bold" if bold else "Helvetica", size) > max_width:
                    c.drawString(x, cy, line)
                    cy -= lh
                    line = w
                else:
                    line = test
            if line:
                c.drawString(x, cy, line)
                cy -= lh
        else:
            c.drawString(x, cy, paragraph)
            cy -= lh
    return cy


def _draw_bullets(c, items, x, y, size=14, color=BLANCO, max_width=None):
    c.setFillColor(color)
    c.setFont("Helvetica", size)
    lh = size * 1.5
    cy = y
    for item in items:
        text = f"\u2022 {item}"
        if max_width and c.stringWidth(text, "Helvetica", size) > max_width:
            cy = _draw_text(c, text, x, cy, size, color, max_width=max_width, leading=lh)
            cy -= lh
        else:
            c.drawString(x, cy, text)
            cy -= lh
    return cy


def _draw_table(c, data, x, y, col_widths=None):
    rows, cols = len(data), len(data[0])
    if col_widths is None:
        col_widths = [CONTENT_W / cols] * cols
    row_height = 24
    table_w = sum(col_widths)
    table_h = rows * row_height

    # Header row
    c.setFillColor(AZUL_CLARO)
    c.rect(x, y - row_height, table_w, row_height, fill=1, stroke=0)
    for j, val in enumerate(data[0]):
        cx = x + sum(col_widths[:j])
        c.setFillColor(BLANCO)
        c.setFont("Helvetica-Bold", 11)
        c.drawString(cx + 4, y - row_height + 7, str(val))

    # Data rows
    for i in range(1, rows):
        ry = y - (i + 1) * row_height
        c.setFillColor(BLANCO)
        c.rect(x, ry, table_w, row_height, fill=1, stroke=0)
        c.setStrokeColor(HexColor("#D0D7DE"))
        c.setLineWidth(0.5)
        c.rect(x, ry, table_w, row_height, fill=0, stroke=1)
        for j, val in enumerate(data[i]):
            cx = x + sum(col_widths[:j])
            c.setFillColor(AZUL_OSCURO)
            c.setFont("Helvetica", 11)
            c.drawString(cx + 4, ry + 7, str(val))

    return y - rows * row_height


# === DECORACIONES IT / SEGURIDAD ===

def _draw_shield(c, cx, cy, size=60, color=AZUL_CLARO):
    """Dibuja un escudo estilizado."""
    s = size
    c.setStrokeColor(color)
    c.setLineWidth(2)
    # Escudo (sin relleno, solo contorno)
    p = c.beginPath()
    p.moveTo(cx, cy + s)
    p.lineTo(cx - s, cy + s * 0.3)
    p.lineTo(cx - s * 0.7, cy - s * 0.5)
    p.lineTo(cx, cy - s * 0.8)
    p.lineTo(cx + s * 0.7, cy - s * 0.5)
    p.lineTo(cx + s, cy + s * 0.3)
    p.close()
    c.drawPath(p, fill=0, stroke=1)
    # Checkmark interno
    c.setStrokeColor(color)
    c.setLineWidth(3)
    c.line(cx - s * 0.3, cy - s * 0.1, cx - s * 0.1, cy + s * 0.2)
    c.line(cx - s * 0.1, cy + s * 0.2, cx + s * 0.4, cy - s * 0.3)


def _draw_circuit_lines(c, x, y, count=3, spacing=20, color=AZUL_CLARO):
    """Dibuja lineas decorativas tipo circuito."""
    c.setStrokeColor(color)
    c.setLineWidth(1)
    for i in range(count):
        cy = y - i * spacing
        c.line(x, cy, x + 30, cy)
        c.line(x + 30, cy, x + 30, cy - spacing // 2)
        c.circle(x + 30, cy - spacing // 2, 2, fill=1, stroke=0)


def _draw_footer(c, text="Predictive IT Infrastructure Analytics"):
    c.setFillColor(GRIS)
    c.setFont("Helvetica", 8)
    c.drawString(MARGIN, 0.3 * inch, text)
    c.drawRightString(PAGE_W - MARGIN, 0.3 * inch, "Confidencial")


# ============================================================
# SLIDE DRAWERS
# ============================================================

def _slide_01_portada(c):
    _draw_bg(c)
    # Circuit decorations
    _draw_circuit_lines(c, MARGIN, PAGE_H - 1.3 * inch, 4, 25, AZUL_CLARO)
    _draw_circuit_lines(c, PAGE_W - MARGIN - 30, PAGE_H - 1.3 * inch, 4, 25, AZUL_CLARO)
    # Shield
    _draw_shield(c, PAGE_W / 2, PAGE_H - 2.2 * inch, 80, AZUL_CLARO)
    # Title
    c.setFillColor(BLANCO)
    c.setFont("Helvetica-Bold", 36)
    c.drawCentredString(PAGE_W / 2, PAGE_H - 3.5 * inch,
                        "Predictive IT Infrastructure Analytics")
    c.setFillColor(AZUL_CLARO)
    c.setFont("Helvetica", 18)
    c.drawCentredString(PAGE_W / 2, PAGE_H - 4.2 * inch,
                        "Deteccion temprana de incidentes en infraestructuras IT")
    c.drawCentredString(PAGE_W / 2, PAGE_H - 4.6 * inch,
                        "mediante Machine Learning")
    # Subtitle
    c.setFillColor(GRIS)
    c.setFont("Helvetica", 14)
    c.drawCentredString(PAGE_W / 2, PAGE_H - 5.5 * inch,
                        "Analisis  ·  Transformacion  ·  Modelado Predictivo")
    # Author
    c.setFillColor(GRIS)
    c.setFont("Helvetica", 12)
    c.drawCentredString(PAGE_W / 2, PAGE_H - 6.3 * inch,
                        "Autor: Ing. Randy Bonucci Martin")
    c.setFillColor(GRIS)
    c.setFont("Helvetica", 9)
    c.drawCentredString(PAGE_W / 2, PAGE_H - 6.7 * inch,
                        "Licencia: MIT — Codigo abierto y redistribuible")
    _draw_footer(c)


def _slide_02_problema(c):
    _draw_bg(c)
    _draw_title(c, "Problema y Objetivo del Proyecto", PAGE_H - 1.0 * inch)
    _draw_bullets(c, [
        "Las infraestructuras IT generan metricas continuas: CPU, memoria, temperatura, latencia...",
        "Detectar fallos antes de que ocurran es critico para la disponibilidad del servicio",
        "El enfoque reactivo ya no es suficiente en entornos complejos",
    ], MARGIN, PAGE_H - 2.0 * inch, 14, BLANCO, CONTENT_W)
    _draw_text(c, "Objetivo General:", MARGIN, PAGE_H - 3.8 * inch,
               18, AZUL_CLARO, True)
    _draw_text(c, "Desarrollar modelos predictivos que permitan la deteccion temprana\n"
                  "de incidentes a partir de metricas de rendimiento del sistema,\n"
                  "facilitando la monitorizacion proactiva y la reduccion de riesgos operativos.",
               MARGIN, PAGE_H - 4.3 * inch, 14, BLANCO, max_width=CONTENT_W)
    _draw_footer(c)


def _slide_03_dataset(c):
    _draw_bg(c)
    _draw_title(c, "El Dataset", PAGE_H - 1.0 * inch)
    _draw_text(c, "IT System Performance & Resource Metrics",
               MARGIN, PAGE_H - 1.8 * inch, 16, AZUL_CLARO, True)
    _draw_table(c, [
        ["Caracteristica", "Valor"],
        ["Registros", "10 000"],
        ["Variables originales", "12 (todas numericas)"],
        ["Valores nulos", "0"],
        ["Registros duplicados", "0"],
        ["Variable objetivo", "status (0 = Normal, 1 = Incidente)"],
    ], MARGIN, PAGE_H - 2.6 * inch, [2.2 * inch, 3.5 * inch])
    _draw_text(c, "Distribucion de la variable objetivo:",
               MARGIN, PAGE_H - 5.0 * inch, 16, AZUL_CLARO, True)
    _draw_text(c, "Normal (0)    :  9 903 registros (99.03 %)",
               MARGIN, PAGE_H - 5.4 * inch, 14, VERDE)
    _draw_text(c, "Incidente (1) :    97 registros   (0.97 %)",
               MARGIN, PAGE_H - 5.8 * inch, 14, ROJO)
    _draw_text(c, "ATENCION: Fuerte desbalance de clases",
               MARGIN + 4.5 * inch, PAGE_H - 5.0 * inch, 14, NARANJA, True)
    _draw_text(c, "- Comportamiento realista en entornos IT",
               MARGIN + 4.5 * inch, PAGE_H - 5.4 * inch, 12, NARANJA)
    _draw_text(c, "  (los fallos son eventos raros)",
               MARGIN + 4.5 * inch, PAGE_H - 5.8 * inch, 12, NARANJA)
    _draw_footer(c)


def _slide_04_eda(c):
    _draw_bg(c)
    _draw_title(c, "Hallazgos del Analisis Exploratorio", PAGE_H - 1.0 * inch)
    _draw_text(c, "Correlacion con el estado del sistema (status):",
               MARGIN, PAGE_H - 1.8 * inch, 16, AZUL_CLARO, True)
    _draw_table(c, [
        ["Variable", "Correlacion"],
        ["system_pressure_score", "0.174"],
        ["memory_usage", "0.140"],
        ["cpu_utilization", "0.136"],
        ["temperature", "0.117"],
        ["context_switches", "0.015"],
        ["uptime", "0.010"],
    ], MARGIN, PAGE_H - 2.5 * inch, [3.0 * inch, 2.0 * inch])
    _draw_bullets(c, [
        "Las variables mas relevantes: CPU, memoria y temperatura",
        "El indicador compuesto system_pressure_score supera a cualquier variable individual",
        "Baja multicolinealidad entre variables -> favorable para modelado",
    ], MARGIN, PAGE_H - 5.2 * inch, 14, BLANCO, CONTENT_W)
    _draw_footer(c)


def _slide_05_insights(c):
    _draw_bg(c)
    _draw_title(c, "Insights Clave del Analisis", PAGE_H - 1.0 * inch)
    y = PAGE_H - 1.8 * inch
    for titulo, texto in [
        ("1. CPU Level vs Estado del Sistema",
         "Los 97 incidentes ocurren exclusivamente en nivel HIGH (>70 % CPU).\n"
         "LOW y MEDIUM: 0 incidentes."),
        ("2. Temperature Level vs Estado del Sistema",
         "Los 97 incidentes ocurren exclusivamente en nivel CRITICAL (>70 C).\n"
         "NORMAL y WARNING: 0 incidentes."),
        ("3. Pressure Level vs Estado del Sistema",
         "79 de 97 incidentes en nivel HIGH de presion.\n"
         "18 en MEDIUM. LOW: 0 incidentes."),
    ]:
        _draw_text(c, titulo, MARGIN, y, 16, AZUL_CLARO, True)
        y = _draw_text(c, texto, MARGIN, y - 22, 13, BLANCO, max_width=CONTENT_W, leading=18)
        y -= 16
    _draw_text(c, "Conclusion: Alta presion del sistema (CPU + temperatura) = alto riesgo de incidente",
               MARGIN, PAGE_H - 6.6 * inch, 14, NARANJA, True, CONTENT_W)
    _draw_footer(c)


def _slide_06_feature_eng(c):
    _draw_bg(c)
    _draw_title(c, "Feature Engineering", PAGE_H - 1.0 * inch)
    _draw_bullets(c, [
        "Categorizacion: CPU, memoria, latencia, temperatura",
        "Normalizacion Min-Max: 5 variables principales",
        "Indicador compuesto: system_pressure_score",
        "Clasificacion: pressure_level (Low/Medium/High)",
        "Etiquetas: status_label (Normal/Incident)",
    ], MARGIN, PAGE_H - 2.0 * inch, 13, BLANCO, 5.0 * inch)
    _draw_text(c, "Antes vs Despues:", MARGIN + 5.5 * inch, PAGE_H - 2.0 * inch,
               16, AZUL_CLARO, True)
    _draw_table(c, [
        ["", "Original", "Transformado"],
        ["Variables", "12", "24"],
        ["Registros", "10 000", "10 000"],
    ], MARGIN + 5.5 * inch, PAGE_H - 2.6 * inch, [1.5 * inch, 1.2 * inch, 1.5 * inch])
    _draw_text(c, "system_pressure_score =", MARGIN + 5.5 * inch, PAGE_H - 4.0 * inch,
               13, GRIS, True)
    _draw_text(c, "promedio de 5 metricas normalizadas:",
               MARGIN + 5.5 * inch, PAGE_H - 4.3 * inch, 13, GRIS)
    _draw_text(c, "cpu_utilization_norm, memory_usage_norm,",
               MARGIN + 5.5 * inch, PAGE_H - 4.7 * inch, 12, GRIS)
    _draw_text(c, "network_latency_norm, temperature_norm,",
               MARGIN + 5.5 * inch, PAGE_H - 5.0 * inch, 12, GRIS)
    _draw_text(c, "power_consumption_norm",
               MARGIN + 5.5 * inch, PAGE_H - 5.3 * inch, 12, GRIS)
    _draw_footer(c)


def _slide_07_modelos(c):
    _draw_bg(c)
    _draw_title(c, "Modelos Predictivos Evaluados", PAGE_H - 1.0 * inch)
    _draw_bullets(c, [
        "Regresion Logistica   -> modelo base, interpretable",
        "Random Forest         -> 200 arboles, class_weight='balanced'",
        "Red Neuronal MLP      -> 2 capas ocultas (32, 16), escalado previo",
        "Stack tecnologico      -> Python (scikit-learn) + Streamlit",
    ], MARGIN, PAGE_H - 2.0 * inch, 14, BLANCO, CONTENT_W)
    _draw_text(c, "Metricas de evaluacion (clase Incidente):",
               MARGIN, PAGE_H - 3.5 * inch, 16, AZUL_CLARO, True)
    csv_path = PROJECT_ROOT / "data" / "final" / "comparacion_modelos.csv"
    if csv_path.exists():
        df_comp = pd.read_csv(csv_path)
        cols = ["Modelo", "Accuracy", "Precision", "Recall", "F1-Score"]
        cols_existentes = [c for c in cols if c in df_comp.columns]
        filas = [[row[cols_existentes[0]]] + [f"{round(row[c2], 2):.2f}" if isinstance(row[c2], (int, float)) else str(row[c2]) for c2 in cols_existentes[1:]] for _, row in df_comp.iterrows()]
        tabla = [cols_existentes] + filas
    else:
        tabla = [["Modelo", "Accuracy", "Precision", "Recall", "F1-Score"]]
    _draw_table(c, tabla, MARGIN, PAGE_H - 4.2 * inch, [2.2 * inch, 1.2 * inch, 1.2 * inch, 1.2 * inch, 1.2 * inch])
    _draw_footer(c)


def _slide_08_rf(c):
    _draw_bg(c)
    _draw_title(c, "Resultados - Random Forest (Modelo Seleccionado)",
                PAGE_H - 1.0 * inch, 24)
    _draw_text(c, "Matriz de Confusion sobre conjunto de prueba (2 000 registros):",
               MARGIN, PAGE_H - 1.8 * inch, 16, AZUL_CLARO, True)
    _draw_table(c, [
        ("", "Predicho: Normal", "Predicho: Incidente"),
        ("Real: Normal", "1 981 (VN)", "0 (FP)"),
        ("Real: Incidente", "1 (FN)", "18 (VP)"),
    ], MARGIN + 1.0 * inch, PAGE_H - 2.7 * inch,
               [2.0 * inch, 2.5 * inch, 2.5 * inch])
    y_ley = PAGE_H - 4.0 * inch
    y_ley = _draw_text(c, "Leyenda:", MARGIN, y_ley, 14, GRIS, True) - 0.15 * inch
    y_ley = _draw_text(c, "VN = Real: Normal, Predicho: Normal (acierto)",
                       MARGIN, y_ley, 11, VERDE, max_width=3.8 * inch) - 0.05 * inch
    y_ley = _draw_text(c, "VP = Real: Incidente, Predicho: Incidente (acierto)",
                       MARGIN, y_ley, 11, VERDE, max_width=3.8 * inch) - 0.05 * inch
    y_ley = _draw_text(c, "FN = Real: Incidente, Predicho: Normal (error - falso negativo)",
                       MARGIN, y_ley, 11, ROJO, max_width=3.8 * inch) - 0.05 * inch
    y_ley = _draw_text(c, "FP = Real: Normal, Predicho: Incidente (error - falso positivo)",
                       MARGIN, y_ley, 11, ROJO, max_width=3.8 * inch) - 0.05 * inch

    _draw_text(c, "Interpretacion:", MARGIN + 4.8 * inch, PAGE_H - 4.0 * inch,
                16, AZUL_CLARO, True)
    _draw_bullets(c, [
        "Detecto 18 de 19 incidentes reales (Recall = 95 %)",
        "Cero falsos positivos (Precision = 100 %)",
        "Solo 1 incidente no detectado (falso negativo)",
        "F1-Score = 0.97 - excelente equilibrio",
    ], MARGIN + 4.8 * inch, PAGE_H - 4.5 * inch, 14, BLANCO, 3.2 * inch)
    _draw_footer(c)


def _slide_09_conclusiones(c):
    _draw_bg(c)
    _draw_title(c, "Conclusiones", PAGE_H - 1.0 * inch)
    y = PAGE_H - 1.8 * inch
    for titulo, cuerpo in TEXTOS_CONCLUSIONES:
        _draw_text(c, titulo, MARGIN, y, 14, AZUL_CLARO, True)
        y -= 18
        y = _draw_text(c, cuerpo, MARGIN, y, 10, BLANCO, max_width=CONTENT_W, leading=13)
        y -= 14
    _draw_footer(c)


def _slide_10_recomendaciones(c):
    _draw_bg(c)
    _draw_title(c, "Recomendaciones", PAGE_H - 1.0 * inch)
    _draw_bullets(c, [
        "Implementar monitorizacion proactiva de CPU, memoria y temperatura",
        "Establecer umbrales de alerta para niveles HIGH de CPU y CRITICAL de temperatura",
        "Utilizar el modelo Random Forest como herramienta de apoyo a la operacion IT",
        "Incorporar nuevas fuentes de datos: logs, almacenamiento, trafico de red",
        "Actualizar y reentrenar los modelos periodicamente",
        "Explorar tecnicas adicionales de balanceo para mejorar deteccion de eventos raros",
        "Validar los resultados en entornos reales de produccion antes del despliegue",
    ], MARGIN, PAGE_H - 2.0 * inch, 14, BLANCO, CONTENT_W)
    _draw_footer(c)


def _slide_11_gracias(c):
    _draw_bg(c)
    # Circuit decorations
    _draw_circuit_lines(c, MARGIN, PAGE_H - 2.0 * inch, 5, 25, AZUL_CLARO)
    _draw_circuit_lines(c, PAGE_W - MARGIN - 30, PAGE_H - 2.0 * inch, 5, 25, AZUL_CLARO)
    c.setFillColor(BLANCO)
    c.setFont("Helvetica-Bold", 44)
    c.drawCentredString(PAGE_W / 2, PAGE_H / 2 + 0.5 * inch, "Gracias")
    c.setFillColor(AZUL_CLARO)
    c.setFont("Helvetica", 20)
    c.drawCentredString(PAGE_W / 2, PAGE_H / 2 - 0.2 * inch,
                        "Predictive IT Infrastructure Analytics")
    c.setFillColor(GRIS)
    c.setFont("Helvetica", 14)
    c.drawCentredString(PAGE_W / 2, PAGE_H / 2 - 0.8 * inch, "?Preguntas?")
    _draw_footer(c)


# ============================================================
# MAIN
# ============================================================

SLIDE_DRAWERS = [
    _slide_01_portada,
    _slide_02_problema,
    _slide_03_dataset,
    _slide_04_eda,
    _slide_05_insights,
    _slide_06_feature_eng,
    _slide_07_modelos,
    _slide_08_rf,
    _slide_09_conclusiones,
    _slide_10_recomendaciones,
    _slide_11_gracias,
]


def generar_presentacion(output_path="Presentacion_Predictive_IT_Analytics.pdf"):
    """
    Crea y guarda el PDF del proyecto.
    """
    c = canvas.Canvas(output_path, pagesize=(PAGE_W, PAGE_H))
    c.setTitle("Predictive IT Infrastructure Analytics - Deteccion temprana de incidentes")
    c.setAuthor("Ing. Randy Bonucci Martin")
    c.setSubject("Presentacion del proyecto Predictive IT Infrastructure Analytics")
    for drawer in SLIDE_DRAWERS:
        drawer(c)
        c.showPage()
    c.save()
    return os.path.abspath(output_path)


if __name__ == "__main__":
    ruta = generar_presentacion()
    print(f"PDF generado: {ruta}")

