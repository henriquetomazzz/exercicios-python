'''Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma lista única que mantenha
os valores pares e ímapares. No final, mostre os valores pares e ímpares em ordem crescente.'''
valores = [[],[]]

for i in range(0, 7): 
  numeros = int(input(f"Digite o {i}º valor: "))

  if numeros%2 == 0: 
    valores[0].append(numeros)
  elif numeros%2 == 1: 
    valores[1].append(numeros)

print('-='*30)
print(f"Os valore pares digitados foram: {valores[0].sort()}")
print(f"Os valore ímpares digitados foram: {valores[1].sort()}")