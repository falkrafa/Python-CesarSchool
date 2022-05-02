import os
os.system("cls")

vetor1= []
vetor2=[]
vetor3= []

for i in range(10):

    vetor1.append(int(input("Digite um valor para o vetor A: ")))

    if vetor1[i]%2!= 0:
        vetor2.append(vetor1[i])
    else:
        vetor3.append(vetor1[i])
print(f"Vetor A :{vetor1}")
print(f"Novo vetor com os valores impares: {vetor2}")
print(f"Novo vetor com os valores pares: {vetor3}")
