'''crie um programa que leia dois valores e mostre um menu na tela: 
[ 1 ] somar
[ 2 ] multiplicar
[ 3 ] maior
[ 4 ] novos números
[ 5 ] sair do programa
seu programa deverá realizar a operação solicitada em cada caso'''
primeiro = int(input("Primeiro valor: "))
segundo = int(input("Segundo valor: "))

while True:
  print("\t[ 1 ] somar")
  print("\t[ 2 ] multiplicar")
  print("\t[ 3 ] maior")
  print("\t[ 4 ] novos números")
  print("\t[ 5 ] sair do programa")
  opcao = int(input(">>>>>> Qual é a sua opção? "))

  if opcao == 1:
    print(f"A soma entre {primeiro} + {segundo} é {primeiro+segundo}")
    print("=-"*30)
    continue
  elif opcao == 2:
    print(f"A multiplicação entre {primeiro} X {segundo} é {primeiro*segundo}")
    print("=-"*30)
    continue
  elif opcao == 3:
    if primeiro > segundo:
      print(f"O maior número é o {primeiro}")
      print("=-"*30)
      continue
    elif segundo > primeiro:
      print(f"O maior número é o {segundo}")
      print("=-"*30)
      continue
    elif segundo == primeiro:
      print(f"Ambos números são iguais")
      print("=-"*30)
      continue
  elif opcao == 4:
    print("Informe os números novamente: ")
    primeiro = int(input("Primeiro valor: "))
    segundo = int(input("Segundo valor: "))
    continue
  elif opcao == 5:
    break