vetor = []

def prodprimos(valores):
    global mult
    mult = 1
    div = 0

    for b in range(1,valores+1):
        if valores%b==0:
            div+=1
    if div==2:
        vetor.append(valores)
        if len(vetor) == 4:
           mult = vetor[0]*vetor[1]*vetor[2]*vetor[3]
    else:
        print("SEM PRODUTO")
        exit()

    if mult != 1:
        print(mult)

valores = input().split()

for i in valores:
    x = [int(i)]
    for a in x:
        prodprimos(a)
        break