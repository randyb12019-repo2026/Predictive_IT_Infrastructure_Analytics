# Conclusiones Generales

## Resumen del Proyecto

El objetivo de este proyecto fue analizar métricas operativas de una infraestructura IT y desarrollar un modelo predictivo capaz de identificar posibles incidencias del sistema a partir de indicadores de rendimiento y consumo de recursos.

A través de un flujo completo de análisis de datos, preparación de variables, exploración estadística y modelado predictivo, se logró construir una solución capaz de detectar patrones asociados a situaciones anómalas dentro del entorno analizado.

---

## Principales Hallazgos

### Calidad de los Datos

- El dataset presentaba una estructura limpia y consistente.
- No se detectaron valores nulos ni registros duplicados.
- Las variables mostraron distribuciones adecuadas para su utilización en modelos de Machine Learning.

### Comportamiento de las Métricas IT

- Los incidentes registrados representan una pequeña proporción del conjunto de datos.
- Las variables de utilización de CPU, uso de memoria y temperatura mostraron una mayor relación con los estados de incidencia.
- La mayoría de los sistemas operan en condiciones normales, reflejando un importante desbalance entre clases.

### Transformación de Datos - Feature Engineering

- Se generaron variables categóricas derivadas para facilitar el análisis de los recursos del sistema.
- La transformación de variables permitió una mejor interpretación de los comportamientos operativos.
- Las nuevas características aportaron información adicional para el modelado predictivo.

### Modelado Predictivo

- Se evaluaron distintos algoritmos de clasificación para detectar incidencias.
- Los modelos fueron entrenados utilizando datos escalados y técnicas para compensar el desbalance de clases.
- Se compararon sus métricas de rendimiento mediante Accuracy, Precision, Recall y F1-Score.

### Selección del Modelo Final

El modelo Random Forest fue seleccionado como modelo final debido a su capacidad para detectar una mayor cantidad de incidencias reales manteniendo un rendimiento equilibrado sobre el conjunto de datos.

Su comportamiento resultó superior en la identificación de eventos críticos, lo que lo convierte en la alternativa más adecuada para escenarios de monitorización y mantenimiento preventivo de infraestructuras IT.

---

## Conclusión Final

Los resultados obtenidos demuestran que las métricas operativas del sistema contienen información suficiente para anticipar posibles incidencias mediante técnicas de Machine Learning.

La utilización de modelos predictivos sobre indicadores como CPU, memoria, temperatura y consumo energético puede servir como apoyo para la detección temprana de anomalías, permitiendo reducir tiempos de respuesta y mejorar la disponibilidad de los servicios tecnológicos.

Este proyecto constituye una base sólida para futuros desarrollos orientados a sistemas de monitorización inteligente, mantenimiento predictivo y observabilidad de infraestructuras IT.