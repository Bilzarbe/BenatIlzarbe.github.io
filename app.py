"""Bilingual CV and portfolio. Run with: streamlit run app.py."""

from html import escape
from pathlib import Path

import streamlit as st

ROOT = Path(__file__).resolve().parent
lang = st.session_state.get("language", "es")
st.set_page_config(
    page_title="Beñat Ilzarbe | " + ("Inteligencia Artificial" if lang == "es" else "Artificial Intelligence"),
    page_icon="✳", layout="wide", initial_sidebar_state="collapsed",
)
st.html((ROOT / "assets" / "style.css").read_text(encoding="utf-8"))


def tr(es, en):
    return es if lang == "es" else en


def html(text):
    st.html(text)


def heading(eyebrow, title, description=""):
    html(f'<div class="section-heading"><p class="eyebrow">{escape(eyebrow)}</p>'
         f'<h2>{escape(title)}</h2><p class="section-intro">{escape(description)}</p></div>')


def tags(items):
    html('<p class="skills-line">' + ' <span aria-hidden="true">/</span> '.join(escape(x) for x in items) + '</p>')


html('<div class="masthead"><span class="wordmark">BI.</span>'
     '<span>BEÑAT ILZARBE DAZA</span><span class="masthead-location">DONOSTIA / SAN SEBASTIÁN</span></div>')
_, language_column = st.columns([2, 1])
with language_column:
    lang = st.radio("Idioma / Language", ["es", "en"],
                    format_func=lambda value: {"es": "Castellano", "en": "English"}[value],
                    key="language", horizontal=True, label_visibility="collapsed")

intro, portrait = st.columns([3, 1], gap="large")
with intro:
    eyebrow = tr("INGENIERÍA EN INTELIGENCIA ARTIFICIAL", "ARTIFICIAL INTELLIGENCE ENGINEERING")
    introduction = tr(
        "Estudiante de Ingeniería en Inteligencia Artificial en Tecnun – Universidad de Navarra. "
        "Soy una persona curiosa y constante, con ganas de seguir aprendiendo, afrontar nuevos retos y aportar en equipo.",
        "Artificial Intelligence Engineering student at Tecnun – University of Navarra. "
        "I am curious and persistent, eager to keep learning, take on new challenges and contribute as part of a team.",
    )
    html(f'<p class="eyebrow hero-eyebrow">{escape(eyebrow)}</p>'
         '<h1>Beñat<br><em>Ilzarbe Daza.</em></h1>'
         f'<p class="hero-intro">{escape(introduction)}</p>')
with portrait:
    st.image(str(ROOT / "assets" / "benat.png"), width=250)
    subtitle = tr("Inteligencia artificial · Datos · Aprendizaje", "Artificial intelligence · Data · Learning")
    html(f'<p class="portrait-caption">Beñat Ilzarbe Daza<br>{escape(subtitle)}</p>')

contact, github, download = st.columns(3)
with contact:
    st.link_button(tr("Hablemos por email", "Get in touch"), "mailto:bilzarbe06@gmail.com", width="stretch", type="primary")
with github:
    st.link_button(tr("Ver mi GitHub", "View my GitHub"), "https://github.com/Bilzarbe", width="stretch")
with download:
    st.download_button(tr("Descargar CV en PDF", "Download CV (Spanish PDF)"),
                       (ROOT / "assets" / "CV_Benat_Ilzarbe.pdf").read_bytes(),
                       file_name="CV_Benat_Ilzarbe.pdf", mime="application/pdf", width="stretch")

st.divider()
section_names = {
    "about": tr("Sobre mí", "About me"),
    "projects": tr("Proyectos", "Projects"),
    "background": tr("Trayectoria", "Background"),
}
section = st.radio("Explora mi perfil / Explore my profile", list(section_names),
                   format_func=section_names.get, key="section", horizontal=True, label_visibility="collapsed")

