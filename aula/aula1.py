num1=int(input("Digite um numero: "))
num2=int(input("Digite outro numero: "))

if num1%2 == 0:
    cont = num1
else:
    cont = num1 + 1
while cont <= num2:
    print(cont)
    cont += 2 
print("a soma dos pares é: ", cont+cont)
    