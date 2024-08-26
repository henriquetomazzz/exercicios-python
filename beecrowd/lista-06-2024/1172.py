def vetor(): 
  for j in range(0, 10):
    num = int(input())
    if num <= 0: 
      print(f"X[{j}] = {1}")
    else:
      print(f"X[{j}] = {num}")

vetor()