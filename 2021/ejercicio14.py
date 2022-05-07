base = input()
input()

dicCrecer = {}
while True:
    entrada = input()
    if entrada == "fin":
        break
    e = entrada.split(" -> ")
    dicCrecer[e[0]] = e[1]

steps = 40
letraInicio, letraFin = base[0], base[len(base) -1]
dicParejas = {}
for i in range(len(base)):
    if i != 0:
        k = base[i-1] + base[i]
        if k in dicParejas.keys(): dicParejas[k] += 1
        else: dicParejas[k] = 1

for i in range(steps):
    dicParejasF = dicParejas.copy()
    for k in dicParejas.keys():
        if k in dicCrecer.keys():
            cantidadParejas = dicParejas[k]
            dicParejasF[k] -= cantidadParejas
            kk1 = k[0] + dicCrecer[k]
            kk2 = dicCrecer[k] + k[1]
            if kk1 in dicParejasF.keys():
                dicParejasF[kk1] += cantidadParejas
            else:
                dicParejasF[kk1] = cantidadParejas

            if kk2 in dicParejasF.keys():
                dicParejasF[kk2] += cantidadParejas
            else:
                dicParejasF[kk2] = cantidadParejas
    dicParejas = dicParejasF


dicCantidadTotal = {}
for k in dicParejas.keys():
    if k[0] in dicCantidadTotal.keys():
        dicCantidadTotal[k[0]] += dicParejas[k]
    else:
        dicCantidadTotal[k[0]] = dicParejas[k]

    if k[1] in dicCantidadTotal.keys():
        dicCantidadTotal[k[1]] += dicParejas[k]
    else:
        dicCantidadTotal[k[1]] = dicParejas[k]

dicCantidadTotal[letraInicio] += 1
dicCantidadTotal[letraFin] += 1


print(dicCantidadTotal)
print((max(dicCantidadTotal.values()) - min(dicCantidadTotal.values())) / 2)