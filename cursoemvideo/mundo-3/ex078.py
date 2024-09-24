'''Faça um programa que leia 5 valores númericos e guarde-os em uma lista.No final, mostre qual foi o meior e o menor
valor digitdo e as suas respectivas posições na lista.'''
lista = []
for i in range(0,5):
  lista.append(int(input(f"Digite um valor para Posição {i}: ")))
print("-="*30)
print(f"Você digitou os valores {lista}")
print(f"O maior valor digitado foi {max(lista)} nas posições", end=' ')
for c, j in enumerate(lista):
  if j == max(lista):
    print(f"{c}...", end=' ')
print()

print(f"O menor valor digitado foi {min(lista)} nas posições", end=' ')
for c, j in enumerate(lista):
  if j == min(lista):
    print(f"{c}...", end=' ')
print()