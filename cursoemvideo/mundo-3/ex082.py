'''Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, crie duas listas extras que 
vão conter apenas os valores pares e os valores ímpares digitados, respectivamente. Ao final, mostre o conteúdo das
três listas geradas.'''
todos = []
impar = []
par = []
while True: 
  numeros = int(input("Digite um número: "))
  todos.append(numeros)

  resp=str(input("Quer continuar? [S/N] ")).strip()[0]
  if resp in 'Nn':
    break

print("-="*30)

print(f"A lista completa é {todos}")

for i in todos:
  if i%2==0: 
    par.append(i)
print(f"A lista de pares é {par}")

for i in todos: 
  if i%2 == 1: 
    impar.append(i)
print(f"A lista de ímpares é {impar}")