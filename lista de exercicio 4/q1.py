import os
os.system("cls")

vetor=[]
graus=[]

for i in range(10):
    temp= float(input("Digite uma temperatura em grau farenheit: "))

    vetor.append(temp)
print("\ntemperaturas em farenheit:", vetor)

for i in range(10):
    C = round(5*(vetor[i]-32)/9,2)

    graus.append(C)
print("\nTemperaturas convertidas para celsius:", graus,"\n")





