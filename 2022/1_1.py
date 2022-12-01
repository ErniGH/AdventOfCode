mayor = 0
acumuladoActual = 0
while True:
    valorActual = input()
    if valorActual == "-":
        break

    if valorActual == "":
        mayor = max(mayor, acumuladoActual)
        acumuladoActual = 0
    else:
        acumuladoActual += int(valorActual)

print(mayor)

