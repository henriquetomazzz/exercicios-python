'''
*FÓRMULA DEE BHASKARA*
Leia 3 valores de ponto flutuante e efetue o cálculo das raízes da equação de Bhaskara.
Se não for possível calcular as raízes, mostre a mensagem correspondente “Impossivel 
calcular”, caso haja uma divisão por 0 ou raiz de numero negativo.

Entrada
Leia três valores de ponto flutuante (double) A, B e C.

Saída
Se não houver possibilidade de calcular as raízes, apresente a mensagem "Impossivel 
calcular". Caso contrário, imprima o resultado das raízes com 5 dígitos após o ponto, 
com uma mensagem correspondente conforme exemplo abaixo. Imprima sempre o final de linha 
após cada mensagem.
'''
val1, val2, val3 = list(map(float, input().split()))

delta = val2 **2 - 4*val1*val3

if val1 <= 0 or delta <= 0:
  print("Impossivel calcular")

else:
   raiz = delta ** 0.5
   x1 = (-val2 + raiz) / (2*val1)
   x2 = (-val2 - raiz) / (2*val1)
   print(f"R1 = {x1:.5f}")
   print(f"R2 = {x2:.5f}")