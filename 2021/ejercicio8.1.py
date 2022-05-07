total = 0
entrada= []
binToReal = {
    1110111: 0,
    100100: 1,
    1011101: 2,
    1101101: 3,
    101110: 4,
    1101011: 5,
    1111011: 6,
    100101: 7,
    1111111: 8,
    1101111: 9
}
while True:
    nuevo = input()
    if nuevo == "fin":
        break
    entrada.append(nuevo)

salida = 0

for linea in entrada:
    parte1, parte2 = linea.split("|")

    diccionario = {}

    uno = ""
    cuatro = ""
    siete = ""
    segmentos6 = []
    ocho = ""
    for palabra in parte1.split(" "):
        if len(palabra) == 2:
            uno = palabra
        elif len(palabra) == 3:
            siete = palabra
        elif len(palabra) == 4:
            cuatro = palabra
        elif len(palabra) == 6:
            segmentos6.append(palabra)
        elif len(palabra) == 7:
            ocho = palabra
    letrasResueltas = ""

    # primer segmento
    for letra in siete:
        if letra not in uno:
            diccionario[letra] = 1
            letrasResueltas += letra

    # tercer y sexto segmentos
    for i, letra in enumerate(uno):
        for palabra in segmentos6:
            if letra not in palabra:
                diccionario[letra] = 100
                letrasResueltas += letra
                diccionario[uno[i-1]] = 100000
                letrasResueltas += uno[i-1]

    # segundo y cuarto segmentos
    letrasBuscar = ''.join([i for i in cuatro if i not in uno])
    for i, letra in enumerate(letrasBuscar):
        for palabra in segmentos6:
            if letra not in palabra:
                diccionario[letra] = 1000
                letrasResueltas += letra
                diccionario[letrasBuscar[i-1]] = 10
                letrasResueltas += letrasBuscar[i-1]

    # quito y sectimo segmentos
    letrasBuscar = ''.join([i for i in ocho if i not in letrasResueltas])
    for i, letra in enumerate(letrasBuscar):
        for palabra in segmentos6:
            if letra not in palabra:
                diccionario[letra] = 10000
                diccionario[letrasBuscar[i-1]] = 1000000
    resultado = 0
    for i, palabra in enumerate(parte2.split(" ")):
        if palabra != "":
            numero = 0
            for letra in palabra:
                numero += diccionario[letra]
            numeroReal = binToReal[numero]
            resultado += (1000 / 10**(i-1)) * numeroReal

    salida += resultado
print(salida)