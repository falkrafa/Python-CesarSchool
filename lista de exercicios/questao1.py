import os 
os.system ("cls")
div=0

n1=int(input("insira um numero: "))

for a in range(1,n1+1):
    if n1%a==0:
        div+=1
if div==2:
    print("primo")
else:
    print("nao primo") 
    

