import streamlit as st

st.title("Mi primera aplicación con Streamlit")

# st.write muestra textos
st.write("Selecciona un número para calcular su cuadrado:")

# Slider es un control deslizante
numero = st.slider('Elige un número', 0, 100, 10)

# Calcular el cuadrado del número
cuadrado = numero * 2

# Mostrar el resultado
st.write(f'El cuadrado de {numero} es {cuadrado}')
