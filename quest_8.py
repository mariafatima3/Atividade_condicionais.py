# 8) Validação de Login: Crie um programa que pede ao usuário um nome de usuário e uma senha. 
# Se o nome de usuário for "admin" e a senha for "12345", exiba "Acesso concedido", caso contrário, exiba "Acesso negado".

nome = input("Digite seu nome: ")
senha = input("Digite sua senha: ")

nome_usuario = "admin"
senha_usuario = "12345"

if nome  == nome_usuario and senha == senha_usuario:
    print("Acesso concedido")

else:
    print("Acesso negado")
    
