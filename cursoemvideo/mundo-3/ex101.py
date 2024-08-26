'''crie um programa que tenha a função chamada voto() que vai receber como parametro o ano de nascimento de
uma pessoa, retornando um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL ou OBRIGATORIO
nas eleições'''
import datetime

data = datetime.date(2024,8,26)

import datetime
def voto(ano):
  anoAt = data.year 

  if ano <= 2006 and ano >= 1955:
    print(f"Com {anoAt - ano} anos: VOTO OBRIGATÓRIO")

  elif ano <= 1954 and ano > 1850:
    print(f"Com {anoAt - ano} anos: VOTO OPCIONAL")

  elif ano >= 2007: 
    print(f"Com {anoAt - ano} anos: VOTO NEGADO")


print("-"*30)
ano = int(input("Em que ano você nasceu? "))
voto(ano)