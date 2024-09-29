'''Escreva um programa em Python que utilize uma pilha para verificar se uma sequência de parênteses está correta. O
programa deve ler uma sequência de parênteses do usuário e usar uma pilha para verificar se cada parêntese de abertura
tem um correspondente de fechamento.
Exemplos:
▪ (2+3)/4 → True
▪ )2+3( → False
▪ ( ) → True
▪ ) ( → False
▪ ((( ))) → True
▪ ((( )) → False
▪ ((tirei100)) → True'''
expr = str(input())

pilha = []

for simb in expr:
  if simb == '(':
    pilha.append('(')
  elif simb == ')':
    if len(pilha) > 0: 
      pilha.pop()
    else: 
      pilha.append(')')
      break
if len(pilha) == 0:
  print(True)
else: 
  print(False)