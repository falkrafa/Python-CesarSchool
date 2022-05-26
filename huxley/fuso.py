x = input()
hora1 = int(x.split(' ')[0])
hora2 = int(x.split(' ')[1])
fuso = int(x.split(' ')[2])
hora_local = (hora1+hora2+fuso)%24
print(hora_local)