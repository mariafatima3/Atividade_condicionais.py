# 1) Escreva um programa que solicita um número ao usuário e determina se é positivo, negativo ou zero.

numero = int(input("Digite um número: "))
# solução 1

if numero > 0:
    print("Positivo")
elif numero < 0:
        print("Negativo")
else:
            print("Zero")

# solução 2
resultado = "Positivo" if numero > 0 else "Negativo" if numero < 0 else "Zero"
print(resultado)
