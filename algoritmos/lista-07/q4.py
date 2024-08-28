'''Escreva um algoritmo que leia as 4 médias bimestrais para cada um dos 40 alunos de uma turma. Em seguida,
deve se calcular e imprimir a média anual de cada aluno e a média anual da turma. Mantenha as médias todas
em uma lista, estrutura que deve ser criada ao longo da entrada. Crie métodos, a sua escolha, para usar 
durante o processamento dos dados.'''
def soma(lista):
  somaTotal = sum(lista)
  mediaTotal = somaTotal/len(lista)

  print(f"A soma total da turma é igual a {somaTotal}")
  print(f"A média total da turma é igual a {mediaTotal}") 

lista = []

def entrada():
  for i in range(0, 40):
    nota1, nota2, nota3, nota4 = map(float, input().split())
    lista.append(nota1)
    lista.append(nota2)
    lista.append(nota3)
    lista.append(nota4)
    print(f"As notas do aluno são: {nota1, nota2, nota3, nota4}")
    print(f"A media é {(nota1+nota2+nota3+nota4)/4}")

  soma(lista)
entrada()