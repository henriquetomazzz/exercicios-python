'''Você foi contratado pela Federação Paraibana de Futebol e recebeu uma tarefa, desenvolver um programa que receba
como entrada uma sequência de resultados de partida de um determinado time e gere como saída a pontuação do time de
de acordo com os resultados. O resultado pode ser vitória, empate ou derrota. Uma vitória vale 3 pontos, empate 1 e
derrota 0. Segue um exemplo de entrada. 
3 2 
0 0 
1 1 
1 4 
6 2 
1 0 
2 1 
1 0 
A pontuação do time para esta sequência de jogos é 17, Observe que o placar sempre apresenta o número de gols do
time na primeira posição.'''
vitoria = empate = 0

for i in range(0, 17):
  x, y = map(int,input().split())
  if x > y: 
    vitoria += 3
  elif x == y: 
    empate += 1
pontos = vitoria+empate

print(f"O time obteve {pontos} pontos no campeonato")