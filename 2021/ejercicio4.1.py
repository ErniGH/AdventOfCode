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
print()

for aleatorio in listaAleatorios:
    index = 0
    while index < len(listaTablas):
        for i in range(5):
            for j in range(5):
                if listaTablas[index][i][j] == int(aleatorio):
                    listaTablas[index][i][j] = -1
                    if listaTablas[index][0][j] + listaTablas[index][1][j] + listaTablas[index][2][j] + listaTablas[index][3][j] + listaTablas[index][4][j] == -5 or listaTablas[index][i][0] + listaTablas[index][i][1] + listaTablas[index][i][2] + listaTablas[index][i][3] + listaTablas[index][i][4] == -5:
                        print(aleatorio)
                        print(listaTablas[index])
                        listaTablas.pop(index)
                        index -= 1

        index += 1