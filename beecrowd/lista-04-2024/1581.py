n = int(input())

for i in range(n):
    k = int(input())
    idioma = input()
    mesmoIdioma = True

    for c in range(1, k):
        s = input()
        
        if(s != idioma):
            mesmoIdioma = False
    
    print("ingles" if not mesmoIdioma else idioma)