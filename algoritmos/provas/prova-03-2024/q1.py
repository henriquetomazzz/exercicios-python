'''Escreva um programa em Python que receba os inteiros X e Y. Em seguida, imprima o quadrado de todos os números 
ímpares no intervalo fechado de X a Y. '''
x = int(input())
y = int(input())

for i in range(x, y+1):
  print(i**2, end=" ")