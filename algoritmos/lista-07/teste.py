lista = [] 
def limites():
  li = int(input())
  ls = int(input())

  for i in range(li, ls+1):
    quadrado = i**2 
    lista.append(quadrado)
  for quadrado in lista:
    print(quadrado, end=' ')
  
  def soma():
    print(sum(lista))
  
  soma()
limites()