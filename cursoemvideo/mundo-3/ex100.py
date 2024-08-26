'''Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteio() e somaPar(). 
A primeira função vai sortear 5 números e vai colocá-los dentro da lista e a segunda função vai mostrar a
soma entre todos os valores pares sorteados pela função anterior'''
numeros = []

def sorteio():
  for i in range(0, 5):
    x = 1, 2, 3, 4, 5, 6, 7, 8, 9, 10
    sort = sorted(x)
    numeros.append(sort)

  print(f"Sorteando 5 valores da lista: {numeros} PRONTO!")

def somaPar():
  for j in range(0, 5):
    par = 0
    if numeros[j]:
      par += numeros[j]
  print(f"Somando os valores pares de {numeros}, temos {par}")

sorteio()
somaPar()
  