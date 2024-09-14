'''Faça um programa que leia o ano de nnascimento de um jovem e informe, de acordo com a sua idade se ele ainda 
vai se alistar ao serviço militar, se é a hora de se alistar ou se já passou do tempo do alistamento. Seu programa
também deverá mostrar o tempo que falta ou que passou do prazo'''
from datetime import date

ano = date.today().year
nascimento = int(input("Ano de nascimento: "))
idade = ano - nascimento

print(f"Quem nasceu em {nascimento} tem {idade} anos em {ano}.")

if idade == 18: 
  print("Você tem que se alistar IMEDIATAMENTE!")
elif idade < 18: 
  print(f"Você ainda não tem 18 anos. Ainda falta {18 - idade}")
elif idade > 18: 
  print(f"Você já deveria ter se alistado há {idade-18} anos")
