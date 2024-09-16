'''Crie um programa que leia vário números inteiros pelo teclado. No final da execução, mostre todos os valores e 
qual foi o maior e o menor valores lidos. O programa deve perguntar ao usuário se ele quer ou não continuar 
a digitar valores.'''
resp = 'S'
soma = contador = media = maior = menor = 0

while resp in 'S':
  num = int(input("Digite um número: "))
  soma += num
  contador += 1
  if contador == 1:
    maior = menor = num
  else:
    if num > maior:
      maior = num
    if num < menor: 
      menor = num 

  resp = str(input("Quer continuar? [S/N] ")).strip().upper()[0]
media = soma/contador
print(f"Você digitou {contador} números e a média foi {media}")
print(f"O maior valor foi {maior} e o menor {menor}")
