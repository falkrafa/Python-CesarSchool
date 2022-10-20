import os
os.system("cls")
# teste
print("Teste de anagrama.")
print()

nome1= input("Digite uma palavra: ")
nome2= input("Digite outra palavra: ")

lista=list(nome1)
lista.sort()
lista1=list(nome2)
lista1.sort()

if lista == lista1:
    print("\nEssas palavras sao anagramas!\n")
else:
    print("\nEssas palavras não sao anagramas!\n")
    

    