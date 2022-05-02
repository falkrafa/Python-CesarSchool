import os
os.system("cls")

vetor = []
cont=0
cont2=0
cont3=0



for i in range(10):
    valor=int(input("Digite um numero: "))

    vetor.append(valor)
print(vetor)

for i in range(10):
    if vetor[i]>vetor[0]:
        cont+=1
    elif vetor[i]<vetor[0]:
        cont2+=1
    elif vetor[i]==vetor[0]:
        cont3+=1

print(f"\nNumeros maiores que o primeiro elemento do vetor: {cont}")
print(f"Numeros menores que o primeiro elemento do vetor: {cont2}")
print(f"Numeros iguais ao primeiro elemento do vetor: {cont3-1}\n")




    
     

