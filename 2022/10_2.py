registroTemporal = []
registroActual = 1
maximoPantalla = 240
while True:
    entrada = input()
    if entrada == "-" or len(registroTemporal) > maximoPantalla:
        break

    registroTemporal.append(registroActual)
    if entrada.split(" ")[0] == "addx":
        registroTemporal.append(registroActual)
        registroActual += int(entrada.split(" ")[1])

pantalla = [6, 40]
for i in range(pantalla[0]):
    acumulado = ""
    for j in range(pantalla[1]):
        valorActual = registroTemporal[40*i + j]
        acumulado += "#" if j in [valorActual, valorActual-1, valorActual+1] else "."
    print(acumulado)

