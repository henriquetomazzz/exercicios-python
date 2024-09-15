'''Faça um programa que leia um número qualquer e mostre o seu fatorial. Exemplo: 5! = 5 x 4 x 3 x 2 x 1 = 120'''
fatorial = int(input("Digite um número para calcular Fatorial: "))
c = fatorial
f = 1
print(f"Calculando {fatorial}! = ", end='')
while c > 0: 
  print(f"{c}", end='')
  print(" x " if c>1 else " = ", end='')
  f *= c
  c-=1
print(f"{f}")