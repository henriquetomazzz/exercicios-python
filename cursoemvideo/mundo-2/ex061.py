'''Refaça o DESAFIO 051, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos de progressão
usando a estrutura while.'''
print("Gerador de PA")
print("-="*15)

primeiro = int(input("Primeiro termo: "))
razao = int(input("Razão da PA: "))
termo = primeiro
contador = 1

while contador <= 10:
  print(f"{termo}"+"-> ", end='')
  termo += razao
  contador += 1
print('FIM')