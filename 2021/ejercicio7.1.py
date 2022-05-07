import math

listaEntradas = [int(i) for i in input().split(",")]

listaConsumo = [0] * 2000

tablaValores = [0]
for i in range(1, 2000):
    tablaValores.append(tablaValores[i-1] + i)

print(tablaValores)

for i in range(len(listaConsumo)):
    for entrada in listaEntradas:
        listaConsumo[i] += tablaValores[abs(entrada - i)]

minimo = min(listaConsumo)
print(minimo, listaConsumo.index(minimo))