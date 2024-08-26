def vetor():
  num = [int(input()) for _ in range(20)]

  for i in range(10):
    num[i], num[19 - i] = num[19 - i], num[i]
    
  for i in range(20):
    print(f"num[{i}] = {num[i]}")

vetor()