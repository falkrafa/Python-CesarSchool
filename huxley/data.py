data = input().split("/")
dia = data[0]
mes = data[1]
ano = data[2]
print("{}/{}/{}".format(mes, dia, ano))
print("{}/{}/{}".format(ano, mes, dia))
print("{}-{}-{}".format(dia, mes, ano))