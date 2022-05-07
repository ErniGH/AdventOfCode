listaEntrada = []
dic = {
    ">" : "<",
    ")" : "(",
    "}" : "{",
    "]" : "["
}
puntuacion = {
    ">": 25137,
    ")": 3,
    "}": 1197,
    "]": 57
}
while True:
    entrada = input()
    if entrada == "fin":
        break

    listaEntrada.append([i for i in entrada])


total = 0
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
    if cMalo != "":
        total += puntuacion[cMalo]

print(total)