'''Escreva um algoritmo que imprima a lista dos 100 primeiros números primos, iniciando do 2. Número primo  ́e
um n ́umero natural que tem apenas dois divisores diferentes, o 1 e ele mesmo. Por definição, 1 não  ́e primo. 
Crie e utilize uma função que indica se um número é primo ou não e mantenha os números primos em uma lista. 
Imprima, ao final, a soma dos 100 números primos impresso. Para isso, crie uma função chamada soma que receba
a lista como parâmetro e retorne a soma.'''
def primo(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6

    return True

def soma(lista):
    return sum(lista)

def encontrarPrimos(quantidade):
    primos = []
    num = 2
    
    while len(primos) < quantidade:
        if primo(num):
            primos.append(num)
        num += 1

    return primos

primos = encontrarPrimos(100)

print("Lista dos 100 primeiros números primos:")
print(primos)

somaPrimos = soma(primos)
print("Soma dos 100 primeiros números primos:", somaPrimos)