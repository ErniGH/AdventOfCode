import math

entrada = ""
while True:
    e = input()
    if e == "fin":
        break

    if entrada != "":
        entrada = "[" + entrada + "," + e + "]"
    else:
        entrada = e


def analisis(index):
    salida = ""
    j = index
    while True:
        c = entrada[j]
        salida += c
        if c in ["[", "]", ","]:
            break
        else:
            j += 1
    return j+1, salida


while True:
    cambios = False
    contadorCorchetes = 0
    i = 0
    explotar = False
    while i < len(entrada):
        t = 0
        i, c = analisis(i)
        if c == "[":
            contadorCorchetes += 1
        elif c == "]":
            contadorCorchetes -= 1
        elif c != ",":
            n1 = int(c)
            i, c2 = analisis(i)
            n2 = int(c2)
            if n1 > 9:
                cambio = "[" + str(math.floor(n1/2)) + "," + str(math.ceil(n1/2)) + "]"
                entrada.replace(c, cambio, 1)
                cambio = True
            elif n2 > 9:
                cambio = "[" + str(math.floor(n2 / 2)) + "," + str(math.ceil(n2 / 2)) + "]"
                entrada.replace(c2, cambio, 1)
                cambio = True
            elif explotar:



        if contadorCorchetes > 4:
            explotar = True



    if not cambios:
        break
