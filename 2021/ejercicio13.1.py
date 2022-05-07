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

for pliegue in pliegues:
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

matrizFinal = [["."]*100 for i in range(100)]
for k in puntosDiferentes.keys():
    p = [int(i) for i in k.split(" ")]
    matrizFinal[p[0]][p[1]] = "0"

for l in matrizFinal:
    print("".join(l))