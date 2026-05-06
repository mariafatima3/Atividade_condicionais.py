# 7) Conversão de Notas: Escreva um programa que converte uma nota de 0 a 100 em uma escala de conceitos: A (90-100), 
# B (80-89), C (70-79), D (60-69) e F (0-59).

nota = float(input("Digite a nota (0 a 100): "))

if nota < 0 or nota > 100:
    print("Nota inválida! Digite um valor entre 0 e 100.")
else:
    # Converte a nota em conceito
    if nota >= 90:
        conceito = 'A'
    elif nota >= 80:
        conceito = 'B'
    elif nota >= 70:
        conceito = 'C'
    elif nota >= 60:
        conceito = 'D'
    else:
        conceito = 'F'
    
    print(f"A nota {nota} corresponde ao conceito '{conceito}'.")