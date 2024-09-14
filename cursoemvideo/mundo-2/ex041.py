'''A confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua
categoria, de acordo com a idade:
-até 9 anos: mirim      -até 19 anos: junior    -acima: master
-até 14 anos: infantil  -até 25 anos: sênior '''
from datetime import date
ano = date.today().year
nascimento = int(input("Ano de nascimento: "))
idade = ano - nascimento

print(f"O atleta tem {idade} anos.")
if idade <= 9:
  print("Classificação: MIRIM")

elif idade > 9 and idade <= 14: 
  print("Classificação: INFANTIL")

elif idade > 14 and idade <= 19:
  print("Classificação: JÚNIOR")

elif idade > 19 and idade <= 25:
  print("Classificação: SÊNIOR")

elif idade > 25:
  print("Classificação: MASTER")
