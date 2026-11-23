# CORES NO TERMINAL
# ANSI -> Escape Sequence
# Base --> Style ; text ; background
# Exemplo --> \033[style;text;backm

'''
STYLE 
[0 -> None], [1 -> Bold], [4 -> Underline], [7 -> Negative]
'''
'''
TEXT
[30 - white]  -->  # Branco/Preto (cor de texto padrão)
[31 - red]    -->  # Vermelho -> Erros, falhas e alertas críticos
[32 - green]  -->  # Verde -> Sucesso, confirmações e status OK (recomendado)
[33 - yellow] -->  # Amarelo -> Avisos (warnings) e valores em destaque (recomendado)
[34 - blue]   -->  # Azul -> Destaques gerais (excelente para fundo claro)
[35 - purple] -->  # Roxo/Magenta -> Tags e categorias secundárias
[36 - cyan]   -->  # Ciano -> Informações, caminhos de arquivo e links (recomendado)
[37 - gray]   -->  # Cinza -> Textos secundários e logs desativados
'''
'''
BACKGROUND
[40 - white]  -->  # Branco/Preto (cor de texto padrão)
[41 - red]    -->  # Vermelho -> Erros, falhas e alertas críticos
[42 - green]  -->  # Verde -> Sucesso, confirmações e status OK (recomendado)
[43 - yellow] -->  # Amarelo -> Avisos (warnings) e valores em destaque (recomendado)
[44 - blue]   -->  # Azul -> Destaques gerais (excelente para fundo claro)
[45 - purple] -->  # Roxo/Magenta -> Tags e categorias secundárias
[46 - cyan]   -->  # Ciano -> Informações, caminhos de arquivo e links (recomendado)
[47 - gray]   -->  # Cinza -> Textos secundários e logs desativados
'''
print('\033[1;30;47mOlá, Mundo!\033[m')