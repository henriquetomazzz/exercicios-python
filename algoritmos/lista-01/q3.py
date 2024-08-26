'''
Faça um Programa que peça 2 números inteiros e um número real. Calcule e
mostre:
o produto do dobro do primeiro com metade do segundo.
a soma do triplo do primeiro com o terceiro.
o terceiro elevado ao cubo.
'''
num1 = int(input("Digite um valor inteiro: "))
num2 = int(input("Digite outro valor inteiro: "))
num3 = float(input("Digite qualquer valor: "))

dobro = (2*num1) + (num2/2)
triplo = (3*num1) + num3
cubo = num3**3

print(f"O produto do dobro do primeiro número com a metade do segundo número é {dobro:.1f}")
print(f"A soma do triplo do primeiro número com o terceiro número é {triplo:.1f}")
print(f"O terceiro número elevado ao cubo {cubo}")