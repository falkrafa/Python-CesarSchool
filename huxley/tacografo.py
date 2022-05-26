num = int(input())

distancia = 0
for i in range(num):
    tempo,velocidade = [int(tempo) for tempo in input().split()]
    dist = velocidade*tempo
    distancia += dist
print(distancia)