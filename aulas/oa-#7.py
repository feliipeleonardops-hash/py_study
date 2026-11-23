#! 📌 ENTRADA DE DADOS E SOMA BÁSICA
n1 = int(input("Digite um número: "))
n2 = int(input("Digite mais um número: "))
s = n1 + n2
# Quatro formas de exibir o resultado
# Calculo usando variável
print("A soma vale {}".format(s))  # noqa: UP032
print(f"A soma vale {s}")
# Calculo direto na string (sem precisar de variável)
print("A soma vale {}".format(n1 + n2))  # noqa: UP032
print(f"A soma vale {n1 + n2}")

# 🧮 OPERADORES ARITMÉTICOS
#  +  -> Adição
#  -  -> Subtração
#  *  -> Multiplicação (Dica: 'Oi' * 5 repete o texto 5 vezes!)
#  /  -> Divisão
#  ** -> Exponenciação (ou use a função pow(base, expoente))
#  // -> Divisão Inteira (ignora o que vem depois da vírgula)
#  %  -> Resto da divisão


# 👑 ORDEM DE PRECEDÊNCIA (Quem o Python resolve primeiro?)
# 1º -> ( )      Parênteses
# 2º -> **       Exponenciação
# 3º -> * / // % Multiplicação, Divisão, Divisão Inteira e Resto
# 4º -> + -      Adição e Subtração


# ✨ ESPECIFICADORES DE FORMATO (Alinhamento em strings)
# Imagine que {:20} reserva um espaço fixo de 20 caracteres para o texto:

print("{:>20}".format("Texto"))  # Alinha à DIREITA (espaços preenchem a esquerda)
print("{:<20}".format("Texto"))  # Alinha à ESQUERDA (comportamento padrão)
print("{:^20}".format("Texto"))  # CENTRALIZA o texto no espaço de 20 caracteres
print(
    "{:=^20}".format("Oi")
)  # CENTRALIZA e preenche os lados vazios com '=' (=======Oi=======)
