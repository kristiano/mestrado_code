def adaptar_conteudo(perfil: dict) -> list:
    """
    Retorna uma lista de strings com sugestões de adaptação de conteúdo 
    educacional com base no perfil FSLSM mapeado.
    """
    sugestoes = []
    
    entrada = perfil.get('entrada', '')
    if entrada == 'Visual':
        sugestoes.append("**[Visual]**: Gerar infográficos, diagramas e mapas mentais para a próxima aula.")
    elif entrada == 'Verbal':
        sugestoes.append("**[Verbal]**: Priorizar textos detalhados, podcasts e explicações escritas passo-a-passo.")
        
    processamento = perfil.get('processamento', '')
    if processamento == 'Ativo':
        sugestoes.append("**[Ativo]**: Sugerir atividades práticas, quizzes instantâneos e fóruns de discussão em grupo.")
    elif processamento == 'Reflexivo':
        sugestoes.append("**[Reflexivo]**: Sugerir leituras complementares e atividades individuais de reflexão (ex: diário de bordo).")

    compreensao = perfil.get('compreensao', '')
    if compreensao == 'Sequencial':
        sugestoes.append("**[Sequencial]**: Apresentar o material de forma linear, do básico ao avançado.")
    elif compreensao == 'Global':
        sugestoes.append("**[Global]**: Mostrar a 'Big Picture' (visão geral) do projeto final antes de entrar nos detalhes.")

    percepcao = perfil.get('percepcao', '')
    if percepcao == 'Sensorial':
        sugestoes.append("**[Sensorial]**: Focar em fatos concretos, exemplos do mundo real e menos teorias abstratas.")
    elif percepcao == 'Intuitivo':
        sugestoes.append("**[Intuitivo]**: Trazer desafios inovadores, teorias complexas e incentivando a descoberta autônoma.")
    
    return sugestoes
