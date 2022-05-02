import os
os.system("cls")

matriz=[[],[],[],[]]
soma=0
for l in range(4):
    for c in range(5):
        matriz[l].append(int(input(f"no trimestre [{l+1}], quantas garrafas foram vendidas na regiao [{c+1}]: ")))
        soma+=matriz[l][c]
print(soma)
