import streamlit as st
import pandas as pd
import plotly.express as px


def predicciones(seccion, predicciones, col_pred):
    if seccion != "Predicciones":
        return

    st.header("🚨 Predicciones de Incidencias")

    if not col_pred:
        st.warning("No se encontró una columna clara de predicción.")
        st.dataframe(predicciones, width='stretch')
        return

    conteo = predicciones[col_pred].value_counts().reset_index()
    conteo.columns = ["Estado", "Cantidad"]
    conteo["Estado"] = conteo["Estado"].replace({0: "Normal", 1: "Incidente"})

    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Distribución de estados predichos")
        fig = px.pie(conteo, names="Estado", values="Cantidad", hole=0.45, title="Normal vs Incidente")
        fig.update_layout(template="plotly_dark", paper_bgcolor="#111827", plot_bgcolor="#111827")
        st.plotly_chart(fig, width='stretch')

    with col2:
        st.subheader("Resumen de predicciones")
        total = conteo["Cantidad"].sum()
        for _, row in conteo.iterrows():
            porcentaje = round((row["Cantidad"] / total) * 100, 2)
            st.metric(f"Estado: {row['Estado']}", f"{row['Cantidad']} registros", f"{porcentaje}%")

    columnas_reales = ["Valor_Real", "valor_real", "Real", "real", "y_test", "y_real"]
    col_real = next((c for c in predicciones.columns if c in columnas_reales), None)

    if col_real:
        st.markdown("### 🎯 Matriz de Confusión - Random Forest")
        matriz = pd.crosstab(
            predicciones[col_real], predicciones[col_pred],
            rownames=["Valor Real"], colnames=["Predicción"]
        )
        fig = px.imshow(matriz, text_auto=True,
                        title="Matriz de Confusión - Valor Real vs Predicción",
                        labels=dict(color="Cantidad"))
        fig.update_layout(template="plotly_dark", paper_bgcolor="#111827", plot_bgcolor="#111827")
        st.plotly_chart(fig, width='stretch')

        aciertos = (predicciones[col_real] == predicciones[col_pred]).sum()
        errores = len(predicciones) - aciertos
        col_a, col_b = st.columns(2)
        col_a.metric("✅ Predicciones correctas", aciertos)
        col_b.metric("❌ Predicciones incorrectas", errores)

    st.markdown("### 🔎 Incidentes detectados y errores de predicción")
    mask = predicciones[col_pred] == 1
    if col_real:
        mask = mask | (predicciones[col_real] != predicciones[col_pred])
    df_vista = predicciones[mask].copy()
    if col_real:
        df_vista["Resultado"] = df_vista.apply(
            lambda r: "✅ Correcto" if r[col_real] == r[col_pred]
                      else "❌ Incorrecto",
            axis=1
        )
    st.dataframe(df_vista, width='stretch')

    if col_real:
        vn = ((predicciones[col_real] == 0) & (predicciones[col_pred] == 0)).sum()
        fp = ((predicciones[col_real] == 0) & (predicciones[col_pred] == 1)).sum()
        fn = ((predicciones[col_real] == 1) & (predicciones[col_pred] == 0)).sum()
        vp = ((predicciones[col_real] == 1) & (predicciones[col_pred] == 1)).sum()
        st.markdown(f"""
        <div style="background:#1e293b; padding:15px; border-radius:8px; margin-top:10px; font-size:14px;">
        <b>Desglose de las {len(predicciones)} predicciones:</b><br>
        ✅ <b>{aciertos}</b> correctas = {vn} VN (real=0, pred=0) + {vp} VP (real=1, pred=1)<br>
        ❌ <b>{errores}</b> incorrecta(s) = {fn} FN (real=1, pred=0) + {fp} FP (real=0, pred=1)
        </div>
        """, unsafe_allow_html=True)
        st.caption("VN = Verdadero Negativo (predijo Normal y era Normal) · VP = Verdadero Positivo (predijo Incidente y era Incidente) · FN = Falso Negativo (predijo Normal pero era Incidente) · FP = Falso Positivo (predijo Incidente pero era Normal)")
        st.markdown(f"En total hay **{aciertos} predicciones correctas** (VN + VP) y **{errores} incorrecta(s)** (FN). "
                    f"Eso significa que el modelo acertó el **{round(aciertos / len(predicciones) * 100, 2)}%** de las veces.") 