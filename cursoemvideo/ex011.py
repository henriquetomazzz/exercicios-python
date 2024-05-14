'''Faça um programa que leia a largura e a altura de uma parada em metros, calcule sua area e a quantidade necessária para pintá-la, sabendo que cada litro de tinta pinta uma aréa de 2 metros2'''
alt = float(input("Digite a altura da parede: "))
larg = float(input("Digite a largura da parede: "))

print(f"A quantidade de tinta necessária será de {(alt*larg)/2}l")