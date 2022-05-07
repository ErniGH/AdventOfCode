listaEntradas = []

def expandirBasin(i, j):
    total = 1
    numeroActual = listaEntradas[i][j]
    listaEntradas[i][j] = 9
    if i != 0 and listaEntradas[i-1][j] != 9:
        total += expandirBasin(i-1, j)
    if i != len(listaEntradas)-1 and listaEntradas[i+1][j] != 9:
        total += expandirBasin(i+1, j)
    if j != 0 and listaEntradas[i][j-1] != 9:
        total += expandirBasin(i, j-1)
    if j != len(listaEntradas[0])-1 and listaEntradas[i][j+1] != 9:
        total += expandirBasin(i, j+1)
    return total

while True:
    linea = input()
    if linea == "fin":
        break
    listaEntradas.append([int(i) for i in list(linea)])

listaBajo = []
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
            listaBajo.append([i,j])
total = []
for bajo in listaBajo:
    total.append(expandirBasin(bajo[0], bajo[1]))

print(total)
mayor1 = max(total)
total.pop(total.index(mayor1))
mayor2 = max(total)
total.pop(total.index(mayor2))
mayor3 = max(total)
total.pop(total.index(mayor3))

print(mayor1, mayor2, mayor3)
print(mayor1 * mayor2 * mayor3)