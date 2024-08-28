'''Escreva um algoritmo que leia 10 nomes e os escreva em ordem alfabética.'''
def ordem():
  lista.sort()
  print(f"A lista de nomes ordenados ficara {", ".join(map(str, lista))}")

lista = []

def entrada():
  for i in range(0, 2):
    nome = input("Escreva o nome: ")
    lista.append(nome)
  ordem()

entrada()