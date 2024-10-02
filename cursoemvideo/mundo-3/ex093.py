'''Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o nome do jogador e 
quantas partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada partida. No final, tudo isso será 
guardado em um dicionário, incluindo o total de gols feitos durando o campeonato'''
dados = dict()
dados['nome'] = str(input('Nome do jogador: '))
partidas = int(input(f'Quantas partidas {dados['nome']} jogou? '))

for i in range(0, partidas+1): 
  dados[f'partida {i}'] = int(input(f'Quantos gols na partida {i}'))

print('-='*30)
print(dados)