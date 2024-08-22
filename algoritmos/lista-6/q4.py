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