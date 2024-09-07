'''Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares. Se o valor
digitado for impar, desconsidere-o'''
contador = []
for c in range(0, 6): 
  entrada = int(input("Digite um número: "))
  if entrada%2==0: 
    contador.append(entrada)
print(f"A soma de todo os números pares digitador vai ser igual a {sum(contador)}")