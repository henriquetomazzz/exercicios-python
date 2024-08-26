'''
2. Faça um programa que verifique se uma letra digitada é "F" ou "M".
Conforme a letra, escrever: F - Feminino, M - Masculino, Sexo Inválido.
Considere que o usuário vai digitar F e M maiúsculo.
'''
sexo = input("Digite o sexo: ")

if sexo == "F" or sexo == "M": 
  if sexo == "F":
    print("F - Feminino")
  elif sexo == "M":
    print("M - Masculino")
else: 
  print("Sexo Inválido")