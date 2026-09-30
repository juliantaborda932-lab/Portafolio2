import streamlit as st
from PIL import Image

# Página ancha para que quepan las 4 columnas cómodamente
st.set_page_config(page_title="Hub de Aplicaciones de IA", layout="wide")

st.title("Hub de Aplicaciones y Proyectos de Inteligencia Artificial")

with st.sidebar:
    st.subheader("Julian Taborda - Portafolio")
    parrafo = (
        "La inteligencia artificial permite mejorar la toma de decisiones con el uso de datos, "
        "automatizar tareas rutinarias y proporcionar análisis avanzados en tiempo real, lo que "
        "resulta en una mayor eficiencia y precisión en diversos campos."
    )
    st.write(parrafo)

url_ia = "https://sites.google.com/view/computacinavanzada"
st.subheader("En el siguiente enlace puedes encontrar páginas y ejercicios prácticos")
st.write(f"Enlace para páginas y ejercicios generales: [Portal de Ejercicios]({url_ia})")

st.divider()

# Imágenes disponibles en imagenes/ (confirmado en tu repo):
# Chat_pdf.png, OIG2.jpg, OIG3.jpg, OIG4.jpg, OIG5.jpg, OIG6.jpg, OIG8.jpg,
# audio_to_txt.png, data_analisis.png

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.subheader("1. Prueba Streamlit")
    image = Image.open('imagenes/audio_to_txt.png')
    st.image(image, width=180)
    st.write("Creación de archivo inicial de prueba y despliegue básico en la plataforma.")
    url1 = "https://intro-pa.streamlit.app/"
    st.write(f"App Prueba: [Enlace]({url1})")

    st.subheader("2. Vectores y Matrices")
    image = Image.open('imagenes/OIG2.jpg')
    st.image(image, width=180)
    st.write("Agrega una fruta con sus características y calcula distancias entre vectores.")
    url2 = "https://frutaspy.streamlit.app/"
    st.write(f"Vectores: [Enlace]({url2})")

    st.subheader("3. Cálculo Aplicado y Gradiente")
    image = Image.open('imagenes/OIG5.jpg')
    st.image(image, width=180)
    st.write("Descenso de gradiente: cambio de función objetivo, derivadas y búsqueda de mínimos.")
    url3 = "https://actividad2.streamlit.app/"
    st.write(f"Gradiente: [Enlace]({url3})")

    st.subheader("4. Lógica, Big-O y Vectorización")
    image = Image.open('imagenes/OIG8.jpg')
    st.image(image, width=180)
    st.write("Análisis de complejidad algorítmica, reglas de negocio y vectorización.")
    url4 = "https://actividad3.streamlit.app/"
    st.write(f"Big-O & Vectorización: [Enlace]({url4})")

with col2:
    st.subheader("5. Preparación de Datos")
    image = Image.open('imagenes/data_analisis.png')
    st.image(image, width=180)
    st.write("Tipos de datos, valores faltantes, normalización, train/test split y correlación.")
    url5 = "https://actividad4paraclase.streamlit.app/"
    st.write(f"Prep. Datos: [Enlace]({url5})")

    st.subheader("6. Datos Ambientales (Lluvia)")
    image = Image.open('imagenes/OIG3.jpg')
    st.image(image, width=180)
    st.write("Datos hidrológicos vía API MARCO de Cornare e Índice de Calidad de Datos (ICD).")
    url6 = "https://rios-y-quebradas.streamlit.app/"
    st.write(f"Datos Cornare: [Enlace]({url6})")

    st.subheader("7. Regresión Lineal")
    image = Image.open('imagenes/Chat_pdf.png')
    st.image(image, width=180)
    st.write("Modelos simple/múltiple, función de costo, learning rate y métricas (MSE, R²).")
    url7 = "https://regresion.streamlit.app/"
    st.write(f"Regresión Lineal: [Enlace]({url7})")

with col3:
    st.subheader("8. Series de Tiempo")
    image = Image.open('imagenes/OIG4.jpg')
    st.image(image, width=180)
    st.write("Tendencia y estacionalidad con ARIMA, SARIMA y Holt-Winters.")
    url8 = "https://series-de-tiempoo.streamlit.app/"
    st.write(f"Series de Tiempo: [Enlace]({url8})")

    st.subheader("9. Calidad del Aire")
    image = Image.open('imagenes/OIG2.jpg')
    st.image(image, width=180)
    st.write("Predicción de PM2.5 y PM10 usando datos de dos estaciones de monitoreo.")
    url9 = "https://calidad-airee.streamlit.app/"
    st.write(f"Calidad del Aire: [Enlace]({url9})")

    st.subheader("10. Captura y Procesamiento IoT")
    image = Image.open('imagenes/OIG6.jpg')
    st.image(image, width=180)
    st.write("Procesamiento de datos en tiempo real (humedad, temperatura) con sensores IoT.")
    url10 = "https://iotejercicio.streamlit.app/"
    st.write(f"Sistema IoT: [Enlace]({url10})")

with col4:
    st.subheader("11. Regresión Logística")
    image = Image.open('imagenes/audio_to_txt.png')
    st.image(image, width=180)
    st.write("Transición de predicción de variables continuas a clasificación por categorías.")
    url11 = "https://regresion-logisticaaaa.streamlit.app/"
    st.write(f"Regresión Logística: [Enlace]({url11})")

    st.subheader("12. Clasificación KNN")
    image = Image.open('imagenes/OIG5.jpg')
    st.image(image, width=180)
    st.write("Algoritmo K-Vecinos más Cercanos, fronteras de decisión y efecto de K.")
    st.info("Desarrollado con HTML interactivo local en clase.")

    st.subheader("13. KNN Suelos AGROSAVIA")
    image = Image.open('imagenes/OIG8.jpg')
    st.image(image, width=180)
    st.write("Clasificación de fertilidad de suelos (baja, media, alta) según análisis químicos.")
    url13 = "https://agrosavia-kjbeg9dh3grekyks94hmrv.streamlit.app/"
    st.write(f"KNN Suelos: [Enlace]({url13})")
