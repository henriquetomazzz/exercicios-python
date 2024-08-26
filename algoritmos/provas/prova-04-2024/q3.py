#palindromo 
def palindromo(palavra):
  palavra = palavra.upper()
  return palavra == palavra[::-1]

print(palindromo("ana"))
print(palindromo("arara"))
print(palindromo("python"))
print(palindromo("Ana"))