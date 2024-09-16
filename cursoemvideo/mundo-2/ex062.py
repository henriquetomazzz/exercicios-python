'''Melhore o DESAFIO 061, perguntando para o usuário se ele quer mostrar mais alguns temos. o programa encerraré
quando ele disser que quer mostrar 0 termos'''
print("Gerador de PA")
print("-="*15)

primeiro = int(input("Primeiro termo: "))
razao = int(input("Razão da PA: "))
termo = primeiro
contador = 1
total = 0
mais = 10

while mais != 0:
  total = total + mais
  while contador <= total:
    print(f"{termo}"+"-> ", end='')
    termo += razao
    contador += 1
  print("PAUSA")
  mais = int(input("Quantos termos você quer mostrar a mair? "))
print("FIM")