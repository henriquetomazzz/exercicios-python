def vetor(): 
  lista = []
  
  num = [float(input()) for _ in range(100)]
  
  for i in range(100):
    if num[i] <= 10:
      print(f"A[{i}] = {num[i]:.1f}")


vetor()