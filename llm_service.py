from google import genai
from google.genai import types
from config import GEMINI_API_KEY
import json

# Instancia o cliente global
cliente = genai.Client(api_key=GEMINI_API_KEY)

def criar_modelo(model_name="gemini-2.5-flash", system_instruction=None):
    """
    Retorna o nome do modelo, o cliente instanciado globalmente e o schema/instruções.
    Na nova SDK, não instanciamos o modelo em si de antemão, passamos os parâmetros 
    na hora de gerar o conteúdo.
    """
    
    # Verifica se há instrução do sistema
    sys_inst = [system_instruction] if system_instruction else None

    # Configura a geração para garantir JSON na saída
    config = types.GenerateContentConfig(
        response_mime_type="application/json",
        temperature=0.2,
        system_instruction=sys_inst
    )

    return model_name, cliente, config

