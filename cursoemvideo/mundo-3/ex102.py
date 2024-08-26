'''crie um porgrama que tenha uma função fatorial() que receba dois parametros: o primeiro que indique um 
número a calcular e o outro chamado show, que será o valor lógico(opcional) indicando se será mostrado ou 
não na tela o processo de cálculo do fatorial'''
def fatorial(num, show=False):
  lista = []
  if show == False: 
    if num == 1: 
      return 1
    return num * fatorial(num-1)
  
  elif show == True: 
    if num == 1: 
      return 1
    print(fatorial(num-1) + "X" + fatorial(num-2) "="* num)

print(fatorial(5, show=True))