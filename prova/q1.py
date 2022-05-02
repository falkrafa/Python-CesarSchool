import os
os.system("cls")

vetor = []
vetor.append(str(input("Voce conhece a vitima do roubo? S ou N: ")).upper())
vetor.append(str(input("Voce esteve no local do roubo? S ou N: ")).upper())
vetor.append(str(input("Voce mora perto da vítima? S ou N: ")).upper())
vetor.append(str(input("A vitima lhe devia? S ou N: ")).upper())
vetor.append(str(input("Voce ja trabalho com a vitima? S ou N: ")).upper())

if vetor.count("S")==2:
    print("\nSuspeito!!\n")
elif vetor.count("S")>2 and vetor.count("S")<5:
    print("\nCumplice!!\n")
elif vetor.count("S")==5:
    print("\nLadrao!!\n")
else:
    print("\nInocente!!\n")




    


