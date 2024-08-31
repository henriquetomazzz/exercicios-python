'''Tuconaldo Tripa é mecânico e anda meio broco. Precisa de sua ajuda. Desenvolva um programa que receba os 
nomes das peças que ele está removendo,  na ordem, e depois vá indicando, uma a uma,  na ordem inversa da 
adição, as peças para remontar o carro. Operações adicionar peça e remover peça.'''
lista = []
def adicionar():
  
  lista.reverse()
  print("Agora vamos fazer o processo contrário\n")
  print(f"A ordem será {", ".join(map(str, lista))}\n")

def remover():
  peca = input("Qual peça você deseja trocar: ") 

  while True: 
    troca = input("Digite o nome da peça removida: ")
    if peca != troca: 
      lista.append(troca)
      continue
    else: 
      lista.append(peca)
      break
  print("="*50)
  print(f"As peças removidas foram {", ".join(map(str, lista))}")
  print("="*50)

  adicionar()

remover()