grupoAnterior = 10000
grupoActual = 0
grupoSiguiente = 0
grupoFuturo = 0
numeroActual = 0
total = 0

while True:
    valorActual = int(input())
    if numeroActual == 0:
        numeroActual += 1
        grupoActual += valorActual
    elif numeroActual == 1:
        numeroActual += 1
        grupoActual += valorActual
        grupoSiguiente += valorActual
    elif numeroActual == 2:
        grupoActual += valorActual
        grupoSiguiente += valorActual
        grupoFuturo += valorActual

        if grupoActual > grupoAnterior:
            total += 1

        grupoAnterior = grupoActual
        grupoActual = grupoSiguiente
        grupoSiguiente = grupoFuturo
        grupoFuturo = 0

    print(total)