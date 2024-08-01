while True: 
  x, y = list(map(int, input().split()))

  if x > y:
    print("Decrescente")
    continue

  elif x < y:
    print("Crescente")
    continue

  elif x == y: 
    break