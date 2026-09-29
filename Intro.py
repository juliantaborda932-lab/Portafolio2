import streamlit as st
from PIL import Image

st.title("Aplicaciones de Inteligencia Artificial.")

with st.sidebar:
    st.subheader("<Tu nombre> - Portafolio de IA")
    parrafo = (
        "Aquí reúno las aplicaciones de inteligencia artificial que desarrollé "
        "durante el curso: reconocimiento de voz, visión artificial, generación "
        "de texto y análisis de datos con agentes."
    )
    st.write(parrafo)

st.subheader("Estas son las aplicaciones que desarrollé en el curso")

# --- Deja solo las columnas/aplicaciones que ya hayas hecho ---
col1, col2, col3 = st.columns(3)

with col1:
    st.subheader("<Nombre app 1, ej. Texto a voz>")
    image = Image.open("<imagen1.png>")   # imagen debe estar subida al repo
    st.image(image, width=190)
    st.write("<Breve descripción de qué hace la app>")
    url = "<https://tu-app-1.streamlit.app/>"
    st.write(f"Enlace: [Abrir app]({url})")

    st.subheader("<Nombre app 2>")
    image = Image.open("<imagen2.png>")
    st.image(image, width=200)
    st.write("<Breve descripción>")
    url = "<https://tu-app-2.streamlit.app/>"
    st.write(f"Enlace: [Abrir app]({url})")

with col2:
    st.subheader("<Nombre app 3>")
    image = Image.open("<imagen3.png>")
    st.image(image, width=200)
    st.write("<Breve descripción>")
    url = "<https://tu-app-3.streamlit.app/>"
    st.write(f"Enlace: [Abrir app]({url})")

    st.subheader("<Nombre app 4>")
    image = Image.open("<imagen4.png>")
    st.image(image, width=190)
    st.write("<Breve descripción>")
    url = "<https://tu-app-4.streamlit.app/>"
    st.write(f"Enlace: [Abrir app]({url})")

with col3:
    st.subheader("<Nombre app 5>")
    image = Image.open("<imagen5.png>")
    st.image(image, width=190)
    st.write("<Breve descripción>")
    url = "<https://tu-app-5.streamlit.app/>"
    st.write(f"Enlace: [Abrir app]({url})")

    st.subheader("<Nombre app 6>")
    image = Image.open("<imagen6.png>")
    st.image(image, width=200)
    st.write("<Breve descripción>")
    url = "<https://tu-app-6.streamlit.app/>"
    st.write(f"Enlace: [Abrir app]({url})")
