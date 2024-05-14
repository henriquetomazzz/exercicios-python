'''Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno, cosseno e tangente desse â ngulo '''
from math import radians, sin, cos, tan   
an = float(input("Digite o ângulo que você deseja: "))
seno = sin(radians(an))
print(f"O angulo de {an} tem o Seno de {seno:.2f}")
cosseno = cos(radians(an))
print(f"O angulo de {an} tem o Cosseno de {cosseno:.2f}")
tangente = tan(radians(an))
print(f"O angulo de {an} tem o Cosseno de {tangente:.2f}")