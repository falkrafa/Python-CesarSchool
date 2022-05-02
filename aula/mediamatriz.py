import os
os.system("cls")

matriz=[[],[],[]]
soma=0
for l in range(3):
    for c in range(4):
        matriz[l].append(int(input(f"digite as notas [{l+1}] [{c+1}]: ")))
        soma+=matriz[l][c]
media = soma/12
print(media)
