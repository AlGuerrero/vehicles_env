import pandas as pd
import plotly.express as px
import streamlit as st

st.header('Análisis de Vehiculos')
car_data = pd.read_csv('vehicles_us.csv') # leer los datos

# Casilla para construir un histograma
build_histogram = st.checkbox('Construir un histograma')
     
if build_histogram:
    st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
    fig = px.histogram(car_data, x="odometer")
    st.plotly_chart(fig, use_container_width=True)

# Casilla para construir un diagrama de dispersión
build_scatter = st.checkbox('Construir un diagrama de dispersión')

if build_scatter:
    st.write('Creación de un gráfico de dispersión: odometer vs price')
    fig2 = px.scatter(car_data, x="odometer", y="price")
    st.plotly_chart(fig2, use_container_width=True)