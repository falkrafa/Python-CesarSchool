import os
os.system ("cls")

lista= []
cont=0

for i in range (0,10):
    num=int(input("digite um numero: "))

    lista.append(num)
print(lista)

print("\no menor elemento da lista é", min(lista))
print("\no menor elemento da lista é", max(lista))

for a in range(10):
    if lista[a]%2!=0:
        cont+=1
        
print("valores impares:", cont)