'''Escreva um programa em Python que irá ler N números reais inseridos pelo usuário. Esses números representam todas
as notas obtidas por um aluno em um curso de programação. O usuário deverá sempre inserir números positivos entre 0 
e 100. O programa deve parar, caso a entrada não esteja entre os números aceitos. Ao parar, o programa deverá exibir
a média final do aluno que é calculada da seguinte forma: junção entre 70% da MAIOR NOTA e 30% da SEGUNDA MAIOR NOTA.
O usuário deverá inserir pelo menos duas notas. Caso contrário, o programa deve exibir um erro.
Ex:
ENTRADA: 8,5; 9,5; 10; 7; 0; -1
MÉDIA: 9,85 → SAÍDA'''
lista = [] 
contador = 0
while True: 
  nota = float(input("Insira sua nota: "))

  if nota < 0 or nota > 100: 
    break
  lista.append(nota)
  contador += 1
  if contador< 2:
    print("Quantidade de notas insuficientes!")
    continue
  
lista.sort()
print(f"Média: {(lista[-1]*0.7) + (lista[-2]*0.3):.2f}")