'''
*PARES, ÍMPARES, POSITIVOS E NEGATIVOS*
Leia 5 valores Inteiros. A seguir mostre quantos valores digitados foram pares, quantos 
valores digitados foram ímpares, quantos valores digitados foram positivos e quantos 
valores digitados foram negativos.

Entrada
O arquivo de entrada contém 5 valores inteiros quaisquer.

Saída
Imprima a mensagem conforme o exemplo fornecido, uma mensagem por linha, não esquecendo 
o final de linha após cada uma.
'''
pares = 0
impares = 0
positivos = 0
negativos = 0

for i in range(5):
  val = float(input())

  if val%2 == 0:
    pares += 1
  if val%2 == 1:
    impares += 1
  if val > 0:
    positivos += 1
  if val < 0:
    negativos +=1

print(pares, "valor(es) par(es)")
print(impares, "valor(es) impar(es)")
print(positivos, "valor(es) positivo(s)")
print(negativos, "valor(es) negativo(s)")

