'''Crie um programa que faça o computado jogar jokenpô com você'''
from random import randint

itens = ("Pedra", "Papel", "Tesoura")
computador = randint(0, 2)

print("Suas opções: ")
print("[ 0 ] PEDRA")
print("[ 1 ] PAPEL")
print("[ 2 ] TESOURA")
escolha = int(input("Qual é a sua jogada? "))

print("-="*10)
print(f"Computador jogou {itens[computador]}")
print(f"Jogador jogou {itens[escolha]}")
print("-="*10)

if computador == 0:
  if escolha == 0:
    print("EMPATE")
  elif escolha == 1:
    print("JOGADOR VENCE")
  elif escolha == 2:
    print("COMPUTADOR VENCE")
  else:
    print("JOGADA INVALIDA!")

elif computador == 1:
  if escolha == 0:
    print("COMPUTADOR VENCE")
  elif escolha == 1:
    print("EMPATE")
  elif escolha == 2:
    print("JOGADOR VENCE")
  else:
    print("JOGADA INVALIDA!")

elif computador == 2:
  if escolha == 0:
    print("JOGADOR VENCE")
  elif escolha == 1:
    print("COMPUTADOR VENCE")
  elif escolha == 2:
    print("EMPATE")
  else:
    print("JOGADA INVALIDA!")