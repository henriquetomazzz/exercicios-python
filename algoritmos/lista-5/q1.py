def limites(li,ls):
  
  for i in range(li, ls+1, 1):
    print(i)

def entrada():
  while True: 
    li = int(input())
    ls = int(input())

    if li == 0 and ls == 0: 
      break
    else: 
      limites(li,ls)

entrada()