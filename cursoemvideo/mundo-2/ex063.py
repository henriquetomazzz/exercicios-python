'''Escreva um programa que leia um número N inteiro qualquer e mostre na tela os N primeiros elementos de uma 
sequêncida de Fibonacci'''
print("-"*30)
print("Sequência de Fibonacci")
print("-"*30)

termos = int(input("Quantos termos você quer mostrar? "))
t1 = 0
t2 = 1

print("~~"*30)
print(f"{t1} -> {t2}", end='')
contador = 3

while contador <= termos: 
  t3 = t1 + t2
  print(f"-> {t3}", end='')
  t1 = t2
  t2 = t3
  contador += 1
print("-> FIM")