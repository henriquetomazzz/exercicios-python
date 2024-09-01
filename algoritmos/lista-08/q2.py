'''Escreva um algoritmo que leia um inteiro  n e uma matriz de dimensão escolhida pelo usuário. Em seguida, 
deve calcular e escrever o resultado do produto escalar.'''
def produtoEscalar(n, matriz):
    resultante = []
    for linha in matriz:
        linhaR = []
        for e in linha: 
            linhaR.append(n*e)
        resultante.append(linhaR)

    return resultante

linhas,colunas = map(int,input("Digite as dimensões da matriz: ").split("x"))

matriz = []
for i in range(linhas):
    matriz.append(list(map(int,input("Digite uma das linhas: ").split(" "))))

n = int(input("Escalar: "))

resultado = produtoEscalar(n, matriz)

for linha in resultado:
    print(" ".join(map(str,linha)))