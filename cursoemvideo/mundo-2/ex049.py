'''Refaça o desafio 009, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando o laço
for'''
entrada = float(input("Digite um número: "))
print("TABUADA")
for c in range(0, 11, 1):
  print(f"{c} X {entrada} = {c*entrada}")