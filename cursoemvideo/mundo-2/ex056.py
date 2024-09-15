'''Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre: 
-A média de idade do grupo
-Qual o nome do homem mais velho
-Quantas mulheres têm menos de 20 anos'''
somaIdade = 0
mediaIdade = 0
maioridadeHomem = 0
nomeVelho = ''
totalMulher20 = 0

for i in range(1, 5):
  print(f"-----------{i}ª PESSOA -----------")
  nome = str(input("Nome ")).strip()
  idade = int(input("Idade "))
  sexo = str(input("Sexo [M/F]: "))
  somaIdade += idade
  if i == 1 and sexo in 'Mm':
    maioridadeHomem = idade
    nomeVelho = nome
  if sexo in 'Mm' and idade > maioridadeHomem:
    maioridadeHomem = idade 
    nomeVelho = nome
  if sexo in 'Ff' and idade < 20:
    totalMulher20 += 1

mediaIdade = somaIdade/4
print(f"A média de idade do grupo de {mediaIdade} anos")
print(f"O homem mais velho tem {maioridadeHomem} anos e se chama {nomeVelho}")
print(f"Ao todo são {totalMulher20} mulheres com menos de 20 anos")