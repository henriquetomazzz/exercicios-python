'''
*MAIOR POSIÇÃO*
Leia 100 valores inteiros. Apresente então o maior valor lido e a posição dentre os 100 
valores lidos.

Entrada
O arquivo de entrada contém 100 números inteiros, positivos e distintos.

Saída
Apresente o maior valor lido e a posição de entrada, conforme exemplo abaixo.
'''
valor = 0
posicao = 0

for valores in range(1, 101):
  num = int(input())
  if num > valor:
    valor = num
    posicao = valores

print(valor)
print(posicao)