if section == "about":
    heading(tr("PERFIL", "PROFILE"), tr("Formación en IA y experiencia aplicada", "AI studies and practical experience"))
    left, right = st.columns([1.4, 1], gap="large")
    with left:
        st.write(tr(
            "Estudio Ingeniería en Inteligencia Artificial desde 2024. Me interesan el machine learning, "
            "el deep learning y el análisis de datos: entender el problema, probar distintas soluciones y evaluar lo que funciona.",
            "I have been studying Artificial Intelligence Engineering since 2024. I am interested in machine learning, "
            "deep learning and data analysis: understanding a problem, trying different approaches and evaluating what works.",
        ))
        st.write(tr(
            "Puedo trabajar con datos, desarrollar y evaluar modelos de inteligencia artificial y abordar problemas "
            "de visión artificial. Mi formación también me permite programar soluciones y trabajar con herramientas de procesamiento de datos.",
            "I can work with data, develop and evaluate AI models, and tackle computer vision problems. "
            "My studies also equip me to build software solutions and work with data processing tools.",
        ))
        st.write(tr(
            "En verano de 2026 realicé prácticas de ingeniería en BieleDigital SL, centradas en la detección de defectos mediante deep learning.",
            "In summer 2026, I completed an engineering internship at BieleDigital SL focused on defect detection using deep learning.",
        ))
        st.write(tr(
            "Me definen la disciplina, la capacidad de aprender y el compromiso. Disfruto colaborando con otras personas y aportando en entornos nuevos.",
            "Discipline, a willingness to learn and commitment define how I work. I enjoy collaborating with others and contributing in new environments.",
        ))
    with right:
        quote = tr("El deporte me ha enseñado a mantener la constancia, también cuando los resultados necesitan tiempo.",
                   "Sport has taught me to stay consistent, even when results take time.")
        html(f'<div class="pullquote">{escape(quote)}</div>')

    heading(tr("CONOCIMIENTOS", "SKILLS"), tr("Herramientas con las que trabajo", "Tools I work with"))
    a, b, c = st.columns(3, gap="large")
    with a:
        st.subheader(tr("Programación", "Programming"))
        tags(["Python", "C++", "MATLAB", "R", "HTML", "JavaScript"])
    with b:
        st.subheader(tr("IA y análisis", "AI and analytics"))
        tags(["Machine Learning", "Deep Learning", "Power BI"])
    with c:
        st.subheader(tr("En mis proyectos", "Project tools"))
        tags(["TensorFlow / Keras", "scikit-learn", "Spark", "Hadoop", "Docker"])
    st.caption(tr("Las herramientas de la última columna aparecen en los proyectos académicos del portfolio.",
                  "The tools in the last column are used in the academic projects in this portfolio."))

    heading(tr("IDIOMAS", "LANGUAGES"), tr("Tres idiomas para conectar", "Connecting in three languages"))
    a, b, c = st.columns(3)
    with a:
        st.subheader(tr("Euskera", "Basque"))
        st.write(tr("Lengua materna", "Mother tongue"))
        st.caption(tr("Certificaciones B1, B2 y C1 de HABE", "HABE B1, B2 and C1 certificates"))
    with b:
        st.subheader(tr("Castellano", "Spanish"))
        st.write(tr("Nativo", "Native"))
    with c:
        st.subheader(tr("Inglés", "English"))
        st.write(tr("Avanzado", "Advanced"))
        st.caption(tr("Cambridge First Certificate y cursos en Reino Unido", "Cambridge First Certificate and courses in the United Kingdom"))

    heading(tr("FUERA DEL AULA", "BEYOND THE CLASSROOM"),
            tr("El deporte forma parte de mi manera de trabajar", "Sport shapes the way I work"))
    st.write(tr(
        "He practicado ciclismo y natación durante años, con medallas en campeonatos provinciales, autonómicos y de ámbito nacional. "
        "En 2022 entrené en el grupo de tecnificación de la Federación Guipuzcoana de Natación.",
        "I have practised cycling and swimming for years, winning medals at provincial, regional and national championships. "
        "In 2022, I trained with the development squad of the Gipuzkoa Swimming Federation.",
    ))
    st.write(tr(
        "Actualmente formo parte de Talento Deportivo, el programa de la Universidad de Navarra que acompaña el desarrollo académico, profesional, deportivo y personal.",
        "I am currently part of Talento Deportivo, the University of Navarra programme supporting academic, professional, sporting and personal development.",
    ))

