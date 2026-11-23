"""
Desafio 062: Melhore o DESAFIO 061, perguntando para o usuário se ele quer mostrar mais alguns termons. O programa encerra quando ele disser que quer mostrar 0 termos.
"""

# Lê os dados iniciais da PA
primeiro_termo = int(input("Digite o primeiro termo da PA: "))
razao = int(input("Digite a razão da PA: "))

# Inicializa as variáveis de controle
termo_atual = primeiro_termo
contador = 1
total_termos = 0
mais_termos = 10  # O programa começa pedindo os 10 primeiros termos

# Laço principal que controla se o programa deve continuar ou parar
while mais_termos != 0:
    total_termos += mais_termos

    # Laço interno que calcula e mostra a quantidade de termos solicitada
    while contador <= total_termos:
        print(f"{termo_atual} → ", end="")
        termo_atual += razao
        contador += 1
    print("PAUSA")

    # Pergunta quantos termos a mais o usuário quer ver
    mais_termos = int(input("Quantos termos você quer mostrar a mais? "))

# Mensagem de encerramento exibindo o total de termos gerados
print(f"Progressão finalizada com {total_termos} termos mostrados.")
