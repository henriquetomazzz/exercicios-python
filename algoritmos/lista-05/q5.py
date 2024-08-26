#função não recursiva
'''
def fatorial(i):
  if i != 0:
    resultado=1
    for j in range(1,i+1):
      resultado *= j
      print(resultado)

def entrada():
  i = int(input())
  
  fatorial(i)

entrada()'''
#função recursiva 
def fatorial(i): 
  if i == 1: 
    return 1
  return i * fatorial(i-1)

i = int(input())
print(fatorial(i))
