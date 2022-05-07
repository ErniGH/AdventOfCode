tabla = [[0]* 1000 for i in range(1000)]

while True:
    entrada = input()
    if entrada == "fin":
        break

    cInicial, cFin = entrada.split(" -> ")
    coordenadasInicial = [int(x) for x in cInicial.split(",")]
    coordenadasFinal = [int(x) for x in cFin.split(",")]

    if coordenadasInicial[0] == coordenadasFinal[0]:
        if coordenadasInicial[1] > coordenadasFinal[1]:
            for i in range(coordenadasFinal[1], coordenadasInicial[1]+1):
                tabla[coordenadasInicial[0]][i] += 1
        else:
            for i in range(coordenadasInicial[1], coordenadasFinal[1]+1):
                tabla[coordenadasInicial[0]][i] += 1

    if coordenadasInicial[1] == coordenadasFinal[1]:
        if coordenadasInicial[0] > coordenadasFinal[0]:
            for i in range(coordenadasFinal[0], coordenadasInicial[0]+1):
                tabla[i][coordenadasInicial[1]] += 1
        else:
            for i in range(coordenadasInicial[0], coordenadasFinal[0]+1):
                tabla[i][coordenadasInicial[1]] += 1

    diferenciaCoordenadas = [coordenadasInicial[0] - coordenadasFinal[0], coordenadasInicial[1] - coordenadasFinal[1]]

    if abs(diferenciaCoordenadas[0]) == abs(diferenciaCoordenadas[1]):
        tabla[coordenadasFinal[0]][coordenadasFinal[1]] += 1
        inicio = coordenadasInicial
        final = coordenadasFinal
        paso = 0, 0
        if diferenciaCoordenadas[0] < 0 and diferenciaCoordenadas[1] < 0:
            paso = 1, 1
        elif diferenciaCoordenadas[0] < 0 and diferenciaCoordenadas[1] > 0:
            paso = 1, -1
        elif diferenciaCoordenadas[0] > 0 and diferenciaCoordenadas[1] > 0:
            paso = -1, -1
        elif diferenciaCoordenadas[0] > 0 and diferenciaCoordenadas[1] < 0:
            paso = -1, 1

        while inicio[0] != final[0]:
            tabla[inicio[0]][inicio[1]] += 1
            inicio[0] += paso[0]
            inicio[1] += paso[1]


contador = 0
for fila in tabla:
    for numero in fila:
        if numero >= 2:
            contador += 1

print(contador)