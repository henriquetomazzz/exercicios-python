'''
Leia um valor inteiro N. Este valor será a quantidade de valores inteiros X que 
serão lidos em seguida.
Mostre quantos destes valores X estão dentro do intervalo [10,20] e quantos estão 
fora do intervalo, mostrando essas informações.

Entrada
A primeira linha da entrada contém um valor inteiro N (N < 10000), que indica o 
número de casos de teste.
Cada caso de teste a seguir é um valor inteiro X (-107 < X <107).
 

Saída
Para cada caso, imprima quantos números estão dentro (in) e quantos valores estão 
fora (out) do intervalo.
'''
n = int(input())
countint = 0
countout = 0

for i in range(n):
  num = float(input())
  
  if num >= 10 and num <= 20:
    countint += 1
  
  if num < 10 or num > 20:
    countout += 1 

print(countint, "in")
print(countout, "out")