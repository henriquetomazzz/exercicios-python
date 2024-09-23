'''Crie um programa que tenha uma tupla totalmente preenchida com uma contagem por extenso, de zero até vinte. Seu 
programa deverá ler um número pelo teckadi(entre 0 e 20) e mostrá-lo por extenso.'''
numeros = ("zero", "um", "dois", "três", "quatro", "cinco", "seis", "sete", "oito", "nove", "dez", "onze", "doze", "treze", "catorze", "quize", "dezesseis", "dezessete", "dezoito", "dezenove", "vinte")
while True: 
  entrada=int(input("Digiet um número entre 0 e 20: "))
  if 0 <= entrada <= 20: 
    print(f"Você digitou {numeros[entrada]}")
    break
  print("Tente novamente. ", end='')