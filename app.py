import streamlit as st
import pandas as pd
import plotly.express as px

# Cargar datos
car_data = pd.read_csv('vehicles_us.csv')

# Eliminar valores nulos necesarios
car_data = car_data.dropna(subset=['odometer', 'price'])

# Título
st.header('Análisis de datos de vehículos')

# Casilla para histograma
show_hist = st.checkbox('Mostrar histograma del kilometraje')

if show_hist:
    st.write(
        'Creación de un histograma para el conjunto de datos de anuncios de venta de coches'
    )
    
    fig_hist = px.histogram(
        car_data,
        x='odometer',
        title='Distribución del kilometraje'
    )
    
    st.plotly_chart(fig_hist, use_container_width=True)

# Casilla para gráfico de dispersión
show_scatter = st.checkbox('Mostrar gráfico de dispersión (precio vs kilometraje)')

if show_scatter:
    st.write(
        'Creación de un gráfico de dispersión entre el precio y el kilometraje'
    )
    
    fig_scatter = px.scatter(
        car_data,
        x='odometer',
        y='price',
        title='Relación entre kilometraje y precio'
    )
    
    st.plotly_chart(fig_scatter, use_container_width=True)
