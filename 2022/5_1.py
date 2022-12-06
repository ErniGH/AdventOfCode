pilas = [
    ["B", "V", "S", "N", "T", "C", "H", "Q"],
    ["W", "D", "B", "G"],
    ["F", "W", "R", "T", "S", "Q", "B"],
    ["L", "G", "W", "S", "Z", "J", "D", "N"],
    ["M", "P", "D", "V", "F"],
    ["F", "W", "J"],
    ["L", "N", "Q", "B", "J", "V"],
    ["G", "T", "R", "C", "J", "Q", "S", "N"],
    ["J", "S", "Q", "C", "W", "D", "M"]
]

while True:
    entrada = input()
    if entrada == "-":
        break

    division = entrada.split(" ")
    numeroMovimientos = int(division[1])
    inicio = int(division[3]) - 1 # ajuste para la lista de pilas
    final = int(division[5]) - 1

    for i in range(numeroMovimientos):
        pilas[final].append(pilas[inicio].pop(-1))

salida = "".join([i[-1] for i in pilas])
print(salida)