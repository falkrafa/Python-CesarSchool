def tabuada(multiplicador):
        resp = num * multiplicador
        return resp


multiplicador = int(input())
resp = 0
for num in range(0,11):
    resp =  tabuada(multiplicador)

    print('{} x {} = {}'.format(num, multiplicador, resp))