import streamlit as st
import plotly.express as px


def comparacion_modelos(seccion, comparacion, col_modelo, col_f1):
    if seccion != "Comparación de Modelos":
        return

    st.header("🤖 Comparación de Modelos Predictivos")
    st.dataframe(comparacion, width='stretch')

    columnas_numericas = comparacion.select_dtypes(include="number").columns.tolist()
    if columnas_numericas:
        metrica = st.selectbox("Selecciona una métrica para comparar:", columnas_numericas)
        fig = px.bar(
            comparacion, x=col_modelo, y=metrica,
            title=f"Comparación de modelos según {metrica}", text=metrica
        )
        fig.update_layout(
            template="plotly_dark", paper_bgcolor="#111827", plot_bgcolor="#111827",
            xaxis_title="Modelo", yaxis_title=metrica
        )
        st.plotly_chart(fig, width='stretch')

    if col_f1:
        mejor_modelo = comparacion.loc[comparacion[col_f1].idxmax()]
        st.success(
            f"Modelo seleccionado: {mejor_modelo[col_modelo]} "
            f"por obtener el mejor F1-Score ({round(mejor_modelo[col_f1], 3)})."
        )
        st.markdown(
            "<div style='background:#0f172a; padding:10px 15px; border-radius:8px; "
            "font-size:13px; border-left:3px solid #2E86C1;'>"
            "<b>📖 ¿Qué es F1-Score?</b><br>"
            "Combina <b>Precisión</b> (de lo que predijo como incidente, cuántos realmente lo eran) "
            "y <b>Recall</b> (de los incidentes reales, cuántos logró detectar).<br>"
            "Un F1 cercano a <b>1.0</b> significa que el modelo detecta bien los incidentes "
            "sin generar falsas alarmas.<br><br>"
            "<b>¿Por qué no usar solo Accuracy?</b><br>"
            "Accuracy mide el porcentaje total de aciertos. Pero con datos desbalanceados "
            "(99% normal, 1% incidente), un modelo que siempre prediga \"Normal\" tendría "
            "<b>99% de accuracy</b> sin detectar ningún incidente. Por eso se usa F1-Score, "
            "que penaliza los falsos negativos (incidentes no detectados)."
            "</div>",
            unsafe_allow_html=True,
        )
