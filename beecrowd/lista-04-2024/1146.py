while True:
    num = int(input())
    x = ''
    if(num == 0):
        break
    
    for i in range(1, num + 1):
        x += str(i) + " "
    print(x[:-1])