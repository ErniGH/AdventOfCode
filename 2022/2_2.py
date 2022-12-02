total = 0

tabla = {
    "AR": 3,
    "AP": 6,
    "AS": 0,
    "BR": 0,
    "BP": 3,
    "BS": 6,
    "CR": 6,
    "CP": 0,
    "CS": 3
}

estrategia = {
    "AX": "S",
    "AY": "R",
    "AZ": "P",
    "BX": "R",
    "BY": "P",
    "BZ": "S",
    "CX": "P",
    "CY": "S",
    "CZ": "R"
}

puntuacionXYZ = {
    "R": 1,
    "P": 2,
    "S": 3
}

while True:
    entrada = input()
    if entrada == "-":
        break
    miGesto = estrategia[entrada[0]+entrada[2]]
    total += tabla[entrada[0]+miGesto]
    total += puntuacionXYZ[miGesto]

print(total)
