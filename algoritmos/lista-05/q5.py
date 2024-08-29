'''A função fatorial  ́e defina da seguinte forma: n! = n x (n - 1)!. Escreva uma função que receba um número 
inteiro e retorne o seu fatorial. Em seguida escreva um programa que leia um inteiro e, usando a função, 
calcule e escreva o seu fatorial.'''
#função não recursiva
def fatorial(i):
  if i != 0:
    resultado=1
    for j in range(1,i+1):
      resultado *= j
      print(resultado)

def entrada():
  i = int(input())
  
  fatorial(i)

entrada()
#função recursiva 
'''
def fatorial(i): 
  if i == 1: 
    return 1
  return i * fatorial(i-1)

i = int(input())
print(fatorial(i))
'''