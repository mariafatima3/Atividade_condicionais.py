# 5) Classificação de Idade: Peça a idade do usuário e classifique-a em "Criança" (0-12), "Adolescente" (13-19), 
# "Adulto" (20-59) ou "Idoso" (60+).

idade = int(input("Digite sua idade: "))

if idade >= 0 and idade <= 12:
    print("Você é uma Criança.")
elif idade >= 13 and idade <= 19:
    print("Você é um Adolescente.")
elif idade >= 20 and idade <= 59:
    print("Você é um Adulto.")
elif idade >= 60:
    print("Você é um Idoso.")
else:
    print("Idade inválida.")