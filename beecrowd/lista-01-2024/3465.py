'''
*CIMBA*
Cimba herdou um terreno em formato triangular após o falecimento de seu pai. Para passar
o terreno para seu nome, o cartório exige que seja informada a área do terreno. Sabe-se
que o terreno é delimitado por uma cerca e Cimba consegue medir cada um dos lados do 
terreno. Você consegue ajudar Cimba a calcular a área do terreno dadas as medidas dos 
lados?

Entrada
A entrada é composta por 3 números a b c, que representam os lados do terreno.

Limites:
1 ≤ a, b, c ≤ 2023

Saída
Seu programa deve mostrar a área do terreno herdado por Cimba com 3 casas decimais, 
seguido do texto "m2". Confira nos exemplos.
'''
a, b, c = list(map (int, input().split()))

soma = (a + b + c)/2
triangulo = (soma * (soma-a) * (soma-b) * (soma-c)) ** 0.5

print(f'{triangulo:.3f} m2')