'''
*CÉDULAS*
Leia um valor inteiro. A seguir, calcule o menor número de notas possíveis (cédulas) no 
qual o valor pode ser decomposto. As notas consideradas são de 100, 50, 20, 10, 5, 2 e 1.
A seguir mostre o valor lido e a relação de notas necessárias.

Entrada
O arquivo de entrada contém um valor inteiro N (0 < N < 1000000).

Saída
Imprima o valor lido e, em seguida, a quantidade mínima de notas de cada tipo necessárias,
conforme o exemplo fornecido. Não esqueça de imprimir o fim de linha após cada linha, 
caso contrário seu programa apresentará a mensagem: “Presentation Error”.
'''
notas = int(input())

print(notas)

notas100 = notas//100
notas = notas%100

notas50 = notas//50
notas = notas%50

notas20 = notas//20
notas = notas%20

notas10 = notas//10
notas = notas%10

notas5 = notas//5
notas = notas%5

notas2 = notas//2
notas = notas%2

notas1 = notas//1
notas = notas%1

print(f"{notas100} nota(s) de R$ 100,00")
print(f"{notas50} nota(s) de R$ 50,00")
print(f"{notas20} nota(s) de R$ 20,00")
print(f"{notas10} nota(s) de R$ 10,00")
print(f"{notas5} nota(s) de R$ 5,00")
print(f"{notas2} nota(s) de R$ 2,00")
print(f"{notas1} nota(s) de R$ 1,00")