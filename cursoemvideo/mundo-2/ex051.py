'''Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final mostre os 10 primeiros termos dessa
progressão'''
termo = int(input("Primeiro termo: "))
razao = int(input("Razão: "))

for i in range(termo, razao*11, razao):
  print(f"{i}", end='-> ')
print("ACABOU")