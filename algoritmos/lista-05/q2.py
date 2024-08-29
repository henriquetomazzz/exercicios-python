'''Um n ́umero par  ́e um n ́umero inteiro que pode ser escrito na forma 2n e n  ́e inteiro. Escreva uma função 
que receba um inteiro e retorne se ele  ́e par ou n ̃ao. Em seguida escreva um programa que leia n ́umeros 
inteiros e indique se  ́e par ou n ̃ao, usando a fun ̧c ̃ao. O programa deve ser encerrado quando a entrada for -1.'''
def par(i):
  if i%2 == 0: 
    print("par")
  else: 
    print("impar")

def entrada(): 
  while True: 
    i = int(input())

    if i == -1:
      break
    else:
      par(i)

entrada()