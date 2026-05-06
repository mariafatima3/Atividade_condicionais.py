# 6) Verificação de Triângulo: Peça ao usuário o comprimento de três lados e verifique se eles podem formar um triângulo. 
# Se sim, determine se é um triângulo equilátero, isósceles ou escaleno.

lado1 = float(input("Digite o comprimento do primeiro lado: "))
lado2 = float(input("Digite o comprimento do segundo lado: "))
lado3 = float(input("Digite o comprimento do terceiro lado: "))

if (lado1 + lado2 > lado3) and (lado1 + lado3 > lado2) and (lado2 + lado3 > lado1):
    print("Os lados podem formar um triângulo.")
    
    if lado1 == lado2 == lado3:
        print("Triângulo Equilátero (todos os lados iguais).")
    elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
        print("Triângulo Isósceles (dois lados iguais).")
    else:
        print("Triângulo Escaleno (todos os lados diferentes).")
else:
    print("Os lados NÃO podem formar um triângulo.")