'''Escreva um algoritmo que leia 10 nomes e os escreva em ordem alfabética.'''
def ordem():
  lista.sort()
  print(f"A lista de nomes ordenados ficara {lista}")

lista = []

def entrada():
  for i in range(0, 10):
    nome = input("Escreva o nome: ")
    lista.append(nome)
  ordem()

entrada()