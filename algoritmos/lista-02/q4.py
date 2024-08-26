'''
Faça um programa que peça o tamanho de um arquivo para download (em
MB) e a velocidade de um link de Internet (em MBps), calcule e informe o
tempo aproximado de download do arquivo usando este link em segundos e
em minutos.
'''
arquivo = float(input("Digite o tamanho do seu arquivo em Megabytes(MB): "))
internet = float(input("Digite a velocidade da sua internet por Megabytes por segundo(MBps): "))

tempo = arquivo/(internet/8)

print(f"O tempo de download será de {tempo} segundos")