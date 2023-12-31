import openai
import pathlib
import sys
import csv
from datetime import datetime
_parentdir = pathlib.Path(__file__).parent.parent.parent.resolve()
sys.path.insert(0, str(_parentdir))
from scripts.config import Config

# Configurar la API key de OpenAI
cfg = Config()
openai.api_key = cfg.openai_api_key # Reemplaza "YOUR_API_KEY" con tu propia API key

txt_file_path = "req.txt" 

# Requerimiento para el cual deseamos generar casos de prueba
def obtener_requerimiento_desde_txt(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        requerimiento = file.read()
    return requerimiento

requerimiento = obtener_requerimiento_desde_txt(txt_file_path)

prompt = f"""Eres un QA Manual crea casos de pruebas **críticos e importantes** para este: {requerimiento} \n\n
        ###Los casos de prueba deben tener el siguiente formato **para luego guardar en csv**:
        1; Caso de prueba ; resultado esperado
        2; Caso de prueba ; resultado esperado
        3; caso de prueba ; resultado esperado
        ...###
        """
respuesta = openai.Completion.create(
    engine="text-davinci-003",
    prompt=prompt,
    temperature=0.8,
    max_tokens=800
)
texto_casos_de_prueba = respuesta.choices[0].text.strip()

# Convertir el texto en una lista de listas (casos de prueba)
casos_de_prueba = [linea.split("; ") for linea in texto_casos_de_prueba.split("\n")]

# Obtener la fecha y hora actual
fecha_hora_actual = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

# Nombre del archivo CSV con fecha y hora
nombre_archivo = f"test_openai_{fecha_hora_actual}.csv"

# Escribir los datos en el archivo CSV
with open(nombre_archivo, mode='w', newline='') as archivo_csv:
    writer = csv.writer(archivo_csv, delimiter=";")
    writer.writerow(["id", "Descripcion","Resultado esperado"])
    writer.writerows(casos_de_prueba)

print(f"Los casos de prueba se han guardado en el archivo '{nombre_archivo}'.")