'''
*O MAIOR*
Faça um programa que leia três valores e apresente o maior dos três valores lidos seguido
da mensagem “eh o maior”. Utilize a fórmula:

https://resources.beecrowd.com/gallery/images/problems/UOJ_1013.png

Obs.: a fórmula apenas calcula o maior entre os dois primeiros (a e b). Um segundo passo,
portanto é necessário para chegar no resultado esperado.

Entrada
O arquivo de entrada contém três valores inteiros.

Saída
Imprima o maior dos três valores seguido por um espaço e a mensagem "eh o maior".
'''
a, b, c = list(map(int, input().split()))

maiorAb = (a+b+abs(a-b))/2
maiorAc = (a+c+abs(a-c))/2

if maiorAb > maiorAc:
  print(f'{maiorAb:.0f} eh o maior')
else: 
  print(f'{maiorAc:.0f} eh o maior')