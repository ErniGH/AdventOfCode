class Mono:
    def __init__(self, objetos, operacion, divisible, objetivos):
        self.objetos = objetos
        self.operacion = operacion
        self.divisible = divisible
        self.objetivos = objetivos
        self.total = 0

    def inspecionar(self):
        listaFinal = []
        while len(self.objetos) != 0:
            actual = self.objetos.pop(0)
            actual = self.operacion(actual)
            actual %= 9699690
            siguienteMono = self.objetivos[0] if actual % self.divisible == 0 else self.objetivos[1]
            listaFinal.append([siguienteMono, actual])
            self.total += 1
        return listaFinal


listaMonos = [
    Mono(
        [99, 67, 92, 61, 83, 64, 98],
        lambda old: old * 17,
        3,
        [4, 2]
    ),
    Mono(
        [78, 74, 88, 89, 50],
        lambda old: old * 11,
        5,
        [3, 5]
    ),
    Mono(
        [98, 91],
        lambda old: old + 4,
        2,
        [6, 4]
    ),
    Mono(
        [59, 72, 94, 91, 79, 88, 94, 51],
        lambda old: old * old,
        13,
        [0, 5]
    ),
    Mono(
        [95, 72, 78],
        lambda old: old + 7,
        11,
        [7, 6]
    ),
    Mono(
        [76],
        lambda old: old + 8,
        17,
        [0, 2]
    ),
    Mono(
        [69, 60, 53, 89, 71, 88],
        lambda old: old + 5,
        19,
        [7, 1]
    ),
    Mono(
        [72, 54, 63, 80],
        lambda old: old + 3,
        7,
        [1, 3]
    )
]

rondas = 10000

for i in range(rondas):
    for mono in listaMonos:
        listaMovimientos = mono.inspecionar()
        for movimiento in listaMovimientos:
            listaMonos[movimiento[0]].objetos.append(movimiento[1])


l = [m.total for m in listaMonos]
max1 = max(l)
l.remove(max1)
max2 = max(l)
print(max1 * max2)

