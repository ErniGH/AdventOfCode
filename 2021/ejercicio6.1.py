import math

listaEntradas = [int(i) for i in input().split(",")]
tiempoTotal = 256
tiempoParaHijo = 7
contador = 0

tablasCalculadas = []

tabla = [1]*(tiempoTotal+1)

sumadorPresente = [0, 0, 0, 0, 0, 0, 0]
sumadorFuturo = [0, 1, 0, 0, 0, 0, 0]
sumadorFuturoFuturo = [0, 0, 0, 0, 0, 0, 0]

puntero = 0

while puntero < len(tabla):
    sumadorPresente = sumadorFuturo.copy()
    sumadorFuturo = [sum(x) for x in zip(sumadorFuturo, sumadorFuturoFuturo)]
    sumadorFuturoFuturo = [0, 0, 0, 0, 0, 0, 0]
    for i in range(7):
        if puntero == len(tabla):
            break
        tabla[puntero] = tabla[puntero-1] + sumadorPresente[i]
        if i+2 >= 7:
            sumadorFuturoFuturo[(i+2)%7] += sumadorPresente[i]
        else:
            sumadorFuturo[(i+2)%7] += sumadorPresente[i]
        puntero += 1
for i in range(6):
    tablasCalculadas.append(tabla[-i-1])

print(tablasCalculadas)
total = 0
for numero in listaEntradas:
    total += tablasCalculadas[numero]

print(total)