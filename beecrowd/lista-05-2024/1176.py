i = int(input())
valores = [1, 1]

def fib(num): 
  if num == 0:
     return 0
  elif num == 1 or num == 2:
     return 1 
  else: 
    
    for j in range(num-2):
      proxNum = valores[-1] + valores[-2]
      valores.append(proxNum)
    return valores[-1]

for c in range(0, i):
    num = int(input())
    print(f"Fib({num}) = {fib(num)}")
