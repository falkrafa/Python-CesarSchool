lista = []
cont = 0

for i in range(100):
    idade = int(input(""))
    if idade == -1:
        break
    x = input("")
    vetor = x.split(" ")
    if idade>=18 and idade<=35 and vetor[0]=="f" and vetor[1]=="l" and vetor[2]=="v":
        cont+=1
    lista.append(idade)

print(f"Mais velho: {max(lista)}\nMulheres com olhos verdes, loiras com 18 a 35 anos: {cont/len(lista):.2%}")