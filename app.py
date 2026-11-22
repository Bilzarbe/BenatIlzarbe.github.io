"""CV y portfolio de Beñat Ilzarbe. Ejecutar: streamlit run app.py"""

from pathlib import Path
from html import escape

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
         '<h1>Beñat<br><em>Ilzarbe Daza.</em></h1>'
         '<p class="hero-intro">Estudiante de Ingeniería en Inteligencia Artificial en '
         'Tecnun – Universidad de Navarra. Desarrollo proyectos de visión artificial, deep learning '
         'y procesamiento de datos. En mis prácticas en BieleDigital trabajé en la detección '
         'de defectos mediante deep learning.</p>')
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
    heading("PERFIL", "Formación en IA y experiencia aplicada")
    left, right = st.columns([1.4, 1], gap="large")
    with left:
        st.write("Estudio Ingeniería en Inteligencia Artificial desde 2024. Me interesan el machine learning, "
                 "el deep learning y el análisis de datos: entender el problema, probar distintas soluciones "
                 "y evaluar lo que funciona.")
        st.write("En mis proyectos académicos he trabajado con clasificación de imágenes de cartas, "
                 "clasificación de señales RFID y procesamiento distribuido de datos. En verano de 2026 "
                 "realicé prácticas de ingeniería en BieleDigital SL, centradas en la detección de defectos "
                 "mediante deep learning.")
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
    st.write("Actualmente formo parte de Talento Deportivo, el programa de la Universidad de Navarra "
             "que acompaña el desarrollo académico, profesional, deportivo y personal.")

elif section == "Proyectos":
    heading("PORTFOLIO", "Proyectos de inteligencia artificial y datos",
            "Una selección de mis trabajos académicos y su enfoque.")

    html('<article class="project-heading"><p class="eyebrow">VISIÓN ARTIFICIAL</p>'
         '<h3>Playing Card Classification</h3></article>')
    st.write("Clasificación de imágenes de cartas de una baraja mediante redes convolucionales. "
             "El proyecto se centra en comparar modelos de deep learning y mejorar su rendimiento "
             "con transfer learning y combinación de modelos.")
    tags(["Python", "TensorFlow / Keras", "Optuna"])
    st.link_button("Ver proyecto de cartas en GitHub",
                   "https://github.com/Bilzarbe/PokerCards_Predictions_ConvolutionalNetworks")

    html('<article class="project-heading"><p class="eyebrow">DEEP LEARNING / SEÑALES</p>'
         '<h3>Chipless RFID Classification</h3></article>')
    st.write("Identificación de etiquetas RFID sin chip a partir de señales ruidosas. "
             "El proyecto se centra en aplicar machine learning y deep learning para reconocer "
             "patrones en las señales y estudiar cómo afecta la distancia de lectura.")
    tags(["Python", "TensorFlow / Keras", "scikit-learn"])
    st.link_button("Ver proyecto RFID en GitHub", "https://github.com/Bilzarbe/Chiplees_RFID_Classification")

    html('<article class="project-heading"><p class="eyebrow">BIG DATA</p>'
         '<h3>DonostIArrak</h3></article>')
    st.write("Procesamiento distribuido de correos ciudadanos sintéticos dirigidos al Ayuntamiento "
             "de Donostia. El proyecto se centra en organizar, validar y analizar grandes volúmenes "
             "de datos con Spark y Hadoop.")
    tags(["Apache Spark", "Hadoop", "Docker", "PySpark"])

    st.divider()
    st.link_button("Explorar mis repositorios en GitHub", "https://github.com/Bilzarbe?tab=repositories")

else:
    heading("EXPERIENCIA", "Primeros pasos en ingeniería")
    html('<div class="timeline-item"><p class="eyebrow">JUNIO – JULIO 2026 · DONOSTIA / SAN SEBASTIÁN</p>'
         '<h3>Prácticas de ingeniería</h3><p class="organization">BieleDigital SL</p>'
         '<p>Prácticas de ingeniería centradas en la detección de defectos mediante deep learning.</p></div>')
    heading("FORMACIÓN", "Una base técnica en crecimiento")
    html('<div class="timeline-item"><p class="eyebrow">2024 – ACTUALIDAD</p>'
         '<h3>Ingeniería en Inteligencia Artificial</h3>'
         '<p class="organization">Tecnun · Universidad de Navarra</p><p>Donostia / San Sebastián</p></div>'
         '<div class="timeline-item"><p class="eyebrow">2022 – 2024</p>'
         '<h3>Bachillerato de Ciencias y Tecnología</h3>'
         '<p class="organization">Zurriola Ikastola</p><p>Donostia / San Sebastián</p></div>')
    heading("OTROS DATOS", "Movilidad y compromiso")
    st.write("Actualmente participo en Talento Deportivo, el programa de la Universidad de Navarra "
             "que acompaña mi desarrollo académico, profesional, deportivo y personal.")
    st.write("Permisos de conducir B y A1. Vehículo propio.")
    st.write("Entre mis aptitudes destacan la determinación, la perseverancia, el pensamiento crítico, "
             "la adaptabilidad y las habilidades de comunicación y colaboración.")

st.divider()
html('<div class="closing"><p class="eyebrow">CONTACTO</p><h2>Sigamos la conversación.</h2>'
     '<p>Si quieres conocer mejor mi perfil o hablar sobre una oportunidad, puedes escribirme.</p>'
     '<a href="mailto:bilzarbe06@gmail.com">bilzarbe06@gmail.com</a></div>'
     '<footer>Beñat Ilzarbe Daza · Donostia / San Sebastián</footer>')
