media=float(input())
faltas=int(input())

def Classificaaluno():
    if media >= 7 and media <=9.5 and faltas <= 10:
        print("APROVADO")
    elif media >= 9.5 and faltas <=10:
        print("APROVADO COM LOUVOR")
    elif media<7 and faltas <=10:
        print("REPROVADO")
    else:
        print("REPROVADO POR FALTAS")
Classificaaluno()