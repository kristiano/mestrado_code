import time
import streamlit as st
from fslsm_classifier import classificar_perfil
from content_adapter import adaptar_conteudo

# Configuração da página Web
st.set_page_config(page_title="Learnglish FSLSM", page_icon="🧠", layout="centered")

def main():
    st.title("📚 Learnglish - Mapeador de Perfil")
    st.markdown("Descubra seu Estilo de Aprendizagem baseado no modelo de **Felder-Silverman** usando Inteligência Artificial.")
    
    st.divider()
    
    with st.form("fslsm_form"):
        st.subheader("Questionário Vocacional")
        
        q1 = st.text_area("1. Como você prefere entender um assunto novo?", 
                          placeholder="Ex: Passo a passo sequencial ou entendendo o quadro geral primeiro?")
        
        q2 = st.text_area("2. Como você percebe e absorve informações em aula?", 
                          placeholder="Ex: Prefere fatos concretos/exemplos ou conceitos teóricos/inovadores?")
        
        q3 = st.text_area("3. Como você prefere que a informação seja apresentada?", 
                          placeholder="Ex: Gosta mais de diagramas/figuras ou de explicações escritas/faladas?")
        
        q4 = st.text_area("4. Como você processa os dados após aprender?", 
                          placeholder="Ex: Prefere debater com amigos em grupo ou refletir sozinho primeiro?")
                          
        submitted = st.form_submit_button("🧠 Analisar Perfil FSLSM")
        
    if submitted:
        if not q1 or not q2 or not q3 or not q4:
            st.error("Por favor, responda todas as perguntas para uma melhor análise.")
            return
            
        respostas_formatadas = (
            f"Pergunta 1: {q1}\n\n"
            f"Pergunta 2: {q2}\n\n"
            f"Pergunta 3: {q3}\n\n"
            f"Pergunta 4: {q4}"
        )
        
        with st.spinner("O Gemini está analisando suas respostas..."):
            perfil_resultado = classificar_perfil(respostas_formatadas)
            
        st.success("Análise Concluída com Sucesso!")
        
        st.header(f"Seu Perfil: {perfil_resultado.get('perfil_completo', 'Indefinido')}")
        
        # Colunas para exibir dimensões
        col1, col2 = st.columns(2)
        with col1:
            st.info(f"**Compreensão:** {perfil_resultado.get('compreensao')}")
            st.info(f"**Entrada:** {perfil_resultado.get('entrada')}")
        with col2:
            st.info(f"**Percepção:** {perfil_resultado.get('percepcao')}")
            st.info(f"**Processamento:** {perfil_resultado.get('processamento')}")
            
        st.markdown(f"**💡 Justificativa da IA:** {perfil_resultado.get('justificativa')}")
        
        st.divider()
        st.subheader("🛠️ Sugestões de Adaptação de Material Educacional")
        
        sugestoes = adaptar_conteudo(perfil_resultado)
        for s in sugestoes:
            st.markdown(f"- {s}")

if __name__ == "__main__":
    main()
