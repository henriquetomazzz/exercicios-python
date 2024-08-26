def primo(i): #define função
  ePrimo = 0 #cria variavel = 0

  for j in range(1, i + 1): #esse laço vai de 1 até a variavrl global +1      
    if i % j == 0: #se i dividido por j tive resto igual a 0 
      ePrimo += 1 #vai concatenar +1 em  'ePrimo'
      
  if ePrimo  == 2 : # se ePrimo é igual a 2 
    print('primo') #vai imprimir 'primo'
  else: #caso contrario
    print('nao primo') #vai imprimir 'não primo'
        
def entrada(): #define função 
  while True: #enquanto for verdadeiro
    i = int(input()) #vai pedir uma entrada inteira

    if i == 1:#se a entrada for igual a 1 ele vai parar
      break
    else: #caso contrário 
      primo(i)#chama a função com parametro de entrada i

entrada()#inicia o programa chamando a função entrada