elif section == "projects":
    heading("PORTFOLIO", tr("Proyectos de inteligencia artificial y datos", "AI and data projects"),
            tr("Una selección de mis trabajos académicos y su enfoque.", "A selection of my academic projects and their focus."))
    projects = [
        {
            "area": tr("VISIÓN ARTIFICIAL", "COMPUTER VISION"),
            "name": "Playing Card Classification",
            "description": tr(
                "Clasificación de imágenes de cartas de una baraja mediante redes convolucionales. El proyecto se centra en comparar modelos "
                "de deep learning y mejorar su rendimiento con transfer learning y combinación de modelos.",
                "Classifying playing card images using convolutional neural networks. The project focuses on comparing deep learning models "
                "and improving their performance through transfer learning and model ensembles.",
            ),
            "tags": ["Python", "TensorFlow / Keras", "Optuna"],
            "url": "https://github.com/Bilzarbe/PokerCards_Predictions_ConvolutionalNetworks",
            "button": tr("Ver proyecto de cartas en GitHub", "View card classification on GitHub"),
        },
        {
            "area": tr("DEEP LEARNING / SEÑALES", "DEEP LEARNING / SIGNALS"),
            "name": "Chipless RFID Classification",
            "description": tr(
                "Identificación de etiquetas RFID sin chip a partir de señales ruidosas. El proyecto se centra en aplicar machine learning "
                "y deep learning para reconocer patrones en las señales y estudiar cómo afecta la distancia de lectura.",
                "Identifying chipless RFID tags from noisy signals. The project focuses on applying machine learning and deep learning "
                "to recognise signal patterns and study the effect of reading distance.",
            ),
            "tags": ["Python", "TensorFlow / Keras", "scikit-learn"],
            "url": "https://github.com/Bilzarbe/Chiplees_RFID_Classification",
            "button": tr("Ver proyecto RFID en GitHub", "View RFID classification on GitHub"),
        },
        {
            "area": "BIG DATA", "name": "DonostIArrak",
            "description": tr(
                "Procesamiento distribuido de correos ciudadanos sintéticos dirigidos al Ayuntamiento de Donostia. El proyecto se centra "
                "en organizar, validar y analizar grandes volúmenes de datos con Spark y Hadoop.",
                "Distributed processing of synthetic citizen emails addressed to Donostia City Council. The project focuses on organising, "
                "validating and analysing large volumes of data with Spark and Hadoop.",
            ),
            "participation": tr("Con este proyecto participé en el concurso Donostia Open Minds.",
                                "I took part in the Donostia Open Minds competition with this project."),
            "tags": ["Apache Spark", "Hadoop", "Docker", "PySpark"],
            "url": "https://github.com/Bilzarbe/DonostIArrak-Citizen-Email-Analytics-with-Apache-Spark-and-Hadoop",
            "button": tr("Ver DonostIArrak en GitHub", "View DonostIArrak on GitHub"),
        },
    ]
    for project in projects:
        html(f'<article class="project-heading"><p class="eyebrow">{escape(project["area"])}</p>'
             f'<h3>{escape(project["name"])}</h3></article>')
        st.write(project["description"])
        if project.get("participation"):
            st.write(project["participation"])
        tags(project["tags"])
        st.link_button(project["button"], project["url"])
    st.divider()
    st.link_button(tr("Explorar mis repositorios en GitHub", "Explore my GitHub repositories"),
                   "https://github.com/Bilzarbe?tab=repositories")

else:
    heading(tr("EXPERIENCIA", "EXPERIENCE"), tr("Primeros pasos en ingeniería", "First steps in engineering"))
    date = tr("JUNIO – JULIO 2026", "JUNE – JULY 2026")
    role = tr("Prácticas de ingeniería", "Engineering internship")
    description = tr("Prácticas de ingeniería centradas en la detección de defectos mediante deep learning.",
                     "Engineering internship focused on defect detection using deep learning.")
    html(f'<div class="timeline-item"><p class="eyebrow">{date} · DONOSTIA / SAN SEBASTIÁN</p>'
         f'<h3>{escape(role)}</h3><p class="organization">BieleDigital SL</p><p>{escape(description)}</p></div>')
    heading(tr("FORMACIÓN", "EDUCATION"), tr("Una base técnica en crecimiento", "Building a technical foundation"))
    degree = tr("Ingeniería en Inteligencia Artificial", "Artificial Intelligence Engineering")
    university = tr("Tecnun · Universidad de Navarra", "Tecnun · University of Navarra")
    school = tr("Bachillerato de Ciencias y Tecnología", "Upper secondary education in Science and Technology")
    current = tr("2024 – ACTUALIDAD", "2024 – PRESENT")
    html(f'<div class="timeline-item"><p class="eyebrow">{current}</p><h3>{escape(degree)}</h3>'
         f'<p class="organization">{escape(university)}</p><p>Donostia / San Sebastián</p></div>'
         f'<div class="timeline-item"><p class="eyebrow">2022 – 2024</p><h3>{escape(school)}</h3>'
         '<p class="organization">Zurriola Ikastola</p><p>Donostia / San Sebastián</p></div>')
    heading(tr("OTROS DATOS", "OTHER INFORMATION"), tr("Movilidad y compromiso", "Mobility and commitment"))
    st.write(tr(
        "Actualmente participo en Talento Deportivo, el programa de la Universidad de Navarra que acompaña mi desarrollo académico, profesional, deportivo y personal.",
        "I currently take part in Talento Deportivo, the University of Navarra programme supporting my academic, professional, sporting and personal development.",
    ))
    st.write(tr("Permisos de conducir B y A1. Vehículo propio.", "B and A1 driving licences. Own vehicle."))
    st.write(tr(
        "Entre mis aptitudes destacan la determinación, la perseverancia, el pensamiento crítico, la adaptabilidad y las habilidades de comunicación y colaboración.",
        "My strengths include determination, perseverance, critical thinking, adaptability, communication and collaboration.",
    ))

st.divider()
closing = tr("Sigamos la conversación.", "Let's talk.")
closing_text = tr("Si quieres conocer mejor mi perfil o hablar sobre una oportunidad, puedes escribirme.",
                  "If you would like to learn more about my background or discuss an opportunity, feel free to get in touch.")
html(f'<div class="closing"><p class="eyebrow">{tr("CONTACTO", "CONTACT")}</p><h2>{escape(closing)}</h2>'
     f'<p>{escape(closing_text)}</p><a href="mailto:bilzarbe06@gmail.com">bilzarbe06@gmail.com</a></div>'
     '<footer>Beñat Ilzarbe Daza · Donostia / San Sebastián</footer>')
