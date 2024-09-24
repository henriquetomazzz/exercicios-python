'''Crie um prgrama onde o usuário possa digitar vários valores numéricos e cadastr-os em uma lista.  Caso o múmero 
já exista lá dentro, ele não será adicionado. No final, serão exibidos todos os calores únicos digitados, em ordem
crescente.'''
numeros = []
while True: 
  n = int(input("Digite um valor: "))
  if n not in numeros: 
    numeros.append(n)
    print("Valor adicionado com sucesso...")
  else: 
    print("Valor duplicado! Não vou adicionar...")
  r = str(input("Quer continuar? [S/N] ")).strip()[0]
  if r in 'Nn':
    break
print("-="*30)
print(f"Você digitou os valores {sorted(numeros)}")
