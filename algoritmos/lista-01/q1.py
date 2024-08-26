'''
Escreva um programa que efetue a apresentação do valor da conversão em real (R$) de um 
valor lido em dólar (US$). O algoritmo deverá solicitar ao usuário o valor da cotação do
dólar e também a quantidade de dólares que ele deseja converter em real.
'''
dollar = float(input("Digite o valor em dólar: US$ "))
cotacao = float(input("Digite a cotação atual do dóla para real: "))

print("O valor em real será: ", dollar*cotacao)