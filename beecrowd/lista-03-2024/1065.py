'''
*PARES ENTRE 5 NÚMEROS*
Faça um programa que leia 5 valores inteiros. Conte quantos destes valores digitados são 
pares e mostre esta informação.

Entrada
O arquivo de entrada contém 5 valores inteiros quaisquer.

Saída
Imprima a mensagem conforme o exemplo fornecido, indicando a quantidade de valores pares 
lidos.
'''
pares = 0

for i in range(5):
  val = float(input())

  if val%2 == 0:
    pares += 1

print(pares, "valores pares")