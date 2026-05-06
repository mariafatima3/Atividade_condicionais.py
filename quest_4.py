# 4) Maior de Três Números: Escreva um programa que solicita três números ao usuário e retorna o maior dentre eles.

numero_1 = int(input("Digite o primeiro número: "))
numero_2 = int(input("Digite o segundo número: ")) 
numero_3 = int(input("Digite o terceiro número: "))

if numero_1 > numero_2 and numero_1 > numero_3:
    maior = numero_1
elif numero_2 > numero_1 and numero_2 > numero_3:
    maior = numero_2
else:
    maior = numero_3

print(f"O maior número é: {maior}")
