import os
os.system ("cls")

total=0
valor=float(input("Digite o valor da sua compra: "))

while valor!=0:
    if valor<0:
        print("valor inválido")
    else:
        total= total+valor
    valor=float(input("Digite o valor da sua compra: "))

if total>1000:

    total-=total*0.01
print("Total a pagar:", total)
    
    






   
    




