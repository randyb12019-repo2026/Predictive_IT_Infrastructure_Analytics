# 📊 Predictive IT Infrastructure Analytics

## Análisis Predictivo de Infraestructuras IT

Proyecto de análisis de datos y aprendizaje automático orientado a la identificación de patrones de comportamiento asociados a incidencias en infraestructuras tecnológicas mediante el análisis de métricas de rendimiento del sistema.

---

# ⚙️ Instalación

## Requisitos

* Python 3.10+
* pip

## Pasos

```bash
# 1. Clonar el repositorio
git clone https://github.com/randyb12019-repo2026/Predictive-IT-Infrastructure-Analytics.git
cd Predictive-IT-Infrastructure-Analytics

# 2. Crear y activar entorno virtual
python -m venv .venv
# Windows:
.venv\Scripts\activate
# Linux/Mac:
# source .venv/bin/activate

# 3. Instalar dependencias
pip install -r requirements.txt

# 4. (Opcional) Instalar dependencias de desarrollo
pip install -r requirements-dev.txt

# 5. Descargar el dataset desde Kaggle y colocarlo en:
#    data/raw/Big_data_dataset.csv
#    Fuente: https://www.kaggle.com/datasets/freshersstaff/it-system-performance-and-resource-metrics

# 6. Ejecutar los notebooks en orden:
#    notebooks/01_exploracion_y_limpieza_dataset.ipynb
#    notebooks/02_transformacion_y_feature_engineering.ipynb
#    notebooks/03_analisis_exploratorio_EDA.ipynb
#    notebooks/04_modelo_predictivo.ipynb
#    notebooks/05_exportacion_resultados.ipynb

# 7. Lanzar el dashboard
streamlit run app/streamlit_app.py

# 8. (Opcional) Ejecutar tests
.venv\Scripts\python.exe -m pytest tests/ -v

> **Nota:** GitHub rechaza archivos `.pkl` por seguridad, por lo que el modelo `models/modelo_prediccion.pkl` está excluido del repositorio (`.gitignore`). Debes generar este archivo ejecutando los notebooks localmente (paso 6). Sin este archivo, el dashboard mostrará un mensaje indicando que no se encontró el modelo, pero el resto de la aplicación funciona con normalidad.
```

## Con Docker

### Requisito

