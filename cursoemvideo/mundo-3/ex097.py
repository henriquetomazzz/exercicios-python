'''Faça um programa que tenha uma função chamada escreva(), que receba um texto qualquer como parametro e
mostre uma mensagem com tamanho adaptável'''
def escreva(text):
  tam = len(text)
  print("~"*tam)
  print(text)
  print("~"*tam)

escreva("Henrique")
escreva("Curso de python")