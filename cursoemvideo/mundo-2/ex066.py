'''Crie um programa que leia números inteiros pelo teclado. O programa só vai parar quando o usuário digitar
o valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre 
eles (desconsiderando o flag).'''
num = 0
contador = 0
somador = 0

while True: 
  num = int(input("Digite um valor (999 para parar): "))
  if num == 999: 
    break
  else: 
    contador += 1
    somador += num
print(f"A soma dos {contador} valores foi {somador}!")
