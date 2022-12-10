bosque = []

while True:
    entrada = input()
    if entrada == "-":
        break
    bosque.append(entrada)


matrizValor = [[1 for j in i]for i in bosque]

# Oeste -> Este
for i in range(len(bosque)):
    listaDistancias = [0 for n in range(10)]
    for j in range(len(bosque[0])):
        vActual = int(bosque[i][j])
        matrizValor[i][j] *= listaDistancias[vActual]
        for n in range(len(listaDistancias)):
            if n <= vActual:
                listaDistancias[n] = 1
            else:
                listaDistancias[n] += 1

# Este -> Oeste
for i in range(len(bosque)):
    listaDistancias = [0 for n in range(10)]
    for j in range(len(bosque[0])-1, 0, -1):
        vActual = int(bosque[i][j])
        matrizValor[i][j] *= listaDistancias[vActual]
        for n in range(len(listaDistancias)):
            if n <= vActual:
                listaDistancias[n] = 1
            else:
                listaDistancias[n] += 1

# Norte -> Sur
for i in range(len(bosque[0])):
    listaDistancias = [0 for n in range(10)]
    for j in range(len(bosque)):
        vActual = int(bosque[j][i])
        matrizValor[j][i] *= listaDistancias[vActual]
        for n in range(len(listaDistancias)):
            if n <= vActual:
                listaDistancias[n] = 1
            else:
                listaDistancias[n] += 1

# Sur -> Norte
for i in range(len(bosque[0])):
    listaDistancias = [0 for n in range(10)]
    for j in range(len(bosque[0])-1, 0, -1):
        vActual = int(bosque[j][i])
        matrizValor[j][i] *= listaDistancias[vActual]
        for n in range(len(listaDistancias)):
            if n <= vActual:
                listaDistancias[n] = 1
            else:
                listaDistancias[n] += 1
maximo = 0
for i in matrizValor:
    for j in i:
        if j > maximo:
            maximo = j

print(maximo)