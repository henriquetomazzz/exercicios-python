'''
Escreva um programa que leia uma temperatura em graus Celsius e a apresente convertida 
em graus Fahrenheit. A fórmula de conversão é: F = (9*C+160) / 5, sendo F a temperatura 
em Fahrenheit e C a temperatura em Celsius.
'''
temp = float(input("Digite a temperatura em Graus Celsius: "))

print(f"A temperatura em graus Fahrenheit é {(9*temp+160)/5:.2f} °F")