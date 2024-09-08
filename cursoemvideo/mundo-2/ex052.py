'''Faça um programa que leia um número inteiro e diga se ele é ou não um número primo'''
entrada = int(input("Digite um número: "))
ePrimo = 0

for j in range(1, entrada + 1):     
  if entrada % j == 0:
    ePrimo += 1
      
if ePrimo == 2: 
  print('primo')
else:
  print('nao primo')