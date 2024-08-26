'''
Um aluno recebe 3 notas, nota das listas, nota do projeto e nota das provas.
Calcule a média pondera dessas notas tal que: nota das listas vale 20%, nota
do projeto vale 30% e nota das provas vale 50%.
'''
lista = float(input("Digite a nota da lista: "))*20/100
projeto = float(input("Digite a nota do projeto: "))*30/100
prova = float(input("Digite a nota da prova: "))*50/100

media = (lista+projeto+prova)/1

print(f"A media será {media}")