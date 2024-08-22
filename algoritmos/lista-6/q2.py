def par(i):
  if i%2 == 0: 
    print("par")
  else: 
    print("impar")

def entrada(): 
  while True: 
    i = int(input())

    if i == -1:
      break
    else:
      par(i)

entrada()