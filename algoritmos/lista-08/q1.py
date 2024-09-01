'''Escreva um algoritmo que leia 2 matrizes,  calcule e escreva o produto delas. O  algoritmo deve permitir 
matrizes de diversas dimensões e deve validar se é possível calcular.'''
def produtoMatrizes(m1,m2):
    resultante = []
   
    for i in range(len(m1)):
        linhaR = []
        for j in range(len(m2[0])):
            soma = 0
            for k in range(len(m2)):
                soma += m1[i][k]*m2[k][j]
            linhaR.append(soma)
        resultante.append(linhaR)
   
    return resultante
   
linhas1,colunas1 = map(int,input("Digite as dimensões da matriz 1: ").split("x"))

matriz1 = []
for i in range(linhas1):
    matriz1.append(list(map(int,input("Digite uma das linhas da matriz 1: ").split(" "))))

linhas2,colunas2 = map(int,input("Digite as dimensões da matriz 2: ").split("x"))

matriz2 = []
for i in range(linhas2):
    matriz2.append(list(map(int,input("Digite uma das linhas da matriz 2: ").split(" "))))

resultado = produtoMatrizes(matriz1, matriz2)

for linha in resultado:
    print(" ".join(map(str,linha)))