'''Faça um programa que mostre na tela uma contagem regressiva para i estouro de fogos de artificio, indo de 10 até
0, com pausa de 1 segundo entre eles'''
import time
for c in range (10, -1, -1):
  print(c)
  time.sleep(1)