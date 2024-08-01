n1 = int(input())
n2 = int(input())

numeros = n1, n2
numeros = list(numeros)
numeros.sort()

def impar(numeros):
    impares = []
    for n in range(numeros[0] + 1, numeros[1]):
        if n % 2 != 0:
            impares.append(n)
    print(sum(impares))
impar(numeros)