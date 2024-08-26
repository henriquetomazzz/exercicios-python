#parenteses
def verifica(exp): 
  cont = 0
  for c in range (exp):
    if c == '(':
       cont += 1
    elif c == ')':
      cont -= 1
    if cont < 0: 
      return False
  
  return cont == 0

exp = input()
print(verifica(exp))