"""CV y portfolio de Beñat Ilzarbe. Ejecutar: streamlit run app.py"""

from pathlib import Path
from html import escape

import pandas as pd
import streamlit as st

ROOT = Path(__file__).resolve().parent
st.set_page_config(
    page_title="Beñat Ilzarbe | Inteligencia Artificial",
    page_icon="✳",
    layout="wide",
    initial_sidebar_state="collapsed",
)
st.html((ROOT / "assets" / "style.css").read_text(encoding="utf-8"))


def html(text):
    st.html(text)


def heading(eyebrow, title, description=""):
    html(f'<div class="section-heading"><p class="eyebrow">{escape(eyebrow)}</p>'
         f'<h2>{escape(title)}</h2><p class="section-intro">{escape(description)}</p></div>')


def tags(items):
    html('<p class="skills-line">' + ' <span aria-hidden="true">/</span> '.join(escape(x) for x in items) + '</p>')


html('<div class="masthead"><span class="wordmark">BI.</span>'
     '<span>BEÑAT ILZARBE DAZA</span><span class="masthead-location">DONOSTIA / SAN SEBASTIÁN</span></div>')

intro, portrait = st.columns([3, 1], gap="large")
with intro:
    html('<p class="eyebrow hero-eyebrow">INGENIERÍA EN INTELIGENCIA ARTIFICIAL</p>'
         '<h1>Aprender.<br>Experimentar.<br><em>Construir.</em></h1>'
         '<p class="hero-intro">Soy Beñat, estudiante de Ingeniería en Inteligencia Artificial en '
         'Tecnun – Universidad de Navarra. Me interesa convertir datos en soluciones y seguir '
         'aprendiendo a través de proyectos y experiencias profesionales.</p>')
with portrait:
    st.image(str(ROOT / "assets" / "benat.png"), width=250)
    html('<p class="portrait-caption">Beñat Ilzarbe Daza<br>Inteligencia artificial · Datos · Aprendizaje</p>')

contact, github, download = st.columns(3)
with contact:
    st.link_button("Hablemos por email", "mailto:bilzarbe06@gmail.com", width="stretch", type="primary")
with github:
    st.link_button("Ver mi GitHub", "https://github.com/Bilzarbe", width="stretch")
with download:
    st.download_button("Descargar CV en PDF", (ROOT / "assets" / "CV_Benat_Ilzarbe.pdf").read_bytes(),
                       file_name="CV_Benat_Ilzarbe.pdf", mime="application/pdf", width="stretch")

st.divider()
section = st.radio("Explora mi perfil", ["Sobre mí", "Proyectos", "Trayectoria"], horizontal=True,
                   label_visibility="collapsed")

if section == "Sobre mí":
    heading("PERFIL", "Curiosidad por la tecnología. Constancia para avanzar.")
    left, right = st.columns([1.4, 1], gap="large")
    with left:
        st.write("Estudio Ingeniería en Inteligencia Artificial desde 2024. Me interesan el machine learning, "
                 "el deep learning y el análisis de datos: entender el problema, probar distintas soluciones "
                 "y evaluar lo que funciona.")
        st.write("En mis proyectos académicos he trabajado con clasificación de señales RFID y procesamiento "
                 "distribuido de datos. En verano de 2026 realicé prácticas de ingeniería en BieleDigital SL.")
        st.write("Me definen la disciplina, la capacidad de aprender y el compromiso. Disfruto colaborando "
                 "con otras personas y aportando en entornos nuevos.")
    with right:
        html('<div class="pullquote">El deporte me ha enseñado a mantener la constancia, '
             'también cuando los resultados necesitan tiempo.</div>')

    heading("CONOCIMIENTOS", "Herramientas con las que trabajo")
    a, b, c = st.columns(3, gap="large")
    with a:
        st.subheader("Programación")
        tags(["Python", "C++", "MATLAB", "R", "HTML", "JavaScript"])
    with b:
        st.subheader("IA y análisis")
        tags(["Machine Learning", "Deep Learning", "Power BI"])
    with c:
        st.subheader("En mis proyectos")
        tags(["TensorFlow / Keras", "scikit-learn", "Spark", "Hadoop", "Docker"])
    st.caption("Las herramientas de la última columna aparecen en los proyectos académicos del portfolio.")

    heading("IDIOMAS", "Tres idiomas para conectar")
    a, b, c = st.columns(3)
    with a:
        st.subheader("Euskera")
        st.write("Lengua materna")
        st.caption("Certificaciones B1, B2 y C1 de HABE")
    with b:
        st.subheader("Castellano")
        st.write("Nativo")
    with c:
        st.subheader("Inglés")
        st.write("Avanzado")
        st.caption("Cambridge First Certificate y cursos en Reino Unido")

    heading("FUERA DEL AULA", "El deporte forma parte de mi manera de trabajar")
    st.write("He practicado ciclismo y natación durante años, con medallas en campeonatos provinciales, "
             "autonómicos y de ámbito nacional. En 2022 entrené en el grupo de tecnificación de la "
             "Federación Guipuzcoana de Natación.")
    st.write("También he formado parte de Talento Deportivo, el programa de la Universidad de Navarra "
             "que acompaña el desarrollo académico, profesional, deportivo y personal.")

