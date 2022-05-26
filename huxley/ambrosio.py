valores={"1": 5.30, "2": 6, "3": 3.20, "4": 2.50}

desconto=0

codigo=input("Codigo do produto: ")
qnt=int(input("quantidade desejada: "))
final=valores[codigo]*qnt

if final >= 40 or qnt >= 15:
    desconto= final-(final*0.15)
    print("Preco final a ser pago: R$ %.2f"%(desconto))
else:
    print("Preco final a ser pago: R$ %.2f"%(final))
