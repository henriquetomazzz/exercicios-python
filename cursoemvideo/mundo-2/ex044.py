'''Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de
pagamento
-à vista dinheiro/cheque: 10% de desconto
-à vista no cartão: 5% de desconto
-em até 2x no cartão: preço formal
-3x ou mais no cartão: 20% de juros'''
print("="*10 + "LOJA" + "="*10)
compra = int(input("Preço das compras: R$ "))

print("FORMAS DE PAGAMENTO")
print("[ 1 ] à vista dinheiro/cheque")
print("[ 2 ] à vista no cartão")
print("[ 3 ] 2x no cartão")
print("[ 4 ] 3x ou mais no cartão")
opcao = int(input("Qual é a opção? "))

if opcao == 1: 
  print(f"Sua compra de R${compra:.2f} vai custar R${compra-(compra*0.10):.2f} COM DESCONTO.")

elif opcao == 2: 
  print(f"Sua compra de R${compra:.2f} vai custar R${compra-(compra*0.5):.2f} COM DESCONTO.")

elif opcao == 3: 
  print(f"Sua compra será parcelada em 2x de R${compra/2} SEM JUROS.")

elif opcao == 4:
  parcelas = int(input("Quantas pascelas? ")) 
  print(f"Sua compra será pascelada em {parcelas}x de R${(compra+(compra*0.2))/parcelas:.2f} COM JUROS")
  print(f"Sua compra de R${compra:.2f} vai custar R${compra+(compra*0.2):.2f} no final.")

else:
  print("Opção inválida!")