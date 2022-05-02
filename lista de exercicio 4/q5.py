import os
os.system ("cls")

matriz=[[],[],[]]

soma=0
soma1=0

for l in range(3):
    for c in range(1):
        matriz[l].append(float(input(f"Estagiário {l+1} digite o seu salario: ")))

for l in range(3):
    for c in range(1):
        matriz[l].append(float(input(f"Estagiário {l+1} digite o valor do seu vale transporte: ")))

for l in range(3):
    for c in range(1):
        matriz[l].append(float(input(f"Estagiário {l+1} digite o valor do seu vale alimentacao: ")))
print()
print("\tsalario\t  VT\t  VA")

for l in range(3):
    for c in range(3): 
        print(f"\t[{matriz[l][c]:^4}]", end="",)
    print()
for l in range(3):
    soma+= matriz[l][0]
    soma1+= matriz[l][1]

print(f"\nA media salarial é {round(soma/3,2)} reais")
print(f"\nO valor total gasto com vale transporte é {soma1} reais\n")





    

    

