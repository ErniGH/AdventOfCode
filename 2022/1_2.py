listaElfos = []
acumuladoActual = 0
while True:
    valorActual = input()
    if valorActual == "-":
        break

    if valorActual == "":
        listaElfos.append(acumuladoActual)
        acumuladoActual = 0
    else:
        acumuladoActual += int(valorActual)

listaElfos.sort(reverse=True)
numeroElfos = 3
totalCalorias = 0

for i in range(numeroElfos):
    totalCalorias += listaElfos[i]

print(totalCalorias)
