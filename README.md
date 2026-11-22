# Beñat Ilzarbe · CV y portfolio

Web personal desarrollada con Streamlit. Incluye perfil, formación, experiencia, conocimientos, idiomas y dos proyectos académicos: Chipless RFID Classification y DonostIArrak.

## Publicar con Streamlit Community Cloud

1. Descarga y descomprime esta carpeta.
2. Entra en el repositorio `Bilzarbe/BenatIlzarbe.github.io` y elige **Add file → Upload files**.
3. Sube **el contenido de esta carpeta a la raíz** del repositorio. `app.py` y `requirements.txt` deben quedar al mismo nivel que este README, no dentro de otra carpeta `benat-streamlit`.
4. Conserva las carpetas `assets/` y `.streamlit/`. Si el explorador oculta `.streamlit`, puedes crear `.streamlit/config.toml` con **Add file → Create new file** y copiar su contenido. La aplicación funciona sin ese archivo, pero perderá la configuración del tema.
5. Guarda los cambios con **Commit changes**.
6. Accede a https://share.streamlit.io/ y conecta tu cuenta de GitHub.
7. Pulsa **Create app**, indica que ya tienes una app y selecciona:
   - Repositorio: `Bilzarbe/BenatIlzarbe.github.io`
   - Rama: la rama donde hayas subido los archivos; normalmente `main`
   - Archivo principal: `app.py`
8. En **Advanced settings**, selecciona Python 3.12 para coincidir con el entorno usado en la comprobación.
9. Elige un subdominio disponible, por ejemplo `benat-ilzarbe`, y pulsa **Deploy**.

La dirección final será la que confirme Streamlit, terminada en `.streamlit.app`. El nombre del repositorio no obliga a usar GitHub Pages ni es necesario cambiarlo.

Documentación: https://docs.streamlit.io/deploy/streamlit-community-cloud/deploy-your-app/deploy

## Ejecutar en tu ordenador

Con Python 3.12 instalado, abre una terminal dentro de esta carpeta:

```powershell
py -3.12 -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe -m streamlit run app.py
```

## Archivos

```text
app.py
requirements.txt
README.md
.gitignore
.streamlit/
    config.toml
assets/
    style.css
    benat.png
    CV_Benat_Ilzarbe.pdf
```

## Personalizar

- **Textos, proyectos y enlaces:** `app.py`.
- **Colores y tipografía:** `assets/style.css` y `.streamlit/config.toml`.
- **Foto:** sustituye `assets/benat.png`.
- **CV descargable:** sustituye `assets/CV_Benat_Ilzarbe.pdf` conservando el nombre.
- **Futuras demos:** añade nuevas secciones o páginas cuando dispongas de modelos y datos aptos para publicación.

El gráfico de RFID permite explorar resultados ya registrados; no ejecuta el clasificador. Los datos de DonostIArrak son sintéticos. No se han añadido enlaces directos a repositorios de proyectos cuya ubicación en la cuenta de Beñat no está confirmada.

La foto y el PDF proceden del CV facilitado por Beñat. El PDF descargable conserva su contenido original, incluido el teléfono y la fecha de nacimiento. Las fuentes se cargan desde Google Fonts; si no están disponibles, se utilizan las fuentes de sistema.

## Estado

Versión preparada para subir a GitHub y publicar en Streamlit Community Cloud. La entrega de los archivos no publica automáticamente la web ni modifica el repositorio remoto.
