import os
os.system ("cls")

matriz= [[],[],[]]
soma=0

for l in range(3):
    for c in range(1): 
        matriz[0].append(int(input(f"Digite o salario medio da profissao {l+1}: ")))
        
for l in range(3):
    for c in range(1):
        matriz[1].append(int(input(f"Digite o tempo mínimo de experiência da profissao {l+1}: ")))
        
for l in range(3):
    for c in range(1):
        matriz[2].append(int(input(f"Digite o valor da hora de trabalho {l+1}: ")))

print("\t  DJ\t  AS\t  CD")
for l in range(3):
    for c in range(3): 
        print(f"\t[{matriz[l][c]:^5}]", end="")
    print()

print("\nmedia dos salario:", sum(matriz[0])/3)

for l in range(3):
    for c in range(3):
        if c==l:
            soma+=matriz[l][c]
print("a soma das diagonais é: ",soma,"\n")