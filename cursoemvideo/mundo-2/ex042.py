'''Refaça o desafio 035 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado: 
-EQUILÁTERO: todos os lados iguais 
-ISÓCELES: dois lado iguais, um diferente
-ESCALENO: todos os lados diferente'''
r1 = int(input("Primeiro segmento: "))
r2 = int(input("Segundo segmento: "))
r3 = int(input("Terceiro segmento: "))

if r1 == r2 and r2 == r3:
  print("Os segmento acima PODEM FORMAR um triângulo EQUILÁTERO")

elif r1 == r2 or r2 == r3: 
  print("Os segmento acima PODEM FORMAR um triângulo ISÓCELES")

elif r1 != r2 or r2 != r3:
  print("Os segmento acima PODEM FORMAR um triângulo ESCALENO")