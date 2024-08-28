'''Escreva um algoritmo que leia dois números, limite inferior e limite superior, imprima o quadrado, x^2 
de todos os números de limite inferior a limite superior e, em seguida,imprima a soma dos números impressos.
Por exemplo, se o usuário digitar 2 como limite inferior e 5 como limite superior, deve imprimir 4, 9, 16 e 
25 e a soma 54. Armazene os valores que serão impressos em uma lista e, para realizar a soma, crie uma funcão.'''

def limites(limiteInf, limiteSup): 
  print(f"Os elementos do limite superior serão {limiteSup}")
  print(f"Os elementos do limite inferior serão {limiteInf}")
  print(f"A soma dos elementos do limite superior com limite inferior será igual a {sum(limiteSup)+sum(limiteInf)}")

limiteSup = []
limiteInf = []

while True:
  li, ls = map(int, input().split())
  if li == 0 and ls == 0:
    break
  limiteSup.append(ls**2)
  limiteInf.append(li**2)
  limites(limiteInf, limiteSup)