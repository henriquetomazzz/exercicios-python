def vetor():
  num = int(input())
  lista = [num]
  
  for j in range(1,10):
    lista.append(lista[-1]*2)
  
  for i in range(10):
    print(f"X[{i}] = {lista[i]}")

vetor()