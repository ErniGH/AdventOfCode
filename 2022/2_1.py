total = 0

tabla = {
    "AX": 3,
    "AY": 6,
    "AZ": 0,
    "BX": 0,
    "BY": 3,
    "BZ": 6,
    "CX": 6,
    "CY": 0,
    "CZ": 3
}

puntuacionXYZ = {
    "X": 1,
    "Y": 2,
    "Z": 3
}

while True:
    entrada = input()
    if entrada == "-":
        break

    total += tabla[entrada[0]+entrada[2]]
    total += puntuacionXYZ[entrada[2]]

print(total)
