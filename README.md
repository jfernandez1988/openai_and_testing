# Generador de Casos de Pruebas

Este repositorio contiene un generador de casos de pruebas utilizando el modelo de lenguaje GPT-3.5 de OpenAI. El código proporciona una interfaz simple para interactuar con el modelo y generar casos de prueba a partir de un requerimiento proporcionado por el usuario.

## Requisitos

Antes de ejecutar el código, asegúrate de tener instaladas las siguientes bibliotecas de Python:

- `openai`
- `gradio`
- `langchain`

Además, necesitarás una clave de API válida de OpenAI para utilizar el modelo de lenguaje GPT-3.5. La clave de API se debe configurar en el archivo `scripts/config.py` en la variable `openai_api_key`.

## Instrucciones de Uso

1. Clona este repositorio en tu máquina local.
2. Instala las bibliotecas requeridas si aún no lo has hecho:
   ```
   pip install openai gradio langchain
   ```
3. Configura tu clave de API de OpenAI en el archivo `scripts/config.py`.
4. Ejecuta el script `main.py` para iniciar la aplicación de generación de casos de prueba.

## Código

El código principal del generador de casos de prueba se encuentra en el archivo `main.py`. A continuación, se presenta una breve descripción de las principales funciones y clases utilizadas:

### Función `chat`

La función `chat(text)` es la función principal que interactúa con el modelo de lenguaje GPT-3.5 para generar los casos de prueba. Toma como entrada un texto que representa el requerimiento del cual se desean generar los casos de prueba. Utiliza plantillas de mensajes tanto para el sistema como para el humano para establecer la conversación con el modelo.

### Interfaz Gráfica con Gradio

El código también proporciona una interfaz gráfica interactiva utilizando la biblioteca Gradio. La interfaz permite a los usuarios ingresar un requerimiento y obtener los casos de prueba generados por el modelo como resultado.

## Ejecución

Para ejecutar la aplicación, simplemente ejecuta el script `main.py` y la interfaz gráfica se abrirá en tu navegador web. Ingresa un requerimiento en el cuadro de texto y haz clic en el botón para obtener los casos de prueba generados por el modelo.

¡Esperamos que este generador de casos de prueba te resulte útil! Si tienes alguna pregunta o comentario, no dudes en contactarnos.

## Notas adicionales

- Asegúrate de tener una conexión a Internet activa para que el modelo de lenguaje GPT-3.5 funcione correctamente.
- Si encuentras algún problema o error, por favor repórtalo en la sección de "Issues" en este repositorio para que podamos ayudarte a resolverlo.
