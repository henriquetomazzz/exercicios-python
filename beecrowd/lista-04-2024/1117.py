cont=0 
soma=0 

while(cont<2):
  n1 = float(input())
  
  if(n1<0 or n1>10):
    print("nota invalida")

  else:
    soma+=n1
    cont+=1
  n2 = float(input())
  
  if(n2<0 or n2>10):
    print("nota invalida")

  else:
    soma+=n2
    cont+=1

  if(n1>=0 and n1<=10 and n1>=0 and n2<=10):
    cont+=2  
    break

print("media = %.2f" %(soma/2))