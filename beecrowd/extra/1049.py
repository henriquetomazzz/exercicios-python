'''
*ANIMAL*
Neste problema, você deverá ler 3 palavras que definem o tipo de animal possível segundo 
o esquema abaixo, da esquerda para a direita.  Em seguida conclua qual dos animais 
seguintes foi escolhido, através das três palavras fornecidas.

https://resources.beecrowd.com/gallery/images/problems/UOJ_1049_b.png

Entrada
A entrada contém 3 palavras, uma em cada linha, necessárias para identificar o animal
segundo a figura acima, com todas as letras minúsculas.

Saída
Imprima o nome do animal correspondente à entrada fornecida.
'''
A = input() 
B = input() 
C = input()

if A == "vertebrado" and B == "ave" and C == "carnivoro":
  print("aguia")
elif A == "vertebrado" and B == "ave" and C == "onivoro":
  print("pomba")

if A == "vertebrado" and B == "mamifero" and C == "onivoro":
  print("homem")
elif A == "vertebrado" and B == "mamifero" and C == "herbivoro": 
  print("vaca")

if A == "invertebrado" and B == "inseto" and C == "hematofago":
  print("pulga")
elif A == "invertebrado" and B == "inseto" and C == "herbivoro":
  print("lagarta")

if A == "invertebrado" and B == "anelideo" and C == "hematofago":
  print("sanguessuga")
elif A == "invertebrado" and B == "anelideo" and C == "onivoro":
  print("minhoca")
