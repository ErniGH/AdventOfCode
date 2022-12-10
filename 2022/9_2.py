
h = [0, 0]
t = [0, 0]

mh = {
    "D": [-1, 0],
    "U": [1, 0],
    "R": [0, 1],
    "L": [0, -1]
}

mt = {
    "00": [0, 0],

    "10": [0, 0],
    "-10": [0, 0],
    "01": [0, 0],
    "0-1": [0, 0],

    "1-1": [0, 0],
    "-11": [0, 0],
    "11": [0, 0],
    "-1-1": [0, 0],

    "20": [1, 0],
    "-20": [-1, 0],
    "02": [0, 1],
    "0-2": [0, -1],

    "12": [1, 1],
    "1-2": [1, -1],
    "-12": [-1, 1],
    "-1-2": [-1, -1],
    "21": [1, 1],
    "2-1": [1, -1],
    "-21": [-1, 1],
    "-2-1": [-1, -1],

    "22": [1, 1],
    "-22": [-1, 1],
    "2-2": [1, -1],
    "-2-2": [-1, -1],

}

visitados = {}
cuerda = [[0, 0] for _ in range(10)]

while True:
    entrada = input()
    if entrada == "-":
        break

    e_split = entrada.split(" ")
    comando, numero = e_split[0], int(e_split[1])
    for i in range(numero):
        cuerda[0][0] += mh[comando][0]
        cuerda[0][1] += mh[comando][1]

        for j in range(1, 10):
            diferencia = str(cuerda[j-1][0] - cuerda[j][0]) + str(cuerda[j-1][1] - cuerda[j][1])
            cuerda[j][0] += mt[diferencia][0]
            cuerda[j][1] += mt[diferencia][1]

        visitados[str(cuerda[9][0]) + "/" + str(cuerda[9][1])] = True

print(len(visitados.keys()))

