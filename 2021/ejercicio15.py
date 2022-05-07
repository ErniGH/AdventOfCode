entrada = []
pF = []
dx = [1, 0,  -1,  0]
dy = [0,  1,  0, -1]


matrizPeso = []


def explorar(posicion):
    for d in range(len(dx)):
        xx = posicion[0] + dx[d]
        yy = posicion[1] + dy[d]

        if 0 <= xx < len(entrada) and 0 <= yy < len(entrada[0]):
            s = matrizPeso[posicion[0]][posicion[1]] + entrada[xx][yy]
            if s < matrizPeso[xx][yy]:
                matrizPeso[xx][yy] = s
                explorar([xx, yy])


while True:
    e = input()
    if e == "fin":
        break
    entrada.append([int(i) for i in e])

pF = [len(entrada), len(entrada[0])]
matrizPeso = [[1000 for i in range(pF[1])] for j in range(pF[0])]

matrizPeso[0][0] = 0
explorar([0, 0])

for i in matrizPeso:
    print(i)