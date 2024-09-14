'''Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final mostre os 10 primeiros termos dessa
progressão'''
termo = int(input("Primeiro termo: "))
razao = int(input("Razão: "))
decimo = termo + (9)*razao

for i in range(termo, decimo+razao, razao):
  print(f"{i}", end='-> ')
print("ACABOU")