'''
Escreva um programa que leia o nome de um aluno e as notas das três provas que ele obteve
no semestre. No final informe o nome do aluno e a sua média(aritmética). 
Exemplo de formatação da saída:
Nome do aluno: Alice
Media de Alice é: 8.5
'''
nome = input("Digite o nome do aluno: ")

nota01 = float(input("Digite a primeira nota: "))
nota02 = float(input("Digite a segunda nota: "))
nota03 = float(input("Digite a terceira nota: "))

media = (nota01 + nota02 + nota03)/3

print("Nome do aluno: ", nome)
print(f"Media de {nome} é: {media:.1f}")