import os
os.system("cls")

dicionario = {}
lista=[]
lista2=[]
lista3=[]
listaf=[lista, lista2, lista3]

for i in listaf:
    nome=input("Digite o seu nome: ")
    i.append(str(input("Qual o seu sexo [M] para Masculino e [F] Feminino: ")).upper())
    i.append(int(input("Digite a sua idade: ")))
    dicionario[nome]= listaf[listaf.index(i)]
print("\n",dicionario)

media=(lista[1]+lista2[1]+lista3[1])/3 

print(f"\n\tA media das idades é: {round(media,2)}\n")



    
    

   
        




