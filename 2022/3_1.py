import math


def v(c):
    if ord(c) > 96:
        return ord(c) - 96
    else:
        return ord(c) - 38


valor = 0
while True:
    entrada = input()
    if entrada == "-":
        break

    mitad = math.floor(len(entrada)/2)
    subString1 = entrada[:mitad]
    subString2 = entrada[mitad:]

    for c in subString1:
        if c in subString2:
            valor += v(c)
            break

print(valor)
