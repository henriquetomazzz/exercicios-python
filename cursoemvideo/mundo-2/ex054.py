'''Crie um programa que leia o ano de nascimento de sete pessoas. No final mostre qauntas pessoas ainda não atingiram
a maioridade e quantos já são de maiores. Considerando a maioridade 21 anos'''
from datetime import date
contador = 0
for c in range(1, 8):
  ano = int(input("Digite o ano em que você nasceu: "))
  data = date.today().year
  
  if data-ano < 21:
    print("Você ainda não atingou a maioridade!")
  elif data-ano >= 21:
    print("Você já atingiu a maioridade!")
    contador += 1

print(f"De todos os anos apresentados, {contador} são pessoas que atingiram a maioridade")
