num = int(input())

def x():
    distancia = 0
    for i in range(num):
        tempo,velocidade = [int(tempo) for tempo in input().split()]
        dist = velocidade*tempo
        distancia += dist
    return distancia
print(x())


