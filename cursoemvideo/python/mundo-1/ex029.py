'''Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado. A multa vai custar R$7,00 por cada Km acima do limite.'''
vel = float(input("Qual a velocidade do carro? "))

if vel > 80:
  print("MULTADO! você excedeu o limite permitido que é de 80km/h")
  print(f"Você deve pagar uma multa de R${(vel-80)*7:.2f}") 
print("Tenha um bom dia! Dirija sempre com segurança!")