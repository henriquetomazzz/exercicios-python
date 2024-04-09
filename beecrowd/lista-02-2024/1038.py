'''
*LANCHE*
Com base na tabela abaixo, escreva um programa que leia o código de um item e a quantidade
deste item. A seguir, calcule e mostre o valor da conta a pagar.

https://resources.beecrowd.com/gallery/images/problems/UOJ_1038_pt.png

Entrada
O arquivo de entrada contém dois valores inteiros correspondentes ao código e à quantidade 
de um item conforme tabela acima.

Saída
O arquivo de saída deve conter a mensagem "Total: R$ " seguido pelo valor a ser pago, 
com 2 casas após o ponto decimal.
'''
cod, qnt = list(map(int, input().split()))

if cod == 1: 
  print(f"Total: R$ {qnt*4:.2f}")
elif cod == 2:
  print(f"Total: R$ {qnt*4.50:.2f}")
elif cod == 3: 
  print(f"Total: R$ {qnt*5:.2f}")
elif cod == 4: 
  print(f"Total: R$ {qnt*2:.2f}")
elif cod == 5: 
  print(f"Total: R$ {qnt*1.50:.2f}")