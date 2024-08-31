'''Cremilda Chantilly é uma dentista e precisa  de ajuda para o gerenciamento de filas de atendimento. 
Desenvolva um programa que permita adicionar pacientes na fila e indique a vez do paciente a ser atendido. 
Minimamente, disponibilize as funcionalidades de adicionar paciente e remover paciente.'''
def paciente():

  fila = []

  while True: 
    print("="*30)
    print("Você deseja:")
    print("1-Adicionar paciente")
    print("2-Remover paciente")
    print("3-Encerrar programa")
    i = int(input("Digite: "))
    print("="*30)

    if i == 1: 
      entrar = input("Digite o paciente que vai entrar na fila: ")
      fila.append(entrar)
      print(f"A ordem será {", ".join(map(str, fila))}")
      continue
  
    elif i == 2: 
      remover = input("Digite o paciente que vai sair da fila: ")
      fila.remove(remover)
      print(f"A ordem será {", ".join(map(str, fila))}")
      continue
    
    elif i == 3:
      break

paciente()