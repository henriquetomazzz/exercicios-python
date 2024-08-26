'''
5. Escreva programa que pergunte a distância em km que um passageiro
deseja percorrer e calcule o preço da passagem, cobrando R$ 0,53 por km
para viagens de até 200 km e R$ 0,47 por km para viagens mais longas.
'''
dist = float(input("Digite a distância que será percorrida em km: "))

if dist <= 200: 
  print(f"O valor da corrida será {dist * 0.53:.2f}")
else:
  print(f"O valor será {dist * 0.47:.2f}")