# Beñat Ilzarbe Daza · CV y portfolio de inteligencia artificial

[Beñat Ilzarbe — CV y portfolio](https://benatilzarbe.streamlit.app/)

[Portada pública de Beñat Ilzarbe / Benat Ilzarbe](https://bilzarbe.github.io/BenatIlzarbe.github.io/)

Portfolio personal de **Beñat Ilzarbe Daza (Benat Ilzarbe)**, estudiante de Ingeniería en Inteligencia Artificial en Tecnun – Universidad de Navarra, en Donostia / San Sebastián.

Web personal desarrollada con Streamlit. Presenta mi formación en Ingeniería en Inteligencia Artificial, mis prácticas en BieleDigital centradas en la detección de defectos con deep learning y mi participación actual en Talento Deportivo.

Incluye un selector de castellano e inglés que traduce la navegación y el contenido, conservando la sección seleccionada. El CV descargable es una versión pública en castellano, sin teléfono ni fecha de nacimiento.

## Proyectos

- **Olist E-Commerce:** organización y depuración de datos de comercio electrónico, análisis con SQL y panel interactivo con PostgreSQL, Python y Streamlit.
- **Playing Card Classification:** clasificación de imágenes de cartas mediante redes convolucionales y transfer learning.
- **Chipless RFID Classification:** identificación de etiquetas RFID sin chip a partir de señales ruidosas mediante machine learning y deep learning.
- **DonostIArrak:** procesamiento distribuido de correos ciudadanos sintéticos con Spark y Hadoop. Con este proyecto participé en el concurso Donostia Open Minds.

La sección de proyectos ofrece un resumen breve de cada trabajo y enlaces a los repositorios públicos.

## Ejecutar en local

Con Python 3.12 instalado, abre una terminal dentro de la carpeta del proyecto:

```powershell
py -3.12 -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe -m streamlit run app.py
```

## Despliegue

La aplicación está conectada a Streamlit Community Cloud con esta configuración:

- Repositorio: `Bilzarbe/BenatIlzarbe.github.io`
- Rama: `main`
- Archivo principal: `app.py`
- Python: `3.12`
- Subdominio: `benatilzarbe`

Los cambios guardados en la rama `main` se despliegan desde Streamlit Community Cloud.

La carpeta `docs/` contiene una portada estática para GitHub Pages, con descripción, datos estructurados del perfil y `sitemap.xml`. GitHub Pages publica desde `main` y `/docs`. Esta portada permite verificar su propia dirección en Google Search Console; esa verificación no verifica el subdominio de Streamlit.

## Personalizar

- **Textos, proyectos y enlaces:** `app.py`.
- **Colores y tipografía:** `assets/style.css` y `.streamlit/config.toml`.
- **Foto:** `assets/benat.png`.
- **CV público descargable:** `assets/CV_Benat_Ilzarbe_Publico.pdf`.

El PDF original se ha retirado del historial de Git. Su ruta está excluida en `.gitignore` para evitar volver a publicarlo por accidente. Los textos de la web se mantienen de forma independiente en `app.py`.
