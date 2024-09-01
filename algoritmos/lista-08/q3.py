''''Escreva um algoritmo que leia uma matriz 2 x 2. Em seguida, deve calcular e imprimir o determinante.'''
def determinante(a, b, c, d):
    return a * d - b * c

# Função principal
def entrada():
    print("Digite os valores para a matriz 2x2:")
    
    a = float(input("Elemento a (posição [0][0]): "))
    b = float(input("Elemento b (posição [0][1]): "))
    c = float(input("Elemento c (posição [1][0]): "))
    d = float(input("Elemento d (posição [1][1]): "))

    resultado = determinante(a, b, c, d)

    print(f"O determinante da matriz é: {resultado}")

entrada()