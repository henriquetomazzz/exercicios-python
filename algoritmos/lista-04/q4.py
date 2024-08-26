'''
4. Faça um Programa que leia um número e exiba o mês correspondente
do ano. (1-Janeiro, 2- Fevereiro, etc.), se digitar outro valor deve aparecer valor
inválido.
'''
mes = int(input("Digite um valor de 1 a 12: "))

if mes == 1:
  print("1-janeiro")
  
elif mes == 2:
  print("2-fevereiro")

elif mes == 3:
  print("3-março")

elif mes == 4:
  print("4-abril")

elif mes == 5:
  print("5-maio")

elif mes == 6:
  print("6-junho")

elif mes == 7:
  print("7-julho")

elif mes == 8:
  print("8-agosto")

elif mes == 9:
  print("9-setembro")

elif mes == 10:
  print("10-outubro")

elif mes == 11:
  print("11-novembro")

elif mes == 12:
  print("12-dezembro")

else: 
  print("Valor inválido")