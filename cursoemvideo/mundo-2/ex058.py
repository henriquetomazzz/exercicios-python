'''Melhore o jogo do DESAFIO 028 onde o computador vai 'pensar' em um número entre 0 a 10. Só que agora o jogador 
vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer'''
from random import randint
print("Sou seu computador...")
print("Acabei de pensar em um número entre 0 e 10.")
print("Será que você consegue adivinhar qual foi? ")
computador = randint(0, 10)
acertou = False
palpites = 0

while not acertou:
  jogador = int(input("Qual o seu palpite? "))
  palpites += 1
  if jogador == computador: 
    acertou = True
print(f"Acertou com {palpites} tentativas. Parabéns!")