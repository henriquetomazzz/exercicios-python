n = int(input())

for i in range(n):
    num = int(input())
    count = 0
    
    for i in range(1,num+1):
        if num%i == 0:
            count+=1

    if count != 2:
        print(f'{num} nao eh primo')

    elif count == 2:
        print(f'{num} eh primo')
        