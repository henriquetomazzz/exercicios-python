'''Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai 
continuar ou não. No final, mostre:
a) qual é o total gasto na compra
b) quantos produtos custam mais de R$1000
c) qual é o nome do produto mais barato'''
print("--"*15)
print("\tLOJA SUPER BARATÃO")
print("--"*15)

total = totMil = menor = cont = 0
barato = ''
while True: 
  nome = str(input("Nome do produto: "))
  preco = float(input("Preço: R$"))
  cont += 1 
  total += preco
  if preco > 100:
    totMil += 1
  if cont == 1 or preco < menor:
    menor = preco
    barato = nome

  resp = ' '

  while resp not in "SN":
    resp = str(input("Quer continuar? [S/N]")).strip().upper()[0]

  if resp in "N":
    break

print("--"*20 + " FIM DO PROGRAMA " + "--"*20)
print(f"O preço total da compra {total:.2f}")
print(f"Temos {totMil} produtos custando mais de R$1000.00")
print(f"O produto mais barato foi {barato} que custa R${menor:.2f}")