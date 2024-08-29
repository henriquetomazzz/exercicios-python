'''Dizemos que um n ́umero natural  ́e triangular se ele  ́e produto de três n ́umeros naturais consecutivos. 
Exemplo: 120  ́e triangular, pois 4 X 5 X 6 = 120. Crie uma função que indica se um n ́umero ́e triangular ou não.
Em seguida escreva um programa que leia n ́umeros inteiros e indique se ́e triangular ou não, usando a função. 
O programa deve ser encerrado quando a entrada for -1.'''
def triangular(a,b,c):
  if a < b and b < c: 
    print(f"{a} X {b} X {c} = {a*b*c}")

def entrada():
  while True: 
    a,b,c = map(int, input().split())

    if a > b and b > c: 
      break
    if a == -1 or b == -1 or c == -1:
      break
    else: 
      triangular(a,b,c)

entrada()