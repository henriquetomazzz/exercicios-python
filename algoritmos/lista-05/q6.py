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

#função sincrona
'''
def fib(i): 
  if i == 1 or i == 2:
    return 1
  
  return fib(i-1) + fib(i-2)

i = int(input())
print(fib(i))'''