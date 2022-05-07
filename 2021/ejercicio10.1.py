import math

listaEntrada = []
dic = {
    ">": "<",
    ")": "(",
    "}": "{",
    "]": "["
}
puntuacion = {
    "<": 4,
    "(": 1,
    "{": 3,
    "[": 2
}
while True:
    entrada = input()
    if entrada == "fin":
        break

    listaEntrada.append([i for i in entrada])


total = []
for entrada in listaEntrada:
    pila = []
    corrupto = False
    cMalo = ""
    for c in entrada:
        if c in ["<", "(", "{", "["]:
            pila.append(c)
        elif len(pila) == 0:
                cMalo = c
                break
        else:
            anterior = pila.pop()
            if anterior != dic[c]:
                cMalo = c
                break
    if cMalo == "" and len(pila) != 0:
        puntuacionActual = 0
        while len(pila) != 0:
            c = pila.pop()
            puntuacionActual *= 5
            puntuacionActual += puntuacion[c]
        total.append(puntuacionActual)

total.sort()
print(total[math.floor(len(total)/2)])