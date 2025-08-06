# Proyecto_Sprint7
Proyecto del sprint 7 para Tripleten "Visualizacion Interctiva de Datos con Streamlit y Plotly"

Descripción:

Esta aplicación web ha sido desarrollada con Streamlit, una herramienta sencilla y potente para crear interfaces interactivas en Python. Su objetivo principal es mostrar visualizaciones dinámicas de datos, permitiendo al usuario explorar la información a través de botones o casillas de verificación.

Actualmente, la aplicación genera dos tipos de gráficos:

Histograma: útil para observar la distribución de los valores de una variable.

Gráfico de dispersión (scatter plot): útil para visualizar la relación entre dos variables y detectar patrones o agrupaciones.

Funcionalidad
Visualización previa de un conjunto de datos generado aleatoriamente.

Botones o checkboxes para mostrar:

Un histograma de la variable x.

Un diagrama de dispersión de x vs y coloreado por categoría.

Uso de Plotly para gráficos interactivos.

App la cual puede ser modificada para agregar mas funcionalidades

Cómo ejecutar:

Asegúrate de tener Python y las librerías necesarias instaladas:

bash
Copy
Edit
pip install streamlit plotly pandas numpy
Ejecuta la aplicación con:

bash
Copy
Edit
streamlit run app.py
La aplicación se abrirá automáticamente en tu navegador web.

### Despliegue en Render

La aplicación ha sido desplegada en la plataforma Render, lo que permite acceder a ella desde cualquier navegador sin necesidad de instalar dependencias localmente.

Para lograr esto:

- Se creó un repositorio en GitHub con los archivos necesarios (`app.py`, `requirements.txt`, `vehicles_us.csv`, etc.).
- Se configuró Render para hacer deploy automático desde GitHub.
- Se incluyó `plotly` y otras dependencias en `requirements.txt` para asegurar la instalación correcta.
- Se utilizó el siguiente comando de inicio en Render:
  ```bash
  `streamlit run app.py`


  ### Link y reflexion del proyecto

  ``` [visita la app desplegada] (https://lecture-8-p2aw.onrender.com)

  este es el link para acceder a la app. 
  
  Finalizando con algunas reflexiones acerca del proyecto realizado, debo decir que esto abre la mente a las tecnologias que diariamente vemos como evolucionan para hacer de la ciencia de datos un completo arte que permite hacer estudios, analizar patrones y lo mas importante que se pueda compartir con el publico en general, no solo para hacer colaboraciones y trabajar en equipo, sino para transmitir al mundo los analizis mas relevantes e interesantes que puedan contribuir en cientos de temas.