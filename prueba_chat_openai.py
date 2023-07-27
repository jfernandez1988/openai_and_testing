import openai
from langchain import PromptTemplate
from langchain.chat_models import ChatOpenAI
from langchain.prompts import SystemMessagePromptTemplate, HumanMessagePromptTemplate, ChatPromptTemplate
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
chatgpt= ChatOpenAI(temperature=0, model_name="gpt-3.5-turbo-16k")
txt_file_path = "req.txt" 

# Requerimiento para el cual deseamos generar casos de prueba
def obtener_requerimiento_desde_txt(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        requerimiento = file.read()
    return requerimiento

req = obtener_requerimiento_desde_txt(txt_file_path)

#Armamos el template para el sistema
prompt_temp_sistema = PromptTemplate(
    template = """Eres un QA Manual crea casos de pruebas **críticos e importantes** para este: {requerimiento} \n\n
                ###Los casos de prueba deben tener el siguiente formato **para luego guardar en csv**:
                1; Caso de prueba ; resultado esperado
                2; Caso de prueba ; resultado esperado
                3; caso de prueba ; resultado esperado
                ...###
                """,
    input_variables=["requerimiento"]
)

template_sistema = SystemMessagePromptTemplate(prompt=prompt_temp_sistema)

#Armamos el template para el humano
#prompt_temp_humano = PromptTemplate(template="{texto}", input_variables=["texto"])
#template_humano = HumanMessagePromptTemplate(prompt=prompt_temp_humano)

chat_prompt = ChatPromptTemplate.from_messages([template_sistema])
chat_prompt_value = chat_prompt.format_prompt(requerimiento=req).to_messages()
chat_resp = chatgpt(chat_prompt_value)

# Convertir el texto en una lista de listas (casos de prueba)
casos_de_prueba = [linea.split("; ") for linea in chat_resp.content.split("\n")]
fecha_hora_actual = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
nombre_archivo = f"test_chatgpt_{fecha_hora_actual}.csv"

# Escribir los datos en el archivo CSV
with open(nombre_archivo, mode='w', newline='') as archivo_csv:
    writer = csv.writer(archivo_csv, delimiter=";")
    writer.writerow(["id", "Descripcion","Resultado esperado"])
    writer.writerows(casos_de_prueba)

print(f"Los casos de prueba se han guardado en el archivo '{nombre_archivo}'.")


