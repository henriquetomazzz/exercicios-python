'''Escreva uma função que receba um número inteiro, i, e retorne o i-ésimo elemento da série. Por exemplo, se o i 
recebido for 6 o retorno deve ser 8 ou se o i recebido for 8 o retorno deve ser 21. Escreva uma função não recursiva. ''' 

def palindromo(palavra):
  palavra = palavra.upper()
  return palavra == palavra[::-1]

print(palindromo("ana"))
print(palindromo("arara"))
print(palindromo("python"))
print(palindromo("Ana"))