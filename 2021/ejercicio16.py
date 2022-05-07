


NO FUNCIONA :v









d = {
    "0": 0,
    "1": 1,
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
    "A": 10,
    "B": 11,
    "C": 12,
    "D": 13,
    "E": 14,
    "F": 15,
}

cola = []
for c in input():
    binC = bin(d[c]).split("b")[1]
    while len(binC) < 4:
        binC = "0" + binC
    for i in binC:
        cola.append(i)

sumaV = [0]


def extraerInt(n, fin, index):
    v, m = extraerBin(n, fin, index)
    return int("0b" + v, 2), m


def extraerBin(n, fin, index):
    v = ""
    movimiento = 0
    for i in range(n):
        s = i + index
        if s < fin:
            v += cola[s]
            movimiento += 1
        else:
            v += "0"
    return v, movimiento


def analizarCadena(inicio, fin):
    p = inicio

    v, m = extraerInt(3, fin, p)
    p += m

    t, m = extraerInt(3, fin, p)
    p += m

    sumaV[0] += v

    if t == 4:
        print("numero")
        s = 1
        valorBin = ""
        while s == 1:
            s, m = extraerInt(1, fin, p)
            p += m

            vB, m = extraerBin(4, fin, p)
            valorBin += vB
            p += m

        print("v", int("0b" + valorBin, 2))
    else:
        print("operador")
        ib, m = extraerInt(1, fin, p)
        p += m

        if ib == 0:
            print("tipo 0")
            l, m = extraerInt(15, fin, p)
            p += m
            usado = 0
            ff = p + l
            while l > usado:
                cantidad = analizarCadena(p, ff)
                usado += cantidad
                p += cantidad

        else:
            print("tipo 1")
            l, m = extraerInt(11, fin, p)
            p += m
            for i in range(l):
                analizarCadena(p, p+11)
                p += 11

    return p - inicio


analizarCadena(0, len(cola))
print("...")
print(sumaV[0])