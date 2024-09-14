'''Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de
acordo com a média antingida:
-Média abaixo de 5.0: REPROVADO
-Média entre 5.0 e 6.9: RECUPERAÇÃO
-Média 7.0 ou superior: APROVADO'''
nota1 = float(input("Primeira nota: "))
nota2 = float(input("Segunda nota: "))
media = (nota1+nota2)/2

print(f"Tirando {nota1} e {nota2} a media do aluno é {media}")

if media < 5.0:
  print("O aluno está REPROVADO!")

elif media >= 5.0 and media <= 6.9:
  print("O aluno está em RECUPERAÇÃO!")

elif media == 7.0 or media > 7.0:
  print("O aluno está APROVADO")