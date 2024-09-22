'''Escreva um programa em Python que receba um inteiro N e em seguida leia N valores reais. O programa deve imprimir
quantos dos N valores são positivos e a média destes (valores positivos). A média deve ser impressa com 1 casa 
decimal.'''
n = int(input())
positivos = somador = 0

for i in range(0, n+1):
  entrada = float(input())
  if entrada > 0:
    positivos+=1
    somador +=entrada

print(f"{somador/positivos:.1f}")