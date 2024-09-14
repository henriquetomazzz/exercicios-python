'''Escreva um programa para aporvar o empréstimo bancário para a compra de uma casa. Pergunte o valor da casa, o
salário do comprador e em quantos anos ele vai pagar. A prestação mensal não pode exceder 30% do salário ou então
o emprestimo será negado'''
casa = float(input("Valor da casa: R$ "))
salario = float(input("Salário do comprador: R$ "))
financiamento = int(input("Quantos anos de financiamento: "))
prestacao = casa/(financiamento*12)

print(f"Para pagar uma casa de R${casa:.2f} em {financiamento} a prestação será de R${prestacao:.2f}")

if prestacao <= salario*0.3: 
  print("Empréstimo pode ser CONCEDIDO!")
else: 
  print("Empréstimo NEGADO!")