'''
Faça um programa que calcule a tabuada. Receba um valor do usuário e
imprima a tabuada deste número.
'''
val = float(input("Digite o valor desejado: "))

for i in range(0, 10, 1):
  print(i, "X", val,  "=", val*i) 