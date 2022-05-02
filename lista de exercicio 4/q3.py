import os
os.system("cls")

vetorA=[]
vetorB=[]
vetorC=[]
soma=0
soma2=0
cont =0

for i in range(5):
    na= int(input("Digite valores para o vetor A: "))

    vetorA.append(na)

print(f"\nVetor A: {vetorA}\n")

for a in range(5):
    nb= int(input("Digite valores para o vetor B: "))

    vetorB.append(nb)
print(f"\nVetor B: {vetorB}\n")

vetorC= vetorA + vetorB
print(f"Uniao de A e B:{vetorC}")

for b in range(10):
    if vetorC[b]%2==0:
        soma = soma+ vetorC[b]
    elif vetorC[b]%2!=0:
        soma2= soma2 + vetorC[b]
        cont=cont+1

print(f"\nA soma dos numero pares da uniao entre (A e B) é: {soma}")
print(f"A media dos numeros impares da uniao entre (A e B) é: {round(soma2/cont,2)}")
print("O menor valor da uniao entre (A e B) é: ", min(vetorC),"\n")

    

    




    



        


    











