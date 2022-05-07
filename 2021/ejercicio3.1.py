listaEmpiezanUno = []
listaEmpiezaCero = []
cantidadUno = 0
cantidadCero = 0
listaInicial = []
listaRestantes = []

while True:
    valorActual = input()

    if valorActual == "fin":
        break
    listaInicial.append(valorActual)

print("------")
listaRestantes = listaInicial

index = 0
while len(listaRestantes) != 1:
    for palabra in listaRestantes:

        if palabra[index] == "1":
            cantidadUno += 1
            listaEmpiezanUno.append(palabra)
        else:
            cantidadCero += 1
            listaEmpiezaCero.append(palabra)

    if cantidadUno >= cantidadCero:
        listaRestantes = listaEmpiezanUno
    else:
        listaRestantes = listaEmpiezaCero

    index += 1
    listaEmpiezanUno = []
    listaEmpiezaCero = []
    cantidadUno = 0
    cantidadCero = 0

print("ox", listaRestantes[0])

listaRestantes = listaInicial

index = 0
while len(listaRestantes) != 1:
    for palabra in listaRestantes:

        if palabra[index] == "1":
            cantidadUno += 1
            listaEmpiezanUno.append(palabra)
        else:
            cantidadCero += 1
            listaEmpiezaCero.append(palabra)

    if cantidadUno >= cantidadCero:
        listaRestantes = listaEmpiezaCero
    else:
        listaRestantes = listaEmpiezanUno

    index += 1
    listaEmpiezanUno = []
    listaEmpiezaCero = []
    cantidadUno = 0
    cantidadCero = 0

print("co2", listaRestantes[0])