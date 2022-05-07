listaAleatorios = input().split(",")
listaTablas = []

while True:
    primeraEntrada = input()
    if primeraEntrada == "fin":
        break

    tablaActual = [[0]* 5 for i in range(5)]
    for i in range(5):
        filaActual = input().split(" ")
        j = 0
        for numero in filaActual:
            if numero != "":
                tablaActual[i][j] = int(numero)
                j += 1

    listaTablas.append(tablaActual)

for aleatorio in listaAleatorios:
    for tablaActual in listaTablas:
        for i in range(5):
            for j in range(5):
                if tablaActual[i][j] == int(aleatorio):
                    tablaActual[i][j] = -1
                    if tablaActual[0][j] + tablaActual[1][j] + tablaActual[2][j] + tablaActual[3][j] + tablaActual[4][j] == -5 or tablaActual[i][0] + tablaActual[i][1] + tablaActual[i][2] + tablaActual[i][3] + tablaActual[i][4] == -5:
                        print(aleatorio)
                        print(tablaActual)

