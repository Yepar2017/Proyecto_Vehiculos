
import streamlit as st
import pandas as pd
import plotly.express as px
import numpy as np 

# Leer los datos
df = pd.read_csv('vehicles_us.csv')

# Encabezado
st.header('Análisis de vehículos usados en EE. UU')

# Instrucción al usuario
st.write("Haz clic en el botón para generar un histograma interactivo de los precios de los vehículos.")

# Botón que genera el gráfico
if st.button("Mostrar histograma"):
    fig = px.histogram(df, x='price', nbins=50, title='Distribución de precios de vehículos')
    st.plotly_chart(fig)

# graficos adicionales con checkboxes

st.title("Demo con Checkboxes: Histogramas y Dispersión")

# Datos de ejemplo
np.random.seed(42)
df = pd.DataFrame({
    "x": np.random.randn(300),
    "y": np.random.randn(300) * 0.8 + 0.2,
    "categoría": np.random.choice(["A", "B", "C"], size=300)
})

st.write("Selecciona qué gráfico(s) quieres ver:")
show_hist = st.checkbox("Mostrar histograma")
show_scatter = st.checkbox("Mostrar dispersión")

if show_hist:
    st.write("**Histograma de `x`**")
    fig_hist = px.histogram(df, x="x", nbins=30, title="Histograma de x")
    st.plotly_chart(fig_hist, use_container_width=True)

if show_scatter:
    st.write("**Diagrama de dispersión `x` vs `y`**")
    fig_scatter = px.scatter(
        df, x="x", y="y", color="categoría",
        title="Dispersión x vs y por categoría", opacity=0.8
    )
    st.plotly_chart(fig_scatter, use_container_width=True)

if not (show_hist or show_scatter):
    st.info("Activa al menos una casilla para ver un gráfico.")
