# 3) Calculadora Simples: Faça uma calculadora que pede ao usuário dois números e uma operação (+, -, *, /) 
# e retorna o resultado dessa operação.

numero_1 = int(input("Digite o primeiro número: "))
numero_2 = int(input("Digite o segundo número: ")) 
operacao = input("Digite a operação (+, -, *, /): ")

if operacao == "+":
    resultado = numero_1 + numero_2
elif operacao == "-":
    resultado = numero_1 - numero_2
elif operacao == "*":
    resultado = numero_1 * numero_2
elif operacao == "/":
    if numero_2 != 0:
        resultado = numero_1 / numero_2
    else:
        resultado = "Erro: divisão por zero!"
else:
    resultado = "Operação inválida!"

print("Resultado:", resultado)

