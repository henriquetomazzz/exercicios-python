'''Desenvolva uma v2 para o programa das filas. Desta vez ele deve manter 2 filas, uma para atendimentos 
regulares e outra para prioridades. No atendimento começar pela prioridade,  se houver, e em seguida ir 
alternando, ou seja,  um prioridade, um regular, outro prioridade e outro regular, até o final das filas.'''
from itertools import zip_longest

def ordem():
   mesclada = [elem for pair in zip_longest(listaP, listaR) for elem in pair if elem is not None]
   print(f"A ordem dos pacientes será {", ".join(map(str, mesclada))}")

def entrada():
  while True: 
    print("="*30)
    print("Você deseja:")
    print("1-Adicionar paciente")
    print("2-Remover paciente")
    print("3-Mostrar fila de espera")
    print("4-Encerrar programa")
    i = int(input("Digite: "))
    print("="*30)

    if i == 1:
      adicionar()
      continue
    elif i == 2:
      remover()
      continue
    elif i == 3: 
      ordem()
      continue
    else:
      break

def adicionar():
  print("Seu paciente é: ")
  print("1-Prioridade")
  print("2-Regular")
  pac = int(input("Digite: "))
  print("="*30)

  if pac == 1: 
    nome = input("Digite aqui o nome do paciente: ")
    listaP.append(nome)

  elif pac == 2: 
    nome = input("Digite aqui o nome do paciente: ")
    listaR.append(nome)

def remover():
  print("Você deseja: ")
  print("1-Remover paciente da fila prioritária")
  print("2-Remover paciente da fila regualar")
  re = int(input("Digite: "))

  if re == 1: 
    nome = input("Digite o nome do paciente que deseja remover da fila prioritária: ")
    listaP.remove(nome)

  elif re == 2: 
    name = input("Digite o nome do paciente que deseja remover da fila regular: ")
    listaR.remove(name)

listaR = []
listaP = []
entrada()