def v(cDestino, cObjetivo):
    if cObjetivo == "E":
        vObjetivo = 25
    elif cObjetivo == "S":
        vObjetivo = 0
    else:
        vObjetivo = ord(cObjetivo) - ord("a")

    if cDestino == "E":
        vDestino = 25
    elif cDestino == "S":
        vDestino = 0
    else:
        vDestino = ord(cDestino) - ord("a")

    return vObjetivo <= vDestino+1


class Nodo:
    def __init__(self, posX, posY, puntuacion):
        self.X = posX
        self.Y = posY
        self.puntuacion = puntuacion

    def __lt__(self, other):
        return self.puntuacion < other.puntuacion


mapa = []
while True:
    entrada = input()
    if entrada == "-":
        break
    mapa.append(entrada)

posicionMapa = [[999 for _ in range(len(mapa[0]))] for _ in range(len(mapa))]
evaluadoMapa = [[False for _ in range(len(mapa[0]))] for _ in range(len(mapa))]
porVisitar = []

# Encontrar la S
S = [0, 0]
E = [0, 0]
for i, string in enumerate(mapa):
    for j, char in enumerate(string):
        if char == "S":
            S = [i, j]
        if char == "E":
            E = [i, j]

posicionMapa[S[0]][S[1]] = 0
evaluadoMapa[S[0]][S[1]] = True
porVisitar.append(Nodo(S[0], S[1], 0))

while len(porVisitar) > 0:
    nodoActual = porVisitar.pop(0)
    posicionMapa[nodoActual.X][nodoActual.Y] = nodoActual.puntuacion

    if nodoActual.X != 0 and not evaluadoMapa[nodoActual.X-1][nodoActual.Y] and v(mapa[nodoActual.X][nodoActual.Y], mapa[nodoActual.X-1][nodoActual.Y]):
        evaluadoMapa[nodoActual.X-1][nodoActual.Y] = True
        porVisitar.append(Nodo(nodoActual.X-1, nodoActual.Y, nodoActual.puntuacion+1))
    if nodoActual.X != len(mapa)-1 and not evaluadoMapa[nodoActual.X+1][nodoActual.Y]:
        if v(mapa[nodoActual.X][nodoActual.Y], mapa[nodoActual.X+1][nodoActual.Y]):
            evaluadoMapa[nodoActual.X+1][nodoActual.Y] = True
            porVisitar.append(Nodo(nodoActual.X+1, nodoActual.Y, nodoActual.puntuacion+1))
    if nodoActual.Y != 0 and not evaluadoMapa[nodoActual.X][nodoActual.Y-1] and v(mapa[nodoActual.X][nodoActual.Y], mapa[nodoActual.X][nodoActual.Y-1]):
        evaluadoMapa[nodoActual.X][nodoActual.Y-1] = True
        porVisitar.append(Nodo(nodoActual.X, nodoActual.Y-1, nodoActual.puntuacion+1))
    if nodoActual.Y != len(mapa[0])-1 and not evaluadoMapa[nodoActual.X][nodoActual.Y+1] and v(mapa[nodoActual.X][nodoActual.Y], mapa[nodoActual.X][nodoActual.Y+1]):
        evaluadoMapa[nodoActual.X][nodoActual.Y+1] = True
        porVisitar.append(Nodo(nodoActual.X, nodoActual.Y+1, nodoActual.puntuacion+1))
    porVisitar.sort()


for i in posicionMapa:
    acumulado = ""
    for j in i:
       acumulado += str(j)+ "\t"
    print(acumulado)

print(posicionMapa[E[0]][E[1]])