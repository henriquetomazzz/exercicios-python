'''
Escreva um programa que calcule com quantos litros de gasolina é preciso abastecer um 
veículo, dada a distância que se deseja percorrer e a quantidade de quilômetros que o
veículo faz por litro.
'''
distancia = float(input("Digite a distância que será percorrida: "))
gasto = float(input("Digite a quantidade de quilômetros que seu carro faz por litro: "))

litros = distancia/gasto

print(f"É preciso abastercer o carro com {litros:.2f}L para percorrer a distância dada.")