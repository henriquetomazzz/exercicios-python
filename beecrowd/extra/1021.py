'''
*NOTAS E MOEDAS*
Leia um valor de ponto flutuante com duas casas decimais. Este valor representa um valor
monetário. A seguir, calcule o menor número de notas e moedas possíveis no qual o valor 
pode ser decomposto. As notas consideradas são de 100, 50, 20, 10, 5, 2. As moedas 
possíveis são de 1, 0.50, 0.25, 0.10, 0.05 e 0.01. A seguir mostre a relação de notas 
necessárias.

Entrada
O arquivo de entrada contém um valor de ponto flutuante N (0 ≤ N ≤ 1000000.00).

Saída
Imprima a quantidade mínima de notas e moedas necessárias para trocar o valor inicial, 
conforme exemplo fornecido.

Obs: Utilize ponto (.) para separar a parte decimal.
'''
valor = float(input())

notas100 = valor//100
valor = valor%100

notas50 = valor//50
valor = valor%50

notas20 = valor//20
valor = valor%20

notas10 = valor//10
valor = valor%10

notas5 = valor//5
valor = valor%5

notas2 = valor//2
valor = valor%2

moeda1 = valor//1
valor = valor%1

moeda50 = valor//0.50
valor = valor%0.50

moeda25 = valor//0.25
valor = valor%0.25

moeda10 = valor//0.10
valor = valor%0.10

moeda5 = valor//0.05
valor = valor%0.05

moeda01 = valor//0.01
valor = valor%0.01

print("NOTAS: ")
print(f"{notas100:.0f} nota(s) de R$ 100.00")
print(f"{notas50:.0f} nota(s) de R$ 50.00")
print(f"{notas20:.0f} nota(s) de R$ 20.00")
print(f"{notas10:.0f} nota(s) de R$ 10.00")
print(f"{notas5:.0f} nota(s) de R$ 5.00")
print(f"{notas2:.0f} nota(s) de R$ 2.00")
print("MOEDAS: ")
print(f"{moeda1:.0f} moeda(s) de R$ 1.00")
print(f"{moeda50:.0f} moeda(s) de R$ 0.50")
print(f"{moeda25:.0f} moeda(s) de R$ 0.25")
print(f"{moeda10:.0f} moeda(s) de R$ 0.10")
print(f"{moeda5:.0f} moeda(s) de R$ 0.05")
print(f"{moeda01:.0f} moeda(s) de R$ 0.01")
