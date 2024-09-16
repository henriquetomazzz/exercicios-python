'''Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário.
O programa será interrompido quando o número solicitado for negativo'''
num = 0

while True: 
  num = int(input("Quer ver a tabuada de qual valor? "))

  if num < 0: 
    break
  else: 
    print("--"*30)
    for i in range(1, 11):
      print(f"{num} x {i} = {i*num}")
    print("--"*30)
print("PROGRAMA TABUADA ENCERRADO. Volte sempre!")