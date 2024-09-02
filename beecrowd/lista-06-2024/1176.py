'''Faça um programa que leia um valor e apresente o número de Fibonacci correspondente a este valor lido. 
Lembre que os 2 primeiros elementos da série de Fibonacci são 0 e 1 e cada próximo termo é a soma dos 2 
anteriores a ele. Todos os valores de Fibonacci calculados neste problema devem caber em um inteiro de 64 bits
sem sinal.

Entrada
A primeira linha da entrada contém um inteiro T, indicando o número de casos de teste. Cada caso de teste 
contém um único inteiro N (0 ≤ N ≤ 60), correspondente ao N-esimo termo da série de Fibonacci.

Saída
Para cada caso de teste da entrada, imprima a mensagem "Fib(N) = X", onde X é o N-ésimo termo da série de 
Fibonacci.'''
i = int(input())
valores = [1, 1]

def fib(num): 
  if num == 0:
     return 0
  elif num == 1 or num == 2:
     return 1 
  else: 
    
    for j in range(num-2):
      proxNum = valores[-1] + valores[-2]
      valores.append(proxNum)
    return valores[-1]

for c in range(0, i):
    num = int(input())
    print(f"Fib({num}) = {fib(num)}")
