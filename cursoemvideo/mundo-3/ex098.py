'''Faça um programa que tenha uma função chamada contador(), que receba três parametros: inicio, fim e passo 
e realizar a contagem. seu programa tem que realizar três contagens através da função criada:
a) de 1 até 10, de 1 em 1
b) de 10 até 0, de 2 em 2
c) uma contagem personalizada'''
import time

def contador(inicio, fim, passo):
  print("-="*50)
  print(f"Contagem de {inicio} até {fim} de {passo} em {passo}")

  if inicio < fim: 
    c = inicio

    while c <= fim: 
      print(c, end=' ')
      c += passo

  elif inicio > fim: 

    c = fim

    while c <= inicio: 
      print(c, end=' ')
      c += passo

contador(1, 10, 1)
time.sleep(1)

contador(10, 0, 2)
time.sleep(1)

print("-="*50)
print("Agora é sua vez de personalizar a contagem!")
ini = int(input("Início: "))
fin = int(input("Fim: "))
pas = int(input("Passo: "))

contador(ini, fin, pas)