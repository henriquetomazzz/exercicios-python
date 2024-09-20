'''Dizemos que um número natural é triangular se ele é produto de três números naturais consecutivos. Exemplo: 120 é 
triangular, pois 4 x 5 x 6 = 120. Implemente uma função que indica se um número é triangular ou não. Em seguida 
escreva um programa que leia números inteiros e indique se é triangular ou não, usando a função. O programa deve ser
encerrado quando a entrada for 0'''
def soma(n): 
  s = str(n)
  if len(s) == 1: 
    return n
  
  return int(s[-1]) + soma(int(s[:-1]))

print(soma(123))
print(soma(451))
print(soma(896))