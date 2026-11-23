"""Desafio 043 — Índice de Massa Corporal: Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu Índice de Massa Corporal (IMC) e mostre seu status de acordo com a tabela: Abaixo de 18.5 (Abaixo do Peso), entre 18.5 e 25 (Peso Ideal), 25 até 30 (Sobrepeso), 30 até 40 (Obesidade), acima de 40 (Obesidade Mórbida)."""

# Lê o peso e a altura do usuário
peso = float(input("Qual é o seu peso? (kg): "))
altura = float(input("Qual é a sua altura? (m): "))

# Calcula o IMC (Peso dividido pela altura ao quadrado)
imc = peso / (altura**2)

# Exibe o resultado formatado com 1 casa decimal
print(f"O seu IMC é de {imc:.1f}")

# Classifica de acordo com a tabela
if imc < 18.5:
    print("Status: **Abaixo do Peso**")
elif 18.5 <= imc < 25:
    print("Status: **Peso Ideal**")
elif 25 <= imc < 30:
    print("Status: **Sobrepeso**")
elif 30 <= imc < 40:
    print("Status: **Obesidade**")
else:
    print("Status: **Obesidade Mórbida**")
