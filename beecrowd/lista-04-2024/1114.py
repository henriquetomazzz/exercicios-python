acesso = input()
senha = '2002'

while True: 
  if acesso != senha: 
    print('Senha Invalida')
    acesso = input()
    continue
  if acesso == senha:
    print("Acesso Permitido")
  break