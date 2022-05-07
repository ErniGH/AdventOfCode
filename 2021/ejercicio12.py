caminos = {
    "start": []
}

while True:
    entrada = input()
    if entrada == "fin":
        break

    entrada = entrada.split("-")
    if entrada[0] == "start":
        caminos["start"].append(entrada[1])
    elif entrada[1] == "start":
        caminos["start"].append(entrada[0])
    elif entrada[0] == "end":
        if entrada[1] not in caminos.keys():
            caminos[entrada[1]] = []
        caminos[entrada[1]].append("end")
    elif entrada[1] == "end":
        if entrada[0] not in caminos.keys():
            caminos[entrada[0]] = []
        caminos[entrada[0]].append("end")
    else:
        if entrada[0] not in caminos.keys():
            caminos[entrada[0]] = []
        if entrada[1] not in caminos.keys():
            caminos[entrada[1]] = []
        caminos[entrada[0]].append(entrada[1])
        caminos[entrada[1]].append(entrada[0])


def recorrerLaberinto(actual, lista_visitados, caminos):
    total = 0
    if actual == "end":
        total += 1
    else:
        for c in caminos[actual]:
            if c not in lista_visitados:
                visitadosNueva = lista_visitados.copy()
                if c.islower():
                    visitadosNueva.append(c)
                total += recorrerLaberinto(c, visitadosNueva, caminos)
    return total


lista_visitados = []
total = recorrerLaberinto("start", lista_visitados, caminos)

print(total)