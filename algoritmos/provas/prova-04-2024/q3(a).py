'''Escreva uma função que receba um número inteiro, i, e retorne o i-ésimo elemento da série. Por exemplo, se o i 
recebido for 6 o retorno deve ser 8 ou se o i recebido for 8 o retorno deve ser 21. Escreva uma função não recursiva. ''' 
def fib(i): 
  if i == 1 or i == 2:
    return 1
  
  anterior = 1
  corrente = 1

  for j in range(i-2):
    proximo = anterior+corrente
    anterior = corrente 
    corrente = proximo 

  return corrente 

i = int(input())
print(fib(i))

def palindromo(palavra):
  palavra = palavra.upper()
  return palavra == palavra[::-1]

print(palindromo("ana"))
print(palindromo("arara"))
print(palindromo("python"))
print(palindromo("Ana"))