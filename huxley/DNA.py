lista = []

qnt = int(input("Digite quantos pares: "))
for i in range(qnt):
    cadeia1 = input("cadeia: ").upper()
    cadeia2 = input("cadeia:").upper()
    count = len(cadeia1)
    
    for j in range(count):
        if cadeia1[j] == "A":
            lista.append("T")
        elif cadeia1[j] == "T":
            lista.append("A")
        elif cadeia1[j] == "G":
            lista.append("C")
        elif cadeia1[j] == "C":
            lista.append("G")
    if cadeia2 == "".join(lista):
        print("COMPLEMENTARES")
    else:
        print("NAO COMPLEMENTARES")
        print("".join(lista))
    lista = []

