import os
os.system("cls")

altura=(float(input("Digite a sua altura: ")))
peso=(float(input("Digite o seu peso: ")))
sexo=(str(input("Digite o seu sexo [M] ou [F]: ")))
homem=round((72.7 * altura)-58,2)
mulher=round((62.1 * altura)-44.7,2)

if sexo == "M":
    print("Peso ideal:", homem)
    if peso>homem:
        print(f"seu peso: {peso}, Voce esta acima do peso")
    elif peso<homem:
        print(f"seu peso: {peso}, Voce esta abaixo do peso")
    else:
        print(f"seu peso: {peso}, Voce esta no peso ideal")
elif sexo== "F":
    print("peso ideal:", mulher)
    if peso>mulher:
        print(f"seu peso: {peso}, voce esta acima do peso")
    elif peso<mulher:
        print(f"seu peso: {peso}, Voce esta abaixo do peso")
    else:
        print(f"seu peso: {peso}, Voce esta no peso ideal")