'''N ́umero primo  ́e um n ́umero natural que tem apenas dois divisores diferentes, o 1 e ele mesmo. Por definição,
1 n ̃ao  ́e primo. Crie uma função que indica se um número é primo ou não. Em seguida escreva um programa que 
leia n ́umeros inteiros e indique se  ́e primo ou não, usando a funçao. O programa deve ser encerrado quando a 
entrada for -1.'''
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