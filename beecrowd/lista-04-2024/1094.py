'''
Maria acabou de iniciar seu curso de graduação na faculdade de medicina
e precisa de sua ajuda para organizar os experimentos de um laboratório
o qual ela é responsável. Ela quer saber no final do ano, quantas cobaias
foram utilizadas no laboratório e o percentual de cada tipo de cobaia utilizada.

Este laboratório em especial utiliza três tipos de cobaias: sapos, ratos e
coelhos. Para obter estas informações, ela sabe exatamente o número de
experimentos que foram realizados, o tipo de cobaia utilizada e a quantidade 
de cobaias utilizadas em cada experimento.

Entrada
A primeira linha de entrada contém um valor inteiro N que indica os vários casos
de teste que vem a seguir. Cada caso de teste contém um inteiro Quantia (1 ≤ Quantia ≤ 15)
que representa a quantidade de cobaias utilizadas e um caractere Tipo ('C', 'R' ou 'S'),
 indicando o tipo de cobaia (R:Rato S:Sapo C:Coelho).

Saída
Apresente o total de cobaias utilizadas, o total de cada tipo de cobaia utilizada
e o percentual de cada uma em relação ao total de cobaias utilizadas, sendo que o 
percentual deve ser apresentado com dois dígitos após o ponto.
'''
n = int(input())
coelho = 0
rato = 0
sapo = 0

for i in range(0, n):
  num, name = input().split()
  num = int(num)

  if name == "C":
    coelho += num
  if name == "R":
    rato += num
  if name == "S":
    sapo += num

total = coelho + rato + sapo

print(f"Total: {total} cobaias") 
print(f"Total de coelhos: {coelho}")
print(f"Total de ratos: {rato}")
print(f"Total de sapos: {sapo}")
print(f"Percentual de coelhos: {(total-coelho)/3} %")
print(f"Percentual de ratos: {(total-rato)/3} %")
print(f"Percentual de sapos: {(total-sapo)/3} %")

'''Total: 92 cobaias
Total de coelhos: 29
Total de ratos: 40
Total de sapos: 23
Percentual de coelhos: 31.52 %
Percentual de ratos: 43.48 %
Percentual de sapos: 25.00 %'''