* Docker instalado ([descargar aquí](https://www.docker.com/products/docker-desktop/))

```bash
# 1. Clonar el repositorio
git clone https://github.com/randyb12019-repo2026/Predictive-IT-Infrastructure-Analytics.git
cd Predictive-IT-Infrastructure-Analytics

# 2. Construir la imagen
docker build -t predictive-it-analytics .

# 3. Ejecutar el contenedor
docker run -p 8501:8501 predictive-it-analytics
```

Luego abrir `http://localhost:8501` en el navegador.

---

# 📌 Descripción del Proyecto

Las infraestructuras informáticas modernas generan continuamente métricas relacionadas con el uso de recursos, rendimiento y estabilidad operativa.

La detección temprana de anomalías permite reducir tiempos de indisponibilidad, mejorar la eficiencia operativa y optimizar la gestión de recursos tecnológicos.

Este proyecto aplica técnicas de análisis de datos y Machine Learning para identificar variables relacionadas con estados anómalos y desarrollar modelos predictivos capaces de anticipar posibles incidencias.

---

# 🎯 Objetivo General

Analizar las métricas de rendimiento de una infraestructura informática para identificar los factores asociados a estados anómalos y desarrollar modelos predictivos orientados a la detección temprana de incidencias.

---

# ❓ Problema de Negocio

Los equipos de operaciones IT suelen reaccionar una vez que el incidente ya ha ocurrido.

La pregunta principal que intenta responder este proyecto es:

> ¿Es posible detectar patrones de comportamiento en las métricas del sistema que permitan anticipar incidencias antes de que afecten al servicio?

---

# 🗂️ Dataset

## Fuente

Dataset: **IT System Performance & Resource Metrics**

Enlace: [https://www.kaggle.com/datasets/freshersstaff/it-system-performance-and-resource-metrics](https://www.kaggle.com/datasets/freshersstaff/it-system-performance-and-resource-metrics)

## Características

* 10.000 registros
* 12 variables originales
* Datos estructurados
* Sin valores nulos
* Sin registros duplicados

---

## Variables Originales

| Variable          | Descripción                          |
| ----------------- | ------------------------------------ |
| cpu_utilization   | Utilización de CPU                   |
| memory_usage      | Uso de memoria                       |
| disk_io           | Actividad de entrada/salida de disco |
| network_latency   | Latencia de red                      |
| process_count     | Número de procesos                   |
| thread_count      | Número de hilos                      |
| context_switches  | Cambios de contexto                  |
| cache_miss_rate   | Tasa de fallos de caché              |
| temperature       | Temperatura del sistema              |
| power_consumption | Consumo energético                   |
| uptime            | Tiempo de actividad                  |
| status            | Estado operativo                     |

---

# 🏗️ Arquitectura del Proyecto

```text
┌─────────────────────────────┐
│ Dataset Original            │
└──────────────┬──────────────┘
               │
               ▼
┌─────────────────────────────┐
│ Exploración y Limpieza      │
│ (Notebook 01)              │
└──────────────┬──────────────┘
               │
               ▼
┌─────────────────────────────┐
│ Transformación y           │
│ Feature Engineering        │
│ (Notebook 02)              │
└──────────────┬──────────────┘
               │
               ▼
┌─────────────────────────────┐
│ Análisis Exploratorio      │
│ de Datos (EDA)             │
│ (Notebook 03)              │
└──────────────┬──────────────┘
               │
               ▼
┌─────────────────────────────┐
│ Modelado Predictivo        │
│ (Notebook 04)              │
└──────────────┬──────────────┘
               │
               ▼
┌─────────────────────────────┐
│ Exportación de Resultados  │
│ y Conclusiones             │
│ (Notebook 05)              │
└─────────────────────────────┘
```

---

# 🔄 Ciclo de Vida del Proyecto

```text
Comprensión del Negocio
          │
          ▼
Comprensión de los Datos
          │
          ▼
Limpieza de Datos
          │
          ▼
Transformación de Datos
          │
          ▼
Ingeniería de Características
          │
          ▼
Análisis Exploratorio
          │
          ▼
Modelado Predictivo
          │
          ▼
Evaluación
          │
          ▼
Insights
          │
          ▼
Conclusiones
```

---

# 📋 Fases del Proyecto

---

## Fase 1. Comprensión del Negocio

### Actividades
* Definición de:
  - Problema a Resolver
  - Objetivos del Proyecto
  - Alcance del Proyecto

### Objetivos

* Definir el problema analítico.
* Establecer objetivos del proyecto.
* Identificar el valor de negocio.

### Entregables

* Definición del problema.
* Objetivos generales y específicos.
* Alcance del proyecto.

---

## Fase 2. Comprensión de los Datos

### Actividades

* Carga del dataset "IT System Performance & Resource Metrics".
* Validación de la estructura general del conjunto de datos.
* Verificación de la calidad de los datos obtenida durante la fase de exploración.
* Validación de los tipos de datos de las variables originales.
* Creación de variables categóricas para facilitar la interpretación de métricas operativas:
  - cpu_level
  - memory_level
  - latency_level
  - temperature_level
* Normalización de variables numéricas relevantes:
  - cpu_utilization_norm
  - memory_usage_norm
  - network_latency_norm
  - temperature_norm
  - power_consumption_norm
* Creación del indicador compuesto **system_pressure_score** para resumir el estado general de la infraestructura.
* Clasificación del nivel de presión del sistema mediante la variable **pressure_level**.
* Creación de la variable descriptiva **status_label** para facilitar la interpretación de la variable objetivo.
* Comparación entre el **dataset original** y el **dataset transformado**.
* Verificación de que no se eliminaron registros ni columnas del conjunto de datos original.
* Exportación del dataset transformado y guardado en la carpeta **/data/processed/** para las fases posteriores de análisis y modelado.

### Resultados

* 10.000 registros analizados.
* 12 variables identificadas.
* Dataset consistente.

---

## Fase 3. Limpieza de Datos

### Actividades

* Verificación de valores nulos.
* Detección de duplicados.
* Validación de integridad.

### Resultados

* Valores nulos: 0
* Duplicados: 0
* Datos consistentes para análisis.

---

## Fase 4. Transformación de Datos

### Actividades

Normalización de variables numéricas:

* cpu_utilization_norm
* memory_usage_norm
* network_latency_norm
* temperature_norm
* power_consumption_norm

Creación de variables categóricas:

* cpu_level
* temperature_level
* latency_level
* pressure_level

---

## Fase 5. Ingeniería de Características

### Nuevas Variables

#### Status Label

Conversión del estado numérico a una representación más interpretable.

| Valor | Estado    |
| ----- | --------- |
| 0     | Normal    |
| 1     | Incidente |

#### System Pressure Score

Indicador compuesto basado en:

* CPU
* Memoria
* Temperatura

---

## Fase 6. Análisis Exploratorio de Datos (EDA)

### Objetivos

Comprender el comportamiento de las variables y detectar patrones relevantes.

### Análisis realizados

#### Análisis Univariante

* Histogramas
* Distribuciones
* Boxplots

#### Análisis Bivariante

* CPU vs Estado
* Memoria vs Estado
* Temperatura vs Estado

#### Correlaciones

Variables con mayor relación con incidencias:

| Variable        | Correlación |
| --------------- | ----------- |
| memory_usage    | 0.140       |
| cpu_utilization | 0.136       |
| temperature     | 0.117       |

---

## Fase 7. Preparación para Machine Learning

### Actividades

* Definición de variable objetivo.
* Selección de características.
* División Train/Test.
* Escalado de variables.

### Variable Objetivo

```python
status
```

---

## Fase 8. Modelado Predictivo

### Modelos Evaluados

#### Regresión Logística

Modelo base para clasificación binaria.

#### Random Forest

Modelo basado en árboles de decisión.

#### Red Neuronal MLP

Red neuronal multicapa con 2 capas ocultas (32 y 16 neuronas).

---

## Fase 9. Evaluación de Modelos

### Métricas

* Accuracy
* Precision
* Recall
* F1 Score

### Visualizaciones

* Matriz de Confusión
* Importancia de Variables

---

## Fase 10. Interpretación de Resultados

### Objetivo

Traducir los resultados técnicos a conclusiones comprensibles para el negocio.

### Aspectos Analizados

* Variables más influyentes.
* Comportamiento de los incidentes.
* Capacidad predictiva del modelo.

---

## Fase 11. Insights de Negocio

### Hallazgo 1

La utilización de CPU presenta una relación positiva con los estados de incidencia.

### Hallazgo 2

El uso de memoria aumenta en los escenarios asociados a incidentes.

### Hallazgo 3

Las temperaturas elevadas muestran una mayor asociación con comportamientos anómalos.

### Hallazgo 4

La combinación de múltiples métricas ofrece mejores resultados que el análisis individual de variables.

---

## Fase 12. Conclusiones y Recomendaciones

### Conclusiones

* Las métricas de infraestructura contienen información útil para identificar estados anómalos.
* CPU, memoria y temperatura son las variables más relevantes.
* Los modelos predictivos permiten detectar patrones asociados a incidencias.

### Recomendaciones

* Incorporar datos reales de monitorización.
* Ampliar el histórico temporal.
* Integrar el modelo con herramientas de observabilidad.
* Implementar alertas predictivas.

---

# 🛠️ Tecnologías Utilizadas

## Lenguaje

* Python

## Análisis de Datos

* Pandas
* NumPy

## Visualización

* Matplotlib
* Seaborn

## Machine Learning

* Scikit-Learn

## Testing

* pytest

### 🧪 Sobre los tests

El proyecto incluye **tests unitarios** con pytest para verificar que las funciones clave del código se comportan correctamente. No dependen de Streamlit ni de archivos externos (CSV, modelos), por lo que se ejecutan de forma rápida y aislada.

**¿Qué cubren?**

| Archivo | Propósito |
|---|---|
| `tests/test_detectores.py` | Verifica que la detección automática de columnas (predicción, modelo, F1) funcione con distintos nombres posibles |
| `tests/test_metricas.py` | Verifica que `obtener_media()` y `obtener_metricas()` devuelvan resultados correctos con distintos tipos de DataFrame |
| `tests/test_conclusiones.py` | Verifica que los textos de conclusiones existan y tengan la estructura esperada |

**¿Por qué son útiles?**

Si modificas el código y sin querer rompes algo (ej: `obtener_media()` empieza a devolver la suma en vez del promedio), los tests fallarán y te avisarán al instante en lugar de descubrirlo al ejecutar la app. Son una red de seguridad para mantener el proyecto a largo plazo.

## Entorno de Desarrollo

* VS Code
* Jupyter Notebook

## Control de Versiones

* Git
* GitHub

---

# 📂 Estructura del Proyecto

```text
Predictive-IT-Infrastructure-Analytics/
│
├── app/
│   └── streamlit_app.py                  # Aplicación web Streamlit
│
├── dashboard/
│   ├── __init__.py
│   └── dashboard.py                      # Orquestador del dashboard
│
├── data/
│   ├── raw/
│   │   ├── Big_data_dataset.csv          # Dataset original
│   │   └── informacion.md
│   ├── processed/
│   │   ├── Big_data_dataset_transformado.csv  # Dataset transformado
│   │   └── informacion.md
│   └── final/
│       ├── comparacion_modelos.csv        # Comparación de modelos
│       ├── incidencias_detectadas_random_forest.csv
│       ├── predicciones_random_forest.csv # Predicciones del modelo
│       └── informacion.md
│
├── models/
│   └── modelo_prediccion.pkl             # Modelo entrenado (Pickle)
│
├── notebooks/
│   ├── 01_exploracion_y_limpieza_dataset.ipynb
│   ├── 02_transformacion_y_feature_engineering.ipynb
│   ├── 03_analisis_exploratorio_EDA.ipynb
│   ├── 04_modelo_predictivo.ipynb
│   └── 05_exportacion_resultados.ipynb
│
├── reports/
│   ├── graphics/                         # Gráficos generados (PNG)
│   │   # Nomenclatura: Nb{notebook}_{nº_figura}_{descripción}.png
│   │   # Ej: Nb03_06_cpu_por_estado.png = Notebook 03, figura 6, "CPU por estado"
│   │   ├── Nb01_11_distribuciones_variables_numericas.png
│   │   ├── Nb01_12_matriz_correlacion.png
│   │   ├── Nb01_13_boxplots_valores_extremos.png
│   │   ├── Nb03_04_distribucion_estado_sistema.png
│   │   ├── Nb03_05_correlacion_con_status.png
│   │   ├── Nb03_06_cpu_por_estado.png
│   │   ├── Nb03_07_memoria_por_estado.png
│   │   ├── Nb03_08_temperatura_por_estado.png
│   │   ├── Nb03_09_cpu_level_vs_status.png
│   │   ├── Nb03_10_temperature_level_vs_status.png
│   │   ├── Nb03_11_pressure_level_vs_status.png
│   │   ├── Nb03_12_system_pressure_score_por_estado.png
│   │   └── Nb03_13_matriz_correlacion_avanzada.png
│   └── conclusiones.md
│
├── src/                                  # Módulos fuente Python
│   ├── __init__.py
│   ├── ui/                               # Componentes de interfaz
│   │   ├── __init__.py
│   │   ├── cabecera.py                   # Cabecera de la app
│   │   ├── estilos.py                    # Estilos CSS personalizados
│   │   ├── plantilla.py                  # Configuración de página
│   │   └── sidebar.py                    # Navegación lateral
│   ├── pages/                            # Páginas del dashboard
│   │   ├── __init__.py
│   │   ├── resumen_ejecutivo.py          # KPIs y resumen
│   │   ├── estado_infraestructura.py     # Estado de infraestructura
│   │   ├── comparacion_modelos.py        # Comparación de modelos
│   │   └── predicciones.py               # Vista de predicciones
│   ├── core/                             # Lógica de negocio y datos
│   │   ├── __init__.py
│   │   ├── datos.py                      # Carga y validación de datos
│   │   ├── detectores.py                 # Detección de columnas
│   │   ├── metricas.py                   # Métricas del modelo
│   │   └── conclusiones.py               # Textos de conclusiones
│   └── export/                           # Generación de reportes PDF
│       ├── __init__.py
│       ├── presentacion.py               # Generación de PDF
│       └── generar_presentacion.py       # Sidebar de exportación PDF
│
├── tests/                                # Tests unitarios (pytest)
│   ├── test_detectores.py                # Tests de detección de columnas
│   ├── test_metricas.py                  # Tests de funciones de métricas
│   └── test_conclusiones.py              # Tests de textos de conclusiones
│
├── LICENCE.md                           # Licencia MIT
├── README.md                            # Este archivo
├── requirements.txt                     # Dependencias del proyecto
└── requirements-dev.txt                 # Dependencias de desarrollo (pytest)
```
---
## 📚 Correspondencia entre Fases y Notebooks

| Fase    | Descripción                                   | Notebook                                           |
|---------|--------------------------------------------|----------------------------------------------------|
| Fase 1  | Comprensión del Negocio                       | `01_exploracion_y_limpieza_dataset.ipynb` y README |
| Fase 2  | Comprensión de los Datos                      | `01_exploracion_y_limpieza_dataset.ipynb` |
| Fase 3  | Exploración Inicial de los Datos              | `01_exploracion_y_limpieza_dataset.ipynb` |
| Fase 4  | Limpieza y Preparación de Datos               | `01_exploracion_y_limpieza_dataset.ipynb` |
| Fase 5  | Transformación de Datos y Feature Engineering | `02_transformacion_y_feature_engineering.ipynb` |
| Fase 6  | Análisis Exploratorio de Datos (EDA)          | `03_analisis_exploratorio.ipynb` |
| Fase 7  | Preparación para Machine Learning             | `04_modelo_predictivo.ipynb` |
| Fase 8  | Modelado Predictivo                           | `04_modelo_predictivo.ipynb` |
| Fase 9  | Comparación y Evaluación de Modelos           | `04_modelo_predictivo.ipynb` |
| Fase 10 | Interpretación de Resultados                  | `04_modelo_predictivo.ipynb` |
| Fase 11 | Exportación y Validación de Resultados        | `05_exportacion_resultados.ipynb` |
| Fase 12 | Conclusiones y Recomendaciones                | `05_exportacion_resultados.ipynb` y README |

---

# 📈 Principales Beneficios

## Beneficios Operativos

* Detección temprana de incidencias.
* Mejora de la monitorización.
* Reducción del tiempo de respuesta.
* Optimización de recursos.

## Beneficios Estratégicos

* Toma de decisiones basada en datos.
* Incremento de la disponibilidad de servicios.
* Reducción del riesgo operativo.

---

# 🎓 Competencias Aplicadas

* Análisis Exploratorio de Datos
* Limpieza y Transformación de Datos
* Ingeniería de Características
* Estadística Descriptiva
* Machine Learning Supervisado
* Evaluación de Modelos
* Interpretación de Resultados
* Comunicación de Insights

---

# 🚀 Líneas Futuras

* Implementación de detección de anomalías en tiempo real.
* Integración con sistemas SIEM y observabilidad.
* Incorporación de métricas históricas.
* Desarrollo de dashboard interactivo.
* Automatización de alertas predictivas.

---

# 👨‍💻 Autor

Proyecto desarrollado como trabajo final del Bootcamp de Data Analytics e Inteligencia Artificial.

**Autor:** Randy Bonucci Martín

**Especialización:** Data Analytics, Infraestructuras IT y Machine Learning.

---

# 📄 Licencia

Este proyecto está bajo la licencia **MIT**. Consulta el archivo `LICENCE.md` para más detalles.