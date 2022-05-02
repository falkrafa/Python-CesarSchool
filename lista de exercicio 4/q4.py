import os 
os.system("cls")

matriz= [[],[],[]]
soma1=0
soma2=0
soma3=0
vetor= []
vetor2= []
vetor3= []

for l in range(3):
    for c in range(3):
        matriz[l].append(float(input(f"digite um valor para [{l}] [{c}]: ")))

for l in range(3):
    for c in range(3): 
        print(f"[{matriz[l][c]:^4}]", end="")
    print()
for l in range(3):
    soma1+=matriz[l][0]
    soma2+=matriz[l][1]
    soma3+=matriz[l][2]

vetor.append(soma1)
vetor2.append(soma2)
vetor3.append(soma3)

print(f"\n O vetor da soma das colunas é: {vetor+vetor2+vetor3}\n")




    
    

