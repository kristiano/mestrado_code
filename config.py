import os
from dotenv import load_dotenv
import streamlit as st

# Carrega as variáveis do arquivo .env (se existir, ex: no ambiente local do Mac)
load_dotenv()

# Tenta obter a chave da API primeiro pelo sistema operacional
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

# Se não achou (ex: no Streamlit Cloud), tenta pegar pelo repositório de Secrets deles
if not GEMINI_API_KEY:
    try:
        GEMINI_API_KEY = st.secrets["GEMINI_API_KEY"]
    except (FileNotFoundError, KeyError):
        pass

if not GEMINI_API_KEY:
    raise ValueError("A chave GEMINI_API_KEY não foi encontrada. Configure no .env local ou nos Secrets do Streamlit Cloud.")
