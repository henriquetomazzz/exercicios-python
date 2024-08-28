'''Escreva um algoritmo que leia 30 numeros inteiros e os armazene em uma lista. Escreva as
funcões maior, menor e soma. Elas devem receber a lista e retornar o respectivo valor. Por
fim, faça chamadas das funçoes e imprima os retornos.'''
def maior(lista):
  maiorLista = max(lista)
  return maiorLista
def menor(lista):
  menorLista = min(lista)
  return menorLista
def soma(lista):
  somaLista = sum(lista)
  return somaLista

contador = 0
lista = []

while contador <= 29:
  entrada = int(input())
  alocando = lista.append(entrada)
  contador += 1

print(f"O maior da lista é {maior(lista)}")
print(f"O menor da lista é {menor(lista)}")
print(f"A soma de todos os elementos da lista é {soma(lista)}")