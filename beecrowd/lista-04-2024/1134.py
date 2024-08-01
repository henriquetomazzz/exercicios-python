alcool = 0
gasolina = 0
diesel = 0

while True: 
  entrada = int(input())
  if entrada == 1:
    alcool += 1
    continue
  if entrada == 2:
    gasolina += 1
    continue
  if entrada == 3:
    diesel += 1
    continue
  if entrada > 4:
    continue
  if entrada == 4:
    break

print("MUITO OBRIGADO")
print("Alcool:", alcool)
print("Gasolina:", gasolina)
print("Diesel:", diesel)