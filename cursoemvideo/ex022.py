'''
Crie um programa que leia o nome completo de uma pessoa e mostre:

– O nome com todas as letras maiúsculas e minúsculas.

– Quantas letras ao todo (sem considerar espaços).

– Quantas letras tem o primeiro nome.'''
name = str(input("Digite seu nome completo: ")).strip()

print("Analisando seu nome...")
print(f"Seu nome em maiúsculas é {name.upper()}")
print(f"Seu nome em minúsculas é {name.lower()}")
print(f"Seu nom tem ao todo {len(name)-name.count(' ')} letras")
separa = name.split()
print(f"Seu pimeiro nome é {separa[0]} e ele tem {name.find(' ')} letras")