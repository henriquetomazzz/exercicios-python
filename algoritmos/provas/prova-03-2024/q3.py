'''A empresa local de abastecimento de água, a Saneamento Básico da Cidade (SBC), está promovendo uma campanha de
conservação de água, distribuindo cartilhas e promovendo ações demonstrando a importância da água para a vida e para
o meio ambiente. Para incentivar mais ainda a economia de água, a SBC alterou os preços de seu fornecimento de forma
que, proporcionalmente, aqueles clientes que consumirem menos água paguem menos pelo metro cúbico. Todo cliente paga
mensalmente uma assinatura de R$7, que inclui uma franquia de 10 m^3 de água. Isto é, para qualquer consumo entre 0
e 10 m^3, o consumidor paga a mesma quantia de R$7 reais (note que o valor da assinatura deve ser pago mesmo que o 
consumidor não tenha consumido água). Acima de 10 m^3, cada metro cúbico subsequente tem um valor diferente, 
dependendo da faixa de consumo. A SBC cobra apenas por quantidades inteiras de metros cúbicos consumidos.
A tabela abaixo especifica o preço por metro cúbico para cada faixa de consumo:'''
consumo = float(input("Digite o consumo de água em m³: "))
total = 7

if consumo > 10:
    consumo -= 10

    if consumo <= 20:
        total += consumo * 1
    
    else:
        total += 20 * 1
        consumo -= 20

        if consumo <= 70:
            total += consumo * 2
    
        else:
            total += 70 * 2
            consumo -= 70
            total += consumo * 5

print(f"O valor total da conta de água é: R$ {total:.2f}")