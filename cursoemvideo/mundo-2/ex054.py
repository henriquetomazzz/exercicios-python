'''Crie um programa que leia o ano de nascimento de sete pessoas. No final mostre qauntas pessoas ainda não atingiram
a maioridade e quantos já são de maiores. Considerando a maioridade 21 anos'''
from datetime import date
data = date.today().year
maior = 0
menor = 0

for c in range(1, 8):
  ano = int(input(f"Digite o ano em que a {c} nasceu? "))
  idade = data - ano
  
  if idade >= 21:
    maior += 1
  else:
    menor += 1

print(f"Ao todo tivemos {maior} pessoas maiores de idade")
print(f"Ao todo tivemos {menor} pessoas menores de idade")
