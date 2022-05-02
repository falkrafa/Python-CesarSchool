import os
os.system ("cls")

valor1=int(input("Digite o primeiro valor: "))
valor2=int(input("Digite o segunda valor: "))
valor3=int(input("Digite o terceiro valor: "))

if valor1<(valor2+valor3) and valor2<(valor1+valor3) and valor3<(valor1+valor2):
    print("Esses valores formam um triangulo!")
else:
    print("Esses valores nao formam um triangulo!")

