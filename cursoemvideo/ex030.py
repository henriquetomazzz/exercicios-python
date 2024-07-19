'''Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.'''
val = int(input("Digite um número: "))

if val % 2 == 0: 
  print(f"{val} é um número PAR!")
else: 
  print(f"{val} é um número ÍMPAR!")