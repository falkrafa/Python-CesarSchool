import os 
os.system("cls")

nome=input("Digite o seu nome: ")
idade=int(input("Digite a sua idade: "))

if idade>=65:
    print("\nAtendimento com prioridade!")
    doenca=input("\nVoce possui alguma doenca contagiosa? ")
    if doenca== "sim" or doenca== "Sim":
        print("\nAguarde, voce sera encaminhado para a sala amarela!\n")
    else:
        print("\nAguarde, voce sera encaminhado para a sala branca!\n")

if idade<65:
    print("\nAtendimento sem prioridade!")
    doenca=input("\nVoce possui alguma doenca contagiosa? ")
    if doenca=="sim" or doenca=="Sim":
        print("\nAguarde, voce sera encaminhado para a sala amarela!\n")
    else:
        print("\nAguarde, voce sera encaminhado para a sala branca!\n")
