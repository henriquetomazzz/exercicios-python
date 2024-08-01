leds = [6, 2, 5, 5, 4, 5, 6, 3, 7, 6]

n = int(input())

for i in range(n):
    v = input().strip()

    resposta = 0
    for numero in v:
        resposta += leds[int(numero)]

    print(f"{resposta} leds")