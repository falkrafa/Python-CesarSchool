vetor=[]
for i in range(0,5):
    n1= float(input("digite a sua nota: "))

    vetor.append(n1)

print(vetor)
media=sum(vetor)/len(vetor)
print("\na media das notas é:", media,"\n")

for a in range(5):
    if vetor[a]>media:
        
        print("a nota",vetor[a],"foi maior que a media")


    