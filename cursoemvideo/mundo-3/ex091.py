'''Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios. Guarde esses resultados em um
dicionário em Python. No final coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número de dado'''
from random import randint
from time import sleep
from operator import itemgetter

jogadores = {'Jogador1': randint(1,6),
             'Jogador2': randint(1,6),
             'Jogador3': randint(1,6),
             'Jogador4': randint(1,6)}

print('Valores sorteado: ')
for k,v in jogadores.items(): 
  print(f'{k} tirou no {v} no dado.')
  sleep(1)

ranking = sorted(jogadores.items(), key=itemgetter(1), reverse=True) 

print('-='*30)
print(f'  == RANKING DOS JOGADORES ==')
for i,v in enumerate(ranking):
  print(f'  {i+1}º lugar: {v[0]} com {v[1]}.')
  sleep(1)