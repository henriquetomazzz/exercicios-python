'''Escreva um programa que leia dois número inteiro e compare-os mostrando na tela uma mensagem: 
- O primeiro valor é maior
- O segundo valor é maior
- Não existe valor maior, os dois são iguais'''
primeiro = int(input("Primeiro número: "))
segundo = int(input("Segundo número: "))

if primeiro > segundo: 
  print("O PRIMEIRO valor é maior")

elif primeiro < segundo: 
  print("O SEGUNDO valor é maior")

elif primeiro == segundo: 
  print("Não existe valor maior, os dois são iguais")