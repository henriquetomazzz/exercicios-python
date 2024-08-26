#soma
def soma(n): 
  s = str(n)
  if len(s) == 1: 
    return n
  
  return int(s[-1]) + soma(int(s[:-1]))

print(soma(123))
print(soma(451))
print(soma(896))