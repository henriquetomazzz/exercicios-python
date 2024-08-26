'''
Agora, faça um programa que receba os valores de x, y e z do usuário e
mostre o resultado da expressão da questão anterior.
'''
x = int(input("Digite o primeiro valor: "))
y = int(input("Digite o segundo valor: "))
z = int(input("Digite o terceito valor: "))

if x*y < z/x or x / y < z * x and z * y < x:
   print("w = True")
else: 
  print("w = False")