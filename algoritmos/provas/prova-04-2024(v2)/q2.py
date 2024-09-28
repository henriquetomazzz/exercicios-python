'''Crie uma função recursiva em Python que calcula a soma dos dígitos de um número inteiro positivo. A soma dos dígitos
é obtida somando todos os dígitos que compõem o número.
Exemplos:
▪ 123 → 6
▪ 541 → 10
▪ 896 → 23'''
def soma(n):
  if len(n) == 0: 
    return 0
  return int(n[-1]) + soma(n[:-1])

n = input()
print(soma(n))
