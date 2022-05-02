import os 
os.system("cls")
soma=0
matriz = [[],[],[]]
somac=0

for l in range(3):
    for c in range(3):
        matriz[l].append(int(input(f"digite um valor para [{l}] [{c}]: ")))

for l in range(3):
    for c in range(3): 
        print(f"[{matriz[l][c]:^4}]", end="")
        if matriz[l][c]%2!=0: 
            soma= matriz[l][c] +soma 
    print()
print(soma)

for l in range(3):
    somac+=matriz[l][0]

print(somac)

for c in range(3):
    menor = min(matriz[2])
print(menor)
 


