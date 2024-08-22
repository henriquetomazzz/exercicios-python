def primo(i):
  ePrimo = 0

  for j in range(1, i + 1):        
    if i % j == 0:
      ePrimo += 1
      
  if ePrimo  == 2 :
    print('primo')
  else:
    print('nao primo')
        
def entrada():
  while True: 
    i = int(input())

    if i == 1:
      break
    else: 
      primo(i)

entrada()