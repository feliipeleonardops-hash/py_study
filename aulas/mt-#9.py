#! 📌 Frases de exemplo
frase = "Curso em Vídeo Python"
frase_espaco = "   Aprenda Python   "

# ✂️ FATIAMENTO (Índice inicial : Índice final-1 : Passo)
print(frase[9])  # 'V'       -> Posição exata (lembrando que começa em 0)
print(frase[9:13])  # 'Víde'    -> Da posição 9 até a 12 (exclui a 13)
print(frase[9:21:2])  # 'VdoPto'  -> Da posição 9 à 20, pulando de 2 em 2
print(frase[:5])  # 'Curso'   -> Do início (0) até a posição 4
print(frase[15:])  # 'Python'  -> Da posição 15 até o final
print(frase[9::3])  # 'Vety'    -> Da posição 9 até o final, de 3 em 3

# 🔍 ANÁLISE
print(len(frase))  # 21 -> Comprimento total da string
print(frase.count("o"))  # 3  -> Conta quantas vezes a letra 'o' aparece
print(frase.count("o", 0, 13))  # 1  -> Conta 'o' apenas entre as posições 0 e 12
print(frase.find("deo"))  # 11 -> Posição onde começa o termo 'deo' (-1 se não achar)
print("Curso" in frase)  # True -> Verifica se a palavra existe na string

# ⚡ TRANSFORMAÇÃO E MODIFICAÇÃO
print(frase.replace("Python", "Android"))  # Troca uma palavra por outra
print(frase.upper())  # Tudo MAIÚSCULO
print(frase.lower())  # Tudo minúsculo
print(frase.capitalize())  # 1ª letra da frase maiúscula
print(frase.title())  # 1ª letra de CADA palavra em maiúscula

# 🧼 REMOÇÃO DE ESPAÇOS
print(
    frase_espaco.strip()
)  # 'Aprenda Python'  -> Remove espaços extras nas duas pontas
print(frase_espaco.rstrip())  # '   Aprenda Python' -> Remove espaços apenas à direita
print(frase_espaco.lstrip())  # 'Aprenda Python   ' -> Remove espaços apenas à esquerda

# 🧩 DIVISÃO E JUNÇÃO
print(
    frase.split()
)  # ['Curso', 'em', 'Vídeo', 'Python'] -> Divide nos espaços, gerando uma lista
print(
    "-".join(frase.split())
)  # 'Curso-em-Vídeo-Python'           -> Junta uma lista usando o separador '-'
