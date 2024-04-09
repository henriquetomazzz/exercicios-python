'''
*SORT SIMPLES*

Leia 3 valores inteiros e ordene-os em ordem crescente. No final, mostre os valores em 
ordem crescente, uma linha em branco e em seguida, os valores na sequência como foram 
lidos.

Entrada
A entrada contem três números inteiros.

Saída
Imprima a saída conforme foi especificado.
'''
val1, val2, val3 = list(map(int, input().split()))

valores = sorted([val1, val2, val3])

print(valores[0])
print(valores[1])
print(valores[2])

print()

print(val1)
print(val2)
print(val3)
