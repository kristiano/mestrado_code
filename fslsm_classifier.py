import json
from llm_service import criar_modelo

SYSTEM_PROMPT = """Você é um especialista em educação focado no Modelo de Estilos de Aprendizagem de Felder-Silverman (FSLSM).
Seu objetivo é analisar as respostas de um estudante e classificá-lo nas 4 dimensões do modelo:
1. Compreensão: Sequencial vs Global
2. Percepção: Sensorial vs Intuitivo
3. Entrada: Visual vs Verbal
4. Processamento: Ativo vs Reflexivo

Você deve analisar as respostas fornecidas pelo usuário e retornar EXCLUSIVAMENTE um objeto JSON válido.
Nenhum texto adicional ou formatação Markdown (como ```json) deve ser incluído ao seu retorno.

Estrutura OBRIGATÓRIA do JSON:
{
    "compreensao": "Sequencial" | "Global",
    "percepcao": "Sensorial" | "Intuitivo",
    "entrada": "Visual" | "Verbal",
    "processamento": "Ativo" | "Reflexivo",
    "perfil_completo": "Resultado1-Resultado2-Resultado3-Resultado4",
    "justificativa": "Uma breve explicação de 2 linhas do porquê esse perfil foi escolhido."
}
"""

def classificar_perfil(respostas_aluno: str) -> dict:
    """
    Envia as respostas do aluno para o Gemini e retorna um dicionário
    com o perfil de Felder-Silverman.
    """
    model_name, cliente, config = criar_modelo(system_instruction=SYSTEM_PROMPT)
    
    prompt_usuario = f"Aqui estão as respostas do aluno sobre suas preferências de estudo:\n\n{respostas_aluno}\n\nClassifique este aluno."
    
    # Nova sintaxe para chamadas ao modelo
    resposta = cliente.models.generate_content(
        model=model_name,
        contents=prompt_usuario,
        config=config,
    )
    
    texto_resposta = resposta.text.strip()
    
    try:
        # Tenta interpretar o texto como JSON
        perfil_json = json.loads(texto_resposta)
        return perfil_json
    except json.JSONDecodeError as e:
        print(f"Erro ao converter a resposta da LLM para JSON: {e}")
        print(f"Resposta bruta da LLM: {texto_resposta}")
        # Retorna um perfil padrão/falha seguro
        return {
            "compreensao": "Indefinido",
            "percepcao": "Indefinido",
            "entrada": "Indefinido",
            "processamento": "Indefinido",
            "perfil_completo": "Erro na Classificação",
            "justificativa": "A LLM não retornou um formato JSON válido."
        }
