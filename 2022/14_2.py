tablero = [["." for _ in range(700)] for _ in range(700)]
masBajo = 0
while True:
    entrada = input()
    if entrada == "-":
        break

    coordenadas = entrada.split(" -> ")
    posI = [int(c) for c in coordenadas.pop(0).split(",")]
    tablero[posI[0]][posI[1]] = "#"
    masBajo = max(posI[1], masBajo)
    while len(coordenadas) > 0:
        posF = [int(c) for c in coordenadas.pop(0).split(",")]
        masBajo = max(posF[1], masBajo)
        if posI[0] == posF[0]:
            ajuste = 1 if posI[1] < posF[1] else -1
            for i in range(posI[1], posF[1] + ajuste, ajuste):
                tablero[i][posI[0]] = "#"
        else:
            ajuste = 1 if posI[0] < posF[0] else -1
            for i in range(posI[0], posF[0] + ajuste, ajuste):
                tablero[posI[1]][i] = "#"
        posI = posF

print(masBajo)
input()
p = [0, 500]
contador = 0

while True:

    if p[0] == masBajo +1:
        tablero[p[0]][p[1]] = "O"
        contador += 1
        p = [0, 500]
    elif tablero[p[0]+1][p[1]] == ".":
        p[0] = p[0] + 1
    elif tablero[p[0]+1][p[1]-1] == ".":
        p[0] = p[0] + 1
        p[1] = p[1] - 1
    elif tablero[p[0]+1][p[1]+1] == ".":
        p[0] = p[0] + 1
        p[1] = p[1] + 1
    else:
        tablero[p[0]][p[1]] = "O"
        contador += 1
        if p == [0, 500]:
            break
        p = [0, 500]


for i in tablero:
    salida = ""
    for j in i:
        salida += j
    print(salida)

print(contador)
