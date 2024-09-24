'''Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, mostre: 
a) Quantos número foram digitados
b) A lista de valores ordenada de forma descrescente.
c) Se o valor 5 foi digitado e está ou não na lista'''
lista = []
while True: 
  numero = int(input("Digite um valor: "))
  lista.append(numero)

  resp = str(input("Quer continuar? [S/N] ")).strip()[0]

  if resp in 'Nn':
    break
print("-="*30)
print(f"Você digitou {len(lista)} elementos")
lista.sort()
print(f"Os valores em ordem decrescente são {lista[::-1]}")
if 5 in lista:
  print("O valor 5 faz parte da lista!")
else:
  print("O valor 5 não foi encontrado na lista!")