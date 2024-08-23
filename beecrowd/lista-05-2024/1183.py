def entrada():
  lista = []
  letra = input()
  contador = 0

  if letra == 'S':
    for i in range(0, 144):
      o = float(input())
      if o > 0:
        lista.append(o)
        total = sum(lista)
    print(f"{total:.1}")

  if letra == 'M':
    for j in range(0, 144):
      o = float(input())
      contador += 1
      if o > 0:
        lista.append(o)
        total = sum(lista)

    print(f"{total/contador:.1f}")
    
entrada()