'''
*CONVERSÃO DE TEMPO*
Leia um valor inteiro, que é o tempo de duração em segundos de um determinado evento em 
uma fábrica, e informe-o expresso no formato horas:minutos:segundos.

Entrada
O arquivo de entrada contém um valor inteiro N.

Saída
Imprima o tempo lido no arquivo de entrada (segundos), convertido para horas:minutos:
segundos, conforme exemplo fornecido.
'''
sec = int(input())

hr = sec//(60*60)
sec = sec%(60*60)

min = sec//60
sec = sec%60

print(f"{hr}:{min}:{sec}")