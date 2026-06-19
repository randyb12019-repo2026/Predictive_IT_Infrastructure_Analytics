# 📊 Predictive IT Infrastructure Analytics

## Análisis Predictivo de Infraestructuras IT

Proyecto de análisis de datos y aprendizaje automático orientado a la identificación de patrones de comportamiento asociados a incidencias en infraestructuras tecnológicas mediante el análisis de métricas de rendimiento del sistema.

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

#### XGBoost

Modelo avanzado de Gradient Boosting.

---

## Fase 9. Evaluación de Modelos

### Métricas

* Accuracy
* Precision
* Recall
* F1 Score
* ROC-AUC

### Visualizaciones

* Matriz de Confusión
* Curva ROC
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
* XGBoost

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
│   ├── streamlit_app.py
├── dashboard/
│   ├── dashboard.py
├── data/
│   ├── raw/
│   ├── processed/
│   ├── final/
├── modelos/
│   ├── modelo_prediccion.pkl
├── notebooks/
│   ├── 01_exploracion_y_limpieza_dataset.ipynb
│   ├── 02_transformacion_y_feature_engineering.ipynb
│   ├── 03_analisis_exploratorio_EDA.ipynb
│   ├── 04_modelo_predictivo.ipynb
│   ├── 05_exportacion_resultados.ipynb
├── reports/
│   ├── graphics/
│   ├── conclusiones.md
├── requirements.txt
│
└── README.md
```
---
## 📚 Correspondencia entre Fases y Notebooks

| Fase    | Descripción                                   | Notebook |
|----------|----------------------------------------------|----------|
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