elif section == "Proyectos":
    heading("PORTFOLIO", "Aprender haciendo, comprobar con datos.",
            "Dos proyectos académicos que muestran mi trabajo con modelos de IA y sistemas de datos.")
    area = st.selectbox("Filtrar proyectos por área", ["Todos", "Deep Learning", "Big Data"])
    if area in ("Todos", "Deep Learning"):
        html('<article class="project-heading"><p class="eyebrow">DEEP LEARNING / SEÑALES</p>'
             '<h3>Chipless RFID Classification</h3><p>Reconocer etiquetas a partir de señales ruidosas.</p></article>')
        st.write("Clasificación de 16 etiquetas RFID sin chip a partir de representaciones tiempo-frecuencia "
                 "CWT. El estudio compara métodos clásicos, redes convolucionales y otras arquitecturas "
                 "con un protocolo común de validación cruzada.")
        a, b, c = st.columns(3)
        a.metric("Accuracy de validación", "97,4 %")
        b.metric("Mediciones de entrenamiento", "4.800")
        c.metric("Clases", "16")
        st.caption("Resultado del ensemble en validación cruzada estratificada de 5 folds. "
                   "El test contiene 2.400 muestras sin etiquetas; no hay una accuracy de test medida.")
        tags(["Python", "TensorFlow / Keras", "scikit-learn", "Optuna", "CWT"])
        with st.expander("Explorar los resultados del proyecto"):
            st.write("El modelo final combina una CNN 1D, dos EfficientNetV2-B0 —con y sin preentrenamiento— "
                     "y una CNN con capas Transformer. Promedia sus probabilidades de clase.")
            breakdown = st.radio("Comparar resultados por", ["Modelo", "Distancia de lectura"], horizontal=True)
            if breakdown == "Modelo":
                results = pd.DataFrame({"Modelo": ["Correlación con referencias", "1-NN", "CNN 1D inicial", "CNN 1D final", "Ensemble"],
                                        "Accuracy (%)": [61.1, 91.2, 96.0, 96.6, 97.4]})
                axis = "Modelo"
            else:
                results = pd.DataFrame({"Distancia": ["50–80 cm", "80–110 cm", "110–140 cm"],
                                        "Accuracy (%)": [99.3, 98.2, 94.6]})
                axis = "Distancia"
            st.bar_chart(results.set_index(axis), color="#235c48", horizontal=True)
            st.dataframe(results, hide_index=True, width="stretch")
            st.caption("Visualización de los resultados registrados en el proyecto; no ejecuta ni reentrena los modelos.")
            st.write("Los errores se concentran en las etiquetas pequeñas y a mayor distancia. "
                     "El análisis incluye matrices de confusión, Grad-CAM, t-SNE y confianza de las predicciones.")
            st.write("Limitación: elegir el ensemble con las mismas predicciones de validación puede introducir "
                     "optimismo en la precisión reportada.")
        st.caption("Proyecto realizado con Iker Elias y Aitor Marcalain.")
        st.divider()

    if area in ("Todos", "Big Data"):
        html('<article class="project-heading"><p class="eyebrow">BIG DATA / SISTEMAS DISTRIBUIDOS</p>'
             '<h3>DonostIArrak</h3><p>Procesamiento distribuido de comunicaciones ciudadanas sintéticas.</p></article>')
        st.write("Arquitectura local para generar y procesar un conjunto de 15 millones de correos sintéticos "
                 "dirigidos al Ayuntamiento de Donostia. Integra almacenamiento distribuido, controles de "
                 "calidad, transformación a Parquet y clasificación con machine learning.")
        tags(["Apache Spark", "Hadoop / HDFS", "YARN", "Docker Compose", "PySpark", "MLlib"])
        with st.expander("Ver el flujo de trabajo"):
            st.markdown("1. Generación reproducible de correos sintéticos.\n"
                        "2. Ingesta y almacenamiento en HDFS.\n"
                        "3. Validación de datos y separación de registros con errores.\n"
                        "4. Transformación a Parquet y agregaciones con Spark.\n"
                        "5. Comparación de Hadoop Streaming con Spark RDD.\n"
                        "6. Clasificación de referencia con Naive Bayes en MLlib.")
            st.caption("Proyecto académico con datos sintéticos. No utiliza comunicaciones reales del Ayuntamiento.")
        st.divider()
    st.link_button("Explorar mis repositorios en GitHub", "https://github.com/Bilzarbe?tab=repositories")

else:
    heading("EXPERIENCIA", "Primeros pasos en ingeniería")
    html('<div class="timeline-item"><p class="eyebrow">JUNIO – JULIO 2026 · DONOSTIA / SAN SEBASTIÁN</p>'
         '<h3>Prácticas de ingeniería</h3><p class="organization">BieleDigital SL</p>'
         '<p>Experiencia profesional como estudiante en prácticas de ingeniería durante dos meses.</p></div>')
    heading("FORMACIÓN", "Una base técnica en crecimiento")
    html('<div class="timeline-item"><p class="eyebrow">2024 – ACTUALIDAD</p>'
         '<h3>Ingeniería en Inteligencia Artificial</h3>'
         '<p class="organization">Tecnun · Universidad de Navarra</p><p>Donostia / San Sebastián</p></div>'
         '<div class="timeline-item"><p class="eyebrow">2022 – 2024</p>'
         '<h3>Bachillerato de Ciencias y Tecnología</h3>'
         '<p class="organization">Zurriola Ikastola</p><p>Donostia / San Sebastián</p></div>')
    heading("OTROS DATOS", "Movilidad y compromiso")
    st.write("Permisos de conducir B y A1. Vehículo propio.")
    st.write("Entre mis aptitudes destacan la determinación, la perseverancia, el pensamiento crítico, "
             "la adaptabilidad y las habilidades de comunicación y colaboración.")

st.divider()
html('<div class="closing"><p class="eyebrow">CONTACTO</p><h2>Sigamos la conversación.</h2>'
     '<p>Si quieres conocer mejor mi perfil o hablar sobre una oportunidad, puedes escribirme.</p>'
     '<a href="mailto:bilzarbe06@gmail.com">bilzarbe06@gmail.com</a></div>'
     '<footer>Beñat Ilzarbe Daza · Donostia / San Sebastián</footer>')
