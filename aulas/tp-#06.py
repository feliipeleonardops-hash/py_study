#! 📌 ENTRADA DE DADOS
n1 = int(input("Digite um número: "))
n2 = int(input("Digite outro número: "))
s = n1 + n2

# 📺 3 FORMAS DE EXIBIR RESULTADOS (Output)
# Forma 1: Concatenação com vírgula (insere espaços automaticamente)
print("A soma entre os valores é igual a", s)

# Forma 2: Método .format() (Note o 'f' removido do início para o .format funcionar)
print("A soma entre {} e {} é igual a {}".format(n1, n2, s))  # noqa: UP032

# Forma 3: f-Strings (A mais moderna, legível e recomendada!)
print(f"A soma entre {n1} e {n2} é igual a {s}.")

# ⚠️ ATENÇÃO: Erro clássico de Concatenação
# print("A soma é: " + s)
# ❌ ERRO! Você não pode somar Texto (str) com Número (int) usando o operador '+'

# 🔍 DESCOBRINDO O TIPO DE UMA VARIÁVEL
# print(type(nome_da_variavel))

# 📦 TIPOS PRIMITIVOS EM PYTHON
# • int()   -> Inteiros: 7, -4, 0, 9875
# • float() -> Decimais (ponto flutuante): 4.5, 0.076, -15.223, 7.0
# • bool()  -> Booleans (Lógicos): True ou False (Sempre com a 1ª letra maiúscula)
# • str()   -> Strings (Textos): 'Olá', '7.5', '' (vazia)
