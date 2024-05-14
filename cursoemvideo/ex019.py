'''Um professor que sortear um de seus quatro alunos para apagar o quadro. Faça um programa que ajude ele, lendo o nome dele e escrevendo o nome do escolhido'''
import random 
n1 = input("Digite o nome do aluno: ")
n2 = input("Digite o nome do aluno: ")
n3 = input("Digite o nome do aluno: ")
n4 = input("Digite o nome do aluno: ")

lista = [n1, n2, n3, n4]

print(f"O aluno escolhido foi {random.choice(lista)}")