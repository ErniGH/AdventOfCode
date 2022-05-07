def mostrarMatriz(m):
    for i in m:
        print("".join(map(str,i)))

entrada = []
for i in range(10):
    entrada.append([int(i) for i in input()])

total = 0
steps = 100

print(str(0), "------------")
mostrarMatriz(entrada)

for s in range(steps):
    porExplotar = []
    explotadas = []
    for i in range(10):
        for j in range(10):
            entrada[i][j] += 1
            if entrada[i][j] > 9:
                porExplotar.append([i, j])
                explotadas.append(str(i) + ", " + str(j))
    while len(porExplotar) > 0:
        total += 1

        e = porExplotar.pop()
        entrada[e[0]][e[1]] = 0

        dX = [-1, -1, -1,  1,  1,  1,  0,  0]
        dY = [-1,  0,  1, -1,  0,  1, -1,  1]

        for i in range(len(dX)):
            xx = e[0] + dX[i]
            yy = e[1] + dY[i]
            if 0 <= xx < 10 and 0 <= yy < 10 and (str(xx) + ", " + str(yy)) not in explotadas:
                entrada[xx][yy] += 1
                if entrada[xx][yy] > 9:
                    porExplotar.append([xx, yy])
                    explotadas.append(str(xx) + ", " + str(yy))
    print(str(s), "------------")
    mostrarMatriz(entrada)
print(total)