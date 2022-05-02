valores=[3.5,6.7,1.0,4.9]

valores.insert(1,2.3)
print(valores)

valores.pop()
print(valores)

valores[2]=9.2
print(valores)

valores.sort()
print(valores)

print(len(valores))

for c,v in enumerate(valores):
    print("na posicao", c, "encontrei o valor", v)
