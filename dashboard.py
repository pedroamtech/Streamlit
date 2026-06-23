import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px

# Cargar el dataset
@st.cache_data
def cargar_datos():
    return sns.load_dataset("iris")

df = cargar_datos()

# TITULO: Título del Dashboard
st.title("Dashboard Interactivo - Visualización del Iris Dataset")

# DROPDOWN: Filtro por especie usando selectbox
especie = st.selectbox("Selecciona una especie:", df['species'].unique())
df_filtrado = df[df['species'] == especie]

# WRITE: Mostrar texto o tablas dinámicamente
st.subheader(f"Datos filtrados para la especie: {especie}")
st.write(df_filtrado)

# PYPLOT: Gráfico de dispersión usando Matplotlib
st.subheader(f"Gráfico de dispersión para {especie}")
fig, ax = plt.subplots()
ax.scatter(df_filtrado['sepal_length'], df_filtrado['sepal_width'], c='blue', label='Sepal')
ax.set_xlabel('Longitud del sépalo')
ax.set_ylabel('Ancho del sépalo')
ax.set_title(f"Dispersión de {especie}")
st.pyplot(fig)

# PLOTLY_CHART: Gráfico interactivo con Plotly
st.subheader("Gráfico interactivo con Plotly")
fig2 = px.scatter(df_filtrado, x="sepal_length", y="sepal_width", color="species", title=f"Dispersión de {especie}")
st.plotly_chart(fig2)

# SLIDER: Control deslizante para seleccionar un rango de longitud de sépalo
longitud_sepal_min, longitud_sepal_max = st.slider(
    "Selecciona el rango de longitud del sépalo",
    min_value=float(df['sepal_length'].min()),
    max_value=float(df['sepal_length'].max()),
    value=(float(df['sepal_length'].min()), float(df['sepal_length'].max()))
)


# SLIDER: Filtrar por rango de longitud de sépalo
df_filtrado_sepal = df[(df['sepal_length'] >= longitud_sepal_min) & (df['sepal_length'] <= longitud_sepal_max)]

# WRITE: Mostrar datos filtrados por rango
st.write(f"Datos filtrados entre {longitud_sepal_min} y {longitud_sepal_max} de longitud de sépalo:")
st.dataframe(df_filtrado_sepal)

# FILE_UPLOADER: Subir archivo CSV para análisis adicional
archivo = st.file_uploader("Sube un archivo CSV para análisis adicional", type='csv')
if archivo:
    df_subido = pd.read_csv(archivo)
    st.write("Datos del archivo cargado:", df_subido)

# METRIC: Agregar métricas clave
sepal_length_avg = df['sepal_length'].mean()
sepal_width_avg = df['sepal_width'].mean()
st.metric("Promedio de Longitud del Sépalo", f"{sepal_length_avg:.2f} cm")
st.metric("Promedio de Ancho del Sépalo", f"{sepal_width_avg:.2f} cm")
