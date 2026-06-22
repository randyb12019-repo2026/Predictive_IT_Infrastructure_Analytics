import streamlit as st

TEXTOS_CONCLUSIONES = [
    ("1. Preparación y Transformación de los Datos",
     "Durante las fases iniciales del proyecto se realizó la exploración, validación y "
     "preparación del dataset de métricas de infraestructura IT. El conjunto de datos no "
     "presentó valores nulos ni registros duplicados, lo que permitió centrar el trabajo en "
     "la transformación y enriquecimiento de las variables. Posteriormente se aplicaron "
     "técnicas de normalización, categorización e ingeniería de características con el "
     "objetivo de facilitar el análisis y mejorar la capacidad predictiva de los modelos."),
    ("2. Análisis Exploratorio de Datos",
     "El análisis exploratorio permitió comprender el comportamiento de las principales "
     "métricas operativas de la infraestructura, incluyendo utilización de CPU, consumo de "
     "memoria, operaciones de disco, latencia de red, temperatura y consumo energético. "
     "Las visualizaciones mostraron distribuciones relativamente estables en la mayoría de "
     "las variables, así como la existencia de relaciones entre determinados indicadores "
     "operativos y el estado registrado del sistema. Asimismo, se observó un fuerte "
     "desbalance entre registros normales e incidencias, siendo los estados normales la "
     "gran mayoría de las observaciones disponibles en el dataset."),
    ("3. Modelo Predictivo",
     "Se entrenaron y evaluaron diferentes algoritmos de Machine Learning para predecir "
     "posibles incidencias dentro de la infraestructura tecnológica. La comparación de "
     "métricas permitió identificar al modelo Random Forest como la alternativa con mejor "
     "rendimiento general para este problema de clasificación."),
    ("4. Resultados Obtenidos",
     "El modelo fue capaz de identificar registros asociados a posibles incidencias dentro "
     "del conjunto de datos analizado. Las métricas obtenidas durante la evaluación, junto "
     "con la matriz de confusión y el análisis de predicciones, permitieron validar el "
     "comportamiento del modelo y comprobar su capacidad para diferenciar entre estados "
     "normales y situaciones potencialmente anómalas."),
    ("5. Aplicación Práctica",
     "El dashboard implementado permite visualizar indicadores operativos, revisar el "
     "comportamiento del modelo predictivo y consultar las incidencias detectadas, "
     "proporcionando una base para futuras soluciones orientadas a observabilidad, soporte "
     "técnico, operaciones IT o detección temprana de anomalías."),
    ("6. Trabajo Futuro",
     "Como posibles líneas de mejora se plantea la incorporación de nuevos datasets con una "
     "mayor representación de incidencias reales, la evaluación de técnicas adicionales de "
     "balanceo de clases, la comparación con nuevos algoritmos predictivos y la integración "
     "de mecanismos de monitorización en tiempo real para la detección automática de anomalías.")
]


def conclusiones(seccion):
    if seccion != "Conclusiones":
        return

    st.header("📌 Conclusiones del Proyecto")
    textos = TEXTOS_CONCLUSIONES
    for titulo, cuerpo in textos:
        st.markdown(f"""
        <div class="info-card">
        <h3>{titulo}</h3>
        <p>{cuerpo}</p>
        </div>
        """, unsafe_allow_html=True)
