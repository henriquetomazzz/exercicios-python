'''Faça um programa que tenha uma função chamada area(), que receba as dimensões de um terreno retangular
(largura e comprimento) e mostre a área do terreno'''
def area():
  print("Controle de terrenos")
  print("-"*30)
  largura = float(input("LARGURA(m): "))
  comprimento = float(input("COMPRIMENTO(m): "))
  print(f"A área de um terreno {largura:.1f}x{comprimento:.1f} é de {largura*comprimento}m2")

area()