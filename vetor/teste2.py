import os
os.system("cls")

dicionario = {}
lista=[]
lista2=[]
lista3=[]
listaf=[lista, lista2, lista3]

nome=input("Digite o seu nome: ")
lista.append(str(input("Qual o seu sexo [M] para Masculino e [F] Feminino: ")).upper())
lista.append(int(input("Digite a sua idade: ")))

nome2=input("Digite o seu nome: ")
lista2.append(str(input("Qual o seu sexo [M] para Masculino e [F] Feminino: ")).upper())
lista2.append(int(input("Digite a sua idade: ")))

nome3=input("Digite o seu nome: ")
lista3.append(str(input("Qual o seu sexo [M] para Masculino e [F] Feminino: ")).upper())
lista3.append(int(input("Digite a sua idade: ")))

dicionario[nome]=lista
dicionario[nome2]=lista2
dicionario[nome3]=lista3

print("\n",dicionario)

media=(lista[1]+lista2[1]+lista3[1])/3 

print(f"\n\tA media das idades é: {round(media,2)}\n")