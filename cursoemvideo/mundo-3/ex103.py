'''faça um programa que tenha uma função chamado ficha(), que receba dois paramêtros opcionais: o nome de um
jogador e quantos gols ele marcou. O prorama deverá ser capaz de mostrar a ficha do jogador, mesmo que algum
dado não tenha sido informado corretamente.'''
def ficha(jogador = '<desconhecido>', gol = 0):
  if jogador == '' and gol == '': 
    print(f"O jogador {jogador} fez {gol} gol(s) no campeonato")
  else: 
    print(f"O jogador {jogador} fez {gol} gol(s) no campeonato")

print("-"*30)
jogador = input("Nome do Jogador: ")
gol = input("Número de gols: ")

ficha(jogador, gol)