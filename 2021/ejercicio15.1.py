entrada = []
en = []
pF = []
dx = [1, 0, -1,  0]
dy = [0, 1,  0, -1]
ayuda = [-1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 2, 3]


while True:
    e = input()
    if e == "fin":
        break
    en.append([int(i) for i in e])

pF = [len(en), len(en[0])]

entrada = [[0 for i in range(pF[1] * 5)] for j in range(pF[0] * 5)]
for i, linea in enumerate(en):
    for j, n in enumerate(linea):
        for x in range(5):
            for y in range(5):
                s = x + y
                sn = s+n
                r = ayuda[sn]
                xx = i+pF[0]*x
                yy = j+pF[1]*y
                entrada[xx][yy] = r

matrizPeso = [[1000000 for i in range(pF[1] * 5)] for j in range(pF[0] * 5)]
matrizVisitado = [[False for i in range(pF[1] * 5)] for j in range(pF[0] * 5)]

matrizPeso[0][0] = 0
listaPorVisitar = []


def pMinimo(listaTupla):
    posicion = 0
    m = 1000000
    for i, t in enumerate(listaTupla):
        if matrizPeso[t[0]][t[1]] < m:
            m = matrizPeso[t[0]][t[1]]
            posicion = i
    return listaTupla.pop(posicion)


listaPorVisitar.append((0, 0))

while len(listaPorVisitar) != 0:
    print(len(listaPorVisitar))
    posicion = pMinimo(listaPorVisitar)

    matrizVisitado[posicion[0]][posicion[1]] = True

    for d in range(len(dx)):
        xx = posicion[0] + dx[d]
        yy = posicion[1] + dy[d]

        if 0 <= xx < len(entrada) and 0 <= yy < len(entrada[0]) and not matrizVisitado[xx][yy]:
            su = matrizPeso[posicion[0]][posicion[1]] + entrada[xx][yy]
            if matrizPeso[xx][yy] > su:
                matrizPeso[xx][yy] = su
                listaPorVisitar.append((xx, yy))

print(matrizPeso[pF[0]*5-1][pF[1]*5-1])