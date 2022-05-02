import os
os.system("cls")


qnt=int(input("Quantos funcionarios a esmpresa possui? "))

for a in range(qnt):
    salario=(float(input("\nDigite o salario do funcionario: ")))
    
    if salario<3000:
        print("\nCom aumento de 10%, o salario ficara:", salario*1.10)
    elif salario>=3000 and salario<5000:
        print("\nCom aumento de 20%, o salario ficara:", salario*1.20)
    elif salario>=5000 and salario<7000:
        print("\nCom aumento de 30%, o salario ficara:", salario*1.30)
    else:
        print("\nCom aumento de 35%, o salario ficara: ", salario*1.35)