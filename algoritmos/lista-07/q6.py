'''Escreva um algoritmo que leia 10 numeros e os escreva em ordem decrescente.'''
def decresente(): 
  lista.sort(reverse=True)
  print(f"A lista ficará {" ".join(map(str, lista))}")

lista = []

def entrada():
  for i in range(0,10):
    num = int(input())
    lista.append(num)
  decresente()

entrada()