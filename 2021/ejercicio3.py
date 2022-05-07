listaUno = [0] * 12
listaCero = [0] *12

while True:
    valorActual = input()

    if valorActual == "fin":
        break

    for i, letra in enumerate(valorActual):
        if letra == "1":
            listaUno[i] += 1
        else:
            listaCero[i] += 1

listaGamma = [0] *12

for i in range(12):
    if listaUno[i] > listaCero[i]:
        listaGamma[i] = 1

print(listaUno)
print(listaCero)
print(listaGamma)