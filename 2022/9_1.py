
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

}

visitados = {}

while True:
    entrada = input()
    if entrada == "-":
        break

    e_split = entrada.split(" ")
    comando, numero = e_split[0], int(e_split[1])
    for i in range(numero):
        h[0] += mh[comando][0]
        h[1] += mh[comando][1]

        diferencia = str(h[0] - t[0]) + str(h[1] - t[1])
        t[0] += mt[diferencia][0]
        t[1] += mt[diferencia][1]

        visitados[str(t[0]) + "/" + str(t[1])] = True

print(len(visitados.keys()))

