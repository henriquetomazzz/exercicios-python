'''Um número primo é um número natural maior que 1 que não pode ser formado pela multiplicação de outros 2 naturais 
menores que ele e maiores que 1. Escreva um programa em Python que receba um inteiro X e, em seguida, imprima os 20 
números primos subsequentes ao valor de X. O valor de X, se for primo, deve ser impresso.'''
# Recebe o valor de X do usuário
x = int(input("Digite um número inteiro: "))

primosEncontrados = 0

while primosEncontrados < 20:
    
    primo = True
    if x < 2:
        primo = False
    else:
        for i in range(2, int(x ** 0.5) + 1):
            if x % i == 0:
                primo = False
                break
    
    if primo:
        print(x)
        primosEncontrados += 1
    
    x += 1
