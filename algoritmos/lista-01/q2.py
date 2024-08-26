'''
Uma empresa quer dar um bônus de Natal (em dezembro, claro) para seus empregados que 
será 60% do cálculo médio do salário de trabalho. Considerando que todos na empresa 
ganhem um mesmo valor de salário, elabore um programa que receba a entrada do salário e 
imprima o valor do bônus de Natal e o valor a ser depositado na conta de cada empregado 
em dezembro.
'''
sal = int(input("Digite seu sálario: "))
bonus = sal*1.06

print(f"O bônus será de R${bonus-sal}")
print(f"Seu sálario com bônus ficará R${bonus:.2f}. Feliz Natal!")