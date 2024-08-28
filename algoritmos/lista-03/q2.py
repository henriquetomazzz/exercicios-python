'''
Faça um programa que receba dados de um funcionário, tais como:
Nome, quantidade de horas trabalhadas, valor por hora trabalhada e
calcule o salário desse funcionário. O salário deve ser exibido na tela
indicando o quanto aquele funcionário receberá.
'''
nome = input("Nome do funcionário: ")
hrs = float(input("Horas trablhadas: "))
valor = float(input("Valor da hora trabalhada: "))

print(f"O salário de {nome} será de {valor*hrs:.2f}")