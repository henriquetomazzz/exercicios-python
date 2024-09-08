'''Crie um programa que leia o ano de nascimento de sete pessoas. No final mostre qauntas pessoas ainda não atingiram
a maioridade e quantos já são de maiores.'''
for c in range(1, 8):
  idade = int(input("Digite a sua idade: "))
  
  if idade < 18:
    print("Você não atingiou a maioridade!")
  elif idade >= 18:
    print("Você já atingiu a maioridade!")
