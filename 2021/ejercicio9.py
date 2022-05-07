listaEntradas = []
while True:
    linea = input()
    if linea == "fin":
        break
    listaEntradas.append([int(i) for i in list(linea)])

peligro = 0
for i, linea in enumerate(listaEntradas):
    for j, numero in enumerate(linea):
        bajo = True
        if i != 0 and listaEntradas[i-1][j] <= numero:
            bajo = False
        elif i != len(listaEntradas)-1 and listaEntradas[i+1][j] <= numero:
            bajo = False
        elif j != 0 and listaEntradas[i][j-1] <= numero:
            bajo = False
        elif j != len(listaEntradas[0])-1 and listaEntradas[i][j+1] <= numero:
            bajo = False

        if bajo:
            peligro += numero + 1

print(peligro)