from google import genai
from google.genai import types
import textwrap

import os
from dotenv import load_dotenv

load_dotenv()

GEMINI_API_KEY = os.getenv("API_KEY_GEMINI") # chave da API GEMINI no .env
MODEL = 'gemini-2.5-flash'

PROMPT_USUARIO = "Me recomende um almoço rápido para hoje. Responda em duas linhas no máximo."

# CONTEXTO = ""
# CONTEXTO = "Você é um nutricionista vegano."
CONTEXTO = "Você é um chef Francês."
# CONTEXTO = "Você é um mineiro, sugira um prato típico de Minas Gerais."

def run_with_context(system_instruction: str, user_input: str) -> str:
    client = genai.Client(api_key=GEMINI_API_KEY)
    resp = client.models.generate_content(
        model=MODEL,
        contents=user_input,
        config=types.GenerateContentConfig(
            system_instruction=system_instruction,
            thinking_config=types.ThinkingConfig(thinking_budget=0)
        ),
    )
    return resp.text

if __name__ == "__main__":
    try:
        out = run_with_context(CONTEXTO, PROMPT_USUARIO)
        print(textwrap.dedent(out).strip())
    except Exception as e:
        print(f"[ERRO] {e}")
