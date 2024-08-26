'''Faça um programa que tenha uma função chamada maior(), que receba vários parametros com valores inteiros.
seu programa tem que analisar todos os valores e dizer qual deles é o maior.'''
def maior(* num):
  print("-=" * 50)
  print("Analisando os valores passados...")
  print(f"{num} foram informados {len(num)} valores ao  todo" )
  print(f"O maior valor informado foi {max(num)}.")

maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)