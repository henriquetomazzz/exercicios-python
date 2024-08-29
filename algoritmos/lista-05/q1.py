'''Escreva uma algoritmo que repetitivamente leia dois n ́umeros, limite inferior e limite superior, e em 
seguida fa ̧ca uma chamada a uma fun ̧c ̃ao que receba estes limites e imprima o intervalo delimitado pelos 
limites. O algoritmo deve ser interrompido quando as entradas forem 0 (zero).'''
def limites(li,ls):
  
  for i in range(li, ls+1, 1):
    print(i)

def entrada():
  while True: 
    li = int(input())
    ls = int(input())

    if li == 0 and ls == 0: 
      break
    else: 
      limites(li,ls)

entrada()