def fatorial(i):
  if i != 0:
    resultado=1
    for j in range(1,i+1):
      resultado *= j
      print(resultado)

def entrada():
  i = int(input())
  
  fatorial(i)

entrada()