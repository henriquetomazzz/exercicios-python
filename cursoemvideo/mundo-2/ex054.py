'''Crie um programa que leia o ano de nascimento de sete pessoas. No final mostre qauntas pessoas ainda não atingiram
a maioridade e quantos já são de maiores.'''
from datetime import date

for c in range(1, 8):
  ano = int(input("Digite o ano em que você nasceu: "))
  data = date.today().year
  
  if data-ano < 18:
    print("Você ainda não atingou a maioridade!")
  elif data-ano >= 18:
    print("Você já atingiu a maioridade!")
