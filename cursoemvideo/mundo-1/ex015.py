'''Escreva um programa que pergunte a qunatidade de km percorridos por um carro alugado e a quantidade de dias pelos
quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro  custa R$60 por dia e R$ 0,15 por km rodado '''
km = float(input("Digite a quantidade de km percorridos: "))*0.15
day = int(input("Digite a quantidade de dias que o carro foi alugado: "))*60

print(f"O valor total do aluguel será de R${km+day}")

