fem = []
masc = []
for x in range(10):
    salario = float(input())
    sexo = input().lower()
    if sexo == 'm':
        masc.append(salario)
    else:
        fem.append(salario)
masc.sort()
fem.sort()
print(len(masc))
print(len(fem))
print("{:.1f}".format((sum(masc)+sum(fem))/(len(masc)+len(fem))))
if masc[-1] > fem[-1]:
    print('m')
else:
    print("f")
print("{:.1f}".format(sum(masc)/len(masc)))