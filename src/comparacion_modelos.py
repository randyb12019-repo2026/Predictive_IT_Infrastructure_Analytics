import streamlit as st
import plotly.express as px


def comparacion_modelos(seccion, comparacion, col_modelo, col_f1):
    if seccion != "Comparación de Modelos":
        return

    st.header("🤖 Comparación de Modelos Predictivos")
    st.dataframe(comparacion, use_container_width=True)

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
        st.plotly_chart(fig, use_container_width=True)

    if col_f1:
        mejor_modelo = comparacion.loc[comparacion[col_f1].idxmax()]
        st.success(
            f"Modelo seleccionado: {mejor_modelo[col_modelo]} "
            f"por obtener el mejor F1-Score ({round(mejor_modelo[col_f1], 3)})."
        )
