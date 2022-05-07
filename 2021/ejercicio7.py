listaEntradas = [int(i) for i in input().split(",")]

listaConsumo = [0] * 2000

for i in range(len(listaConsumo)):
    for entrada in listaEntradas:
        listaConsumo[i] += abs(entrada - i)

minimo = min(listaConsumo)
print(minimo, listaConsumo.index(minimo))