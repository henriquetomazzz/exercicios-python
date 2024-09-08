'''Crie um programa que leia uma frase e diga se ela é um palindromo, desconsiderando os espaços'''
frase = input("Digite uma frase: ")
fraseSemEspaco = frase.replace(" ", "").lower()

for c in range(1, 2):
  if fraseSemEspaco == fraseSemEspaco[::-1]:
    print("É um palindromo")
  else: 
    print("Não é um palindromo")
