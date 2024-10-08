'''Leia um caractere maiúsculo, que indica uma operação que deve ser realizada e uma matriz M[12][12]. 
Em seguida, calcule e mostre a soma ou a média considerando somente aqueles elementos que estão acima da 
diagonal principal da matriz, conforme ilustrado abaixo (área verde).

Entrada
A primeira linha de entrada contem um único caractere Maiúsculo O ('S' ou 'M'), indicando a operação (Soma ou 
Média) que deverá ser realizada com os elementos da matriz. Seguem os 144 valores de ponto flutuante que 
compõem a matriz.

Saída
Imprima o resultado solicitado (a soma ou média), com 1 casa após o ponto decimal.
'''
def entrada():
  lista = []
  letra = input()
  contador = 0

  if letra == 'S':
    for i in range(0, 144):
      o = float(input())
      if o > 0:
        lista.append(o)
        total = sum(lista)
    print(f"{total:.1}")

  if letra == 'M':
    for j in range(0, 144):
      o = float(input())
      contador += 1
      if o > 0:
        lista.append(o)
        total = sum(lista)

    print(f"{total/contador:.1f}")
    
entrada()