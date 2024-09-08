'''Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos'''
lista = []
for c in range(0, 5): 
  peso = float(input("Digite seu peso: "))
  lista.append(peso)

print(f"O maior peso apresentado foi de {max(lista)} kg")
print(f"O menor peso apresentado foi de {min(lista)} kg")