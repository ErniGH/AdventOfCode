listaPuntos = []
while True:
    entrada = input()
    if entrada == "":
        break
    listaPuntos.append([int(i) for i in entrada.split(",")])

pliegues = []
while True:
    entrada = input()
    if entrada == "fin":
        break
    e = entrada.split(" ")
    r = e[2].split("=")
    pliegues.append([r[0], int(r[1])])
print(listaPuntos)
pliegue = pliegues[0]
for punto in listaPuntos:
    if pliegue[0] == "x":
        if punto[0] > pliegue[1]:
            distancia = punto[0] - pliegue[1]
            punto[0] = pliegue[1] - distancia
    else:
        if punto[1] > pliegue[1]:
            distancia = punto[1] - pliegue[1]
            punto[1] = pliegue[1] - distancia

puntosDiferentes = {}
for punto in listaPuntos:
    puntosDiferentes[str(punto[0]) + " " + str(punto[1])] = 1

print(puntosDiferentes.keys())
print(len(puntosDiferentes.keys()))