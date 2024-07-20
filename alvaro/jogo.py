import random

print("=="*40)
print("                      Vamos Jogar Pedra, Papel ou Tesoura!                      ")
print("=="*40)

print("\n--------------\033[7;40mPor favor escreva a primeira letra sempre maiúscula\033[m---------------")

opcoes = ["Pedra", "Papel", "Tesoura"]

while True:
  escolha = input("\nEscolha o que você vai jogar: ")
  computador = random.choice(opcoes)

  if escolha == "Pedra" and computador == "Papel" or escolha == "Papel" and computador == "Tesoura" or escolha == "Tesoura" and computador == "Pedra":
    print(f"Você jogou {escolha} e eu joguei {computador} então... \033[1;41m VOCÊ PERDEU \033[m")
    break
  
  elif escolha == "Pedra" and computador == "Tesoura" or escolha == "Papel" and computador == "Pedra" or escolha == "Tesoura" and computador == "Papel":
    print(f"Você jogou {escolha} e eu joguei {computador} então... \033[1;42m VOCÊ GANHOU \033[m")
    break

  elif escolha == computador: 
   print(f"Que coicidência!!! Jogamos igual vamos mais uma vez...")
   continue

  elif escolha != "Pedra" or escolha != "Papel" or escolha != "Tesoura": 
    print("\n\033[1;41mPor favor escreva da maneira correta!\033[m")
    continue

#pedra ganha da tesoura
#papel ganha da pedra 
#tesoura ganha do papel

# pedra perde pra papel
# papel perde pra tesoura
# tesoura perde pra pedra